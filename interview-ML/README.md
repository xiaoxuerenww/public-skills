# ML Interview Prep Skills

End-to-end Staff+ MLE interview prep with fundamentals, system design, and concept teaching.

## Overview

This is a **coordinating skill** that routes to specialized sub-skills based on your request type. The agent automatically selects the right skill for your needs.

## Skills Included

### Core Interview Skills

- **[ml-fundamentals-interview](./ml-fundamentals-interview/)** — ML/LLM fundamentals quizzes, drills, learn/practice/mock modes, question banks, and solutions
- **[ml-system-design-interview](./ml-system-design-interview/)** — ML system design prep, keyword practice, outline review, companion learning, and mocks
- **[teach](./teach/)** — Quick concept one-pagers or stateful course mode for deep learning
- **[system-design-material-finder](./system-design-material-finder/)** — Reference curation and source discovery for system design prep

### Routing Logic

The agent automatically routes your request:

| Request Type | Routes To | Example |
|-------------|-----------|---------|
| Theory/fundamentals questions | ml-fundamentals-interview | "Quiz me on transformers" |
| System design problems | ml-system-design-interview | "Design a recommendation system" |
| Concept learning | teach | "Teach me about RLHF" |
| Finding references | system-design-material-finder | "Find papers on RAG systems" |
| Learn mode for topics | ml-fundamentals-interview | "Learn about attention mechanisms" |
| Mock interviews | Appropriate skill's mock mode | "Run ML fundamentals mock" |

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

## Agent Architecture

The unified agent at `agents/openai.yaml` provides intelligent routing:

### Routing Process

1. **Context Resolution** — Identifies topic directory, problem directory, or current note
2. **Request Classification** — Determines request type (fundamentals, system design, concept, reference)
3. **Skill Selection** — Routes to the narrowest appropriate skill
4. **Workflow Coordination** — Manages multi-skill workflows when needed

### Invocation

You don't need to know which sub-skill to use. Just describe what you want:

```
"Help me prep for ML fundamentals interview"
→ Routes to ml-fundamentals-interview

"Create system design practice for recommendation systems"
→ Routes to ml-system-design-interview

"Teach me about transformers"
→ Routes to teach

"Find papers on RAG systems"
→ Routes to system-design-material-finder
```

The agent handles the routing automatically based on your natural language request.

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

### ML Fundamentals (Routes to ml-fundamentals-interview)

**Learn mode:**
```
"Learn about attention mechanisms"
"Teach me transformer architecture"
"Explain batch normalization"
```

**Practice mode:**
```
"Practice transformer questions"
"Quiz me on RLHF"
"Drill me on distributed training"
```

**Mock mode:**
```
"Run ML fundamentals mock with 5 questions"
"Mock interview on LLM internals"
```

**Topic prep:**
```
"Create question bank for attention mechanisms"
"Generate solutions for transformer questions"
```

### System Design (Routes to ml-system-design-interview)

**Prep mode:**
```
"Create prep artifacts for recommendation system"
"Set up practice for model serving system"
```

**Practice mode:**
```
"Practice ML system design with keyword outline"
"Guide me through ranking system design"
```

**Mock mode:**
```
"Run mock for recommendation system design"
"Mock interview for ML infrastructure"
```

**Learn mode:**
```
"Learn about recommendation system design"
"Companion mode for model serving"
```

### Concept Learning (Routes to teach)

**Quick concepts:**
```
"Teach me about RLHF"
"Explain batch normalization at Staff MLE depth"
"Quick intro to distributed training"
```

**Course mode:**
```
"Start a course on transformers"
"Create learning plan for system design"
```

### Reference Finding (Routes to system-design-material-finder)

```
"Find references for RAG systems"
"Search papers on recommendation algorithms"
"Locate resources for model serving"
```

### Multi-Skill Workflows

The agent can coordinate across skills:

```
"Find references for recommendation systems, then help me design one"
→ 1. system-design-material-finder (find references)
→ 2. ml-system-design-interview (design system)

"Teach me about transformers, then quiz me on it"
→ 1. teach (concept explanation)
→ 2. ml-fundamentals-interview (practice questions)
```

## Key Features

### Intelligent Routing
- Automatically selects the right sub-skill based on request type
- No need to remember which skill does what
- Seamless handoffs between skills

### Multi-Mode Support
Each sub-skill offers multiple modes:
- **Learn** — Passive Q&A with companion notes
- **Practice** — Active drills with feedback
- **Mock** — Realistic interview simulation
- **Prep** — Create study artifacts
- **Solve** — Generate comprehensive solutions

### Durable Artifacts
- Question banks stored in markdown
- Mock sessions in dated directories
- Companion notes for learning
- Keyword outlines for practice
- Solutions for reference

### Progress Tracking
- Tracks which questions you've seen
- Records pass/fail for practice
- Maintains spaced repetition queue
- Builds on previous sessions

## Skill Capabilities Matrix

| Capability | ml-fundamentals-interview | ml-system-design-interview | teach | material-finder |
|-----------|--------------------------|---------------------------|-------|----------------|
| Learn mode | ✓ | ✓ | ✓ | - |
| Practice mode | ✓ | ✓ | - | - |
| Mock mode | ✓ | ✓ | - | - |
| Prep mode | ✓ | ✓ | - | - |
| Solve mode | ✓ | ✓ | - | - |
| Question banks | ✓ | - | - | - |
| Reference curation | - | ✓ | - | ✓ |
| Course mode | - | - | ✓ | - |
| Quick concepts | - | - | ✓ | - |

## Notes

- Skills use `the user` as a generic placeholder (sanitized from original personal references)
- Default paths assume a Databricks interview prep structure — customize as needed
- All file operations create backups and preserve existing content
- Mock sessions append to dated files to track progress over time
- Python scripts use `os.path.expanduser()` for cross-platform compatibility
