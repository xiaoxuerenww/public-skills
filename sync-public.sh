#!/bin/bash
# Sync public skills from public-skills repo into this vault.
#
# Usage:
#   ./sync-public.sh          # pull latest public skills
#   ./sync-public.sh --diff   # preview what would change
#
# Setup:
#   origin  → private-skills (push all)
#   public  → public-skills  (pull public skills from here)

set -euo pipefail

cd "$(dirname "$0")"

# Fetch latest from public remote
git fetch public

if [[ "${1:-}" == "--diff" ]]; then
    echo "=== Changes in public/main vs last sync ==="
    git diff HEAD...public/main -- . ':!.claude' ':!.claudian' ':!private-*' 2>/dev/null || echo "No common base; will need --allow-unrelated-histories on first merge."
    exit 0
fi

# Merge public/main into current branch
# --allow-unrelated-histories needed on first merge only
# --no-edit to accept default merge message
echo "Merging public/main..."
git merge public/main --allow-unrelated-histories --no-edit \
    -m "Sync: pull latest from public-skills" || {
    echo ""
    echo "Merge conflict detected. Resolve conflicts, then:"
    echo "  git add . && git commit"
    exit 1
}

echo ""
echo "Public skills synced. Run 'git push origin main' to push to private-skills."
