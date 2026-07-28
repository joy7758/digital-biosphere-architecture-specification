# Ecology Box 001 Execution Readiness Package v0.1

This directory makes the pre-execution gaps for the frozen ten-task experiment
explicit and machine-checkable. It does not assign a participant, adopt a
Provider, create a blind key, authorize execution or run the experiment.

## Current result

```text
READINESS_PACKAGE_COMPLETE=true
OPERATIONAL_PREREQUISITES_SATISFIED=false
GO_NO_GO_STATUS=NO_GO
GO_NO_GO_REASON=NO_GO_PENDING_OPERATIONAL_ASSIGNMENTS_AND_HUMAN_AUTHORIZATION
EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
VALUE_PROVEN=false
```

## Entry order

1. [`source-snapshot-manifest.yaml`](source-snapshot-manifest.yaml)
2. [`execution-prerequisites-matrix.yaml`](execution-prerequisites-matrix.yaml)
3. [`execution-readiness.yaml`](execution-readiness.yaml)
4. [`go-no-go-checklist.md`](go-no-go-checklist.md)
5. assignment and Provider templates
6. budget, data, randomization and confounder controls
7. [`experiment-runbook.md`](experiment-runbook.md)
8. [`abort-and-rollback-plan.md`](abort-and-rollback-plan.md)
9. [`final-go-no-go-review-template.md`](final-go-no-go-review-template.md)

Existing participant Schema, role registry, task registry, metrics, Evidence
and Verification boundaries remain canonical. This directory only references
them.

```text
READINESS_NE_AUTHORIZATION=true
AUTHORIZATION_NE_EXECUTION=true
EXECUTION_NE_VALUE_PROOF=true
SYNTHETIC_DRY_RUN_NE_EXPERIMENT_EXECUTION=true
```
