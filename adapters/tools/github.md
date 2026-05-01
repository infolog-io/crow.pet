# GitHub Tool Adapter

## Purpose

Interact with GitHub without changing skills.

## Runtime Target

GitHub API, CLI, or connector.

## Capabilities

- Read issues.
- Read pull requests.
- Inspect checks.
- Create comments after approval.

## Inputs

- Task record.
- Repository.
- Issue, PR, or check ID.

## Outputs

- Check summary.
- PR summary.
- Handoff report.

## Permissions

- Ask before comments, pushes, PRs, or merges.

## Invocation

Use the configured GitHub surface.

## Failure Modes

- Missing auth.
- Rate limit.
- Permission denied.

## Logging

Log repo, URL, action, and task ID.

## Verification

Confirm URLs and action results.

## Handoff Mapping

Map GitHub results into task artifacts and handoff reports.
