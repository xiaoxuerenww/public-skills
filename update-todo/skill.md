---
name: update-todo
description: "Add, complete, or list tasks in the user's todo file. Use when the user says 'add to my todo', 'mark X done', 'what's on my todo', or asks to track/remember a task."
---

# Update TODO

Manage tasks in the user's `todo.md` file.

## Step 1: Resolve todo file location

Search in this order:
1. `todo.md` in the **nearest parent directory** of the current working file/directory
2. `todo.md` in the **vault root**

If no `todo.md` exists anywhere, ask:

> No todo.md found. Create one in:
> 1. Current directory (`<path>`)
> 2. Vault root
> 3. Other location

Create the file at the chosen location with a `# TODO` header.

## Step 2: Determine action

| Trigger | Action |
|---------|--------|
| "add X to todo", "track X", "remember to X" | **Add** task |
| "mark X done", "complete X", "finished X" | **Complete** task |
| "what's on my todo", "show tasks", "list todo" | **List** tasks |
| "remove X", "delete X from todo" | **Remove** task |

## Step 3: Execute action

### Add task
1. **Find related note** — search the vault for a file related to the task:
   - Check if user mentioned a specific note (`@note` or `[[note]]`)
   - Otherwise, search for files matching key terms from the task (use `find` + `grep`)
   - If multiple matches, pick the most specific one (prefer exact title match > content match)
   - If no match, omit the link
2. **Format the task:**
   - With link: `- [ ] <task> — [[path/to/related-note.md]]`
   - Without link: `- [ ] <task>`
3. **Append** under the appropriate section (or create `## Tasks` if none exists)
4. If user specifies a category/project, add under that heading

### Complete task
- Find the matching `- [ ]` line, change to `- [x]`
- If multiple matches, ask which one

### List tasks
- Read the file, show pending tasks (`- [ ]`) grouped by section
- Mention count of completed tasks

### Remove task
- Find and delete the line
- Confirm before removing if ambiguous

## Step 4: Confirm

After any mutation, state what changed:
- "Added: `- [ ] <task>` to `<file>`"
- "Completed: `<task>`"
- "Removed: `<task>`"

Use wikilinks for the file path so user can click to open.
