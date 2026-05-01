# LLM Wiki - Personal Knowledge Base

A markdown-based knowledge base maintained by the active agent.

This is the crow.pet software package version.

Information Logistics working memory belongs in `../il-crow.pet`.

It uses the Karpathy Compilation Pattern.

It is portable markdown with strict YAML front matter.

Obsidian support lives behind adapters.

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `/raw/` | Immutable source files. Drop web clippings, PDFs, and images here. |
| `/wiki/` | Compiled knowledge base. The active agent owns these files. |
| `/wiki/indices/` | Auto-maintained master index, system log, and summaries. |
| `/outputs/` | Synthesized reports, QA reports, Marp slide decks, query answers. |
| `/assets/` | Local images referenced by wiki pages. |
| `/adapters/memory/` | Bounded recall rules for agents and native memory tools. |
| `/adapters/tools/obsidian.md` | Optional Obsidian vault adapter. |
| `/plans/` | Adoption and migration plans. |

## Operations

| Command | What it does |
|---------|--------------|
| **Ingest** | Reads new files in `/raw/`, creates wiki entries, updates the master index. |
| **Query** | Searches the wiki, synthesizes an answer, saves output, reinforces wiki pages. |
| **Lint** | Scans for broken links, missing YAML, contradictions. Generates a QA report. |

## How to Use

1. Add source material to `/raw/`.
2. Ask the active agent to "ingest" the new files.
3. Ask questions. The agent searches the wiki and writes answers to `/outputs/`.
4. Run "lint" periodically to catch gaps and contradictions.

## Memory Shape

Markdown is the map, not the warehouse.

Use indexes, source manifests, and context capsules.

Do not paste full user profiles, identity files, or transcripts into tasks.

## Obsidian

Use Obsidian through the adapter.

Do not make Obsidian syntax a core memory requirement.

## Schema

`CLAUDE.md` contains the full schema and behavioral rules governing all wiki operations.
