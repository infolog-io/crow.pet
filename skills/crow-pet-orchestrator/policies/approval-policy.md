# Approval Policy

Policy precedence: `Block > Ask > Notify > Silent`.

Skills and adapters may raise risk. They may not lower risk.

## Levels

| Level | Name | Behavior |
| --- | --- | --- |
| 0 | Silent | Run and summarize later. |
| 1 | Notify | Run and notify before or after. |
| 2 | Ask | Request explicit approval. |
| 3 | Block | Refuse until policy changes. |

## Decision Axes

Classify proposed actions by:

- scope: local read, local write, repo write, external read, external write
- reversibility: reversible, hard to reverse, destructive
- sensitivity: public, internal, private, secret
- auth surface: none, user session, scoped token, admin token
- blast radius: one file, repo, account, production
- cost: free, metered, purchase
- publication: private draft, shared, public

## Always Ask

- Push branches.
- Open pull requests.
- Send messages externally.
- Publish assets.
- Change environment variables.
- Spend money.
- Apply whole-file self-improvement rewrites.
- Send private context to remote tools.

## Always Block

- Expose secrets.
- Delete production data.
- Remove safety gates.
- Merge without explicit approval.
- Bypass the policy gate.
