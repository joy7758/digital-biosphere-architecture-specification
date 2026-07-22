---
document_id: TMAI-PRODUCTION-ARCHITECTURE-BASELINE-FREEZE-RECORD-0.1
title: TMAI Production Architecture Baseline Freeze Record v0.1
title_zh: TMAI 生产架构基线冻结记录 v0.1
status: immutable-content-baseline-remote-verified
recorded_at: 2026-07-22T12:05:04+08:00
decided_by_ref: zhangbin
primary_repository: digital-biosphere-architecture
production_ready: false
---

# TMAI Production Architecture Baseline Freeze Record v0.1

中文：TMAI 生产架构基线冻结记录 v0.1。

## Frozen Content Identity（冻结内容身份）

```text
BRANCH=codex/production-observability-baseline
BASE_COMMIT=769b5589d07eb9bc9efbaf0930039c3d49632372
CONTENT_COMMIT=264f3171c3dfa8a9f614c7d0c835e4be26870d01
CONTENT_TREE=b83f25d9f5e6b47f7d6717320026cc242c817b03
CONTENT_COMMIT_SUBJECT=feat(architecture): adopt production observability baseline
```

`CONTENT_COMMIT` 是后继 DBOS `DQ-018` 实施必须绑定的规范内容身份。本冻结记录位于后继 governance
attestation commit（治理见证提交）中，避免让内容基线引用自身而产生循环 SHA。

## Recorded Decisions（已记录决定）

```text
DQ-022=ADOPT_OTLP_1_11_0_REFERENCE_BASELINE
DQ-023=ADOPT_OTEL_SEMCONV_1_43_CORE_AND_PINNED_GENAI_MAPPING
DQ-024=ADOPT_OTEL_SCHEMA_RESOURCE_1_59_AND_QUARANTINE_DEVELOPMENT_ENTITY
DQ-025=ADOPT_OTEL_COLLECTOR_V0_156_CUSTOM_MINIMAL_INVENTORY
ADR-024=ACCEPT_STAGED_TELEMETRY_PRODUCTION_PATH
DQ-018=AUTHORIZE_DBOS_PR_2A_TELEMETRY_ADMISSION_FOUNDATION
decided_by_ref=zhangbin
dbos_domain_owner_ref=zhangbin
```

## Validation Bound to the Content Commit（内容提交所绑定验证）

- site production build：`PASS`；
- site tests：`11/11 PASS`；
- site lint：`PASS`；
- Draft 2020-12 Schema：`15/15` meta-valid；
- canonical data/example pairs：`15/15 PASS`；
- decision registry negatives：`15/15 REJECTED`；
- decision-input digests：`13/13 MATCH`；
- Markdown local links：`156 files / 816 checked / 0 missing`；
- OTLP / Semantic / Schema-Resource / Collector catalogs：`56/46/45/48` complete，全部
  `NOT_EXECUTED`。

## Authority Boundary（权力边界）

该冻结关闭 DBA `PR-G0` 的内容身份前置。后继 DQ-018 的实现事实由独立 DBOS receipts 证明，
不能反向改写本冻结记录。它不选择
production backend，不构建 Collector，不创建 listener、Agent、Runtime、Entity、Evidence 或 Permission，
也不形成 deployment 或 `PRODUCTION_READY`。

## Remote Verification Update（远端复验更新）

```text
DBA_REMOTE_BRANCH=codex/production-observability-baseline
DBA_REMOTE_RECEIPT_COMMIT=05589af948a788f38982b5b197427a6e1c357fa8
DBA_CONTENT_COMMIT_REACHABLE=true
DBOS_DQ018_SOURCE_COMMIT=5c52c1c2f44767c0b13b4ac9670425721b9ea0dd
DBOS_DQ018_RECEIPT_COMMIT=aa6440e83f35cc63483f487367ccb573bba7681a
REMOTE_BRANCH_VERIFICATION_PENDING=false
```

```text
ARCHITECTURE_CONTENT_FROZEN=true
REMOTE_BRANCH_VERIFICATION_PENDING=false
DQ_018_IMPLEMENTATION_AUTHORIZED=true
DQ_018_IMPLEMENTATION_MAY_START=false
FRESH_DBOS_BEFORE_STATE_REQUIRED=false
COLLECTOR_SELECTED=false
BACKEND_SELECTED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
EVIDENCE_CREATED=false
PERMISSION_GRANTED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
