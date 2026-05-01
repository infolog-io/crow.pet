# OpenClaude Target Adapter

## Purpose

Export crow.pet skills into OpenClaude-native configuration.

## Runtime Target

OpenClaude agent directories.

## Native Constructs

- Claude Code config.
- Hindsight MCP memory.
- Workspace `MEMORY.md`.
- `USER.md`.
- `SOUL.md`.
- Hooks.
- Subagents.
- Skills.

## Capabilities

- Use crow.pet skills as OpenClaude skills.
- Use Hindsight for long-term recall.
- Use capped workspace files for hot context.
- Use hooks to enforce memory size.
- Use subagents for delegated work.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Memory adapter.
- Agent workspace path.
- Hindsight config.

## Outputs

- OpenClaude workspace mapping.
- Claude Code config notes.
- Hindsight memory mapping.
- Hook recommendations.

## Permissions

- Keep per-agent memories isolated.
- Ask before cross-agent memory migration.
- Do not mutate `SOUL.md` silently.
- Keep `MEMORY.md` capped.

## Invocation

Use an OpenClaude agent directory per durable agent.

Use Hindsight for recall before reading daily logs.

Use context capsules for delegated prompts.

## Export Mapping

Map `SKILL.md` folders into OpenClaude skills.

Map project rules into workspace `AGENTS.md`.

Map long-term memory to Hindsight retain and recall.

Map hot facts to capped `MEMORY.md` proposals.

Map user context to selected `USER.md` excerpts.

Map identity context to selected `SOUL.md` excerpts.

## Failure Modes

- Hindsight is unreachable.
- Hook blocks oversized memory writes.
- Agent workspace files conflict.
- Nightly memory processing is stale.

## Logging

Record agent name, workspace, source skill, and capsule ID.

## Verification

Run one task that requires Hindsight recall.

Confirm `MEMORY.md` remains within cap.

## Handoff Mapping

Map OpenClaude output into the common handoff report.
