---
name: tidy-dir
description: "Reorganize files and folders under a directory into a coherent structure. Use when the user asks to reorganize, restructure, sort, or clean up a folder of notes, documents, or files — especially when files need moving, merging, splitting, renaming, or grouping by topic."
argument-hint: "Which directory to reorganize?"
---

Reorganize files under a directory into a coherent topic structure. This is not single-file tidying (use `tidy-doc` for that) — this skill rearranges **files and folders** across a directory tree.

## Step 1: Inventory

Read every file in the target directory (recursively if needed). For each file, note:

- Filename and path.
- Primary topic(s) — from headings, frontmatter, or content scan.
- Approximate weight — light (a few bullets or a stub), medium (a focused note), heavy (a long reference doc covering multiple subtopics).
- Incoming wikilinks — which other files in the directory link to this file.

Completion criterion: every file in the directory is catalogued with topic and weight. No file is skipped.

## Step 2: Plan

Propose a reorganization plan. Present it to the user before executing. The plan includes:

1. **Topic clusters** — group files by topic. Name each cluster.
2. **File actions** — for each file, one of:
   - **Keep** — stays where it is, unchanged.
   - **Move** — relocate to a different folder. State the destination.
   - **Rename** — new filename. State old and new names.
   - **Merge** — combine into another file. State the target. Use when two or more files cover the same topic and are individually light enough that a single note is cleaner.
   - **Split** — break a heavy file covering multiple distinct topics into separate files. State the new files and which content goes where.
3. **New folders** — any directories to create.
4. **Link updates** — wikilinks that will break and how they'll be fixed.

### Content preservation rules

- **Remove only true duplicates.** If the same information appears in two files verbatim or near-verbatim, keep the better version and remove the copy. If two files cover the same topic but with different details, **merge the details** — do not discard either.
- **Do not trim aggressively.** Preserve all non-duplicate content. Do not summarize, condense, or cut material for brevity. The goal is reorganization, not reduction.
- **Merge or split by weight and topic relevance.** A light stub on the same topic as another note should merge into it. A heavy file spanning unrelated topics should split. Medium files on a focused topic stay as-is.

### Merge/split decision guide

| Situation | Action |
|---|---|
| Two light files, same topic | Merge into one |
| Light file + medium/heavy file, same topic | Merge the light into the heavier one |
| Heavy file, multiple unrelated topics | Split into separate files per topic |
| Heavy file, one coherent topic | Keep as-is |
| Medium file, focused topic | Keep as-is |

Wait for the user to approve, adjust, or reject the plan before proceeding.

## Step 3: Execute

Apply the approved plan:

1. Create new directories if needed.
2. Move and rename files.
3. Merge files: combine content into the target file, preserving all non-duplicate material. After merging, invoke `tidy-doc` on the merged file to reorder and deduplicate within it.
4. Split files: create new files, move the relevant content into each, and leave nothing behind in the original. After splitting, invoke `tidy-doc` on each resulting file to clean up internal structure.
5. Update all wikilinks across the directory so nothing breaks. Check every file that was catalogued in Step 1.

Completion criterion: every action in the approved plan is applied. No wikilink in the directory points to a moved/renamed file's old path.

## Step 4: Index

Generate an `index.md` in the target directory root that reflects the final structure.

### Index format

```md
---
type: directory-index
created: <YYYY-MM-DD>
scope: <directory name>
---

# <Directory Name>

<1-3 sentence description of what this directory contains and how it's organized.>

## Structure

### <Cluster Name>

- [ ] [[path/to/file-1]] — one-line summary
- [ ] [[path/to/file-2]] — one-line summary

### <Cluster Name>

- [ ] [[path/to/file-3]] — one-line summary

## Uncategorized

- [ ] [[path/to/misc-file]] — one-line summary
```

Rules:
- Use checkboxes (`- [ ]`) for linked materials so the user can track reading progress.
- Use wikilinks for every file reference.
- Group files by the topic clusters from the plan.
- One-line summary per file: what it covers, not what it is ("attention mechanisms and self-attention variants", not "a document about attention").
- If a file doesn't fit any cluster, put it under `## Uncategorized`.
- If `index.md` already exists, update it in place rather than creating a duplicate.

Completion criterion: `index.md` exists, lists every file in the directory, and every wikilink resolves.

## Step 5: Report

Tell the user:
- Files moved, merged, split, or renamed (with old → new paths).
- Wikilinks updated.
- Path to the generated `[[index.md]]`.
- Any files left uncategorized.
