---
name: tidy-doc
description: Tidy and reorganize existing Markdown, text, or note-style documents while preserving the original content. Use when the user asks to clean up, regroup, deduplicate, reorder, or structure a document without rewriting it, especially to group related topics as basic-to-follow-up progressions, remove duplicate topics, and order material from basic to advanced.
---

# Tidy Doc

## Purpose

Reorganize a document into a clearer study or reference structure without
changing the substance. Preserve the user's content, wording, examples, and
technical claims unless a small connective heading or label is needed.

## Workflow

1. Read the target document before editing.
2. Identify the unit of organization: headings, questions, bullets, sections,
   cards, or paragraphs.
3. Cluster related material by topic.
4. Within each topic, order material from basic to advanced:
   - basic definitions or intuitions
   - core mechanisms or formulas
   - implementation details or examples
   - follow-up questions, edge cases, comparisons, or failure modes
   - advanced extensions or interview probes
5. Remove duplicate topics by merging overlapping sections into the clearest
   existing location.
6. Preserve all non-duplicate content. If two duplicate sections contain
   different details, merge the details instead of deleting them.
7. Patch the original file in place unless the user asks for a separate output.

## Editing Rules

- Preserve original wording as much as possible.
- Do not summarize away details.
- Do not add new technical content unless the user asks.
- Do not change facts, equations, code, examples, or citations.
- Do not flatten useful hierarchy. Prefer topic -> basic -> follow-up.
- Do not over-format. Use the document's existing heading depth, bullets, and
  style.
- Keep links, wikilinks, images, code blocks, tables, and citations attached to
  the relevant topic.
- If duplicate content conflicts, keep both claims and mark the conflict with a
  short `TODO: reconcile` note instead of silently choosing one.

## Output Shape

For study or interview-prep docs, prefer this structure when it fits:

```markdown
## <Topic>

### Basics

### Core Mechanism

### Follow-ups

### Advanced / Edge Cases
```

Use lighter headings when the source file is short. If the source already has a
good custom structure, preserve it and only move content within it.

## Verification

Before finishing:

- Check that every original non-duplicate topic still appears.
- Check that duplicate topics were merged, not lost.
- Check that basic material appears before follow-ups and advanced material.
- Report the edited file and the main reorganization decisions.
