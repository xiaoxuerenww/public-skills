---
name: tidy-doc
description: Tidy and reorganize existing Markdown, text, or note-style documents while preserving the original content. Use when the user asks to clean up, regroup, deduplicate, reorder, or structure a document without rewriting it, migrate scratch notes into canonical files, consolidate learn_notes.md into deep_dive.md, or clean up source buffers. Supports three modes: standard tidy (single doc), consolidation (two docs), and migration (scratch → canonical with cleanup).
---

# Tidy Doc

## Purpose

Reorganize documents into clearer study or reference structures without
changing the substance. Preserve the user's content, wording, examples, and
technical claims unless a small connective heading or label is needed.

Supports three modes:
1. **Standard Tidy** — Reorganize a single document
2. **Consolidation** — Merge content from source into target, clean up source
3. **Migration** — Migrate scratch notes (learn_notes.md) into canonical notes (deep_dive.md) with full cleanup

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

### Migration Mode (Scratch → Canonical with Full Cleanup)

When the user asks to migrate, merge, or clean scratch notes (e.g., `learn_notes.md`) into canonical notes (e.g., `deep_dive.md`):

**Triggers:** "migrate learn_notes", "clean up learn_notes", "consolidate notes", "merge companion notes"

**Default pattern:** `<topic>/learn_notes.md` → `<topic>/deep_dive.md`

1. **Locate files:**
   - Infer from current note, `@file` references, or ask user
   - Use relative paths inside Obsidian vaults

2. **Read both files:**
   - Treat `deep_dive.md` as canonical (preserve structure, high-value content)
   - Treat `learn_notes.md` as scratch (Q&A, companion notes, incremental material)
   - Preserve existing headings, callouts, equations, links, examples

3. **Build topic map:**
   - Extract unique concepts from `learn_notes.md`
   - Map each to existing or new section in `deep_dive.md`
   - Order sections basic → advanced (see structure guide below)

4. **Merge into canonical:**
   - Patch `deep_dive.md` in place
   - Merge content into most relevant sections
   - Deduplicate repeated explanations
   - Synthesize Q&A into concise explanations (unless target uses Q&A format)
   - Keep Obsidian style: wikilinks, concise tables, callouts
   - Expand abbreviations on first use

5. **Apply tidy rules:**
   - Regroup related topics (basic before follow-ups)
   - Deduplicate overlapping sections
   - Order basic → advanced throughout

6. **Clean up scratch file:**
   - Replace migrated content with status stub and migration map:
     ```markdown
     # Learn Notes - <Topic>
     
     **Status**: Migrated into [[path/to/deep_dive]] on YYYY-MM-DD.
     
     This file is now a lightweight companion-mode buffer. Durable notes were regrouped into [[path/to/deep_dive]] from basic to advanced topics, with duplicate explanations removed.
     
     ## Migration map
     
     | Original learn note topic | Durable destination |
     |---|---|
     | <topic> | [[path/to/deep_dive#section]] |
     
     ## New notes buffer
     ```
   - Keep "New notes buffer" section for future companion-mode notes
   - Do NOT delete the file unless user explicitly asks

7. **Verify:**
   - All source topics have destinations
   - Canonical file flows basic → advanced
   - Duplicates were merged (not copied twice)
   - Obsidian links and headings are valid

**Suggested canonical structure (adapt to existing note):**
1. Core mental model and notation
2. Fundamental mechanism or formula
3. Shape flow or implementation details
4. Major subcomponents and division of labor
5. Variants and architecture families
6. Training or optimization stability
7. Inference, serving, latency, memory, or cost
8. Long-context or advanced tradeoffs
9. Debugging and reliability
10. Common wrong answers or interview phrasing
11. Source list or migration notes

**Optional suggestions (low-noise only):**
- Add interview-ready answer section if deep dive is too reference-heavy
- Add source list if mixing local sources and learn-mode Q&A
- Add common-wrong-answers table for mock-interview prep
- Add migration map for future learn notes

Do not perform extra restructuring beyond the user's request unless necessary to complete migration safely.

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
- **Equation annotations:** When an equation appears for the first time in the document:
  - Add inline annotations explaining variables and terms if not already present
  - Use format: `where X = explanation, Y = explanation`
  - Only annotate on first occurrence (skip subsequent uses of the same equation)
  - Keep annotations concise and in the user's voice
  - Example: `Loss = -log(p(correct))` becomes `Loss = -log(p(correct))` where `p(correct)` is the probability of the correct token
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

### Migration Mode

Before finishing:

- Verify all source topics from scratch file have destinations in canonical
- Verify canonical file flows basic → advanced
- Verify duplicates were merged (not copied twice)
- Verify scratch file has migration stub with status and map
- Verify Obsidian links are valid
- Report:
  - Migration map showing source topics → canonical sections
  - Path to canonical file
  - Path to cleaned scratch file
