# One-Pager Format

A one-pager is a single dense note that gives the reader working knowledge of a topic in 5-10 minutes. It prioritizes breadth and orientation over exhaustive depth.

## Design Principles (Inspired by Google ML Course)

1. **Visual-first**: Target ~60% visual content, 40% text. Every major concept should have a diagram, chart, or visualization.
2. **Concrete thread**: Use one recurring real-world example (like "spam classifier" in Google's ROC guide) that appears across multiple sections.
3. **Progressive complexity**: Start with simple binary cases, then introduce nuance and edge cases.
4. **Minimal formalism**: Prefer intuitive explanations over heavy mathematical notation. Use formulas sparingly and explain them in words.
5. **Short paragraphs**: Rarely exceed 2-3 sentences before a visual, list, or section break.
6. **Explanation → Visualization → Application** pattern for each major concept.

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

2-4 bullet points summarizing:
- What this is in one sentence
- Why it matters (the problem it solves)
- The key tradeoff or insight to remember

## What Is [Topic]?

**Definition in plain language** (1-2 sentences), followed immediately by a visual.

![[media/images/concept-overview.png]]

*Figure: [Caption explaining what the visual shows]*

**Concrete example**: Introduce a recurring real-world scenario (e.g., "fraud detection with 1% fraud rate", "spam classifier sorting 1M emails/day") that will appear throughout the note. Name it and refer to it consistently.

## Key Concepts / Landscape

The fundamental building blocks or competing approaches in this space.

**For mechanisms** (algorithms, architectures):
- Define each component with 1-2 sentences + formula (if needed)
- Show visual for each major component
- Use the recurring example to illustrate each concept

**For landscapes** (ecosystems, tool categories):
Use a comparison table:

| Approach | Strengths | Weaknesses | When to use |
|----------|-----------|------------|-------------|
| A | ... | ... | ... |
| B | ... | ... | ... |

## How It Works

**Progressive complexity**: Start simple, add nuance.

1. **Simple case**: Explain with minimal variables using recurring example
   - Visual showing the simple case
   - 2-3 sentences max before visual

2. **General case**: Introduce full complexity
   - Step-by-step algorithm or process (numbered list)
   - Visual showing workflow or architecture
   - Formulas if needed (with intuitive explanation)

3. **Edge cases**: What changes in extreme scenarios
   - Visual comparing normal vs edge case

**Math handling**: Use display math `$$` only for key formulas. Always follow with intuitive explanation: *"In words: this measures..."*

## When to Use [Topic]

Decision matrix or scenario-based guidance:

| Scenario | Recommendation | Reasoning |
|----------|---------------|-----------|
| Balanced data | Use ROC-AUC | ... |
| Imbalanced data | Use PR-AUC | ... |

**Reference back to recurring example** to make it concrete.

## Tradeoffs & Limitations

> [!warning] **What Breaks**
> Name the failure modes. When does this approach fall apart? What assumptions must hold?

Use comparison table for tradeoffs:

| Limitation | Impact | Mitigation |
|------------|--------|-----------|
| ... | ... | ... |

**Concrete failure scenario**: Show the recurring example hitting a failure mode (e.g., "Our spam classifier achieves ROC-AUC = 0.95 but PR-AUC = 0.20 because...").

## Common Pitfalls

Numbered list of mistakes practitioners make, each with:
1. **Pitfall name**: Brief description
   - **Problem**: What goes wrong
   - **Fix**: How to avoid it
   - **Example**: Recurring scenario showing the pitfall

## Best Practices (<YYYY-MM>)

Actionable workflow or checklist format:

**Standard workflow**:
```
1. Step one
2. Step two
3. Step three
```

Or decision tree / guideline table.

## Current State (<YYYY-MM>)

What's new, what's changing, what to watch. Date-stamp claims that will age.
Skip this section for timeless topics (e.g., graph algorithms).

## Check Your Understanding

[!tip] **Self-Assessment**
- Question 1: [Answer: ...]
- Question 2: [Answer: ...]
- Question 3: [Answer: ...]

Optional: Include if research uncovered good exercises or the topic benefits from active recall.

## Sources

### Primary References
- [Label](url) — authoritative source, comprehensive

### Deep Dives
- [Label](url) — aspect covered
- [Label](url) — aspect covered

### Examples & Case Studies
- [Label](url) — real-world application
```

## Rules

### Content Depth & Clarity
- The note should be scannable in under 10 minutes. If it takes longer, you wrote too much — cut.
- **Paragraphs**: Rarely exceed 2-3 sentences before a visual, list, table, or section break.
- **Visual ratio**: Target ~60% visual content (images, tables, charts), ~40% text.
- **Recurring example**: Choose ONE concrete real-world scenario and reference it across at least 3 different sections for consistency.
- **Progressive complexity**: Always explain simple cases before general cases, binary scenarios before nuanced edge cases.

### Structure & Formatting
- Every section earns its place. Omit sections that add no signal for this particular topic.
- **Formula handling**: Use display math `$$` sparingly (only key formulas). Always follow with *"In words: ..."* intuitive explanation.
- **Comparison tables** are strongly preferred over prose when contrasting 2+ alternatives.
- Use Obsidian callouts (`[!warning]`, `[!tip]`, `[!info]`) sparingly for high-signal warnings or tips — not for decoration.

### Visuals
- **Every major concept** should have a visual (diagram, chart, or screenshot).
- Embed images using `![[media/images/filename.png]]` with descriptive captions.
- For each visual, reference it in surrounding text: "As shown in the diagram above..." or "Figure 2 illustrates..."

### Sources
- Sources must be real URLs that were actually consulted. Do not fabricate citations.
- Annotate every source with what it's useful for.
- Organize sources by category (Primary References, Deep Dives, Examples & Case Studies).
- Frontmatter `sources` count must match the actual number of sources listed.

### File Naming
- Use kebab-case for the filename: `{topic-slug}.md`.
