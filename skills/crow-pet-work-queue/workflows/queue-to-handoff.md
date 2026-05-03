# Queue To Handoff Workflow

Use this workflow when an approved spec should be handed to a builder through a markdown work item.

## Loop

```text
SPEC.MD -> Work Item -> Capability Binding -> Harness Handoff -> Verification -> Handoff Report
```

## Steps

1. Confirm `SPEC.MD` has enough acceptance criteria to verify a build.
2. Create a work item from `../../../templates/work-item.md`.
3. Set status to `queued`.
4. Bind semantic capability needs through the Capability Broker.
5. Apply policy gate when the build can change files, call tools, publish, spend, or touch sensitive context.
6. Select the builder skill or harness adapter.
7. Set status to `ready` when the builder handoff is complete.
8. Attach the handoff report and artifacts after the builder returns.
9. Set status to `built`, `failed`, or `needs-human` based on verification.
10. Set status to `accepted` only after the acceptance criteria pass.

## State Rule

The work item is the lifecycle record. The spec is the build contract. The handoff report is the result record.
