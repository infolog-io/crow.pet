# Public Export Policy

This repository contains reusable source material for crow.pet.

## Public-Safe Rules

- Keep reusable software and architecture here.
- Use neutral aliases in public examples.
- Prefer simulated examples over real user or customer traces.
- Preserve license and attribution notices.

## Memory Boundary

The Memory Garden (`/wiki/`) in this repo is public package knowledge only.

Personal or organization-specific Memory Gardens belong in a separate instance.

## Obsidian Boundary

Obsidian is an adapter, not core memory.

Keep `.obsidian/` workspace files out of the package.

## Pre-Publish Check

Before publishing:

1. Search for environment-specific identifiers.
2. Search for credential-like strings.
3. Confirm `.obsidian/` is untracked.
4. Confirm examples use public-safe simulated data.
5. Confirm generated artifacts do not contain private context.
