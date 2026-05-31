---
name: coding-interview-companion
description: "End-to-end coding interview prep for algorithms, data structures, and practical coding rounds. Use when preparing technical interview problems in solve, learn, or mock mode: first locate the current problem directory, then use its input/ and output/ subdirectories. Solve mode analyzes input/0_requirements.md and creates interview-ready solutions, learn mode defaults to interactive Q&A with interview-relevant auto-notes, mock mode simulates an interviewer and reviews the user's attempt."
---

# Coding Interview Companion

**Purpose:** Complete lifecycle support for coding interview prep, from requirements analysis through solution writing, learning review, and mock interviews.

**Important:** First identify the current problem directory. All `input/` and `output/` paths are subdirectories of that problem directory, not necessarily the shell's current directory.

## Problem Directory Resolution

Before reading or writing files, set `problem_dir`:

1. If the user provides a problem directory or file path, use that directory. If they provide a file inside `input/` or `output/`, use its parent problem directory.
2. Otherwise, if the current directory contains `input/` or `output/`, use the current directory.
3. Otherwise, search nearby child directories for `input/0_requirements.md`, `input/*.md`, or `output/deep_dive.md` and choose the directory that matches the current problem context.
4. If multiple directories match and the current problem is ambiguous, ask one concise clarification question.

After resolving `problem_dir`, use:
- `problem_input = <problem_dir>/input`
- `problem_output = <problem_dir>/output`

Create `problem_input` and `problem_output` if the selected mode needs them and they do not exist.

## Quick Setup

1. **Create a directory** for your interview prep:
   ```bash
   mkdir my-interview-prep
   cd my-interview-prep
   ```

2. **Create input folder and requirements file:**
   ```bash
   mkdir input
   echo "# Interview Round
   - Type: Coding + System Design + Behavioral
   - Date: June 2026
   - Focus areas: algorithms, data structures
   " > input/0_requirements.md
   ```

3. **Invoke the skill** from this directory or pass the problem directory explicitly:
   ```
   /coding-interview-companion
   
   "Solve mode for ./my-interview-prep"
   ```

## Directory Structure

All paths are **relative to the resolved problem directory**:

```
problem-directory/
  input/
    0_requirements.md          # Raw interview info (you create this)
    <problem_name>.md          # Problem statement (created by solve mode)
    <problem_name>.py          # Skeleton/interface (created by solve mode)
  output/
    interview_discussion.md         # Interview-ready answers (created by solve mode)
    <problem_name>_solution.py      # Full reference solution (created by solve mode)
    deep_dive.md                    # Broader concepts and deep dives (created/updated by solve and learn)
    learn_notes.md                  # Learning session notes (created by learn mode, merged into deep_dive)
    mock_<problem_name>_<part>.py   # Mock scaffold and user attempt (created in mock mode)
    mock_feedback.md                # Mock interview feedback (created by mock mode)
```

The skill will:
- **Resolve:** `problem_dir` before any file operation
- **Read from:** `<problem_dir>/input/0_requirements.md`
- **Write to:** `<problem_dir>/input/` and `<problem_dir>/output/`
- **Create directories** if they don't exist

## Modes

All paths are relative to the resolved `problem_dir`:

- **Solve mode:** Read `<problem_dir>/input/0_requirements.md`, create frozen problem setup files in `<problem_dir>/input/`, then generate `<problem_dir>/output/interview_discussion.md`, `<problem_dir>/output/<problem_name>_solution.py`, and `<problem_dir>/output/deep_dive.md`.
- **Learn mode:** Default to interactive Q&A: answer the user's immediate interview-prep questions, ask targeted follow-ups when useful, record only interview-relevant notes in `<problem_dir>/output/learn_notes.md`, and merge durable takeaways into `<problem_dir>/output/deep_dive.md`.
- **Mock mode:** Interview as a hiring engineer, create/review `<problem_dir>/output/mock_<problem_name>_<part>.py`, and record feedback in `<problem_dir>/output/mock_feedback.md`.

---

## Solve Mode Workflow

Use this workflow to analyze an interview round and produce interview-ready solutions.

### Phase 1: Requirements Analysis

All file operations are relative to the resolved `problem_dir`.

1. Read `<problem_dir>/input/0_requirements.md`:
   - Identify all interview problems, constraints, follow-ups, and context.
   - If the requirements reference multiple problems or parts, break them into discrete problems.
   - Surface any ambiguities early.

2. Create problem setup files in `<problem_dir>/input/`:
   - For each distinct problem, create `<problem_dir>/input/<problem_name>.md` with:
     - Problem statement (clean, formatted for reference)
     - Input/output contract
     - Constraints and edge cases
     - Example test cases
     - Follow-up questions or variations
   - For coding problems, create `<problem_dir>/input/<problem_name>.py` with:
     - Public function/class signatures and type hints (from problem description)
     - Docstrings explaining the interface
     - Stub bodies with `raise NotImplementedError()`
     - Keep this file frozen for learn and mock modes; write reference solutions and attempts under `<problem_dir>/output/`.

3. Brief summary:
   - Recap the problem landscape and what you'll solve in order.
   - Call out any non-obvious constraints or tradeoffs.

### Phase 2: Solve Each Problem

For each problem in order:

1. **Approach & Design:**
   - State the input/output contract and key invariants.
   - Outline your approach, complexity, and why you chose it.
   - Compare with alternative approaches if relevant.

2. **Implementation (Coding Problems):**
   - Implement in `<problem_dir>/output/<problem_name>_solution.py` with:
     - Docstrings and type hints
     - Concise comments on non-obvious logic (pointers, state, edge cases, base cases, DP transitions)
     - Interview-appropriate style: clear over clever
   - Add focused tests or a small `if __name__ == "__main__":` smoke-test block when useful.
   - Test thoroughly; include edge cases in reasoning and report the command you ran.

3. **Write `<problem_dir>/output/interview_discussion.md`:**
   - Create one section per problem with:
     - **Problem Statement** (condensed from input)
     - **Key Insights** (2-3 bullet points: what makes this hard, what's the aha moment)
     - **Approach** (pseudocode + explanation, not full code)
     - **Complexity** (time/space with reasoning)
     - **Code Walkthrough** (short snippets + explanation, not full listing)
     - **Edge Cases** (how the solution handles them)
     - **Follow-Ups** (how to extend, optimize, or adapt)
   - Write as if explaining to an interviewer: conversational, confident, complete.

4. **Create `<problem_dir>/output/deep_dive.md`:**
   - One section per problem with:
     - **Context** (where this pattern appears, what makes it Interview-hard)
     - **Mental Model** (how to think about the problem without code)
     - **Solution & Why** (full explanation + concise code snippets)
     - **Complexity Analysis** (detailed reasoning)
     - **Variants & Trade-offs** (alternative approaches and when to use them)
     - **Common Pitfalls** (what candidates often miss)
     - **Related Concepts** (link to your study notes if available)
   - Deeper and broader than `interview_discussion.md`; assume you know the basics.

5. **Walk-through:**
   - Summarize each solved problem: key insight, approach, complexity.
   - Mention which output files were created or updated.

---

## Learn Mode Workflow

Use this workflow as an interactive Q&A companion with auto-notes. Do not edit frozen files in `<problem_dir>/input/`.

### Setup

1. Confirm you're in learn mode and state which problem/concept you're exploring.
2. Default to answering the user's next question directly; offer a short menu only if the user has not chosen a focus.
3. Create `<problem_dir>/output/learn_notes.md` if it does not exist.

### During Learning

1. **Interactive Q&A Loop:**
   - Treat the user's question as the driver of the session.
   - Answer the immediate question first, then add only the context needed to make it interview-useful.
   - Ask at most one targeted follow-up or check-for-understanding question before continuing.
   - If the user says "next", continue to the next natural interview-relevant question or subtopic without extra framing.

2. **Explanations:**
   - Use plain language first, then technical depth.
   - Keep answers concise; answer the immediate question, then add context.
   - Use one small concrete example per explanation; avoid stacking examples.
   - Tie code to the problem statement and `<problem_dir>/output/deep_dive.md` when available.
   - Highlight what you should say in a real interview.

3. **Answer Questions:**
   - When you ask about solution details, approach trade-offs, complexity, or edge cases, answer fully.
   - If you notice confusion, clarify the mental model before going deeper.
   - Point out common pitfalls and how tests or examples expose them.

4. **Auto-Notes (Default):**
   - For every interview-relevant question or insight, record it in `<problem_dir>/output/learn_notes.md`:
     - **Q:** Your question (concise)
     - **A:** The answer (1-3 sentences)
     - **Why it matters:** One sentence on the mental model or edge case
     - **Example:** One-line example if it clarified something
   - Do NOT take notes for workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.
   - Keep notes chronological and slightly raw.

5. **Merge into Deep Dive (Proactive):**
   - As you finish learning a problem, merge insights from `<problem_dir>/output/learn_notes.md` into `<problem_dir>/output/deep_dive.md`:
     - Add a "Learning Notes & Refinements" subsection.
     - Distill Q&A entries into 1-2 sentence takeaways.
     - Link each takeaway to the relevant solution section.
     - Delete the merged entries from `<problem_dir>/output/learn_notes.md` and update the date.
   - Keep `<problem_dir>/output/deep_dive.md` interview-ready; use it as the reference before a real interview.

6. **Interactive & Pause:**
   - After answering, keep the session open for the next question.
   - Ask one check-for-understanding question only when it would expose a likely interview misconception.

### End of Learn Session

- Confirm that `<problem_dir>/output/learn_notes.md` is cleaned up and merged into `<problem_dir>/output/deep_dive.md`.
- Summarize what you now understand differently compared to the start.

---

## Mock Mode Workflow

Use this workflow to simulate a real interview with step-by-step feedback.

### Setup

1. **Frame the interview:**
   - State only the interview problem and your role as interviewer; do not tell the user the sequence of steps to follow unless they explicitly ask about process.
   - Do not reveal the full intended solution upfront.
   - Keep feedback in interviewer tone: concise, probing, honest.
   - Ask exactly one question per assistant turn in mock mode; do not bundle multiple numbered questions or prompts in the same turn.
   - Treat the exchange like a real interview: do not coach, narrate what the candidate should do next, or provide a checklist of tasks.

2. **Create problem scaffold:**
   - Create `<problem_dir>/output/mock_<problem_name>_<part>.py` with public function/class signatures and type hints only.
   - Stub bodies with `raise NotImplementedError()`.
   - Do NOT include algorithm hints, helper functions, test harnesses, or expected outputs.

### During Mock

1. **Clarification Questions (Your Turn):**
   - When you ask clarifying questions, I answer directly with constraints and examples.
   - I pick reasonable assumptions for ambiguous points.
   - I do NOT volunteer hidden edge cases or gotchas.
   - Ask one clarification question at a time, then wait for the answer before asking the next question.
   - Do not suggest which clarifying questions to ask; wait for the candidate to drive this phase.
   - Record Q&A in `<problem_dir>/output/mock_feedback.md`.

2. **Approach Explanation (Your Turn):**
   - When you outline your approach, I give concise feedback:
     - Correct or missing constraints? Call them out.
     - Overcomplicating? Ask a probing question that exposes the issue; do not volunteer hints unless the candidate asks for clarification.
     - Prune the idea? Validate it and move forward.
   - End feedback with at most one targeted next question.
   - Record approach feedback in `<problem_dir>/output/mock_feedback.md`.

3. **Coding (Your Turn):**
   - You implement in the scaffolded `<problem_dir>/output/mock_<problem_name>_<part>.py` or in a matching notebook if requested.
   - I do NOT edit files or paste full implementations.
   - Do not provide hints, API reminders, or solution direction unless the candidate explicitly asks for clarification or help.
   - Record hints in `<problem_dir>/output/mock_feedback.md`.

4. **Code Review (My Turn):**
   - When you say "done", I review `<problem_dir>/output/mock_<problem_name>_<part>.*`:
     - List correctness bugs first, then edge cases, complexity, clarity, communication.
     - Provide smallest conceptual fix for each issue (no auto-patching).
     - Ask which tests you wrote; if none, note that test coverage was your responsibility.
   - Record findings in `<problem_dir>/output/mock_feedback.md`.

5. **Follow-up:**
   - If there are multiple coding parts, repeat Setup and During Mock steps 1-4 for the next part.
   - If there are no more coding parts, ask one design or scaling follow-up question at a time.

6. **Closing (My Turn):**
   - Give a verdict: "pass/lean pass/lean no/no-hire for this round" (or score if you ask).
   - Include 2-4 focused improvements for the next attempt.
   - Ask one follow-up question an interviewer might ask (optimization, concurrency, testing strategy, etc.).
   - Record verdict, improvements, and follow-up in `<problem_dir>/output/mock_feedback.md`.

### Note-Taking (Proactive)

- Record every interview-relevant turn in `<problem_dir>/output/mock_feedback.md`:
  - Your clarification Qs and my answers
  - Your approach + my feedback
  - Hints given during coding
  - Code review findings
  - Final verdict and improvements
- This becomes a learning record and a self-review guide.
- Do not record workflow, environment, IDE, file-conversion, or tooling questions unless explicitly asked.

---

## Tips for Best Results

- **Solve mode:** Create interview-ready `interview_discussion.md` first; it's your cheat sheet before a real interview.
- **Learn mode:** Default to Q&A with auto-notes; merge notes into `deep_dive.md` once a topic is stable.
- **Mock mode:** Treat it like a real interview: no Googling, no pausing to think for too long, explain as you code.
- **Between rounds:** Review `interview_discussion.md` to warm up, then run a mock to stress-test under time pressure.

---

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|-----------|-----------------|------------------|
| `<problem_dir>/input/0_requirements.md` | Raw interview info | You | No | No |
| `<problem_dir>/input/<problem>.md` | Problem statement | Solve | No | No |
| `<problem_dir>/input/<problem>.py` | Public interface | Solve | No | No |
| `<problem_dir>/output/interview_discussion.md` | Interview cheat sheet | Solve | Yes (optional) | Reference |
| `<problem_dir>/output/<problem>_solution.py` | Full solution | Solve | No | No |
| `<problem_dir>/output/deep_dive.md` | Concept deep dives | Solve + Learn | Yes (merge notes) | Reference |
| `<problem_dir>/output/learn_notes.md` | Raw learning notes | Learn | Yes (merge into deep_dive) | No |
| `<problem_dir>/output/mock_<problem_name>_<part>.py` | Your attempt | You | No | Yes |
| `<problem_dir>/output/mock_feedback.md` | Interview feedback | Mock | No | Record |
