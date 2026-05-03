# Adapter Support

Version 0.1 is a spec/prototype. Adapter support reflects markdown coverage and current maintenance intent, not guaranteed upstream compatibility.

Last reviewed: 2026-05-03.

## Primary

| Adapter family | Status | Notes |
| --- | --- | --- |
| Codex-compatible harnesses | Primary | Main working target for repo-local coding and handoff patterns. |
| Markdown bounded memory | Primary | Default public-safe memory pattern. |
| Capability Broker pattern | Primary | Default semantic binding pattern. |

## Best Effort

| Adapter family | Status | Notes |
| --- | --- | --- |
| Claude Desktop | Best effort | Desktop invocation requires local focus and permission checks. |
| OpenClaude / OpenClaw / Hermes | Best effort | Documented as target or harness mappings. |
| GitHub / browser / MCP / Vercel / image tools | Best effort | Use only when the active harness exposes the matching surface and policy allows it. |
| Target exports | Best effort | Generated views; canonical source remains `skills/`. |

## Maintenance Rule

When an upstream harness changes its skill, tool, MCP, or memory format, update only the relevant adapter or target export. Do not fork canonical skills for one runtime.
