# Obsidian Tool Adapter

## Purpose

Use Obsidian as an optional vault editor and renderer.

## Runtime Target

Obsidian desktop, vault folders, plugins, and CLI tools.

## Capabilities

- Read and write Obsidian-flavored markdown.
- Preserve wikilinks, embeds, callouts, and properties.
- Create `.base` operational views.
- Create JSON Canvas maps.
- Use CLI tools when installed.
- Validate vault-facing output.

## Inputs

- Task record.
- Context capsule.
- Vault path.
- Target file path.
- Output type.
- Obsidian compatibility requirements.

## Outputs

- Updated note.
- Generated `.base` file.
- Generated `.canvas` file.
- Validation result.
- Handoff report.

## Permissions

- Ask before changing vault settings.
- Ask before installing plugins.
- Ask before deleting notes.
- Keep secrets out of notes.
- Use aliases for private project names in public exports.

## Invocation

Use this adapter only for Obsidian-specific output.

Use portable markdown when Obsidian is not required.

Call the memory adapter before reading large vault sections.

## Failure Modes

- Obsidian syntax leaks into portable output.
- Vault path is wrong.
- Plugin or CLI is missing.
- Generated `.base` YAML is invalid.
- Generated canvas has broken node references.

## Logging

Log vault path alias, target file, output type, and capsule ID.

Do not log raw private note content.

## Verification

Validate markdown front matter.

Validate `.base` YAML.

Validate `.canvas` JSON.

Open or preview in Obsidian when available.

## Handoff Mapping

Map generated files into `artifacts`.

Map selected vault context into `context_capsules`.

Map note maintenance proposals into `memory_updates`.
