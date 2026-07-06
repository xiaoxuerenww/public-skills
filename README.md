# Codex Skills

Personal Codex skills for Julie's Staff/Senior Staff MLE interview prep, career planning, writing, job search, and local evidence-processing workflows.

**Status:** Active personal skill workspace  
**Last Updated:** July 2026  
**Index:** [SKILLS_INDEX.md](SKILLS_INDEX.md)

---

## What Lives Here

This repository contains triggerable Codex skills installed under `/Users/xue/.codex/skills`.

The main interview-prep skills work directly in local prep folders and produce durable Markdown artifacts. The supporting skills cover document-grounded Q&A, job search, writing cleanup, coaching, scraping output cleanup, and skill authoring.

Use [SKILLS_INDEX.md](SKILLS_INDEX.md) as the current map of available skills, paths, and routing guidance.

---

## Core Interview Prep Skills

| Skill | Use for |
| --- | --- |
| `interview-prep-multi-agent` | Coordinate prep across coding, ML/LLM fundamentals, ML system design, project deep dives, behavioral prep, readiness audits, and panel mocks. |
| `coding-interview-companion` | Algorithms, data structures, practical coding rounds, solve/learn/practice/mock workflows, starter code, tests, and feedback. |
| `ml-fundamentals-interview` | Daily ML/LLM fundamentals quizzes, spaced review, learn mode, mock mode, Databricks topic prep, and grounded question banks. |
| `ml-system-design-interview` | ML system design prep for ranking, retrieval, serving, evaluation, experiment platforms, ML infra, and research infrastructure. |
| `project-deep-dive-interview` | Staff/Senior Staff project deep-dive prep, project narrative shaping, pressure testing, and mock interviews. |
| `behavioral-interview-coach` | Behavioral story brainstorming, grilling, CARL scripts, culture/HM prep, and Staff+ mock feedback. |

---

## Supporting Skills

| Skill | Use for |
| --- | --- |
| `doc-grounded-qa` | Answer questions from PDFs, docs, notes, resumes, job descriptions, company research, or pasted material with source-grounded notes. |
| `teach` | Quick concept one-pagers or stateful course workspaces for ML, systems, coding, math, research, or product concepts. |
| `system-design-material-finder` | Find and curate interview-ready learning resources for system design and ML system design prompts. |
| `frontier-lab-jobs` | Find, shortlist, and apply to frontier AI lab roles using the local `Applied_Roles.md` tracker. |
| `frontier-lab-news-digest` | Generate a daily mobile-friendly HTML digest of frontier AI lab news. |
| `personalized-life-coach` | Work through career/life decisions, recurring blockers, principle tradeoffs, and next actions. |
| `mle-swe-growth-goal` | Pick a focused MLE/SWE/AI-engineer growth direction over a 3 to 6 month horizon. |
| `humanizer` | Edit writing to sound more natural and less AI-generated. |
| `post-process-scraper-outputs` | Convert local scraper outputs into raw, linked evidence files by company and interview round. |
| `grilling` / `grill-me` | Stress-test a plan or design through focused questioning. |
| `handoff` | Compact the current conversation into a handoff document for another agent. |
| `writing-great-skills` | Reference principles and vocabulary for creating predictable skills. |

---

## Typical Workflow

1. Work from the relevant prep folder, note, tracker, or project directory.
2. Invoke the skill by name or describe the task naturally.
3. Let the skill read the local source of truth before writing.
4. Review the generated Markdown artifacts, tests, feedback docs, or tracker updates.

For ML coding exercises in the interview vault, use:

```bash
cd ~/Documents/interview/2026_interview/"3.2 ML Coding"
python3 ex1_vectorization.py
python3 -m pytest exN_*.py
```

---

## Repository Notes

- User skills live in top-level directories with a `SKILL.md`.
- Bundled system skills live under `.system/`.
- `scraper/` is a local utility project, not a triggerable skill because it has no `SKILL.md`.
- Some skills include agents, scripts, examples, templates, or README files used by the skill.
- Keep high-level routing in this README and [SKILLS_INDEX.md](SKILLS_INDEX.md); keep detailed behavior inside each `SKILL.md`.

---

**Author:** Julie Xue Wang  
**Repository:** https://github.com/xiaoxuerenww/skills
