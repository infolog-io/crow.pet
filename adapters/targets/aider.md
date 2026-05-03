# Aider Target Adapter

## Purpose

Export crow.pet guidance into Aider-compatible context.

## Runtime Target

Aider terminal agent.

## Native Constructs

- Convention files.
- `/read` context files.
- `.aider.conf.yml`.
- Repo map.
- `AGENTS.md`.

## Capabilities

- Read-only convention context.
- Repository map awareness.
- Git-based editing.
- Configured context loading.

## Inputs

- Root `AGENTS.md`.
- Canonical skill summaries.
- Coding conventions.
- Verification commands.

## Outputs

- `CONVENTIONS.md`.
- `.aider.conf.yml` notes.
- Optional repo maps.

## Permissions

- Keep convention files concise.
- Use `/read` for read-only context.
- Ask before external writes.

## Invocation

Load conventions with `/read`.

Configure always-read files when stable.

## Export Mapping

Map `AGENTS.md` to always-read guidance.

Map skill summaries to convention docs.

Map repo context to repo maps.

## Failure Modes

- Context file not loaded.
- Repo map omits needed code.
- Conventions are too broad.

## Logging

Record loaded files and source skill summaries.

## Verification

Run Aider with exported conventions on one small task.

## Handoff Mapping

Map Aider output into the common handoff report.
