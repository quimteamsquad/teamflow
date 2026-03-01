#!/bin/bash
set -euo pipefail

# Find .workflow/state.md in current or parent dirs (up to 3 levels)
state=""
dir="$PWD"
for _ in 1 2 3 4; do
  if [ -f "$dir/.workflow/state.md" ]; then
    state="$dir/.workflow/state.md"
    break
  fi
  dir="$(dirname "$dir")"
done

if [ -n "$state" ]; then
  summary=$(head -15 "$state" | tr '\n' '\\' | sed 's/\\/\\n/g' | sed 's/"/\\"/g')
  printf '{"additionalContext":"TeamFlow state:\\n%s"}' "$summary"
else
  printf '{"additionalContext":"No TeamFlow project active. Use /spec to start or /quick for fixes."}'
fi
