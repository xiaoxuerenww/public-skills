---
name: system-design-material-finder
description: Find, curate, and write high-quality learning materials into a Markdown reference index doc for a system design or ML system design interview question. Use when the user asks to find resources, learning materials, references, examples, videos, mock solutions, source links, or a research packet for a specific system design prompt, especially ML system design topics such as recommendation, search, ranking, moderation, ads, feed, retrieval, evaluation, model serving, or data pipelines.
---

# System Design Material Finder

Find strong learning materials for one concrete system design question, then write a curated Markdown reference index doc and return a short summary with the file link.

## Core workflow

1. **Identify the target question**
   - Use the user's prompt, current note, selected text, or problem directory name.
   - Normalize it into 3 to 6 search concepts, for example `harmful content detection`, `content moderation`, `trust and safety ML`, `multi-modal classification`, `human review queue`.
   - If the target question is ambiguous, make the most likely interpretation and say the assumption briefly.

2. **Search live sources**
   - Browse the web. Do not rely only on memory because resource pages, paywalls, and video availability change.
   - Search both exact and adjacent phrasings.
   - Prefer queries that combine the topic with `system design`, `ML system design`, `interview`, `architecture`, `case study`, `paper`, or `YouTube`.

3. **Prioritize sources by usefulness**
   - Prefer interview-shaped walkthroughs for first-pass learning.
   - Add production engineering posts, papers, or docs when they improve depth.
   - Include YouTube only when the title/channel suggests a real walkthrough, mock interview, or high-quality explanation, not generic hype.
   - Avoid low-signal SEO pages, copied content, ungrounded Medium posts, and pages with no concrete architecture or trade-offs.

4. **Curate, do not dump links**
   - Return 6 to 12 resources max unless the user asks for more.
   - Group by learning purpose: `Best starting point`, `Interview walkthroughs`, `Production depth`, `Video`, `Adjacent examples`.
   - For each resource, include link, source, why it helps, and what to extract.
   - Clearly mark paywalled, login-required, or only partially accessible resources.

5. **Write the reference index doc**
   - Default to writing the curated packet into a Markdown doc, not only returning it in chat.
   - If the user points to a problem directory, write to `<problem_dir>/reference/reference_index.md` and create `reference/` if needed.
   - If the user points to a note, write to a sibling `reference/reference_index.md` under that note's parent directory unless the user names a target file.
   - If the user names a target file, write there instead.
   - Do not create `reference/learning_materials.md` by default.
   - Use Obsidian-friendly Markdown and wikilinks for local files.
   - Do not overwrite existing curated notes. If the target file exists, append a dated section or merge surgically.
   - In the final chat response, include only a concise summary and a wikilink to the doc.

## Source tiers

Read [references/source_catalog.md](references/source_catalog.md) when ranking or expanding the source list.

Default priority:

1. Hello Interview and Hack2Hire for interview-shaped ML system design examples.
2. ByteByteGo for general system design patterns and some ML system design chapters.
3. YouTube walkthroughs from credible channels, especially Hello Interview, ByteByteGo, System Design Fight Club, Exponent, MLEpath, or staff-engineer mock interviews.
4. Production engineering blogs from Meta, Google, Netflix, Uber, DoorDash, Pinterest, Airbnb, LinkedIn, Spotify, Discord, Cloudflare, OpenAI, Anthropic, and Databricks.
5. Papers, books, and course material for deeper ML systems concepts, especially Chip Huyen, Stanford CS329S, RecSys papers, retrieval/ranking papers, and moderation/trust-and-safety papers.
6. Community sources such as Reddit, Blind, Medium, and Substack only as secondary leads unless the author and content quality are strong.

## Search query templates

Use several of these patterns:

```text
"<question>" "ML system design"
"<question>" "system design interview"
site:hellointerview.com <topic> "system design"
site:hack2hire.com/questions/ml-system-design <topic>
site:bytebytego.com <topic> "machine learning system design"
site:youtube.com <topic> "ML system design interview"
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

Use this concise format for the Markdown doc unless the user requests a different artifact:

```markdown
## Learning materials for <question>

### Best starting point
1. [Title](url) - Source
   - Why: <why this is useful for this question>
   - Extract: <specific sections, patterns, diagrams, or trade-offs to study>

### Interview walkthroughs
...

### Production depth
...

### Video
...

### Search coverage
- Searched: <short list of query families and source sites>
- Skipped: <low-signal or irrelevant source types, if useful>
```

## Quality bar

A good final packet should help the user answer the interview question, not just learn the topic. Prefer resources that contain at least one of:

- Problem framing and clarifying questions.
- Requirements and scale assumptions.
- Data/model/serving architecture.
- Evaluation, metrics, and trade-offs.
- Failure modes, monitoring, abuse, privacy, or safety concerns.
- Staff-level depth that can become talking points.

## Julie-specific defaults

- Favor ML system design over generic backend system design.
- Favor frontier-lab-relevant topics: LLM systems, recommendation, ranking, retrieval, evaluation, model serving, data pipelines, safety, and agentic workflows.
- Write the reference search results into `reference_index.md` by default, and keep the output concise, scannable, and durable.
- Expand abbreviations on first use, for example `Approximate Nearest Neighbor (ANN)` before `ANN`.
- Avoid em dashes.
