# OpenAI Codex LLM Adapter

## Purpose

Describe OpenAI Codex model behavior for coding tasks.

## Runtime Target

OpenAI Codex models or Codex-backed harnesses.

## Capabilities

- Codebase inspection.
- Patch generation.
- Test-driven repair.

## Inputs

- Task record.
- Repo path.
- Verification criteria.

## Outputs

- Code changes.
- Verification result.
- Handoff report.

## Permissions

- Follow repo write scope.
- Ask before push, PR, or merge.

## Invocation

Use a Codex-compatible harness adapter.

## Failure Modes

- Test failure.
- Merge conflict.
- Missing dependency.

## Logging

Log model name, repo, task ID, and commands.

## Verification

Run the requested verification command.

## Handoff Mapping

Map Codex output into the common handoff report.
