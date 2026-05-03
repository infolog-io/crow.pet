# crow.pet Skills

This folder holds runtime-neutral crow.pet skills.

Each skill follows the Anthropic-style semantic folder rule:

- one lowercase hyphenated skill folder
- one root `SKILL.md`
- YAML frontmatter with `name` and `description`
- support folders named by purpose

## Progressive Disclosure

Load the root `SKILL.md` first.

Load workflows, templates, references, contracts, rubrics, examples, or policies only when the selected skill says the task needs them.

Use context capsules for task context. Do not load full memory files, wiki folders, transcripts, or raw sources by default.

Do not use a vector database, embedding index, or hidden retrieval layer for v1 skill routing. Use semantic markdown: names, descriptions, tags, declared edges, and bounded indexes.

Use playbooks for reusable lessons. Use `../templates/delta-update.yaml` for evidence-backed updates.

Use `../templates/SPEC.md` when a build request needs clarification before implementation. `crow-pet-spec-writer` should ask only high-leverage questions, write the spec, then delegate to the selected builder skill or harness.

Use `../templates/work-item.md` when an approved spec should become queued builder work. `crow-pet-work-queue` tracks lifecycle and handoff state; it does not run a daemon.

Use `crow-pet-skill-architect` and `../templates/skill-architecture.md` before creating, changing, composing, or hardening a skill or repeated workflow.

Use `../templates/stage-handoff.md` only when the selected execution mode is `composed-pipeline`.

## Skill Map

`skill-map.md` is a derived semantic routing map.

The source of truth remains each root `SKILL.md`.

Update the root skill first, then refresh `skill-map.md`.

The map helps a harness choose the smallest useful skill set before loading support files.

Adapters live in `../adapters`.

Use `../adapters/patterns/capability-broker.md` when a skill needs semantic abilities such as `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, or `external_write` before a concrete adapter is known.

Use `../adapters/patterns/execution-architecture.md` when a portable execution shape needs to map onto a specific harness, tool, or target runtime.

Do not fork skills for a specific runtime.

Do not let self-improvement rewrite whole skills, policies, rubrics, contracts, or playbooks without explicit approval.
