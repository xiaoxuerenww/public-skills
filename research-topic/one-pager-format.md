# One-Pager Format

A one-pager is a single dense note that gives the reader working knowledge of a topic in 5-10 minutes. It prioritizes breadth and orientation over exhaustive depth.

## Template

```md
---
topic: <topic name>
type: research/one-pager
created: <YYYY-MM-DD>
sources: <number of sources cited>
tags:
  - <relevant-tag>
---

# <Topic Name>

## TL;DR

2-3 sentences. What this is, why it matters, and the one thing to remember.

## Landscape

The key concepts, players, approaches, or components that make up this space.
Dense bullets or a short narrative. If there are natural alternatives or
competing approaches, use a comparison table:

| Approach | Strengths | Weaknesses | When to use |
|----------|-----------|------------|-------------|
| A | ... | ... | ... |
| B | ... | ... | ... |

## How It Works

Core mechanics, architecture, algorithm, or workflow. Be precise but concise.
Use numbered steps for processes, diagrams-as-text for architectures, and
display math `$$` for formulas that matter.

Omit this section if the topic is a landscape/ecosystem rather than a
mechanism.

## Tradeoffs & Failure Modes

> [!warning] What breaks
> Name the real tensions. When does this approach fail? What do practitioners
> complain about? What looks good on paper but falls apart in practice?

## Current State (<YYYY-MM>)

What's new, what's changing, what to watch. Date-stamp claims that will age.
Skip this section for timeless topics (e.g., graph algorithms).

## Open Questions

Things the research didn't fully resolve, or areas where experts disagree.
Omit if nothing is genuinely unresolved.

## Sources

- [Short label](url) — one-line annotation: what it covers, why trustworthy.
- [Short label](url) — ...
```

## Rules

- The note should be scannable in under 10 minutes. If it takes longer, you wrote too much — cut.
- Every section earns its place. Omit sections that add no signal for this particular topic.
- Use Obsidian callouts sparingly for high-signal warnings or tips — not for decoration.
- Comparison tables are strongly preferred over prose when contrasting 2+ alternatives.
- Sources must be real URLs that were actually consulted. Do not fabricate citations. Annotate every source with what it's useful for.
- Frontmatter `sources` count must match the actual number of sources listed.
- Use kebab-case for the filename: `{topic-slug}.md`.
