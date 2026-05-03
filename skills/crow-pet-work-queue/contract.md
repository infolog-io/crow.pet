# Work Queue Contract

The Work Queue succeeds when it turns an approved `SPEC.MD` into one builder-ready markdown work item and tracks the outcome without requiring a live scheduler.

Required:

- preserve the linked spec as the build contract
- include task ID, spec ID, status, priority, policy decision, selected builder, selected skill, selected adapters, spec path, handoff report, and artifacts
- route builder selection through Capability Broker when the builder is not already fixed
- route permission-sensitive work through policy gate
- record verification evidence before marking work `built` or `accepted`
- keep GitHub Issues, Linear, and other trackers outside v0.1 core

Forbidden:

- execute a background runner
- treat a work item as a replacement for `SPEC.MD`
- mark accepted work without evidence
- hardcode one harness as the only builder
