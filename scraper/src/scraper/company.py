from __future__ import annotations

import argparse
import ast
from datetime import date, datetime
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

import requests

from .cli import extract_post_id, save_post_content
from .forum import (
    ForumPostRecord,
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
        help=(
            "Fetch company input HTML pages again before scraping. Incremental mode does this by "
            "default; --full-scrape reuses existing input HTML unless this is set."
        ),
    )
    parser.add_argument(
        "--since-last-scrape",
        action="store_true",
        help=(
            "Deprecated no-op: this is now the default unless --full-scrape is set."
        ),
    )
    parser.add_argument(
        "--start-date",
        help="Start date in YYYY-MM-DD format. You will still be prompted to confirm.",
    )
    parser.add_argument(
        "--full-scrape",
        action="store_true",
        help="Disable the default date cutoff and scrape all posts from the selected company pages.",
    )
    parser.add_argument(
        "--filter-condition",
        help=(
            "Natural-language filter over company-page fields, for example "
            "'MLE or Machine Learning posts'. Use expr:<condition> for structured filters."
        ),
    )
    args = parser.parse_args()

    if args.full_scrape and (args.since_last_scrape or args.start_date):
        parser.error("--full-scrape cannot be combined with --since-last-scrape or --start-date.")

    start_date = None
    if not args.full_scrape:
        inferred_start_date = (
            parse_start_date(args.start_date)
            if args.start_date
            else infer_last_company_scrape_date(
                args.company,
                inputs_root=Path(args.inputs_root),
                outputs_root=Path(args.outputs_root),
            )
        )
        start_date = prompt_for_start_date(args.company, inferred_start_date)

    stats = run_company_scrape(
        args.company,
        inputs_root=Path(args.inputs_root),
        outputs_root=Path(args.outputs_root),
        env_file=args.env_file,
        max_pages=args.max_pages,
        refresh_inputs=args.refresh_inputs or start_date is not None,
        start_date=start_date,
        filter_condition=args.filter_condition,
    )

    print(
        "Finished: "
        f"{stats['identified']} posts identified, "
        f"{stats['already_exists']} already exists, "
        f"{stats['newly_scraped']} newly scraped, "
        f"{stats['failed']} failed scraping."
    )
    if stats.get("start_date"):
        print(f"start_date: {stats['start_date']}")
    if stats.get("filter_condition"):
        print(f"filter_condition: {stats['filter_condition']}")
    print(f"combined_output: {stats['combined_output_path']}")


def run_company_scrape(
    company: str,
    *,
    inputs_root: Path,
    outputs_root: Path,
    env_file: str | None = None,
    max_pages: int = 1,
    refresh_inputs: bool = False,
    start_date: date | None = None,
    filter_condition: str | None = None,
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
        stop_after_date=start_date,
    )
    if not html_files and start_date is not None:
        html_files = limit_input_html_files(sorted_company_html_files(input_dir), max_pages=max_pages)
    if not html_files:
        raise FileNotFoundError(f"No company input HTML files available in {input_dir}")

    scrape_post_records = collect_company_post_records_from_files(html_files)
    post_records = filter_post_records_after_start_date(scrape_post_records, start_date=start_date)
    post_records = filter_post_records_by_condition(
        post_records,
        filter_condition=filter_condition,
    )
    all_post_targets = [record.target for record in scrape_post_records]
    post_targets = [record.target for record in post_records]
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

    combine_html_files = (
        limit_input_html_files(sorted_company_html_files(input_dir), max_pages=-1)
        if start_date is not None
        else html_files
    )
    combine_post_records = collect_company_post_records_from_files(combine_html_files)
    combine_post_records = filter_post_records_by_condition(
        combine_post_records,
        filter_condition=filter_condition,
    )
    post_metadata = metadata_from_post_records(combine_post_records)

    combine_company_posts(
        company,
        post_targets=[record.target for record in combine_post_records],
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
        "start_date": start_date.isoformat() if start_date else None,
        "filter_condition": filter_condition,
    }


def collect_company_post_targets(input_dir: Path) -> list[str]:
    return collect_company_post_targets_from_files(sorted_company_html_files(input_dir))


def collect_company_post_targets_from_files(html_files: list[Path]) -> list[str]:
    return [record.target for record in collect_company_post_records_from_files(html_files)]


def collect_company_post_records_from_files(html_files: list[Path]) -> list[ForumPostRecord]:
    records: list[ForumPostRecord] = []
    seen_ids: set[str] = set()

    for html_file in html_files:
        parsed_records = parse_post_records_from_html_file(html_file)
        if not parsed_records:
            parsed_records = [
                ForumPostRecord(
                    post_id=extract_post_id(target),
                    target=target,
                    tags=(),
                )
                for target in parse_post_targets_from_html_file(html_file)
            ]

        for record in parsed_records:
            if record.post_id in seen_ids:
                continue
            seen_ids.add(record.post_id)
            records.append(record)

    return records


def collect_company_post_metadata(input_dir: Path) -> dict[str, list[str]]:
    return collect_company_post_metadata_from_files(sorted_company_html_files(input_dir))


def collect_company_post_metadata_from_files(html_files: list[Path]) -> dict[str, list[str]]:
    return metadata_from_post_records(collect_company_post_records_from_files(html_files))

def metadata_from_post_records(records: list[ForumPostRecord]) -> dict[str, list[str]]:
    metadata_by_post_id: dict[str, list[str]] = {}

    for record in records:
        metadata_by_post_id.setdefault(record.post_id, list(record.tags))

    return metadata_by_post_id


def load_company_input_files(
    company: str,
    *,
    input_dir: Path,
    session,
    refresh_inputs: bool,
    max_pages: int,
    stop_after_date: date | None = None,
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

    return fetch_company_input_pages(
        company,
        input_dir=input_dir,
        session=session,
        max_pages=max_pages,
        stop_after_date=stop_after_date,
    )


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
    stop_after_date: date | None = None,
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
        if stop_after_date is not None:
            newer_page_records = filter_post_records_after_start_date(
                page_records,
                start_date=stop_after_date,
            )
            if not newer_page_records:
                print(
                    f"[inputs] stopping before page {page}: no posts after {stop_after_date.isoformat()}"
                )
                break

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
        if stop_after_date is not None and page_contains_posts_on_or_before_date(
            page_records,
            stop_after_date,
        ):
            print(f"[inputs] stopping after page {page}: reached {stop_after_date.isoformat()}")
            break

        page += 1

    return saved_paths


def filter_post_records_after_start_date(
    records: list[ForumPostRecord],
    *,
    start_date: date | None,
) -> list[ForumPostRecord]:
    if start_date is None:
        return list(records)

    filtered: list[ForumPostRecord] = []
    for record in records:
        record_date = record_date_from_dateline(record.dateline)
        if record_date is None or record_date > start_date:
            filtered.append(record)
    return filtered


def filter_post_records_by_condition(
    records: list[ForumPostRecord],
    *,
    filter_condition: str | None,
) -> list[ForumPostRecord]:
    if not filter_condition:
        return list(records)

    if should_parse_structured_filter(filter_condition):
        expression = parse_filter_condition(strip_expression_prefix(filter_condition))
        return [
            record
            for record in records
            if evaluate_filter_expression(expression, build_filter_context(record))
        ]

    query_groups = parse_natural_language_filter(filter_condition)
    return [
        record
        for record in records
        if matches_natural_language_filter(record, query_groups)
    ]


def should_parse_structured_filter(filter_condition: str) -> bool:
    if filter_condition.strip().startswith("expr:"):
        return True
    return re.search(
        r"==|!=|<=|>=|<|>|\bnot\s+in\b|\bin\b|\bcontains\s*\(|\bregex\s*\(",
        filter_condition,
    ) is not None


def strip_expression_prefix(filter_condition: str) -> str:
    stripped = filter_condition.strip()
    if stripped.startswith("expr:"):
        return stripped[len("expr:") :].strip()
    return filter_condition


def parse_filter_condition(filter_condition: str) -> ast.Expression:
    try:
        expression = ast.parse(filter_condition, mode="eval")
    except SyntaxError as exc:
        raise ValueError(f"Invalid filter condition: {filter_condition}") from exc
    validate_filter_ast(expression)
    return expression


def validate_filter_ast(node: ast.AST) -> None:
    allowed_nodes = (
        ast.Expression,
        ast.BoolOp,
        ast.UnaryOp,
        ast.Compare,
        ast.Name,
        ast.Load,
        ast.Constant,
        ast.List,
        ast.Tuple,
        ast.Set,
        ast.Call,
        ast.And,
        ast.Or,
        ast.Not,
        ast.Eq,
        ast.NotEq,
        ast.Lt,
        ast.LtE,
        ast.Gt,
        ast.GtE,
        ast.In,
        ast.NotIn,
    )
    for child in ast.walk(node):
        if not isinstance(child, allowed_nodes):
            raise ValueError(f"Unsupported filter syntax: {type(child).__name__}")
        if isinstance(child, ast.Call):
            if not isinstance(child.func, ast.Name) or child.func.id not in {"contains", "regex"}:
                raise ValueError("Only contains(...) and regex(...) calls are supported in filters.")
            if child.keywords:
                raise ValueError("Filter function keyword arguments are not supported.")


def build_filter_context(record: ForumPostRecord) -> dict[str, object]:
    record_date = record_date_from_dateline(record.dateline)
    context: dict[str, object] = {
        "post_id": record.post_id,
        "target": record.target,
        "subject": record.subject or "",
        "title": record.subject or "",
        "en_subject": record.en_subject or "",
        "source": record.source or "",
        "tags": tuple(record.tags),
        "dateline": record.dateline,
        "date": record_date.isoformat() if record_date else None,
        "position_type": record.tags[3] if len(record.tags) >= 4 else "",
    }
    if record.options:
        for key, value in record.options.items():
            if isinstance(key, str) and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
                context[key] = value
    return context


def evaluate_filter_expression(expression: ast.Expression, context: dict[str, object]) -> bool:
    return bool(evaluate_filter_ast(expression.body, context))


def evaluate_filter_ast(node: ast.AST, context: dict[str, object]) -> object:
    if isinstance(node, ast.BoolOp):
        if isinstance(node.op, ast.And):
            return all(bool(evaluate_filter_ast(value, context)) for value in node.values)
        if isinstance(node.op, ast.Or):
            return any(bool(evaluate_filter_ast(value, context)) for value in node.values)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return not bool(evaluate_filter_ast(node.operand, context))
    if isinstance(node, ast.Compare):
        left = evaluate_filter_ast(node.left, context)
        for operator, comparator in zip(node.ops, node.comparators):
            right = evaluate_filter_ast(comparator, context)
            if not evaluate_comparison(left, operator, right):
                return False
            left = right
        return True
    if isinstance(node, ast.Name):
        if node.id not in context:
            raise ValueError(f"Unknown filter field: {node.id}")
        return context[node.id]
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return [evaluate_filter_ast(element, context) for element in node.elts]
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        args = [evaluate_filter_ast(arg, context) for arg in node.args]
        if node.func.id == "contains":
            if len(args) != 2:
                raise ValueError("contains(...) expects exactly two arguments.")
            return filter_contains(args[0], args[1])
        if node.func.id == "regex":
            if len(args) != 2:
                raise ValueError("regex(...) expects exactly two arguments.")
            return re.search(str(args[1]), stringify_filter_value(args[0])) is not None
    raise ValueError(f"Unsupported filter syntax: {type(node).__name__}")


def evaluate_comparison(left: object, operator: ast.cmpop, right: object) -> bool:
    if isinstance(operator, ast.Eq):
        return left == right
    if isinstance(operator, ast.NotEq):
        return left != right
    if isinstance(operator, ast.In):
        return left in right  # type: ignore[operator]
    if isinstance(operator, ast.NotIn):
        return left not in right  # type: ignore[operator]
    if isinstance(operator, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)):
        if isinstance(operator, ast.Lt):
            return left < right  # type: ignore[operator]
        if isinstance(operator, ast.LtE):
            return left <= right  # type: ignore[operator]
        if isinstance(operator, ast.Gt):
            return left > right  # type: ignore[operator]
        if isinstance(operator, ast.GtE):
            return left >= right  # type: ignore[operator]
    raise ValueError(f"Unsupported comparison operator: {type(operator).__name__}")


def filter_contains(value: object, needle: object) -> bool:
    needle_text = str(needle).lower()
    if isinstance(value, dict):
        return any(needle_text in stringify_filter_value(item).lower() for item in value.values())
    if isinstance(value, (list, tuple, set)):
        return any(needle_text in stringify_filter_value(item).lower() for item in value)
    return needle_text in stringify_filter_value(value).lower()


def stringify_filter_value(value: object) -> str:
    if value is None:
        return ""
    return str(value)


NATURAL_LANGUAGE_FILTER_STOPWORDS = {
    "a",
    "an",
    "and",
    "about",
    "all",
    "by",
    "company",
    "condition",
    "conditions",
    "filter",
    "for",
    "from",
    "include",
    "includes",
    "including",
    "interview",
    "interviews",
    "only",
    "post",
    "posts",
    "related",
    "scrape",
    "show",
    "that",
    "the",
    "to",
    "with",
}


def parse_natural_language_filter(filter_condition: str) -> list[list[str]]:
    raw_groups = re.split(r"\b(?:or|或者)\b|或", filter_condition, flags=re.IGNORECASE)
    groups: list[list[str]] = []
    for raw_group in raw_groups:
        phrases = [match.strip().lower() for match in re.findall(r'"([^"]+)"|\'([^\']+)\'', raw_group) for match in match if match.strip()]
        unquoted = re.sub(r'"[^"]+"|\'[^\']+\'', " ", raw_group)
        tokens = [
            token.lower()
            for token in re.findall(r"[A-Za-z0-9]+|[\u4e00-\u9fff]+", unquoted)
            if token.lower() not in NATURAL_LANGUAGE_FILTER_STOPWORDS
        ]
        terms = phrases + tokens
        if terms:
            groups.append(terms)
    if groups:
        return groups

    fallback = filter_condition.strip().lower()
    return [[fallback]] if fallback else []


def matches_natural_language_filter(
    record: ForumPostRecord,
    query_groups: list[list[str]],
) -> bool:
    if not query_groups:
        return True
    haystack = build_natural_language_filter_text(record)
    return any(all(term in haystack for term in group) for group in query_groups)


def build_natural_language_filter_text(record: ForumPostRecord) -> str:
    context = build_filter_context(record)
    values: list[str] = []
    for value in context.values():
        if isinstance(value, (list, tuple, set)):
            values.extend(stringify_filter_value(item) for item in value)
        else:
            values.append(stringify_filter_value(value))
    return " ".join(values).lower()


def page_contains_posts_on_or_before_date(records: list[ForumPostRecord], cutoff: date) -> bool:
    for record in records:
        record_date = record_date_from_dateline(record.dateline)
        if record_date is not None and record_date <= cutoff:
            return True
    return False


def record_date_from_dateline(dateline: int | None) -> date | None:
    if dateline is None:
        return None
    return datetime.fromtimestamp(dateline).date()


def parse_start_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"start date must use YYYY-MM-DD format: {value}") from exc


def prompt_for_start_date(company: str, default_start_date: date) -> date:
    while True:
        response = input(
            f"Start incremental scrape for {company} after {default_start_date.isoformat()}? "
            "Press Enter to accept, type YYYY-MM-DD to override, or q to abort: "
        ).strip()
        if not response:
            return default_start_date
        if response.lower() in {"q", "quit", "n", "no"}:
            print("Aborted before scraping.")
            sys.exit(1)
        try:
            return parse_start_date(response)
        except ValueError as exc:
            print(exc)


def infer_last_company_scrape_date(
    company: str,
    *,
    inputs_root: Path,
    outputs_root: Path,
) -> date:
    timestamps: list[float] = []
    input_dir = inputs_root / company
    for html_file in sorted_company_html_files(input_dir):
        timestamps.append(html_file.stat().st_mtime)

    raw_posts_dir = outputs_root / "raw_posts"
    combined_output_path = outputs_root / company / f"{company}.md"
    for post_id in extract_post_ids_from_markdown(combined_output_path):
        raw_post_path = raw_posts_dir / f"{post_id}.md"
        if raw_post_path.exists():
            timestamps.append(raw_post_path.stat().st_mtime)

    if not timestamps:
        raise FileNotFoundError(
            f"Could not infer last scrape date for {company}; pass --start-date YYYY-MM-DD."
        )
    return datetime.fromtimestamp(max(timestamps)).date()


def extract_post_ids_from_markdown(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    return sorted(set(re.findall(r'<a id="post-(\d+)"></a>', text)))


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
