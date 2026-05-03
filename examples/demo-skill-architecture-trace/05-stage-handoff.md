---
schema_version: "0.1"
handoff_id: H-STAGE-DEMO-001
task_id: T-DEMO-SKILL-ARCH-001
architecture_id: ARCH-DEMO-001
stage_id: gather-signals
status: pass
output_file: outputs/demo-skill-architecture/gather-signals-summary.md
output_schema: stage_signal_summary
summary_token_budget: 200
created_at: "2026-05-04T00:00:00-07:00"
---

# Stage Handoff

## Stage Goal

Distill selected source snippets into a compact evidence summary for downstream brief writing.

## Summary

The stage found three relevant signal categories: recent launch activity, hiring pattern, and positioning language. It returned source references and short notes only.

## Inputs Used

- approved source list
- rendered source snippets
- scoring notes from workflow reference

## Outputs

- compact signal summary
- source reference list
- unresolved evidence gaps

## Evidence

- output file path: `outputs/demo-skill-architecture/gather-signals-summary.md`
- no full raw scrape included

## Next Stage Inputs

- compact signal summary
- unresolved evidence gaps

## Risks

- Source freshness depends on selected adapter.

## Redactions

- None required in this simulated trace.
