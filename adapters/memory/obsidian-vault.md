# Obsidian Vault Memory Adapter

## Purpose

Select vault context without making Obsidian the memory core.

## Runtime Target

Obsidian vault folders and vault-derived indexes.

## Native Memory Model

Obsidian stores markdown notes, properties, links, embeds, Bases, and Canvas files.

crow.pet treats those files as a view over portable knowledge.

The vault is not the only source of truth.

## Context Budget

Read index notes first.

Keep vault context capsules below 2,000 tokens by default.

Prefer backlinks, summaries, and properties over full notes.

Use raw files only when the vault summary is insufficient.

## Selective Recall

Select notes by task goal, role, tags, properties, and backlinks.

Include Obsidian-only syntax only when the target is Obsidian.

Exclude private notes unless they affect the task.

Exclude plugin config unless the task concerns vault behavior.

## Capabilities

- Read vault indexes.
- Follow wikilinks and backlinks.
- Read front matter properties.
- Read Bases as operational views.
- Read Canvas files as visual maps.
- Emit task-specific context capsules.

## Inputs

- Task record.
- Vault path or alias.
- Query or note selector.
- Tag and property filters.
- Context budget.

## Outputs

- Context capsule.
- Source note list.
- Exclusion reasons.
- Vault maintenance proposal.

## Permissions

- Do not read excluded private folders.
- Do not expose raw note paths in public exports.
- Ask before importing private notes into another runtime.

## Invocation

Use after task planning.

Use before the Obsidian tool adapter edits files.

Use before delegating vault-dependent context to subagents.

## Failure Modes

- Link graph is stale.
- Note aliases collide.
- Front matter is invalid.
- Vault plugin output is not portable.
- Capsule includes too much personal context.

## Logging

Log vault alias, selectors, note count, and capsule ID.

Log excluded folders without note content.

## Verification

Check capsule size.

Check each included note has a reason.

Check private folders were excluded.

Check Obsidian-only syntax is target-appropriate.

## Handoff Mapping

Map capsule path into `context_capsules`.

Map selected notes into `artifacts`.

Map maintenance proposals into `memory_updates`.
