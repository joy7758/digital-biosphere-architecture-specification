---
document_id: TMAI-DQ-019-PERSISTENCE-CANDIDATE-ASSESSMENT-20260722
title: DQ-019 Production Persistence Candidate Assessment
title_zh: DQ-019 生产持久化候选评估
status: blocked-input-shortlist-ready-provider-due-diligence-pending
decision_id: DQ-019
primary_repository: digital-biosphere-architecture
backend_selected: false
implementation_authorized: false
production_ready: false
observed_at: 2026-07-22
---

# DQ-019 Production Persistence Candidate Assessment

中文：DQ-019 生产持久化候选评估。

## 1. Outcome First（结论先行）

当前可以冻结候选集，但不能选择 production backend（生产后端），也不能授权 DBOS 实施：

1. `P0` SQLite 继续只承担单机 reference conformance（参考符合性），禁止生产；
2. `P1` 单节点 PostgreSQL-compatible 可作为未来 staging（预生产验证）候选，但禁止生产；
3. `P2` 只保留两条生产候选：自管 PostgreSQL-compatible HA 与百度云 RDS PostgreSQL 双机高可用；
4. distributed SQL（分布式 SQL）在没有明确 multi-region（多地域）需求时延后；
5. 任何单节点拓扑（包括未来复用既有闲置服务器）都不能提供独立同步备用节点和故障域，只能作为
   `P1` 候选，不能证明 `P2`；本评估没有创建或指定任何生产资源。

```text
CANDIDATE_SHORTLIST_READY=true
BACKEND_SELECTED=false
DBOS_IMPLEMENTATION_AUTHORIZED=false
CLOUD_RESOURCE_AUTHORIZED=false
PRODUCTION_READY=false
```

## 2. Authority and OpenTelemetry Boundary（权力与 OTel 边界）

OpenTelemetry 是 vendor-neutral（厂商中立）的 telemetry receive/process/export（遥测接收／处理／导出）
体系，不是 observability backend（可观测后端）。因此：

```text
OpenTelemetry telemetry storage != DBOS canonical persistence
Collector queue/WAL != DBOS acknowledged canonical record
Telemetry signal != Evidence != Truth
```

Collector 存储不得与 DBOS canonical store 共用数据库、Schema、service account、backup path、
physical volume、secret/key 或 network policy。OTel 在本决策中只提供自观测语言和边界参考，不选择
DBOS 数据库。

## 3. Frozen Requirements（冻结要求）

候选必须在 exact profile（精确画像）中证明：

- transaction + authorization + append-only write 处于同一提交边界；
- acknowledged success 只在 canonical commit 后返回；
- optimistic previous reference、monotonic version、idempotency 与 replay protection；
- unknown commit outcome 可解析，失败记录不可静默删除；
- `P2` 同步复制、lag/quorum/degraded state 可观测，具备 fencing/split-brain control；
- full/base backup + continuous WAL + PITR，恢复到新目标并核对 continuity/count/digest/integrity；
- 在声明 failure domain 内测得 `RPO=0`，timed drill 测得 `RTO<=30m`；
- encryption、key/role separation、retention、immutability、audit 与 migration rollback；
- OTel 自观测只输出有界指标，不包含 ID、payload、SQL、secret、path 或用户值。

## 4. Candidate Matrix（候选矩阵）

| candidate | tier / disposition | consistency and durability | failure domain / recovery | operations / portability | current result |
|---|---|---|---|---|---|
| Self-managed PostgreSQL-compatible HA | `P2_CANDIDATE` | PostgreSQL 可表达 Serializable、同步提交和 WAL/PITR；具体版本、拓扑和 failover tool 未选择 | 需要至少独立 primary/standby failure domain、同步策略、fencing、backup archive 与新目标恢复演练 | 可移植性高；补丁、升级、监控、备份、故障转移和 24x7 owner 成本最高 | `CONDITIONALLY_ELIGIBLE_DUE_DILIGENCE_REQUIRED` |
| Baidu Cloud RDS PostgreSQL dual-node HA | `P2_CANDIDATE` | 官方材料声明主备高可用同步；DBOS 所需 commit/ack、隔离级别、同步确认和 fencing 仍需 exact engine/SKU 证明 | 官方材料描述双机和备份/API，但 region/AZ、SLA、PITR、restore drill、RPO/RTO 和导出证据未绑定 | 运维负担较低；存在 provider/API/SLA/版本/费用与可移植性约束 | `CONDITIONALLY_ELIGIBLE_PROVIDER_EVIDENCE_REQUIRED` |
| SQLite reference backend | `P0_ONLY` | 当前 DQ-018 本地单机合同验证；没有多节点 HA | 不提供独立 failure domain 或 production PITR/SLA | 最简单，但不能外推生产 | `REJECTED_FOR_PRODUCTION` |
| Distributed SQL | `P3_DEFERRED` | 尚无必要性和 exact product assessment | 可能覆盖 multi-region，但引入更大一致性、运维和成本复杂度 | 当前需求不足 | `DEFERRED_NO_MULTI_REGION_REQUIREMENT` |

## 5. Official Source Observations（官方来源观察）

| source | bounded observation | cannot prove |
|---|---|---|
| [OpenTelemetry: What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/) | OTel 不是 observability backend，存储/可视化交给其他工具 | DBOS canonical persistence 选型 |
| [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) | Collector 接收、处理并导出 telemetry 到一个或多个 backend | Collector queue/WAL 等于 DBOS durability |
| [PostgreSQL 18 replication](https://www.postgresql.org/docs/current/runtime-config-replication.html) | `remote_apply` 可让 COMMIT 等待同步备用节点应用 | 已有 HA、fencing、RPO/RTO 或生产配置 |
| [PostgreSQL 18 transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | Serializable 可检测序列化异常，应用必须处理事务重试 | DBOS adapter 已实现或正确 |
| [PostgreSQL 18 continuous archiving/PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) | base backup + archived WAL 支持 PITR | 备份策略、restore drill 或 RTO 已存在 |
| [Baidu RDS product series](https://cloud.baidu.com/doc/RDS/s/rjzz9p3n4) | PostgreSQL 支持单机基础版与主备高可用同步的双机高可用版 | exact PostgreSQL version/SKU/region、同步确认或 SLA |
| [Baidu RDS HA/DR](https://cloud.baidu.com/doc/RDS/s/vkaz2cvyz) | provider 描述主备/跨可用区与故障切换能力 | DBOS failure-domain proof、RPO/RTO drill 或 fencing evidence |
| [Baidu RDS automatic backup](https://intl.cloud.baidu.com/zh/doc/RDS/s/Hk941vehq-intl) | 新版材料描述 PostgreSQL 双机高可用的自动备份与保留 | 与目标地域/SKU/API 的完整一致性及实际恢复成功 |
| [Baidu RDS SLA](https://cloud.baidu.com/doc/RDS/s/vjwvyzgds) | 2026-04 页面将双机高可用纳入 `99.99%` 月度可用性承诺 | DBOS 实测 availability、RPO/RTO、数据完整性或赔偿外的风险 |
| [Baidu RDS primary/standby switch](https://cloud.baidu.com/doc/RDS/s/0jwvz0cps) | PostgreSQL 双机高可用支持自动／手动主备切换及可靠性／可用性优先策略 | exact replication acknowledgement、旧主 fencing、RPO=0 或切换时间 |
| [Baidu RDS PostgreSQL instance profile](https://intl.cloud.baidu.com/zh/doc/RDS/s/Wjztjsvu5-intl) | 2025-08 页面登记 PostgreSQL 双机高可用版本和规格 | 目标日期/地域当前可购买版本、minor policy 或 exact SKU |
| [Baidu RDS API directory](https://cloud.baidu.com/doc/RDS/s/ajwvz0x1m) | 存在实例、账号、备份、安全、参数、日志和版本管理 API | API 对目标 PostgreSQL SKU 的完整性或 agent-readable receipt 已实现 |

百度云不同更新时间的材料对 PostgreSQL 自动备份支持存在可解释但未消除的歧义；不同产品页面还出现
`99.95%` 与较新 SLA `99.99%` 两种可用性表述。选择 managed candidate 前必须取得同一目标
region/SKU/version/date 的当前产品说明、SLA、API 行为、备份/PITR/恢复证明，不能跨页面自动拼成
production claim。供应商 SLA 也不能代替 DBOS 自己的 SLO 测量。

机器可读尽调输入见
[`architecture/production-persistence-candidate-profiles.v0.1.json`](architecture/production-persistence-candidate-profiles.v0.1.json)
及其 [strict Schema](architecture/schemas/production-persistence-candidate-profiles.schema.v0.1.json)；当前四个
候选中 `P2_DECISION_ELIGIBLE=0`。

## 6. DQ-018 Direct Evidence Binding（DQ-018 直接证据绑定）

DBOS 远端精确源码与 clean-clone review packet（干净检出审查包）记录：

```text
source_commit=a3e491c954e911d84baa09fd6d9466fb80280941
receipt_commit=5f437b0719936470535211b796af3e9722e8f11b
implementation_manifest_sha256=9a8c3546a925812f0da86dad6cd09aa4680b2b29b734cd07dcfa9bc51f8dfe95
implementation_files=56
tests=523/523
telemetry_tests=189/189
validators=35/35
pr_g2_criteria=10/10_READY_FOR_HUMAN_REVIEW
pr_g2_human_review_approved=false
```

这关闭了 DQ-019 所需的 exact source + clean-clone input（精确源码与干净检出输入），但没有自动
关闭 PR-G2 Human Review，也没有提供任一 `P2` 候选的直接后端证据。因此它仍不能形成 DQ-019
implementation authorization（实施授权），更不能证明任一 `P2` 后端。

## 7. Remaining Decision Inputs（剩余决策输入）

| input | status | required output |
|---|---|---|
| exact DBOS source commit + clean-clone receipts | `BLOCKED` | immutable DQ-018 source/evidence binding |
| hosting policy | `MISSING` | managed external cloud allowed/denied；data residency |
| topology and failure domain | `MISSING` | region/AZ/node/quorum/fencing/connection topology |
| exact candidate profile | `MISSING` | engine/version/SKU/replication/failover/backup/encryption |
| Owner and on-call | `MISSING` | accountable owner、escalation、runbook/rollback |
| security review | `MISSING` | IAM/TLS/key/secret/network/audit/backup separation |
| cost review | `MISSING` | monthly cap、storage/IO/backup/egress/operations estimate |
| RPO/RTO acceptance | `MISSING` | accept or revise `RPO=0` / `RTO<=30m` target |
| direct drills | `NOT_EXECUTED` | failover、unknown commit、backup/PITR/new-target restore receipts |

## 8. Stop Rules（停止规则）

- 不得因 PostgreSQL 官方功能存在就声明 DBOS production ready；
- 不得因 RDS 名称包含“高可用”就声明满足 DBOS failure-domain/RPO/RTO；
- 不得把任何单节点拓扑或闲置服务器包装成 `P2`；
- 不得创建数据库、账号、实例、网络、secret、backup 或 production record；
- 不得把模型建议、供应商页面或本评估变成 Human Decision；
- 缺少任一 exact profile、Owner、security/cost review 或 direct drill 时必须失败关闭。
