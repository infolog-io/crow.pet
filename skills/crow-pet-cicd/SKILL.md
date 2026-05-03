---
name: crow-pet-cicd
description: Inspect CI/CD failures, route fixes, rerun tests, and summarize deployment status.
---

# crow.pet CI/CD

Use this skill for delivery loops.

## Workflow

1. Identify the repo, branch, PR, or deployment.
2. Read local or remote failures.
3. Summarize the failing check.
4. Delegate fixes when needed.
5. Rerun verification.
6. Ask before push, PR, merge, promote, or rollback.

## Progressive Disclosure

Load `workflows/fix-ci.md` when inspecting or fixing a failing check.

Load `examples/ci-task.md` only for examples, tests, or target export.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `delegates_to`: `crow-pet-codex-delegate` when code changes are needed.
- `uses_adapter`: `adapters/tools/github.md`, `adapters/tools/vercel.md`, or selected local harness/tool adapters when inspecting checks.
- `loads_context`: context capsule when repo, deployment, or prior failure memory affects diagnosis.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Read before changing.
- Link check URLs.
- Keep fix scope small.
- Require approval for external writes.
