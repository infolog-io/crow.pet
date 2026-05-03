---
name: crow-pet-self-improvement
description: Convert corrections, approvals, failures, and task patterns into memory, examples, rubrics, and policy proposals.
---

# crow.pet Self-Improvement

Use this skill to make crow.pet need less human interaction over time.

## Workflow

1. Read the task record and evaluation.
2. Identify correction, pattern, discovery, or approval trend.
3. Write the smallest memory update.
4. Keep large context in raw sources, providers, or capsules.
5. Propose skill or policy changes when evidence exists.
6. Ask before lowering approval levels.
7. Record before and after behavior notes.

## Progressive Disclosure

Load `workflows/self-improve.md` when processing a completed task, correction, failure, or `/learn` note.

Load only the matching file under `memory/` for the learning type.

Load `templates/evaluation-report.md` only when writing or checking an evaluation report.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `promotes_to`: skill update, rubric update, contract update, policy proposal, or Memory Garden note.
- `loads_context`: context capsule when task history or owner feedback affects the learning.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Do not remove safety gates.
- Do not rewrite history.
- Keep memory specific.
- Keep always-on memory bounded.
- Link improvements to task IDs.
