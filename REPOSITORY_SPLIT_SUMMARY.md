# Repository Split Summary

**Date:** 2026-07-20

## Overview

Successfully split skills into two repositories:
- **Public Skills** — Interview prep skills (public)
- **Private Skills** — Personal workflow skills (private)

## Public Skills Repository

**URL:** https://github.com/xiaoxuerenww/public-skills  
**Visibility:** PUBLIC

### Contains (5 skills)

1. ✅ **behavioral-interview-coach** — Staff+ behavioral interview prep
2. ✅ **interview-ML** — ML/LLM fundamentals and system design
3. ✅ **interview-coding** — Algorithm and data structure prep
4. ✅ **interview-prep-multi-agent** — Multi-agent coordinator
5. ✅ **interview-project-deep-dive** — Project deep dive preparation

**Total:** 43 files, 7,262 lines of code

### Features

- ✅ All personal information sanitized
- ✅ Portable paths using `~/` notation
- ✅ Comprehensive README for each skill
- ✅ Agent configurations included
- ✅ Python scripts with proper path expansion
- ✅ .gitignore for clean tracking

## Private Skills Repository

**URL:** https://github.com/xiaoxuerenww/private-skills  
**Visibility:** PRIVATE

### Contains (16 skills)

**Productivity & Organization:**
- journal
- tidy-doc
- sanitize-pii

**Content & Writing:**
- write-article
- grilling
- grill-me

**Research & Information:**
- doc-grounded-qa
- frontier-lab-jobs
- frontier-lab-news-digest
- tech-interview-question-scraper

**Development & Tools:**
- file-cleaner
- writing-great-skills
- handoff

**Coaching & Personal:**
- personalized-life-coach
- humanizer

### Changes Applied

**Removed from private-skills:**
- behavioral-interview-coach
- interview-ML
- interview-coding
- interview-prep-multi-agent
- interview-project-deep-dive
- SANITIZATION_SUMMARY.md
- PUBLIC_SKILLS_SETUP.md

**Updated:**
- README.md now points to public-skills for interview prep

## Local Setup

### Interview Skills (Local)

Each interview skill directory in `~/.codex/skills/` tracks the public-skills repo:

| Directory | Repository | Status |
|-----------|------------|--------|
| behavioral-interview-coach | public-skills | Initialized |
| interview-ML | public-skills | Initialized |
| interview-coding | public-skills | Initialized |
| interview-prep-multi-agent | public-skills | Initialized |
| interview-project-deep-dive | public-skills | Initialized |

### Private Skills (Local)

Other skills in `~/.codex/skills/` can optionally track private-skills repo.

## Repository Structure

### public-skills/
```
├── README.md                       # Main documentation
├── .gitignore                      # Git ignore patterns
├── behavioral-interview-coach/
├── interview-ML/
│   ├── ml-fundamentals-interview/
│   ├── ml-system-design-interview/
│   ├── system-design-material-finder/
│   └── teach/
├── interview-coding/
├── interview-prep-multi-agent/
└── interview-project-deep-dive/
    ├── md2slides/
    ├── slide-styler/
    └── system-diagram/
```

### private-skills/
```
├── README.md
├── 00_inbox/
├── doc-grounded-qa/
├── file-cleaner/
├── frontier-lab-jobs/
├── frontier-lab-news-digest/
├── grill-me/
├── grilling/
├── handoff/
├── humanizer/
├── journal/
├── personalized-life-coach/
├── sanitize-pii/
├── tech-interview-question-scraper/
├── tidy-doc/
├── write-article/
└── writing-great-skills/
```

## Commit History

### public-skills
- Initial commit: "Initial commit: Interview prep skills collection"
- 43 files added, fully sanitized

### private-skills
- Latest commit: "Move interview skills to public repository"
- 16 files changed, 1,382 deletions
- README updated to point to public repo

## Access & Sharing

### Public Skills
- ✅ Anyone can view and clone
- ✅ Ready for portfolio/sharing
- ✅ Zero personal information
- ✅ Complete documentation

### Private Skills
- 🔒 Private repository
- 🔒 Access controlled
- 🔒 May contain personal workflows
- 🔒 Not for public distribution

## Next Steps

### To Update Public Skills

1. Make changes in local skill directories
2. Commit locally
3. Copy to a fresh clone of public-skills
4. Push to public-skills main branch

Or set up subtree/submodule for easier sync.

### To Share Interview Skills

Simply share the link:
```
https://github.com/xiaoxuerenww/public-skills
```

Users can:
- Browse online
- Clone entire collection
- Copy individual skills
- Fork and customize

## Summary

✅ **Public skills:** 5 interview prep skills, sanitized and documented  
✅ **Private skills:** 16 personal workflow skills, kept private  
✅ **Separation complete:** Clear distinction between public and private content  
✅ **Ready to share:** Public repository is fully prepared for distribution
