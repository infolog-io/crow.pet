---
schema_version: "0.1"
architecture_id: ARCH-DEMO-001
task_id: T-DEMO-SKILL-ARCH-001
spec_id: SPEC-DEMO-SKILL-ARCH-001
status: draft
skill_slug: crow-pet-research-to-outreach
execution_mode: composed-pipeline
isolation: per-stage-isolated-context
side_effects: none
handoff_strategy: stage-handoff-files
dynamic_context: script-rendered
cleanup_policy: retain-on-failure
context_budget: standard
created_at: "2026-05-04T00:00:00-07:00"
---

# Skill Architecture

## Requested Skill Or Workflow

Reusable research-to-outreach workflow that turns company signals into a brief, scored angles, and a draft note.

## Execution Decision

- mode: `composed-pipeline`
- reason: noisy research, brief synthesis, scoring, and drafting benefit from isolated stages and compact handoffs
- not chosen: `inline` and `thin-references` would overfill hot context; `deterministic-script` alone cannot judge angle quality; `manual-side-effect` is unnecessary because sending is out of scope
- runtime assumptions: any capable harness can run the stages; target adapters map isolation and allowed tools

## Structure

| Part | Path or Surface | Purpose |
| --- | --- | --- |
| Root skill | `skills/crow-pet-research-to-outreach/SKILL.md` | Thin router for the workflow. |
| References | `skills/crow-pet-research-to-outreach/reference/` | Optional scoring guidance and examples. |
| Scripts | `skills/crow-pet-research-to-outreach/scripts/render-context.py` | Distill selected source snippets before model injection. |
| Stage skills | none in v0.1 | Stages are defined as workflow steps, not separate root skills yet. |
| Contracts | `contract.md` | Defines accepted brief, score, and draft outputs. |
| Rubrics | `rubric.md` | Scores evidence, relevance, tone, and bounded context. |

## Stage Plan

| Stage | Isolation | Inputs | Output | Handoff |
| --- | --- | --- | --- | --- |
| gather-signals | per-stage | approved source list | evidence summary | `templates/stage-handoff.md` |
| distill-brief | per-stage | evidence summary | company brief | `templates/stage-handoff.md` |
| score-angles | per-stage | company brief | ranked angle list | `templates/stage-handoff.md` |
| draft-note | per-stage | top angle and brief | outreach draft | handoff report |

## Context Plan

- load first: root `SKILL.md`
- load on demand: source list, reference examples, contract, rubric
- never bulk-load: full scrape, transcript, mailbox, CRM export, or wiki folder
- dynamic context: script-rendered summaries with source references
- max returned summary: 250 tokens per stage handoff

## Capability Needs

| Need | Reason | Adapter Hint |
| --- | --- | --- |
| `web_research` | Gather public company signals. | Browser or API adapter selected by Capability Broker. |
| `text_generation` | Draft brief and note. | Any selected harness. |
| `evaluation` | Score evidence and draft quality. | Contract and rubric. |

## Runtime Adapter Mapping

| Portable Need | Target Mapping | Warning |
| --- | --- | --- |
| per-stage isolation | Codex subagent, Claude forked context, or sequential harness sessions | If unsupported, use explicit stage handoff files in one session. |
| script-rendered dynamic context | local script, tool call, or manual summarized input | Do not inject raw source bundles. |
| stage-handoff-files | markdown files under `outputs/` or task-local artifacts | Handoff must include source references and redactions. |

## Policy Notes

- External sending is out of scope.
- Authenticated browsing would require Policy Gate classification.

## Evaluation

- contract: `skills/crow-pet-skill-architect/contract.md`
- rubric: `skills/crow-pet-skill-architect/rubric.md`
- context-efficiency checks: root skill stays thin; stages return compact summaries
- verification: simulated trace includes one stage handoff and a final evaluation

## Open Questions

- Which specific source types should the eventual workflow allow by default?
