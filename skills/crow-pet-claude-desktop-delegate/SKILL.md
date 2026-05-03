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

## Progressive Disclosure

Load `policies/focus-safety.md` only before desktop invocation.

Load `workflows/claude-desktop-delegate.md` only when preparing or running the bridge workflow.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `uses_adapter`: `adapters/harnesses/claude-desktop.md`.
- `loads_context`: context capsule only when target conversation context affects the prompt.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Never type into an unverified window.
- Never paste secrets into Claude Desktop.
- Ask before sensitive content.
- Capture prompt metadata.
