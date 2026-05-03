# User Context Selection Adapter

## Purpose

Select only the user and identity context a task actually needs.

## Runtime Target

Any harness with user profile, identity, or persona files.

## Native Memory Model

User data may live in `USER.md`, profiles, project notes, or providers.

Identity may live in `SOUL.md`, `IDENTITY.md`, or runtime prompts.

`sole.md` is treated as a legacy alias for `SOUL.md`.

## Context Budget

User context should stay below 500 tokens per task.

Identity excerpts should stay below 300 tokens per task.

Prefer one-line preferences over narrative biographies.

## Selective Recall

Include profile facts only when they change execution.

Include communication preferences when the reply format matters.

Include `SOUL.md` excerpts for tone, boundaries, and defaults.

Exclude personal facts that do not affect the task.

Exclude private details from low-trust target apps.

## Capabilities

- Extract task-relevant profile facts.
- Extract task-relevant identity excerpts.
- Redact sensitive personal data.
- Explain why each item was included.
- Record why excluded items were skipped.

## Inputs

- Task record.
- User request.
- Role and target app.
- `USER.md` or profile provider output.
- `SOUL.md`, `sole.md`, or identity provider output.
- Approval and privacy policy.

## Outputs

- User context capsule section.
- Identity excerpt capsule section.
- Redaction notes.
- Exclusion reasons.

## Permissions

- Never infer sensitive traits for storage.
- Never include secrets, credentials, or tokens.
- Ask before sending user profile data to external tools.
- Ask before changing identity files.

## Invocation

Run inside the active memory adapter.

Run only after the task goal and role are known.

## Failure Modes

- Profile context feels like surveillance.
- Identity excerpt overrides task policy.
- Old preferences conflict with new instructions.
- `sole.md` and `SOUL.md` disagree.

## Logging

Log source file names, selectors, and redaction counts.

Do not log raw private profile text.

## Verification

Check every included user fact is actionable.

Check identity excerpts do not override policy.

Check capsule size before delegation.

## Handoff Mapping

Map selected context into the context capsule.

Map profile corrections into memory update proposals.
