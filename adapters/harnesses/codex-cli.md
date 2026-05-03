# Codex CLI Harness Adapter

## Purpose

Delegate coding tasks to Codex CLI sessions.

## Runtime Target

Codex CLI.

## Capabilities

- Start a session.
- Pass repo path and task goal.
- Read final reports.
- Capture changed files.

## Inputs

- Task record.
- Repo path.
- Success criteria.
- Verification commands.
- Context capsule.

## Outputs

- Handoff report.
- Changed file list.
- Commands run.

## Permissions

- Ask before push, PR, or merge.
- Preserve unrelated user changes.

## Invocation

Launch Codex with a bounded subagent brief.

Attach only the selected context capsule.

## Failure Modes

- Session fails to start.
- Repo path is invalid.
- Verification command fails.

## Logging

Log session ID, repo path, branch, and commands.

Log context capsule ID when used.

## Verification

Run a targeted code task and confirm a structured handoff.

## Handoff Mapping

Map Codex final output into the common handoff report.

Map accepted memory notes into `memory_updates`.
