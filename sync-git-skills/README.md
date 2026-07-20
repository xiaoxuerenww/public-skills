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
Check sync state across both remotes:
```
/sync-git-skills status
```

### Pull
Pull latest updates from public-skills into local main:
```
/sync-git-skills pull
```

### Push Private
Push main branch to private-skills:
```
/sync-git-skills push private
```

### Push Public
Rebuild public-only branch and push to public-skills:
```
/sync-git-skills push public
```

### Full Sync (Default)
Run all operations in order:
```
/sync-git-skills
```

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

- **PII Sanitization**: Prompts to run `/sanitize-pii` before pushing to public
- **Verification**: Checks public repo after push to ensure no private content leaked
- **Force Push**: Uses `--force` on public to maintain clean history
- **Conflict Handling**: Asks user to resolve merge conflicts manually

## Remotes Setup

The skill expects these remotes:

```bash
git remote -v
# origin  https://github.com/xiaoxuerenww/private-skills.git
# public  https://github.com/xiaoxuerenww/public-skills.git
```

If not configured, the skill will guide you to add them.

## Example Session

```
User: "sync skills"

1. Status check
   - origin/main: synced
   - public/main: 2 commits ahead

2. Pull from public
   ✓ Merged latest changes from public-skills

3. Push to private
   ✓ Pushed main to private-skills

4. Push to public
   ⚠️  Run /sanitize-pii first? (y/n)
   y
   [sanitization runs]
   ✓ Rebuilt public-only branch
   ✓ Removed private directories
   ✓ Pushed to public-skills
   ✓ Verified no private content in public repo

Summary:
- private-skills: updated (3 commits)
- public-skills: updated (2 commits)
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
