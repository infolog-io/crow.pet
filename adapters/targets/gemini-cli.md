# Gemini CLI Target Adapter

## Purpose

Export crow.pet context into Gemini CLI configuration.

## Runtime Target

Gemini CLI.

## Native Constructs

- `GEMINI.md`.
- Configured context filenames.
- `/memory`.
- Custom commands.
- `save_memory`.

## Capabilities

- Hierarchical context files.
- Persistent memory.
- Reusable commands.
- Large context workflows.

## Inputs

- Root `AGENTS.md`.
- Canonical skill summaries.
- Memory policy.
- Command templates.

## Outputs

- `GEMINI.md`.
- `.gemini/settings.json` notes.
- Custom command files.

## Permissions

- Keep secrets out of memory.
- Prefer `AGENTS.md` as shared source.

## Invocation

Configure Gemini to load `AGENTS.md` when possible.

Use `GEMINI.md` for Gemini-specific hints.

## Export Mapping

Map `AGENTS.md` into configured context files.

Map workflows into custom commands.

Map durable facts into memory entries.

Map skills into brief context pointers.

## Failure Modes

- Context file not discovered.
- Memory is stale.
- Import path is broken.

## Logging

Record generated context files and settings paths.

## Verification

Run `/memory show` and confirm crow.pet context loads.

## Handoff Mapping

Map Gemini output into the common handoff report.
