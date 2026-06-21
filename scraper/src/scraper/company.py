from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlparse

import requests

from .cli import extract_post_id, save_post_content
from .forum import (
    parse_post_records_from_html,
    parse_post_records_from_html_file,
    parse_post_targets_from_html_file,
)
from .post import (
    DownloadableAsset,
    ScrapedPost,
    _rate_limited_get,
    build_authenticated_session,
    scrape_post,
)

THREAD_PAGE_SIZE = 20
COMPANY_PAGE_LIST_MIN_REQUEST_INTERVAL = 30.0


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape all company posts from saved forum HTML files.")
    parser.add_argument("company", help="Company folder name under inputs/, for example anthropic.")
    parser.add_argument(
        "--inputs-root",
        default="inputs",
        help="Root folder that contains per-company HTML directories.",
    )
    parser.add_argument(
        "--outputs-root",
        default="outputs",
        help="Root folder for raw posts, assets, and combined markdown output.",
    )
    parser.add_argument(
        "--env-file",
        help="Optional legacy .env file containing a raw cookie header or SCRAPER_COOKIE_HEADER.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=1,
        help="Maximum number of input HTML pages to use. Use -1 to use all pages.",
    )
    parser.add_argument(
        "--refresh-inputs",
        action="store_true",
        help="Fetch company input HTML pages again before scraping. By default, existing input HTML files are reused.",
    )
    args = parser.parse_args()

    stats = run_company_scrape(
        args.company,
        inputs_root=Path(args.inputs_root),
        outputs_root=Path(args.outputs_root),
        env_file=args.env_file,
        max_pages=args.max_pages,
        refresh_inputs=args.refresh_inputs,
    )

    print(
        "Finished: "
        f"{stats['identified']} posts identified, "
        f"{stats['already_exists']} already exists, "
        f"{stats['newly_scraped']} newly scraped, "
        f"{stats['failed']} failed scraping."
    )
    print(f"combined_output: {stats['combined_output_path']}")


def run_company_scrape(
    company: str,
    *,
    inputs_root: Path,
    outputs_root: Path,
    env_file: str | None = None,
    max_pages: int = 1,
    refresh_inputs: bool = False,
) -> dict[str, object]:
    if max_pages == 0 or max_pages < -1:
        raise ValueError("max_pages must be -1 or a positive integer.")

    input_dir = inputs_root / company
    session = build_authenticated_session(env_file=env_file)
    setattr(session, "_scraper_retry_on_429", False)
    html_files = load_company_input_files(
        company,
        input_dir=input_dir,
        session=session,
        refresh_inputs=refresh_inputs,
        max_pages=max_pages,
    )
    if not html_files:
        raise FileNotFoundError(f"No company input HTML files available in {input_dir}")

    all_post_targets = collect_company_post_targets_from_files(html_files)
    post_metadata = collect_company_post_metadata_from_files(html_files)
    post_targets = all_post_targets
    if max_pages == -1:
        print(f"Identified {len(post_targets)} posts from {len(html_files)} HTML files.")
    else:
        print(
            f"Identified {len(post_targets)} posts from the first {len(html_files)} HTML files "
            f"due to --max-pages={max_pages}."
        )

    raw_posts_dir = outputs_root / "raw_posts"
    raw_images_dir = outputs_root / "raw_images"
    raw_attachments_dir = outputs_root / "raw_attachements"
    combined_output_path = outputs_root / company / f"{company}.md"

    raw_posts_dir.mkdir(parents=True, exist_ok=True)
    raw_images_dir.mkdir(parents=True, exist_ok=True)
    raw_attachments_dir.mkdir(parents=True, exist_ok=True)
    combined_output_path.parent.mkdir(parents=True, exist_ok=True)

    identified = len(post_targets)
    already_exists = 0
    newly_scraped = 0
    failed = 0
    for index, post_target in enumerate(post_targets, start=1):
        post_id = extract_post_id(post_target)
        raw_post_path = raw_posts_dir / f"{post_id}.md"

        if raw_post_path.exists():
            already_exists += 1
            print(f"[{index}/{identified}] skip {post_id}: already exists")
            continue

        print(f"[{index}/{identified}] scraping {post_id}")
        try:
            post = scrape_post(post_target, session)
            save_post_content(post, output_root=raw_posts_dir)
            image_count, attachment_count = download_post_assets(
                post,
                post_id=post_id,
                session=session,
                image_root=raw_images_dir,
                attachment_root=raw_attachments_dir,
            )
            newly_scraped += 1
            print(
                f"[{index}/{identified}] saved {post_id}"
                f" ({image_count} images, {attachment_count} attachments)"
            )
        except Exception as exc:
            failed += 1
            print(f"[{index}/{identified}] failed {post_id}: {exc}")
            if is_http_403_or_429_error(exc):
                print("Stopping early after an HTTP 403/429 response to reduce account risk.")
                break

    combine_company_posts(
        company,
        post_targets=post_targets,
        raw_posts_dir=raw_posts_dir,
        output_path=combined_output_path,
        post_metadata=post_metadata,
    )

    return {
        "identified": identified,
        "identified_total": len(all_post_targets),
        "already_exists": already_exists,
        "newly_scraped": newly_scraped,
        "failed": failed,
        "combined_output_path": combined_output_path,
    }


def collect_company_post_targets(input_dir: Path) -> list[str]:
    return collect_company_post_targets_from_files(sorted_company_html_files(input_dir))


def collect_company_post_targets_from_files(html_files: list[Path]) -> list[str]:
    targets: list[str] = []
    seen_ids: set[str] = set()

    for html_file in html_files:
        for target in parse_post_targets_from_html_file(html_file):
            post_id = extract_post_id(target)
            if post_id in seen_ids:
                continue
            seen_ids.add(post_id)
            targets.append(target)

    return targets


def collect_company_post_metadata(input_dir: Path) -> dict[str, list[str]]:
    return collect_company_post_metadata_from_files(sorted_company_html_files(input_dir))


def collect_company_post_metadata_from_files(html_files: list[Path]) -> dict[str, list[str]]:
    metadata_by_post_id: dict[str, list[str]] = {}

    for html_file in html_files:
        for record in parse_post_records_from_html_file(html_file):
            metadata_by_post_id.setdefault(record.post_id, list(record.tags))

    return metadata_by_post_id


def load_company_input_files(
    company: str,
    *,
    input_dir: Path,
    session,
    refresh_inputs: bool,
    max_pages: int,
) -> list[Path]:
    existing_html_files = sorted_company_html_files(input_dir)
    if existing_html_files and not refresh_inputs:
        limited_existing_html_files = limit_input_html_files(existing_html_files, max_pages=max_pages)
        print(
            f"Using {len(limited_existing_html_files)} existing input HTML files from {input_dir}."
        )
        return limited_existing_html_files

    if refresh_inputs and existing_html_files:
        print(f"Refreshing input HTML files in {input_dir}.")
    else:
        print(f"Fetching input HTML files into {input_dir}.")

    return fetch_company_input_pages(company, input_dir=input_dir, session=session, max_pages=max_pages)


def limit_input_html_files(html_files: list[Path], *, max_pages: int) -> list[Path]:
    if max_pages == -1:
        return list(html_files)
    return list(html_files[:max_pages])


def sorted_company_html_files(input_dir: Path) -> list[Path]:
    return sorted(input_dir.glob("*.html"), key=_html_page_sort_key)


def fetch_company_input_pages(
    company: str,
    *,
    input_dir: Path,
    session,
    max_pages: int,
) -> list[Path]:
    input_dir.mkdir(parents=True, exist_ok=True)

    page = 1
    last_dateline = 0
    saved_paths: list[Path] = []
    total = 0
    seen_page_targets: set[tuple[str, ...]] = set()

    while True:
        html_text = fetch_company_page_html(
            company,
            page=page,
            session=session,
        )
        page_records = parse_post_records_from_html(html_text)
        page_targets = tuple(record.target for record in page_records)
        if not page_targets or page_targets in seen_page_targets:
            break
        seen_page_targets.add(page_targets)
        total += len(page_targets)

        output_path = input_dir / f"{page}.html"
        output_path.write_text(html_text, encoding="utf-8")
        saved_paths.append(output_path)
        print(f"[inputs] saved {output_path} ({len(page_targets)} threads)")

        if max_pages != -1 and page >= max_pages:
            break
        if len(page_targets) < THREAD_PAGE_SIZE:
            break

        page += 1

    return saved_paths


def _html_page_sort_key(path: Path) -> tuple[int, str]:
    try:
        return (int(path.stem), path.name)
    except ValueError:
        return (10**9, path.name)


def fetch_company_page_html(
    company: str,
    *,
    page: int,
    session,
) -> str:
    response = _rate_limited_get(
        session,
        build_company_page_url(company, page=page),
        timeout=30.0,
        min_interval_override=COMPANY_PAGE_LIST_MIN_REQUEST_INTERVAL,
    )
    response.raise_for_status()
    return response.text


def build_company_page_url(company: str, *, page: int) -> str:
    company_slug = company.strip().lower()
    if not company_slug:
        raise ValueError("company must not be empty")
    return f"https://www.1point3acres.com/interview/company/{company_slug}?page={page}"


def download_post_assets(
    post: ScrapedPost,
    *,
    post_id: str,
    session,
    image_root: Path,
    attachment_root: Path,
) -> tuple[int, int]:
    image_count = _download_assets(post.images, post_id=post_id, session=session, output_root=image_root)
    attachment_count = _download_assets(
        post.attachments,
        post_id=post_id,
        session=session,
        output_root=attachment_root,
    )
    return image_count, attachment_count


def _download_assets(
    assets: list[DownloadableAsset],
    *,
    post_id: str,
    session,
    output_root: Path,
) -> int:
    output_root.mkdir(parents=True, exist_ok=True)
    saved_count = 0
    seen_urls: set[str] = set()

    for index, asset in enumerate(assets, start=1):
        if asset.url in seen_urls:
            continue
        seen_urls.add(asset.url)

        response = _rate_limited_get(session, asset.url, timeout=30.0)
        response.raise_for_status()

        output_path = output_root / build_asset_filename(asset.url, post_id=post_id, index=index)
        output_path.write_bytes(response.content)
        saved_count += 1

    return saved_count


def build_asset_filename(url: str, *, post_id: str, index: int) -> str:
    path = unquote(urlparse(url).path)
    basename = Path(path).name
    if basename:
        return f"{post_id}_{sanitize_filename(basename)}"

    return f"{post_id}_asset-{index}"


def sanitize_filename(filename: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", filename).strip("._")
    return sanitized or "asset"


def is_http_403_or_429_error(exc: Exception) -> bool:
    if isinstance(exc, requests.HTTPError) and exc.response is not None:
        return exc.response.status_code in {403, 429}

    response = getattr(exc, "response", None)
    return getattr(response, "status_code", None) in {403, 429}


def combine_company_posts(
    company: str,
    *,
    post_targets: list[str],
    raw_posts_dir: Path,
    output_path: Path,
    post_metadata: dict[str, list[str]] | None = None,
) -> Path:
    display_company = company[:1].upper() + company[1:] if company else company
    parts: list[str] = [f"# {display_company}", ""]
    published_dates: list[str] = []
    post_metadata = post_metadata or {}

    included = 0
    for target in post_targets:
        post_id = extract_post_id(target)
        post_path = raw_posts_dir / f"{post_id}.md"
        if not post_path.exists():
            continue
        post_text = post_path.read_text(encoding="utf-8").rstrip()
        published_date = extract_published_date(post_text)
        post_text = inject_post_tags_into_markdown(
            post_text,
            tags=post_metadata.get(post_id, []),
            published_date=published_date,
        )
        if published_date:
            published_dates.append(published_date)
        if included > 0:
            parts.extend(["", "---", ""])
        parts.append(f'<a id="post-{post_id}"></a>')
        parts.append("")
        parts.append(post_text)
        included += 1

    body = "\n".join(parts).rstrip() + "\n"
    toc = build_table_of_contents(body)
    summary = build_summary(included, published_dates)
    body_parts = body.split("\n", 2)
    body_without_title = body_parts[2] if len(body_parts) >= 3 else ""
    preamble_parts = [f"# {display_company}", ""]
    if summary:
        preamble_parts.extend([summary, ""])
    if toc:
        preamble_parts.append(toc.rstrip())
        preamble_parts.append("")
    combined = "\n".join(preamble_parts) + body_without_title
    output_path.write_text(combined.rstrip() + "\n", encoding="utf-8")
    return output_path


def inject_post_tags_into_markdown(
    markdown_content: str,
    *,
    tags: list[str],
    published_date: str | None,
) -> str:
    position_type_tag = extract_position_type_tag(tags)
    if not position_type_tag and not published_date:
        return markdown_content

    lines = markdown_content.splitlines()
    if not lines or not lines[0].startswith("# "):
        return markdown_content

    title = lines[0][2:].strip()
    heading_parts = [title]
    if published_date:
        heading_parts.append(published_date)
    heading = " ".join(heading_parts)
    if position_type_tag:
        heading = f"{heading} [{position_type_tag}]"
    lines[0] = f"# {heading}"
    return "\n".join(lines)


def extract_position_type_tag(tags: list[str]) -> str | None:
    if len(tags) >= 4:
        return tags[3]
    return None


def build_summary(post_count: int, published_dates: list[str]) -> str:
    if post_count == 0:
        return "This file contains 0 posts."
    if not published_dates:
        return f"This file contains {post_count} posts."
    return (
        f"This file contains {post_count} posts created between "
        f"{min(published_dates)} and {max(published_dates)}."
    )


def build_table_of_contents(markdown_content: str) -> str:
    toc_lines: list[str] = []
    lines = markdown_content.splitlines()
    pending_anchor_id: str | None = None

    for index, line in enumerate(lines):
        anchor_match = re.fullmatch(r'<a id="(?P<anchor>post-\d+)"></a>', line.strip())
        if anchor_match:
            pending_anchor_id = anchor_match.group("anchor")
            continue

        if not line.startswith("# "):
            continue

        heading = line[2:].strip()
        if not heading or heading == lines[0][2:].strip():
            continue
        if pending_anchor_id is None:
            continue

        display_heading = heading
        if not re.search(r"\d{4}-\d{2}-\d{2}", heading):
            metadata_line = ""
            for candidate in lines[index + 1 :]:
                if candidate.strip():
                    metadata_line = candidate
                    break
            if metadata_line:
                posted_match = re.match(
                    r"^`Post ID: .*?\| .*?\| `?Published: (?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})",
                    metadata_line,
                )
                if posted_match:
                    display_heading = (
                        f"{heading} "
                        f"{posted_match.group('year')}-"
                        f"{int(posted_match.group('month')):02d}-"
                        f"{int(posted_match.group('day')):02d}"
                    )

        toc_lines.append(f"- [{display_heading}](#{pending_anchor_id})")
        pending_anchor_id = None

    if not toc_lines:
        return ""

    return "## Table of Contents\n\n" + "\n".join(toc_lines) + "\n\n"


def extract_published_date(markdown_content: str) -> str | None:
    match = re.search(
        r"`Published: (?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})",
        markdown_content,
    )
    if match is None:
        return None
    return f"{match.group('year')}-{int(match.group('month')):02d}-{int(match.group('day')):02d}"
