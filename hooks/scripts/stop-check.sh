#!/bin/bash
set -euo pipefail

reminders=""

# Check uncommitted .workflow/ changes
if git status --porcelain .workflow/ 2>/dev/null | grep -q .; then
  reminders="Uncommitted .workflow/ changes exist. Consider committing workflow state."
fi

# Check if state.md exists with active work
if [ -f ".workflow/state.md" ]; then
  phase=$(grep -i 'phase:' .workflow/state.md 2>/dev/null | head -1 | sed 's/.*: *//' || true)
  if [ -n "$phase" ]; then
    reminders="${reminders}${reminders:+\\n}Active phase: ${phase}. Remember to update state before leaving."
  fi
fi

if [ -n "$reminders" ]; then
  printf '{"additionalContext":"Reminders:\\n%s"}' "$reminders"
else
  printf '{}'
fi
