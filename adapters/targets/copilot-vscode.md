# Copilot VS Code Target Adapter

## Purpose

Export crow.pet skills into GitHub Copilot and VS Code customizations.

## Runtime Target

GitHub Copilot in VS Code.

## Native Constructs

- `.github/copilot-instructions.md`.
- `.github/instructions/*.instructions.md`.
- Prompt files.
- Custom agents.
- Agent skills.
- Hooks.
- MCP servers.

## Capabilities

- Repository-wide guidance.
- Path-specific instructions.
- Repeatable prompts.
- Specialized agents.
- Tool connections.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Path scopes.
- Tool adapters.

## Outputs

- Copilot instruction files.
- Prompt files.
- Agent files.
- Skill folders.

## Permissions

- Ask before external writes.
- Keep secrets out of instructions.

## Invocation

Use instructions for standards.

Use prompt files for repeatable tasks.

Use skills for multi-step workflows.

## Export Mapping

Map `AGENTS.md` to repository instructions.

Map scoped rules to `*.instructions.md`.

Map workflows to prompt files.

Map specialist roles to custom agents.

Map skills to agent skills.

## Failure Modes

- Parent repo discovery disabled.
- Path rule does not match.
- Agent customization preview changes.

## Logging

Record generated `.github/` paths and source skills.

## Verification

Run one Copilot chat task with the generated files.

## Handoff Mapping

Map Copilot output into the common handoff report.
