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
6. Attach a bounded context capsule when memory is needed.
7. Launch the subagent with `workflows/subagent-launch.md`.
8. Collect the handoff report.
9. Evaluate the result.
10. Record useful memory.
11. Send a concise status reply.

## Rules

- Keep skills runtime-neutral.
- Use adapters for runtime-specific behavior.
- Use memory adapters for selective recall.
- Ask before high-risk actions.
- Preserve audit trails.
- Stop when policy blocks progress.
