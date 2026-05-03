# Execution Architecture Pattern Adapter

## Purpose

Map portable crow.pet skill execution architecture into target harness behavior.

Use this pattern when a skill architecture plan declares isolation, selected agent, allowed tools, dynamic context, scripts, stages, or compact handoffs before a concrete runtime is selected.

## Runtime Target

Runtime-neutral execution semantics mapped by target adapters to Codex, Claude Code, Claude Desktop, OpenClaude, OpenClaw, Hermes, Cursor, Devin, or other harnesses.

## Capabilities

- Represent execution modes without hardcoding one harness.
- Represent `inline`, `thin-references`, `deterministic-script`, `composed-pipeline`, and `manual-side-effect`.
- Represent `none`, `single-isolated-context`, `per-stage-isolated-context`, and `manual-only` isolation.
- Map isolated stage work to harness-native subagents, forked context, or equivalent delegated sessions.
- Map allowed tools to target-specific permission surfaces.
- Map dynamic context to safe script-rendered or adapter-injected context.
- Map compact stage handoffs to files, handoff reports, or target-native artifacts.
- Warn when a target cannot support a requested execution feature.

## Inputs

- Skill architecture plan.
- Task record.
- Linked `SPEC.MD`.
- Target harness or adapter selection.
- Policy decision.
- Context capsule when memory affects execution.

## Outputs

- Runtime mapping notes.
- Target-specific warnings.
- Builder handoff requirements.
- Verification requirements.
- Handoff report references.

## Permissions

- Follow policy gate before mapping side-effect workflows.
- Do not grant target tools beyond the architecture plan.
- Do not treat isolated execution as approval for external action.
- Do not inject raw large files into model context.

## Invocation

Read `templates/skill-architecture.md`.

Choose a target mapping only after the execution mode is clear.

Translate portable fields such as `isolation`, `dynamic_context`, `handoff_strategy`, and `side_effects` into the selected harness adapter.

For targets that do not support a feature directly, emit an explicit warning and use the safest equivalent handoff pattern.

Keep the root skill authoritative for behavior. Keep the target mapping disposable.

## Failure Modes

- Target harness cannot support requested isolation.
- Dynamic context would inject too much content.
- Stage handoff lacks a compact output reference.
- Side-effect workflow lacks policy approval.
- Target adapter cannot express tool restrictions.

## Logging

Log architecture ID, target adapter, mapped features, warnings, policy decision, and verification requirements.

Do not log full raw stage outputs.

## Verification

Confirm the mapped runtime behavior preserves the architecture plan.

Confirm unsupported target features have warnings.

Confirm composed pipeline stages return compact handoffs.

Confirm dynamic context is distilled before injection.

## Handoff Mapping

Map runtime warnings, selected target behavior, stage handoffs, and verification evidence into the common handoff report.
