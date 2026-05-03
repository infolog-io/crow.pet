# Image Generation Tool Adapter

## Purpose

Route image tasks to approved generation or editing tools.

## Runtime Target

Configured image generation tool.

## Capabilities

- Generate drafts.
- Edit images.
- Store prompts.
- Store outputs.

## Inputs

- Task record.
- Image brief.
- Source images.
- Brand constraints.

## Outputs

- Image files.
- Prompt history.
- Evaluation notes.

## Permissions

- Ask before publishing externally.
- Never claim generated images are real photos.

## Invocation

Use the configured image tool for draft generation.

## Failure Modes

- Tool unavailable.
- Output misses brief.
- Unsafe prompt.

## Logging

Log prompt, output path, tool name, and task ID.

## Verification

Evaluate output against the image brief.

## Handoff Mapping

Map image outputs into task artifacts and handoff reports.
