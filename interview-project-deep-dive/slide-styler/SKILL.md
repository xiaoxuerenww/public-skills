---
name: slide-styler
description: "Visual design system and layout rules for HTML slide decks. Use when building or styling 16:9 presentation slides (inline-styled HTML), choosing slide layouts, applying typography hierarchy, color-coding categories, or structuring content for interview deep-dive decks. Provides aesthetic direction, type rules, layout conventions, and reusable component patterns."
---

# Slide Styler

Visual design system for editorial, interview-ready 16:9 HTML slide decks. This skill captures taste and principles — not exact values — so it travels to any future deck.

## Purpose & audience

- **Context:** ML/AI technical deep-dive for interviews (a peer engineer with ML background).
- **Goal per slide:** demonstrate Staff/Senior-Staff signal — system-level thinking, technical depth, and leadership through influence (not authority).
- **Tone:** visual and confident, *not* wordy. Every slide reads at a glance; the talk track carries detail (in speaker notes).

## Aesthetic direction

- **Editorial, restrained, "good taste."** Think a design-conscious print/editorial feel, not a corporate template. Apple-like restraint: whitespace, hierarchy, and one confident accent doing the work.
- **Warm, light, paper-like base** with near-black ink and a **single hero accent** used sparingly for emphasis. Reserve **dark full-bleed panels** for key-insight / reframe moments and section dividers — they punctuate, so don't overuse.
- **One accent, one idea per slide.** Highlight the single key phrase in the headline and the single hero number; let everything else stay quiet.
- **Multi-category color-coding** (pillars, teams) uses a *coherent, evenly-weighted* hue family — same lightness/saturation, only hue varies — so categories feel like one system. The hero/most-important item keeps the primary accent. (Pick a perceptually-uniform set; keep it harmonious.)

## Type

- **Three roles, three treatments:** a strong display face for headings + big numbers (heavy weight, tight tracking); a clean humanist sans for body; a **mono for eyebrows, labels, metrics, and page counters** (uppercase, wide tracking).
- Headlines large with tight leading; **highlight the key phrase in the accent color.**
- Big stat numbers are heroes — oversize them.
- Don't go below a sensible floor; intentional micro-type is only for genuinely secondary label rows.

## Layout conventions (every content slide)

- **Eyebrow row** at top: mono section label (left) + `NN / TT` page counter in accent (right).
- **Headline** with one accent-colored span.
- Content area fills the height — see rules below.

## Hard-won layout rules

1. **No giant boxes with blank space.** Cards fit their content or distribute it. If tall, center the grouped content OR spread with space-between — never pin content to the top with a void beneath.
2. **Don't combine an auto-pushed footer with centered content** — it creates a gap. Pick one.
3. **Size boxes to content and center the group** rather than stretching rows to fill; cap width and center when a grid shouldn't span full-bleed.
4. **Prefer editorial/airy over boxy.** When a table feels heavy: hairline-separated rows, ghosted index numbers, generous gaps, a clean two-column "before -> after."
5. **Diagrams over text matrices.** A text-in-every-cell grid -> convert to a timeline/Gantt, spine, or flow. Let position and color carry meaning; milestone keywords <= 3 words.
6. **Color-code distinct categories**, each its own hue from one coherent family; keep the hero item in the primary accent.
7. **Section dividers are dark, full-bleed.**
8. **Smaller, denser-but-readable beats sparse.** If a slide feels empty, tighten and add substance; if it feels crammed, cut words and switch to a diagram — aim for the informative middle.

## How to structure content into layout

**Start from the ONE thing the slide must prove.** Write that as the headline (with the key phrase in accent). Everything else is evidence for it. If you can't name the one takeaway, the slide isn't ready.

**Pick the layout from the shape of the content, not habit:**

| Content shape | Layout pattern |
|---|---|
| One idea + proof | Big hero number/statement, supporting caption, generous whitespace |
| A process / sequence | Left-to-right flow or timeline with arrows; steps as equal nodes. Never a bullet list for a sequence |
| Cause -> effect / problem -> fix | Two-column "before -> after": muted/struck problem left, accent fix right, arrow between. Hairline rows, not boxes |
| A comparison across items | Aligned columns with a shared evaluation dimension in every column; highlight the chosen/winning one |
| Breadth / portfolio (N workstreams) | Color-coded grid or Gantt; each item same card shape; one hero item stands out |
| Relationships / org | Spine or hub-and-spoke diagram, not a table |
| Time | Real timeline/Gantt with an axis; bar span shows duration, dots show milestones |

**Compose the slide in horizontal bands, top to bottom:** eyebrow -> headline -> primary evidence band (fills height) -> optional summary/insight strip. Give the primary band `flex:1` and make it actually fill.

**Within a band, structure for scanning:**

- 3-6 items max per group; if more, group them under sub-labels (e.g. tier headers).
- Every item in a group shares one template (same fields, same order) — consistency is what makes it scannable.
- Put a mono label on each region so the eye knows what it's looking at before reading.
- Rank visually: hero (big/dark/accent) > supporting (card) > detail (muted caption). One hero per slide.
- Align to a grid; equal gaps; hairlines to separate instead of heavy borders.

**Density target:** the informative middle. If it feels empty -> tighten spacing, add a substantive line (a "why", a metric, a tradeoff), or enlarge the hero. If it feels crammed -> cut words to keywords and convert prose/tables into a diagram. Words are the first thing to cut, not the structure.

**Reduce, don't fill:** prefer a diagram with 3-word labels over a paragraph; prefer position/color to carry meaning over repeating text in every cell.

## Recurring components

- **Metric band:** big display numbers separated by hairlines, mono caption under each.
- **Chips/pills:** rounded, thin border or soft tint, mono/label text.
- **Tier tags:** small mono uppercase chips to rank importance (primary / guard / quality, etc.).
- **Key-insight / reframe block:** dark panel, accent kicker, medium-weight display quote.
- **Pipeline / funnel:** node cards joined by arrows; missing/gap states dashed + accent.
- **Radial org / hub-and-spoke:** dark center hub, category-colored nodes, spokes carrying short "how I lead" labels + arrowheads.
- **Timeline / Gantt:** quarter axis + one bar per track, short milestone keywords on dots; ring the pivotal milestone.

## Content principles

- Lead with thesis/impact; make the number the hero.
- Frame leadership as **influence through data, requirements, and launch gates** — call out "none reported to me."
- Show system-level reasoning: whole-stack gaps, staged de-risking, debiasing, guardrails.
- **Ground claims in source docs; never invent metrics.** Honest tradeoffs (e.g. a paused workstream) are a plus.
- **Bullet-style speaker notes** on every slide with delivery cues.
- Keep appendix deep-cuts after a dark "Appendix" divider — surfaced only on Q&A.

## Exemplar layouts (reuse these)

| Pattern | When to use |
|---|---|
| **Numbered workstream cards + dark key-insight strip** | "Here's my plan in N parts." 3 equal cards, each with NN + title + labeled sub-fields (Goal / Strategy) + footer "my leverage"; full-width dark insight bar underneath |
| **Gantt / timeline** | Sequencing and compounding over time. Quarter or phase axis, one bar per track, milestone dots with <= 3-word keywords, pivotal milestone ringed |
| **Lifecycle cards with progress/lifespan bars** | Staged states like "accepted -> retired." Equal cards with labeled fields + small bar visualizing duration/decay + status pill |
| **Radial hub-and-spoke** | Influence-without-authority and cross-team scope. Dark center hub = me/role, category-colored nodes, spokes with "how I lead/influence" labels + arrowheads |
| **Color-coded distinct nodes/pillars** | Portfolio/breadth at a glance. Each category its own coherent hue, hero item in primary accent |

## Deck mechanics

- Fixed 16:9 slides; inline styles; web fonts loaded once.
- Every slide carries a label, a screen-label index, and speaker notes.
- When adding/removing slides, renumber both the visible `NN / TT` counters and the screen-label indices in order.
