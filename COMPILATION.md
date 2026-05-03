# Compilation Contract

crow.pet treats the LLM context window as a compiler for markdown operating artifacts.

## Source Language

The source language is portable markdown:

- root `SKILL.md` files
- adapter files
- task records
- context capsules
- handoff reports
- SPEC.MD build contracts
- markdown work items
- skill architecture plans
- stage handoffs
- contracts and rubrics
- policy files
- playbooks and delta updates
- Memory Garden notes

## Required Inputs

A compiled task needs:

- task record with `schema_version`, `id`, `status`, `risk_level`, `goal`, and `success_criteria`
- one selected root skill
- policy decision for any action with side effects
- adapter binding when runtime/tool/model/channel translation is required
- context capsule when memory affects execution
- `SPEC.MD` when a build request needs clarification before delegation
- work item when an approved spec is queued for builder handoff
- skill architecture plan when a task creates, changes, composes, or hardens a skill or repeated workflow

## Resolution Order

1. Task record defines the user goal and success criteria.
2. Orchestrator selects the smallest matching root skill.
3. Skill Architect chooses execution shape when the task creates, changes, composes, or hardens a skill or repeated workflow.
4. SPEC Writer clarifies ambiguous build requests and writes `SPEC.MD` when needed.
5. Work Queue turns approved specs into markdown work items when builder handoff is needed.
6. Selected skill controls progressive disclosure.
7. Policy gate classifies action risk.
8. Capability Broker binds semantic capabilities to adapters when needed.
9. Adapter translates into the active harness, tool, model, memory, or target runtime.
10. Contract, rubric, skill architecture plan, `SPEC.MD` acceptance criteria, work item evidence, and stage handoffs evaluate the result.

## Conflict Rules

- Policy wins over skill and adapter instructions.
- `Block > Ask > Notify > Silent`.
- Skills and adapters may raise risk; they may not lower it.
- More specific skill trigger language wins over generic trigger language.
- When two skills remain equally specific, use `skills/skill-map.md` order and record the assumption.

## Ambiguity Rules

Ask when ambiguity changes outcome, risk, external side effects, or private-context exposure.

Proceed with an explicit assumption when ambiguity affects only wording, ordering, or low-risk formatting.

## Missing Inputs

- Missing required task field: mark task `needs-human`.
- Missing selected skill: ask for task framing or route to orchestrator.
- Missing adapter: try Capability Broker fallback; if no safe binding exists, mark task `blocked`.
- Missing context capsule: continue only if memory is not task-relevant.
- Missing build acceptance criteria: route to SPEC Writer or mark task `needs-human`.
- Missing work item for queued builder work: create one from `templates/work-item.md`.
- Missing skill architecture plan for a new or composed skill: create one from `templates/skill-architecture.md` or mark evaluation `partial`.
- Missing contract or rubric: complete the draft, then mark evaluation `partial`.

## Contract Failure

If a result violates a contract, the task is not complete.

Retry once when policy allows and the fix is bounded. Otherwise return a handoff report with `Result: fail` or `Result: needs-human`.

## Relationship To Portable Skill Specs

crow.pet preserves the Anthropic-style skill folder shape and keeps target exports disposable. It is currently an independent markdown package, not a formal implementation of an external portable skill spec.
