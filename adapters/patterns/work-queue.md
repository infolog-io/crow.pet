# Work Queue Pattern Adapter

## Purpose

Represent Symphony-like queued work as portable markdown work items.

Use this pattern when crow.pet needs to turn an approved `SPEC.MD` into builder-ready work without adopting a daemon, scheduler, GitHub Issue integration, or Linear integration as v0.1 core.

## Runtime Target

Repo-local markdown files interpreted by an LLM harness, orchestrator skill, or future queue adapter.

## Capabilities

- Track one builder-ready unit of work.
- Link a work item to a task record, `SPEC.MD`, policy decision, selected builder, selected adapters, artifacts, and handoff report.
- Preserve queue lifecycle state in markdown.
- Bind builder selection through Capability Broker.
- Map future issue trackers into the same work item shape.

## Inputs

- Task record.
- Approved `SPEC.MD`.
- Policy decision.
- Capability binding.
- Selected builder skill or harness adapter.
- Context capsule when memory affects execution.

## Outputs

- Markdown work item.
- Builder handoff packet.
- Updated work item status.
- Handoff report reference.
- Artifact references.

## Permissions

- Follow the policy gate before handing work to a builder that can write files, call tools, publish, spend, or touch sensitive context.
- Do not escalate permissions because work is queued.
- Do not treat queue assignment as approval.

## Invocation

Create one work item from `templates/work-item.md` for each approved spec that needs builder execution.

Use `status` to track lifecycle: `queued`, `needs-human`, `ready`, `assigned`, `building`, `blocked`, `built`, `failed`, or `accepted`.

Use Capability Broker before selecting a concrete builder when the spec declares semantic needs rather than a fixed harness.

## Failure Modes

- Spec lacks acceptance criteria.
- No safe builder can satisfy the capability needs.
- Policy blocks the requested build.
- Handoff report is missing or unverifiable.
- Work item status diverges from builder evidence.

## Logging

Log work item ID, task ID, spec ID, selected builder, selected adapters, policy decision, status changes, artifact paths, and handoff report path.

Do not log secrets or full context dumps.

## Verification

Confirm the work item links to an existing `SPEC.MD`.

Confirm selected adapters exist or are explicitly future bindings.

Confirm `built` and `accepted` states cite verification evidence.

Confirm no background runner, GitHub Issue integration, or Linear integration is required.

## Handoff Mapping

Map work item status, builder, adapters, artifacts, and verification evidence into the common handoff report.

Map reusable queue lessons to Self-Improvement proposals only after evaluation.
