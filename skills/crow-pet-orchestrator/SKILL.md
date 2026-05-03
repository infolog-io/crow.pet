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
5. Select the specialist skill and adapter.
6. Use the Capability Broker when the task asks for semantic abilities before a concrete adapter is known.
7. Attach a bounded context capsule when memory is needed.
8. Launch the subagent with `workflows/subagent-launch.md`.
9. Collect the handoff report.
10. Evaluate the result.
11. Record useful memory.
12. Send a concise status reply.

## Progressive Disclosure

Load `templates/task-record.md` when creating a task record.

Load `policies/risk-matrix.md` and `policies/approval-policy.md` before policy decisions.

Load `workflows/subagent-launch.md` only when delegation is needed.

Load `../../adapters/patterns/capability-broker.md` only when a skill or role brief declares semantic capabilities such as `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, or `external_write`.

Load `templates/context-capsule.md` only when memory affects execution.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `routes_to`: `crow-pet-codex-delegate`, `crow-pet-claude-desktop-delegate`, `crow-pet-cicd`, `crow-pet-marketing`, `crow-pet-image`, `crow-pet-self-improvement`, `crow-pet-crow-voice`.
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
