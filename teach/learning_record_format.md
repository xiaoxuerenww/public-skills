# Learning Record Format

Learning records live in the `## Learning records` section of `0_index.md`. Do not create a `learning_records/` directory or separate learning-record files.

They are the teaching equivalent of ADRs: they capture non-obvious lessons, key insights, and stated prior knowledge that will steer future sessions. They are used to calculate the zone of proximal development.

## Template

```md
- {YYYY-MM-DD}: {durable insight, corrected misconception, weak spot, or strong interview phrasing}. Next action: {specific review, drill, or task link}.
```

That is the whole format. A learning record should be a single bullet. The value is recording _that_ this is now known and _why_ it changes what to teach next - not in filling out sections.

## Optional sections

Only include extra evidence or implications in the same bullet when they add genuine value. Most records will not need them.

## Numbering

Do not number learning records. Use date-prefixed bullets inside `0_index.md`.

## When to write a learning record

Write one when any of these is true:

1. **The user demonstrated genuine understanding of something non-trivial** - not just exposure, but evidence they can use the concept correctly. This sets a new floor for what to teach next.
2. **The user disclosed prior knowledge** - "I already know X." Record it so future sessions don't re-teach it. Also record the _depth_ claimed.
3. **A misconception was corrected** - the user previously believed something wrong and now sees why. These are high-value: they predict future stumbling blocks for related topics.
4. **The mission shifted in response to learning** - the user discovered they cared about something different than they thought. Update `0_index.md`.

### What does _not_ qualify

- Material that was merely covered. Coverage is not learning. Wait for evidence.
- Anything already captured tersely in `2_deep_dive.md` as a term definition. Don't duplicate.
- Session-by-session activity logs. Learning records are not a journal - they are decision-grade insights.

## Supersession

When a later record contradicts an earlier one (the user's understanding deepened or corrected), add a dated correction bullet and leave the old bullet in place unless it would actively mislead future teaching.
