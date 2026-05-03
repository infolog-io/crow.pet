# Obsidian Skills Adoption Plan

## Purpose

Adopt useful Obsidian agent patterns without making Obsidian core.

Obsidian is a renderer, editor, and vault surface.

The Memory Garden (`/wiki/`) remains a Karpathian LLM Wiki: portable markdown and structured memory.

## Source

Use `kepano/obsidian-skills` as the reference package.

It includes skills for markdown, Bases, JSON Canvas, CLI, and Defuddle.

## Design Rule

Keep Obsidian behind adapters.

Core wiki files must remain useful without Obsidian installed.

Use Obsidian syntax only when the selected adapter requests it.

## Adapter Plan

Create `adapters/tools/obsidian.md`.

It owns app, vault, CLI, plugin, and render behavior.

Create `adapters/memory/obsidian-vault.md`.

It owns vault recall, graph links, and context capsules.

Create `adapters/targets/obsidian-skills.md`.

It maps crow.pet skills into Obsidian-compatible skill exports.

Create `adapters/patterns/public-export-obfuscation.md`.

It defines public-safe naming, bundling, and alias rules.

## Skill Mapping

Map `obsidian-markdown` to note formatting and wikilinks.

Map `obsidian-bases` to dashboards and operational views.

Map `json-canvas` to visual maps and agent workflow boards.

Map `obsidian-cli` to vault automation and validation.

Map `defuddle` to clean web ingestion before wiki compile.

## LLM Workflow

The LLM reads indexes before vault pages.

The LLM writes context capsules before delegation.

The LLM uses Obsidian syntax only for Obsidian output.

The LLM keeps raw sources out of hot memory.

The LLM validates generated `.base` and `.canvas` files.

## Obfuscation Plan

Use generic public names in crow.pet.

Use private aliases only in a separate local instance.

Minify or bundle generated helper scripts for exports.

Rename generated helper functions with neutral identifiers.

Strip comments that expose local paths or company details.

Never hide secrets through obfuscation.

Never treat obfuscation as access control.

## Adoption Phases

Phase 1 documents adapters and export rules.

Phase 2 imports selected reference skill ideas.

Phase 3 adds validation for `.md`, `.base`, and `.canvas`.

Phase 4 wires vault recall into context capsules.

Phase 5 adds public export and alias checks.

## Acceptance

Obsidian support can be removed without breaking core memory.

Generated Obsidian files render in Obsidian.

Context capsules cite vault source pages.

Public exports contain no private paths or company details.

Instance-specific names stay inside the separate local instance.
