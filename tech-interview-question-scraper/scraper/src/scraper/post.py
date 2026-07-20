from __future__ import annotations

from dataclasses import dataclass, field
import html
import os
from pathlib import Path
import random
import re
import time
from typing import Iterable
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from .constants import REQUEST_COOKIE

DEFAULT_MIN_REQUEST_INTERVAL = 10.0
DEFAULT_REQUEST_INTERVAL_JITTER = 2.0
DEFAULT_MAX_TOTAL_REQUESTS = 60
DEFAULT_COOKIE_DOMAIN = ".1point3acres.com"
DEBUG_HTML_DIR = Path(".tmp/raw_html")
ATTACHMENT_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",
    ".csv",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
}


@dataclass(slots=True)
class DownloadableAsset:
    url: str
    kind: str


@dataclass(slots=True)
class ScrapedPost:
    url: str
    title: str
    author: str | None
    published_at: str | None
    content: str
    images: list[DownloadableAsset] = field(default_factory=list)
    attachments: list[DownloadableAsset] = field(default_factory=list)


class RequestLimitExceededError(RuntimeError):
    """Raised when a scrape session exceeds the configured live-request cap."""


def build_authenticated_session(
    *,
    cookie_header: str | None = None,
    cookie_domain: str | None = None,
    env_file: str | None = None,
) -> requests.Session:
    """Build a requests session from local configuration."""
    env_path = env_file or (".env" if Path(".env").exists() else None)
    env_values = load_env_file(env_path) if env_path else {}
    cookie_header = (
        cookie_header
        or os.getenv("SCRAPER_COOKIE_HEADER")
        or env_values.get("SCRAPER_COOKIE_HEADER")
        or REQUEST_COOKIE
    )
    cookie_domain = (
        cookie_domain
        or os.getenv("SCRAPER_COOKIE_DOMAIN")
        or env_values.get("SCRAPER_COOKIE_DOMAIN")
        or DEFAULT_COOKIE_DOMAIN
    )

    if not cookie_header:
        raise ValueError(
            "Missing cookies. Set SCRAPER_COOKIE_HEADER in .env or pass cookie_header explicitly."
        )

    session = requests.Session()
    apply_cookie_header(session, cookie_header, domain=cookie_domain)
    session.headers["User-Agent"] = "scraper/1.0 (+polite rate-limited requests)"
    setattr(
        session,
        "_scraper_min_request_interval",
        _load_min_request_interval(env_values),
    )
    setattr(
        session,
        "_scraper_request_interval_jitter",
        _load_request_interval_jitter(env_values),
    )
    setattr(
        session,
        "_scraper_max_total_requests",
        _load_max_total_requests(env_values),
    )
    setattr(session, "_scraper_total_requests_made", 0)
    setattr(session, "_scraper_retry_on_429", True)
    setattr(session, "_scraper_last_request_time", None)
    return session


def scrape_post(
    url: str,
    session: requests.Session,
    *,
    timeout: float = 30.0,
) -> ScrapedPost:
    """Fetch a post page with an authenticated session and parse its contents."""
    response = _rate_limited_get(session, url, timeout=timeout)
    response.raise_for_status()
    _save_debug_html(response.text, url=url, label="initial")
    try:
        return parse_post_html(response.text, url=url)
    except ValueError as exc:
        legacy_url = _extract_legacy_thread_url(response.text, url=url)
        if legacy_url is None or legacy_url == url:
            raise exc

        legacy_response = _rate_limited_get(session, legacy_url, timeout=timeout)
        legacy_response.raise_for_status()
        _save_debug_html(legacy_response.text, url=legacy_url, label="legacy")
        return parse_post_html(legacy_response.text, url=legacy_url)


def apply_cookie_header(
    session: requests.Session,
    cookie_header: str,
    *,
    domain: str,
) -> None:
    """Populate a session with cookies from a browser-style Cookie header."""
    for chunk in cookie_header.split(";"):
        if "=" not in chunk:
            continue
        name, value = chunk.split("=", 1)
        name = name.strip()
        value = value.strip()
        if name:
            session.cookies.set(name, value, domain=domain)


def parse_post_html(html: str, *, url: str) -> ScrapedPost:
    """Parse post data from 1Point3Acres HTML."""
    soup = BeautifulSoup(html, "html.parser")

    title = _extract_title(soup)
    content, author, published_at, images, attachments = _parse_html_post_content(soup, url=url)

    return ScrapedPost(
        url=url,
        title=title,
        author=author,
        published_at=published_at,
        content=content,
        images=images,
        attachments=attachments,
    )

def _extract_title(soup: BeautifulSoup) -> str:
    title = _extract_text(
        soup,
        [
            "h1",
            ".ts h1",
            ".article-title",
            '[data-testid="post-title"]',
            "title",
        ],
    )
    if not title:
        raise ValueError("Could not find post title in the provided HTML.")
    return title


def _extract_legacy_thread_url(html: str, *, url: str) -> str | None:
    current_post_id = _extract_post_id_from_url(url)
    if current_post_id is None:
        return None

    matches = re.findall(r"/bbs/thread-(\d+)-1-1\.html", html)
    for matched_post_id in matches:
        if matched_post_id == current_post_id:
            return f"https://www.1point3acres.com/bbs/thread-{matched_post_id}-1-1.html"
    return None


def _extract_post_id_from_url(url: str) -> str | None:
    path = urlparse(url).path.rstrip("/")
    for pattern in (
        r"/home/pins/(\d+)",
        r"/bbs/thread-(\d+)-1-1\.html",
        r"/interview/post/(\d+)",
    ):
        match = re.fullmatch(pattern, path)
        if match is not None:
            return match.group(1)
    return None


def _save_debug_html(html_text: str, *, url: str, label: str) -> Path:
    post_id = _extract_post_id_from_url(url) or "unknown"
    DEBUG_HTML_DIR.mkdir(parents=True, exist_ok=True)
    output_path = DEBUG_HTML_DIR / f"{post_id}_{label}.html"
    output_path.write_text(html_text, encoding="utf-8")
    return output_path


def _extract_text(
    soup: BeautifulSoup,
    selectors: Iterable[str],
    *,
    prefer_attr: str | None = None,
) -> str | None:
    tag = _first_tag(soup, selectors)
    if tag is None:
        return None

    if prefer_attr:
        attr_value = tag.get(prefer_attr)
        if isinstance(attr_value, str) and attr_value.strip():
            return _normalize_text(attr_value)

    return _normalize_text(tag.get_text(" ", strip=True))


def _first_tag(soup: BeautifulSoup, selectors: Iterable[str]) -> Tag | None:
    for selector in selectors:
        tag = soup.select_one(selector)
        if isinstance(tag, Tag):
            return tag
    return None


def _normalize_text(text: str) -> str:
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def _optional_normalized_text(value: object) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    return _normalize_text(value)


def _coerce_timestamp(value: object) -> str | None:
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _parse_html_post_content(
    soup: BeautifulSoup,
    *,
    url: str,
) -> tuple[str, str | None, str | None, list[DownloadableAsset], list[DownloadableAsset]]:
    entry_roots = _collect_entry_roots(soup)
    if not entry_roots:
        raise ValueError("Could not find post content in the provided HTML.")

    main_root = entry_roots[0]
    author = _extract_author_from_entry(main_root) or _extract_page_author(soup)
    published_at = _extract_published_at_from_entry(main_root) or _extract_page_published_at(soup)
    main_content = _normalize_text(main_root.get_text("\n", strip=True))
    images = _collect_images_from_tag(main_root, url)
    attachments = _collect_attachments_from_tag(main_root, url)

    if len(entry_roots) == 1:
        return main_content, author, published_at, images, attachments

    sections = [main_content, "Replies:"]
    seen_assets = {asset.url for asset in images + attachments}
    for position, reply_root in enumerate(entry_roots[1:], start=2):
        reply_content = _normalize_text(reply_root.get_text("\n", strip=True))
        if not reply_content:
            continue
        reply_author = _extract_author_from_entry(reply_root) or "Unknown"
        reply_published_at = _extract_published_at_from_entry(reply_root)
        header_parts = [f"#{position}", reply_author]
        if reply_published_at:
            header_parts.append(f"at {reply_published_at}")
        sections.append(" ".join(header_parts))
        sections.append(reply_content)

        for asset in _collect_images_from_tag(reply_root, url):
            if asset.url not in seen_assets:
                images.append(asset)
                seen_assets.add(asset.url)
        for asset in _collect_attachments_from_tag(reply_root, url):
            if asset.url not in seen_assets:
                attachments.append(asset)
                seen_assets.add(asset.url)

    return "\n\n".join(sections), author, published_at, images, attachments


def _collect_entry_roots(soup: BeautifulSoup) -> list[Tag]:
    selectors = [
        "div[id^=post_] .comiis_message",
        "div[id^=post_] .message",
        "div[id^=post_] .pcb .t_f",
        ".comiis_postlist .comiis_message",
        ".comiis_postlist .message",
        ".comiis_mmlist .comiis_message",
        ".comiis_mmlist .message",
        ".comiis_message",
        ".message",
        ".pcb .t_f",
        ".article-content",
        '[data-testid="post-content"]',
        ".post-content",
        "article",
    ]
    roots: list[Tag] = []
    seen_ids: set[int] = set()
    for selector in selectors:
        for tag in soup.select(selector):
            if not isinstance(tag, Tag):
                continue
            tag_identity = id(tag)
            if tag_identity in seen_ids:
                continue
            seen_ids.add(tag_identity)
            roots.append(tag)
    return roots


def _extract_page_author(soup: BeautifulSoup) -> str | None:
    return _extract_text(
        soup,
        [
            ".authi .xw1",
            ".pi .authi a",
            ".user-nick",
            ".author-name",
            'meta[name="author"]',
        ],
    )


def _extract_page_published_at(soup: BeautifulSoup) -> str | None:
    return _extract_text(
        soup,
        [
            "time",
            ".authi em",
            ".post-date",
            ".publish-time",
            '[data-testid="post-time"]',
        ],
        prefer_attr="datetime",
    )


def _extract_author_from_entry(content_root: Tag) -> str | None:
    entry_root = _entry_container_for_content(content_root)
    authi_tag = entry_root.select_one(".authi")
    if isinstance(authi_tag, Tag):
        author_text = _extract_author_from_authi(authi_tag)
        if author_text:
            return author_text
    return _extract_text(
        entry_root,
        [
            ".authi .xw1",
            ".pi .authi a",
            ".user-nick",
            ".author-name",
        ],
    )


def _extract_published_at_from_entry(content_root: Tag) -> str | None:
    entry_root = _entry_container_for_content(content_root)
    title_tag = entry_root.select_one(".authi em span[title]")
    if isinstance(title_tag, Tag):
        title_value = title_tag.get("title")
        if isinstance(title_value, str) and title_value.strip():
            return _normalize_text(title_value)
    return _extract_text(
        entry_root,
        [
            "time",
            ".authi em",
            ".post-date",
            ".publish-time",
        ],
        prefer_attr="datetime",
    )


def _entry_container_for_content(content_root: Tag) -> Tag:
    for ancestor in content_root.parents:
        if not isinstance(ancestor, Tag):
            continue
        if ancestor.get("id", "").startswith("post_"):
            return ancestor
        classes = ancestor.get("class", [])
        if any(
            cls in {"plhin", "plc", "comiis_postli", "comiis_mmlist_li"}
            for cls in classes
        ):
            return ancestor
    return content_root


def _extract_author_from_authi(authi_tag: Tag) -> str | None:
    author_text = authi_tag.get_text(" ", strip=True)
    for removable_tag in authi_tag.select("em, a"):
        removable_text = removable_tag.get_text(" ", strip=True)
        if removable_text:
            author_text = author_text.replace(removable_text, " ")

    author_text = re.split(r"\s*\|\s*", author_text, maxsplit=1)[0]
    author_text = author_text.replace("\xa0", " ").strip(" ;|\t\r\n")
    author_text = re.sub(r"\s+", " ", author_text).strip()
    return author_text or None


def _get_with_rate_limit_retry(
    session: requests.Session,
    url: str,
    *,
    params: dict[str, object] | None = None,
    timeout: float,
    max_attempts: int = 4,
) -> requests.Response:
    response = _rate_limited_get(session, url, params=params, timeout=timeout)
    attempt = 1
    should_retry_on_429 = bool(getattr(session, "_scraper_retry_on_429", True))
    while response.status_code == 429 and should_retry_on_429 and attempt < max_attempts:
        retry_after = response.headers.get("Retry-After")
        delay = float(retry_after) if retry_after and retry_after.isdigit() else float(attempt)
        time.sleep(delay)
        attempt += 1
        response = _rate_limited_get(session, url, params=params, timeout=timeout)
    return response


def _rate_limited_get(
    session: requests.Session,
    url: str,
    *,
    params: dict[str, object] | None = None,
    timeout: float,
    min_interval_override: float | None = None,
) -> requests.Response:
    raw_min_interval = getattr(session, "_scraper_min_request_interval", DEFAULT_MIN_REQUEST_INTERVAL)
    base_min_interval = (
        max(0.0, float(raw_min_interval))
        if isinstance(raw_min_interval, (int, float))
        else DEFAULT_MIN_REQUEST_INTERVAL
    )
    if isinstance(min_interval_override, (int, float)):
        min_interval = max(base_min_interval, max(0.0, float(min_interval_override)))
    else:
        min_interval = base_min_interval
    raw_jitter = getattr(
        session,
        "_scraper_request_interval_jitter",
        DEFAULT_REQUEST_INTERVAL_JITTER,
    )
    jitter = (
        max(0.0, float(raw_jitter))
        if isinstance(raw_jitter, (int, float))
        else DEFAULT_REQUEST_INTERVAL_JITTER
    )
    last_request_time = getattr(session, "_scraper_last_request_time", None)
    now = time.monotonic()
    if isinstance(last_request_time, (int, float)) and min_interval > 0:
        target_interval = min_interval + random.uniform(0.0, jitter)
        delay = target_interval - (now - last_request_time)
        if delay > 0:
            time.sleep(delay)
    max_total_requests = getattr(session, "_scraper_max_total_requests", DEFAULT_MAX_TOTAL_REQUESTS)
    total_requests_made = getattr(session, "_scraper_total_requests_made", 0)
    normalized_total_requests_made = (
        total_requests_made if isinstance(total_requests_made, int) else 0
    )
    if isinstance(max_total_requests, int) and max_total_requests > 0:
        if normalized_total_requests_made >= max_total_requests:
            raise RequestLimitExceededError(
                f"Stopping because the live-request cap of {max_total_requests} requests was reached."
            )
    response = session.get(url, params=params, timeout=timeout)
    setattr(session, "_scraper_total_requests_made", normalized_total_requests_made + 1)
    setattr(session, "_scraper_last_request_time", time.monotonic())
    return response


def _load_min_request_interval(env_values: dict[str, str]) -> float:
    raw_value = os.getenv("SCRAPER_MIN_REQUEST_INTERVAL") or env_values.get(
        "SCRAPER_MIN_REQUEST_INTERVAL"
    )
    if raw_value is None:
        return DEFAULT_MIN_REQUEST_INTERVAL

    try:
        return max(0.0, float(raw_value))
    except ValueError:
        return DEFAULT_MIN_REQUEST_INTERVAL


def _load_request_interval_jitter(env_values: dict[str, str]) -> float:
    raw_value = os.getenv("SCRAPER_REQUEST_INTERVAL_JITTER") or env_values.get(
        "SCRAPER_REQUEST_INTERVAL_JITTER"
    )
    if raw_value is None:
        return DEFAULT_REQUEST_INTERVAL_JITTER

    try:
        return max(0.0, float(raw_value))
    except ValueError:
        return DEFAULT_REQUEST_INTERVAL_JITTER


def _load_max_total_requests(env_values: dict[str, str]) -> int:
    raw_value = os.getenv("SCRAPER_MAX_TOTAL_REQUESTS") or env_values.get(
        "SCRAPER_MAX_TOTAL_REQUESTS"
    )
    if raw_value is None:
        return DEFAULT_MAX_TOTAL_REQUESTS

    try:
        parsed = int(raw_value)
    except ValueError:
        return DEFAULT_MAX_TOTAL_REQUESTS

    return parsed if parsed > 0 else DEFAULT_MAX_TOTAL_REQUESTS


def _bbcode_to_text(value: str) -> str:
    text = value.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\[quote[^\]]*\].*?\[/quote\]\s*", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[url=[^\]]+\](.*?)\[/url\]", r"\1", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[img\](.*?)\[/img\]", r"\1", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[(?:/?)(?:b|color|size|quote|i|u|list|\*|align|backcolor)[^\]]*\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[/?[a-z0-9_]+(?:=[^\]]+)?\]", "", text, flags=re.IGNORECASE)
    return html.unescape(text)


def _collect_assets_from_entries(
    entries: list[dict[str, object]],
    *,
    base_url: str,
) -> tuple[list[DownloadableAsset], list[DownloadableAsset]]:
    images: list[DownloadableAsset] = []
    attachments: list[DownloadableAsset] = []
    seen_image_urls: set[str] = set()
    seen_attachment_urls: set[str] = set()

    for entry in entries:
        message_html = entry.get("message_html")
        if isinstance(message_html, str) and message_html.strip():
            entry_images, entry_attachments = _collect_assets_from_html(message_html, base_url)
        else:
            message_bbcode = entry.get("message_bbcode")
            entry_images, entry_attachments = _collect_assets_from_bbcode(
                message_bbcode if isinstance(message_bbcode, str) else "",
                base_url,
            )

        for asset in entry_images:
            if asset.url not in seen_image_urls:
                seen_image_urls.add(asset.url)
                images.append(asset)
        for asset in entry_attachments:
            if asset.url not in seen_attachment_urls:
                seen_attachment_urls.add(asset.url)
                attachments.append(asset)

    return images, attachments


def _collect_assets_from_html(
    html_fragment: str,
    base_url: str,
) -> tuple[list[DownloadableAsset], list[DownloadableAsset]]:
    soup = BeautifulSoup(html_fragment, "html.parser")
    root = soup.body or soup
    return _collect_images_from_tag(root, base_url), _collect_attachments_from_tag(root, base_url)


def _collect_assets_from_bbcode(
    value: str,
    base_url: str,
) -> tuple[list[DownloadableAsset], list[DownloadableAsset]]:
    images: list[DownloadableAsset] = []
    attachments: list[DownloadableAsset] = []
    seen_image_urls: set[str] = set()
    seen_attachment_urls: set[str] = set()

    for match in re.finditer(r"\[img\](.*?)\[/img\]", value, flags=re.IGNORECASE | re.DOTALL):
        asset_url = _normalize_asset_url(match.group(1), base_url)
        if asset_url and asset_url not in seen_image_urls:
            seen_image_urls.add(asset_url)
            images.append(DownloadableAsset(url=asset_url, kind="image"))

    for match in re.finditer(
        r"\[url=(.*?)\](.*?)\[/url\]",
        value,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        asset_url = _normalize_asset_url(match.group(1), base_url)
        if asset_url and _looks_like_attachment(asset_url) and asset_url not in seen_attachment_urls:
            seen_attachment_urls.add(asset_url)
            attachments.append(DownloadableAsset(url=asset_url, kind="attachment"))

    return images, attachments


def _collect_images_from_tag(content_root: Tag, base_url: str) -> list[DownloadableAsset]:
    images: list[DownloadableAsset] = []
    seen_urls: set[str] = set()
    for image in content_root.find_all("img", src=True):
        asset_url = _normalize_asset_url(image.get("src"), base_url)
        if asset_url and asset_url not in seen_urls:
            seen_urls.add(asset_url)
            images.append(DownloadableAsset(url=asset_url, kind="image"))
    return images


def _collect_attachments_from_tag(content_root: Tag, base_url: str) -> list[DownloadableAsset]:
    attachments: list[DownloadableAsset] = []
    seen_urls: set[str] = set()
    for anchor in content_root.find_all("a", href=True):
        asset_url = _normalize_asset_url(anchor.get("href"), base_url)
        if not asset_url or asset_url in seen_urls:
            continue
        if _looks_like_attachment(asset_url):
            seen_urls.add(asset_url)
            attachments.append(DownloadableAsset(url=asset_url, kind="attachment"))
    return attachments


def _normalize_asset_url(value: str | None, base_url: str) -> str | None:
    if not isinstance(value, str):
        return None
    candidate = value.strip()
    if not candidate or candidate.startswith(("data:", "javascript:", "mailto:", "#")):
        return None
    return urljoin(base_url, candidate)


def _looks_like_attachment(url: str) -> bool:
    path = urlparse(url).path.lower()
    if any(path.endswith(extension) for extension in ATTACHMENT_EXTENSIONS):
        return True
    return "attachment" in path or "attach" in path


def load_env_file(path: str) -> dict[str, str]:
    values: dict[str, str] = {}
    with open(path, encoding="utf-8") as env_file:
        raw_content = env_file.read()

    stripped_content = raw_content.strip()
    if not stripped_content:
        return values

    content_lines = [
        line.strip()
        for line in stripped_content.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if _looks_like_raw_cookie_header(content_lines):
        values["SCRAPER_COOKIE_HEADER"] = stripped_content
        return values

    for line in content_lines:
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def _looks_like_raw_cookie_header(lines: list[str]) -> bool:
    if len(lines) != 1:
        return False
    line = lines[0]
    if ";" not in line:
        return False
    if line.startswith("SCRAPER_COOKIE_HEADER="):
        return False
    return True
