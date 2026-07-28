# Ecology Box 001 Experiment Runbook v0.1

## Status

```text
RUNBOOK_DEFINED=true
RUNBOOK_ADOPTED=false
EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
```

The runbook operates only after the final Go/No-Go review returns `GO` and
`HD-EB-06=ACCEPT`. Its source is the exact frozen ten-task registry; it cannot
substitute a three-task sample.

## Preflight

1. Verify the frozen source, ten tasks, metrics, roles and criteria hashes.
2. Verify every blocking prerequisite is `SATISFIED`.
3. Verify participant, lineage, Reviewer, custodian and Provider records.
4. Verify budgets, data policy, randomization and abort controls are accepted.
5. Record the exact Human execution authorization and expiry.

Any failure returns `NO_GO` without starting a session.

## Human-first arm

Use the frozen [`../baseline-execution-plan.md`](../baseline-execution-plan.md)
and its readiness
[`human-first-baseline-operation-plan.md`](human-first-baseline-operation-plan.md).
The prospective matched plan must use the same source, tasks, inputs, outputs,
rubric and blind evaluation as the Agent-native arm. Historical work cannot
silently become the matched baseline.

## Agent-native arm

Use the frozen
[`../agent-native-execution-plan.md`](../agent-native-execution-plan.md) and
its readiness
[`agent-native-arm-operation-plan.md`](agent-native-arm-operation-plan.md):

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

Each stage must record:

- `input_ref`, `participant_ref`, `role_ref`, `source_revision`;
- `start_time`, `end_time`, `action_count`, `output_ref`;
- `evidence_binding`, `human_intervention`;
- `failure`, `abstention`, `limitations`.

## Prohibitions

- no Agent self-authorization or self-approval;
- no Contributor as sole Reviewer;
- no same-session self-approval;
- no task, metric, context or Permission expansion;
- no Agent-declared final outcome;
- no real Git, external network or unapproved Provider fallback.

Negative, mixed, invalidated and aborted outcomes remain preserved under their
exact state and cannot be deleted or rewritten as value proof.
