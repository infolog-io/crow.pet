---
schema_version: "0.1"
work_item_id: W-WQ-DEMO-0001
task_id: T-WQ-DEMO-0001
spec_id: SPEC-WQ-DEMO-0001
status: accepted
priority: normal
created_at: "2026-05-03T00:00:00-07:00"
updated_at: "2026-05-03T00:00:00-07:00"
policy_decision: Silent
selected_builder: any-harness
selected_skill: crow-pet-codex-delegate
selected_adapters:
  - adapters/patterns/capability-broker.md
  - adapters/harnesses/codex-cli.md
spec_path: examples/demo-work-queue-trace/03-spec.md
handoff_report: examples/demo-work-queue-trace/09-handoff-report.md
artifacts:
  - examples/demo-work-queue-trace/07-artifact.md
---

# Work Item

## Goal

Build one HTML snippet from the approved SPEC.MD.

## Spec Link

- `examples/demo-work-queue-trace/03-spec.md`

## Capability Needs

| Need | Reason | Selected Adapter | Permission |
| --- | --- | --- | --- |
| code_generation | Produce HTML from the spec. | adapters/harnesses/codex-cli.md | Silent |

## Builder Handoff

- builder: any harness, Codex-compatible example
- skill: crow-pet-codex-delegate
- adapters: adapters/patterns/capability-broker.md, adapters/harnesses/codex-cli.md
- allowed files or surfaces: examples/demo-work-queue-trace/07-artifact.md
- approval needed: false

## Verification

- `examples/demo-work-queue-trace/08-verification.md`

## Result

- accepted

## Open Questions

- None.
