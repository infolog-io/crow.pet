---
name: crow-pet-policy-gate
description: Classify action risk and return Silent, Notify, Ask, or Block decisions before sensitive, external, or state-changing work.
---

# crow.pet Policy Gate

Use this skill when a task can read sensitive context, write files, call tools, publish, spend money, change external systems, or mutate crow.pet behavior.

## Workflow

1. Read the task record and proposed action.
2. Classify the action across decision axes.
3. Apply policy precedence: `Block > Ask > Notify > Silent`.
4. Return one decision with a short reason.
5. Include the exact approval request when the decision is `Ask`.
6. Stop when the decision is `Block`.

## Decision Axes

| Axis | Values |
| --- | --- |
| scope | local_read, local_write, repo_write, external_read, external_write |
| reversibility | reversible, hard_to_reverse, destructive |
| sensitivity | public, internal, private, secret |
| auth_surface | none, user_session, scoped_token, admin_token |
| blast_radius | one_file, repo, account, production |
| cost | free, metered, purchase |
| publication | private_draft, shared, public |

## Decisions

| Decision | Meaning |
| --- | --- |
| Silent | Run and summarize later. |
| Notify | Run and notify before or after. |
| Ask | Request explicit approval before proceeding. |
| Block | Refuse until policy changes or task is reframed. |

## Progressive Disclosure

Load `examples/policy-decisions.md` when examples are needed.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

Use `../crow-pet-orchestrator/policies/approval-policy.md` and `../crow-pet-orchestrator/policies/risk-matrix.md` as the default policy source.

## Dependency Edges

- `loads_context`: task record, proposed action, selected adapter, context sensitivity, and approval history.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Policies may raise risk but never lower it below the task or adapter risk.
- Skills and adapters cannot bypass the policy gate.
- External writes, publishing, purchases, secrets, production data, and safety-gate changes require `Ask` or `Block`.
- Whole-file self-improvement rewrites require `Ask`.
