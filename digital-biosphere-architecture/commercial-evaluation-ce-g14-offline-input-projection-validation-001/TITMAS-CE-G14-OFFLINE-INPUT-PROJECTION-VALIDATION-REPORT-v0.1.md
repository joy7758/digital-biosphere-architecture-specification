---
document_id: TITMAS-CE-G14-OFFLINE-INPUT-PROJECTION-VALIDATION-REPORT-0.1
title: TITMAS CE-G14 Offline Input Projection Validation Report v0.1
title_zh: TITMAS CE-G14 离线输入投影验证报告 v0.1
status: FAIL_CLOSED_AUTHORIZATION_CONSUMED
observed_at: 2026-07-28T15:04:36+08:00
primary_repository: digital-biosphere-architecture
execution_id: TITMAS-CE-G14-OFFLINE-PROJECTION-EXEC-001
decision_id: TITMAS-CE-G14-OFFLINE-PROJECTION-D01
implementation_effect: none
commercial_effect: none
authority_effect: none
---

# TITMAS CE-G14 Offline Input Projection Validation Report v0.1

## Result

```text
RESULT=FAIL_CLOSED
AUTHORIZATION_CONSUMED=true
EXECUTION_ATTEMPTS=1
RETRY=0
AUTOMATIC_REPAIR=0
CE_G14_EXECUTION_READINESS=false
```

The single authorized offline cycle stopped during positive canonical projection
validation. The program raised `AssertionError` at
`validate_projection(candidate)` before writing any projection artifact.

The exact failed assertion was not persisted. Therefore the cause is
`UNKNOWN`; this report does not infer or reconstruct it.

## Completed checks

- Isolated worktree and exact base commit: `PASS`.
- Decision and qualifying `qwen3.7-max` review binding: `PASS`.
- Source bundle SHA-256, byte count, and 16-resource count: `PASS`.
- Frozen five-resource selection and metadata/content binding: `PASS`.
- Positive canonical projection validation: `FAIL_CLOSED`.
- Negative cases executed: `0`.

## Artifact accounting

No projection/profile/schema/budget/fixture artifact was created:

```text
projection-profile.v0.1.json=false
context-compatible-input-projection.schema.v0.1.json=false
context-compatible-input-projection.v0.1.json=false
model-visible-byte-budget.v0.1.json=false
validation-fixtures.v0.1.json=false
```

Only the three failure-retention records exist:

1. `offline-validation-result.v0.1.json`;
2. `execution-receipt.v0.1.json`;
3. this report.

## Bounded execution observation

```text
NETWORK_REQUESTS=0
MODEL_REQUESTS=0
CREDENTIAL_READS=0
EXTERNAL_OR_CHILD_REPOSITORY_WRITES=0
RUNTIME_CREATED=false
AGENT_CREATED=false
ENTITY_CREATED=false
CAPABILITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_TRUTH_CHANGED=false
```

No retry, repair, diagnosis, public GET, technical reuse, model execution,
release, deployment, certification, or commercial offer was performed.

## Governance effect

This failure consumes the one-cycle execution authorization. It does not create
CE-G14 execution readiness and does not authorize a second execution.

The next eligible action is a new Recommendation-only artifact for a bounded,
read-only diagnostic that can identify the exact failed positive sub-check. That
diagnostic requires a new independent Decision and is not authorized by this
report.

```text
EVIDENCE_NE_TRUTH=true
EVALUATION_NE_AUTHORITY=true
RECOMMENDATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
CUSTOMER_ADOPTION_VERIFIED=false
MARKET_DEMAND_VERIFIED=false
COMMERCIAL_OFFERING=false
STANDARD_READY=false
PRODUCTION_READY=false
```
