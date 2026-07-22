---
spec_id: TMAI-PRODUCTION-PERSISTENCE-CANDIDATE-DUE-DILIGENCE-0.1
title: Production Persistence Candidate Due Diligence Contract v0.1
title_zh: 生产持久化候选尽职调查契约 v0.1
status: defined-machine-profile-not-assessed-no-backend-selected
decision_reference: DQ-019
primary_repository: digital-biosphere-architecture
backend_selected: false
implementation_authorized: false
cloud_resource_created: false
production_ready: false
---

# Production Persistence Candidate Due Diligence Contract v0.1

中文：生产持久化候选尽职调查契约 v0.1。

## 1. Purpose（目的）

本契约把 DQ-019 的候选比较转换为 strict machine profile（严格机器画像），使编码、检索、审查
智能体能区分：官方资料、候选声明、直接测试、Human Decision 和实际部署。

```text
Official feature documentation != Exact candidate profile
Provider SLA != DBOS measured SLO
Schema valid != Due diligence pass
Candidate eligible != Backend selected
Backend selected != Resource creation or deployment authorization
```

对应机器文件：

- [`production-persistence-candidate-profiles.v0.1.json`](production-persistence-candidate-profiles.v0.1.json)；
- [`schemas/production-persistence-candidate-profiles.schema.v0.1.json`](schemas/production-persistence-candidate-profiles.schema.v0.1.json)。

本契约不实施数据库、不调用供应商 API、不创建云资源，也不改变 DBOS/SAEE。

## 2. Candidate Evidence Layers（候选证据层）

| layer | meaning | can close DQ-019 gate? |
|---|---|---|
| `OFFICIAL_UPSTREAM_REFERENCE` | PostgreSQL/OpenTelemetry 官方语义与能力 | no；只能定义可验证要求 |
| `PROVIDER_OFFICIAL_CLAIM` | 供应商产品、SLA、备份、API 文档 | no；必须绑定 exact region/version/SKU/terms |
| `EXACT_CANDIDATE_PROFILE` | exact product/version/topology/config/digest/Owner | partial；仍需直接测试 |
| `DIRECT_CONTROLLED_RECEIPT` | failover、unknown commit、PITR、restore、security、load 直接回执 | yes，限精确环境和 failure domain |
| `INDEPENDENT_REVIEW` | 技术、安全、成本和恢复审查 | yes，作为 Human Decision 输入 |
| `HUMAN_DECISION` | DQ-019 exact token | selects/authorizes only within stated effect |
| `DEPLOYMENT_OBSERVATION` | 未来 staging/production 运行观察 | production gate only；不能倒推决策授权 |

任何上层不得用下层缺失值自动补齐。`null`、`BLOCKED`、`NOT_ASSESSED` 必须保持失败关闭。

## 3. Exact Profile Requirements（精确画像要求）

每个 `P2` 候选至少绑定：

1. distribution/product、engine version、provider、region、SKU；
2. topology、failure domains、node/quorum、connection endpoint class；
3. immutable configuration、artifact/image/package、terms、pricing snapshot digest；
4. transaction isolation、commit-before-ack、unknown commit、idempotency、append-only enforcement；
5. synchronous replication policy、degraded behavior、failover、fencing/split-brain control；
6. base/full backup、continuous WAL/PITR、retention/immutability、new-target restore；
7. TLS/workload identity、writer/reader/migration/backup/restore roles、key/secret/network/storage separation；
8. migration N/N-1、rollback、capacity、connection exhaustion 和 SLO measurement；
9. accountable Owner、on-call、runbook、rollback、cost cap 和 license/portability review；
10. exact source commit/environment/workload/command/result/digest 的直接证据。

## 4. Gate Status Contract（闸门状态合同）

候选每个 gate 只能使用：

| status | meaning |
|---|---|
| `NOT_ASSESSED` | 尚未收集可审查输入 |
| `PARTIAL_REFERENCE_ONLY` | 只有 upstream/provider 文档；无 exact/direct proof |
| `BLOCKED` | 存在明确缺口，禁止继续推断 |
| `PASS_DIRECT` | exact profile + direct controlled receipt + reviewer binding 通过 |
| `FAIL` | 直接证据不满足要求 |
| `NOT_APPLICABLE` | 有书面理由且不削弱 P2 必需控制 |

`READY_FOR_DECISION_REVIEW` 只能在所有 P2 required gate 为 `PASS_DIRECT`、unresolved inputs 为空、
exact profile 不含 `null`，并经独立技术/安全审查后出现。Schema valid 本身不能生成该状态。

## 5. OpenTelemetry Database Semantics（OpenTelemetry 数据库语义）

本画像继承已采纳的 Semantic Conventions `v1.43.0`，但严格分开标准数据库 client telemetry 与
TMAI canonical semantic operation（规范语义操作）：

| observation | authority / stability | TMAI rule |
|---|---|---|
| database client span | OTel database span, Stable | 覆盖调用方观察到的逻辑数据库调用和内部 retry；不能证明 canonical commit |
| `db.client.operation.duration` | OTel database client metric, Stable | 记录数据库 client operation；单位 `s`；不得替代 TMAI commit/outcome accounting |
| `db.system.name` | OTel attribute, Stable | exact PostgreSQL 使用 `postgresql`；不作为 backend selection 决策 |
| `db.operation.name` | OTel attribute, Stable | 只允许低基数命令类别 allowlist，不允许任意 SQL |
| `error.type` | OTel attribute, Stable | 只允许 bounded error class；不得输出原始异常、DSN、path 或用户数据 |
| `db.query.text` | OTel attribute, Opt-In | TMAI v0.1 强制禁用，即使已净化也不能默认采集 |
| `db.query.summary` | OTel attribute, Stable/Recommended | 默认禁用；安全/基数审查和 Human Data Decision 后才可单独启用 |
| connection-pool metrics | OTel database metrics, Development | 不进入 v0.1 stable baseline；若观察必须单独 pin exact source/version |

TMAI 自定义指标继续描述 DBOS canonical operation semantics，不冒充标准 OTel 指标：

```text
tmai.dbos.persistence.operations
tmai.dbos.persistence.duration
tmai.dbos.persistence.conflicts
tmai.dbos.persistence.unknown_commit_outcomes
tmai.dbos.persistence.replication_lag
tmai.dbos.persistence.backup_age
tmai.dbos.persistence.restore_verification_failures
tmai.dbos.persistence.migration_state
```

两类指标必须使用不同 Instrumentation Scope，具有书面 aggregation/correlation rule，禁止双计数。
标准 DB client success 不能自动产生 TMAI canonical success；TMAI success 只来自 commit/outcome contract。

## 6. Sensitive and Cardinality Boundary（敏感与基数边界）

禁止进入 span/metric/log/event attribute：

- SQL/query text、query parameter、statement plan；
- database/namespace/table/schema name；
- object/entity/execution/evidence/authorization ID；
- DSN、hostname/IP、port、filesystem/backup path；
- credential、certificate、key、token、secret reference；
- payload、prompt、tool input/output 或任意用户值。

允许的默认 attributes 只有：bounded operation class、bounded outcome、`db.system.name`、backend profile
version、consistency mode、bounded error class、deployment environment class。任何新增 attribute 必须先做
cardinality/privacy/data-authority review。

## 7. Provider Due Diligence（供应商尽调）

Managed candidate 必须把 provider claim 和 direct proof 分开记录。至少确认：

- SLA 是否适用于目标 PostgreSQL 双机高可用 region/SKU；排除项与赔偿不是 DBOS SLO proof；
- exact PostgreSQL version、minor upgrade policy、extension/parameter/connection restrictions；
- commit acknowledgement 与主备同步／退化行为；不能从“实时同步”四字推断 `RPO=0`；
- 自动/手动 failover、可靠性优先／可用性优先、旧主 fencing 和连接恢复；
- backup/PITR 的目标版本/SKU 支持、保留、加密、下载、跨账号/新实例恢复和 API；
- region/AZ、data residency、network/private access、TLS、IAM/role、audit、key ownership；
- API/SDK 能否输出 immutable、agent-readable operation/restore receipts；
- storage/IO/backup/egress/API/support/operations 的月度成本上限；
- export/migration/exit plan 和 vendor portability。

官方文档发生矛盾或跨时间更新时，状态必须为 `BLOCKED`，直至目标产品的当前书面说明与直接测试
一致，不能选取对候选最有利的页面自动合并。

## 8. Required Direct Drills（必需直接演练）

| group | minimum receipt |
|---|---|
| transaction | serialization/deadlock retry、lost update、atomic unit、unknown commit resolution |
| HA | primary/standby/quorum/network loss、degraded behavior、automatic/manual failover、fencing |
| backup/PITR | base/full backup、continuous WAL、tamper/wrong-key/retention negative、point-in-time new-target restore |
| continuity | acknowledged inventory、count、sequence、digest、authorization chain、foreign-key integrity |
| migration | N/N-1、interruption/resume、newer-schema reject、rollback/restore |
| security | role cross-use deny、secret/SQL/path canary、TLS/certificate rotation/revocation、audit append-only |
| capacity | steady/burst/2x/5x、connection exhaustion、replication lag、first refusal point |
| OTel | standard/custom scope separation、bounded attributes、no double count、no query/identifier leakage |

每个 receipt 必须绑定 exact candidate profile digest。换 region/version/SKU/topology/config 后不得复用旧 PASS。

## 9. Decision and Execution Boundary（决策与执行边界）

```text
DQ_019_CANDIDATE_PROFILE_SCHEMA_DEFINED=true
DQ_019_CANDIDATES_ASSESSED=false
DQ_019_BACKEND_SELECTED=false
DQ_019_IMPLEMENTATION_AUTHORIZED=false
CLOUD_RESOURCE_CREATED=false
DATABASE_CREATED=false
PRODUCTION_READY=false
```
