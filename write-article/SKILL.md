---
name: write-article
description: Capture thoughts, learnings, or observations and accumulate them into topic-based articles. Use when the user shares a thought, learning, observation, idea, or snippet they want to save, or asks to draft, outline, write, or revise an article. Also use when the user asks to review or publish an article.
---

# Write Article

Accumulate random thoughts and learnings into evolving articles. Each invocation either routes a new thought to the right article or works on an article directly.

Articles live in `write-article/articles/<topic>.md`. The index lives at `write-article/articles/INDEX.md`.

## Branches

Detect the branch from the user's input:

- **Capture** (default) — user shares a thought, learning, or observation. Route it to the best-matching article.
- **Draft** — user asks to turn accumulated notes into a polished article.
- **Revise** — user asks to tighten or edit an existing article.
- **Review** — user asks to see what articles exist or check status.
- **Publish** — user asks to publish an article to GitHub Pages.

## Capture Branch

This is the core workflow. The user drops a thought; you file it.

1. **Read INDEX.md** to see all existing articles and topics. If INDEX.md doesn't exist, create it (see Index Format below).
2. **Match the thought.** Score each existing article by relevance to the user's input. Consider: topic overlap, shared concepts, thematic fit.
3. **Present the match.** Tell the user:
   - The best-matching article (with a one-line reason why it fits).
   - 1-2 runner-up articles if close.
   - Offer to create a new article if nothing fits well.
   - Let the user confirm, pick a different article, or name a new topic.
4. **Wait for confirmation.** Do not append until the user confirms or specifies.
5. **Append the thought.** Add to the article file under a dated entry:
   - If the file doesn't exist, create it with frontmatter and the first entry.
   - If it exists, append under a new dated heading or the current date's section.
   - Preserve the user's voice. Light editing for clarity only, no rewriting.
6. **Update INDEX.md** — add the article if new, update the last-modified date.

### Article File Format

```markdown
---
topic: <topic name>
status: draft
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
---

# <Topic Name>

## <YYYY-MM-DD>

- <thought or learning, lightly edited for clarity>

## <earlier date>

- <previous entries>
```

### Index Format

```markdown
# Article Index

| Topic | File | Status | Created | Last Modified |
|-------|------|--------|---------|---------------|
| <name> | [[<topic>.md]] | draft | YYYY-MM-DD | YYYY-MM-DD |
```

Status values: `draft` (accumulating notes), `completed` (polished article), `published`.

## Draft Branch

Turn accumulated notes into a polished article.

1. Read the target article file — all the captured thoughts.
2. Identify the through-line: what story do these fragments tell together?
3. Build the arc:
   - **Problem** — what's broken, missing, or misunderstood.
   - **Constraints** — what made it hard.
   - **Approach** — what was tried, including dead ends.
   - **Solution** — what worked and why.
   - **Result** — measurable outcome or takeaway.
4. Draft following the style rules below. Preserve the user's original insights and voice.
5. Write the polished article to the same file (keep raw notes in a collapsed section at the bottom).
6. Update INDEX.md status to `completed`.

## Revise Branch

Tighten an existing article against the style rules and editing checklist below. Update INDEX.md if status changes.

## Review Branch

Read and present INDEX.md contents. Summarize article count by status, suggest which drafts have enough material to polish.

## Publish Branch

Publish a completed article to GitHub Pages.

**Prerequisites**: A GitHub Pages repository must exist. Typical setup:
- Repo named `<username>.github.io` OR any repo with GitHub Pages enabled
- Jekyll-based (GitHub Pages default) or static HTML

**Workflow**:

1. **Check article status** — read the target article and INDEX.md. Only publish articles with status `completed`. If status is `draft`, suggest running Draft mode first.

2. **Check for publish config** — look for `write-article/publish-config.json`:
   ```json
   {
     "repo_path": "/path/to/username.github.io",
     "posts_dir": "_posts",
     "default_layout": "post",
     "default_categories": ["articles"]
   }
   ```
   
   If missing, prompt the user to create it or provide:
   - Path to their GitHub Pages repo
   - Posts directory (default: `_posts` for Jekyll, or root for simple HTML)
   - Layout preference (Jekyll: `post`, `page`, or custom)

3. **Convert to Jekyll post format**:
   - Filename: `YYYY-MM-DD-<slug>.md` where slug is kebab-case topic name
   - Add Jekyll frontmatter:
     ```yaml
     ---
     layout: post
     title: "<Article Title>"
     date: <article created date or last_modified>
     categories: [<inferred from topic>]
     ---
     ```
   - Strip internal article metadata (status, topic field)
   - Keep article content (exclude raw notes section if collapsed)

4. **Write to GitHub Pages repo**:
   - Write formatted post to `<repo_path>/<posts_dir>/<filename>.md`
   - Create the file if new, or confirm overwrite if it exists

5. **Update INDEX.md**:
   - Set status to `published`
   - Add `published_date` field
   - Add `published_url` field (construct from repo URL + post slug)

6. **Prompt for git commit**:
   - Show the file path created
   - Suggest commit message: `"Publish: <article title>"`
   - Ask user if they want Claude to commit and push, or handle manually
   - If yes:
     ```bash
     cd <repo_path>
     git add <posts_dir>/<filename>.md
     git commit -m "Publish: <article title>"
     git push origin main
     ```

7. **Confirm publication**:
   - Show the expected URL: `https://<username>.github.io/<slug>/` (Jekyll) or repo-specific URL
   - Note: "GitHub Pages may take 1-2 minutes to rebuild and deploy"

**Example**:

User says: "publish the attention mechanisms article"

1. Read `articles/attention-mechanisms.md` (status: `completed`)
2. Read `publish-config.json` → repo: `/Users/xue/dev/xue-wang.github.io`
3. Convert to Jekyll post:
   - File: `2026-07-20-attention-mechanisms.md`
   - Frontmatter:
     ```yaml
     ---
     layout: post
     title: "Understanding Attention Mechanisms"
     date: 2026-07-20
     categories: [ml, transformers]
     ---
     ```
4. Write to `/Users/xue/dev/xue-wang.github.io/_posts/2026-07-20-attention-mechanisms.md`
5. Update INDEX.md:
   - Status: `published`
   - Published: `2026-07-20`
   - URL: `https://xue-wang.github.io/attention-mechanisms/`
6. Ask: "Article written to GitHub Pages repo. Commit and push now?"
7. If yes, run git commands and confirm publication

**Error handling**:
- If repo path doesn't exist → ask user to create/clone the GitHub Pages repo first
- If article not completed → suggest Draft mode
- If post file exists → confirm overwrite (default: yes with timestamp in commit message)
- If git push fails → show error, suggest manual resolution

## Style Rules

**Sentences**
- One idea per sentence. One theme per paragraph.
- Short sentences create pace. Long ones slow down. Alternate deliberately.
- Active voice. Kill filler: "basically," "simply," "just," "obviously," "in order to."

**Opening**
- First paragraph answers: "Why should I keep reading?"
- No throat-clearing. Start with the thing.

**Technical content**
- Concrete before abstract. Example first, principle after.
- Name the "why" behind every decision.
- Minimal code examples. Annotate non-obvious lines only.
- Show before/after or failure/fix.

**Voice**
- Write like you talk, then edit out the filler.
- No hedging. Commit to what you're saying.

## Editing Checklist

- [ ] Opening states what the reader walks away with.
- [ ] Every paragraph advances the arc.
- [ ] No sentence requires re-reading.
- [ ] No filler words survive.
- [ ] Every "what" has a "why."
- [ ] Read it as someone with 3 minutes. Does it land?
