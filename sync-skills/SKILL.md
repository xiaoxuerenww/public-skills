---
name: sync-skills
description: "Sync skills vault between private and public repos. Use when the user says sync, push, pull, or update skills, or asks to check sync status."
---

# Sync Skills

Sync the local skills vault with two GitHub remotes:

- **origin** → `private-skills` (private) — push everything
- **public** → `public-skills` (public) — pull public skill updates, push public-safe changes back

## Branches

- **Status** — show sync state across both remotes.
- **Pull** — pull latest from public into local.
- **Push private** — push all local changes to origin (private-skills).
- **Push public** — push public-safe changes to public remote.
- **Full sync** (default) — pull public, then push to both remotes.

Detect from context. If the user just says "sync", run Full sync.

## Status

Run these and report a table:

```bash
git fetch origin
git fetch public
```

Report:

| Remote | Branch | Local vs Remote | Action Needed |
|--------|--------|-----------------|---------------|
| origin (private) | main | ahead N / behind N / up to date | push / pull / none |
| public | main | ahead N / behind N / up to date | push / pull / none |

Also report uncommitted changes if any.

## Pull Public

```bash
git fetch public
git merge public/main --allow-unrelated-histories --no-edit -m "Sync: pull latest from public-skills"
```

If merge conflicts occur, list them and ask the user how to resolve.

## Push Private

```bash
git push origin main
```

## Push Public

Public repo must not receive private content. Before pushing:

1. Read the private directories list from the `PRIVATE_DIRS` section below.
2. Run `git diff public/main..HEAD --name-only` to see what would be pushed.
3. Check if any changed files are in private directories. If yes, warn the user and do NOT push.
4. If safe, push:

```bash
git push public main
```

If the histories diverged (rejected), pull public first, resolve, then retry.

## Full Sync

Run in order:

1. **Status** — show current state.
2. **Pull public** — merge latest public changes.
3. **Push private** — push everything to origin.
4. **Push public** — push public-safe changes (with private dir check).
5. **Report** — summary of what happened.

## PRIVATE_DIRS

These directories must never be pushed to the public remote. Check any file path against these prefixes:

```
private-journal/
private-life-coach/
.claude/
.claudian/
sync-public.sh
```

Update this list when the user adds new private-only skills. Any directory prefixed with `private-` is private by convention.

## Error Handling

- **No remote configured**: show `git remote -v` output, tell user to add the missing remote.
- **Auth failure**: suggest `gh auth status` to check GitHub auth.
- **Merge conflict**: list conflicted files, do not auto-resolve, ask the user.
- **Diverged histories on first sync**: use `--allow-unrelated-histories`.
