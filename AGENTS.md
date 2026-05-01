# crow.pet Agent Guide

crow.pet is a runtime-neutral agent operating system.

This folder is the upstream software version.

Do not store Information Logistics private context here.

Use `/Users/informationlogistics/Developer/il-crow.pet` for that instance.

Use `skills/` as the source of truth.

Use `adapters/` for tool-specific translation.

Do not fork skills for a specific model or app.

## Core Layout

- `crow.pet-prd.md`: Product requirements.
- `skills/`: Canonical skills and workflows.
- `adapters/`: Runtime, tool, and target mappings.
- `adapters/memory/`: Bounded recall and context selection.
- `outputs/`: Generated task artifacts.
- `raw/`: Raw source inputs.
- `wiki/`: Working knowledge.
- `plans/`: Adoption and migration plans.

## Rules

- Preserve the Anthropic-style skill folder format.
- Keep one root `SKILL.md` per skill folder.
- Keep target exports disposable.
- Update canonical skills before target adapters.
- Ask before external writes.
- Never expose secrets.
- Keep markdown files bounded and navigational.
- Use context capsules instead of dumping full memory files.
- Pull `USER.md` facts only when they change execution.
- Pull `SOUL.md` or `sole.md` excerpts only for tone and boundaries.
- Treat Obsidian as an adapter, not as core memory.
