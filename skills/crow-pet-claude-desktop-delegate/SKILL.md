---
name: crow-pet-claude-desktop-delegate
description: Delegate bounded prompts to Claude Desktop through a safe desktop harness adapter.
---

# crow.pet Claude Desktop Delegate

Use this skill for Claude Desktop workflows.

## Workflow

1. Read the task record.
2. Prepare the prompt.
3. Confirm focus safety with `policies/focus-safety.md`.
4. Invoke a desktop harness adapter.
5. Capture response or failure state.
6. Return a handoff report.

## Rules

- Never type into an unverified window.
- Never paste secrets into Claude Desktop.
- Ask before sensitive content.
- Capture prompt metadata.
