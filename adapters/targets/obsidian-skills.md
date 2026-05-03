# Obsidian Skills Target Adapter

## Purpose

Export crow.pet behavior into Obsidian-compatible agent skills.

## Runtime Target

Skills-compatible agents working inside Obsidian vaults.

## Native Constructs

- Agent Skills.
- `SKILL.md`.
- Obsidian-flavored markdown.
- Bases.
- JSON Canvas.
- Obsidian CLI.
- Defuddle extraction.

## Capabilities

- Generate Obsidian-facing skill packs.
- Preserve portable crow.pet source skills.
- Add Obsidian references as adapter details.
- Validate generated vault artifacts.
- Produce public-safe exported names.

## Inputs

- Canonical crow.pet skill folder.
- Obsidian adapter policy.
- Vault compatibility target.
- Public export profile.
- Alias map.

## Outputs

- Obsidian skill export notes.
- Generated skill package plan.
- Validation checklist.
- Public-safe naming report.

## Permissions

- Keep canonical skills runtime-neutral.
- Do not copy private IL context into public exports.
- Preserve upstream license notices.
- Ask before installing generated skills globally.

## Invocation

Use when producing Obsidian-specific skills.

Use after core skill behavior is stable.

Run obfuscation checks before public export.

## Export Mapping

Map core wiki behavior to `obsidian-markdown`.

Map dashboards to `obsidian-bases`.

Map relationship maps to `json-canvas`.

Map vault automation to `obsidian-cli`.

Map web cleanup to `defuddle`.

Map private names through alias rules before export.

## Failure Modes

- Export becomes source of truth.
- Obsidian syntax leaks into core skills.
- Private aliases are missing.
- Generated skill exceeds context budget.
- Validation relies on a missing plugin.

## Logging

Log source skill hash, export target, alias profile, and validation result.

## Verification

Confirm exported skills have root `SKILL.md`.

Confirm generated files render in Obsidian.

Confirm public export contains no private paths.

## Handoff Mapping

Map exported package paths into `artifacts`.

Map validation findings into the handoff report.
