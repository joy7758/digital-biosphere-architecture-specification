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

```text
PACKAGE_STATUS=PREPARED
PREREGISTRATION_COMPLETE=true
EXECUTION_REVIEW_COMPLETE=true
FAIRNESS_REVIEW_STATUS=PASS
FAIRNESS_PASS_SCOPE=PROTOCOL_DESIGN_COMPLETENESS_ONLY
EXECUTION_PREREQUISITES_STATUS=NOT_SATISFIED
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
