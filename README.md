# Public Skills

Collection of Claude Code skills for interview preparation, content creation, research, and productivity workflows.

## Interview Prep Skills

### Core Interview Skills

- **[behavioral-interview-coach](./behavioral-interview-coach/)** — Staff/Senior Staff behavioral interview prep with story building and mock interviews
- **[interview-coding](./interview-coding/)** — Algorithm and data structure coding interview prep
- **[interview-ML](./interview-ML/)** — ML/LLM fundamentals and ML system design interview prep
- **[interview-project-deep-dive](./interview-project-deep-dive/)** — Project deep dive preparation with presentation generation
- **[interview-prep-multi-agent](./interview-prep-multi-agent/)** — Multi-agent coordinator for end-to-end interview prep
- **[tech-interview-question-scraper](./tech-interview-question-scraper/)** — Scrape and organize interview questions

## Content & Writing Skills

- **[write-article](./write-article/)** — Article drafting, revision, and thought capture
- **[grilling](./grilling/)** — Critical questioning and feedback
- **[grill-me](./grill-me/)** — Interactive grilling sessions
- **[tidy-doc](./tidy-doc/)** — Document cleanup and formatting

## Research & Information

- **[doc-grounded-qa](./doc-grounded-qa/)** — Document-based Q&A
- **[frontier-lab-jobs](./frontier-lab-jobs/)** — Frontier AI lab job tracking
- **[frontier-lab-news-digest](./frontier-lab-news-digest/)** — News aggregation for AI labs

## Development & Tools

- **[file-cleaner](./file-cleaner/)** — Clean up temporary and generated files
- **[sanitize-pii](./sanitize-pii/)** — Remove personal information from directories for public sharing
- **[writing-great-skills](./writing-great-skills/)** — Guidelines for creating Claude Code skills
- **[handoff](./handoff/)** — Project handoff documentation
- **[humanizer](./humanizer/)** — Humanize AI-generated content

## Utilities

- **[00_inbox](./00_inbox/)** — Inbox for temporary notes and processing

## Features

- ✅ **Sanitized** — All personal information removed
- ✅ **Portable** — Uses `~/` notation for user-specific paths
- ✅ **Documented** — Each skill includes comprehensive README
- ✅ **Multi-mode** — Most skills support multiple workflows (learn, practice, mock, etc.)
- ✅ **Durable artifacts** — Persistent progress tracking

## Installation

### Option 1: Clone Entire Collection

```bash
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git
```

### Option 2: Individual Skills

Copy individual skill directories to your `~/.codex/skills/` directory:

```bash
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git temp
cp -r temp/behavioral-interview-coach .
rm -rf temp
```

### Option 3: Symlink

Create symlinks to use skills directly from the cloned repo:

```bash
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git
ln -s public-skills/behavioral-interview-coach .
ln -s public-skills/write-article .
# etc.
```

## Customization

Most skills require updating workspace paths. See each skill's README for details:

- **Interview skills**: Various workspace paths for prep materials
- **Research skills**: Source directories and output locations
- **Content skills**: Article and draft directories

Update `SKILL.md` files to match your directory structure.

## Usage

Once installed, invoke skills by name:

```
"Run a behavioral mock interview"
"Practice ML fundamentals"
"Write an article about transformers"
"Sanitize my-project/ for public release"
"Search for AI safety job postings"
```

## Skill Categories

### Interview Preparation (6 skills)
Complete end-to-end interview prep from fundamentals to mocks

### Content Creation (4 skills)
Writing, editing, and critical review workflows

### Research & Tracking (3 skills)
Information aggregation and analysis

### Development Tools (5 skills)
Code quality, documentation, and project management

### Utilities (1 skill)
General-purpose inbox and processing

## Contributing

These skills are shared as-is under MIT License. Feel free to:
- Fork and customize
- Submit issues or suggestions
- Share improvements back to the community

## Related

- [Private Skills](https://github.com/xiaoxuerenww/private-skills) — Personal workflow skills (journal, life coaching)
- [Claude Code](https://claude.ai/code) — Official Claude Code documentation

## License

MIT License - see LICENSE file for details.

---

**Total Skills:** 19  
**Last Updated:** 2026-07-20
