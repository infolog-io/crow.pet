---
schema_version: "0.1"
spec_id: SPEC-WQ-DEMO-0001
task_id: T-WQ-DEMO-0001
work_item_id: W-WQ-DEMO-0001
status: approved
spec_type: app
created_at: "2026-05-03T00:00:00-07:00"
---

# SPEC.MD

## User Ask

Build a tiny landing page section that explains the crow.pet SPEC.MD build loop.

## Clarifying Questions

| Question | Answer | Decision Impact |
| --- | --- | --- |
| Should this be executable app code or a docs snippet? | Docs snippet. | Selects a self-contained HTML artifact and avoids repo setup. |

## Goal

Create a compact HTML section that explains the ask-to-spec-to-handoff loop.

## Non-Goals

- No live runner.
- No daemon.
- No external tracker integration.

## Output Contract

- kind: HTML snippet
- target user: crow.pet repo visitor
- target surface: documentation or README-adjacent page
- done when: snippet names the loop and Version 0.1 limitation clearly

## Requirements

- Include the terms `SPEC.MD`, `Work Item`, `Capability Binding`, `Harness Handoff`, `Verification`, and `Handoff Report`.
- State that the queue is markdown/spec-layer behavior.

## Constraints

- No external assets.
- No scripts.
- Keep the snippet short.

## Capability Needs

| Need | Reason | Adapter Hint | Permission |
| --- | --- | --- | --- |
| code_generation | Produce HTML from the spec. | any harness; Codex-compatible example | Silent |

## Context Inputs

- `templates/SPEC.md`
- `templates/work-item.md`
- `README.md`

## Build Plan

1. Draft one semantic HTML section.
2. Verify that wording does not imply a live scheduler.

## Harness Handoff

- preferred builder: any harness
- selected skill: crow-pet-codex-delegate
- selected adapters: adapters/harnesses/codex-cli.md
- files or surfaces allowed: examples/demo-work-queue-trace/07-artifact.md
- approval needed: false

## Acceptance Criteria

- One HTML snippet is produced.
- It names the six-step loop.
- It says Version 0.1 is spec/prototype behavior.
- It does not mention a daemon, background scheduler, GitHub Issues, or Linear as implemented.

## Verification

- Read the snippet and compare it to the acceptance criteria.

## Policy Notes

- Local markdown artifact only.

## Open Questions

- None.
