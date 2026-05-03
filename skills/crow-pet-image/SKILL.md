---
name: crow-pet-image
description: Generate, edit, and evaluate image assets from briefs, brand tasks, and campaign requests.
---

# crow.pet Image

Use this skill for image generation and editing.

## Workflow

1. Gather an image brief.
2. Confirm dimensions and format.
3. Load brand constraints when relevant.
4. Select the image tool adapter.
5. Generate or edit drafts.
6. Evaluate against the brief.
7. Store prompts and outputs.
8. Ask before external publishing.

## Progressive Disclosure

Load `templates/image-brief.md` only for image generation or editing.

Load `workflows/generate-image.md` only when producing drafts.

Load `examples/image-task.md` only for examples, tests, or target export.

Load `contract.md` and `rubric.md` only for acceptance or evaluation.

## Dependency Edges

- `uses_adapter`: `adapters/tools/image-generation.md`.
- `loads_context`: context capsule when brand constraints or prior image memory affects the brief.
- `evaluates_with`: `contract.md`, `rubric.md`.

## Rules

- Never claim generated imagery is real photography.
- Store prompt history.
- Use brand references for branded work.
- Evaluate every final candidate.
