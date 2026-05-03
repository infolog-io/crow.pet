# Adapter Contract

Each adapter is one markdown file.

When an adapter is generated or substantially changed by a harness, draft a `SPEC.MD` first when the capability, permissions, inputs, outputs, or verification are ambiguous.

Each adapter must use these headings:

- Purpose
- Runtime Target
- Capabilities
- Inputs
- Outputs
- Permissions
- Invocation
- Failure Modes
- Logging
- Verification
- Handoff Mapping

Target adapters must also use these headings:

- Native Constructs
- Export Mapping

Memory adapters may add these headings:

- Native Memory Model
- Context Budget
- Selective Recall

Adapters must map external inputs into `skills/crow-pet-orchestrator/templates/task-record.md`.

Adapters must map execution results into `skills/crow-pet-orchestrator/templates/handoff-report.md`.

Memory adapters must map retrieved context into context capsules.

Use `skills/crow-pet-orchestrator/templates/context-capsule.md`.

Adapters must not alter task schema field names.

Adapters must not alter approval policy semantics.

Adapters must not require skill folder changes for runtime swaps.

Adapter `SPEC.MD` files are builder contracts. They do not replace this adapter contract or the runtime-facing adapter markdown.

Target adapters must describe how to export canonical `skills/`.

Target adapters must treat generated native files as disposable.

Memory adapters must not dump full user profiles into every task.

Memory adapters must prefer source links, summaries, and retrieval handles.
