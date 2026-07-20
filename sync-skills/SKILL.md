---
name: sync-skills
description: "Sync skills vault between private and public repos. Use when the user says sync, push, pull, or update skills, or asks to check sync status."
---

# Sync Skills

Sync the local skills vault with two GitHub remotes using a two-branch strategy:

- **main** branch → pushed to `origin` (private-skills). Contains everything.
- **public-only** branch → pushed to `public` (public-skills). Private dirs stripped.

## Remotes

| Remote | Repo | Branch | Contains |
|--------|------|--------|----------|
| origin | private-skills (private) | main | everything |
| public | public-skills (public) | public-only → main | public content only |

## Branches

- **Status** — show sync state across both remotes.
- **Pull** — pull latest from public into local main.
- **Push private** — push main to origin.
- **Push public** — rebuild public-only branch and push to public.
- **Full sync** (default) — all of the above in order.

Detect from context. If the user just says "sync", run Full sync.

## PRIVATE_DIRS

These paths must never appear in the public repo. Any directory prefixed with `private-` is private by convention.

```
private-journal/
private-life-coach/
.claude/
.claudian/
sync-public.sh
```

Update this list when the user adds new private-only skills.

## Status

```bash
git fetch origin
git fetch public
```

Report:

| Remote | Local Branch | Remote Branch | Status | Action |
|--------|-------------|---------------|--------|--------|
| origin (private) | main | origin/main | ahead N / behind N / synced | push / pull / none |
| public | public-only | public/main | ahead N / behind N / synced | push / pull / none |

Also report uncommitted changes if any.

## Pull Public

Pull public updates into local main:

```bash
git fetch public
git merge public/main --allow-unrelated-histories --no-edit -m "Sync: pull latest from public-skills"
```

If merge conflicts, list them and ask the user how to resolve.

## Push Private

```bash
git push origin main
```

## Push Public

Rebuild the public-only branch from main, stripping private content:

1. Start from main:
   ```bash
   git checkout main
   git branch -D public-only 2>/dev/null
   git checkout -b public-only main
   ```

2. Remove every path listed in PRIVATE_DIRS:
   ```bash
   git rm -r --ignore-unmatch private-journal/ private-life-coach/ .claude/ .claudian/ sync-public.sh
   ```

3. Also remove any directory matching `private-*/`:
   ```bash
   git ls-files 'private-*' | xargs -r git rm -r
   ```

4. Commit and push:
   ```bash
   git commit -m "Sync: update public-skills"
   git push public public-only:main --force
   ```

5. Switch back:
   ```bash
   git checkout main
   ```

6. Verify no private content leaked:
   ```bash
   gh api repos/xiaoxuerenww/public-skills/git/trees/main --jq '.tree[] | select(.path | test("private|.claude|.claudian")) | .path'
   ```
   If output is empty, push is clean.

## Full Sync

Run in order:

1. **Status** — show current state.
2. **Pull public** — merge latest public changes into main.
3. **Push private** — push main to origin.
4. **Push public** — rebuild public-only, push to public.
5. **Report** — summary table of what happened.

## Error Handling

- **No remote configured**: show `git remote -v`, tell user to add the missing remote.
- **Auth failure**: suggest `gh auth status`.
- **Merge conflict**: list conflicted files, do not auto-resolve, ask the user.
- **Diverged histories on first sync**: use `--allow-unrelated-histories`.
- **Private content in public repo**: immediately rebuild and force-push public-only.
