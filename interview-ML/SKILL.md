---
name: interview-ML
description: "End-to-end Staff+ MLE interview prep: ML fundamentals quizzes, system design, concept teaching, and reference finding. Routes to the right sub-skill based on request type."
argument-hint: "What would you like to work on? (e.g., 'quiz me on transformers', 'design a rec system', 'teach me RLHF')"
---

# ML Interview Prep Router

Route the user's request to the narrowest matching sub-skill. Read the user's message, classify it, then invoke the correct skill.

## Routing Table

| Request pattern | Invoke skill | Examples |
|----------------|-------------|----------|
| Theory, fundamentals, quiz, drill, learn/practice/mock on ML concepts | `$ml-fundamentals-interview` | "Quiz me on attention", "Practice LLM fundamentals", "Mock ML interview" |
| System design, architecture, ranking, recommendation, serving, infra | `$ml-system-design-interview` | "Design a recommendation system", "System design mock", "Practice keyword outline" |
| Explain, teach, learn a concept, one-pager, course | `$teach` | "Teach me RLHF", "Explain KV cache", "Start a course on diffusion" |
| Find references, papers, materials for a topic | `$system-design-material-finder` | "Find papers on RAG", "Curate references for model serving" |
| Prep sprint, study plan, 1-week prep, track progress, prep status | `$one-week-prep` | "Prepare for ML breadth in 1 week", "Log today's study", "How am I doing on prep?" |

## Routing Rules

1. Read the user's request and any linked note or selection context.
2. If the request clearly matches one row, invoke that sub-skill immediately with the user's full request as input. Do not re-ask what they want.
3. If the request spans multiple skills (e.g., "find references on X then design it"), run them sequentially: invoke the first, complete it, then invoke the next.
4. If the request is ambiguous between exactly two skills, pick the more likely one and state which you chose in one sentence. Do not ask a clarifying question unless genuinely stuck.
5. If the user says just "interview-ML" with no further context, briefly list the five modes and ask what they'd like to work on.
