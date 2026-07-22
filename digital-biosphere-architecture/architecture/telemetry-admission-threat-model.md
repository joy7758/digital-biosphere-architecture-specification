---
document_id: TMAI-DBOS-TELEMETRY-ADMISSION-THREAT-MODEL-0.1
title: DBOS Telemetry Admission Foundation Threat Model v0.1
title_zh: DBOS 遥测准入基础威胁模型 v0.1
status: proposed-preimplementation-threat-model
scope: DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION
decision_reference: DQ-018
implementation_authorized: false
security_review_complete: false
production_ready: false
---

# DBOS Telemetry Admission Foundation Threat Model v0.1

中文：DBOS 遥测准入基础威胁模型 v0.1。

## 1. Scope and Method（范围与方法）

本文件对 proposed（拟议的）离线／本地 Telemetry Admission Foundation 做 architecture-level threat analysis（架构级威胁分析）。它使用 spoofing、tampering、repudiation、information disclosure、denial of service、elevation of privilege 等类别组织问题，但不声称完成独立安全审计、渗透测试或合规认证。

首切片没有网络 listener、Collector、raw telemetry store、Agent 或 Permission。因此本威胁模型覆盖：untrusted normalized envelope（不可信规范化封装）进入 validator、transactional store、backup/restore 和 self-observation 的路径。

## 2. Assets（保护资产）

| asset | required property |
|---|---|
| Admission history | append-only、可追溯、不静默删除 |
| Source/provenance metadata | 不被伪造为认证 Identity 或 Truth |
| State transition | 有序、唯一、失败关闭 |
| Idempotency binding | 不被冲突重用或静默覆盖 |
| Store and backup | integrity、least privilege、可恢复 |
| Sensitive-data boundary | raw content、credentials、PII 不进入 store/log/metrics |
| Authority boundary | admission 不生成 Evidence、Permission、Fitness 或 Decision |
| Availability boundary | resource exhaustion 可见且不会伪造成功 |

## 3. Trust Boundaries（信任边界）

```text
Untrusted source / future OTLP adapter
  ↓ TB-1: normalized envelope boundary
Closed-schema validator
  ↓ TB-2: policy and duplicate classification
Admission transaction
  ↓ TB-3: SQLite file / WAL / lock / filesystem
Backup and restore
  ↓ TB-4: restored store validation
Read-only consumers / future Evidence admission
```

- `TB-1` 之前的一切字段均为 untrusted declaration（不可信声明）；
- `TB-2` 通过只表示策略接纳，不建立真实性；
- `TB-3` 的 commit acknowledgement 是本地事务事实，不是 end-to-end OTLP acknowledgement；
- `TB-4` 后仍需 Evidence admission 才能进入 canonical Evidence。

## 4. Threat Actors（威胁来源）

- malformed or malicious producer（恶意／错误生产者）；
- compromised instrumentation or Collector（受控插桩／收集器）；
- buggy future transport adapter（有缺陷的未来适配器）；
- local user with excessive filesystem access（本地越权用户）；
- concurrent process causing race/lock pressure（并发进程）；
- operator mistake during migration/restore（运维误操作）；
- dependency or build compromise（依赖／构建链污染）；
- accidental sensitive-data emission（意外敏感数据发射）。

Human Reviewer、DBOS component 或 signed artifact 也不能被假设永远可信；所有可验证边界仍需直接证据。

## 5. Threat Register（威胁台账）

| ID | severity | threat | required control | required proof |
|---|---|---|---|---|
| `TA-T01` | `CRITICAL` | telemetry attribute 被冒充为 DBOS Identity、Authorization 或 Permission | schema 禁止 authority fields；Resource/Context 与 Identity 分离 | negative tests for `entity_id`、permission、authorization injection |
| `TA-T02` | `CRITICAL` | `ACCEPTED_AS_MATERIAL` 被直接升级为 Evidence/Truth | 独立 object kind/state；无 Evidence write path；输出无 Evidence ID | source scan + negative tests + API surface inventory |
| `TA-T03` | `HIGH` | producer/source reference spoofing | 所有 source 字段标记 declared；digest 不等于 signature；未来认证另行绑定 | unbound source remains limitation; no authenticity claim |
| `TA-T04` | `HIGH` | forged/malformed `traceparent` 建立虚假因果链 | strict syntax validation；无 parent 时不猜测；Context 只相关 | invalid/all-zero/wrong-length/flag tests |
| `TA-T05` | `HIGH` | replay、producer 伪造 DBOS receipt 或重试产生双重 Evidence 候选 | confirmed 只由已 commit admission row + DBOS-issued receipt + same digest 查询形成；external key 仅 suspected；冲突拒绝 | fabricated/uncommitted receipt, concurrent replay and same-receipt/different-digest tests |
| `TA-T06` | `HIGH` | fingerprint 误杀合法相同观测 | 无可信 idempotency 时只标 `DUPLICATE_SUSPECTED`，不得删除 | two legitimate identical-content cases retained |
| `TA-T07` | `CRITICAL` | prompt、tool arguments/results、token、credential、PII 或 dynamic metadata 进入 store/log/metrics | closed input schema、exact persistence allowlist、opaque bounded references、prohibited-key defense-in-depth、bounded errors | dynamic-field and seeded secret/PII canary tests across output/store/backup/exception/log/metrics/test artifacts |
| `TA-T08` | `HIGH` | schema URL 触发 SSRF 或供应链漂移 | runtime network fetch 禁止；exact allowlist/pin；unknown fail closed | monkeypatch/socket audit + unknown URL tests |
| `TA-T09` | `HIGH` | GenAI development semconv 自动漂移 | exact version/commit、isolated mapping、default disabled | unpinned/latest/deprecated attribute tests |
| `TA-T10` | `HIGH` | partial success、drop、sampling 被隐藏成完整 | explicit delivery/sampling/limitations + accepted/rejected counts | partial/drop/sampled-out fixtures and result checks |
| `TA-T11` | `HIGH` | oversized/deep/high-cardinality input 导致 memory/CPU/disk exhaustion | pre-parse/body size boundary at adapter、post-parse depth/count/length limits | size/depth/count/budget adversarial tests |
| `TA-T12` | `HIGH` | decompression bomb / malformed protobuf | 不在本切片解压／解码；未来 adapter 必须在解压前后限额 | absence audit now; future gate required |
| `TA-T13` | `CRITICAL` | transaction commit 中断却返回成功 | acknowledge-after-commit；atomic transaction；fault injection | injected failures before/during/after commit |
| `TA-T14` | `CRITICAL` | disk full/page-WAL corruption 导致 acknowledged record 丢失 | fail closed、integrity checks、backup/restore to new path、no automatic repair | disk-full, separate-process crash, corrupt page/header/WAL, restore drill |
| `TA-T15` | `HIGH` | concurrent writers 绕过 single-use idempotency | unique constraints + `BEGIN IMMEDIATE`/equivalent + bounded lock timeout | multi-process/thread race tests |
| `TA-T16` | `HIGH` | migration 部分应用或 checksum 被替换 | immutable migration checksum、single transaction、pre-backup、post-validation | tampered migration and interruption tests |
| `TA-T17` | `HIGH` | backup 是不一致文件副本、被替换或跨版本静默转换 | SQLite backup API/equivalent、manifest digest、permissions、cross-version migrate-or-block、restore validation | live-write backup, tamper, prior-compatible-version and restore tests |
| `TA-T18` | `HIGH` | error/detail 或 metrics label 泄漏 payload／造成高基数 | stable reason codes、bounded details、allowlisted low-cardinality labels | canary and cardinality tests |
| `TA-T19` | `MEDIUM` | time skew/rollback 伪造顺序 | sequence is canonical ordering；timestamps carry clock source/limitation | backward/equal/future timestamp tests |
| `TA-T20` | `HIGH` | local DB/backup world-readable or path traversal | explicit resolved path、owner permissions、symlink/parent checks | permission and symlink/path traversal tests |
| `TA-T21` | `HIGH` | self-observation failure changes admission result or hides outage | metrics side channel cannot commit state；diagnostic on failure | metric exporter failure injection |
| `TA-T22` | `HIGH` | dependency/build artifact compromised | lockfile/SBOM/hash/scan/reproducible package gate | dependency inventory, artifact hash, security scan |
| `TA-T23` | `CRITICAL` | rollback deletes failed or post-baseline history | rollback disables code, not history；restore preserves superseded ledger separately | rollback exercise + before/after record inventory |
| `TA-T24` | `HIGH` | implementation silently creates network listener or external side effect | no socket/server dependency/surface；network denied in tests | source/import scan and denied-network test |

## 6. Security Invariants（安全不变量）

```text
RAW_TELEMETRY_PERSISTED=false
CONTENT_CAPTURE_DEFAULT=DISABLED
PERSISTENCE_FIELD_ALLOWLIST_REQUIRED=true
PRODUCER_CAN_SELF_ATTEST_DBOS_RECEIPT=false
RUNTIME_SCHEMA_FETCH=false
TRACE_CONTEXT_IS_AUTHORITY=false
DIGEST_IS_SIGNATURE=false
ADMISSION_IS_EVIDENCE=false
ADMISSION_IS_PERMISSION=false
SAEE_CALLED=false
NETWORK_LISTENER_CREATED=false
ACK_BEFORE_COMMIT=false
FAILED_HISTORY_DELETED=false
```

## 7. Security Stop Conditions（安全停止条件）

出现以下任一情况，实施 review 必须 `FAIL` 或 `BLOCKED`：

- 任一路径可由 input 生成 Identity、Authorization、Permission、Evidence、Verification、Fitness 或 Decision；
- raw content、secret canary 或任意 prohibited key 出现在 store、exception、log、metric 或 test artifact；
- acknowledged record 在 crash/restore 范围内丢失或顺序断裂；
- same idempotency key + different digest 被覆盖或接受；
- `DUPLICATE_SUSPECTED` 被静默删除；
- unsupported schema/semconv 被静默降级；
- schema URL 触发网络访问；
- migration/rollback 改写历史；
- Critical/High finding 未修复且没有独立、限时、明确范围的 Human Risk Acceptance；
- DBOS/SAEE 冻结或既有 Evidence 被修改。

## 8. Residual Risk（残余风险）

即便本威胁模型和首切片测试全部通过，仍保留：

- 无真实 OTLP decoder/listener 的 transport risk；
- 无 Collector deployment 的 pipeline/configuration risk；
- 无 external identity/authentication binding；
- SQLite single-host availability 和 filesystem risk；
- SQLite 只是 reference conformance backend，未选定 production persistence backend；
- 无 multi-tenant isolation；
- 无 canonical Evidence admission 和 Verification；
- 无真实容量、staging soak、RTO/RPO 和 production pilot evidence。

这些风险分别留在 `PR-G3`、`PR-G5` 和 `PR-G6`，不能由本切片关闭。

## 9. Current State（当前状态）

```text
THREAT_MODEL_DEFINED=true
INDEPENDENT_SECURITY_REVIEW_COMPLETE=false
SECURITY_TESTS_EXECUTED=false
CRITICAL_HIGH_FINDINGS_CLOSED=false
IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```
