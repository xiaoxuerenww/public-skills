#!/usr/bin/env python3
"""Print likely raw scraper blocks for a company and interview round."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "by",
    "for",
    "from",
    "in",
    "interview",
    "of",
    "on",
    "or",
    "round",
    "the",
    "to",
}


@dataclass
class Block:
    post_id: str
    source: str
    label: str
    text: str
    score: int


def normalize_token(value: str) -> str:
    return value.strip().lower()


def query_terms(round_name: str, keywords: str) -> list[str]:
    raw = re.split(r"[\s,;/|]+", f"{round_name} {keywords}")
    terms = []
    for item in raw:
        token = normalize_token(item)
        if len(token) < 2 or token in STOPWORDS:
            continue
        if token not in terms:
            terms.append(token)
    return terms


def post_ids_from_company_index(scraper_root: Path, company: str) -> set[str]:
    company_file = scraper_root / "outputs" / company / f"{company}.md"
    if not company_file.exists():
        return set()
    text = company_file.read_text(encoding="utf-8", errors="replace")
    return set(re.findall(r"thread-(\d+)-1-1\.html|raw_posts/(\d+)\.md|Post ID:\s*(\d+)", text))


def flatten_post_ids(matches: set[tuple[str, ...] | str]) -> set[str]:
    ids: set[str] = set()
    for match in matches:
        if isinstance(match, str):
            if match:
                ids.add(match)
            continue
        for item in match:
            if item:
                ids.add(item)
    return ids


def source_url(text: str, post_id: str) -> str:
    match = re.search(r"^Source:\s*(\S+)", text, flags=re.MULTILINE)
    if match:
        return match.group(1)
    return f"https://www.1point3acres.com/bbs/thread-{post_id}-1-1.html"


def split_blocks(post_text: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    post_match = re.search(
        r"## Post\s*\n(?P<body>.*?)(?:\n---\s*\n\s*## Replies|\Z)",
        post_text,
        flags=re.DOTALL,
    )
    if post_match:
        blocks.append(("Post", post_match.group("body").strip()))

    replies_match = re.search(r"## Replies\s*\n(?P<body>.*)", post_text, flags=re.DOTALL)
    if not replies_match:
        return blocks

    reply_body = replies_match.group("body").strip()
    parts = re.split(r"(?=^\*\*#\d+\s)", reply_body, flags=re.MULTILINE)
    for part in parts:
        cleaned = part.strip()
        if not cleaned:
            continue
        first_line = cleaned.splitlines()[0].strip()
        blocks.append((first_line, cleaned))
    return blocks


def score_text(text: str, terms: list[str], phrase: str) -> int:
    lowered = text.lower()
    score = 0
    if phrase and phrase.lower() in lowered:
        score += 10
    for term in terms:
        if re.fullmatch(r"[a-z0-9_+-]+", term):
            score += len(re.findall(rf"(?<![a-z0-9_+-]){re.escape(term)}(?![a-z0-9_+-])", lowered))
        else:
            score += lowered.count(term)
    return score


def collect_blocks(
    scraper_root: Path,
    company: str,
    round_name: str,
    keywords: str,
    post_ids: set[str],
) -> list[Block]:
    raw_dir = scraper_root / "outputs" / "raw_posts"
    if not raw_dir.exists():
        raise SystemExit(f"Missing raw post directory: {raw_dir}")

    inferred_ids = flatten_post_ids(post_ids_from_company_index(scraper_root, company))
    target_ids = post_ids or inferred_ids
    terms = query_terms(round_name, keywords)
    blocks: list[Block] = []

    for path in sorted(raw_dir.glob("*.md")):
        post_id = path.stem
        if target_ids and post_id not in target_ids:
            continue
        post_text = path.read_text(encoding="utf-8", errors="replace")
        url = source_url(post_text, post_id)
        for label, text in split_blocks(post_text):
            score = score_text(text, terms, round_name)
            if score <= 0:
                continue
            blocks.append(Block(post_id=post_id, source=url, label=label, text=text, score=score))

    blocks.sort(key=lambda item: (-item.score, item.post_id, item.label))
    return blocks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scraper-root", default=".", help="Path to scraper repo root.")
    parser.add_argument("--company", required=True, help="Company slug, matching outputs/<company>.")
    parser.add_argument("--round", required=True, dest="round_name", help="Interview round phrase.")
    parser.add_argument("--keywords", default="", help="Comma or space separated extra search terms.")
    parser.add_argument("--post-id", action="append", default=[], help="Restrict to a known post ID.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum candidate blocks to print.")
    args = parser.parse_args()

    blocks = collect_blocks(
        scraper_root=Path(args.scraper_root).expanduser().resolve(),
        company=args.company,
        round_name=args.round_name,
        keywords=args.keywords,
        post_ids=set(args.post_id),
    )

    print(f"# Candidate raw blocks for {args.company} / {args.round_name}")
    print()
    print("Review manually before using. Preserve only raw text copied from source files.")
    print()
    for block in blocks[: args.limit]:
        print(f"## Score {block.score} | Source `{block.post_id}` | {block.label}")
        print()
        print(f"Original post: {block.source}")
        print()
        print("```text")
        print(block.text)
        print("```")
        print()


if __name__ == "__main__":
    main()
