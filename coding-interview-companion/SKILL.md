---
name: coding-interview-companion
description: End-to-end coding interview prep with solve/learn/mock modes. Use when preparing for technical interviews: solve mode analyzes requirements and builds interview-ready solutions, learn mode companions your understanding with auto-notes, mock mode simulates interviews with step-by-step feedback. Works with input/0_requirements.md and outputs to output/ folder (relative to current directory).
---

# Interview Problem Companion

**Purpose:** Complete lifecycle support for coding interview prep—from requirements analysis through mock interviews.

**Important:** This skill works with files relative to your current directory. All paths (input/, output/) are relative to where you invoke the skill.

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

3. **Invoke the skill** from this directory:
   ```
   /coding-interview-companion
   
   "Solve mode: I have these coding problems to prepare..."
   ```

## Directory Structure

All paths are **relative to your current working directory**:

```
current-directory/
  input/
    0_requirements.md          # Raw interview info (you create this)
    <problem_name>.md          # Problem statement (created by solve mode)
    <problem_name>.py          # Skeleton/interface (created by solve mode)
  output/
    interview_solutions.md     # Interview-ready answers (created by solve mode)
    <problem_name>.py          # Full solution (created by solve mode)
    deep_dive.md              # Broader concepts & deep dives (created/updated by solve & learn)
    learn_notes.md            # Learning session notes (created by learn mode, merged into deep_dive)
    my_solution.md/.py/.ipynb # Your solution attempts (reviewed by mock mode)
    mock_feedback.md          # Mock interview feedback (created by mock mode)
```

The skill will:
- **Read from:** `./input/0_requirements.md` (relative to current directory)
- **Write to:** `./input/` and `./output/` (relative to current directory)
- **Create directories** if they don't exist

## Modes

All paths are relative to your current directory:

- **Solve mode:** Read `./input/0_requirements.md`, create problem setup files in `./input/`, solve in depth/breadth, generate `./output/interview_solutions.md` + solution code + `./output/deep_dive.md`.
- **Learn mode:** Companion your learning journey, auto-take notes in `./output/learn_notes.md`, proactively merge into `./output/deep_dive.md`.
- **Mock mode:** Interview as hiring engineer, review `./output/my_solution.*`, give step-by-step feedback, take notes in `./output/mock_feedback.md`.

---

## Solve Mode Workflow

Use this workflow to analyze an interview round and produce interview-ready solutions.

### Phase 1: Requirements Analysis

All file operations are relative to your current directory.

1. Read `./input/0_requirements.md` (relative to current directory):
   - Identify all interview problems, constraints, follow-ups, and context.
   - If the requirements reference multiple problems or parts, break them into discrete problems.
   - Surface any ambiguities early.

2. Create problem setup files in `./input/`:
   - For each distinct problem, create `./input/<problem_name>.md` with:
     - Problem statement (clean, formatted for reference)
     - Input/output contract
     - Constraints and edge cases
     - Example test cases
     - Follow-up questions or variations
   - For coding problems, create `./input/<problem_name>.py` with:
     - Public function/class signatures and type hints (from problem description)
     - Docstrings explaining the interface
     - Stub bodies with `raise NotImplementedError()`

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
   - Implement in `output/<problem_name>.py` with:
     - Docstrings and type hints
     - Concise comments on non-obvious logic (pointers, state, edge cases, base cases, DP transitions)
     - Interview-appropriate style: clear over clever
   - Test thoroughly; include edge cases in reasoning.

3. **Write `output/interview_solutions.md`:**
   - Create one section per problem with:
     - **Problem Statement** (condensed from input)
     - **Key Insights** (2-3 bullet points: what makes this hard, what's the aha moment)
     - **Approach** (pseudocode + explanation, not full code)
     - **Complexity** (time/space with reasoning)
     - **Code Walkthrough** (short snippets + explanation, not full listing)
     - **Edge Cases** (how the solution handles them)
     - **Follow-Ups** (how to extend, optimize, or adapt)
   - Write as if explaining to an interviewer: conversational, confident, complete.

4. **Create `output/deep_dive.md`:**
   - One section per problem with:
     - **Context** (where this pattern appears, what makes it Interview-hard)
     - **Mental Model** (how to think about the problem without code)
     - **Solution & Why** (full explanation + concise code snippets)
     - **Complexity Analysis** (detailed reasoning)
     - **Variants & Trade-offs** (alternative approaches and when to use them)
     - **Common Pitfalls** (what candidates often miss)
     - **Related Concepts** (link to your study notes if available)
   - Deeper and broader than `interview_solutions.md`; assume you know the basics.

5. **Walk-through:**
   - Summarize each solved problem: key insight, approach, complexity.
   - Mention which output files were created or updated.

---

## Learn Mode Workflow

Use this read-only workflow to companion your learning and auto-document insights.

### Setup

1. Confirm you're in learn mode and state which problem/concept you're exploring.
2. Outline what you'll walk through (e.g., "solution code walkthrough", "complexity analysis", "follow-up adaptations").

### During Learning

1. **Explanations:**
   - Use plain language first, then technical depth.
   - Keep answers concise; answer the immediate question, then add context.
   - Use one small concrete example per explanation; avoid stacking examples.
   - Tie code to problem statement and deep_dive.md.
   - Highlight what you should say in a real interview.

2. **Answer Questions:**
   - When you ask about solution details, approach trade-offs, complexity, or edge cases, answer fully.
   - If you notice confusion, clarify the mental model before going deeper.
   - Point out common pitfalls and how tests or examples expose them.

3. **Take Notes (Proactive):**
   - For every interview-relevant question or insight, record it in `output/learn_notes.md`:
     - **Q:** Your question (concise)
     - **A:** The answer (1-3 sentences)
     - **Why it matters:** One sentence on the mental model or edge case
     - **Example:** One-line example if it clarified something
   - Do NOT take notes for workflow/environment/tooling questions.
   - Keep notes chronological and slightly raw.

4. **Merge into Deep Dive (Proactive):**
   - As you finish learning a problem, merge insights from `learn_notes.md` into `output/deep_dive.md`:
     - Add a "Learning Notes & Refinements" subsection.
     - Distill Q&A entries into 1-2 sentence takeaways.
     - Link each takeaway to the relevant solution section.
     - Delete the merged entries from `learn_notes.md` and update the date.
   - Keep `deep_dive.md` interview-ready; use it as the reference before a real interview.

5. **Interactive & Pause:**
   - After explaining a concept or showing code, ask one check-for-understanding question.
   - Offer to dive deeper into any section.

### End of Learn Session

- Confirm that `learn_notes.md` is cleaned up and merged into `deep_dive.md`.
- Summarize what you now understand differently compared to the start.

---

## Mock Mode Workflow

Use this workflow to simulate a real interview with step-by-step feedback.

### Setup

1. **Frame the interview:**
   - State: "I'm your interviewer for <problem>. Ask clarifying questions, then explain your approach, then code."
   - Do not reveal the full intended solution upfront.
   - Keep feedback in interviewer tone: concise, probing, honest.

2. **Create problem scaffold:**
   - Create `input/mock_<problem_name>.py` with public function/class signatures and type hints only.
   - Stub bodies with `raise NotImplementedError()`.
   - Do NOT include algorithm hints, helper functions, test harnesses, or expected outputs.

### During Mock

1. **Clarification Questions (Your Turn):**
   - When you ask clarifying questions, I answer directly with constraints and examples.
   - I pick reasonable assumptions for ambiguous points.
   - I do NOT volunteer hidden edge cases or gotchas.
   - Record Q&A in `output/mock_feedback.md`.

2. **Approach Explanation (Your Turn):**
   - When you outline your approach, I give concise feedback:
     - Correct or missing constraints? Call them out.
     - Overcomplicating? Suggest a simpler direction without full code.
     - Prune the idea? Validate it and move forward.
   - Record approach feedback in `output/mock_feedback.md`.

3. **Coding (Your Turn):**
   - You implement in `output/my_solution.py` or `output/my_solution.ipynb`.
   - I do NOT edit files or paste full implementations.
   - If you ask for mid-code help, I give localized hints or API reminders only.
   - Record hints in `output/mock_feedback.md`.

4. **Code Review (My Turn):**
   - When you say "done", I review `output/my_solution.*`:
     - List correctness bugs first, then edge cases, complexity, clarity, communication.
     - Provide smallest conceptual fix for each issue (no auto-patching).
     - Ask which tests you wrote; if none, note that test coverage was your responsibility.
   - Record findings in `output/mock_feedback.md`.

5. **Closing (My Turn):**
   - Give a verdict: "pass/lean pass/lean no/no-hire for this round" (or score if you ask).
   - Include 2-4 focused improvements for the next attempt.
   - Ask one follow-up question an interviewer might ask (optimization, concurrency, testing strategy, etc.).
   - Record verdict, improvements, and follow-up in `output/mock_feedback.md`.

### Note-Taking (Proactive)

- Record every turn in `output/mock_feedback.md`:
  - Your clarification Qs and my answers
  - Your approach + my feedback
  - Hints given during coding
  - Code review findings
  - Final verdict and improvements
- This becomes a learning record and a self-review guide.

---

## Tips for Best Results

- **Solve mode:** Create interview-ready `interview_solutions.md` first; it's your cheat sheet before a real interview.
- **Learn mode:** Merge notes into `deep_dive.md` immediately; it keeps your reference doc sharp.
- **Mock mode:** Treat it like a real interview: no Googling, no pausing to think for too long, explain as you code.
- **Between rounds:** Review `interview_solutions.md` to warm up, then run a mock to stress-test under time pressure.

---

## File Reference

| File | Purpose | Created by | Edited in Learn | Reviewed in Mock |
|------|---------|-----------|-----------------|------------------|
| `input/0_requirements.md` | Raw interview info | You | No | No |
| `input/<problem>.md` | Problem statement | Solve | No | No |
| `input/<problem>.py` | Public interface | Solve | No | No |
| `output/interview_solutions.md` | Interview cheat sheet | Solve | Yes (optional) | Reference |
| `output/<problem>.py` | Full solution | Solve | No | No |
| `output/deep_dive.md` | Concept deep dives | Solve + Learn | Yes (merge notes) | Reference |
| `output/learn_notes.md` | Raw learning notes | Learn | Yes (merge into deep_dive) | No |
| `output/my_solution.py` | Your attempt | You | No | Yes |
| `output/mock_feedback.md` | Interview feedback | Mock | No | Record |
