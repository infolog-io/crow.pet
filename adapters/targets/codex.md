# Codex Target Adapter

## Purpose

Export crow.pet skills into Codex-native configuration.

## Runtime Target

Codex CLI, app, IDE extension, and web agent.

## Native Constructs

- Agent Skills.
- `AGENTS.md`.
- Rules.
- Hooks.
- Workflows.
- Subagents.

## Capabilities

- Native `SKILL.md` invocation.
- Repository guidance.
- Coding automation.
- Parallel agent work.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Adapter permissions.
- Verification commands.

## Outputs

- Codex-readable skill folders.
- Codex project instructions.
- Optional hooks and subagents.

## Permissions

- Ask before push, PR, or merge.
- Preserve unrelated user changes.

## Invocation

Use native Codex skills when available.

Use `AGENTS.md` for project bearings.

## Export Mapping

Map `skills/*/SKILL.md` directly.

Map `AGENTS.md` directly.

Map `workflows/` into Codex workflows or prompts.

Map specialist roles into subagents.

## Failure Modes

- Skill not discovered.
- `AGENTS.md` scope conflict.
- Hook blocks execution.

## Logging

Record Codex session, skill, repo, and task ID.

## Verification

Run one skill-triggering task.

## Handoff Mapping

Map Codex final output into the common handoff report.
