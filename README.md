# crow.pet

![crow.pet architectural hero image](assets/crow-pet-hero.png)

**crow.pet is a context-compiled agent package.**

An LLM harness points at this folder and uses its context window as the compiler. The source language is portable markdown: skills, adapters, templates, rubrics, policies, examples, and bounded memory. The compiled output is agent behavior: task records, delegated work, verification, artifacts, and durable learning.

crow.pet is built to stay thin, portable, and durable across future LLM harnesses.

## What It Is

crow.pet is a runtime-neutral agent operating system for folders.

It is not a hosted service, a vector database, or a single-model prompt. It is a markdown package that lets a harness such as Codex, Claude Code, OpenClaude, Cline, or another agent runtime load only the skills and context it needs, then produce useful work through that context window.

The core pattern is simple:

1. A user asks for something.
2. The orchestrator turns the ask into a task record.
3. Skills provide behavior.
4. Adapters translate into the active harness, tool, model, memory, or target runtime.
5. The policy gate decides whether to check, ask, allow, or stop.
6. The result becomes artifacts, answers, apps, docs, images, plans, or durable learning.

## Core Primitives

| Primitive | Purpose |
| --- | --- |
| Skills | Runtime-neutral behaviors. |
| Adapters | Runtime, tool, channel, memory, model, target, and capability translation. |
| Task records | The common form for incoming work. |
| Context capsules | Bounded task context selected from memory or source files. |
| Handoff reports | The common form for completed delegated work. |
| Contracts | Acceptance boundaries for a skill or adapter. |
| Rubrics | Evaluation criteria for result quality. |
| Policy gate | Permission checkpoint for reads, writes, external actions, and sensitive context. |
| Capability Broker | Semantic ability binding before the concrete adapter is known. |
| Memory Garden | Durable knowledge layer at `/wiki/`. |

## Glossary

| Name | Technical referent |
| --- | --- |
| Memory Garden (`/wiki/`) | A Karpathian LLM Wiki for durable ideas, concepts, sources, and synthesized thinking. |
| Garden Map (`wiki/indices/master_index.md`) | Index of Memory Garden concepts. |
| Garden Ledger (`wiki/indices/system_log.md`) | Audit trail for Memory Garden operations. |
| Crow Voice (`crow-pet-crow-voice`) | Token-efficient harness communication. |

Technical primitive names stay stable: skills, adapters, task records, context capsules, handoff reports, contracts, rubrics, and the policy gate.

## Package Shape

| Layer | Purpose |
| --- | --- |
| `skills/` | Canonical runtime-neutral behaviors and workflows. |
| `adapters/` | Runtime, tool, channel, memory, capability binding, and target translation. |
| `skills/*/templates/` | Common intermediate forms such as task records and handoffs. |
| `contract.md` and `rubric.md` | Acceptance checks and evaluation criteria. |
| `wiki/` and `raw/` | Memory Garden inputs for context compilation. |
| `outputs/` | Generated artifacts and synthesized results. |
| `assets/` | Images and visual assets used by the package. |
| `plans/` | Adoption and migration plans. |

Current canonical skills cover orchestration, Codex delegation, Claude Desktop delegation, CI/CD, marketing, image generation, self-improvement, and Crow Voice.

## Progressive Disclosure

Load the smallest useful unit first.

Start with root `SKILL.md` files. Load workflows, templates, references, contracts, rubrics, examples, and policies only when the selected skill says the task needs them.

Use `skills/skill-map.md` as a derived semantic routing map. The source of truth remains the root `SKILL.md` files.

Use context capsules for task context. Do not bulk-load memory, wiki folders, transcripts, or raw sources by default.

Do not add a vector database, embedding index, or hidden retrieval layer for v1 routing.

## Capability Binding

When a task needs an ability before it knows the concrete tool, use the Capability Broker (`adapters/patterns/capability-broker.md`).

Examples include `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, and `external_write`.

The broker binds those requests to available adapters such as MCP gateways, browser automation, CLIs, APIs, harness-native tools, local app surfaces, or LLM capability profiles.

Prefer specific APIs, CLIs, connectors, and tool adapters before generic browser or desktop automation.

## Memory Garden

The Memory Garden (`/wiki/`) is crow.pet's Karpathian LLM Wiki.

Markdown is the map, not the warehouse. Use indexes, source manifests, and context capsules. Keep raw sources and full transcripts out of hot context unless the task requires them.

Use Obsidian through adapters. Do not make Obsidian syntax a core memory requirement.

## How To Use

1. Point an LLM harness at this folder.
2. Load `AGENTS.md` and the relevant root `SKILL.md`.
3. Use `skills/skill-map.md` to select the smallest useful skill set.
4. Attach a context capsule only when memory affects execution.
5. Let adapters translate to the active harness, model, tool, target, or memory surface.
6. Evaluate results with the relevant contract and rubric.
7. Promote durable learning into skills, rubrics, contracts, policies, or the Memory Garden.

## Schema

`CLAUDE.md` contains the full schema and behavioral rules governing all Memory Garden (`/wiki/`) operations.
