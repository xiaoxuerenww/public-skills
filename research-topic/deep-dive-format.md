# Deep Dive Format

A deep dive produces an index note plus multiple subtopic notes. Each subtopic
note is self-contained — readable on its own — but the index provides the
breadth view and ties everything together.

## Directory Structure

```
{topic-slug}/
  index.md              — landscape overview, subtopic map, combined sources
  {subtopic-1-slug}.md  — self-contained subtopic page
  {subtopic-2-slug}.md  — self-contained subtopic page
  ...
```

## Index Note Template

```md
---
topic: <topic name>
type: research/deep-dive
created: <YYYY-MM-DD>
subtopics: <number of subtopic notes>
sources: <total unique sources across all notes>
tags:
  - <relevant-tag>
---

# <Topic Name>

## TL;DR

3-5 sentences. What this space is about, why it matters now, and the key
tensions or decisions a practitioner faces.

## Topic Map

Overview of how the subtopics relate. Use a short narrative, a numbered
list, or a simple text diagram — whichever makes the structure clearest.

### Subtopics

- [[{subtopic-1-slug}]] — one-line summary of what this covers
- [[{subtopic-2-slug}]] — one-line summary
- ...

## Landscape Summary

A dense 1-2 paragraph synthesis that a reader can use without opening any
subtopic notes. Covers the main approaches, tradeoffs, and current state.

## How to Read This

Suggested reading order or "pick your path" guidance:
- New to the topic? Start with [[subtopic-1]] then [[subtopic-2]].
- Already know the basics? Jump to [[subtopic-3]] for the current state.
- Evaluating for a project? Read [[subtopic-4]] for tradeoffs.

## All Sources

Deduplicated list of every source cited across all subtopic notes:

- [Short label](url) — annotation. Used in: [[subtopic-1]], [[subtopic-3]].
- [Short label](url) — annotation. Used in: [[subtopic-2]].
```

## Subtopic Note Template

Each subtopic note follows the one-pager format with these adjustments:

```md
---
topic: <subtopic name>
parent: "[[index]]"
type: research/deep-dive/subtopic
created: <YYYY-MM-DD>
sources: <number of sources cited in this note>
tags:
  - <relevant-tag>
---

# <Subtopic Name>

> [!info] Part of [[index|<Parent Topic Name>]]
> <One sentence placing this subtopic in the broader context.>

## TL;DR

2-3 sentences specific to this subtopic.

## <Core content sections>

Use the same section types as the one-pager format — Landscape, How It Works,
Tradeoffs, Current State — but only the ones that apply to this subtopic.
Go deeper here than a one-pager would. Include:

- Implementation details, pseudocode, or architecture sketches when useful.
- Concrete examples from real systems or papers.
- Display math for important formulas.
- Comparison tables for alternatives within this subtopic.

## Connections

How this subtopic relates to siblings:
- Builds on: [[other-subtopic]] (what prerequisite knowledge)
- Contrasts with: [[other-subtopic]] (what's different)
- Feeds into: [[other-subtopic]] (what comes next)

Omit if the subtopic is standalone.

## Sources

- [Short label](url) — annotation.
```

## Rules

- Target 3-7 subtopics. Fewer than 3 means a one-pager would have sufficed.
  More than 7 means the scope needs slicing.
- Each subtopic note should be readable in 5-10 minutes independently.
- The index note should be scannable in 3-5 minutes and give the reader
  enough orientation to decide which subtopics to read.
- Wikilinks between notes must resolve correctly. Use `[[slug]]` format
  (no extensions needed if Obsidian is configured for shortest-path).
- Every subtopic note links back to `[[index]]` via the callout at the top.
- Sources in each subtopic note are a subset of the "All Sources" list in
  the index. The index deduplicates and annotates which subtopics use each
  source.
- All filenames use kebab-case.
- All notes use Obsidian-native formatting: callouts, display math, tables,
  wikilinks.
