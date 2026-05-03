---
schema_version: "0.1"
architecture_id: ARCH-0000
task_id: T-0000
spec_id:
status: draft # draft | approved | superseded
skill_slug: crow-pet-example
execution_mode: inline # inline | thin-references | deterministic-script | composed-pipeline | manual-side-effect
isolation: none # none | single-isolated-context | per-stage-isolated-context | manual-only
side_effects: none # none | filesystem | network | external-service | publication
handoff_strategy: none # none | handoff-report | stage-handoff-files | generated-artifacts
dynamic_context: none # none | adapter-injected | script-rendered
cleanup_policy: none # none | delete-on-success | retain-on-failure | retain-days
context_budget: standard # tiny | standard | expanded
created_at: ISO-8601
---

# Skill Architecture

## Requested Skill Or Workflow

-

## Execution Decision

- mode:
- reason:
- not chosen:
- runtime assumptions:

## Structure

| Part | Path or Surface | Purpose |
| --- | --- | --- |
| Root skill |  |  |
| References |  |  |
| Scripts |  |  |
| Stage skills |  |  |
| Contracts |  |  |
| Rubrics |  |  |

## Stage Plan

| Stage | Isolation | Inputs | Output | Handoff |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Context Plan

- load first:
- load on demand:
- never bulk-load:
- dynamic context:
- max returned summary:

## Runtime Adapter Mapping

| Portable Need | Target Mapping | Warning |
| --- | --- | --- |
|  |  |  |

## Capability Needs

| Need | Reason | Adapter Hint |
| --- | --- | --- |
|  |  |  |

## Policy Notes

-

## Evaluation

- contract:
- rubric:
- context-efficiency checks:
- verification:

## Open Questions

-
