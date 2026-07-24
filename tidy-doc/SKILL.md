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

### Standard Tidy (Single Document)

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

### Consolidation Mode (Two Documents)

When the user asks to consolidate `source.md` into `target.md`:

1. Read both source and target documents.
2. Identify content in source that belongs in target:
   - Core concepts, formulas, comparisons that match target's scope
   - Remove implementation-specific Q&A, session notes, or tangential content
3. Find the best location in target for each piece of source content:
   - Insert into existing sections where topics overlap
   - Add new sections if source covers topics not in target
4. Merge source content into target using standard tidy rules (basic → advanced).
5. **Clean up source document after consolidation:**
   - Remove content that was moved to target
   - Keep only content unique to source (e.g., implementation details, session-specific Q&A)
   - Add a note at the top indicating where content was consolidated:
     ```markdown
     **Note:** Most conceptual content has been consolidated into:
     - [[target.md]] — [topic areas moved]
     
     This file retains [what remains].
     ```
6. Report what was moved, what was kept in source, and where it went in target.

## Editing Rules

- Preserve original wording as much as possible.
- Do not summarize away details.
- Do not add new technical content unless the user asks.
- Do not change facts, equations, code, examples, or citations.
- Do not flatten useful hierarchy. Prefer topic -> basic -> follow-up.
- **Formatting improvements (when applicable):** Apply `$doc-formatter` conventions to improve scannability:
  - Convert bullet-list comparisons to comparison tables
  - Convert bullet-list tradeoffs to tables with clear columns
  - Use **bold** for key terms and decisions
  - Keep the document's existing heading depth and style otherwise
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

### Standard Tidy

Before finishing:

- Check that every original non-duplicate topic still appears.
- Check that duplicate topics were merged, not lost.
- Check that basic material appears before follow-ups and advanced material.
- Report the edited file and the main reorganization decisions.

### Consolidation Mode

Before finishing:

- Verify all conceptual content from source appears in target.
- Verify source document was cleaned up (duplicates removed).
- Verify source has a note pointing to where content was consolidated.
- Report:
  - What was moved to target and where
  - What was kept in source and why
  - Both file paths for verification
