---
spec_id: TMAI-DBOS-PRODUCTION-PERSISTENCE-ADAPTER-0.1
title: DBOS Production Persistence Adapter Specification v0.1
title_zh: DBOS 生产持久化适配器规范 v0.1
status: proposed-pending-dq-019-not-implemented
primary_repository: digital-biosphere-os
architecture_owner: digital-biosphere-architecture
implementation_authorized: false
backend_selected: false
database_created: false
data_migration_authorized: false
production_ready: false
---

# DBOS Production Persistence Adapter Specification v0.1

中文：DBOS 生产持久化适配器规范 v0.1。

## 1. Purpose（目的）

本规范定义 DBOS canonical records（规范记录）从 SQLite reference-conformance backend（参考符合性后端）进入首个可审查生产持久化实现时必须满足的 backend-neutral contract（后端中立合同）。

```text
SQLite Reference Pass != Production Persistence Pass
Database Commit != End-to-end Evidence Completeness
Replication != Backup
Backup != Restore Proof
Persistence != Activation
Persistence != Permission
```

本文件不选定产品、不创建数据库、不迁移数据，也不授权 DBOS 实施。

## 2. Reliability Domains（可靠性域）

| domain | authoritative material | allowed storage | required semantics |
|---|---|---|---|
| OTel transport buffer | Trace/Metric/Log 传输数据 | Collector memory queue、WAL、message queue | bounded loss/retry/drop visibility；不是 DBOS truth |
| Telemetry Admission | Envelope 和 append-only Admission Record | DQ-018 reference store，未来 production adapter | commit-before-ack、duplicate/partial/unknown 保留 |
| DBOS canonical records | Identity、Lifecycle、Capability、Execution、Evidence、Verification | production persistence backend | transaction、immutability、authorization、recovery、audit |
| SAEE derived records | Evaluation、Recommendation | SAEE-owned store / immutable exchange | read-only input refs、model/version provenance；无 DBOS writeback |

OTel queue/WAL 的存在不能关闭 DBOS canonical durability（规范持久性）闸门。DBOS database 的存在也不能声称 upstream telemetry 没有丢失。

### 2.1 Enforced Storage Separation（强制存储隔离）

- Collector queue/WAL/message queue 不得使用 DBOS canonical database、schema、service account 或 backup path；
- DBOS canonical writer 不得具有 Collector WAL/broker administration 权限；
- deployment validation 必须比对 DSN/endpoint、credential identity、network policy、volume mount、backup target 和 encryption key reference；
- 同一 physical disk/volume/secret 或“同库不同表”不算隔离；
- Collector 丢失或清空 queue 不能删除 DBOS history；DBOS restore 不能回放 Collector queue 并声称 end-to-end continuity；
- 必须有 negative test 故意将 Collector storage 指向 canonical DBOS target，部署验证应失败。

## 3. Deployment Tiers（部署等级）

| tier | purpose | candidate backend class | production claim |
|---|---|---|---|
| `P0_REFERENCE` | schema、事务、幂等、迁移和恢复符合性 | SQLite single-host | prohibited |
| `P1_STAGING` | production adapter integration、load/fault rehearsal | single-node relational database with WAL/PITR | prohibited |
| `P2_SINGLE_REGION_PRODUCTION_CANDIDATE` | 首个 self-hosted single-tenant 生产候选 | PostgreSQL-compatible primary + synchronous standby/quorum candidate | only after `PR-G2/G5/G6/G7` |
| `P3_MULTI_REGION` | 跨区域、更高可用或联邦 | not selected | out of v0.1 scope |

`P2` 中的 PostgreSQL-compatible 只是进入 `DQ-019` 的 reference candidate（参考候选），不是已采纳选型。具体 distribution、version、hosting、replication 和 backup system 必须另行决策并锁定 exact artifact digest。

## 4. Storage Port Contract（存储端口合同）

实现不得向 domain layer 暴露 vendor SQL 或用“换数据库”改变对象语义。最小能力：

```text
append_object_version(object_kind, object_id, version, payload_digest, payload_ref, provenance)
append_state_transition(subject_ref, expected_previous_ref, transition, authorization_ref)
bind_idempotency(scope, key_digest, request_digest, committed_result_ref)
read_current(subject_ref, consistency_requirement)
read_history(subject_ref, cursor, limit)
commit_atomic(unit_of_work)
verify_integrity(scope, checkpoint_ref)
create_backup(checkpoint_ref)
restore_to_new_target(backup_ref)
```

本合同是 architecture method inventory（架构方法清单），不是 API 或 endpoint。

## 5. Transaction and Ordering Invariants（事务与顺序不变量）

1. acknowledgement 只能在 authoritative transaction commit 后返回；
2. state transition 必须校验 expected previous record，防止 lost update；
3. 同一 object lifecycle 使用 monotonic version/sequence，不使用 wall clock 作为唯一顺序；
4. canonical history 只追加；更正、撤销和 supersession 使用新 record；
5. authorization check 和状态写入必须属于同一 consistency boundary，不允许 time-of-check/time-of-use 空隙；
6. outbox/event publication 如存在，必须与 canonical write 同事务记录，消费者保持幂等；
7. cross-object unit of work 不得拆成多个“各自成功”的 JSON/file writes；
8. transaction retry 必须区分 serialization conflict、deadlock、timeout、permanent validation failure 和 unknown commit outcome。

## 6. Idempotency and Unknown Commit（幂等与未知提交）

| condition | required result |
|---|---|
| same scoped key + same request digest + committed result | return/reference original result；append retry observation if required |
| same scoped key + different request digest | conflict；never overwrite |
| connection lost before commit outcome known | query committed binding before retry；state remains `UNKNOWN` until resolved |
| caller lacks stable key | operation cannot claim exactly-once；use explicit at-least-once + duplicate handling |

`Exactly once` 不是全局声明。最多可声明“在 exact database transaction + idempotency scope 内的 single committed result”，网络、Collector、SAEE 和外部系统仍需独立语义。

## 7. Durability, HA and Recovery（持久性、高可用与恢复）

`P2` 候选必须直接证明：

- committed WAL 在声明 failure domain 内的 synchronous replication policy；
- replica lag、quorum loss、read-only/degraded mode 可观测；
- 自动 failover 不产生 split brain，旧 primary 被 fencing；
- periodic full backup + continuous WAL/PITR（时点恢复）；
- backup encryption、key separation、retention、immutability 和 restore inventory；
- restore 到 new target，不覆盖故障库；
- exact object count、foreign key、sequence、digest、authorization chain 和 acknowledged inventory 验证；
- declared `RPO=0` 只在 acknowledged canonical records + tested failure domain 内有效；
- `RTO<=30m` 需要 timed drill，不能由 replication 配置推断。

## 8. Schema and Migration Governance（模式与迁移治理）

1. 每个 migration 有 monotonic ID、digest、owner、compatibility class 和 rollback/restore plan；
2. expand→backfill→dual-read verification→contract 是不可停机迁移的候选步骤，不允许一步破坏；
3. application N/N-1 兼容窗口必须预先声明和测试；
4. unknown newer schema 失败关闭，不自动 downgrade；
5. backfill 必须可恢复、可限速、可观测，并保留 source digest；
6. destructive migration 要求独立 Human Decision、已验证 backup 和可执行 rollback；
7. telemetry/observability backend 的 schema 不得成为 DBOS canonical schema authority。

## 9. Security and Access（安全与访问）

- service identity + mutually authenticated transport，不使用共享超级账号；
- writer/read-only/migration/backup/restore 角色分离；
- migration 账号不在正常 Runtime 中长期存在；
- secrets 来自受管注入，不进入 repo、logs、OTel attributes 或 backup manifest；
- row/field redaction 不代替数据分类和最小化；
- audit record 不允许 writer 删除自己的失败历史；
- database、backup、WAL archive、monitoring 和 key store 的访问边界分开审计。

## 10. OpenTelemetry Self-observation（OpenTelemetry 自观测）

Persistence adapter 必须输出 bounded OTel metrics/traces（有界 OTel 指标/追踪），但这些信号不得回流成 canonical Evidence：

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

Attributes 只允许 operation class、outcome、backend profile/version、consistency mode 和 bounded error class。禁止 object ID、entity ID、payload、SQL、secret、path 和任意用户值。

## 11. Required Conformance and Failure Matrix（必需符合性与故障矩阵）

| group | minimum proof |
|---|---|
| transaction | atomic multi-object unit、lost-update conflict、deadlock/serialization retry、unknown commit resolution |
| idempotency | same/same、same/different、concurrent retry、scope isolation |
| append-only | no update/delete surface、supersession、failure retention |
| replication | primary loss、standby loss、quorum loss、fencing、replica lag |
| backup/PITR | full backup、WAL replay、point-in-time restore、tamper、wrong key、expired retention |
| migration | N/N-1、interruption、backfill resume、newer schema、breaking change reject |
| capacity | steady load、burst、large history、index growth、connection exhaustion |
| security | role separation、secret canary、TLS/auth failure、audit immutability、dependency/SBOM |
| OTel storage isolation | Collector DSN/volume/secret/key/network 与 canonical DBOS store 强制分离；cross-wiring negative test |

所有测试必须记录 exact database/distribution version、configuration digest、node topology、failure domain、workload、seed、commands 和 results。

## 12. Decision Inputs for DQ-019（DQ-019 决策输入）

`DQ-019` 必须比较至少：

1. self-managed PostgreSQL-compatible HA；
2. managed PostgreSQL-compatible service（若允许外部云资源）；
3. 保持 SQLite/reference only 并不进入 production；
4. 任何 distributed SQL 候选（仅在有明确 multi-region requirement 时）。

评审维度：consistency、failure domain、RPO/RTO、operations burden、backup/PITR、migration、security、cost、license、vendor portability 和 agent-readable operability。

## 13. Exit Gate（退出闸门）

```text
PRODUCTION_PERSISTENCE_SPECIFICATION_DEFINED=true
PRODUCTION_BACKEND_SELECTED=false
PRODUCTION_ADAPTER_IMPLEMENTED=false
PRODUCTION_MIGRATION_EXECUTED=false
HA_VALIDATED=false
RPO_RTO_VALIDATED=false
PR_G2_PERSISTENCE_PASS=false
PR_G5_RECOVERY_PASS=false
PRODUCTION_READY=false
```
