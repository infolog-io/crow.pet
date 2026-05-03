# OpenClaude Memory Adapter

## Purpose

Map crow.pet recall into OpenClaude memory behavior.

## Runtime Target

OpenClaude agent directories.

## Native Memory Model

OpenClaude uses Hindsight as primary long-term memory.

It keeps a curated `MEMORY.md` cheat sheet always in context.

The curated file has a 50-line cap.

`USER.md`, `IDENTITY.md`, `SOUL.md`, and `TOOLS.md` live in workspace.

Daily logs and session manifests act as cold memory.

## Context Budget

Respect the 50-line `MEMORY.md` cap.

Prefer Hindsight recall for detailed history.

Use workspace files as selectors, not bulk prompt payloads.

Keep task capsules below 2,000 tokens unless approved.

## Selective Recall

Use Hindsight recall for project history and prior decisions.

Use `MEMORY.md` for critical current facts.

Use `USER.md` for execution preferences only.

Use `SOUL.md` for voice, values, and boundaries only.

Use `TOOLS.md` only when local environment details matter.

## Capabilities

- Query Hindsight recall.
- Reflect across retained memories.
- Read bounded workspace files.
- Enforce the working-memory cap.
- Emit context capsules for delegated tasks.

## Inputs

- Agent workspace path.
- Hindsight bank or MCP config.
- Task record.
- Target role.
- User request.
- Workspace file selectors.

## Outputs

- Context capsule.
- Hindsight recall handles.
- `MEMORY.md` update proposal.
- Daily log reference.

## Permissions

- Keep per-agent memory isolated.
- Ask before moving memory across agents.
- Do not copy full `USER.md` into external prompts.
- Do not mutate `SOUL.md` without notifying the owner.

## Invocation

Run before OpenClaude task delegation.

Use Hindsight first for long-term recall.

Use `MEMORY.md` only for current critical facts.

## Failure Modes

- Hindsight container is unavailable.
- `MEMORY.md` exceeds the line cap.
- Workspace identity files conflict.
- Nightly memory missed a recent session.

## Logging

Log agent name, Hindsight bank, selectors, and capsule ID.

Log rejected `MEMORY.md` writes above the cap.

## Verification

Check `MEMORY.md` line count.

Check Hindsight recall returns source handles.

Check selected profile facts are task-relevant.

## Handoff Mapping

Map capsule path into `context_capsules`.

Map accepted memory writes into `memory_updates`.

Map Hindsight handles into `artifacts`.
