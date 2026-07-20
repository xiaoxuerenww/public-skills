# Interview Project Deep Dive

Collect, outline, polish, and drill project deep-dive interview materials for Staff/Senior Staff MLE or SWE roles at frontier AI labs.

## Purpose

Turn real project material into credible Staff/Senior Staff project deep dives. Outputs a single durable artifact (`_deep_dive.md`) that demonstrates depth, judgment, ownership, and cross-functional influence.

## Modes

1. **Collect Mode** — Gather and organize raw project material
2. **Outline Mode** — Design presentation structure with storytelling flow
3. **Polish Mode** — Iteratively refine each section/slide
4. **Drill Mode** — Pressure-test technical and execution decisions

## Directory Structure

```
<project_name>/
├── context/              # Raw project material (preserved)
├── _deep_dive.md         # Main deep dive document
├── presentation/
│   ├── outline.md        # Presentation structure
│   └── slides/           # Individual slide content
└── drill_notes.md        # Q&A and pressure-test notes
```

## Included Tool: md2slides

Convert Markdown slide documents into PPTX presentations.

**Usage:**
```bash
# Basic conversion
python3 ~/.codex/skills/md2slides/scripts/generate_slides.py presentation.md output.pptx

# With images directory
python3 ~/.codex/skills/md2slides/scripts/generate_slides.py presentation.md output.pptx --images-dir ./images
```

**Markdown conventions:**
- `# Deck title` → Title slide
- `## Slide N: Title` → New slide with title
- First paragraph → Subtitle (if short)
- `- bullets` → Bullet lists
- Tables, images, blockquotes supported

## Customization Required

The md2slides script references:
```
~/.codex/skills/md2slides/scripts/generate_slides.py
```

This path is already sanitized and portable across users using `~/` notation.

## Usage Examples

```
"Collect material for my ML platform migration project"
"Create presentation outline with 10 slides"
"Polish the technical architecture section"
"Drill me on scalability tradeoffs"
"Convert my deep dive to PPTX slides"
```

## File Structure

```
interview-project-deep-dive/
├── README.md                     # This file
├── SKILL.md                      # Main skill definition
├── .claude-plugin/
│   └── plugin.json               # Plugin metadata
└── md2slides/
    ├── SKILL.md                  # Slides generation skill
    └── scripts/
        └── generate_slides.py    # PPTX converter
```

## Storytelling Philosophy

Presentations must:
- Lead with tension, not the solution
- Calibrate for smart non-domain interviewers
- Have a one-sentence thesis as backbone
- Explain business value in accessible language

## Notes

- All personal references sanitized to "the user"
- Paths use portable `~/` notation
- Single artifact approach (`_deep_dive.md`)
- Supports both Markdown and PPTX output formats
