# DEB-TITMAS-001 Experiment Package

Machine- and human-readable preparation package for
**TITMAS Agent-Native Ecology Box 001**.

Start in this order:

1. [Constitution](constitution.md)
2. [Protocol](protocol.md)
3. [Pre-registration](pre-registration.md)
4. `freeze-manifest.yaml` and `freeze-review.yaml`
5. [Fairness review](fairness-review.md) and [bias analysis](bias-analysis.md)
6. [Blind evaluation protocol](blind-evaluation-protocol.md),
   `independent-reviewer-model.yaml` and `blind-custodian-protocol.yaml`
7. `provider-privacy-retention-policy.yaml` and `agent-lineage-plan.yaml`
8. [Human-first plan](baseline-execution-plan.md) and
   [Agent-native plan](agent-native-execution-plan.md)
9. `stop-rules.yaml` and [success criteria](success-criteria.md)
10. `participants/schema.json` and `participants/registry.yaml`
11. `roles/registry.yaml` and `tasks/task-registry.yaml`
12. `metrics/schema.json`, `failure-scenarios/registry.yaml` and
    [Final report template](reports/final-report-template.md)
13. [Execution Readiness Package](readiness/README.md)
14. [Operational Calibration Record](calibration/calibration-report-v0.1.md)
15. [Operational Calibration v0.2 Record](calibration/v0.2/calibration-report-v0.2.md)
16. [Candidate Grounding and Incremental Validation](calibration/grounding/candidate-grounding-report-v0.1.md)

```text
PACKAGE_STATUS=PREPARED
PREREGISTRATION_COMPLETE=true
EXECUTION_REVIEW_COMPLETE=true
FAIRNESS_REVIEW_STATUS=PASS
FAIRNESS_PASS_SCOPE=PROTOCOL_DESIGN_COMPLETENESS_ONLY
EXECUTION_PREREQUISITES_STATUS=NOT_SATISFIED
EXECUTION_READINESS_PACKAGE_COMPLETE=true
OPERATIONAL_PREREQUISITES_SATISFIED=false
GO_NO_GO_STATUS=NO_GO
GO_NO_GO_REASON=NO_GO_PENDING_OPERATIONAL_ASSIGNMENTS_AND_HUMAN_AUTHORIZATION
EXECUTION_AUTHORIZATION_CANDIDATE_READY=true
EXECUTION_AUTHORIZATION_CANDIDATE_READY_MEANS=HUMAN_REVIEW_PACKET_COMPLETE_NOT_EXECUTION_READY
EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
VALUE_PROVEN=false
REAL_AGENT_CONTRIBUTION_AUTHORIZED=false
REAL_GIT_ACCESS_AUTHORIZED=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
```

The separately authorized operational calibration was attempted with three
exact Provider/Model lineages and stopped fail-closed after a local
normalization exception caused critical handoff-record loss:

```text
OPERATIONAL_CALIBRATION_EXECUTED=true
CALIBRATION_STATUS=CALIBRATION_ABORTED_FOR_SAFETY
OPERATIONAL_PIPELINE_DEMONSTRATED=false
FORMAL_EXPERIMENT_STATE_EFFECT=NONE
```

The calibration result does not close any of the sixteen formal readiness
blockers, change `GO_NO_GO_STATUS=NO_GO`, or establish value. See the
[full calibration report](../../../TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-OPERATIONAL-CALIBRATION-REPORT-v0.1.md).

The separately authorized v0.2 hardening passed 14/14 deterministic failure
injections and 36/36 role-contract fixtures. Its one permitted rerun completed
all three durable pipelines across the three exact Provider/Model lineages,
but one candidate still referenced a missing machine surface and failed local
conformance:

```text
OPERATIONAL_CALIBRATION_V0_2_EXECUTED=true
CALIBRATION_V0_2_STATUS=CALIBRATION_NEGATIVE_RESULT
PIPELINES_COMPLETED_DURABLY=3
OPERATIONAL_PIPELINE_DEMONSTRATED=false
CALIBRATION_ROUTE_DECISION=STOP_DIRECT_CALIBRATION_RERUNS
```

The v0.2 result demonstrates that the two v0.1 persistence and type-safety
defects were removed in this run. It does not demonstrate Agent-native value,
formal experiment readiness, adoption or commercial value. Direct calibration
reruns now require a new Human decision and a minimal runner redesign review.

The deterministic Candidate Grounding redesign now resolves required
references against the exact frozen repository tree before Reviewer handoff.
Its historical replay rejects the v0.2 Task 1 missing machine surface before
review, and its 20/20 grounding plus 6/6 metric fixtures pass. This is a design
and local validation result only:

```text
CANDIDATE_GROUNDING_REDESIGN_COMPLETE=true
RESOURCE_RESOLUTION_GATE_OPERATIONAL=true
INCREMENTAL_CONFORMANCE_OPERATIONAL=true
REVIEWER_GROUNDING_CONTRACT_OPERATIONAL=true
MODEL_CALL_COUNT=0
CALIBRATION_V0_3_AUTHORIZED=false
CALIBRATION_V0_3_EXECUTED=false
```

The original v0.2 candidate, Reviewer `PASS`, final failure and route decision
remain immutable. The Review Catch correction is append-only and does not
rewrite history or prove Reviewer effectiveness, model-pipeline behavior, or
Agent-native value.

The files under `runs/`, `reviews/`, `memories/` and `reports/` are contracts
or templates. They are not execution records, canonical Evidence, adopted
Memory, experiment results or public reports.

`EXECUTION_AUTHORIZATION_CANDIDATE_READY=true` means that a bounded Human
decision packet can be reviewed. It does not mean that fairness corrections
are operationally instantiated or that experiment execution is ready or
authorized.

The fairness `PASS` applies only to protocol-design completeness. Reviewer and
blind-custodian instances remain unassigned, no Provider profile is adopted,
all lineage counts are zero and every Human Decision remains `UNDECIDED`.

The readiness package is a Human review candidate, not an execution-
authorization result. Its deterministic `NO_GO` identifies open assignments,
adoptions and decisions without treating them as an experiment failure.
