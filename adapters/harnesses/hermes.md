# Hermes Harness Adapter

## Purpose

Run crow.pet tasks through Hermes Agent when Hermes is the host.

## Runtime Target

Hermes Agent.

## Capabilities

- Load project context files.
- Use Hermes skills and tool gateway.
- Use Hermes built-in memory.
- Use configured external memory providers.
- Dispatch tasks from messaging surfaces.

## Inputs

- Task record.
- Skill name.
- Operator identity.
- Context capsule.
- Hermes profile or home path.

## Outputs

- Handoff report.
- Runtime logs.
- Memory write proposals.
- Provider recall handles.

## Permissions

- Follow crow.pet approval policy.
- Use Hermes permissions as runtime enforcement.
- Ask before external actions.

## Invocation

Map the common task record into a Hermes task prompt.

Use `adapters/memory/hermes.md` before delegation.

## Failure Modes

- Hermes context file priority hides expected rules.
- Memory provider is disabled.
- Frozen memory lacks same-session writes.
- Messaging surface drops an approval reply.

## Logging

Log Hermes session ID, profile, task ID, and capsule ID.

## Verification

Run one no-op task and confirm memory capsule loading.

## Handoff Mapping

Map Hermes output into the common handoff report.
