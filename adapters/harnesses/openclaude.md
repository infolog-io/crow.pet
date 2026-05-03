# OpenClaude Harness Adapter

## Purpose

Run crow.pet tasks through OpenClaude agent directories.

## Runtime Target

OpenClaude on Claude Code.

## Capabilities

- Start an agent workspace.
- Use Hindsight-backed recall.
- Use curated workspace files.
- Run configured skills and subagents.
- Log sessions for nightly memory processing.

## Inputs

- Task record.
- Agent workspace path.
- Target subagent.
- Context capsule.
- Hindsight bank or MCP config.

## Outputs

- Handoff report.
- Changed files or artifacts.
- Hindsight recall handles.
- Memory write proposals.

## Permissions

- Keep agent memories isolated.
- Ask before cross-agent memory migration.
- Follow crow.pet approval policy.
- Ask before external writes.

## Invocation

Map the common task record into an OpenClaude agent prompt.

Use `adapters/memory/openclaude.md` before delegation.

## Failure Modes

- Hindsight container is down.
- Agent workspace is missing.
- `MEMORY.md` cap blocks a write.
- Hook rejects a file change.

## Logging

Log agent name, workspace path, task ID, and capsule ID.

## Verification

Run one no-op task and confirm Hindsight recall works.

## Handoff Mapping

Map OpenClaude output into the common handoff report.
