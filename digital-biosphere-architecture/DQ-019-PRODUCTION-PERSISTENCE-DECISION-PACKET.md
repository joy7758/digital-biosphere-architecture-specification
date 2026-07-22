---
document_id: TMAI-DQ-019-PERSISTENCE-DECISION-PACKET-20260722
title: DQ-019 Production Persistence Decision Packet
title_zh: DQ-019 生产持久化决策包
status: blocked-input-candidate-shortlist-ready
decision_id: DQ-019
primary_repository: digital-biosphere-architecture
decision_ready: false
backend_selected: false
implementation_authorized: false
production_ready: false
---

# DQ-019 Production Persistence Decision Packet

中文：DQ-019 生产持久化决策包。

## 1. Decision Question（决策问题）

选择哪个 exact production persistence backend/profile（精确生产持久化后端／画像），并是否授权
DBOS 在独立 Git 决策和全部前置证据满足后实施 exact adapter slice（精确适配器切片）？

当前答案：`NOT_READY_FOR_HUMAN_SELECTION`。候选集已经收敛，但 backend、version、topology、Owner、
cost/security、RPO/RTO 和 direct drill 证据仍缺失。

## 2. Normative Inputs（规范输入）

| input | status | role |
|---|---|---|
| [`architecture/production-persistence-adapter-specification.md`](architecture/production-persistence-adapter-specification.md) | `PROPOSED_DQ_019_BLOCKED_INPUT` | backend-neutral transaction/HA/PITR/security/OTel contract |
| [`architecture/production-persistence-candidate-due-diligence-contract.md`](architecture/production-persistence-candidate-due-diligence-contract.md) | `DEFINED_NO_ASSESSMENT_NO_SELECTION` | evidence layers、exact profile、OTel database semantics、provider/direct drill contract |
| [`architecture/production-persistence-candidate-profiles.v0.1.json`](architecture/production-persistence-candidate-profiles.v0.1.json) / [Schema](architecture/schemas/production-persistence-candidate-profiles.schema.v0.1.json) | `SCHEMA_VALID_4_CANDIDATES_P2_ELIGIBLE_0` | machine-readable fail-closed candidate state |
| [`architecture/production-slo-and-evidence-gates.md`](architecture/production-slo-and-evidence-gates.md) | `TARGETS_DEFINED_NOT_MEASURED` | candidate RPO/RTO/SLO and direct-evidence gates |
| [`DQ-019-PRODUCTION-PERSISTENCE-CANDIDATE-ASSESSMENT.md`](DQ-019-PRODUCTION-PERSISTENCE-CANDIDATE-ASSESSMENT.md) / [JSON](DQ-019-PRODUCTION-PERSISTENCE-CANDIDATE-ASSESSMENT.json) | `SHORTLIST_READY_BLOCKED_INPUT` | candidate comparison and official-source registry |
| DQ-018 DBOS local review packet | `9/10_BLOCKED_EXACT_SOURCE_COMMIT` | reference-contract direct local input only |
| [`DQ-019-PRODUCTION-PERSISTENCE-AGENT-RECOMMENDATION.md`](DQ-019-PRODUCTION-PERSISTENCE-AGENT-RECOMMENDATION.md) | `TWO_PROVIDER_RECOMMENDED_AS_BLOCKED_INPUT` | adversarial advisory review; never authorization or backend selection |

## 3. Current Candidate Set（当前候选集）

```text
P2_A=SELF_MANAGED_POSTGRESQL_COMPATIBLE_HA
P2_B=BAIDU_RDS_POSTGRESQL_DUAL_NODE_HA
P0_SQLITE=REJECT_FOR_PRODUCTION
P3_DISTRIBUTED_SQL=DEFER_NO_MULTI_REGION_REQUIREMENT
```

不在本包中选定 PostgreSQL distribution/version、managed SKU、region/AZ、replication mode、failover
manager、backup tool、observability backend 或云资源。

## 4. Decision Readiness Matrix（决策就绪矩阵）

| gate | result | reason |
|---|---|---|
| candidate set bounded | `PASS` | 两个 P2 候选，P0/P3 disposition 明确 |
| architecture contract | `PASS` | backend-neutral invariants 和 separation 已定义 |
| official source registry | `PASS_WITH_GAPS` | upstream/provider 官方来源已登记，managed exact product evidence 未闭合 |
| strict candidate-profile Schema | `PASS_STRUCTURE_ONLY` | 4 candidates；5/5 negative mutations rejected；`P2_DECISION_ELIGIBLE=0` |
| DQ-018 exact source binding | `BLOCKED` | 本地实现没有 authorized exact commit |
| exact backend profile | `BLOCKED` | distribution/version/SKU/region/topology 未确定 |
| Owner/on-call | `BLOCKED` | production operator 未指派 |
| security/cost review | `BLOCKED` | 未形成审查记录 |
| RPO/RTO acceptance | `BLOCKED` | candidate targets 尚未由人类接受或修改 |
| failover/backup/PITR/restore evidence | `BLOCKED` | 未执行，不存在生产资源 |
| independent agent review | `PASS_FOR_BLOCKED_INPUT_ONLY` | 两路均推荐作为 blocked pre-decision input；均拒绝 backend selection 和 production recommendation |

## 5. Inputs Required From Human Owner（需要人类 Owner 补充）

```text
managed_cloud_allowed=<true|false>
data_residency=<region-and-policy>
monthly_cost_cap=<currency-and-amount>
production_owner_ref=<human-reference>
on_call_model=<reference>
target_failure_domain=<single-region-multi-az|other>
rpo_target=<accept-0-or-revise>
rto_target=<accept-30m-or-revise>
preferred_due_diligence_lane=<self-managed-ha|baidu-rds-postgresql-ha|both>
```

这些输入只允许完成 due diligence（尽职调查）和决策准备，不自动创建云资源或授权实现。

## 6. Future Decision Options（未来决策选项）

只有第 4 节全部为 `PASS` 且 packet 绑定 exact artifact 后，才可生成最终 token：

### Option A — Select and Authorize Exact Backend Slice

```text
DQ-019=SELECT_<EXACT_BACKEND_PROFILE>_AND_AUTHORIZE_DBOS_PERSISTENCE_ADAPTER
dbos_domain_owner_ref=<human-reference>
```

效力必须局限于 exact adapter、migrations、tests、failure drills 和 bounded OTel self-observation。
不得隐含数据迁移、云资源购买/创建、production deployment、traffic 或 release。

### Option B — Hold at P0/P1

```text
DQ-019=HOLD_PRODUCTION_PERSISTENCE_AT_REFERENCE_AND_STAGING_ONLY
reason=<reason>
```

### Option C — Return for Revision

```text
DQ-019=RETURN_PRODUCTION_PERSISTENCE_CANDIDATES_FOR_REVISION
reason=<reason>
```

本文件当前不提供可直接复制的 Option A exact token，因为具体 backend profile 不存在。生成虚假 token
会把候选评估误写成实施授权。

## 7. Required Separate Authorizations（必须分开的授权）

即使未来 DQ-019 选型通过，以下仍须分开：

- DBOS implementation authorization（若 exact DQ-019 token 未包含）；
- DBOS commit/push/PR/merge；
- cloud account/resource/procurement；
- data migration；
- staging deployment；
- production deployment/traffic；
- release/public production claim。

## 8. Current Truth（当前事实）

```text
DQ_019_STATUS=BLOCKED_INPUT
CANDIDATE_SHORTLIST_READY=true
AGENT_RECOMMENDATION_COMPLETE=true
HUMAN_BACKEND_DECISION_RECORDED=false
BACKEND_SELECTED=false
DBOS_PERSISTENCE_IMPLEMENTATION_AUTHORIZED=false
DBOS_PERSISTENCE_IMPLEMENTATION_STARTED=false
CLOUD_RESOURCE_CREATED=false
PRODUCTION_READY=false
```
