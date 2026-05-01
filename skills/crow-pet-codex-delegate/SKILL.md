---
name: crow-pet-codex-delegate
description: Delegate bounded coding tasks to Codex-compatible harnesses for implementation, tests, and structured handoffs.
---

# crow.pet Codex Delegate

Use this skill for coding work.

## Workflow

1. Read the task record.
2. Create a subagent brief from `templates/subagent-brief.md`.
3. Select the harness adapter.
4. Start the Codex-compatible session.
5. Collect changed files and verification evidence.
6. Return `templates/handoff-report.md`.

## Rules

- Touch only files required by the task.
- Preserve unrelated user changes.
- Ask before push, PR, or merge.
- Include commands run.
- Include remaining risks.
