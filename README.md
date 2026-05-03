# crow.pet

crow.pet is a context-compiled agent package.

An LLM harness points at this folder and uses its context window as the compiler. The source language is portable markdown: skills, adapters, templates, rubrics, policies, examples, and bounded memory. The compiled output is agent behavior: task records, delegated work, verification, artifacts, and durable learning.

This is the upstream software package version.

Information Logistics working memory belongs in `../il-crow.pet`.

It uses the Karpathy Compilation Pattern.

It is portable markdown with strict YAML front matter.

Obsidian support lives behind adapters.

The Memory Garden (`/wiki/`) is a Karpathian LLM Wiki for durable ideas, concepts, sources, and synthesized thinking.

## Package Shape

| Layer | Purpose |
|-------|---------|
| `skills/` | Canonical runtime-neutral behaviors. |
| `adapters/` | Runtime, tool, channel, memory, capability binding, and target translation. |
| `skills/*/templates/` | Common intermediate forms such as task records and handoffs. |
| `rubric.md` and `contract.md` | Evaluation and acceptance checks. |
| `wiki/` and `raw/` | Memory Garden inputs for context compilation. |

Current canonical skills cover orchestration, Codex delegation, Claude Desktop delegation, CI/CD, marketing, image generation, self-improvement, and Crow voice for token-efficient harness communication.

## crow.pet Glossary

| Name | Technical referent |
|------|---------------------|
| Memory Garden (`/wiki/`) | A Karpathian LLM Wiki for durable ideas, concepts, sources, and synthesized thinking. |
| Garden Map (`wiki/indices/master_index.md`) | Index of Memory Garden concepts. |
| Garden Ledger (`wiki/indices/system_log.md`) | Audit trail for Memory Garden operations. |
| Crow Voice (`crow-pet-crow-voice`) | Token-efficient harness communication. |

Core primitives keep their technical names: skills, adapters, task records, context capsules, handoff reports, contracts, rubrics, and the policy gate.

## Capability Binding

When a task needs an ability before it knows the concrete tool, use the Capability Broker (`adapters/patterns/capability-broker.md`).

Examples include `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, and `external_write`.

The broker binds those requests to available adapters such as MCP gateways, browser automation, CLIs, APIs, harness-native tools, local app surfaces, or LLM capability profiles.

Prefer specific APIs, CLIs, connectors, and tool adapters before generic browser or desktop automation.

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `/skills/` | Canonical skills and workflows. |
| `/adapters/` | Tool-specific translation, memory selection, and target exports. |
| `/raw/` | Immutable source files. Drop web clippings, PDFs, and images here. |
| `/wiki/` | Memory Garden: compiled knowledge base. The active agent owns these files. |
| `/wiki/indices/` | Garden Map, Garden Ledger, and summaries. |
| `/outputs/` | Synthesized reports, QA reports, Marp slide decks, query answers. |
| `/assets/` | Local images referenced by wiki pages. |
| `/adapters/memory/` | Bounded recall rules for agents and native memory tools. |
| `/adapters/tools/obsidian.md` | Optional Obsidian vault adapter. |
| `/plans/` | Adoption and migration plans. |

## Operations

| Command | What it does |
|---------|--------------|
| **Ingest** | Reads new files in `/raw/`, creates Memory Garden entries, updates the Garden Map. |
| **Query** | Searches the Memory Garden, synthesizes an answer, saves output, reinforces concept pages. |
| **Lint** | Scans for broken links, missing YAML, contradictions. Generates a QA report. |

## How to Use

1. Add source material to `/raw/`.
2. Ask the active agent to "ingest" the new files.
3. Ask questions. The agent searches the Memory Garden (`/wiki/`) and writes answers to `/outputs/`.
4. Run "lint" periodically to catch gaps and contradictions.

## Memory Shape

Markdown is the map, not the warehouse.

Use indexes, source manifests, and context capsules.

Do not paste full user profiles, identity files, or transcripts into tasks.

## Obsidian

Use Obsidian through the adapter.

Do not make Obsidian syntax a core memory requirement.

## Schema

`CLAUDE.md` contains the full schema and behavioral rules governing all Memory Garden (`/wiki/`) operations.
