# Cline Target Adapter

## Purpose

Export crow.pet skills into Cline customization.

## Runtime Target

Cline.

## Native Constructs

- Rules.
- Skills.
- Workflows.
- Hooks.
- `.clineignore`.

## Capabilities

- Always-on rules.
- On-demand skills.
- Slash-invoked workflows.
- Lifecycle hooks.

## Inputs

- Canonical skill folder.
- Workflow templates.
- Ignore policy.
- Hook policy.

## Outputs

- `.clinerules/` files.
- `.clinerules/skills/` folders.
- `.clinerules/workflows/` files.
- Hook notes.

## Permissions

- Keep rules small.
- Use skills for task procedures.
- Ask before external writes.

## Invocation

Use rules for project conventions.

Use skills for on-demand expertise.

Use workflows for repeatable slash tasks.

## Export Mapping

Map `SKILL.md` to Cline skills.

Map policies to `.clinerules/`.

Map workflows to Cline workflows.

Map hooks to Cline hooks.

## Failure Modes

- Skill trigger is unclear.
- Rule consumes too much context.
- Workflow is not manually invoked.

## Logging

Record generated Cline paths and source skills.

## Verification

Ask Cline to use one exported skill.

## Handoff Mapping

Map Cline output into the common handoff report.
