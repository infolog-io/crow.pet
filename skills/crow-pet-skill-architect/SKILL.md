---
name: crow-pet-skill-architect
description: Choose the execution architecture for new or changing skills before implementation: inline, thin references, deterministic scripts, composed pipeline, or manual side-effect workflow.
---

# crow.pet Skill Architect

Use this skill when crow.pet is asked to create, adapt, compose, or harden a skill or repeated workflow.

## Workflow

1. Read the task record, user ask, and linked `SPEC.MD` when present.
2. Decide whether the request is a simple skill, large reference workflow, deterministic repeated operation, high-output multi-stage workflow, or side-effect workflow.
3. Draft a skill architecture plan from `../../templates/skill-architecture.md`.
4. Choose one execution mode: `inline`, `thin-references`, `deterministic-script`, `composed-pipeline`, or `manual-side-effect`.
5. Declare isolation, handoff strategy, dynamic context, context budget, cleanup policy, and capability needs.
6. For composed pipelines, define stages and compact handoffs from `../../templates/stage-handoff.md`.
7. Route semantic needs through Capability Broker.
8. Route side effects through Policy Gate.
9. Map portable execution semantics through `../../adapters/patterns/execution-architecture.md` when a harness-specific feature is needed.
10. Hand the approved architecture to `crow-pet-spec-writer`, `crow-pet-work-queue`, or the selected builder skill.
11. Evaluate the result for correctness, portability, and context efficiency.

## Progressive Disclosure

Load `../../templates/skill-architecture.md` only when drafting or checking an architecture plan.

Load `../../templates/stage-handoff.md` only when the chosen mode is `composed-pipeline`.

Load `../../adapters/patterns/execution-architecture.md` when mapping portable execution semantics to a target harness.

Load `../../adapters/patterns/capability-broker.md` only when semantic capabilities need concrete adapter bindings.

Load `../crow-pet-policy-gate/SKILL.md` when side effects, external services, publication, destructive actions, or sensitive context are involved.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `delegates_to`: `crow-pet-spec-writer`, `crow-pet-work-queue`, selected builder skill, or selected target adapter.
- `uses_adapter`: `adapters/patterns/execution-architecture.md`, `adapters/patterns/capability-broker.md`, and selected harness or target adapters.
- `loads_context`: task record, linked `SPEC.MD`, existing skill files, and context capsule only when task-relevant memory affects the architecture.
- `evaluates_with`: `contract.md`, `rubric.md`, `templates/skill-architecture.md`, and stage handoff evidence when used.

## Rules

- Do not make every skill a pipeline.
- Prefer the smallest execution architecture that satisfies the workflow.
- Keep canonical skills portable; map runtime-specific fields through adapters.
- Use scripts for deterministic repeated work when they reduce context and ambiguity.
- Use composed pipelines only for large, noisy, repeated, or multi-stage workflows.
- Use manual-side-effect mode for workflows that publish, spend, deploy, message externally, or mutate high-risk systems.
- Stage outputs should be compact references or summaries, not raw dumps.
- Avoid nested delegated-agent structures unless the user explicitly asks for them and the selected harness supports them.
- Dynamic context must be distilled before injection; never treat a whole file tree, transcript, or raw scrape as a stage input.
