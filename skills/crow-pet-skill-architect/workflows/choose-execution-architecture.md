# Choose Execution Architecture Workflow

Use this workflow before creating or materially changing a skill.

## Decision Table

| Trigger | Choose |
| --- | --- |
| One short repeatable task | `inline` |
| Long instructions but one task | `thin-references` |
| Repeated deterministic operations | `deterministic-script` |
| Multi-stage workflow with noisy tools or high-output research | `composed-pipeline` |
| External side effects or high-risk mutation | `manual-side-effect` |

## Steps

1. Identify the repeated job and expected outputs.
2. Estimate workflow complexity, context volume, and side effects.
3. Choose the smallest execution mode that can be verified.
4. Define what loads in root `SKILL.md` and what loads on demand.
5. Define scripts only for deterministic or validation-heavy work.
6. Define stages and stage handoffs only for composed pipelines.
7. Define policy gates for side-effect workflows.
8. Record adapter mappings for runtime-specific features.
9. Define validation gates and stage handoff evidence before implementation.
10. Evaluate the architecture against the rubric before implementation.

## Runtime Mapping Rule

Canonical crow.pet architecture uses portable terms such as isolation, selected agent, allowed tools, dynamic context, and compact handoffs.

Target adapters translate those terms into runtime-specific features such as Claude Code forked context, Codex subagents, target-specific tool allowlists, shell injection, or preflight scripts.

Do not make runtime features canonical. If a target supports a stronger feature, record it as an adapter mapping and keep the root skill portable.

## Context Efficiency Check

Before accepting the architecture, confirm:

- the root `SKILL.md` can be loaded without support files
- support files have clear trigger conditions
- stage outputs are compact enough for downstream stages
- dynamic context is summarized, referenced, or script-rendered before injection
- heavier modes were rejected unless they add verification, safety, or token savings
