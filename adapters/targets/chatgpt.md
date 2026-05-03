# ChatGPT Target Adapter

## Purpose

Export crow.pet skills into ChatGPT-native configuration.

## Runtime Target

ChatGPT web, desktop, Projects, and custom GPTs.

## Native Constructs

- Custom GPT instructions.
- Custom GPT knowledge files.
- GPT Actions.
- Projects.
- Project instructions.
- Custom Instructions.

## Capabilities

- Reusable guided workflows.
- Project-level context.
- Uploaded reference files.
- External API actions.

## Inputs

- Canonical skill folder.
- Shared `AGENTS.md`.
- Adapter permissions.
- Action schemas.

## Outputs

- Custom GPT configuration notes.
- Project instruction text.
- Knowledge file bundle.
- GPT Action spec.

## Permissions

- Ask before external API actions.
- Keep secrets outside uploaded files.
- Treat knowledge as reference, not behavior.

## Invocation

Use a custom GPT for repeated workflows.

Use a Project for long-running context.

Use Actions for external API calls.

## Export Mapping

Map `SKILL.md` rules into GPT instructions.

Map reference files into GPT knowledge.

Map tool adapters into GPT Actions.

Map memory into Project sources.

## Failure Modes

- Instructions exceed limits.
- Knowledge files are stale.
- Action auth fails.
- Project context drifts.

## Logging

Record GPT name, version, source skill, and action schema.

## Verification

Preview the GPT with one trigger prompt.

## Handoff Mapping

Map GPT output into the common handoff report.
