# crow.pet Adapters

Adapters isolate runtime-specific behavior from the stable `skills/` tree.

Use adapters for channels, harnesses, LLMs, tools, and orchestration patterns.

Use the Capability Broker pattern when a skill needs a semantic ability before it knows which adapter should satisfy it.

Use `patterns/execution-architecture.md` when a skill architecture plan needs to map portable execution semantics to a target harness.

Use `patterns/work-queue.md` when mapping approved specs into markdown work items.

Use `../templates/SPEC.md` when creating or changing an adapter, tool, target, or harness mapping from an ambiguous build request.

Use memory adapters for recall, profile, identity, and wiki selection.

Use the Obsidian adapter for vault-specific rendering and automation.

Use target adapters to export canonical skills into native tool formats.

Use `SUPPORT.md` to distinguish primary adapter support from best-effort mappings.

Adapters translate into the common task record.

Adapters return the common handoff report.

Adapters must not create runtime-specific copies of skills.

## Folders

- `channels/`: user-facing entrypoints.
- `harnesses/`: agent runners and desktop automation surfaces.
- `llms/`: model and provider behavior.
- `memory/`: bounded recall and context selection.
- `patterns/`: orchestration strategies, including semantic capability binding.
- `targets/`: native export mappings for each tool.
- `tools/`: external systems, MCP gateways, browser surfaces, and local tools.

## Rule

Changing a model, harness, channel, tool, or pattern should change only `adapters/`.

Changing a memory backend should change only `adapters/memory/`.

Change `skills/` only when the product behavior itself changes.

Native target files are generated views.

Do not treat target exports as source of truth.

## Capability Binding

Skills may ask for semantic capabilities such as `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, or `external_write`.

`patterns/capability-broker.md` binds those requests to available adapters at runtime.

Prefer specific APIs, CLIs, connectors, and tool adapters before generic browser or desktop automation.

MCP and ACE-style local app surfaces are adapters behind the broker, not privileged core dependencies.

## Execution Architecture

Canonical skills may declare portable execution needs such as `inline`, `thin-references`, `deterministic-script`, `composed-pipeline`, `manual-side-effect`, isolation, dynamic context, side effects, and handoff strategy.

Adapters translate those needs into runtime-specific features. They must warn when a target cannot support the requested isolation, tool restriction, dynamic context, or handoff behavior.
