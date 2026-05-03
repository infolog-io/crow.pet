---
schema_version: "0.1"
spec_id: SPEC-DEMO-SKILL-ARCH-001
task_id: T-DEMO-SKILL-ARCH-001
work_item_id:
architecture_id: ARCH-DEMO-001
status: draft
spec_type: tool
created_at: "2026-05-04T00:00:00-07:00"
---

# SPEC.MD

## Goal

Create a reusable markdown skill package for a research-to-outreach workflow.

## Non-Goals

- Do not send outreach.
- Do not add a live runner, database, or external tracker.
- Do not hardcode one harness.

## Output Contract

- kind: skill package plan
- target user: harness or agent using crow.pet
- target surface: `skills/crow-pet-research-to-outreach/`
- done when: architecture, stages, contract, and rubric are clear enough for a builder

## Capability Needs

| Need | Reason | Adapter Hint | Permission |
| --- | --- | --- | --- |
| `web_research` | gather public signals | Capability Broker chooses browser/API | Ask for authenticated sources |
| `text_generation` | synthesize and draft | selected harness | Silent |
| `evaluation` | score outputs | contract/rubric | Silent |

## Skill Architecture

- architecture needed: yes
- architecture path: `examples/demo-skill-architecture-trace/03-skill-architecture.md`
- execution mode: `composed-pipeline`
- handoff strategy: `stage-handoff-files`

## Acceptance Criteria

- The root skill loads without the full workflow context.
- Each stage names its required input and compact output.
- Runtime-specific features live in adapters.
- External writes remain policy-gated.

## Verification

Check against `skills/crow-pet-skill-architect/contract.md` and `skills/crow-pet-skill-architect/rubric.md`.
