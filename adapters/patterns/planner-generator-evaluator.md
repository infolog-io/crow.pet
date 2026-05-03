# Planner Generator Evaluator Pattern Adapter

## Purpose

Run tasks through planner, generator, and evaluator stages.

## Runtime Target

Runtime-neutral orchestration pattern.

## Capabilities

- Plan work.
- Generate outputs.
- Evaluate against criteria.
- Retry once when policy allows.

## Inputs

- Task record.
- Success criteria.
- Rubric.

## Outputs

- Plan.
- Draft output.
- Evaluation report.
- Handoff report.

## Permissions

- Follow approval policy before external writes.

## Invocation

Apply this pattern when quality risk is higher than latency risk.

## Failure Modes

- Bad plan.
- Failed evaluation.
- Retry limit reached.

## Logging

Log each stage and evaluation outcome.

## Verification

Confirm every generated output has an evaluation result.

## Handoff Mapping

Map the final evaluation into the common handoff report.
