from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup

BASE_URL = "https://www.1point3acres.com"
POST_TARGET_PATTERN = re.compile(
    r"https://www\.1point3acres\.com/home/pins/\d+"
    r"|https://www\.1point3acres\.com/bbs/thread-\d+-1-1\.html"
    r"|https://www\.1point3acres\.com/interview/post/\d+"
    r"|/home/pins/\d+"
    r"|/bbs/thread-\d+-1-1\.html"
    r"|/interview/post/\d+"
)
POST_ID_PATTERN = re.compile(
    r"/home/pins/(\d+)|/bbs/thread-(\d+)-1-1\.html|/interview/post/(\d+)"
)


@dataclass(frozen=True)
class ForumPostRecord:
    post_id: str
    target: str
    tags: tuple[str, ...]


def parse_post_ids_from_html_file(path: str | Path) -> list[str]:
    html_path = Path(path)
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    return parse_post_ids_from_html(html)


def parse_post_ids_from_html(html: str) -> list[str]:
    post_ids: list[str] = []
    for target in parse_post_targets_from_html(html):
        post_id = extract_post_id_from_target(target)
        if post_id is not None:
            post_ids.append(post_id)
    return post_ids


def parse_post_targets_from_html_file(path: str | Path) -> list[str]:
    html_path = Path(path)
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    return parse_post_targets_from_html(html)


def parse_post_records_from_html_file(path: str | Path) -> list[ForumPostRecord]:
    html_path = Path(path)
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    return parse_post_records_from_html(html)


def parse_post_records_from_html(html: str) -> list[ForumPostRecord]:
    soup = BeautifulSoup(html, "html.parser")
    thread_items = soup.find_all(attrs={"data-sentry-component": "ForumThreadItem"})
    records: list[ForumPostRecord] = []
    seen_ids: set[str] = set()

    for thread_item in thread_items:
        target = _find_first_post_target(thread_item)
        if target is None:
            continue
        post_id = extract_post_id_from_target(target)
        if post_id is None or post_id in seen_ids:
            continue
        seen_ids.add(post_id)
        records.append(
            ForumPostRecord(
                post_id=post_id,
                target=target,
                tags=tuple(_extract_thread_item_tags(thread_item)),
            )
        )

    if records:
        return records

    return _parse_next_data_post_records(soup)


def parse_post_targets_from_html(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    post_targets: list[str] = []
    seen: set[str] = set()

    thread_items = soup.find_all(attrs={"data-sentry-component": "ForumThreadItem"})
    if thread_items:
        for record in parse_post_records_from_html(html):
            if record.target not in seen:
                seen.add(record.target)
                post_targets.append(record.target)
        return post_targets

    for record in _parse_next_data_post_records(soup):
        if record.target not in seen:
            seen.add(record.target)
            post_targets.append(record.target)
    if post_targets:
        return post_targets

    for tag in soup.find_all(href=True):
        href = tag.get("href")
        if not isinstance(href, str):
            continue
        _collect_post_targets(href, post_targets, seen)

    _collect_post_targets(html, post_targets, seen)
    return post_targets


def extract_post_id_from_target(target: str) -> str | None:
    match = POST_ID_PATTERN.search(target)
    if match is None:
        return None
    for group in match.groups():
        if group:
            return group
    return None


def _collect_post_targets(value: str, post_targets: list[str], seen: set[str]) -> None:
    for match in POST_TARGET_PATTERN.finditer(value):
        target = canonicalize_post_target(match.group(0))
        if target not in seen:
            seen.add(target)
            post_targets.append(target)


def canonicalize_post_target(target: str) -> str:
    if target.startswith("http://") or target.startswith("https://"):
        return target
    return f"{BASE_URL}{target}"


def _find_first_post_target(thread_item) -> str | None:
    for tag in thread_item.find_all(href=True):
        href = tag.get("href")
        if not isinstance(href, str):
            continue
        match = POST_TARGET_PATTERN.search(href)
        if match is None:
            continue
        return canonicalize_post_target(match.group(0))
    return None


def _extract_thread_item_tags(thread_item) -> list[str]:
    metadata_blocks = thread_item.find_all("div")
    for block in metadata_blocks:
        classes = block.get("class", [])
        if "text-xs" not in classes:
            continue

        tags: list[str] = []
        for span in block.find_all("span", recursive=False):
            text = span.get_text(" ", strip=True)
            if not text:
                continue
            span_classes = span.get("class", [])
            if "bg-muted-foreground" in span_classes:
                continue
            tags.append(text)
        if tags:
            return tags

    return []


def _parse_next_data_post_records(soup: BeautifulSoup) -> list[ForumPostRecord]:
    script = soup.find("script", id="__NEXT_DATA__")
    if script is None:
        return []

    raw_json = script.string or script.get_text()
    if not raw_json:
        return []

    try:
        next_data = json.loads(raw_json)
    except json.JSONDecodeError:
        return []

    queries = (
        next_data.get("props", {})
        .get("pageProps", {})
        .get("trpcState", {})
        .get("json", {})
        .get("queries", [])
    )
    if not isinstance(queries, list):
        return []

    records: list[ForumPostRecord] = []
    seen_ids: set[str] = set()
    for query in queries:
        data = _get_query_data_list(query)
        if data is None:
            continue
        for item in data:
            if not isinstance(item, dict):
                continue
            post_id = item.get("tid")
            if not isinstance(post_id, int):
                continue
            post_id_text = str(post_id)
            if post_id_text in seen_ids:
                continue
            seen_ids.add(post_id_text)
            records.append(
                ForumPostRecord(
                    post_id=post_id_text,
                    target=f"{BASE_URL}/bbs/thread-{post_id_text}-1-1.html",
                    tags=(),
                )
            )

    return records


def _get_query_data_list(query: object) -> list[object] | None:
    if not isinstance(query, dict):
        return None
    data = query.get("state", {}).get("data", {}) if isinstance(query.get("state"), dict) else {}
    if not isinstance(data, dict):
        return None
    items = data.get("data")
    if not isinstance(items, list):
        return None
    if not any(isinstance(item, dict) and isinstance(item.get("tid"), int) for item in items):
        return None
    return items
