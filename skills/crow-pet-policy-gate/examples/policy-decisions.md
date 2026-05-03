# Policy Decision Examples

## Silent

Action: read `README.md` and summarize the package.

Decision: Silent.

Reason: local read, public content, no side effect.

## Notify

Action: generate a local draft image asset.

Decision: Notify.

Reason: local artifact creation, reversible, no external publication.

## Ask

Action: open a pull request on GitHub.

Decision: Ask.

Reason: external write and public/repo-visible action.

Approval text: Approve opening a pull request with branch, title, files changed, and validation summary.

## Block

Action: paste a secret token into an unknown browser form.

Decision: Block.

Reason: secret exposure to untrusted external surface.
