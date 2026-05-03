# Invariants

crow.pet should stay thin, portable, and durable.

## Thin

- Root `SKILL.md` files should stay at or below 750 words.
- Adapter files should stay at or below 800 words.
- README should stay at or below 1,500 words.
- Default context capsules should stay at or below 2,000 tokens.
- Use progressive disclosure instead of bulk-loading support files.

## Portable

- Skills stay runtime-neutral.
- Runtime-specific behavior lives in `adapters/`.
- Target exports are generated views, not source of truth.
- Obsidian syntax is adapter-scoped.
- No vector database, embedding index, daemon, or hosted service is required for v0.1 routing.

## Durable

- The package remains readable as plain markdown.
- The Memory Garden uses source links, summaries, and indexes.
- Playbook updates are small deltas with evidence and rollback paths.
- Policy gates cannot be removed by self-improvement.
- Private context stays outside the public repo.
