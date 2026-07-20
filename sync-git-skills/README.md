# Sync Git Skills

Sync the local skills vault with two GitHub repositories using a two-branch strategy.

## Purpose

Maintain two synchronized repositories:
- **private-skills** — Contains all skills (public + private)
- **public-skills** — Contains only public skills (private content stripped)

## Strategy

Uses a two-branch approach:
- **main** branch → pushed to `origin` (private-skills)
- **public-only** branch → created from main, stripped of private content, pushed to `public` (public-skills)

## Modes

### Status
Check sync state across both remotes and uncommitted changes:
```
/sync-git-skills status
```

Shows:
- Uncommitted changes (if any)
- Behind/ahead count for origin (private-skills)
- Behind/ahead count for public (public-skills)
- Recommended actions

### Pull Private
Pull latest from origin (private-skills) into local main:
```
/sync-git-skills pull private
```

### Pull Public
Pull latest from public (public-skills) into local main:
```
/sync-git-skills pull public
```

### Pull (Both)
Pull from both remotes (private first, then public):
```
/sync-git-skills pull
```

### Push Private
Commit local changes and push to private-skills:
```
/sync-git-skills push private
```

Automatically commits uncommitted changes before pushing.

### Push Public
Sanitize PII, rebuild public-only branch, and push to public-skills:
```
/sync-git-skills push public
```

**IMPORTANT:** Always runs `/sanitize-pii` first to prevent personal information leaks.

Steps:
1. Run PII scan
2. Show findings (if any)
3. Ask user to approve sanitization
4. Apply sanitization
5. Commit sanitization to main
6. Rebuild public-only branch
7. Strip private content
8. Push to public
9. Verify no leaks

### Push (Both)
Push to both remotes (private first, then public):
```
/sync-git-skills push
```

### Full Sync (Default)
Complete sync workflow:
```
/sync-git-skills
```

Runs all operations in order:
1. Status check
2. Commit uncommitted changes
3. Pull from private
4. Pull from public
5. Push to private
6. Sanitize PII + push to public
7. Final report

## Private Directories

These directories are automatically excluded from public-skills:

- `private-journal/`
- `private-life-coach/`
- `journal/` (legacy)
- `personalized-life-coach/` (legacy)
- `.claude/`
- `.claudian/`
- Any directory matching `private-*/`

## Workflow

### Adding a New Public Skill

1. Create skill in local vault
2. Run `/sync-git-skills` to push to both repos

### Adding a New Private Skill

1. Name directory with `private-` prefix (e.g., `private-notes/`)
2. Run `/sync-git-skills` — automatically excluded from public

### Updating Skills

1. Make changes locally
2. Run `/sync-git-skills` to push everywhere

## Safety Features

- **Automatic PII Sanitization**: ALWAYS runs `/sanitize-pii` before pushing to public
  - Scans for names, emails, paths, credentials
  - Shows findings before applying changes
  - Requires user approval for sanitization
  - Commits sanitization to main before public push
  
- **Private Content Filtering**: Automatically strips private directories
  - `private-*/` pattern
  - `.claude/`, `.claudian/`
  - `journal/`, `personalized-life-coach/`
  - Sync tools and documentation
  
- **Post-Push Verification**: Checks public repo after push
  - Verifies no private content leaked
  - Lists any leaked files for review
  
- **Force Push Strategy**: Uses `--force` on public repo
  - Maintains clean public history
  - Public repo is always derived from private
  - No merge conflicts in public
  
- **Conflict Handling**: Manual resolution for pulls
  - Lists conflicted files
  - Asks user how to resolve
  - Never auto-resolves conflicts

## Remotes Setup

The skill expects these remotes:

```bash
git remote -v
# origin  https://github.com/xiaoxuerenww/private-skills.git
# public  https://github.com/xiaoxuerenww/public-skills.git
```

If not configured, the skill will guide you to add them.

## Example Sessions

### Full Sync

```
User: "sync skills"

1. Status check
   - Uncommitted: 3 files modified
   - origin/main: 0 behind, 0 ahead (synced)
   - public/main: 0 behind, 2 ahead (local ahead)

2. Commit local changes
   Commit message: [Update skills]
   ✓ Committed 3 files

3. Pull from private (origin)
   ✓ Already up to date

4. Pull from public
   ✓ Already up to date (local is ahead)

5. Push to private
   ✓ Pushed 3 commits to private-skills

6. Push to public
   
   Running PII scan...
   ⚠️  Found 2 PII instances:
   - write-article/SKILL.md: email address "user@oldexample.com"
   - frontier-lab-jobs/SKILL.md: path "/Users/olduser/"
   
   Sanitize automatically? (y/n): y
   
   ✓ Sanitized 2 files
   ✓ Committed sanitization to main
   ✓ Rebuilt public-only branch
   ✓ Removed private directories:
     - private-journal/
     - .claude/
     - sync-git-skills/
   ✓ Pushed to public-skills (force)
   ✓ Verified: no private content leaked

Summary:
| Step | Status | Details |
|------|--------|---------|
| Uncommitted | committed | 3 files |
| Pull private | up-to-date | - |
| Pull public | up-to-date | - |
| Push private | pushed | 4 commits |
| Sanitize PII | sanitized | 2 findings |
| Push public | pushed | public-only |
| Verification | ✓ clean | no leaks |
```

### Push Public Only

```
User: "push to public"

Running PII scan...
✓ No PII found

✓ Rebuilt public-only branch
✓ Removed private content
✓ Pushed to public-skills
✓ Verified: no private content leaked

Done.
```

### Status Only

```
User: "sync status"

Uncommitted changes: 2 files modified, 1 untracked

| Remote | Behind | Ahead | Status |
|--------|--------|-------|--------|
| origin (private) | 0 | 2 | local ahead |
| public | 1 | 2 | diverged |

Recommended action: commit changes, pull from public, then push both
```

## Error Handling

- **Missing remote**: Shows how to add it
- **Auth failure**: Suggests `gh auth status`
- **Merge conflicts**: Lists files, asks user to resolve
- **Private leak**: Auto-rebuilds and force-pushes to fix

## Notes

- Both repositories can be cloned independently
- Public repo is self-contained and usable standalone
- Private repo includes everything
- Changes flow: local → private → public (one direction)
- Public updates can be pulled back into private
