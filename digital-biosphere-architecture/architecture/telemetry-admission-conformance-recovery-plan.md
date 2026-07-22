---
document_id: TMAI-DBOS-TELEMETRY-ADMISSION-CONFORMANCE-RECOVERY-0.1
title: DBOS Telemetry Admission Conformance and Recovery Plan v0.1
title_zh: DBOS 遥测准入符合性与恢复计划 v0.1
status: proposed-preimplementation-test-plan
scope: DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION
decision_reference: DQ-018
tests_executed: false
recovery_validated: false
implementation_authorized: false
production_ready: false
---

# DBOS Telemetry Admission Conformance and Recovery Plan v0.1

中文：DBOS 遥测准入符合性与恢复计划 v0.1。

## 1. Purpose（目的）

本计划预注册 `DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION` 的 conformance（符合性）、negative（负例）、fault（故障）、concurrency（并发）、migration（迁移）、backup/restore（备份恢复）和 rollback（回退）证据。它不执行测试，也不授权实现。

## 2. Test Truth Boundary（测试事实边界）

```text
Test Plan != Test Execution
Unit Pass != Production Conformance
Fault Injection Pass != Disaster Recovery Complete
Benchmark Result != SLO Achievement
Restore Pass != High Availability
```

所有结果必须绑定 exact source commit、Python/SQLite/platform versions、filesystem、test seed、fixture digests 和 command。任何 0-test discovery 必须失败。

## 3. Test Groups（测试组）

### 3.0 OTLP Reference Case Binding（OTLP 参考用例绑定）

[`otlp-v1.11-conformance-profile.md`](otlp-v1.11-conformance-profile.md) 与机器目录 [`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json) 将本计划的 protocol-facing subset（面向协议子集）冻结为 exact case IDs：

- `DQ-018` 获得实施授权后，只可执行 `OTLP-CG-SIGNAL_SCHEMA` 和 `OTLP-CG-AUTHORITY_BOUNDARY`；
- gRPC/HTTP listener、size-limit transport、retry、TLS、Collector 和 end-to-end accounting 属 `DQ-020/PR-G3`，明确不在 `DQ-018` 实施范围；
- `DQ-022` 未经 Human Version Decision 前，目录仍是 candidate-reference preregistration（候选参考预注册），不能称为 adopted conformance profile；
- catalog case result 必须同时映射到对应 `TA-*` case，二者任何一个失败都不能形成 `PR-G2` 通过。

### 3.1 Schema and Object Conformance（schema 与对象符合性）

| test ID | case | expected result |
|---|---|---|
| `TA-C001` | minimum valid TRACE metadata envelope | `ACCEPTED_AS_MATERIAL`; no Evidence ID |
| `TA-C002` | valid METRIC metadata envelope | accepted material with `NOT_APPLICABLE` context allowed |
| `TA-C003` | valid LOG metadata envelope | accepted material; no raw log body stored |
| `TA-C004` | PROFILE signal | `REJECTED / TA_SIGNAL_UNSUPPORTED` |
| `TA-C005` | unknown top-level/nested field | `REJECTED / TA_SHAPE_INVALID` |
| `TA-C006` | missing Resource | `REJECTED / TA_RESOURCE_MISSING` |
| `TA-C007` | missing Instrumentation Scope | rejected or `UNKNOWN` exactly as frozen policy; never accepted complete |
| `TA-C008` | unsupported object/profile version | fail closed with version reason |
| `TA-C009` | unknown semconv/schema URL | `UNKNOWN` or `REJECTED`; no runtime fetch |
| `TA-C010` | unpinned GenAI semconv | `REJECTED / TA_GENAI_SEMCONV_UNPINNED` |
| `TA-C011` | timestamp without timezone / invalid reference | rejected |
| `TA-C012` | limitations duplicate/overflow | rejected or deterministically normalized per frozen schema |

### 3.2 Authority and Evidence Negative Cases（权力与证据负例）

| test ID | injected claim | expected result |
|---|---|---|
| `TA-N001` | `entity_id` / identity verification | reject; no Entity record |
| `TA-N002` | Capability/Authorization/Permission fields | reject; no grant |
| `TA-N003` | `evidence_status=VALID` or Evidence ID | reject; no Evidence Object |
| `TA-N004` | `fitness`, `risk`, `recommendation`, `decision` | reject; no SAEE/Governance result |
| `TA-N005` | Collector reports `verified=true` | reject/ignore as prohibited authority claim |
| `TA-N006` | `trace_id` used as `observation_id` or idempotency key | reject |
| `TA-N007` | Admission result consumed as lifecycle activation | no callable path; source scan must prove absence |

### 3.3 Context, Delivery and Duplicate Cases（上下文、交付与重复）

| test ID | case | expected result |
|---|---|---|
| `TA-D001` | valid 16-byte trace ID / 8-byte span ID representation | correlation retained only |
| `TA-D002` | all-zero, wrong length or invalid Context | `TA_CONTEXT_INVALID`; no parent inference |
| `TA-D003` | replay same DBOS-issued receipt + admission ID + digest; committed row exists | original lifecycle retained; new append-only result `DUPLICATE_CONFIRMED`; no producer-auth claim |
| `TA-D004` | same DBOS-issued receipt + different admission ID or digest | `REJECTED / TA_IDEMPOTENCY_CONFLICT` |
| `TA-D005` | same upstream idempotency hint or fingerprint, but no valid DBOS receipt | both retained; second `DUPLICATE_SUSPECTED` |
| `TA-D006` | same `trace_id`, different valid observations | both retained |
| `TA-D007` | declared OTLP partial success | accepted/rejected counts and limitation preserved; no retry instruction invented |
| `TA-D008` | dropped/sampled-out/unknown delivery | never represented as complete |
| `TA-D009` | out-of-order timestamps | sequence remains canonical; clock limitation recorded |
| `TA-D010` | producer fabricates/self-declares DBOS receipt or references uncommitted row | `REJECTED / TA_INTAKE_RECEIPT_INVALID` |
| `TA-D011` | same fingerprint under different canonicalization versions | no confirmed duplicate; unsupported policy fails closed |
| `TA-D012` | deliberate fingerprint collision / legitimate identical metadata | both records retained; suspected only |

### 3.4 Sensitive Data and Resource Abuse（敏感数据与资源滥用）

| test ID | case | expected result |
|---|---|---|
| `TA-S001` | prompt/response/tool args/results keys | reject before persistence |
| `TA-S002` | bearer token/API key/session cookie canaries | no canary in output, exception, DB, backup, log or metrics |
| `TA-S003` | nested object depth overflow | bounded rejection |
| `TA-S004` | object/reference/reason/list size overflow | bounded rejection |
| `TA-S005` | high-cardinality IDs in metrics | IDs absent from metric attributes |
| `TA-S006` | schema URL pointing localhost/link-local/file | no network/filesystem read; unsupported result |
| `TA-S007` | control characters/log injection in detail | stable reason + escaped bounded detail |
| `TA-S008` | symlink/path traversal/world-readable target | store initialization rejected |
| `TA-S009` | unknown dynamic attribute hidden in input object / `extras` | exact serializer allowlist omits or rejects before persistence |
| `TA-S010` | user text, URL query, email or filesystem path supplied as a reference | rejected; only bounded opaque reference accepted |
| `TA-S011` | sensitive canary appears only in exception path or failed fixture artifact | no canary in exception, test report or retained diagnostic |

Canary 值必须由 test harness（测试框架）临时生成，不写入 repository。扫描覆盖 exact temporary store、WAL、backup、captured stdout/stderr、exception、metric sink 和 test artifact；报告只保留 `canary_present=false`、scanner version 和不可逆 fixture reference，不保留 canary 本文。

### 3.5 Transaction and Concurrency Faults（事务与并发故障）

| test ID | injection point | expected result |
|---|---|---|
| `TA-F001` | before transaction begins | no record, explicit failure |
| `TA-F002` | after lifecycle insert before record insert | rollback; no orphan lifecycle |
| `TA-F003` | before commit acknowledgement | either committed and discoverable or failed with no partial state |
| `TA-F004` | immediately after commit | committed record recoverable and idempotent on retry |
| `TA-F005` | lock timeout | `TA_STORAGE_UNAVAILABLE`; no fabricated acceptance |
| `TA-F006` | simulated disk full/write failure | rollback/fail closed; diagnostic retained outside false success path |
| `TA-F007` | database integrity/corruption detection | reads fail closed; no automatic repair/overwrite |
| `TA-F008` | 32 workers submit same key+digest | one original acceptance, remaining confirmed duplicates, no crash |
| `TA-F009` | 32 workers submit same key+different digests | at most one original binding; all conflicts rejected |
| `TA-F010` | self-observation sink failure | admission truth unchanged; bounded diagnostic emitted |
| `TA-F011` | WAL header/frame corruption or missing WAL after acknowledged commit fixture | integrity/recovery check fails closed; failed store preserved |
| `TA-F012` | abrupt separate-process termination at each persistence fault point | result is committed-and-discoverable or absent-and-failed; never partial success |
| `TA-F013` | concurrent thread + async task cancellation during validate/commit/receipt lookup | no partial state, leaked lock or false acknowledgement; retry classification deterministic |
| `TA-F014` | asynchronous cancellation during backup/restore validation | source and destination retained; neither becomes silently current |

Concurrency counts are deterministic stress fixtures, not a throughput SLO or production capacity claim.

### 3.6 Migration Tests（迁移测试）

| test ID | case | expected result |
|---|---|---|
| `TA-M001` | initialize empty v0.1 store | exact schema/migration checksum |
| `TA-M002` | reopen current version | no migration and no mutation |
| `TA-M003` | unknown newer store version | fail closed; no downgrade |
| `TA-M004` | tampered migration checksum | fail before apply |
| `TA-M005` | injected migration interruption | transaction rollback; original store usable |
| `TA-M006` | compatible additive fixture | backup→dry-run→apply→validate succeeds |
| `TA-M007` | breaking fixture without declared migration | rejected |
| `TA-M008` | second execution of same migration | deterministic no-op or explicit already-applied result |
| `TA-M009` | backup from prior compatible `0.1.x` fixture restored then migrated | pre-backup remains immutable; migration and post-validation deterministic |
| `TA-M010` | application binary older than store schema | open rejected; no automatic downgrade or mutation |
| `TA-M011` | malformed prior schema: missing table/column/index, invalid type or forged version row | preflight fails before mutation; original fixture retained |
| `TA-M012` | explicitly backward-incompatible fixture without approved migration | rejected and classified breaking; no best-effort conversion |

No real historical DBOS data is migrated in this slice. All migration fixtures must be synthetic.

### 3.7 Backup and Restore Tests（备份与恢复测试）

| test ID | case | expected result |
|---|---|---|
| `TA-R001` | backup quiescent database | manifest count/digest/version match |
| `TA-R002` | backup while bounded writes occur | SQLite backup API/equivalent produces consistent snapshot |
| `TA-R003` | restore valid backup to new explicit path | integrity, foreign keys, sequence, counts and digests pass |
| `TA-R004` | tampered backup bytes/manifest | restore rejected |
| `TA-R005` | truncated backup | restore rejected |
| `TA-R006` | wrong schema version backup | restore blocked pending migration decision |
| `TA-R007` | restore then retry last acknowledged admission | deterministic duplicate result; no second original |
| `TA-R008` | failed admission history after restore | failure remains present and immutable |
| `TA-R009` | page/header/index corruption variants | each detected; restore only to a new path from verified backup |
| `TA-R010` | prior compatible schema backup restored with current implementation | explicit migrate-or-block result; no silent conversion |

SQLite backup in this slice has one declared storage format only；there is no cross-format restore claim（不声称跨格式恢复）。A future production backend or export format must define its own canonical manifest, conversion and consistency suite instead of inheriting these results.

For acknowledged, committed admission records inside this single database scope, candidate target is `RPO=0`. This is not global DBOS RPO and requires direct drill evidence before it can be claimed.

## 4. Deterministic Fixture Matrix（确定性 fixture 矩阵）

Minimum fixtures（最小 fixture）：

- 3 positive signals：TRACE、METRIC、LOG；
- 3 OTel version/schema combinations：supported、unknown、unsupported；
- 5 delivery states：received、partial、retrying、dropped、unknown；
- 4 duplicate classes：confirmed、conflict、suspected、same-trace-not-duplicate；
- 11 sensitive/resource abuse cases；
- 14 storage/fault/concurrency cases；
- 12 migration cases；
- 10 backup/restore cases。

Fixture payloads必须 synthetic、无秘密、带 deterministic digest。失败 fixture 与成功 fixture 同等保留。

## 5. Reference Load and Soak Characterization（参考负载与长稳表征）

首切片不是生产服务，但必须暴露实现的基本退化行为：

| run | workload | required output |
|---|---|---|
| `TA-P001` | 10,000 unique metadata-only admissions | total time、p50/p95/p99 commit latency、DB/WAL size、CPU/memory peak |
| `TA-P002` | 10,000 confirmed retries over 1,000 originals | duplicate accuracy、growth、latency |
| `TA-P003` | 32 concurrent workers, bounded 5-minute run | lock timeout/error distribution、no corruption |
| `TA-P004` | repeated backup during bounded writes | backup latency、write impact、restore pass rate |
| `TA-P005` | 60-minute local soak with mixed success/failure | memory growth、file growth、failure retention、integrity checks |

这些数值是 characterization workload（表征负载），不是 `SLO-001` 至 `SLO-012` 的达标证明。任何 pass/fail threshold 必须在实施前由 DBOS Domain Owner 根据 reference environment 冻结，不能在看到结果后调整。

本组负载只表征 SQLite single-host reference backend（SQLite 单机参考后端），不允许形成 production database、HA、multi-tenant capacity 或 hosted service 声明。任何替换存储后端的实现必须重跑全部 `TA-C/N/D/S/F/M/R/P` 测试，不继承 SQLite 的 pass 结论。

## 6. Rollback Plan（回退计划）

### 6.1 Trigger（触发条件）

- schema/validator 产生 authority 或 Evidence elevation；
- corruption、acknowledged loss、sequence break 或 idempotency conflict overwrite；
- sensitive canary 泄漏；
- migration/restore failure；
- existing DBOS tests/validators regression；
- Critical/High unresolved finding；
- implementation exceeds DQ-018 scope。

### 6.2 Procedure（步骤）

```text
1. stop new admission calls at caller boundary
2. preserve current database, WAL, logs and failure diagnostics read-only
3. record exact source/artifact/config/version and incident reference
4. select last pre-change verified backup
5. restore to a new explicit path; never overwrite the failed store
6. run integrity/foreign-key/sequence/count/digest validation
7. compare acknowledged admission inventory
8. switch caller only after explicit Human rollback decision
9. retain failed and superseded stores per incident policy
```

Rollback 不允许删除失败历史、重写 frozen DBOS Evidence、自动降级 schema 或切换到 JSON store 后声称连续性不变。

## 7. Required Evidence Package（必需证据包）

```text
slice_id=DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION
source_commit=
artifact_hash=
python_version=
sqlite_version=
platform=
filesystem=
schema_version=
migration_checksums=
test_command=
test_count=
positive_results=
negative_results=
fault_results=
concurrency_results=
migration_results=
backup_restore_results=
load_characterization=
secret_canary_scan=
network_denial_check=
existing_dbos_tests=
existing_dbos_validators=
open_findings=
rollback_exercise_ref=
reviewed_by_ref=
result=PASS|FAIL|BLOCKED
```

## 8. Exit Gate（退出闸门）

```text
ALL_PREREGISTERED_TESTS_PASS=false
EXISTING_DBOS_REGRESSION_PASS=false
RECOVERY_VALIDATED=false
SECURITY_FINDINGS_CLOSED=false
PR_G2_READY_FOR_REVIEW=false
```

只有直接执行证据填满上述 Evidence Package 后，DBA 才能审查 `PR-G2`。本计划本身不改变这些值。
