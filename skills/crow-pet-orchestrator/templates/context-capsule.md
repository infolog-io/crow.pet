# Context Capsule

```yaml
id: C-0000
task_id: T-0000
created_at: ISO-8601
source_adapter: adapters/memory/contract.md
token_budget: 2000
sources:
  - kind: user | soul | memory | wiki | provider | raw
    path: path-or-provider-handle
    selector: heading-or-query
    sensitivity: public | internal | private | secret
included:
  user_profile: []
  identity_excerpt: []
  project_memory: []
  wiki_context: []
  provider_context: []
excluded:
  - source: path-or-provider-handle
    reason: not relevant | sensitive | stale | too large
redactions: []
expires_after: task | session | persistent
```
