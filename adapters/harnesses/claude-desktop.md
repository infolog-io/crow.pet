# Claude Desktop Harness Adapter

## Purpose

Delegate bounded tasks to Claude Desktop.

## Runtime Target

Claude Desktop on macOS.

## Capabilities

- Focus a target window.
- Send a prompt.
- Capture response text.
- Detect unsafe focus.

## Inputs

- Task record.
- Prompt text.
- Target conversation context.
- Context capsule.

## Outputs

- Response text.
- Failure state.
- Handoff report.

## Permissions

- Never type secrets into unknown windows.
- Ask before sending sensitive content.

## Invocation

Use the approved macOS bridge path.

Use a memory adapter before sending task-specific context.

## Failure Modes

- Wrong window focus.
- Accessibility permission failure.
- Response capture failure.

## Logging

Log prompt hash, target app, window title, and task ID.

Log context capsule ID when used.

## Verification

Run a harmless prompt and confirm captured response text.

## Handoff Mapping

Map Claude Desktop output into the common handoff report.

Map accepted memory notes into `memory_updates`.
