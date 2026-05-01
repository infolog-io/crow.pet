# Cursor Target Adapter

## Purpose

Export crow.pet skills into Cursor-native customization.

## Runtime Target

Cursor editor and Cursor CLI.

## Native Constructs

- Agent Skills.
- `.cursor/rules/*.mdc`.
- User Rules.
- Memories.
- Custom Modes.
- Subagents.
- MCP servers.

## Capabilities

- Scoped coding rules.
- On-demand skills.
- Custom tool modes.
- Parallel subagents.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Adapter permissions.
- File globs.

## Outputs

- `.cursor/skills/` entries.
- `.cursor/rules/*.mdc` files.
- Custom mode notes.
- Subagent specs.

## Permissions

- Ask before destructive edits.
- Respect Cursor tool limits.

## Invocation

Use skills for procedures.

Use rules for always-on guidance.

Use modes for tool sets.

## Export Mapping

Map `SKILL.md` to `.cursor/skills/<name>/SKILL.md`.

Map project bearings to `.cursor/rules/*.mdc`.

Map roles to subagents or custom modes.

## Failure Modes

- Rule activation mismatch.
- Skill not discovered.
- Memory conflicts with rules.

## Logging

Record generated Cursor paths and source skill hashes.

## Verification

Open Cursor and trigger one exported skill.

## Handoff Mapping

Map Cursor agent output into the common handoff report.
