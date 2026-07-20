---
name: system-design-material-finder
description: Find, curate, and write high-quality learning materials into a Markdown reference index doc for a system design or ML system design interview question. Use when the user asks to find resources, learning materials, references, examples, videos, mock solutions, source links, or a research packet for a specific system design prompt, especially ML system design topics such as recommendation, search, ranking, moderation, ads, feed, retrieval, evaluation, model serving, or data pipelines.
---

# System Design Material Finder

Find interview-ready learning materials for one concrete system design question first, then add production-depth sources only after the interview walkthrough layer is covered. Write a curated Markdown reference index doc and return a short summary with the file link.

## Core workflow

Three phases. Phase 1 always runs. Phases 2 and 3 run when the user says "download," "save," "scan and download," "reindex," or gives a target directory -- or by default when the topic is broad enough to warrant a local reference collection (e.g., an entire interview domain like "agent system design" rather than a single narrow question).

---

### Phase 1: Research material

1. **Identify the target question**
   - Use the user's prompt, current note, selected text, or problem directory name.
   - Normalize it into 3 to 6 search concepts, for example `harmful content detection`, `content moderation`, `trust and safety ML`, `multi-modal classification`, `human review queue`.
   - If the target question is ambiguous, make the most likely interpretation and say the assumption briefly.

2. **Search live sources, interview-ready first**
   - Browse the web. Do not rely only on memory because resource pages, paywalls, and video availability change.
   - Start with interview-ready pages for the exact prompt, especially Hello Interview problem breakdowns like `https://www.hellointerview.com/learn/ml-system-design/problem-breakdowns/harmful-content`, Hack2Hire ML system design questions, ByteByteGo ML system design chapters, Interviewing.io mocks, Exponent mocks, and YouTube mock walkthroughs.
   - Search both exact and adjacent phrasings.
   - Prefer first-pass queries that combine the topic with `ML system design interview`, `problem breakdown`, `mock interview`, `interview question`, `real interview question`, `case study`, or `YouTube`.
   - Only after the interview-ready layer is covered, search production engineering posts, official docs, papers, and architecture case studies for Staff-level depth.

3. **Prioritize sources by interview readiness**
   - Put interview-shaped walkthroughs before production docs, even if the production docs are more technically authoritative.
   - Rank a direct Hello Interview, Hack2Hire, ByteByteGo, Interviewing.io, or high-quality mock video above a generic company blog for the same topic.
   - Use production engineering posts, official docs, papers, and architecture case studies as depth sources, not as the first starting point unless no interview-ready source exists.
   - Include YouTube only when the title/channel suggests a real walkthrough, mock interview, or high-quality explanation, not generic hype.
   - Avoid low-signal Search Engine Optimization (SEO) pages, copied content, ungrounded Medium posts, and pages with no concrete architecture or trade-offs.

4. **Curate, do not dump links**
   - Return 6 to 12 resources max unless the user asks for more.
   - Group by learning purpose: `Best starting point`, `Interview walkthroughs`, `Production depth`, `Video`, `Adjacent examples`.
   - For each resource, include link, source, why it helps, and what to extract.
   - Clearly mark paywalled, login-required, or only partially accessible resources.

5. **Write an initial reference index doc**
   - Default to writing the curated packet into a Markdown doc, not only returning it in chat.
   - If the user points to a problem directory, write to `<problem_dir>/reference/0_reference_index.md` and create `reference/` if needed.
   - If the user points to a note, write to a sibling `reference/0_reference_index.md` under that note's parent directory unless the user names a target file.
   - If the user names a target file, write there instead.
   - Use Obsidian-friendly Markdown and wikilinks for local files.
   - Do not overwrite existing curated notes. If the target file exists, append a dated section or merge surgically.
   - In the final chat response, include only a concise summary and a wikilink to the doc.

---

### Phase 2: Scan and download best sources

After Phase 1 produces a curated link list, fetch and save the most relevant documents locally so the user has durable, offline reference material.

1. **Rank sources for download**
   - From the Phase 1 results, select the top sources that are:
     - Freely accessible (skip paywalled or login-gated pages)
     - Substantive (contain architecture, patterns, trade-offs, or interview frameworks -- not just link lists)
     - Non-redundant (don't download two sources that cover the same ground)
   - Prioritize: (a) canonical frontier-lab guides (Anthropic, OpenAI engineering blogs), (b) interview-structured walkthroughs with concrete frameworks, (c) production case studies with real system details, (d) comprehensive curated lists (awesome-lists with high signal)

2. **Fetch and save each source**
   - Use WebFetch to extract the full article content.
   - Save each as a Markdown file in `<problem_dir>/reference/` using the article title as the filename (sanitized for filesystem).
   - Preserve the source URL, author, and published date in YAML frontmatter with a `clippings` tag.
   - Keep the original article structure (headings, tables, lists). Strip navigation chrome, ads, and sidebar content.
   - For very long articles, keep all substantive content but omit repeated boilerplate (footers, author bios, related-post sections).

3. **Verify downloads**
   - After all fetches, list the saved files and confirm each has substantive content (not just a 403/paywall stub).
   - Note any sources that could not be fetched so they remain as external links in the index.

---

### Phase 3: Reindex for Staff-level interview goal

After Phase 2 populates local reference files, reindex everything into a comprehensive, prioritized reference doc that is ready for Staff-level interview prep.

1. **Inventory all local materials**
   - Read every `.md` file under `<problem_dir>/reference/` (excluding the index itself).
   - For each file, extract: title, source, key topics covered, unique value (what this doc covers that others don't).

2. **Organize into priority tiers**
   - **Tier 1 (Must-read foundations)**: 2-4 documents that define the vocabulary and patterns interviewers expect. For each, write a detailed extraction guide: specific concepts, frameworks, tables, and patterns to memorize. Use wikilinks to the local file.
   - **Tier 2 (Interview depth)**: 2-4 documents that extend Tier 1 with complementary perspectives, deeper coordination patterns, or production context. Summarize key content in bullet points.
   - **Tier 3 (Staff-level production depth)**: Documents with production engineering details, real system case studies, or architectural insights that signal Staff-level thinking. Highlight specific talking points that differentiate Staff from mid-level answers.
   - **Tier 4 (Company/domain-specific)**: Documents relevant to a specific target company or product area. Summarize concisely with links.

3. **Build quick-reference cheat sheet**
   - Synthesize across all tiers into scannable tables:
     - Architecture patterns table (pattern, shape, when to use)
     - Core components table (component, what to discuss)
     - Failure modes table (failure, mitigation)
     - Interview answer structure (step-by-step framework like ORBIT or similar)
     - Staff-level differentiators (5-8 talking points that signal depth beyond basic patterns)

4. **Add reading order recommendation**
   - Suggest a phased reading plan with estimated time per phase.

5. **Write the final reindexed doc**
   - Overwrite or replace the initial reference index at `<problem_dir>/reference/0_reference_index.md`.
   - The `0_` prefix keeps it sorted first in the directory.
   - Include: frontmatter with topic/tags, all tiers with wikilinks to local files, cheat sheet, external links section (sources not downloaded), reading order.
   - Tone: concise, scannable, no filler. Every line should help the user answer an interview question or signal Staff-level depth.

## Source tiers

Read [references/source_catalog.md](source_catalog.md) when ranking or expanding the source list.

Default priority:

1. Direct interview-ready problem breakdowns: Hello Interview, Hack2Hire, ByteByteGo ML system design chapters, Interviewing.io mocks, Exponent mocks, and similar structured interview walkthroughs.
2. Interview-ready videos from credible channels, especially Hello Interview, ByteByteGo, System Design Fight Club, Exponent, MLEpath, or Staff-level mock interviews.
3. Close sibling interview prompts when the exact prompt is unavailable, for example content moderation for harmful content detection or Spark OOM troubleshooting for notebook OOM prediction.
4. Production engineering blogs from Meta, Google, Netflix, Uber, DoorDash, Pinterest, Airbnb, LinkedIn, Spotify, Discord, Cloudflare, OpenAI, Anthropic, and Databricks.
5. Official docs and platform references that provide feature, serving, observability, or operational details.
6. Papers, books, and course material for deeper ML systems concepts, especially Chip Huyen, Stanford CS329S, RecSys papers, retrieval/ranking papers, and moderation/trust-and-safety papers.
7. Community sources such as Reddit, Blind, Medium, and Substack only as secondary leads unless the author and content quality are strong.

## Search query templates

Use several of these patterns:

```text
"<question>" "ML system design interview"
"<question>" "problem breakdown"
"<question>" "mock interview"
"<question>" "real interview question"
site:hellointerview.com/learn/ml-system-design/problem-breakdowns <topic>
site:hack2hire.com/questions/ml-system-design <topic>
site:bytebytego.com <topic> "machine learning system design"
site:interviewing.io/mocks <topic> "ML"
site:youtube.com <topic> "ML system design interview"
site:youtube.com <topic> "mock interview"
<company> engineering blog <topic> recommendation ranking retrieval moderation architecture
<topic> production machine learning system architecture case study
<topic> paper ranking retrieval recommender moderation system
```

For ML system design prompts, also search component-level concepts:

```text
candidate generation ranking retrieval feature store model serving evaluation online learning
human review queue calibration active learning content moderation trust safety
embedding retrieval vector search approximate nearest neighbor ANN recommendation system
```

## Output format

### Phase 1 output (research only, no downloads)

Use this concise format when only Phase 1 runs:

```markdown
## Learning materials for <question>

### Interview-ready starting points
1. [Title](url) - Source
   - Why: <why this is useful for this question>
   - Extract: <specific sections, patterns, diagrams, or trade-offs to study>

### Additional interview walkthroughs
...

### Production depth
...

### Video
...

### Search coverage
- Searched: <short list of query families and source sites>
- Skipped: <low-signal or irrelevant source types, if useful>
```

### Phase 3 output (full reindex after downloads)

Use the tiered format when Phases 2+3 run:

```markdown
## <Topic> -- Reference Index

<One-line scope statement.>

---

## Tier 1: Must-read (interview foundations)

### 1. <Title>
> [[local-filename]] | [source](url)

**Why this is essential.** <one sentence>

Key content to internalize:
- ...

## Tier 2: Interview depth (read after Tier 1)
### N. <Title>
> [[local-filename]] | [source](url)
Key content:
- ...

## Tier 3: Staff-level production depth
...

## Tier 4: Company/domain-specific
...

## Quick-reference cheat sheet
<tables: patterns, components, failure modes, answer structure, staff differentiators>

## External resources (no local copy)
- [Title](url) -- source, one-line description

## Reading order recommendation
| Phase | What to read | Time |
```

## Quality bar

A good final packet should help the user answer the interview question, not just learn the topic. It should lead with interview-ready materials whenever they exist, then add depth sources. Prefer resources that contain at least one of:

- Problem framing and clarifying questions.
- Requirements and scale assumptions.
- Data/model/serving architecture.
- Evaluation, metrics, and trade-offs.
- Failure modes, monitoring, abuse, privacy, or safety concerns.
- Staff-level depth that can become talking points.

## the user-specific defaults

- Favor interview-ready ML system design walkthroughs over generic backend system design or raw production docs.
- Favor frontier-lab-relevant topics: LLM systems, recommendation, ranking, retrieval, evaluation, model serving, data pipelines, safety, and agentic workflows.
- Write the reference search results into `reference_index.md` by default, and keep the output concise, scannable, and durable.
- Expand abbreviations on first use, for example `Approximate Nearest Neighbor (ANN)` before `ANN`.
- Avoid em dashes.
