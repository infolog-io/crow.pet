---
name: crow-pet-spec-writer
description: Ask clarifying questions, write a bounded SPEC.MD, and hand it to the right harness or agent for building.
---

# crow.pet SPEC Writer

Use this skill when the user wants something built but the build target, constraints, acceptance criteria, or builder surface need to be made explicit first.

## Workflow

1. Read the user ask and task record.
2. Decide whether a build spec is needed.
3. Ask the smallest set of clarifying questions needed to write `SPEC.MD`; prefer one to three questions.
4. If the answer is already clear, write assumptions instead of asking.
5. Draft `SPEC.MD` from `../../templates/SPEC.md`.
6. Link a skill architecture plan when the build creates, changes, composes, or hardens a skill or repeated workflow.
7. Declare semantic capability needs such as `code_generation`, `image_generation`, `repo_write`, `web_research`, `browser_control`, or `tool_execution`.
8. Route permission-sensitive actions through `crow-pet-policy-gate`.
9. Use the Capability Broker when the build needs a runtime, tool, model, or harness binding.
10. Delegate the approved spec to the selected builder skill or harness adapter.
11. Evaluate the built result against the spec acceptance criteria.
12. Return the spec path, build artifact, verification, and remaining risks in the handoff report.

## Progressive Disclosure

Load `../../templates/SPEC.md` only when drafting or checking a spec.

Load `../crow-pet-skill-architect/SKILL.md` when the spec concerns a new skill, adapter-backed workflow, composed workflow, deterministic script-backed skill, or side-effect workflow.

Load `../crow-pet-policy-gate/SKILL.md` when the spec includes external writes, repo writes, auth-sensitive workflows, publication, spending, destructive actions, or sensitive context.

Load `../../adapters/patterns/capability-broker.md` only when semantic capability needs must bind to a concrete adapter, tool, model, or harness.

Load `../crow-pet-codex-delegate/SKILL.md` when the spec should become code, an app, a tool, an adapter, or repository changes.

Load `../crow-pet-image/SKILL.md` when the spec should become an image or visual asset.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `delegates_to`: `crow-pet-skill-architect`, `crow-pet-codex-delegate`, `crow-pet-image`, or another selected builder skill.
- `uses_adapter`: `adapters/patterns/capability-broker.md`, `adapters/patterns/execution-architecture.md` when a skill architecture needs target mapping, plus selected harness, tool, model, or target adapters.
- `loads_context`: context capsule only when task-relevant memory or source material affects the spec.
- `evaluates_with`: `contract.md`, `rubric.md`, and the `SPEC.MD` acceptance criteria.

## Rules

- A spec is a build contract, not a brainstorm dump.
- Ask only questions that change the artifact, permission, builder, or acceptance criteria.
- Keep unknowns explicit as assumptions or open questions.
- Do not delegate a build until the spec has enough acceptance criteria to verify the result.
- Keep `SPEC.MD` portable across harnesses.
