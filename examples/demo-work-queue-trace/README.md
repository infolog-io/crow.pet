# Demo Work Queue Trace

This is a simulated public-safe trace for the crow.pet Work Queue pattern.

It shows the intended spec-layer loop:

```text
user ask
-> task record
-> SPEC.MD
-> markdown work item
-> capability binding
-> harness handoff
-> simulated artifact
-> verification
-> handoff report
```

The trace uses Any Harness semantics with a Codex-compatible delegate as one possible builder binding.

## Package Surfaces Referenced

- `skills/crow-pet-spec-writer/SKILL.md`
- `skills/crow-pet-work-queue/SKILL.md`
- `skills/crow-pet-codex-delegate/SKILL.md`
- `templates/SPEC.md`
- `templates/work-item.md`
- `skills/crow-pet-orchestrator/templates/task-record.md`
- `skills/crow-pet-orchestrator/templates/handoff-report.md`
- `adapters/patterns/capability-broker.md`
- `adapters/patterns/work-queue.md`
- `adapters/harnesses/codex-cli.md`
