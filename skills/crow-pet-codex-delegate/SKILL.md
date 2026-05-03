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

## Progressive Disclosure

Load `templates/subagent-brief.md` only when preparing code delegation.

Load `workflows/codex-delegate.md` only when launching or monitoring a Codex-compatible session.

Load `examples/code-task.md` only for examples, tests, or target export.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `uses_adapter`: `adapters/harnesses/codex-cli.md` or another Codex-compatible harness adapter.
- `loads_context`: context capsule when repo or user memory affects implementation.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Touch only files required by the task.
- Preserve unrelated user changes.
- Ask before push, PR, or merge.
- Include commands run.
- Include remaining risks.
