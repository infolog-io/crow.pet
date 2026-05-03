# Task Record

```yaml
schema_version: "0.1"
id: T-0000
created_at: ISO-8601
requested_by: telegram-user-id
source_channel: telegram
status: queued # queued | running | blocked | needs-human | passed | failed
risk_level: 0 # 0 | 1 | 2 | 3
goal: string
success_criteria:
  - string
assigned_role: orchestrator
apps: []
adapters: []
context_capsules: []
repos: []
artifacts: []
approvals: []
verification: []
memory_updates: []
```

## Required Fields

- `schema_version`
- `id`
- `created_at`
- `requested_by`
- `source_channel`
- `status`
- `risk_level`
- `goal`
- `success_criteria`

## Optional Fields

- `assigned_role`
- `apps`
- `adapters`
- `context_capsules`
- `repos`
- `artifacts`
- `approvals`
- `verification`
- `memory_updates`

## Validation Checklist

- `goal` is specific enough to select a skill.
- `success_criteria` contains at least one observable outcome.
- `risk_level` matches the policy gate decision.
- `context_capsules` are included only when memory affects execution.
- `approvals` include explicit human approval for Level 2 actions.
- No secrets, private transcripts, or private local paths appear in public examples.
