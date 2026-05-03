# Work Queue Rubric

| Criterion | Points | Check |
| --- | ---: | --- |
| Spec linkage | 2 | Work item points to the correct `SPEC.MD` and preserves the build contract. |
| Lifecycle clarity | 2 | Status, priority, builder, handoff, artifacts, and evidence are explicit. |
| Builder neutrality | 2 | Builder can be any harness selected through Capability Broker. |
| Policy fit | 2 | Permission-sensitive work is gated before handoff. |
| Verification | 2 | Built or accepted status requires evidence. |

Pass: 8/10.

Fail when the queue implies a daemon, external tracker, or single mandatory harness.
