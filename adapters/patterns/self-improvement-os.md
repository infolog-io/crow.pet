# Self-Improvement OS Pattern Adapter

## Purpose

Convert corrections and repeated outcomes into safer future behavior.

## Runtime Target

Runtime-neutral improvement pattern.

## Capabilities

- Capture corrections.
- Detect repeated approvals.
- Propose skill updates.
- Propose policy updates.

## Inputs

- Task record.
- Owner correction.
- Evaluation report.
- Approval history.

## Outputs

- Memory note.
- Skill update proposal.
- Policy update proposal.

## Permissions

- Ask before lowering approval levels.
- Block removal of safety gates.

## Invocation

Run after task completion or explicit `/learn` commands.

## Failure Modes

- Conflicting memory.
- Unsafe policy change.
- Weak evidence.

## Logging

Log source task IDs and proposed changes.

## Verification

Require before and after behavior notes.

## Handoff Mapping

Map improvement output into memory updates and proposals.
