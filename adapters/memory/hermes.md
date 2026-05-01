# Hermes Memory Adapter

## Purpose

Map crow.pet recall into Hermes Agent memory behavior.

## Runtime Target

Hermes Agent.

## Native Memory Model

Hermes uses bounded `MEMORY.md` and `USER.md` files.

They are injected as frozen startup context.

Hermes can add external memory providers alongside built-in memory.

Hermes can also search stored sessions on demand.

`SOUL.md` is loaded from `HERMES_HOME`, not the working directory.

## Context Budget

Respect the native `MEMORY.md` and `USER.md` character limits.

Treat those files as hot memory only.

Use external providers or session search for cold recall.

Use context capsules for task-specific warm recall.

## Selective Recall

Pull user profile facts from `USER.md` only when task-relevant.

Pull agent lessons from `MEMORY.md` only when operationally relevant.

Pull `SOUL.md` excerpts only for tone, boundaries, and identity.

Do not copy complete memory files into delegated prompts.

## Capabilities

- Read hot memory summaries.
- Use provider tools when configured.
- Use session search for older conversations.
- Mirror accepted crow.pet memory writes.
- Respect Hermes context-file priority.

## Inputs

- Hermes memory snapshot.
- Hermes provider status.
- Task record.
- Target role.
- User request.
- Optional `SOUL.md` section selectors.

## Outputs

- Context capsule.
- Hermes memory write proposal.
- Provider recall handles.
- Exclusion notes.

## Permissions

- Never export Hermes user profile text without approval.
- Never send secrets through provider writes.
- Scan recalled files before prompt injection.

## Invocation

Run after Telegram intake and before delegation.

Use Hermes provider tools for broad recall.

Use bounded files for stable preferences and conventions.

## Failure Modes

- Frozen startup memory misses live writes.
- Provider context is stale.
- `SOUL.md` is too broad for the task.
- Session recall returns noisy history.

## Logging

Log memory source, provider, selectors, and capsule ID.

Log live writes that need next-session visibility.

## Verification

Confirm capsule size.

Confirm each included entry has task relevance.

Confirm provider recall has source handles.

## Handoff Mapping

Map capsule path into `context_capsules`.

Map Hermes memory writes into `memory_updates`.

Map provider handles into `artifacts`.
