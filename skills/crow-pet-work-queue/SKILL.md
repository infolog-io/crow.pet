---
name: crow-pet-work-queue
description: Turn approved SPEC.MD files into markdown work items for harness or agent builders, then track verification and handoff state.
---

# crow.pet Work Queue

Use this skill when an approved spec should become builder-ready queued work without introducing a runner, daemon, or external issue tracker.

## Workflow

1. Read the task record and approved `SPEC.MD`.
2. Create one markdown work item from `../../templates/work-item.md`.
3. Copy spec identity, optional architecture identity, goal, capability needs, acceptance criteria, and verification into the work item.
4. Route permission-sensitive or state-changing work through `crow-pet-policy-gate`.
5. Use the Capability Broker to bind requested capabilities to the safest available harness, tool, model, or adapter.
6. Select the builder skill or harness adapter.
7. Mark the work item `ready` when it can be handed to a builder.
8. Mark it `needs-human`, `blocked`, `built`, `failed`, or `accepted` as evidence arrives.
9. Record the handoff report path and artifacts.
10. Return a concise status update.

## Progressive Disclosure

Load `../../templates/work-item.md` only when creating or checking a queued work item.

Load `../../templates/SPEC.md` only when validating the linked build contract.

Load `../../templates/skill-architecture.md` only when the linked spec has an `architecture_id` or the builder needs execution architecture constraints.

Load `../../adapters/patterns/work-queue.md` only when explaining, exporting, or evaluating queue behavior.

Load `../../adapters/patterns/capability-broker.md` only when semantic capabilities need concrete builder or adapter bindings.

Load `../crow-pet-policy-gate/SKILL.md` when the work item includes external writes, repo writes, auth-sensitive workflows, publication, spending, destructive actions, or sensitive context.

Load the selected builder skill only after the work item is `ready`.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `delegates_to`: selected builder skill such as `crow-pet-codex-delegate`, `crow-pet-image`, or another harness-backed specialist.
- `uses_adapter`: `adapters/patterns/work-queue.md`, `adapters/patterns/capability-broker.md`, and selected harness, tool, model, or target adapters.
- `loads_context`: task record, approved `SPEC.MD`, optional skill architecture plan, work item, policy decision, and context capsule only when task memory affects execution.
- `evaluates_with`: `contract.md`, `rubric.md`, linked `SPEC.MD`, and handoff report.

## Rules

- The work queue is a markdown package surface, not a background scheduler.
- One work item tracks one builder-ready unit of work.
- `SPEC.MD` remains the build contract; the work item tracks lifecycle, assignment, evidence, and handoff.
- GitHub Issues, Linear, and other trackers are future adapters, not v0.1 core.
- Do not mark work `accepted` without verification evidence.
