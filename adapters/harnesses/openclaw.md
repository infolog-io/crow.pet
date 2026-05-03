# OpenClaw Harness Adapter

## Purpose

Run crow.pet skills through OpenClaw when OpenClaw is the host runtime.

## Runtime Target

OpenClaw local instance.

## Capabilities

- Load skills.
- Route channel messages.
- Execute local workflows.
- Persist task logs.

## Inputs

- Task record.
- Skill name.
- Operator identity.
- Context capsule.

## Outputs

- Handoff report.
- Runtime logs.
- Approval requests.

## Permissions

- Follow crow.pet approval policy.
- Use OpenClaw permissions only as a runtime wrapper.

## Invocation

Map the common task record into the OpenClaw skill invocation format.

Use the configured memory adapter before delegation.

## Failure Modes

- Skill not loaded.
- Channel adapter failure.
- Permission mismatch.

## Logging

Log OpenClaw task ID with the crow.pet task ID.

Log context capsule ID when used.

## Verification

Run one no-op task through OpenClaw and confirm the handoff report.

## Handoff Mapping

Map OpenClaw output into the common handoff report.

Map accepted memory notes into `memory_updates`.
