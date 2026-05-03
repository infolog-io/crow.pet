---
name: crow-pet-orchestrator
description: Route crow.pet tasks into records, policy, adapters, subagents, evaluation, and memory.
---

# crow.pet Orchestrator

Use this skill as the main crow.pet control plane.

## Workflow

1. Read the incoming request.
2. Create a task record from `templates/task-record.md`.
3. Classify risk with `policies/risk-matrix.md`.
4. Apply approval rules from `policies/approval-policy.md`.
5. Route sensitive or state-changing actions through `crow-pet-policy-gate`.
6. Route ambiguous build requests through `crow-pet-spec-writer`.
7. Route approved spec-first builder work through `crow-pet-work-queue`.
8. Route new, changed, or composed skills and repeated workflows through `crow-pet-skill-architect`.
9. Select the specialist skill and adapter.
10. Use the Capability Broker when the task asks for semantic abilities before a concrete adapter is known.
11. Attach a bounded context capsule when memory is needed.
12. Launch the subagent with `workflows/subagent-launch.md`.
13. Collect the handoff report.
14. Evaluate the result.
15. Record useful memory.
16. Send a concise status reply.

## Progressive Disclosure

Load `templates/task-record.md` when creating a task record.

Load `policies/risk-matrix.md` and `policies/approval-policy.md` before policy decisions.

Load `../crow-pet-policy-gate/SKILL.md` when a task can read sensitive context, write files, call tools, publish, spend money, change external systems, or mutate crow.pet behavior.

Load `../crow-pet-spec-writer/SKILL.md` when the user wants something built and the output contract, constraints, acceptance criteria, or builder surface need to be made explicit.

Load `../crow-pet-work-queue/SKILL.md` when an approved `SPEC.MD` should become builder-ready queued work.

Load `../crow-pet-skill-architect/SKILL.md` when the task creates, changes, composes, or hardens a skill, adapter-backed workflow, repeated procedure, or multi-stage agent pattern.

Load `workflows/subagent-launch.md` only when delegation is needed.

Load `../../adapters/patterns/capability-broker.md` only when a skill or role brief declares semantic capabilities such as `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, or `external_write`.

Load `templates/context-capsule.md` only when memory affects execution.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `routes_to`: `crow-pet-spec-writer`, `crow-pet-work-queue`, `crow-pet-skill-architect`, `crow-pet-codex-delegate`, `crow-pet-claude-desktop-delegate`, `crow-pet-cicd`, `crow-pet-marketing`, `crow-pet-image`, `crow-pet-self-improvement`, `crow-pet-crow-voice`, `crow-pet-policy-gate`.
- `uses_adapter`: channel, memory, pattern, harness, and tool adapters selected by task, including `adapters/patterns/capability-broker.md` when semantic capability binding is needed.
- `loads_context`: context capsule only when task-relevant memory is needed.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Keep skills runtime-neutral.
- Use adapters for runtime-specific behavior.
- Use the Capability Broker for semantic capability requests before choosing browser, MCP, CLI, API, local app, tool, harness, or LLM capability surfaces.
- Use memory adapters for selective recall.
- Ask before high-risk actions.
- Preserve audit trails.
- Stop when policy blocks progress.
