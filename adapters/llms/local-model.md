# Local Model LLM Adapter

## Purpose

Support local or private models without changing skills.

## Runtime Target

Local model runtime.

## Capabilities

- Offline inference.
- Private task processing.
- Low-risk drafting.

## Inputs

- Task record.
- Prompt text.
- Local context.

## Outputs

- Model response.
- Confidence notes.
- Handoff report.

## Permissions

- Keep data local.
- Follow the same approval policy as hosted models.

## Invocation

Use the configured local model runner.

## Failure Modes

- Model unavailable.
- Low-quality output.
- Missing context window.

## Logging

Log local model name, task ID, and runtime errors.

## Verification

Run a known prompt and compare against expected structure.

## Handoff Mapping

Map local model output into the common handoff report.
