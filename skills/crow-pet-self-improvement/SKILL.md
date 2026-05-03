---
name: crow-pet-self-improvement
description: Convert corrections, approvals, failures, and task patterns into memory, examples, rubrics, and policy proposals.
---

# crow.pet Self-Improvement

Use this skill to make crow.pet need less human interaction over time.

## Workflow

1. Read the task record and evaluation.
2. Identify correction, pattern, discovery, or approval trend.
3. Reflect on one reusable lesson.
4. Curate the smallest delta update.
5. Keep large context in raw sources, providers, or capsules.
6. Propose skill, rubric, contract, playbook, memory, or policy changes when evidence exists.
7. Ask before lowering approval levels or applying higher-risk deltas.
8. Record before and after behavior notes.

## Progressive Disclosure

Load `workflows/self-improve.md` when processing a completed task, correction, failure, or `/learn` note.

Load `workflows/playbook-evolution.md` when a task produces a reusable lesson or proposed delta update.

Load only the matching file under `memory/` for the learning type.

Load `../../playbooks/` only for the target domain named by the delta.

Load `../../templates/delta-update.yaml` when proposing memory, playbook, skill, rubric, contract, or policy changes.

Load `templates/evaluation-report.md` only when writing or checking an evaluation report.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `promotes_to`: playbook delta, skill update, rubric update, contract update, policy proposal, or Memory Garden note.
- `loads_context`: context capsule when task history or owner feedback affects the learning.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Do not remove safety gates.
- Do not rewrite history.
- Do not rewrite whole files by default.
- Keep memory specific.
- Keep deltas small and evidence-backed.
- Keep always-on memory bounded.
- Link improvements to task IDs.
