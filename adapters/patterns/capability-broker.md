# Capability Broker Pattern Adapter

## Purpose

Bind semantic capability requests to the safest available adapter.

Use this pattern when a skill, role brief, or future Agent Assembly task needs an ability such as `web_research`, `browser_control`, `deploy_inspect`, `repo_read`, `visual_understanding`, `external_write`, or `tool_execution` without naming a specific tool.

Keep durable semantics in skills and task-local artifacts. Keep runtime bindings at the adapter edge.

## Runtime Target

Runtime-neutral orchestration over available adapters, harness-native tools, MCP gateways, browser automation, local app control surfaces, and LLM capability profiles.

## Capabilities

- Normalize capability requests into task-local capability bindings.
- Select specific adapters before generic automation when both are available.
- Bind `web_research` to an approved browser, MCP, search, or harness-native research surface.
- Bind `deploy_inspect` and `deploy_change` to Vercel, GitHub, CLI, MCP, or browser surfaces according to policy.
- Bind `repo_read` and `repo_write` to harness, CLI, GitHub, or local filesystem surfaces according to policy.
- Bind `visual_understanding` to image, browser, or LLM capability profiles when available.
- Bind LLM needs such as `reasoning`, `vision_language`, `small_local`, `tool_action`, `code_generation`, and `multimodal_grounding` without creating acronym-specific adapters.
- Produce an invocation plan with permission, verification, and handoff requirements.

## Inputs

- Task record.
- Selected skill or role brief.
- Requested semantic capabilities.
- Available adapter descriptions.
- Policy gate result.
- Context capsule when memory affects execution.

## Outputs

- Task-local capability bindings.
- Selected adapter list.
- Permission requirements.
- Invocation plan.
- Verification notes.
- Handoff report.

## Permissions

- Follow the policy gate before invoking any bound adapter.
- Ask before external writes, auth-sensitive actions, deploy changes, purchases, uploads, publishing, or destructive operations.
- Ask before sending private user or project context to remote tools.
- Do not escalate permissions automatically because a preferred adapter is unavailable.
- Prefer read-only inspection before state-changing actions.

## Invocation

1. Read the requested capabilities from the selected skill, role brief, or task-local ontology.
2. Inspect the relevant adapter descriptions already available to the harness.
3. Prefer dedicated tool, harness, CLI, API, or connector adapters over browser or desktop automation.
4. Use MCP gateways when they expose the needed tool, resource, or prompt through the active harness.
5. Use browser or local app control only when the task requires visual or interactive behavior, no safer specific adapter exists, or the user requested that surface.
6. Record the task-local capability binding before invocation.
7. Invoke each selected adapter with the smallest necessary context.
8. Verify the result through the selected adapter or an independent read path.

## Failure Modes

- No adapter can satisfy a requested capability.
- Multiple adapters satisfy the same capability with different permission profiles.
- The safest adapter lacks auth, scope, or runtime availability.
- Browser or local app automation reaches an ambiguous UI state.
- MCP tool metadata is incomplete or stale.
- A bound adapter returns output that cannot be verified.

## Logging

Log task ID, requested capability, selected adapter, permission level, invocation surface, verification method, and fallback reason when a less specific adapter is used.

Do not log secrets, credentials, private profile details, or full memory files.

## Verification

Confirm each capability binding points to an existing adapter, harness-native tool, MCP surface, browser surface, local app surface, or LLM capability profile.

Confirm state-changing actions have approval before invocation.

Confirm results through URLs, command output, screenshots, API reads, local file checks, or adapter-specific verification.

## Handoff Mapping

Map selected capability bindings into the handoff report as adapter decisions.

Map outputs from bound adapters into task artifacts, verification notes, and `memory_updates` only when learning should be promoted through Self-Improvement.
