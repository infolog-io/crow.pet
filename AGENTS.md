# crow.pet Agent Guide

crow.pet is a runtime-neutral agent operating system.

This folder is the upstream software version.

Keep this upstream repo focused on reusable package source.

Use a separate instance for organization-specific context.

Use `skills/` as the source of truth.

Use `adapters/` for tool-specific translation.

Do not fork skills for a specific model or app.

The Memory Garden (`/wiki/`) is a Karpathian LLM Wiki for durable ideas, concepts, sources, and synthesized thinking.

## Core Layout

- `crow.pet-prd.md`: Product requirements.
- `skills/`: Canonical skills and workflows.
- `adapters/`: Runtime, tool, and target mappings.
- `adapters/memory/`: Bounded recall and context selection.
- `playbooks/`: Reusable public-safe strategies and mistakes with helpful/harmful counters.
- `templates/`: Shared cross-skill templates such as delta updates, specs, work items, skill architecture plans, and stage handoffs.
- `examples/`: Public-safe golden traces.
- `outputs/`: Generated task artifacts.
- `raw/`: Raw source inputs.
- `wiki/`: Memory Garden working knowledge.
- `plans/`: Adoption and migration plans.

## crow.pet Glossary

- Memory Garden (`/wiki/`): Karpathian LLM Wiki for durable ideas, concepts, sources, and synthesized thinking.
- Garden Map (`wiki/indices/master_index.md`): index of Memory Garden concepts.
- Garden Ledger (`wiki/indices/system_log.md`): audit trail for Memory Garden operations.
- Crow Voice (`crow-pet-crow-voice`): token-efficient harness communication.

Keep technical primitive names stable: skills, adapters, task records, context capsules, handoff reports, contracts, rubrics, and the policy gate.

## Progressive Disclosure

- Load root `SKILL.md` first.
- Load support files only when the selected skill says they are needed.
- Use `skills/skill-map.md` as a derived routing aid, not as source of truth.
- Use context capsules for task context; never bulk-load memory, wiki folders, transcripts, or raw sources.
- Do not add a vector database, embedding index, or hidden retrieval layer for v1 routing.
- Use the Capability Broker for semantic capability requests; bind them to adapters at runtime instead of hardcoding browser, MCP, CLI, API, local app, tool, harness, or model choices in skills.
- Use playbook deltas for learning; do not rewrite whole files unless explicitly approved.
- Use `templates/SPEC.md` when a user asks for something built and the acceptance criteria or builder handoff need to be made explicit.
- Use `templates/work-item.md` when an approved spec should become queued builder work.
- Use `crow-pet-skill-architect` and `templates/skill-architecture.md` before creating, changing, composing, or hardening skills and repeated workflows.
- Use `templates/stage-handoff.md` only for composed workflows where compact stage-to-stage evidence saves context or improves verification.

## Rules

- Preserve the Anthropic-style skill folder format.
- Keep one root `SKILL.md` per skill folder.
- Keep target exports disposable.
- Update canonical skills before target adapters.
- Keep runtime-specific execution features in adapters, not canonical skills.
- Ask before external writes.
- Ask before auth-sensitive browser actions, deploy changes, MCP writes, purchases, uploads, publishing, or destructive actions.
- Never expose secrets.
- Keep markdown files bounded and navigational.
- Use context capsules instead of dumping full memory files.
- Pull `USER.md` facts only when they change execution.
- Pull `SOUL.md` or `sole.md` excerpts only for tone and boundaries.
- Treat Obsidian as an adapter, not as core memory.
- Keep `.obsidian/` untracked.
