# Memory Adapter Contract

## Purpose

Define how crow.pet recalls context without bloating markdown.

## Runtime Target

All memory-capable harnesses and target exports.

## Native Memory Model

Each runtime can keep its native memory system.

crow.pet adds a shared selection layer above it.

The selection layer emits context capsules.

## Context Budget

Hot memory must stay below 1,500 tokens.

Task capsules should stay below 2,000 tokens.

Long sources must stay as links or retrieval handles.

Capsules may exceed the budget only after explicit task need.

## Selective Recall

Select context by goal, risk, role, and target app.

Prefer exact project facts over broad personal notes.

Include user preferences only when they affect execution.

Include identity excerpts only when they affect tone or boundaries.

## Capabilities

- Read native memory indexes.
- Query long-term memory providers.
- Select user profile facts.
- Select bounded `SOUL.md` excerpts.
- Attach context capsules to task records.
- Propose memory writes after completion.

## Inputs

- Task record.
- User request.
- Role and target app.
- `USER.md` or native profile store.
- `SOUL.md` or native identity file.
- Wiki index and source manifests.
- Native memory provider handles.

## Outputs

- Context capsule.
- Memory write proposal.
- Recall trace.
- Exclusion reasons.

## Permissions

- Never include secrets in capsules.
- Never include private personal facts without task need.
- Ask before exporting profile data to another service.
- Treat identity files as policy-bearing context.

## Invocation

Run before delegation.

Run again only when the task changes scope.

Use provider tools before reading large markdown files.

## Failure Modes

- Over-broad context selection.
- Stale memory from an old provider.
- Conflicting user preferences.
- Prompt injection inside a recalled source.
- Sensitive facts copied into a low-trust app.

## Logging

Log capsule ID, source paths, selectors, token estimate, and exclusions.

Do not log raw secrets or private profile text.

## Verification

Check capsule size before delegation.

Check every included fact has a source.

Check excluded sensitive sources have reasons.

## Handoff Mapping

Write capsule paths into `context_capsules`.

Write accepted memory proposals into `memory_updates`.

Write provider recall IDs into `artifacts` when needed.
