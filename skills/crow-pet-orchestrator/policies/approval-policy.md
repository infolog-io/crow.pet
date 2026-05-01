# Approval Policy

## Levels

| Level | Name | Behavior |
| --- | --- | --- |
| 0 | Silent | Run and summarize later. |
| 1 | Notify | Run and notify before or after. |
| 2 | Ask | Request explicit approval. |
| 3 | Block | Refuse until policy changes. |

## Always Ask

- Push branches.
- Open pull requests.
- Send messages externally.
- Publish assets.
- Change environment variables.
- Spend money.

## Always Block

- Expose secrets.
- Delete production data.
- Remove safety gates.
- Merge without explicit approval.
