# Policy Gate Contract

The policy gate must:

- classify the proposed action across the decision axes
- return exactly one of `Silent`, `Notify`, `Ask`, or `Block`
- apply precedence `Block > Ask > Notify > Silent`
- include a reason
- include approval text for `Ask`
- refuse blocked actions without reframing the task

It must not:

- lower risk assigned by another policy, skill, or adapter
- approve secret exposure
- remove or bypass safety gates
- approve destructive production actions without explicit policy change
