# Context Capsule

```yaml
schema_version: "0.1"
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

## Selection Rule

Capsules are skill-curated in v0.1.

The selected skill names the smallest files, headings, provider handles, or Memory Garden slices needed for the task. The harness may use filenames, headings, and declared selectors; it must not use a vector database, embedding index, or hidden retrieval layer for v0.1 routing.

## Required Fields

- `schema_version`
- `id`
- `task_id`
- `created_at`
- `source_adapter`
- `token_budget`
- `sources`
- `included`
- `excluded`
- `redactions`
- `expires_after`

## Validation Checklist

- Every source has `kind`, `path`, `selector`, and `sensitivity`.
- Secret sources are excluded unless a policy explicitly allows a local-only use.
- Private user or project facts include a task-specific reason.
- Excluded sources record why they were left out.
- Capsule stays within `token_budget`.
