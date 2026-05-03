# Devin Target Adapter

## Purpose

Export crow.pet skills into Devin configuration.

## Runtime Target

Devin web app and Devin for Terminal.

## Native Constructs

- Skills.
- Playbooks.
- Knowledge.
- `AGENTS.md`.
- Subagents.

## Capabilities

- Repo-scoped reusable procedures.
- Org-level playbooks.
- Contextual knowledge.
- Custom subagents.

## Inputs

- Canonical skill folder.
- Root `AGENTS.md`.
- Memory notes.
- Role definitions.

## Outputs

- `.agents/skills/<name>/SKILL.md`.
- Devin playbook drafts.
- Knowledge suggestions.
- Subagent specs.

## Permissions

- Use skills for repo procedures.
- Use playbooks for cross-repo prompts.
- Ask before external writes.

## Invocation

Use `@skills:name` for explicit skill use.

Use playbooks for broad session templates.

## Export Mapping

Map `SKILL.md` folders to Devin skills.

Map workflows to playbooks when cross-repo.

Map memory notes to Knowledge suggestions.

Map roles to subagents.

## Failure Modes

- Only one skill can be active.
- Knowledge is too vague.
- Playbook scope is too broad.

## Logging

Record generated Devin paths and playbook names.

## Verification

Start one Devin session with an exported skill.

## Handoff Mapping

Map Devin output into the common handoff report.
