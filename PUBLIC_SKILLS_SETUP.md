# Public Skills Setup Summary

**Date:** 2026-07-20  
**Repository:** https://github.com/xiaoxuerenww/public-skills

## Published Skills

The following interview prep skills have been published to the public repository:

1. ✅ **behavioral-interview-coach** — Staff+ behavioral interview prep
2. ✅ **interview-ML** — ML/LLM fundamentals and system design
3. ✅ **interview-coding** — Algorithm and data structure prep
4. ✅ **interview-prep-multi-agent** — Multi-agent coordinator
5. ✅ **interview-project-deep-dive** — Project deep dive preparation

## Repository Structure

```
public-skills/
├── README.md                           # Main documentation
├── .gitignore                          # Git ignore patterns
├── behavioral-interview-coach/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── .claude-plugin/plugin.json
├── interview-ML/
│   ├── README.md
│   ├── agents/openai.yaml
│   ├── ml-fundamentals-interview/
│   ├── ml-system-design-interview/
│   ├── system-design-material-finder/
│   └── teach/
├── interview-coding/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── .claude-plugin/plugin.json
├── interview-prep-multi-agent/
│   ├── README.md
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── .claude-plugin/plugin.json
└── interview-project-deep-dive/
    ├── README.md
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── md2slides/
    ├── slide-styler/
    └── system-diagram/
```

## Local Setup

Each interview directory in `~/.codex/skills/` now tracks the public-skills repository:

| Directory | Remote | Branch | Status |
|-----------|--------|--------|--------|
| behavioral-interview-coach | public-skills | main | Clean |
| interview-ML | public-skills | main | Clean |
| interview-coding | public-skills | main | Clean |
| interview-prep-multi-agent | public-skills | main | Clean |
| interview-project-deep-dive | public-skills | main | Clean |

## What Was Published

**Total files:** 43 files, 7262 lines of code

**Included:**
- ✅ All SKILL.md definitions
- ✅ README documentation for each skill
- ✅ Agent configurations (openai.yaml)
- ✅ Plugin metadata (.claude-plugin/plugin.json)
- ✅ Python scripts with sanitized paths
- ✅ Reference documentation (frameworks, templates)
- ✅ Main README with installation instructions

**Excluded:**
- ❌ Cache files (__pycache__)
- ❌ .DS_Store files
- ❌ Personal data (sanitized)
- ❌ Workspace directories with user content

## Sanitization Applied

All published skills have:
- Personal names replaced with "the user"
- Absolute paths (`/Users/xue`) replaced with `~/`
- Python scripts using `os.path.expanduser()`
- No email addresses, phone numbers, or credentials
- Portable configuration across different users

## Usage

### For Others to Install

```bash
# Clone the entire collection
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git

# Or install individual skills
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git temp
cp -r temp/interview-ML .
rm -rf temp
```

### For You to Update

Since your local directories track the public repo:

```bash
# Make changes to a skill
cd ~/.codex/skills/behavioral-interview-coach
vim SKILL.md

# Commit and push
git add .
git commit -m "Update behavioral interview coach"
git push origin main
```

Note: Each directory is a separate git repo, not a monorepo. To update the main public-skills repo, you'll need to copy changes back to the centralized repo.

## Repository Links

- **Public Skills:** https://github.com/xiaoxuerenww/public-skills
- **Private Skills:** https://github.com/xiaoxuerenww/private-skills

## Next Steps

To keep the public repo in sync with local changes:

1. Make changes in local skill directories
2. Commit locally in each directory
3. Copy updated skills to a clone of public-skills
4. Commit and push to public-skills main branch

Or set up subtree/submodule structure for easier sync.

## Documentation

Each skill includes:
- README.md with overview and customization instructions
- SKILL.md with complete mode documentation
- Agent configuration for multi-agent workflows
- Usage examples and file structure diagrams

All ready for public consumption with no personal data.
