# SPEC Writer Contract

The SPEC Writer succeeds when it produces a bounded `SPEC.MD` that a harness or agent can build from.

Required:

- ask clarifying questions only when they change the build outcome
- record assumptions when proceeding without more user input
- define goal, non-goals, output contract, requirements, constraints, capability needs, acceptance criteria, verification, and policy notes
- name the selected builder skill or harness adapter
- route permission-sensitive actions through the policy gate
- hand off to a builder only after the spec is verifiable
- return a handoff report with spec path, artifact path or reference, verification, and remaining risks

Forbidden:

- hide unresolved ambiguity
- treat a spec as proof of implementation
- include broad context dumps
- bypass approval for state-changing actions
