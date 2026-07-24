---
name: research-topic
description: "Research any topic from the web and synthesize a learning artifact. Use when the user asks to research, explore, survey, map out, or learn about a topic they don't yet understand, especially when current or external information matters. Produces a one-pager (default) or a multi-page deep dive."
argument-hint: "What topic would you like to research?"
---

The user wants to learn about a topic by gathering and synthesizing information from the web. This is not teaching from parametric knowledge (use `teach` for that) — this skill goes outward: searches, reads, and synthesizes from real sources.

## Branch Selection

Detect the branch from the user's input:

- **One-pager** (default) — user says "research X," "what's the landscape of X," "overview of X," "one-pager on X," or names a topic without asking for depth.
- **Deep dive** — user says "deep dive into X," "research X in depth," "multi-page on X," "thorough research on X," or the topic is clearly too broad for a single page.

If genuinely ambiguous, default to one-pager. The user can always ask for more depth after.

## Step 1: Scope

Parse the topic. Determine:

1. **Subject** — the core topic.
2. **Angle** — why the user wants to learn this (interview prep, evaluating a technology, general curiosity, building something). Infer from context; ask only if it materially changes what to research.
3. **Slice** — if the topic is too broad for the chosen branch, pick the most useful slice and state it in one sentence. For one-pagers, a topic like "distributed systems" needs slicing; "consistent hashing" does not.

Ask at most one clarifying question. If the topic is clear enough, proceed to the checkpoint.

### Checkpoint: confirm scope before researching

Before running any web searches, present the user with:

1. **Branch:** one-pager or deep dive.
2. **Subject:** the core topic as you understood it.
3. **Angle:** the inferred learning angle (or "general" if none).
4. **Slice:** if you narrowed the scope, state what you're covering and what you're leaving out.
5. **Subtopics** (deep dive only): the 3-7 subtopics you plan to cover, each with a one-line description.

Wait for the user to confirm, adjust, or add/remove subtopics before proceeding to Step 2. Do not start web searches until the user approves the scope.

## Step 2: Research

Delegate research to `/deep-research`. Construct a research prompt from the confirmed scope and invoke it.

### Building the research prompt

Compose a prompt for `/deep-research` that includes:

1. The confirmed **subject**, **angle**, and **slice** from Step 1.
2. The specific questions to answer, derived from the format template sections:
   - What is this and why does it matter? (TL;DR)
   - What are the key concepts, players, and approaches? (Landscape)
   - How does it work mechanically? (How It Works)
   - What are the alternatives and how do they compare? (Comparisons)
   - What are the tradeoffs, failure modes, and limitations? (Tradeoffs)
   - What is the current state and recent developments? (Current State)
3. **For deep dive:** include the confirmed subtopics and ask for coverage of each.
4. Ask for sources with URLs and dates when available.

Example research prompt:
```
Research RLHF (Reinforcement Learning from Human Feedback) for a Staff MLE
interview prep angle. Cover: what it is and why it matters, the training
pipeline (reward model, PPO), how it compares to DPO and RLAIF, known failure
modes (reward hacking, mode collapse), and the current state of the art as of
2026. Provide sources with URLs.
```

### After /deep-research completes

Review the research output. Extract and organize:

- **Key findings** per section of the output template.
- **Source URLs** with short annotations (what each covers, why trustworthy).
- **Conflicts or gaps** — areas where sources disagree or coverage is thin.

Apply these source quality filters:

- Prefer primary sources (papers, official docs, author blogs) over summaries and aggregators.
- Prefer sources with dates; flag undated claims about fast-moving fields.
- When sources conflict, surface the conflict — don't silently pick a side.

### Checkpoint: write skeleton and wait for review

After research is complete, write a **skeleton draft** to the output file(s) before full synthesis. The skeleton uses the same file structure as the final output (one file for one-pager, directory with index + subtopic files for deep dive) but contains only:

1. **Section headings** — the full heading structure from the format template.
2. **Key terms and keywords** — important concepts, names, and jargon discovered during research, placed under the relevant heading as bullet points.
3. **Key points** — 1-3 bullet points per section summarizing the main findings. Short phrases or single sentences, not full prose.
4. **Source links** — every source found during research, listed under the section(s) where it's relevant, in `[short label](url) — one-line annotation` format. Also collected in the Sources section at the bottom.
5. **Open gaps** — mark any section where research was thin or sources conflicted with `<!-- GAP: description -->`.

The skeleton is a real file the user can open in Obsidian, review, reorder sections, delete irrelevant points, add their own notes, or flag areas to expand. Save it to the output location (per Step 4 rules) and report the path using wikilinks.

Tell the user the skeleton is ready for review. Wait for the user to confirm, edit, or give direction before proceeding to Step 3. Do not synthesize until the user approves.

## Step 3: Synthesize

Take the skeleton (which the user may have edited) as the outline. Read it back before writing. Expand the skeleton into the full output following the format templates:

- **One-pager:** follow the template in [one-pager-format.md](one-pager-format.md).
- **Deep dive:** follow the template in [deep-dive-format.md](deep-dive-format.md).
- **Formatting:** Apply `$doc-formatter` conventions for scannable, visually structured documents:
  - Use **tables** for comparisons, alternatives, and tradeoffs (not bullet lists)
  - Add **TL;DR** summaries at major sections
  - Use **bold** for key terms and important distinctions
  - Structure **tension/tradeoffs** as comparison tables
  - Use callouts for tips/warnings/info

### Synthesis principles

- **Breadth first, then selective depth.** Cover the landscape before zooming in. The reader should understand what exists and how pieces relate before getting details on any one piece.
- **Concrete before abstract.** Lead with examples, systems, or use cases. Follow with principles and theory.
- **Tradeoffs over descriptions.** "X is good at A but bad at B" beats "X does A and B." Name the tensions. **Use tables** for tradeoff comparisons.
- **Cite inline.** Every factual claim from a source gets a linked citation. Use `[short label](url)` format.
- **Distinguish known from recent.** Separate established knowledge from recent developments or speculation.
- **No filler.** Every sentence should teach something. Cut throat-clearing, hedging, and broad surveys that don't inform decisions.
- **Obsidian-native.** Use callouts (`[!tip]`, `[!warning]`, `[!info]`), display math `$$`, comparison tables, and wikilinks where they improve scannability.

## Step 4: Save

Resolve the output location:

1. If the user specifies a path, use it.
2. If a `<linked_note>` or `<editor_selection>` provides context suggesting a location, use the parent directory of that note.
3. Default: the current working directory.

**One-pager:** write a single file `{topic-slug}.md`.

**Deep dive:** create a directory `{topic-slug}/` containing `index.md` and one file per subtopic.

Use lowercase kebab-case for all generated file and directory names.

After saving, report the file path(s) using wikilinks so the user can click to open.

## Step 5: Offer Next Steps

After delivering the artifact, briefly offer (do not execute without confirmation):

- "Want me to go deeper on any subtopic?" (upgrade one-pager section to its own page, or expand a deep-dive subtopic)
- "Want me to turn this into a teach course?" (hand off to `teach` skill with the research as grounding)
- "Want me to save specific sources for later?" (append to an existing resources note)

One line each. Do not over-prompt.
