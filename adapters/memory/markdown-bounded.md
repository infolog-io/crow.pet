# Bounded Markdown Memory Adapter

## Purpose

Keep markdown memory readable, portable, and bounded.

## Runtime Target

Markdown-first memory, wiki, and context files.

## Native Memory Model

Markdown stores indexes, summaries, manifests, and small hot memories.

Raw transcripts, logs, assets, and source documents stay outside summaries.

## Context Budget

Single hot memory files should stay under 100 lines.

Curated always-on memory should stay under 1,500 tokens.

Wiki concept pages should prefer summary plus links.

Split pages when one topic needs separate decisions or history.

## Selective Recall

Read index files first.

Read concept pages second.

Read raw sources only when the wiki lacks detail.

Return a capsule, not a folder dump.

## Capabilities

- Maintain indexes.
- Maintain source manifests.
- Link raw sources to wiki summaries.
- Split pages by semantic scope.
- Detect pages that exceed budget.

## Inputs

- `wiki/indices/master_index.md`.
- `wiki/indices/system_log.md`.
- Relevant wiki pages.
- Raw source paths.
- Task record.

## Outputs

- Context capsule.
- Wiki maintenance proposal.
- Split or archive proposal.

## Permissions

- Do not rewrite raw sources.
- Do not erase contradictory history.
- Ask before deleting or archiving user-authored notes.

## Invocation

Use this adapter for local markdown recall.

Use it before provider fallback when the wiki index is enough.

## Failure Modes

- Page becomes a transcript.
- Index becomes a duplicate wiki.
- Summary loses source provenance.
- Cross-links point to missing pages.

## Logging

Log pages read, pages skipped, token estimate, and split proposals.

## Verification

Run a wiki lint pass after large ingestion.

Flag files without front matter or source links.

Flag pages above the line or token budget.

## Handoff Mapping

Attach the capsule to the task record.

Write split proposals as memory updates.
