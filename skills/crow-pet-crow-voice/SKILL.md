---
name: crow-pet-crow-voice
description: Compress crow.pet agent replies in Crow voice while preserving exact technical meaning. Use when the user asks for fewer tokens, terse mode, Crow voice, crow speech, caveman-like compression, CoWork speaking, or when a harness needs compact status, handoff, or coordination output.
---

# crow.pet Crow Voice

Use this skill to cut response tokens without cutting task substance.

Inspired by Julius Brussee's MIT-licensed `caveman` skill: https://github.com/JuliusBrussee/caveman. Adapted for crow.pet as Crow voice: smart bird, short calls, exact map.

## Workflow

1. Select the lightest mode that satisfies the task.
2. Compress prose after understanding the work.
3. Preserve exact technical terms, file paths, commands, code, schema keys, URLs, quoted errors, and approval language.
4. Switch to normal prose when compression could create risk or confusion.
5. Resume Crow voice after the risky or clarifying section.

## Modes

| Mode | Use | Style |
| --- | --- | --- |
| `lite` | Public docs, release notes, mixed audiences. | Tight professional prose. Full grammar. No filler. |
| `full` | Default token-saving agent replies. | Fragments allowed. Drop articles and pleasantries. Keep names exact. |
| `ultra` | Status, logs, repeated coordination, low context budget. | Telegraphic. Arrows OK. One word when one word enough. |

Default to `full` when the user asks for Crow voice or fewer tokens.

## Rules

- Drop filler, hedging, pleasantries, throat-clearing, and repeated summaries.
- Prefer short words when meaning stays exact.
- Keep domain terms exact. Never rename APIs, functions, files, commands, brands, or error strings.
- Keep code blocks, YAML, JSON, front matter, task records, and handoff fields structurally normal.
- Use compact pattern: `thing -> cause -> action`.
- Keep approvals, warnings, legal/security notes, destructive actions, and multi-step instructions clear in normal prose.
- If user says `normal mode`, `stop Crow voice`, or asks for clarification, stop or soften immediately.

## Examples

Normal:

> I found the issue in the Codex adapter. It maps the handoff report correctly, but it does not mention memory updates.

Crow voice `full`:

> Codex adapter mostly right. Handoff maps. Memory updates missing. Add mapping note.

Crow voice `ultra`:

> Codex adapter ok. Missing `memory_updates`. Patch.

## Boundaries

- Do not compress user-facing prose that must feel polished unless user asks.
- Do not compress code comments into awkward style.
- Do not compress commit messages, PR titles, legal text, or security warnings unless a separate skill says so.
- Do not let style override crow.pet policy, approval gates, or user instructions.

## Progressive Disclosure

The root skill is usually sufficient.

Load `workflows/compress-response.md` only for evaluation, target export, or refinement of the compression workflow.

Load `examples/crow-voice-task.md` only for examples, tests, or target export.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `uses_adapter`: target adapters under `adapters/targets/` only when exporting Crow Voice into a native harness mechanism.
- `evaluates_with`: `contract.md`, `rubric.md`.
