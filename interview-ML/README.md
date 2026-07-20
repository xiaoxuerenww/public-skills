# ML Interview Prep Skills

End-to-end Staff+ MLE interview prep with fundamentals, system design, and concept teaching.

## Skills Included

- **ml-fundamentals-interview** — ML/LLM fundamentals quizzes, drills, learn/practice/mock modes
- **ml-system-design-interview** — ML system design prep, keyword practice, outline review, mocks
- **teach** — Quick concept explanations or stateful course mode
- **system-design-material-finder** — Reference curation and source discovery

## Customization Required

These skills reference user-specific paths that need to be updated for your environment:

### 1. Question Banks and Prep Materials

The skills reference these default paths:
```
~/Documents/work/0_databricks/0_db_ml_fundamental/
~/Documents/work/0_databricks/Templates/
~/Documents/work/0_inbox/
```

**To customize:**

Either:
- **Option A**: Create the same directory structure in your home directory
- **Option B**: Update the paths in the SKILL.md files to match your setup

Files to update:
- `ml-fundamentals-interview/SKILL.md` — Search for `~/Documents/work/` and replace with your path
- `ml-fundamentals-interview/scripts/pick_question.py` — Update `QUIZ_DIR` constant (line 16)
- `ml-system-design-interview/SKILL.md` — Search for `~/Documents/work/` and replace with your path

### 2. Python Script

The `pick_question.py` script uses `os.path.expanduser()` to resolve `~/` to your home directory, so it will work across different users once you update the path structure.

## Agent

The unified agent at `agents/openai.yaml` routes requests to the appropriate sub-skill.

**Usage:**
```
"Help me prep for ML fundamentals interview"
"Create system design practice for recommendation systems"
"Teach me about transformers"
```

## File Structure

```
ml-interview/
├── README.md                           # This file
├── agents/
│   └── openai.yaml                     # Unified agent config
├── ml-fundamentals-interview/
│   ├── SKILL.md                        # Fundamentals prep skill
│   ├── scripts/pick_question.py        # Question selection script
│   └── agents/openai.yaml              # Fundamentals agent
├── ml-system-design-interview/
│   ├── SKILL.md                        # System design prep skill
│   ├── references/*.md                 # Framework guides
│   └── agents/openai.yaml              # System design agent
├── teach/
│   ├── SKILL.md                        # Teaching skill
│   └── *.md                            # Format documentation
└── system-design-material-finder/
    ├── SKILL.md                        # Material finder skill
    └── references/source_catalog.md    # Source catalog
```

## Usage Examples

### ML Fundamentals Quiz
```
"Run ML fundamentals mock with 5 questions"
"Learn about attention mechanisms"
"Practice transformer questions"
```

### System Design Practice
```
"Create prep artifacts for recommendation system design"
"Practice ML system design with keyword outline"
"Run mock for model serving system"
```

### Concept Teaching
```
"Teach me about RLHF"
"Explain batch normalization at Staff MLE depth"
"Start a course on distributed training"
```

## Notes

- Skills use `the user` as a generic placeholder (sanitized from original personal references)
- Default paths assume a Databricks interview prep structure — customize as needed
- All file operations create backups and preserve existing content
- Mock sessions append to dated files to track progress over time
