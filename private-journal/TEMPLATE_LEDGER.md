# Ledger Entry Template

Use this format for each daily entry appended to `journal/journal.md`:

```markdown
## YYYY-MM-DD (Day of Week)

### Plan
- [ ] Task 1
- [ ] Task 2

### Log
- Completed X
- Blocked on Y

### Reflection
One-liner takeaway (only if user provides one)
```

Rules:
- Include `### Plan` if the user gives planned tasks; omit if they only logged.
- Include `### Log` if the user gives completed/blocked items; omit if they only planned.
- Check off plan items (`- [x]`) when the user reports them done in a later update.
- `### Reflection` is optional — include only when the user offers one.
