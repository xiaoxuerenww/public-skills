---
name: databricks-ml-fundamentals-prep
description: Use for Julie's Databricks ML fundamentals interview-prep topic directories when asked to set up or update mock artifacts, convert /Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md into topic-level mock prep, infer the topic from a directory name such as 3_transformer or use an explicitly specified topic, refresh a teach-style course from mock_question_bank.md, or keep index.md, solution.md, deep_dive.md, learn_notes.md, mock.md, and mock_question_bank.md consistent. Especially relevant under /Users/xue/Documents/work/0_databricks/0_db_ml_fundamental for topics such as linear regression, Word2Vec, transformer attention/QKV, evaluation, retrieval, and debugging.
---

# Databricks ML Fundamentals Prep

## Purpose

Build and maintain Julie's Databricks ML fundamentals topic directories as reusable interview-prep workspaces. Preserve two separate modes:

- **Mock mode artifacts:** `mock_question_bank.md`, `solution.md`, and `mock.md`.
- **Teach/course artifacts:** `index.md`, `solution.md`, `deep_dive.md`, and `learn_notes.md`.

When a topic directory has both modes, keep `solution.md` as the shared file: preserve the mock answer key and append teach/course prep below it.

## Topic Directory Resolution

1. If Julie provides a topic directory, use it.
2. If she provides a file, walk upward to the nearest directory containing `mock_question_bank.md`, `mock.md`, `index.md`, `solution.md`, or `deep_dive.md`.
3. If no topic is explicit, use the current directory only if it is already a topic directory.
4. If multiple nearby topic directories match, ask one concise clarification question.

## Default Question Bank and Topic Selection

Use this source bank by default unless Julie explicitly provides another question-bank file:

```text
/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md
```

Topic selection order:

1. If Julie specifies a topic, use that exact topic string to find the relevant section in the default bank.
2. Otherwise infer the topic from `topic_dir` name.
3. Normalize directory names by removing leading numeric prefixes and separators, then matching meaningful words. Examples:
   - `1_linear_regression` -> linear regression
   - `2_word2vec` -> Word2Vec, embeddings, representation learning
   - `3_transformer` -> transformer architecture and attention
4. Read the default bank and select the closest matching topic section, plus any nearby packet or checklist items that explicitly name the topic.
5. If the inferred topic maps to more than one plausible bank section, ask one concise clarification question rather than mixing sections silently.
6. If the topic has no matching section in the default bank, report the gap and ask Julie for a topic label or source-bank path.

For `3_transformer`, use the bank sections named `Transformer Architecture & Attention`, `7. Transformer Architecture and Attention`, and relevant items from `Packet C: Deep Learning / Transformer 45-Minute Mock`.

## Source Grounding Rules

- Read the selected source question-bank section completely before creating or updating mock artifacts. Skim the surrounding headings enough to ensure the topic boundary is correct.
- For this Databricks prep family, default to `/Users/xue/Documents/work/0_databricks/0_db_ml_fundamental/0_db_ml_fundamentals_question_bank.md`; use another local source bank only when Julie explicitly provides it.
- Do not invent new source questions unless Julie explicitly asks to broaden the bank.
- Keep the round framed as conversational ML fundamentals, usually no coding, with Staff/Senior Staff MLE depth.
- Emphasize mechanism, equations, assumptions, tensor shapes, failure modes, debugging discipline, and practical Databricks-relevant retrieval/eval/agent grounding.

## Workflow A: Set Up Mock Artifacts

Use when Julie asks to set up, prepare, or initialize a mock for a topic directory.

1. Resolve `topic_dir` and source question bank.
2. Resolve the topic explicitly from Julie's request or implicitly from `topic_dir` name.
3. Create or update `mock_question_bank.md` from the selected source-bank topic section.
   - Every entry must be a Markdown checkbox.
   - Include candidate-facing question, tests, expected answer/evaluation notes, grounding, and blank `Asked:`.
   - Keep unchecked boxes unless a completed mock actually asked the question.
4. Create or update root `solution.md` as the interviewer answer key.
   - Include one `### Q:` section for every question in `mock_question_bank.md`.
   - Preserve existing answer-key content when present.
   - Add `Needs answer source` rather than unsupported claims when guidance is missing.
5. Create or update `mock.md`.
   - Include only candidate-facing setup, source references, transcript placeholders, feedback placeholders, verdict, weaknesses, next review, and next-round probes.
   - Do not leak answer keys in `mock.md`.
6. Verify counts:
   - `rg -c "^- \\[ \\] \\*\\*Q:\\*\\*" mock_question_bank.md`
   - `rg -c "^### Q:" solution.md`

## Workflow B: Update Teach Course Artifacts

Use when Julie invokes `$teach update <topic_dir>/`, asks to update the course, or points at a topic with `mock_question_bank.md`.

1. Read `mock_question_bank.md` completely.
2. Read existing `solution.md` completely and treat the mock answer key as source material.
3. Read existing `index.md`, `deep_dive.md`, and `learn_notes.md` if present.
4. Create or refresh only:
   - `index.md`
   - `solution.md`
   - `deep_dive.md`
   - `learn_notes.md`
5. Do not create `question_bank.md`; teach quiz mode should use `mock_question_bank.md`.
6. Preserve `mock_question_bank.md` and `mock.md` as source/mock artifacts.
7. If `solution.md` already contains the mock answer key, append teach prep below a divider such as `# Active Teach Prep` instead of replacing it.

## Required Course Content

`index.md` must include:

- Mission, success criteria, scope, and out-of-scope items.
- Current status.
- How to use the course across sessions.
- Course docs with wikilinks.
- `## Course tasks` with doc-reading tasks at the top:
  - `Read [[index]] to understand mission and progress. (5 min)`
  - `Read [[solution]] for the active lesson, drills, and Q&A. (15-25 min)`
  - `Read [[deep_dive]] for polished synthesis, formulas, glossary, sources, and quick review. (15-30 min)`
- One 30-second target answer or a clear link to it in `solution.md`.
- Must-answer list.
- Review schedule.
- `## Learning records`.
- Restart instructions.
- `## Legacy source files` only when legacy files actually exist.

`solution.md` must include:

- Existing mock answer key, preserved.
- Active lesson sequence.
- Worked answer templates.
- Retrieval/self-check drills.
- Short spoken interview phrasing.
- Pointers to `deep_dive.md`.

`deep_dive.md` must include:

- Durable synthesis organized by topic clusters and source questions.
- Key equations in display LaTeX blocks.
- Compact tables for shape flow, variants, traps, and tradeoffs.
- PyTorch or pseudocode snippets when they improve implementation intuition.
- Staff+ failure modes, debugging plans, and Databricks-relevant LLM/retrieval/eval implications.
- Source list pointing back to `mock_question_bank.md`, `solution.md`, and the original source bank.

`learn_notes.md` must be retained or created as the companion notes buffer. If older useful notes exist, preserve them and add a dated course-update note rather than replacing them with an empty placeholder.

## Integrity Audit

Before reporting completion:

1. Verify active docs exist and are non-empty: `index.md`, `solution.md`, `deep_dive.md`, `learn_notes.md`.
2. Verify all wikilinks in active docs resolve relative to `topic_dir`.
3. Verify `solution.md` has one `### Q:` answer-key entry per question in `mock_question_bank.md`.
4. Check `index.md` has mission, current status, course tasks, course links, learning records, review schedule, restart instructions, 30-second target answer, and must-answer list.
5. Do not delete or clean up unrelated legacy files unless Julie explicitly asks.
6. Mention unrelated dirty worktree changes only if they affect the requested update.

## Reporting

Report concisely:

- Active docs updated, using wikilinks.
- Mock/source artifacts preserved.
- Question and answer-key coverage counts.
- Wikilink and integrity-audit result.
- Any cleanup recommendation, without performing cleanup.
