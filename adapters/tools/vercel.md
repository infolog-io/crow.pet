# Vercel Tool Adapter

## Purpose

Interact with Vercel deployments and logs.

## Runtime Target

Vercel API, CLI, or connector.

## Capabilities

- Read deployments.
- Read logs.
- Inspect environment metadata.
- Trigger approved deployment actions.

## Inputs

- Task record.
- Project.
- Deployment URL or ID.

## Outputs

- Deployment status.
- Log summary.
- Handoff report.

## Permissions

- Ask before promote, rollback, or env changes.

## Invocation

Use the configured Vercel surface.

## Failure Modes

- Missing auth.
- Project not linked.
- Deployment unavailable.

## Logging

Log project, deployment ID, action, and task ID.

## Verification

Confirm deployment state through the Vercel surface.

## Handoff Mapping

Map Vercel results into task artifacts and handoff reports.
