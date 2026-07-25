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

Conduct comprehensive research using web search. If `/deep-research` skill is available, delegate to it; otherwise conduct research directly using WebSearch and WebFetch tools.

### Building the research query

Target these content types in order of priority:

1. **Text sources** covering:
   - What is this and why does it matter? (TL;DR)
   - What are the key concepts, players, and approaches? (Landscape)
   - How does it work mechanically? (How It Works)
   - What are the alternatives and how do they compare? (Comparisons)
   - What are the tradeoffs, failure modes, and limitations? (Tradeoffs)
   - What is the current state and recent developments? (Current State)
   - **Common pitfalls and mistakes**: Search for "[topic] pitfalls", "[topic] mistakes", "[topic] gotchas"
   - **Best practices**: Search for "[topic] best practices", "[topic] workflow", "[topic] checklist"

2. **Visual content** — diagrams, charts, infographics that explain the concept:
   - Search for: "[topic] diagram", "[topic] visualization", "[topic] infographic"
   - Prioritize sources: official docs (TensorFlow, PyTorch, scikit-learn), educational platforms (Google ML, Fast.ai, Coursera, DataCamp), research papers with clear figures
   - Download relevant images to `media/images/` using curl
   - Read images to verify quality and relevance
   - Name files descriptively: `{topic-concept}.png` (e.g., `roc-perfect-model.png`, `transformer-architecture.png`)

3. **Concrete examples and case studies**:
   - Search for: "[topic] example", "[topic] case study", "[topic] real-world", "when to use [topic]"
   - Look for scenarios showing when the concept succeeds vs fails
   - Find concrete numbers, datasets, or production deployments
   - **Critical**: Identify ONE recurring example to use as a thread throughout the document (e.g., "spam classifier", "fraud detection with 1% fraud rate"). This example should:
     - Be mentioned in sources (not invented)
     - Be specific enough to illustrate multiple concepts
     - Be realistic and relatable to the target audience

Example research sequence:
```
1. WebSearch: "ROC curve precision recall AUC evaluation metrics"
2. WebSearch: "ROC curve diagram visualization tutorial"
3. WebFetch: official docs URLs from search results
4. Download images: curl key diagrams to media/images/
5. WebSearch: "ROC AUC example when misleading imbalanced data"
6. Read downloaded images to verify content
```

### After research completes

Review and organize the research output:

- **Key findings** per section of the output template
- **Source URLs** with short annotations (what each covers, why trustworthy)
- **Visual assets** — which images were downloaded, what they show, where they'll be placed
- **Recurring example** — identify the ONE concrete scenario that will thread through the document
- **Conflicts or gaps** — areas where sources disagree or coverage is thin
- **Concrete examples** — real scenarios, datasets, production cases (beyond the main recurring one)
- **Progressive complexity path** — identify simple cases, general cases, and edge cases to present in order

Apply these source quality filters:

- Prefer primary sources (papers, official docs, author blogs) over summaries and aggregators
- Prefer sources with dates; flag undated claims about fast-moving fields
- When sources conflict, surface the conflict — don't silently pick a side
- Verify downloaded images are clear, relevant, and from reputable sources

### Checkpoint: write skeleton and wait for review

After research is complete, write a **skeleton draft** to the output file(s) before full synthesis. The skeleton uses the same file structure as the final output (one file for one-pager, directory with index + subtopic files for deep dive) but contains only:

1. **Section headings** — the full heading structure from the format template.
2. **Key terms and keywords** — important concepts, names, and jargon discovered during research, placed under the relevant heading as bullet points.
3. **Key points** — 1-3 bullet points per section summarizing the main findings. Short phrases or single sentences, not full prose.
4. **Visual embeds** — all downloaded images embedded using `![[media/images/filename.png]]` syntax with captions explaining what they show. Place images in relevant sections.
5. **Source links** — every source found during research, listed under the section(s) where it's relevant, in `[short label](url) — one-line annotation` format. Also collected in the Sources section at the bottom.
6. **Concrete examples** — real-world scenarios, datasets, or production cases that illustrate key concepts. Mark with "Example:" prefix.
7. **Open gaps** — mark any section where research was thin, sources conflicted, or concrete examples are missing with `<!-- GAP: description -->`.

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

**Structure & Flow (inspired by Google ML pedagogy)**:
- **Breadth first, then selective depth.** Cover the landscape before zooming in. The reader should understand what exists and how pieces relate before getting details on any one piece.
- **Progressive complexity.** Always follow this sequence: simple cases → general cases → edge cases. Binary scenarios before nuanced ones.
- **Explanation → Visualization → Application** pattern for each major concept. Don't explain without showing; don't show without applying.
- **Short paragraphs.** Rarely exceed 2-3 sentences before a visual, list, table, or section break.

**Examples & Concreteness**:
- **Recurring example thread.** Use the same real-world scenario across 3+ sections to build familiarity (e.g., spam classifier, fraud detection). Reference it by name consistently.
- **Concrete before abstract.** Lead with examples, systems, or use cases. Follow with principles and theory. Every abstract concept should have at least one concrete example.
- **Real scenarios over toy examples.** "Fraud detection with 0.1% fraud rate" beats "imbalanced dataset." Use actual numbers, datasets, systems.

**Visuals**:
- **Show, then explain.** Use embedded images to show concepts visually before explaining them in text. Target 60% visual content, 40% text.
- **Reference visuals in prose.** "As shown in Figure 1 above...", "The diagram illustrates..."
- **Visual for every major concept.** If explaining ROC curve, threshold selection, and failure modes, have visuals for all three.

**Clarity & Depth**:
- **Minimal math formalism.** Use display math `$$` only for key formulas. Always follow with intuitive explanation: *"In words: this measures how many..."*
- **Tradeoffs over descriptions.** "X is good at A but bad at B" beats "X does A and B." Name the tensions. **Use tables** for tradeoff comparisons.
- **Cite inline.** Every factual claim from a source gets a linked citation. Use `[short label](url)` format.
- **Distinguish known from recent.** Separate established knowledge from recent developments or speculation.
- **No filler.** Every sentence should teach something. Cut throat-clearing, hedging, and broad surveys that don't inform decisions.

**Obsidian-native formatting**:
- Use callouts (`[!tip]`, `[!warning]`, `[!info]`) sparingly for high-signal content
- Embed images with `![[path]]` and descriptive captions
- Use comparison tables, wikilinks, and display math where they improve scannability

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
