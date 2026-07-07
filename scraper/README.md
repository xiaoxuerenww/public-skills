# 1Point3Acres Scraper

Scrape individual 1Point3Acres posts or build a combined company markdown file from saved company pages.

## Setup

Install the project with Poetry:

```bash
poetry install
```

Available commands:

```bash
poetry run scrape-post --help
poetry run scrape-company --help
```

Create a local `.env` file from `.env.example`, then set your logged-in cookie string:

```bash
cp .env.example .env
```

```dotenv
SCRAPER_COOKIE_HEADER="name1=value1; name2=value2; name3=value3"
```

To copy the cookie from Chrome or Edge:

1. Log into `https://www.1point3acres.com`
2. Open the page you want
3. Press `Cmd + Option + I`
4. Open `Network`
5. Refresh the page
6. Click the main document request
7. In `Headers`, copy the full `Cookie` value under `Request Headers`

Treat that cookie string like a password. Do not commit it.

## Usage

### Scrape One Post

```bash
poetry run scrape-post https://www.1point3acres.com/home/pins/1175782
```

`scrape-post` fetches the browser-facing post page URL you pass in, then saves the parsed markdown.

This saves:

```text
outputs/raw_posts/1175782.md
```

JSON output:

```bash
poetry run scrape-post https://www.1point3acres.com/home/pins/1175782 --json
```

### Scrape One Company

By default, scrape only posts newer than the last local scrape. The command infers
a start date from existing input pages and raw posts, then prompts you to confirm
or override it before making requests:

```bash
poetry run scrape-company databricks
```

Use the first `n` refreshed input pages for the default incremental scrape:

```bash
poetry run scrape-company anthropic --max-pages 3
```

Use all refreshed input pages for the default incremental scrape:

```bash
poetry run scrape-company anthropic --max-pages -1
```

Provide the proposed start date explicitly. The command still prompts you to
confirm or override it:

```bash
poetry run scrape-company databricks --start-date 2026-05-29
```

Filter the company-page records before scraping. The filter is natural language
by default and matches against fields parsed from the company list page, including
`subject`, `en_subject`, `tags`, `date`, `position_type`, and option values.

```bash
poetry run scrape-company databricks --filter-condition 'MLE or Machine Learning posts'
```

```bash
poetry run scrape-company databricks --filter-condition 'ML LLM fundamentals'
```

Use `expr:` only when you want a structured boolean filter. Structured filters
can reference `post_id`, `subject`, `en_subject`, `source`, `tags`, `date`,
`dateline`, `position_type`, and option keys such as `company`, `jobcategory`,
`jobtype`, `jobyear`, `jobseason`, and `fresh`. Supported helpers are
`contains(value, text)` and `regex(value, pattern)`.

```bash
poetry run scrape-company databricks --filter-condition 'expr:jobcategory == 12'
```

Run the old full scrape behavior without a date cutoff:

```bash
poetry run scrape-company anthropic --full-scrape
```

Use existing saved input pages in full-scrape mode:

```bash
poetry run scrape-company anthropic --full-scrape --max-pages 3
```

Fetch fresh company input pages in full-scrape mode:

```bash
poetry run scrape-company anthropic --full-scrape --refresh-inputs
```

With default incremental mode or `--refresh-inputs`, the scraper fetches the browser-facing company list pages at
`https://www.1point3acres.com/interview/company/<company>?page=<n>`
and saves the raw HTML into `inputs/<company>/`.

## Inputs And Outputs

Company input pages live under:

```text
inputs/<company>/
```

Examples:

```text
inputs/anthropic/1.html
inputs/anthropic/2.html
inputs/anthropic/3.html
```

Outputs:

```text
outputs/raw_posts/<post_id>.md
outputs/raw_images/<post_id>_<filename>
outputs/raw_attachements/<post_id>_<filename>
outputs/<company>/<company>.md
outputs/<company>/<company>_<interview_round>.md
```

Example:

```text
outputs/raw_posts/1175782.md
outputs/raw_images/1175782_example.png
outputs/raw_attachements/1175782_example.pdf
outputs/anthropic/anthropic.md
outputs/databricks/databricks_ml_llm_fundamental.md
```

## Post-Process Round Evidence

Use the `post-process-scraper-outputs` Codex skill to turn scraped raw posts into
a round-specific raw evidence file:

```text
/Users/xue/.codex/skills/post-process-scraper-outputs/SKILL.md
```

The output file is:

```text
outputs/<company>/<company>_<interview_round>.md
```

When the user asks to collect `<company> <interview topic>` questions, route the
request to this skill after confirming the relevant company output exists under
`outputs/<company>/` or the source posts exist under `outputs/raw_posts/`.

The post-processing contract is:

- group raw posts and replies by interview question or topic
- preserve raw post/reply content inside fenced `text` blocks
- do not rewrite, translate, normalize, or summarize scraped content
- link every included item to the original post

Example request:

```text
[$post-process-scraper-outputs] databricks, ml / llm fundamental
collect Harvey algorithm coding questions from the scraper output
extract OpenAI behavioral interview questions and preserve raw post content
```

Example output:

```text
outputs/databricks/databricks_ml_llm_fundamental.md
```

## Supported URLs

The scraper works with the human-facing URLs used on 1Point3Acres.

For individual posts, `scrape-post` supports:

```text
https://www.1point3acres.com/home/pins/<post_id>
https://www.1point3acres.com/bbs/thread-<post_id>-1-1.html
https://www.1point3acres.com/interview/post/<post_id>
```

Notes:

- If you pass a newer `/home/pins/<post_id>` URL and the page is only the app shell, the scraper follows the visible legacy thread link and parses that page instead.
- If you pass the legacy `/bbs/thread-<post_id>-1-1.html` URL directly, the scraper parses it directly.
- Both the new and legacy URL forms map to the same saved raw post file: `outputs/raw_posts/<post_id>.md`

For company list pages, `scrape-company --refresh-inputs` fetches browser-facing pages like:

```text
https://www.1point3acres.com/interview/company/<company>?page=1
https://www.1point3acres.com/interview/company/<company>?page=2
```

Those raw HTML pages are saved under:

```text
inputs/<company>/1.html
inputs/<company>/2.html
```

## What `scrape-company` Does

1. Optionally fetches browser-facing company pages into `inputs/<company>/`
2. Loads `inputs/<company>/1.html`, `2.html`, and so on
3. Extracts post IDs from those pages
4. Skips posts already present in `outputs/raw_posts`
5. Scrapes missing posts using the visible post page URLs from those company pages
6. Downloads discovered images and attachments
7. Rebuilds the combined markdown file

## Progress Output

Example progress:

```text
[1/30] skip 1175782: already exists
[2/30] scraping 1176000
[2/30] saved 1176000 (0 images, 0 attachments)
```

Example summary:

```text
Finished: 100 posts identified, 90 already exists, 5 newly scraped, 5 failed scraping.
```

## Safety Notes

- `scrape-company` stops early on any HTTP `403` or `429`
- live requests are rate-limited and capped per run
- using authenticated scraping can still put your account at risk

If you want the safest workflow, use this project mainly with saved local HTML files instead of repeated live scraping.
