---
spec_id: TMAI-PRODUCTION-IMPLEMENTATION-SEQUENCE-0.1
title: TMAI Staged Production Implementation Sequence v0.1
title_zh: TMAI 分阶段生产实施序列 v0.1
status: proposed-sequence-no-implementation-authority
architecture_owner: digital-biosphere-architecture
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# TMAI Staged Production Implementation Sequence v0.1

中文：TMAI 分阶段生产实施序列 v0.1。

## 1. Sequence Principle（序列原则）

```text
Contract before transport
Admission before Evidence promotion
Reference conformance before production persistence
Production persistence before production claim
Observation before evaluation
Evaluation before recommendation
Recommendation before decision
Decision before authorized execution
Security/recovery before pilot
Pilot before production authorization
```

每一阶段的 pass 只允许进入下一个人工审查，不能跨级变成生产声明。

### 1.1 Two Different Freezes（两种不同冻结）

```text
S0 Architecture Contract Freeze
  = immutable DBA rules + decision packet + external reference decision + schema/profile selection criteria
  != Collector/database/runtime artifact selection

S2/S3 Deployment Profile Freeze
  = exact database/Collector distribution + version + image/component/config/SBOM/topology
  requires DQ-019/DQ-020 and direct implementation/deployment evidence
```

S0 不要求、也不允许提前创建或选择 Collector configuration。相反，`NOT_SELECTED/NOT_CREATED` 是 S0 的诚实状态；只有到 S2/S3 才能冻结 exact deployment profile。Architecture Contract Freeze 不能关闭 `PR-G2/PR-G3`，Deployment Profile Freeze 也不能反向修改已冻结架构规则。

## 2. Critical Path（关键路径）

| step | decision/gate | primary repo | exact deliverable | stop condition |
|---|---|---|---|---|
| `S0` | current DBA baseline | DBA | TMAP、OTel Profile、SLO、PR-G1 mapping、DQ-018 packet、`DQ-022` OTLP、`DQ-023` semantic、`DQ-024` Schema/Resource/Entity 与 `DQ-025` Collector distribution 四个独立 external reference decision records | 任一所需 version/sequence decision 未记录或 baseline 未 commit/push |
| `S1` | `DQ-018` → `PR-G2A` | DBOS | pinned offline OTLP decoder selected subset + Telemetry Admission Foundation + SQLite reference-conformance backend；无 listener | authority/evidence elevation、fault/recovery failure、decoder 访问网络 |
| `S2` | `DQ-019` → `PR-G2B/PR-G5A` | DBOS + deployment infra | selected production persistence adapter/backend + migration/recovery evidence | backend unselected、RPO/RTO/HA 无直接证据 |
| `S2.5` | `PR-G2T` | DBOS + deployment infra | DQ-018 admission 迁移到 production staging backend；Collector storage/canonical store 隔离和 unknown-commit/retry 集成 | store cross-wiring、migration/recovery/lineage 不一致 |
| `S3A` | `DQ-025` + `DQ-020` → `PR-G3A-C` | deployment infra + DBOS adapter | adopted exact custom-minimal inventory 的 reproducible build、SBOM/provenance/signature/vulnerability proof；[`opentelemetry-collector-deployment-profile.v0.1.json`](opentelemetry-collector-deployment-profile.v0.1.json) 与 [`opentelemetry-collector-operational-evidence-profile.v0.1.json`](opentelemetry-collector-operational-evidence-profile.v0.1.json) 的 exact digests；仅 synthetic fixtures 的 pinned authenticated loopback OTLP listener；gRPC/HTTP size、partial/retry/RetryInfo/`Retry-After`、authn/authz 与 Collector distribution 48-case conformance | source/build/config/OTLP 语义或限制丢失，未授权网络面、出现 Evidence 写入，或任一 profile 中 required exact value 仍为 `null` |
| `S3B` | `PR-G3D-F` | deployment infra + DBOS adapter | 经人类授权的 immutable versioned configuration（不可变版本化配置）canary rollout/rollback；>=2 gateway Collector staging → queue/WAL/failure/delivery reconciliation；复验 exact inventory/config/runtime、metric naming/stability/query/alert/route/runbook bindings、独立 self-observation/blackbox/storage/drift、no-data/alert-delivery drills、composite readiness truth table 与 48/48 distribution result | HA/security/version/queue/single-writer/drift、self-telemetry/no-data/alert delivery、readiness predicate 或 distribution reconciliation 未通过 |
| `S4` | `DQ-021` → `PR-G2C/PR-G5B` | DBOS | Telemetry-to-Evidence admission + independent Verification | Telemetry 直接成 Evidence/Truth |
| `S5` | future SAEE decision → `PR-G4` | SAEE | read-only production adapter、timeout/version/conflict/resource isolation、zero writeback | SAEE 获得 Decision/DBOS write authority |
| `S6` | `PR-G5` | DBOS + deployment + DBA review | independent security review、supply chain、DR、rollback、capacity/soak | Critical/High open，restore/rollback fail |
| `S7` | explicit Pilot Authorization → `PR-G6` | deployment-specific | 7-day staging + 30-day bounded observation + failure drills | scope/owner/rollback/SLO 不完整 |
| `S8` | Human Production Decision → `PR-G7` | DBA governance | exact artifact/environment/workload/risk/runbook authorization | any gate not scoped PASS |
| `S9` | separate Deployment Authorization | deployment-specific | canary deployment、continuous observation、incident/rollback ownership | production Decision 缺失/撤销 |

## 3. Why the Order Is Mandatory（为什么顺序不可跳过）

### `S1` before `S3`

先打开 OTLP listener 会让未受控外部数据进入系统，而当前尚无准入状态、去重、隐私和失败保留基础。因此 reference admission 先于 transport。

`S1` 只执行 [`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json) 的 `OTLP-CG-SIGNAL_SCHEMA` 和 `OTLP-CG-AUTHORITY_BOUNDARY`，使用 offline synthetic fixtures。只有 `DQ-023`/`DQ-024` 分别作出人工决定且 DQ-018 明确授权对应实现范围时，S1 才可追加 offline semantic 与 Schema/Resource/Entity cases；`DQ-024` 本身不授权执行。`S3A/S3B` 才执行 gRPC/HTTP size、retry/partial、deployment security/capacity、真实 acquisition/network 与 delivery reconciliation groups。两阶段不得分别创建不同 decoder、schema translator 或 signal semantics；S3 必须复用 S1 已验证的 exact contracts。

### `S2` before production traffic

SQLite 只能证明单机合同，不能承担 production HA/PITR/RPO/RTO。任何真实长期数据前必须先通过 production persistence gate。

### `S2.5/S3A/S3B` before `S4`, but transport success never implies Evidence

Evidence admission 需要真实 delivery/partial/drop/retry/provenance 材料，但它必须是独立决策和实现。OTLP success 不能绕过 `S4`。

### `S4` before SAEE production evaluation

SAEE 不能用 raw telemetry 或 Collector health 自行补齐 Evidence。生产 Adapter 必须消费已准入对象和明示 limitations。

## 4. Repository and Authority Routing（仓库与权力路由）

| artifact | repository | authority needed |
|---|---|---|
| architecture contracts / ADR / gate records | DBA | Architecture Governance + Human decisions where required |
| DBOS admission/persistence/evidence code | DBOS | exact DBOS implementation authorization |
| Collector config/manifests/runbooks | dedicated deployment infrastructure repository | deployment owner + security/operations review |
| SAEE adapter/evaluation isolation | SAEE | exact SAEE implementation authorization |
| pilot workload/instrumentation | Digital Entity/application repository | entity capability + pilot authorization |

DBA 不能为了减少仓库数量而收容 Runtime、Collector config secret 或运行数据。

## 5. Decision Queue Projection（决策队列投影）

| decision | question | current state | prerequisite |
|---|---|---|---|
| `DQ-022` | 是否采纳 official OTLP `v1.11.0@790608c...` 为 architecture reference？ | `DECIDED_REFERENCE_ADOPTED` | Runtime compatibility 仍需直接测试 |
| `DQ-023` | 是否采纳 core/GenAI semantic mapping 与 46-case contract？ | `DECIDED_REFERENCE_ADOPTED` | DQ-018 authorized subset 32/32 PASS；deployment subset blocked |
| `DQ-024` | 是否采纳 Schema/Resource/Entity provenance profile 与 45-case contract？ | `DECIDED_REFERENCE_AND_QUARANTINE_ADOPTED` | DQ-018 authorized subset 36/36 PASS；deployment subset blocked |
| `DQ-025` | 是否采纳 Collector `v0.156.0` custom-minimal 8-component/2-provider inventory 与 48-case contract？ | `DECIDED_REFERENCE_INVENTORY_ADOPTED` | 不授权 build/config/deployment |
| `DQ-018` | 是否实施 reference Telemetry Admission Foundation？ | `IMPLEMENTED_PR_G2A_REVIEW_READY_NOT_APPROVED` | source `5c52c1c…`、receipt `aa6440e…`、manifest `fdda745c…` |
| `DQ-019` | 选择哪个 production persistence backend/profile，是否授权 adapter 实施？ | `BLOCKED_INPUT` | PR-G2A Human Review approval + candidate exact inputs |
| `DQ-020` | 是否允许 authenticated OTLP/Collector staging？ | `BLOCKED_INPUT` | DQ-018 + DQ-019 + DQ-022/023/024/025 + deployment profile/schema/readiness matrix + exact owner/repository/build/config/topology/security/capacity/readiness/direct evidence；当前只定义 profile，不创建配置或部署 |
| `DQ-021` | 是否实施 Telemetry-to-Evidence admission？ | `BLOCKED_INPUT` | DQ-018 + exact Evidence policy/object mapping + security review |

未来 SAEE、Pilot 和 Production Decision ID 在所需输入齐备后再分配，避免决策队列伪装成 roadmap completion。

## 6. Operational Role Matrix（运维角色矩阵）

| role | accountable for | cannot unilaterally do |
|---|---|---|
| Human Program Owner | cross-stage priority and decision source | operate DBOS/Collector/database without domain authorization |
| DBOS Service Owner | admission、canonical store、Evidence/Verification service correctness | change Architecture rules or SAEE model |
| Database Owner | HA、backup/PITR、restore、migration operations | change canonical object meaning or grant Permission |
| Collector Platform Owner | Collector distribution/config、capacity、queue/WAL、upgrade | promote telemetry to Evidence or create Identity |
| Security Reviewer | threat model、identity/TLS/secrets/supply chain findings | silently accept Critical/High risk |
| Data Steward / Privacy Reviewer | classification、purpose、retention、residency、access | certify technical integrity as legal compliance |
| SAEE Domain Owner | evaluation model、read-only adapter、failure isolation | write DBOS facts or execute recommendation |
| Incident Commander | time-bounded incident coordination and rollback decision routing | rewrite/delete history or permanently alter policy without review |
| Human Production Authority | exact deployment production decision | treat decision as deployment execution |

每个角色在 staging 前必须有 named human/service reference、on-call/escalation route、backup owner 和可执行 runbook。任何空白 Owner 使对应 gate `BLOCKED_INPUT`。

## 7. Evidence Package Per Step（每步证据包）

下列人工可读字段的规范机器投影是 [`production-gate-evidence-manifest-specification.md`](production-gate-evidence-manifest-specification.md)、[`schemas/production-gate-evidence-manifest.schema.v0.1.json`](schemas/production-gate-evidence-manifest.schema.v0.1.json) 和 [`production-gate-evidence-profiles.v0.1.json`](production-gate-evidence-profiles.v0.1.json)。未来实现不得另建宽松的 `passed=true` 文件或仅用 CI status 关闭 gate。

```text
step_id=
decision_ref=
gate_id=
architecture_commit=
architecture_tree_digest=
architecture_decision_packet_digest=
implementation_repo=
source_commit=
artifact_digest=
dependency_lock_or_sbom=
configuration_digest=
environment_and_topology=
workload_and_seed=
positive_tests=
negative_tests=
fault_tests=
security_findings=
delivery_loss_partial_duplicate_accounting=
backup_restore_or_rollback_ref=
open_unknowns=
reviewed_by_ref=
human_decision_ref=
result=PASS|FAIL|BLOCKED|NOT_ASSESSED
```

Implementation CI/review 必须将 `architecture_commit`、decision packet digest 和 referenced normative files 清单与已推送 immutable DBA baseline 比对：任一未提交工作树文件、digest drift、missing ref 或 superseded decision 使 gate 失败。该检查只证明实施引用哪个规范基线，不自动授权实施。

Human gate criteria（人工闸门准则）必须在执行前冻结，至少包含链接的 `SLO-001`–`SLO-017`、容量包络、allowed failures、zero-tolerance authority/security failures、RTO/RPO、观察周期、未知项处置和 rollback threshold。不允许只写“Human Review passed”而没有查询、阈值和证据。

## 8. Per-stage Rollback and Re-entry（逐阶段回退与重进）

| stage | rollback action | preserved evidence | re-entry requirement |
|---|---|---|---|
| `S1` | disable admission caller; preserve SQLite/WAL; restore only to new path | failed DB、test/fault outputs、source/config digest | DQ-018 scope unchanged + all reference tests pass |
| `S2/S2.5` | fence failed writer; switch only to verified target/backup by Human decision | failed cluster/store、WAL、backup、ack inventory | HA/PITR/migration/continuity drill pass |
| `S3A` | disable listener route and revoke staging credential; preserve rejected fixtures/results | transport exchanges、authn/authz、size/retry/partial/unknown records | exact transport/security case groups pass |
| `S3B` | drain/remove canary gateways; revert exact config/image/query/alert digest | queues/WAL、drop/partial/retry/unknown counts、drift/no-data/alert/incident logs | canary + HA/failover + independent self-observation + alert delivery + delivery reconciliation pass |
| `S4` | stop new Evidence admission; preserve all requests/records/Evidence/Verification | admitted/rejected/hold/unknown histories | identity/data governance/signature/policy tests pass |
| `S5` | disconnect SAEE adapter; retain DBOS facts and failed evaluations | input/output/version/timeout/conflict records | read-only/zero-writeback suite pass |
| `S6/S7` | stop workload/canary; execute service/database/Collector rollback runbooks | incidents、SLO windows、failures、human interventions | new explicit security/pilot review |

Rollback 不等于删数据或将失败改写成未发生。自动 rollback 只能执行预批准、有界、可逆的部署动作；不得自动修改 Architecture、Evidence 或 Permission。

## 9. Security and Data-governance Checkpoints（安全与数据治理检查点）

`S6` 是综合 Security/Recovery Gate，但安全不是到 `S6` 才开始。`S1`–`S5` 每阶段都必须在启用新 attack surface 前完成 scoped threat model、secret/network/data inventory、negative tests、dependency/SBOM 和 unresolved finding review。

`S4` 另外必须通过 Identity Continuity (`PR-G2I`) 和 Data Governance Gate；它们不能被加密签名、Collector authentication 或 schema validation 替代。`DQ-025` 只允许采纳 distribution architecture reference；不能单独授权 S3 build、configuration、listener、staging 或 deployment。

## 10. Pilot Duration and Mandatory Drills（试点周期与强制演练）

v0.1 最小时间为 7 天 staging soak + 30 天 bounded production observation，总计至少 37 个连续日历天，不是二者取其一。这个周期必须同时包含：

- 试点前冻结 failure-domain inventory：node、zone/rack、load balancer、DNS、certificate/identity、database quorum、backup/WAL archive、Collector WAL/PVC、message queue（如有）、observability backend、DBOS、SAEE 和 human/on-call；

- 完整 full-backup + WAL/PITR 周期和 timed restore；
- database primary/standby/quorum/fencing drill；
- Collector replica/node/load-balancer/backend/WAL/queue/disk failure；
- OTLP partial/retryable/permanent/disconnect/duplicate/drop reconciliation；
- config drift、mixed-version rollout 和 rollback；
- Evidence admission hold/reject/signature revocation/SAEE unavailable；
- steady、2x sustained、5x bounded burst 容量表征；
- on-call alert、incident command、human stop 和 runbook execution。

如 37 天内未覆盖完整 backup/retention cycle、声明 failure domains 或足够工作日/周末模式，Pilot 必须延长。High-impact profile 需独立决策设定更长周期；“90 天”不是无工作负载/故障演练时的自动充分条件。

## 11. Global Stop Rules（全局停止规则）

- 需要通过上一 gate 的“计划”而不是直接证据；
- Agent recommendation 被写成 Authorization 或 Customer Adoption；
- OTel Resource/Context 被写成 DBOS Identity/Permission；
- Collector/OTLP success 被写成 Evidence/Verification/Truth；
- sampling/drop/partial/duplicate/unknown 不可查；
- canonical acknowledged records 无法在声明 failure domain 恢复；
- SAEE 写回 DBOS 或自动执行 Recommendation；
- Critical/High 风险被模型、validator 或超时默认接受；
- 任何阶段创建未授权 Agent、Runtime、Permission 或 production resource。

## 12. Current State（当前状态）

```text
PRODUCTION_IMPLEMENTATION_SEQUENCE_DEFINED=true
CURRENT_STEP=S1_PR_G2A_HUMAN_REVIEW
DQ_022_REFERENCE_ADOPTED=true
S1_IMPLEMENTATION_AUTHORIZED=true
S1_IMPLEMENTATION_COMPLETE=true
PR_G2A_HUMAN_REVIEW_APPROVED=false
FULL_PR_G2_READY=false
S2_BACKEND_SELECTED=false
S3_OTLP_COLLECTOR_AUTHORIZED=false
S4_EVIDENCE_ADMISSION_AUTHORIZED=false
S5_SAEE_PRODUCTION_ADAPTER_AUTHORIZED=false
S6_SECURITY_RECOVERY_PASS=false
S7_PILOT_AUTHORIZED=false
S8_PRODUCTION_AUTHORIZED=false
S9_DEPLOYED=false
PRODUCTION_READY=false
```
