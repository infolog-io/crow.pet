# Windsurf Target Adapter

## Purpose

Export crow.pet skills into Windsurf Cascade customization.

## Runtime Target

Windsurf Cascade.

## Native Constructs

- Rules.
- `AGENTS.md`.
- Workflows.
- Skills.
- Memories.

## Capabilities

- Always-on behavior rules.
- Manual workflows.
- On-demand skills.
- Auto-generated memories.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Workflow templates.
- Memory policy.

## Outputs

- `.windsurf/rules/*.md`.
- Workflow files.
- Skill folders.
- Memory guidance.

## Permissions

- Prefer rules or `AGENTS.md` for durable team knowledge.
- Treat auto memories as local hints.

## Invocation

Use rules for conventions.

Use workflows for manual tasks.

Use skills for complex procedures.

## Export Mapping

Map `AGENTS.md` to shared rules.

Map `workflows/` to Windsurf workflows.

Map `SKILL.md` folders to Windsurf skills.

Map memory policy to memory guidance.

## Failure Modes

- Rule activation mismatch.
- Memory retrieves stale context.
- Workflow requires manual invocation.

## Logging

Record generated Windsurf paths and source skills.

## Verification

Trigger one rule, workflow, and skill.

## Handoff Mapping

Map Cascade output into the common handoff report.
