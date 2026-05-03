# Demo Marketing Trace

This is a simulated public-safe golden trace for Version 0.1.

It shows the intended package loop without requiring a packaged runtime:

```text
user ask
-> task record
-> selected skill
-> context capsule
-> adapter binding
-> artifact
-> reflection / evaluation
-> proposed delta update
-> policy decision
-> handoff report
```

The trace uses `crow-pet-marketing` because it avoids external writes and can demonstrate playbook evolution safely.

## Package Surfaces Referenced

- `skills/crow-pet-marketing/SKILL.md`
- `skills/crow-pet-marketing/contract.md`
- `skills/crow-pet-marketing/rubric.md`
- `adapters/memory/markdown-bounded.md`
- `adapters/patterns/planner-generator-evaluator.md`
- `playbooks/marketing.md`
- `templates/delta-update.yaml`
