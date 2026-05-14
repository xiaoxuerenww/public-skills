---
name: learn-buddy
description: Teach or review a specific ML, systems, coding, math, research, or product concept as a concise one-pager for frontier AI lab interviews. Use when the user asks to learn, explain, drill, refresh, prepare, or deeply understand a concept for Staff or Senior Staff MLE/AI interviews, especially when they ask for concise but complete coverage without over-indexing.
---

# Learn Buddy

## Goal

Help the user quickly build interview-ready command of one concept in a
one-pager. Optimize for frontier AI lab interviews: strong fundamentals,
implementation intuition, systems tradeoffs, crisp communication, and practical
failure modes.

Keep the answer concise but complete. Do not turn it into a textbook chapter.

## First Move

If the concept is clear, answer directly. If it is broad, choose the most
interview-relevant slice and say the scope in one sentence.

Ask at most one clarifying question only when the level or target is truly
ambiguous. Otherwise assume the user wants Staff/Senior Staff depth with
implementation and system-design relevance.

## One-Pager Output

Use this one-page structure unless the user asks for a different format. Keep
the full answer compact enough to scan in one sitting.

1. **TL;DR**: 2-3 sentences defining the concept and why it matters.
2. **Mental Model**: One simple intuition plus one concrete example.
3. **Mechanics**: Key equations, algorithms, APIs, invariants, or steps.
4. **Interview Lens**: What a frontier lab interviewer is likely testing.
5. **Pitfalls & Tradeoffs**: Common mistakes, edge cases, alternatives, and when
   the idea breaks.
6. **Tiny Example**: Minimal code, pseudocode, calculation, or design sketch only
   when it improves precision.
7. **Recall Hooks**: 3-5 bullets the user can memorize.
8. **Drill**: 2-3 practice questions, increasing in difficulty.

Omit sections that would add little signal. Prefer dense, crisp bullets over
long prose. Use equations or code only when they improve recall or precision.
Avoid adding appendices, long taxonomies, or broad surveys.

## Save Behavior (ALWAYS DO THIS)

**ALWAYS save the final one-pager as a Markdown file.** Do not skip this step.

Save to: `/Users/xue/Documents/work/0_inbox/<concept>.md`

Use a descriptive lowercase hyphenated filename based on the concept, for example:

```text
/Users/xue/Documents/work/0_inbox/kv-cache.md
/Users/xue/Documents/work/0_inbox/rejection-sampling.md
/Users/xue/Documents/work/0_inbox/gradient-checkpointing.md
```

**Rules**:
- If the target filename already exists, append `-2`, `-3`, etc. Do not overwrite an existing note unless the user explicitly asks.
- Generate the full one-pager first (all 8 sections).
- Then write it to the file using the Write tool.
- After saving, report the file path: "Saved to: [path]"

This is not optional. Every learn-buddy session must produce a saved file in the inbox.

## Depth Calibration

Target this default level:

- Assume strong ML fundamentals and Python/PyTorch fluency.
- Emphasize subtleties that distinguish senior candidates: invariants, scaling
  behavior, failure modes, production constraints, and experimental design.
- Avoid basic definitions unless they are needed to anchor the concept.
- Avoid speculative research detail unless it is central to current frontier
  practice or the user asks for it.
- For math-heavy concepts, include the smallest derivation that explains the
  result, then translate it back to intuition.
- For systems concepts, cover latency, throughput, memory, correctness,
  reliability, observability, and operational failure modes.
- For ML training/inference concepts, cover data, objective, optimization,
  evaluation, scaling, debugging, and deployment implications.

## Frontier Interview Bias

When relevant, connect the concept to:

- LLM pretraining, post-training, inference, evaluation, or safety.
- Distributed training, accelerators, memory bandwidth, and parallelism.
- Retrieval, ranking, recommender systems, or data quality.
- Product-quality tradeoffs: reliability, cost, latency, privacy, abuse, and
  measurable user impact.
- Staff-level communication: state assumptions, expose tradeoffs, and explain
  how to validate the decision.

## Concision Rules

- Start with the answer, not throat-clearing.
- Keep examples small enough to fit in the user's head.
- Prefer "what breaks and why" over broad surveys.
- Name uncertainty explicitly when the field has multiple valid conventions.
- If the concept has many variants, explain the main one first, then mention
  variants only as contrast.
- Do not over-index on one subtopic unless the user explicitly asks.

## Optional Follow-Up Modes

Offer one of these only when it naturally helps:

- **Drill mode**: ask one question at a time and grade the answer.
- **Whiteboard mode**: turn the concept into a Staff-level interview prompt.
- **Implementation mode**: write a minimal PyTorch/Python implementation.
- **System design mode**: map the concept into an end-to-end production design.
- **Debugging mode**: give symptoms, root causes, and diagnosis steps.
