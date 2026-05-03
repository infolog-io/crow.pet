# Demo Skill Architecture Trace

This simulated trace shows `crow-pet-skill-architect` choosing a composed skill architecture before a builder receives work.

It demonstrates the portable pattern:

```text
user ask
-> task record
-> skill architecture plan
-> SPEC.MD
-> stage handoff
-> capability binding
-> evaluation
-> handoff report
```

The key idea is that crow.pet decides the execution shape in markdown first. Runtime-specific features are mapped later through `adapters/patterns/execution-architecture.md` and `adapters/patterns/capability-broker.md`.

Referenced surfaces:

- `skills/crow-pet-orchestrator/SKILL.md`
- `skills/crow-pet-skill-architect/SKILL.md`
- `skills/crow-pet-spec-writer/SKILL.md`
- `templates/skill-architecture.md`
- `templates/stage-handoff.md`
- `templates/SPEC.md`
- `adapters/patterns/execution-architecture.md`
- `adapters/patterns/capability-broker.md`
- `skills/crow-pet-skill-architect/contract.md`
- `skills/crow-pet-skill-architect/rubric.md`
