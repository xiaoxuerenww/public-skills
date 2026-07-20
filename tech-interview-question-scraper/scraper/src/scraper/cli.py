from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from datetime import datetime
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from .post import ScrapedPost, build_authenticated_session, scrape_post

DISPLAY_TIMEZONE = ZoneInfo("America/Los_Angeles")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape an authenticated 1Point3Acres post.")
    parser.add_argument("url", help="The full post URL to scrape.")
    parser.add_argument(
        "--env-file",
        help="Optional legacy .env file containing a raw cookie header or SCRAPER_COOKIE_HEADER.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the scraped post as JSON instead of plain text.",
    )
    args = parser.parse_args()

    session = build_authenticated_session(env_file=args.env_file)
    post = scrape_post(args.url, session)
    output_path = save_post_content(post)

    if args.json:
        print(
            json.dumps(
                {
                    "url": post.url,
                    "title": post.title,
                    "author": post.author,
                    "published_at": post.published_at,
                    "content": post.content,
                    "output_path": str(output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    print(f"saved_to: {output_path}")
    print(f"title: {post.title}")
    print(f"author: {post.author}")
    print(f"published_at: {post.published_at}")
    print(f"url: {post.url}")
    print("content:")
    print(post.content)


def save_post_content(post: ScrapedPost, *, output_root: Path | None = None) -> Path:
    output_dir = (output_root or Path("outputs/raw_posts")).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{extract_post_id(post.url)}.md"
    output_path.write_text(format_post_markdown(post), encoding="utf-8")
    return output_path


def extract_post_id(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    thread_match = re.fullmatch(r"/bbs/thread-(\d+)-1-1\.html", path)
    if thread_match is not None:
        return thread_match.group(1)

    pin_match = re.fullmatch(r"/home/pins/(\d+)", path)
    if pin_match is not None:
        return pin_match.group(1)

    post_id = path.split("/")[-1]
    if not post_id:
        raise ValueError(f"Could not determine post id from URL: {url}")
    return post_id


def format_post_markdown(post: ScrapedPost) -> str:
    main_content, replies = split_post_content(post.content)
    lines = [f"# {post.title}", ""]

    metadata_parts = [f"Post ID: {extract_post_id(post.url)}"]
    if post.author:
        metadata_parts.append(f"Author: {post.author}")
    formatted_published_at = format_timestamp(post.published_at)
    if formatted_published_at:
        metadata_parts.append(f"Published: {formatted_published_at}")
    lines.append(" | ".join(f"`{part}`" for part in metadata_parts))
    lines.append("")
    lines.append(f"Source: {post.url}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Post")
    lines.append("")
    lines.extend(main_content.splitlines())

    if replies:
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Replies")
        lines.append("")
        for reply in replies:
            header = f"**#{reply['position']} {reply['author']}**"
            timestamp = format_timestamp(reply["published_at"])
            if timestamp:
                header = f"{header} | `{timestamp}`"
            lines.append(header)
            lines.append("")
            lines.extend(reply["body"].splitlines())
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def split_post_content(content: str) -> tuple[str, list[dict[str, str]]]:
    marker = "\n\nReplies:\n\n"
    if marker not in content:
        return content, []

    main_content, raw_replies = content.split(marker, 1)
    chunks = [chunk.strip() for chunk in raw_replies.split("\n\n") if chunk.strip()]
    replies: list[dict[str, str]] = []

    for index in range(0, len(chunks), 2):
        if index + 1 >= len(chunks):
            break
        header = chunks[index]
        body = chunks[index + 1]
        match = re.fullmatch(r"#(?P<position>\d+|\?)\s+(?P<author>.+?)(?:\s+at\s+(?P<published_at>.+))?", header)
        if match is None:
            continue
        replies.append(
            {
                "position": match.group("position"),
                "author": match.group("author"),
                "published_at": match.group("published_at") or "",
                "body": body,
            }
        )

    return main_content, replies


def format_timestamp(value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    if not stripped:
        return None
    if stripped.isdigit():
        return datetime.fromtimestamp(int(stripped), tz=DISPLAY_TIMEZONE).strftime(
            "%Y-%m-%d %H:%M:%S %Z"
        )
    return stripped


if __name__ == "__main__":
    main()
