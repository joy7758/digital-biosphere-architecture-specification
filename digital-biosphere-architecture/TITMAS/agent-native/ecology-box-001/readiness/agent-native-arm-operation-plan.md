# Agent-native Arm Operation Plan v0.1

This readiness supplement operationalizes but does not alter the frozen
[`agent-native-execution-plan.md`](../agent-native-execution-plan.md).

```text
Discovery
-> Eligibility Check
-> Task Match
-> Bounded Lease
-> Finding
-> Value Gate
-> Contribution Candidate
-> Independent Review
-> Revision
-> Conformance
-> Blind Submission
-> Outcome Evaluation
-> Memory Binding
```

Every stage records `input_ref`, `participant_ref`, `role_ref`,
`source_revision`, `start_time`, `end_time`, `action_count`, `output_ref`,
`evidence_binding`, `human_intervention`, `failure`, `abstention` and
`limitations`.

The Agent cannot change task, metric, context, budget, role or lease. A
Contributor cannot be the only Reviewer; one session cannot self-approve; any
Human correction or exception after session start is a Human intervention.

```text
PARTICIPANT_ASSIGNED=false
SESSION_CREATED=false
EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
```
