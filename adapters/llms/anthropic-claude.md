# Anthropic Claude LLM Adapter

## Purpose

Describe Claude model behavior for crow.pet tasks.

## Runtime Target

Anthropic Claude models.

## Capabilities

- Long-form reasoning.
- Writing and editing.
- Tool-aware task planning.

## Inputs

- Task record.
- Skill instructions.
- Context files.

## Outputs

- Model response.
- Tool plan when available.
- Handoff summary.

## Permissions

- Follow task policy gates.
- Do not expose secrets in prompts or outputs.

## Invocation

Use the selected Claude runtime through a harness adapter.

## Failure Modes

- Model refusal.
- Context overflow.
- Tool mismatch.

## Logging

Log model name, task ID, and redacted prompt metadata.

## Verification

Run a known prompt and compare against the expected handoff shape.

## Handoff Mapping

Map model output into the common handoff report.
