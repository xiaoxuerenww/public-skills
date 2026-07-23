---
title: "Project Deep-Dive — Technical Presentation — Anthropic Interview Question"
source: "https://www.1point3acres.com/interview/problems/company/anthropic/onsite-project-deep-dive"
author:
  - "[[Anthropic interview candidates]]"
published:
created: 2026-07-15
description: "Present a past technical project of your choice for 20–25 minutes, then field 25–30 minutes of deep-dive Q&A. Interviewers probe architecture decisions, tradeoffs, your personal role, and what you'd do differently. The round is universal across roles and is one of the most consistent positive signals when done well."
tags:
  - "clippings"
---
## Requirements

### Structure

- ~20–25 minutes candidate presentation.
- ~25–30 minutes of interviewer Q&A.
- Slides or a code walkthrough are both acceptable. A live demo is uncommon.

### What interviewers grade on

- Clarity of problem statement and why it mattered.
- Architecture choices and **alternatives considered** — not just what you built but what you didn't and why.
- Your specific contribution vs. the team's. Be precise; "we" is fine if you also surface the "I."
- Quantified impact: latency, cost, accuracy, headcount-time-saved, revenue.
- Reflective depth: what surprised you, what you'd redesign, what the next version looks like.

### Common Q&A traps

- "Why didn't you use X?" — interviewer pushes a plausible alternative; have the comparison rehearsed.
- "What would you change with hindsight?" — give two concrete answers, not platitudes.
- "What was the hardest unanticipated challenge?" — be specific; vague answers read as second-hand.
- "Was it worth it?" — be ready to defend the project's ROI in dollars. Interviewers from infra / research orgs translate effort into cost (e.g., a 50-engineer-year project at ~$400K / eng-year ≈ $20M) and ask whether the measured return justified that spend. Have both the cost and the return of your headline project quantified.

## Notes

- Multiple candidates report this round as the *highest-leverage* on the loop: nail it and you can absorb a weaker round elsewhere.
- Pick a project that maps to the team's domain when possible, but a sharp deep-dive on a tangentially-related project beats a shallow one on a perfectly-matched project.
- Watch the time. Several candidates describe getting stuck on early slides and running short on Q&A — interviewers see incomplete presentation as a signal too.

## Preparation

- Build a 25-minute deck that can flex to 15 or 35 with a slide cut/expand plan. Rehearse it timed at least three times.
- Mock the Q&A with a peer who will *actually* push back — list 15 likely follow-ups, have a 60-second answer for each.
- Memorize the numbers: throughput before/after, cost, headcount, percentages.
- Bring a one-page architecture diagram you can sketch on the doc if asked — interviewers often want the picture in real time.