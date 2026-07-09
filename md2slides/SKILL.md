---
name: md2slides
description: "Convert Markdown slide documents into PowerPoint PPTX decks. Use when the user asks to turn a Markdown presentation, Obsidian slide note, deep_dive_presentation.md, or any md slide outline into a .pptx file, especially when preserving simple headings, bullets, tables, and local image embeds."
---

# Markdown to Slides

Convert a Markdown-native presentation into a simple 16:9 PowerPoint deck using `scripts/generate_slides.py`.

## Input format

Prefer a Markdown file with this structure:

```markdown
# Deck title

## Slide 1: Thesis
Short subtitle

- Bullet
- Bullet

| Column | Column |
|---|---|
| Value | Value |

![[image.png]]
```

Supported elements:

- `## Slide N: Title` or `## Title` as slide boundaries.
- The first short paragraph after a slide heading as subtitle.
- Bullets, numbered lines, blockquotes, and simple bold markers.
- Markdown tables.
- Obsidian image embeds `![[image.png]]` and Markdown images `![alt](path)`.

## Workflow

1. Locate the Markdown source file. For project deep dives, default to `projects/<project_slug>/deep_dive_presentation.md`.
2. Check that each slide starts with a `##` heading and that dense detail has been moved out of the presentation doc.
3. Run the bundled converter:

```bash
python3 /Users/xue/.codex/skills/md2slides/scripts/generate_slides.py path/to/deep_dive_presentation.md path/to/output.pptx --images-dir path/to/images
```

Omit `--images-dir` if images live beside the Markdown file or image paths are absolute.

4. If `python-pptx` is missing, install it in a temporary virtualenv rather than changing the user's project environment:

```bash
python3 -m venv /tmp/md2slides-venv
/tmp/md2slides-venv/bin/pip install python-pptx
/tmp/md2slides-venv/bin/python /Users/xue/.codex/skills/md2slides/scripts/generate_slides.py path/to/deck.md path/to/deck.pptx
```

5. Verify the output exists. If the deck is important, render or inspect it using available presentation/PDF tools and iterate on the Markdown or script only as needed.

## Style expectations

- Keep one idea per slide.
- Prefer tables for comparisons and sequences.
- Keep the Markdown presentation sparse before conversion.
- Do not invent slide content during conversion. If content is missing, update the source Markdown first.
