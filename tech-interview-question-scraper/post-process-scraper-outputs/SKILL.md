---
name: post-process-scraper-outputs
description: Post-process local scraper outputs into company-and-round evidence files. Use when the user asks to extract raw comments, posts, replies, or interview questions from scraper output for any company and any interview round, group the raw evidence by question, preserve original wording without rewriting or summarizing, and link each item back to the original post. Produces files named with the company slug and interview round.
---

# Post Process Scraper Outputs

## Purpose

Create a raw evidence document from scraper outputs for one company and one interview round.

The output contract is strict:

- Write `outputs/<company>/<company>_<interview_round>.md` by default.
- Group evidence by question or topic asked in that interview round.
- Preserve raw post/reply content exactly inside fenced `text` blocks.
- Link every included item to the original post.
- Do not rewrite, translate, normalize, or summarize scraped content.

## Workflow

1. Resolve parameters:
   - `company`: use the company slug from the user request or existing `outputs/<company>/` folder.
   - `interview_round`: use the user's round phrase, such as `ml fundamental`, `system design`, `coding`, `behavioral`, or `hiring manager`.
   - Output filename: lowercase, replace non-alphanumeric runs with `_`, then write `<company>_<interview_round>.md`.
2. Locate sources:
   - Prefer `outputs/<company>/<company>.md` as the company index if present.
   - Read relevant `outputs/raw_posts/*.md` files directly for raw content.
   - If an existing round summary exists, use it only as a locator for post IDs, not as source wording.
3. Gather candidate evidence:
   - Run `scripts/extract_round_candidates.py` to get likely raw post/reply blocks.
   - Use `rg` over `outputs/raw_posts/` for additional round-specific synonyms.
   - Include both direct interview questions and replies that clarify the round format or exact question.
4. Group by question:
   - Create one `## <Question Or Topic>` section per distinct question.
   - Use concise headings to organize evidence; headings may be normalized, but fenced scraped content must remain raw.
   - If the evidence only describes round format, use a heading like `## Round Format`.
5. Write each source item:
   - Use a source subheading with post ID and original URL.
   - Put raw content in a fenced `text` block.
   - Include reply headers when the reply metadata matters.
6. Verify:
   - Re-open the output and compare included text against the raw post file before finalizing.
   - Run `rg -n "<key phrase>" outputs/raw_posts/<post_id>.md` for several included phrases.
   - Confirm every source item has an original post URL.

## Candidate Extraction

Use the helper from the scraper repo root:

```bash
python3 /Users/xue/.codex/skills/post-process-scraper-outputs/scripts/extract_round_candidates.py \
  --scraper-root /Users/xue/.codex/skills/scraper \
  --company <company> \
  --round "<interview_round>"
```

Optional flags:

- `--keywords "term one,term two"` adds synonyms when the round name is too broad or too narrow.
- `--post-id 123 --post-id 456` restricts extraction to known post IDs.
- `--limit 80` changes the number of candidate blocks printed.

Treat the helper output as candidate evidence only. It ranks text blocks by lexical matches; the final file still requires manual judgment and raw-text verification.

## Output Template

```markdown
# <Company> <Interview Round> Raw Comments By Question

Source corpus: local scrape under `outputs/raw_posts/`.

Rule: raw post/reply content is preserved. No rewriting or summarization inside quoted blocks.

## <Question Or Topic>

### Source: `<post_id>`

Original post: <url>

```text
<raw post or reply content copied exactly>
```
```

If a single post contains multiple relevant questions, repeat the same source under each question with the exact raw block that supports that group.

## Guardrails

- Do not paraphrase raw content.
- Do not translate Chinese or mixed-language content.
- Do not merge multiple comments into one rewritten paragraph.
- Do not infer that a post belongs to a round unless the raw text supports it.
- Do not use scraped summaries as evidence text; only use raw post/reply files for final quoted blocks.
- Keep unrelated git changes untouched.
