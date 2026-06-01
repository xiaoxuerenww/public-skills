# Interview Prep Skills Ecosystem

A comprehensive, integrated suite of Claude skills for Staff/Senior Staff MLE interview preparation at frontier AI labs (Anthropic, OpenAI, xAI, Google DeepMind, Meta).

**Status:** Production-ready  
**Last Updated:** May 2026

---

## Overview

This repository contains a redesigned interview prep ecosystem with 4 primary skills and several supporting skills. The primary skills follow a unified **solve → learn → mock** workflow with clean input/output folder structure and auto-note merging.

### Key Features

✅ **Unified Workflow** — All 3 primary skills use the same solve/learn/mock modes  
✅ **Auto-Note Merging** — Learning notes automatically consolidate into deep dives  
✅ **Interview-Ready Output** — Generate cheat sheets, solutions, and feedback docs  
✅ **Staff+ Calibration** — Rubric-based feedback aligned with frontier lab standards  
✅ **Multi-Round Orchestration** — Plan and execute full mock interviews with coordinator skill  

---

## Primary Skills (Recommended)

### 1. **coding-interview-companion**

End-to-end coding interview prep with solve/learn/mock modes.

**Use when:**
- Solving algorithm and data structure problems
- Preparing for technical coding rounds
- Need interview-ready solution explanations

**Modes:**
- **Solve** — Parse requirements, create problem setup, solve in depth/breadth, generate interview solutions + solution code + deep dive
- **Learn** — Companion your learning, auto-take notes in `learn_notes.md`, proactively merge into `deep_dive.md`
- **Mock** — Act as interviewer, review `my_solution.py`, give step-by-step feedback, take notes in `mock_feedback.md`

---

### 2. **ml-system-design-interview**

ML system design interview prep with L6+ (Staff) calibration.

**Use when:**
- Designing recommendation systems, ranking platforms, experiment pipelines
- Preparing for ML infrastructure design rounds
- Need L6+ system design answers

**Key Focus Areas:**
- Problem framing and ambiguity ownership
- ML correctness (experiment validity, data quality, reproducibility)
- Operational maturity (debugging, monitoring, rollback)
- Platform thinking (APIs, contracts, invariants)
- Cross-team impact and pragmatic reuse

---

### 3. **behavioral-interview-coach**

Behavioral interview prep with Staff+ rubric calibration.

**Use when:**
- Building and refining STAR stories
- Preparing for behavioral/culture screens
- Need feedback on scope, impact, ambiguity ownership, influence

**Staff+ Dimensions:**
- Scope & Impact (org/team-level problems, measurable outcomes)
- Technical Judgment (right problem framing, trade-off analysis)
- Ambiguity Navigation (underspecified goals, changing context)
- People Leadership (mentoring, growing others, process change)
- Cross-Functional Influence (stakeholder alignment, difficult conversations)
- Communication (crisp causal chain, concrete examples)

---

### 4. **interview-prep-multi-agent**

Orchestration and coordination across all interview domains.

**Use when:**
- Planning your full interview prep across multiple rounds
- Need a readiness audit across all domains
- Want to run a full multi-round mock interview
- Need parallel reviews of multiple artifacts

**Modes:**
- **Audit Mode** — Review your prep status across coding, system design, behavioral, fundamentals
- **Plan Mode** — Create a concrete study schedule with verifiable goals
- **Panel Mode** — Full mock interview with all rounds (coding → system design → behavioral)
- **Parallel Review Mode** — Get independent reviews of drafts from multiple perspectives
- **Integration Mode** — Overall readiness assessment (pass-ready vs. practice-ready vs. at-risk)

---

## Supporting Skills

### **learn-buddy**
Single concept learning for ML, systems, coding fundamentals. Use for refreshers, one-pagers, and targeted drills.

### **ml-daily-quiz**
ML/LLM fundamentals quizzes with spaced review. Use for daily drills, Staff/Senior Staff MLE technical depth.

### **frontier-lab-jobs**
Job search and role tracking across frontier AI labs.

### **doc-grounded-qa**
Document analysis and Q&A. Use to read and analyze PDFs, job descriptions, company notes.

### **frontier-lab-news-digest**
Daily news digest from frontier AI labs (Anthropic, OpenAI, xAI, Google DeepMind, Meta).

### **personalized-life-coach**
Career and life coaching for decision-making and principle-based reasoning.

---

## Getting Started

### 1. Install Skills in Claude Code / VS Code

Skills are automatically discovered from `~/.claude/skills/`. Restart VS Code to refresh the skill list.

### 2. Create an Interview Round Directory

```bash
mkdir ~/my-interview-prep
cd ~/my-interview-prep
mkdir input

# Create requirements file
echo "# Interview Round: Company X
- Interview type: Coding + System Design + Behavioral
- Focus areas: ML systems, leadership
" > input/0_requirements.md
```

### 3. Use the Primary Skills

**For Coding Problems:**
```
/coding-interview-companion

"Solve mode: I have this coding problem..."
```

**For System Design:**
```
/ml-system-design-interview

"Solve mode: Design a recommendation system..."
```

**For Behavioral:**
```
/behavioral-interview-coach

"Solve mode: I need to prepare stories for Anthropic..."
```

**For Full Interview Planning:**
```
/interview-prep-multi-agent

"Plan mode: I have 4 weeks until my interview loop"
"Mock mode: Run a full 3-round mock interview"
```

---

## Workflow Example: 2-Week Prep Sprint

### Week 1: Solve + Learn

**Days 1-2: Coding**
- Solve 3-5 algorithmic problems
- Learn: Walk through each solution, auto-take notes
- Output: `interview_solutions.md` + `deep_dive.md`

**Days 3-4: System Design**
- Design 2 systems (e.g., recommender + experiment platform)
- Learn: Deep dive on L6+ patterns, ownership, trade-offs
- Output: `interview_solutions.md` + `deep_dive.md`

**Day 5: Behavioral**
- Build 8-10 STAR stories across themes
- Learn: Refine for Staff+ signals (scope, judgment, influence)
- Output: `story_library.md` + `strength_examples.md`

### Week 2: Mock + Audit

**Days 6-7: Full Mocks**
- Run 3-round mock (coding → system design → behavioral)
- Get comprehensive feedback on all dimensions

**Day 8: Readiness Audit + Final Drills**
- Assess pass-ready vs. practice-ready status
- Run targeted drills on weak areas
- Final polish of cheat sheets

---

## Output Documents Reference

| Document | Purpose | Created By |
|----------|---------|-----------|
| `interview_solutions.md` | Interview cheat sheet | Solve |
| `<problem>.py` / `my_solution.md` | Full solution/design | Solve |
| `deep_dive.md` | Concept deep dives | Solve + Learn |
| `story_library.md` | STAR stories by theme | Solve + Learn |
| `strength_examples.md` | Staff+ dimension examples | Solve |
| `mock_feedback.md` | Interview feedback | Mock |

---

## Tips & Best Practices

### Solve Mode
- Start with highest-risk domain first
- Use `interview_solutions.md` as your pre-interview cheat sheet
- Create solve notes before attempting mocks

### Learn Mode
- Ask specific questions about weak points
- Notes auto-merge into polished docs
- Ask to merge and update `deep_dive.md` when done

### Mock Mode
- Treat as a real interview: don't pause, don't look up answers
- Speak naturally
- Review `mock_feedback.md` immediately after

---

## FAQ

**Q: Can I migrate existing prep work?**  
A: Use solve mode and reference your existing files. The skill will re-organize and enhance your notes.

**Q: How often should I mock?**  
A: Final week: 2-3 full mocks. Earlier: targeted drills on weak areas.

**Q: Do notes auto-save?**  
A: Notes are created in your `output/` folder on disk. You manage version control (git) explicitly.

---

## Repository Structure

```
~/.claude/skills/
├── coding-interview-companion/
│   ├── SKILL.md
│   └── .claude-plugin/plugin.json
├── ml-system-design-interview/
│   ├── SKILL.md
│   └── .claude-plugin/plugin.json
├── behavioral-interview-coach/
│   ├── SKILL.md
│   └── .claude-plugin/plugin.json
├── interview-prep-multi-agent/
│   ├── SKILL.md
│   └── .claude-plugin/plugin.json
├── learn-buddy/
├── ml-daily-quiz/
└── [other skills...]
```

---

**Last Updated:** May 29, 2026  
**Author:** Julie Xue Wang  
**Repository:** https://github.com/xiaoxuerenww/skills
