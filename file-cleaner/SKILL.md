---
name: file-cleaner
description: Consolidate scratch Markdown notes into durable canonical notes and clean up source buffers. Use when the user asks to migrate, merge, consolidate, regroup, deduplicate, or clean files such as topic learn_notes.md files into matching deep_dive.md files, especially in Obsidian interview-prep vaults where `learn_notes.md` is a companion-mode buffer and `deep_dive.md` is the canonical study note.
---

# File Cleaner

## Core workflow

1. Locate the source and destination files.
   - Default pattern: `<topic>/learn_notes.md` -> `<topic>/deep_dive.md`.
   - If paths are ambiguous, infer from the current note or named `@file` references before asking.
   - Use relative paths inside an Obsidian vault.

2. Read both files fully enough to understand structure.
   - Treat `deep_dive.md` as canonical unless the user says otherwise.
   - Treat `learn_notes.md` as scratch, Q&A, companion notes, or incremental learn-mode material.
   - Preserve existing high-value headings, callouts, equations, links, examples, and interview phrasing.

3. Build a topic map before editing.
   - Extract unique concepts from `learn_notes.md`.
   - Map each concept to an existing or new section in `deep_dive.md`.
   - Order sections from basic to advanced: mental model -> mechanics -> implementation/shapes -> variants -> serving/cost -> debugging/reliability -> interview phrasing/source list.

4. Patch `deep_dive.md` in place.
   - Merge source content into the most relevant durable section.
   - Deduplicate repeated explanations instead of appending raw notes at the end.
   - Prefer concise synthesis over preserving Q&A format unless Q&A is the destination style.
   - Keep the user's Obsidian style: Markdown-native, wikilinks, concise tables, callouts when useful.
   - Expand abbreviations on first use, then use the abbreviation.
   - Avoid em dashes.

5. Invoke `$tidy-doc` on the patched destination file when the cleanup includes
   regrouping, deduplication, or ordering topics.
   - Use `$tidy-doc` to preserve content while regrouping related topics.
   - Ensure basic material appears before follow-ups and advanced material.
   - Remove duplicate topics by merging details, not dropping distinct content.
   - Keep the destination file as the edited artifact; do not create a separate
     tidy copy unless the user asks.

6. Clean `learn_notes.md` after a successful merge.
   - Replace migrated content with a lightweight status stub and migration map.
   - Keep a `New notes buffer` section for future companion-mode notes.
   - Do not delete the file unless the user explicitly asks.

7. Verify the result.
   - Re-read changed files or inspect the diff.
   - Check that all source topics from `learn_notes.md` have a destination.
   - Check that `deep_dive.md` flows from basic to advanced.
   - Check that duplicate sections were collapsed rather than copied twice.
   - Check Obsidian links and headings are reasonable.

## Suggested destination structure

Use this order as a default, adapting to the existing note:

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

## Learn notes cleanup stub

After migration, rewrite `learn_notes.md` roughly like this:

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

## Optional improvements to suggest

After the requested cleanup, suggest only improvements that are directly useful and low-noise, for example:

- Add a short interview-ready answer section if the deep dive is too reference-heavy.
- Add a source list if the note mixes local sources and learn-mode Q&A.
- Add a common-wrong-answers table for mock-interview prep.
- Split an overly long deep dive only if it hurts usability.
- Add a migration map when future learn notes will continue accumulating.

Do not perform extra restructuring beyond the user's request unless it is necessary to complete the consolidation safely.
