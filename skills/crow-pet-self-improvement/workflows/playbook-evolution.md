# Playbook Evolution Workflow

Use this workflow when a completed task creates a reusable lesson.

## Loop

```text
Generator -> Reflector -> Curator -> Playbook Delta
```

## Steps

1. Read the task record.
2. Read the handoff report.
3. Read the evaluation report or rubric result.
4. Classify outcome: success, partial, failure, or needs-human.
5. Extract one reusable lesson.
6. Check whether the lesson already exists in the target playbook, memory note, skill, rubric, contract, or policy.
7. Create the smallest useful delta update from `../../../templates/delta-update.yaml`.
8. Attach evidence and rollback instructions.
9. Assign risk level and approval requirement.
10. Apply only silent-safe deltas; otherwise request approval.

## No Whole Rewrite Rule

Self-improvement must not rewrite full skills, policies, rubrics, contracts, or playbooks by default.

Allowed low-risk deltas:

- add one playbook bullet
- update one playbook bullet
- increment helpful or harmful count
- mark one bullet for review
- add one public-safe example
- propose one policy change

Whole-file rewrites require explicit approval.
