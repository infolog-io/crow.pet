# MCP Gateway Tool Adapter

## Purpose

Use MCP tools, resources, and prompts as capability surfaces without making MCP core architecture.

The Capability Broker may bind semantic needs such as `web_research`, `repo_read`, `deploy_inspect`, `memory_lookup`, or `tool_execution` to an MCP server when the active harness exposes one.

## Runtime Target

MCP servers, tools, resources, and prompts available through the active harness.

## Capabilities

- Discover MCP tools, resources, and prompts exposed by the harness.
- Map MCP surfaces to crow.pet semantic capabilities.
- Read MCP resources when policy allows.
- Invoke MCP tools when policy allows.
- Capture MCP outputs as task artifacts or context capsule inputs.
- Report unavailable, ambiguous, or unsafe MCP bindings.

## Inputs

- Task record.
- Capability binding from the Capability Broker.
- MCP server, tool, resource, or prompt identifier.
- Permission classification.
- Context capsule when task context is required.

## Outputs

- Tool result.
- Resource excerpt or reference.
- Prompt output.
- Invocation notes.
- Handoff report.

## Permissions

- Follow the policy gate before reading sensitive resources or invoking tools.
- Ask before external writes, deploy changes, publishing, uploads, destructive actions, or sending private context to remote MCP servers.
- Treat unknown MCP servers as untrusted until the harness or user confirms scope.
- Do not pass full Memory Garden, user profile, identity, or secret-bearing files to MCP tools by default.

## Invocation

Use the active harness MCP surface.

Bind one semantic capability to one MCP surface at a time unless the Capability Broker explicitly selects a multi-step plan.

Pass the smallest useful task context.

Prefer a dedicated first-party adapter when one exists and has the required permission scope.

## Failure Modes

- MCP server unavailable.
- Tool or resource name changed.
- Permission scope missing.
- Tool result is partial, stale, or unverifiable.
- MCP server requests broader context than the task needs.
- External side effect requires approval that has not been granted.

## Logging

Log task ID, MCP server, tool/resource/prompt name, permission level, arguments summary, and result reference.

Do not log secrets or full private context.

## Verification

Confirm the MCP result satisfies the requested capability.

Confirm state-changing results through a read-back action, URL, status output, or dedicated adapter verification when available.

Confirm sensitive context was not sent beyond the approved scope.

## Handoff Mapping

Map MCP outputs into task artifacts, evidence references, and handoff verification notes.

Map reusable MCP capability bindings to Self-Improvement proposals only after repeated successful use.
