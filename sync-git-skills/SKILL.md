---
name: sync-git-skills
description: "Sync skills vault between private and public repos. Use when the user says sync, push, pull, or update skills, or asks to check sync status."
---

# Sync Git Skills

Sync the local skills vault with two GitHub remotes using a two-branch strategy:

- **main** branch → pushed to `origin` (private-skills). Contains everything.
- **public-only** branch → pushed to `public` (public-skills). Private dirs stripped.

## Remotes

| Remote | Repo | Branch | Contains |
|--------|------|--------|----------|
| origin | private-skills (private) | main | everything |
| public | public-skills (public) | public-only → main | public content only |

## Modes

- **Status** — show sync state across both remotes and uncommitted changes.
- **Pull private** — pull latest from origin (private-skills) into local main.
- **Pull public** — pull latest from public (public-skills) into local main.
- **Pull** (no arg) — pull from both remotes in order: origin first, then public.
- **Push private** — commit and push main to origin.
- **Push public** — sanitize PII, rebuild public-only branch, push to public.
- **Push** (no arg) — push to both remotes in order: private first, then public.
- **Full sync** (default) — all operations: status → pull both → push both → report.

Detect from context. If the user just says "sync", run Full sync.

## Trigger Detection

Match user intent to the appropriate mode:

**Status checks:**
- "sync status"
- "check sync"
- "show sync state"
→ Run Status mode

**Pull operations:**
- "pull private"
- "pull from private"
→ Pull private only

- "pull public"
- "pull from public"
→ Pull public only

- "pull skills"
- "pull both"
- "sync pull"
→ Pull from both (private then public)

**Push operations:**
- "push private"
- "push to private"
→ Push private only (commit + push)

- "push public"
- "push to public"
- "publish skills"
→ Push public only (sanitize + rebuild + push)

- "push skills"
- "push both"
- "sync push"
→ Push to both (private then public)

**Full sync:**
- "sync"
- "sync skills"
- "sync everything"
- "full sync"
→ Complete sync workflow

When in doubt, clarify with user which operation they want.

## PRIVATE_DIRS

These paths must never appear in the public repo. Any directory prefixed with `private-` is private by convention.

**Convention:** Any directory matching `private-*/` is automatically excluded. This includes:

**Private skills (current):**
```
private-journal/
private-career-coach/
private-frontier-lab-jobs/
private-grilling/
private-grill-me/
private-humanizer/
private-handoff/
private-doc-grounded-qa/
private-writing-great-skills/
```

**Legacy private skills:**
```
journal/                    # Renamed to private-journal
personalized-life-coach/    # Renamed to private-career-coach
```

**Configuration and sync tools:**
```
.claude/
.claudian/
sync-git-skills/            # Sync tool itself (not needed in public)
sync-public.sh             # Legacy sync script
```

**Documentation (private-only context):**
```
SYNC_SKILL_MERGE_SUMMARY.md
FINAL_REPOSITORY_SPLIT.md
REPOSITORY_SPLIT_SUMMARY.md
PUBLIC_SKILLS_SETUP.md
SANITIZATION_SUMMARY.md
PUBLIC_SKILLS_SANITIZATION_REPORT.md
README.private.md              # Private README with sync instructions
PUBLIC_PRIVATE_TRACKING.md     # Tracking doc (in sync-git-skills/)
```

**README handling:** The main `README.md` contains only public skills. `README.private.md` contains the full private vault README with sync instructions and private skills list. When pushing to public, `README.md` is already sanitized and goes as-is.

**Tracking:** See `sync-git-skills/PUBLIC_PRIVATE_TRACKING.md` for the current list of public vs private skills. Update after each move.

Update this list when the user adds new private-only content.

## Status

Check sync state and uncommitted changes:

```bash
# Fetch latest from both remotes
git fetch origin
git fetch public

# Check uncommitted changes
git status --short

# Compare local with remotes
git rev-list --left-right --count origin/main...HEAD
git rev-list --left-right --count public/main...HEAD
```

Report:

| Remote | Local → Remote | Behind | Ahead | Status | Action Needed |
|--------|----------------|--------|-------|--------|---------------|
| origin (private) | main → origin/main | N | N | synced/ahead/behind | pull / push / both |
| public | main → public/main | N | N | synced/ahead/behind | pull / push / both |

**Uncommitted changes:** N files modified, M untracked

If there are uncommitted changes, ask user if they want to commit before syncing.

## Pull Private

Pull latest from origin (private-skills) into local main:

```bash
git fetch origin
git merge origin/main --no-edit -m "Sync: pull latest from private-skills"
```

If merge conflicts, list them and ask the user how to resolve.

## Pull Public

Pull public updates into local main:

```bash
git fetch public
git merge public/main --allow-unrelated-histories --no-edit -m "Sync: pull latest from public-skills"
```

If merge conflicts, list them and ask the user how to resolve.

## Pull (Both)

Pull from both remotes in order:

1. Pull from origin (private-skills) first
2. Pull from public (public-skills) second

This ensures private changes are integrated before public changes.

## Push Private

Commit local changes and push to origin (private-skills):

1. **Check for uncommitted changes**:
   ```bash
   git status --short
   ```

2. **If there are changes, ask user for commit message**. Default: "Update skills"

3. **Commit**:
   ```bash
   git add -A
   git commit -m "Update skills
   
   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
   ```

4. **Push**:
   ```bash
   git push origin main
   ```

## Push Public

Sanitize PII, rebuild public-only branch, strip private content, then push.

1. **Sanitize PII first** (REQUIRED):
   - Invoke `/sanitize-pii` skill in scan mode on the vault root
   - If PII found, show findings and ask user to approve automatic sanitization
   - If user approves, run `/sanitize-pii` in sanitize mode
   - Commit sanitization changes to main before proceeding
   - This prevents PII from ever reaching the public repo

2. **Start from main**:
   ```bash
   git checkout main
   git branch -D public-only 2>/dev/null
   git checkout -b public-only main
   ```

3. **Remove private directories** (from PRIVATE_DIRS list):
   ```bash
   git rm -r --ignore-unmatch private-journal/ private-life-coach/ journal/ personalized-life-coach/ .claude/ .claudian/ sync-public.sh
   ```

4. **Remove any `private-*` directories**:
   ```bash
   git ls-files 'private-*' | xargs -r git rm -r
   ```

5. **Remove sync and repository management files**:
   ```bash
   git rm -r --ignore-unmatch sync-git-skills/ SYNC_SKILL_MERGE_SUMMARY.md FINAL_REPOSITORY_SPLIT.md REPOSITORY_SPLIT_SUMMARY.md PUBLIC_SKILLS_SETUP.md SANITIZATION_SUMMARY.md PUBLIC_SKILLS_SANITIZATION_REPORT.md
   ```

6. **Replace README with public version**:
   ```bash
   git mv README.private.md README.private.md.bak
   # README.md is already the public version, just verify
   git add README.md
   ```

7. **Commit and push**:
   ```bash
   git commit -m "Sync: update public-skills
   
   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
   git push public public-only:main --force
   ```

8. **Switch back**:
   ```bash
   git checkout main
   ```

9. **Verify no private content leaked**:
   ```bash
   gh api repos/xiaoxuerenww/public-skills/git/trees/main --jq '.tree[] | select(.path | test("private|.claude|.claudian|sync-git-skills")) | .path'
   ```
   
   If output is empty, push is clean. Otherwise, list leaked files and ask user to review.

## Push (Both)

Push to both remotes in order:

1. **Push to private** (origin) first — includes all local changes
2. **Push to public** — sanitizes PII and strips private content

This ensures private repo has everything before public gets sanitized subset.

## Full Sync

Complete end-to-end sync workflow. Run in order:

1. **Status** — show current state (uncommitted changes, behind/ahead for both remotes).

2. **Commit local changes** (if any):
   - If uncommitted changes exist, ask user for commit message
   - Commit with message + co-author

3. **Pull private** — pull latest from origin (private-skills) into main.

4. **Pull public** — pull latest from public (public-skills) into main.

5. **Push private** — push main to origin (private-skills).

6. **Push public**:
   - Run `/sanitize-pii` scan
   - If PII found, ask user to approve sanitization
   - Apply sanitization if approved
   - Rebuild public-only branch
   - Strip private content
   - Push to public (public-skills)

7. **Report** — summary table:
   
   | Step | Status | Details |
   |------|--------|---------|
   | Uncommitted changes | committed / none | N files |
   | Pull private | merged / up-to-date / conflicts | N commits |
   | Pull public | merged / up-to-date / conflicts | N commits |
   | Push private | pushed / up-to-date | N commits |
   | Sanitize PII | clean / sanitized | N findings fixed |
   | Push public | pushed / up-to-date | public-only branch |
   | Verification | ✓ clean / ✗ leaked | private content check |

## Error Handling

- **No remote configured**: show `git remote -v`, tell user to add the missing remote.
- **Auth failure**: suggest `gh auth status`.
- **Merge conflict**: list conflicted files, do not auto-resolve, ask the user.
- **Diverged histories on first sync**: use `--allow-unrelated-histories`.
- **Private content in public repo**: immediately rebuild and force-push public-only.
