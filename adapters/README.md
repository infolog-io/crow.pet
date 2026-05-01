# crow.pet Adapters

Adapters isolate runtime-specific behavior from the stable `skills/` tree.

Use adapters for channels, harnesses, LLMs, tools, and orchestration patterns.

Use memory adapters for recall, profile, identity, and wiki selection.

Use the Obsidian adapter for vault-specific rendering and automation.

Use target adapters to export canonical skills into native tool formats.

Adapters translate into the common task record.

Adapters return the common handoff report.

Adapters must not create runtime-specific copies of skills.

## Folders

- `channels/`: user-facing entrypoints.
- `harnesses/`: agent runners and desktop automation surfaces.
- `llms/`: model and provider behavior.
- `memory/`: bounded recall and context selection.
- `patterns/`: orchestration strategies.
- `targets/`: native export mappings for each tool.
- `tools/`: external systems and local tools.

## Rule

Changing a model, harness, channel, tool, or pattern should change only `adapters/`.

Changing a memory backend should change only `adapters/memory/`.

Change `skills/` only when the product behavior itself changes.

Native target files are generated views.

Do not treat target exports as source of truth.
