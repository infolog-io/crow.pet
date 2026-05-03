# Skill Architect Contract

The Skill Architect succeeds when it chooses a minimal, portable execution architecture for a skill or repeated workflow before implementation.

Required:

- classify the workflow as `inline`, `thin-references`, `deterministic-script`, `composed-pipeline`, or `manual-side-effect`
- explain why the selected mode fits and why heavier modes were not chosen
- define isolation, handoff strategy, dynamic context, context budget, cleanup policy, and capability needs
- use stage handoffs for composed pipelines
- route runtime-specific behavior through adapters
- route side effects through policy gate
- declare unsupported target-harness features as warnings instead of silently dropping them
- evaluate context efficiency before accepting the architecture

Forbidden:

- add pipeline structure without a workflow need
- put Claude-, Codex-, or harness-specific fields directly into canonical skills as the source of truth
- inject raw large files as context
- bypass compact handoffs for noisy stages
