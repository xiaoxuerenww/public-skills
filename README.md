# Public Skills

Collection of Claude Code skills for interview preparation and technical workflows.

## Interview Prep Skills

### Core Interview Skills

- **[behavioral-interview-coach](./behavioral-interview-coach/)** — Staff/Senior Staff behavioral interview prep with story building and mock interviews
- **[interview-coding](./interview-coding/)** — Algorithm and data structure coding interview prep
- **[interview-ML](./interview-ML/)** — ML/LLM fundamentals and ML system design interview prep
- **[interview-project-deep-dive](./interview-project-deep-dive/)** — Project deep dive preparation with presentation generation
- **[interview-prep-multi-agent](./interview-prep-multi-agent/)** — Multi-agent coordinator for end-to-end interview prep

### Features

- ✅ **Sanitized** — All personal information removed
- ✅ **Portable** — Uses `~/` notation for user-specific paths
- ✅ **Documented** — Each skill includes comprehensive README
- ✅ **Multi-mode** — Learn, practice, mock, and solve modes
- ✅ **Durable artifacts** — Persistent progress tracking

## Installation

### Option 1: Individual Skills

Copy individual skill directories to your `~/.codex/skills/` directory:

```bash
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git temp
cp -r temp/behavioral-interview-coach .
rm -rf temp
```

### Option 2: Clone Entire Collection

```bash
cd ~/.codex/skills
git clone https://github.com/xiaoxuerenww/public-skills.git
# Symlink or copy skills as needed
```

## Customization

Most skills require updating workspace paths. See each skill's README for details:

- **behavioral-interview-coach**: `~/Documents/work/3_BQ/`
- **interview-ML**: `~/Documents/work/0_databricks/`
- **interview-prep-multi-agent**: `~/Documents/work/0_inbox/`

Update `SKILL.md` files to match your directory structure.

## Usage

Once installed, invoke skills by name:

```
"Run a behavioral mock interview"
"Practice ML fundamentals"
"Create system design prep for recommendation systems"
"Help me prepare a project deep dive"
```

## Contributing

These skills are shared as-is. Feel free to fork, customize, and adapt for your own use.

## License

MIT License - see individual skill directories for details.

## Related

- [Private Skills](https://github.com/xiaoxuerenww/private-skills) — Personal/private skill collection
- [Claude Code](https://claude.ai/code) — Official Claude Code documentation
