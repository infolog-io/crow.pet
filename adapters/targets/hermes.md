# Hermes Target Adapter

## Purpose

Export crow.pet skills into Hermes-native configuration.

## Runtime Target

Hermes Agent.

## Native Constructs

- Skills.
- Context files.
- `MEMORY.md`.
- `USER.md`.
- `SOUL.md`.
- Memory providers.
- Session search.

## Capabilities

- Use crow.pet skills as Hermes skills.
- Load project instructions through context files.
- Select bounded memory through Hermes memory tools.
- Use provider tools for long-term recall.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Memory adapter.
- Provider configuration.

## Outputs

- Hermes skill export notes.
- Context file mapping.
- Memory provider mapping.
- Context capsule policy.

## Permissions

- Keep `SOUL.md` global to the Hermes instance.
- Keep user profile excerpts private by default.
- Ask before exporting profile context externally.

## Invocation

Use Hermes skills for repeat workflows.

Use context files for project bearings.

Use memory adapters for recall before delegation.

## Export Mapping

Map `SKILL.md` folders to Hermes skills.

Map `AGENTS.md` to project context.

Map user profile needs to bounded `USER.md` excerpts.

Map identity needs to selected `SOUL.md` excerpts.

Map long-term recall to configured providers.

## Failure Modes

- Context file priority hides expected rules.
- Provider tools are unavailable.
- Memory snapshot is stale during the session.

## Logging

Record exported paths, provider, source skill, and capsule ID.

## Verification

Run one task that requires a selected user preference.

Confirm the full profile was not injected.

## Handoff Mapping

Map Hermes output into the common handoff report.
