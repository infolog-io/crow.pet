# Browser Tool Adapter

## Purpose

Use browser automation for web research, visual inspection, and interactive web workflows when a safer specific adapter is unavailable or the user requests browser control.

Browser automation is an adapter capability, not the default path.

## Runtime Target

Browser automation, computer-use browser control, harness-native browser tools, or local browser surfaces.

## Capabilities

- Search and navigate web pages.
- Capture source URLs, page text, screenshots, and visual state.
- Extract bounded information for task artifacts.
- Fill forms, click controls, copy, and paste when policy allows.
- Inspect authenticated pages when the user has approved the scope.
- Support `web_research`, `browser_control`, `visual_inspection`, and interactive fallback workflows.

## Inputs

- Task record.
- Capability binding from the Capability Broker.
- URL, search query, or target web workflow.
- Allowed action scope.
- Context capsule when task context is required.

## Outputs

- Research notes.
- Source URLs.
- Screenshots or visual observations.
- Extracted facts.
- Completed approved browser action.
- Handoff report.

## Permissions

- Prefer official APIs, CLIs, connectors, or MCP tools when they provide the same capability safely.
- Ask before login-sensitive actions, external posting, purchases, uploads, deploy changes, destructive operations, or form submissions that affect other systems.
- Ask before copying private user or project data into a web page.
- Do not store credentials.
- Do not bypass paywalls, access controls, rate limits, or explicit site restrictions.

## Invocation

Use browser automation only when the task needs web research, visual confirmation, an interactive-only workflow, or an explicit user-requested browser action.

Keep navigation scoped to the task.

Capture source URLs for facts used in outputs.

Before a state-changing click or submission, stop for approval unless the task and policy already grant that exact action.

Verify final state through the page, a confirmation URL, screenshot, or a dedicated adapter read-back when available.

## Failure Modes

- Page requires unavailable authentication.
- UI state is ambiguous.
- Site blocks automation.
- Extracted content is stale or contradicted by another source.
- Browser action has an external side effect that lacks approval.
- Visual state cannot be verified.

## Logging

Log task ID, URLs, action class, permission level, screenshot paths when captured, and verification method.

Do not log credentials, session tokens, or full private page contents unless explicitly approved for the task artifact.

## Verification

Confirm facts against source URLs or screenshots.

Confirm state-changing actions through visible page state, confirmation messages, API/CLI read-back, or another approved adapter.

Confirm no out-of-scope browser action occurred.

## Handoff Mapping

Map browser findings into task artifacts with source URLs and screenshots where useful.

Map approved browser actions into handoff verification notes and memory updates only when they affect future execution.
