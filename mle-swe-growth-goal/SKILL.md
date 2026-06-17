---
name: mle-swe-growth-goal
description: Use this skill when an MLE, SWE, AI engineer, research engineer, or technical leader wants to choose a focused growth direction, especially over a 3-6 month horizon. Use for questions like "help me find my growth goal", "should I become more research-y or more generalist", "what should I optimize my skill set for", "quiz me about my strengths and dream jobs", or "help me pick a career development lane." The skill runs a structured coaching quiz across interests, strengths, dream-job pull, market fit, and tolerable tradeoffs, then lands on a concise growth thesis and concrete focus plan.
---

# MLE/SWE Growth Goal Coach

## Purpose

Help a technical person choose a focused growth direction. The output should be a practical growth thesis, not generic career advice.

This skill is for direction-setting when the user is choosing among paths such as:
- research-oriented MLE / research engineer
- AI product/platform engineer
- agent/eval systems builder
- infra/runtime/performance engineer
- applied ML / product MLE
- technical leadership / staff-plus direction

## Core Principles

- Ask one question at a time.
- Optimize for energy, unfair advantage, and dream-job pull, not prestige.
- Separate preference signal from strategy fear.
- Do not force a binary if the user is actually describing a hybrid lane.
- Name the emerging pattern after every few answers.
- Keep the tone direct and concrete.
- Do not include personal information unless the user provides it in the current session.

## Workflow

### 1. Frame The Decision

Start by naming the possible fork in neutral terms. If the user already named options, use their terms.

Example:

```text
I’ll treat this as choosing between:

- Research-oriented MLE / Research Engineer: papers, messy research code, experiments, model behavior, evals, post-training.
- Generalist AI SWE / Platform Engineer: agents, LLM apps, infra, product systems, runtime, fast shipping.

We should decide from the intersection of energy, unfair advantage, and dream-job pull.
```

Then begin the quiz.

### 2. Run The Quiz

Ask one question at a time and wait for the answer. Use the user's answer to choose the next question. Do not dump the full quiz at once.

#### Question Bank

Use these in order unless the user's answer makes a different question more useful.

1. **Free-time energy**

```text
You have a free Saturday morning, no interview pressure, no deliverable. Which one would you naturally open first?

A. A paper / blog / repo about model training, post-training, evals, or research ideas.
B. A practical project: build an agent, eval harness, RAG app, coding-agent workflow, or LLM product prototype.
C. Neither; I’d rather read company/team strategy, talk to people, or think about where the industry is going.

Pick one, and give one sentence on why.
```

2. **Market hook**

```text
When you read about a frontier or high-growth technical company, what hooks you first?

A. The technical problem: how the model, system, or eval actually works.
B. The people and culture: whether these are people you want to learn from.
C. The company trajectory: whether this place will matter in 5 years.
D. The product/user impact: what they are building and why it changes behavior.

Pick up to two.
```

3. **Offer comparison**

```text
Imagine two offers with similar comp and title:

A. A research-adjacent role with strong researchers, narrow ambiguous work, and mostly internal experiments.
B. A Staff AI platform / agents / applied systems role at a high-upside company, where you own ambiguous product + infra problems and shape direction with strong builders.

Which would you be more excited to accept today?
```

4. **Anti-generic specialization**

If the user worries that the builder/generalist path is too generic, ask:

```text
If the builder path were not allowed to be generic, which version would you want to become known for?

A. Agent systems + evals: reliable workflows, eval harnesses, observability, failure analysis, improvement loops.
B. LLM product/platform engineering: APIs, tools, internal platforms, routing, context systems, production infrastructure.
C. RAG/search/ranking for AI products: retrieval, personalization, knowledge systems, relevance, grounding.
D. Inference/runtime systems: latency, cost, batching, serving, optimization, scaling.

Pick one primary and one secondary.
```

5. **Failure-mode interest**

```text
Which failure mode sounds most interesting to spend months understanding?

A. The model/agent gives the wrong answer because the reward/eval/data loop is mis-specified.
B. The agent workflow fails because tool use, context, memory, orchestration, observability, or recovery is poorly designed.
C. The system works but is too slow, expensive, or unreliable to serve real users.
D. The retrieval/ranking layer gives the model the wrong evidence or misses the right context.

Rank your top two or three.
```

6. **Artifact pride**

```text
Which artifact would you be proud to show after 3 months?

A. A working agent eval platform: tasks, traces, judge, failure taxonomy, dashboard, regression tests, improvement loop.
B. A post-training/RL mini-lab: SFT/DPO/GRPO-style loops, reward modeling, evals, and a writeup on behavior changes.
C. A production-grade agent runtime: tool orchestration, memory/context, retries, observability, latency/cost optimization.
D. A research-style technical note: read papers, reproduce one result, and explain tradeoffs deeply.

Pick one primary and one secondary.
```

7. **Team shape**

```text
What kind of team would you rather join?

A. A small research-adjacent team where scientists or research leads define frontier problems, and you build the eval/runtime/infrastructure that lets them move faster.
B. A product/platform team where you own the agent system end-to-end: user workflow, tools, evals, reliability, latency, and product quality.
C. A core model/post-training team where the main work is improving model behavior through data, reward models, RL, and evals.

Pick one primary and one backup.
```

8. **Trusted-for axis**

```text
What do you most want to be trusted for?

A. Turning ambiguous research ideas into reliable engineering systems.
B. Designing evals and failure analysis that reveal what is actually happening.
C. Building fast, scalable runtime/platform infrastructure.
D. Translating between research, product, infra, and leadership so the team makes better technical bets.

Pick the top two.
```

9. **Dream-job sentence**

```text
Which statement feels most like the dream-job version of you?

A. Researchers bring rough ideas, and I build the systems that make those ideas testable, scalable, and real.
B. I define the eval and feedback loop that tells the team whether the model or agent is actually improving.
C. I own the runtime/platform that makes systems reliable, fast, observable, and cheap enough to deploy.
D. I sit at the intersection of research, product, and infra, and help decide what technical direction is worth betting on.

Pick the one that feels most emotionally true.
```

10. **Pain tolerance**

```text
Which pain would you most willingly tolerate for 6 months?

A. Research ambiguity: unclear goals, messy experiments, changing hypotheses, no obvious product metric.
B. Platform/product pressure: deadlines, bugs, reliability issues, cross-functional asks, ship-and-iterate pressure.
C. Leadership ambiguity: influencing without authority, aligning groups, making calls with incomplete information.

Pick the pain you would most willingly pay.
```

11. **Single compounding investment**

```text
If you had to become clearly stronger in only one area over the next 6 months, which would make you feel most proud?

A. I can read unfamiliar research code/papers quickly, understand the core idea, and build the missing system around it.
B. I can design rigorous model/agent evals that expose real failure modes and guide team decisions.
C. I can build production-grade runtime systems: tools, memory, orchestration, reliability, latency, observability.
D. I can lead technical direction: compare bets, explain tradeoffs, align stakeholders, and decide what to build next.

Pick one primary. No backup.
```

### 3. Interpret Patterns

After answers accumulate, summarize the signal in plain language. Use this table as guidance, not as rigid scoring.

| Repeated Signal | Likely Growth Lane |
| --- | --- |
| Papers, research code, experiments, algorithm behavior | Research-oriented MLE / Research Engineer |
| Agent failure modes, evals, feedback loops | Agent/model eval systems |
| Runtime, latency, cost, reliability | AI platform / runtime systems |
| RAG, ranking, grounding, retrieval quality | Search/RAG/relevance systems |
| Company trajectory, people, technical bets, cross-functional direction | Staff+ technical direction / research-adjacent leadership |
| Product impact, users, fast iteration | Applied AI product/platform engineer |

When the user chooses multiple lanes, find the center of gravity.

Examples:
- Evals + runtime + research-adjacent team -> "research-adjacent agent/eval systems builder."
- RAG + product impact + users -> "applied LLM product MLE focused on retrieval and grounding."
- Runtime + performance + infra pain tolerance -> "AI inference/runtime platform engineer."
- Technical bets + team translation + company trajectory -> "Staff+ technical direction with enough depth to lead bets."

### 4. Separate Preference From Fear

If the user says "but that path is too competitive" or "the other path is deeper," reflect the distinction:

```text
I want to separate two things:

- Preference signal: what you repeatedly chose when asked about energy and dream jobs.
- Strategy fear: what sounds safer, more legible, or less crowded.

We should respect the market, but not let fear pick the identity.
```

Then ask one pressure-test question:

```text
If nobody rewarded the path for prestige, which work would you still want to do for the next 6 months?
```

### 5. Land The Growth Thesis

End with a concise output:

```text
Your likely growth direction is:

[Lane name]

One-sentence thesis:
> [Identity sentence]

3-6 month focus stack:
1. [Primary skill]
2. [Secondary skill]
3. [Supporting skill]
4. [Career artifact or leadership practice]

Deprioritize:
- [What not to study]
- [What not to over-optimize]

Proof artifact:
- [One concrete artifact that demonstrates the lane]
```

## Example Final Outputs

### Research-Adjacent Agent/Eval Systems Builder

```text
Your direction is research-adjacent agent/eval systems builder.

Thesis:
> I build systems that make frontier model or agent ideas testable, reliable, and usable.

3-6 month focus stack:
1. Agent/model eval systems: task suites, traces, judges, failure taxonomies, regression evals.
2. Agent runtime reliability: tool use, context, retries, observability, latency/cost.
3. Research fluency: read papers and research code well enough to build the missing system.
4. Technical direction: write short memos comparing bets and recommending what to build.

Deprioritize generic full-stack, broad cloud certification study, and pure algorithm research unless it supports the artifact.

Proof artifact:
- A working eval + runtime harness for agent tasks, plus a technical memo explaining failures, tradeoffs, and next bets.
```

### Post-Training Research Engineer

```text
Your direction is post-training research engineer.

Thesis:
> I improve model behavior through data, reward/eval design, and rigorous experiments.

3-6 month focus stack:
1. SFT, DPO, GRPO/PPO, reward modeling fundamentals.
2. Research-code reading and reproduction.
3. Evaluation design and failure analysis.
4. Concise experiment writeups.

Proof artifact:
- A mini post-training lab with reproducible runs, evals, and a writeup of what changed behavior.
```

### AI Runtime Platform Engineer

```text
Your direction is AI runtime platform engineer.

Thesis:
> I make AI systems fast, reliable, observable, and cost-effective enough to serve real users.

3-6 month focus stack:
1. Inference serving, batching, caching, routing, cost/latency tradeoffs.
2. Reliability and observability for LLM/agent systems.
3. Distributed systems fundamentals for AI workloads.
4. Platform APIs and developer experience.

Proof artifact:
- A production-style agent runtime with metrics, traces, retries, cost/latency dashboard, and load-test notes.
```

## Guardrails

- Do not pretend the quiz is a psychometric assessment.
- Do not over-index on market popularity if the user's energy points elsewhere.
- Do not push pure research as automatically higher status.
- Do not push generalist SWE as automatically safer.
- Do not include names, employers, family details, locations, or personal history unless the user brings them up in the current session and wants them included.
- If the user asks for a written plan, keep it concrete and time-boxed.
