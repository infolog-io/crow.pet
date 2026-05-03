# OpenCode Target Adapter

## Purpose

Export crow.pet skills into OpenCode customization.

## Runtime Target

OpenCode.

## Native Constructs

- Agent Skills.
- `AGENTS.md`.
- Custom agents.
- System prompt files.

## Capabilities

- Native skill discovery.
- Project rules.
- Specialized agents.
- Tool and model selection.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Role definitions.
- Permission rules.

## Outputs

- `.opencode/skills/` files.
- `.opencode/agents/` files.
- OpenCode rules.

## Permissions

- Keep global instructions brief.
- Use skills for procedures.
- Ask before external writes.

## Invocation

Use skills for reusable procedures.

Use `AGENTS.md` for project bearings.

Use agents for specialist roles.

## Export Mapping

Map `SKILL.md` folders to OpenCode skills.

Map `AGENTS.md` directly.

Map specialist roles to OpenCode agents.

## Failure Modes

- Skill discovery path mismatch.
- Agent prompt conflicts with rules.
- Model selection mismatch.

## Logging

Record generated OpenCode paths and source skills.

## Verification

Run one task that should invoke a skill.

## Handoff Mapping

Map OpenCode output into the common handoff report.
