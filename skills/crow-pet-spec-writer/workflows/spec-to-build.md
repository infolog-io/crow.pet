# SPEC To Build Workflow

Use this workflow when a user asks crow.pet to create an app, image, tool, adapter, research artifact, document, or other concrete output.

## Loop

```text
Ask -> SPEC.MD -> Harness Handoff -> Build -> Verify -> Handoff Report
```

## Steps

1. Restate the intended output in one sentence.
2. Identify missing decisions that would change the output.
3. Ask one to three clarifying questions when needed.
4. Draft `SPEC.MD` from `../../../templates/SPEC.md`.
5. Mark unresolved unknowns as assumptions or open questions.
6. Declare capability needs.
7. Bind capabilities to adapters through the Capability Broker.
8. Apply the policy gate before any state-changing build action.
9. Hand the spec to the selected builder skill or harness.
10. Verify the artifact against the spec acceptance criteria.
11. Produce the handoff report.

## Question Budget

Ask only questions that change one of these:

- artifact shape
- target user or surface
- constraints
- permissions
- acceptance criteria
- builder or adapter selection

If a question would only refine taste or wording, proceed with a clear assumption.
