# Behavioral Interview Coach

End-to-end behavioral interview prep for Staff/Senior Staff MLE and SWE roles at frontier AI labs.

## Purpose

Help prepare for Staff/Senior Staff behavioral interviews by moving from raw career material to high-signal stories, concise interview scripts, and realistic mock feedback.

## Modes

1. **Brainstorm Mode** — Generate candidate stories from career background
2. **Decode Mode** — Analyze a question and select the best story
3. **Build Mode** — Develop stories through grilling and CARL drafting
4. **Mock Mode** — Run realistic mock interviews with calibrated feedback

## Customization Required

The skill references this default workspace path:
```
~/Documents/work/3_BQ/
```

**Folder structure:**
```
3_BQ/
├── input/
│   └── 0_requirements.md           # Ground-truth requirements
├── output/
│   ├── 00_story_inventory.md       # All candidate stories
│   ├── 01_preferences_rubrics/     # Answer style preferences
│   ├── 02_stories/                 # Individual story artifacts
│   └── 03_mocks/                   # Mock session transcripts
```

**To customize:**

Either:
- **Option A**: Create the same structure at `~/Documents/work/3_BQ/`
- **Option B**: Update `SKILL.md` and replace `~/Documents/work/3_BQ` with your path

## Usage Examples

```
"Brainstorm behavioral stories from my background"
"Decode: Tell me about a time you resolved conflict"
"Build a story about my ML platform migration"
"Run a behavioral mock interview"
```

## File Structure

```
behavioral-interview-coach/
├── README.md           # This file
├── SKILL.md            # Main skill definition
└── .claude-plugin/
    └── plugin.json     # Plugin metadata
```

## Notes

- All personal references sanitized to "the user"
- Default paths use `~/` notation (portable across users)
- Works with input/0_requirements.md as ground truth
- Outputs are durable artifacts under output/
