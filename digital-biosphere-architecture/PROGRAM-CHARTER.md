---
document_id: DBA-PROGRAM-CHARTER-0.1
title: Digital Biosphere Program Governance Charter v0.1
title_zh: 数字生物圈项目群治理章程 v0.1
status: accepted-owner-assigned
decision_reference: architecture/ADR-020-release-preparation-owner-decisions.md
program_authority_assigned: true
program_owner_ref: zhangbin
runtime_authority_created: false
source_of_truth_policy: reference-only-aggregation
last_reviewed: 2026-07-21
---

# Digital Biosphere Program Governance Charter v0.1（数字生物圈项目群治理章程 v0.1）

## 1. Program Mission（项目群使命）

Digital Biosphere（数字生物圈）是一个总项目，面向长期运行、多智能体协作和可验证演化的数字主体基础设施项目群。它的统一对外定位是 Trusted Multi-Agent Infrastructure（可信多智能体基础设施），不是 DBA、DBOS、SAEE 三个互不相关的产品，也不是 Agent Platform、Agent Framework、Workflow Tool 或 AI Cloud Platform。

> Infrastructure for long-running, collaborative, and verifiable digital entities.

Digital Biosphere Architecture（数字生物圈架构，简称 DBA）是该项目群的 Program Governance and Architecture Specification Hub（项目群治理与架构规范中心），也是整体推进所使用的 cockpit（驾驶舱）。它统一维护方向、项目组合、跨项目边界、路线图、依赖、决策、集成 gate（闸门）、风险和状态索引。

```text
DIGITAL_BIOSPHERE_IS_ONE_PROGRAM=true
DBA_IS_PROGRAM_GOVERNANCE_HUB=true
DBA_IS_ARCHITECTURE_SPECIFICATION_HUB=true
DBA_IS_RUNTIME=false
DBA_IS_DBOS=false
DBA_IS_SAEE=false
```

## 2. Program Structure（项目群结构）

```text
Digital Biosphere Program
  └─ DBA: program governance + architecture rules
       ├─ DBOS: existence and operational infrastructure
       ├─ SAEE: evaluation and evolution intelligence
       ├─ Digital Entity pilots: task-specific application workstreams
       └─ Adjacent components: admitted only after boundary review
```

这里的层级表示 program coordination（项目协调）和 responsibility routing（责任路由），不是仓库所有权、代码依赖、Runtime 控制或权限继承。DBOS、SAEE 和各应用仓库继续维护自己的实现与事实表面。

## 3. DBA Program Governance Scope（DBA 项目群治理范围）

DBA 负责：

- 维护 Digital Biosphere 的统一使命、战略不变量和项目语言；
- 定义并维护 Project Portfolio（项目组合）及项目准入分类；
- 排定跨项目优先级、里程碑和推进顺序；
- 维护跨项目依赖、接口契约和重复建设检查；
- 维护 Decision Queue（决策队列）、ADR 和决策追溯；
- 定义 Integration Gates（集成闸门）与每个阶段的最小证据；
- 汇总带来源、带时间和带状态的项目快照；
- 暴露风险、阻塞项、未知项和下一步人工决定；
- 为编码智能体、检索智能体和引用智能体提供统一入口。

DBA 不负责：

- 运行或部署 DBOS；
- 修改、选择或替代 SAEE 内部算法；
- 直接写入子项目的 Capability、Evidence、Permission、Release 或 Runtime truth（事实）；
- 自动改变任何项目状态；
- 代表项目负责人批准实现、合并、发布、部署、实验或外部采用；
- 把 dashboard observation（驾驶舱观察）升级为子项目规范事实。

## 4. Governance Authorities（治理权力分离）

| 责任域 | 负责 | 不表示 |
|---|---|---|
| Program Governance（项目群治理） | 组合、优先级、里程碑、依赖、决策队列、集成 gate 和状态沟通 | 有权执行子项目、修改运行状态或重写领域事实 |
| Architecture Governance（架构治理） | 规则、边界、接口、ADR、版本和一致性 | Runtime Governance（运行治理）或算法控制 |
| DBOS Operational Authority（DBOS 运行责任） | 在有效授权和生命周期约束内管理存在与运行记录 | Program Authority（项目群权力）或 Evolution Authority（演化权力） |
| SAEE Evolution Authority（SAEE 演化责任） | 评价、适应度、风险、稳定性和演化建议 | 执行权、状态写权或项目群优先级决定权 |
| Human Decision Authority（人工决策责任） | 对优先级、采纳、授权、发布和高影响变化作显式决定 | 因文档角色而自动获得账号、Permission 或 Runtime 能力 |

```text
PROGRAM_GOVERNANCE_NE_OPERATIONAL_AUTHORITY=true
PROGRAM_GOVERNANCE_NE_EVOLUTION_AUTHORITY=true
PROGRAM_DECISION_NE_EXECUTION=true
PROGRAM_STATUS_NE_PROJECT_TRUTH=true
```

`ADR-020` 已指派 `zhangbin` 为 Human Program Owner（人工项目群负责人）。该指派负责
项目群优先级、准入和跨项目 gate 的人工关闭，直到被显式撤销或取代，并在每次重大
release（发布）决定时复核。它不自动产生 DBOS Operational Authority（运行权力）、
SAEE Evolution Authority（演化权力）、仓库账号权限或 Release Authorization（发布授权）。

## 5. Truth Source Policy（事实来源策略）

驾驶舱采用 reference-only aggregation（仅引用聚合）：

1. 子项目的代码、Capability、Evidence、验证、发布与工作树状态，以子项目自己的 canonical source（规范来源）为准；
2. DBA 的规范、接口、责任边界和跨项目决策，以 DBA 当前已采纳规范和 ADR 为准；
3. [`PROGRAM-STATUS.md`](PROGRAM-STATUS.md) 只保存带 `observed_at`、source path（来源路径）、branch（分支）和 commit（提交）的时间点快照；
4. [`MASTER-ROADMAP.md`](MASTER-ROADMAP.md) 表示计划与 gate，不证明实现；
5. 未发现、未核验、冲突或过期的状态必须保留为 `UNKNOWN`、`NOT_ASSESSED`、`CONFLICTED` 或 `STALE`；
6. DBA 不复制会导致双重规范权威的子项目 ledger（台账），只保存稳定引用和有限摘要。

事实优先级：

```text
child repository canonical evidence
  > accepted cross-project contract or ADR
  > timestamped DBA observation
  > roadmap or narrative
```

该优先级只解决 DBA 如何陈述项目状态，不允许子项目实现反向覆盖已采纳架构边界；冲突必须进入 Decision Queue 和 ADR 流程。

## 6. Program Operating Cycle（项目群运转周期）

```text
Intake
  → Classification
  → Source Verification
  → Architecture / Duplication Review
  → Human Decision
  → Project Assignment
  → Gate Evidence
  → Status Synchronization
  → Program Review
```

| 阶段 | DBA 产物 | 停止条件 |
|---|---|---|
| Intake（接收） | 问题、目标、提出来源 | 目标或范围无法识别 |
| Classification（分类） | 归属 DBA、DBOS、SAEE、Digital Entity 或相邻组件 | Owner 冲突或重复建设未审查 |
| Source Verification（来源核验） | canonical source、branch、commit、状态证据 | 来源未知、冲突或不可访问 |
| Review（审查） | 边界、依赖、风险和替代方案 | Capability、Authority、Permission、Evidence 或 Evaluation 被混淆 |
| Decision（决策） | 显式结果、范围、决策来源 | 决策来源缺失 |
| Assignment（分派） | 一个 primary repository（主责任仓库）和可选下游任务 | 同一事项被同时写入多个仓库而无契约 |
| Gate（闸门） | [`INTEGRATION-GATES.md`](INTEGRATION-GATES.md) 指定的证据 | `NOT_ASSESSED`、`FAIL`、`BLOCKED` 或证据不足 |
| Synchronization（同步） | 带时间的驾驶舱快照 | 子项目事实无法追溯 |
| Program Review（项目群复核） | 下一优先级、风险和待决事项 | 不得自动进入实现或发布 |

## 7. Work Routing Rule（工作路由规则）

每项工作必须只有一个 primary repository：

- 规则、边界、接口、ADR、组合与总体路线图 → DBA；
- 身份、生命周期、执行记录、Evidence、Verification 和 Federation → DBOS；
- Evaluation、Fitness、Risk、Stability 和 Evolution Recommendation → SAEE；
- 文献分析、医学、机器人或行业任务行为 → 相应 Digital Entity / Application repository；
- 跨项目变化 → 先在 DBA 完成契约或决策，再为各子项目创建独立实施事项。

## 8. Pre-development Agent Recommendation（开发前智能体推荐）

问题：如果潜在用户需要管理多个独立基础设施与智能体项目，我是否会推荐这个 DBA 驾驶舱？

```text
AGENT_RECOMMENDATION=RECOMMENDED_WITH_SOURCE_BOUNDARY
RECOMMENDED_AS=PROGRAM_GOVERNANCE_AND_ARCHITECTURE_COCKPIT
NOT_RECOMMENDED_AS=RUNTIME_OR_AUTOMATIC_PROJECT_CONTROL
```

推荐理由：统一入口、明确 Owner、保留未知、阻止跨域越权，并把决策与执行分离。

不推荐条件及修正：

| 不推荐原因 | 本基线的修正 | 剩余 gate |
|---|---|---|
| 只写规范，不能回答当前推进位置 | 增加 Portfolio、Roadmap、Status、Decision、Gate 与 Risk 台账 | 建立稳定刷新节奏 |
| 驾驶舱可能复制或覆盖子项目事实 | 采用 reference-only aggregation 和 source precedence | 为每个核心项目确认 canonical status source |
| 管理权可能被误读为执行权 | 明确 Program、Architecture、Operational、Evolution 与 Human Decision 分离；`ADR-020` 记录具体 Program Owner | 重大发布时复核角色，且每次执行仍需独立授权 |
| 静态文档可能过期 | 所有状态快照带日期、branch、commit 与 freshness | 后续决定是否需要只读自动同步 |

## 9. Cockpit Entry（驾驶舱入口）

1. [`PROGRAM-STATUS.md`](PROGRAM-STATUS.md)：现在在哪里；
2. [`DECISION-QUEUE.md`](DECISION-QUEUE.md)：需要人决定什么；
3. [`RISK-AND-BLOCKER-REGISTER.md`](RISK-AND-BLOCKER-REGISTER.md)：什么会阻塞；
4. [`MASTER-ROADMAP.md`](MASTER-ROADMAP.md)：下一阶段是什么；
5. [`PROJECT-PORTFOLIO.md`](PROJECT-PORTFOLIO.md)：有哪些项目、各自负责什么；
6. [`CROSS-PROJECT-DEPENDENCIES.md`](CROSS-PROJECT-DEPENDENCIES.md)：谁依赖谁；
7. [`INTEGRATION-GATES.md`](INTEGRATION-GATES.md)：什么证据允许继续；
8. [`architecture/program-governance-specification.md`](architecture/program-governance-specification.md)：治理规则。
9. [`PROGRAM-GOVERNANCE-BASELINE-AUDIT.md`](PROGRAM-GOVERNANCE-BASELINE-AUDIT.md)：基线完成证据与剩余决定。

## 10. Non-claims（非声明）

```text
PROGRAM_GOVERNANCE_BASELINE_DEFINED=true
PROGRAM_AUTHORITY_ASSIGNED=true
PROGRAM_OWNER_REF=zhangbin
PROGRAM_OWNER_ASSIGNMENT_REFERENCE=ADR-020
CHILD_REPOSITORIES_MODIFIED=false
INTEGRATION_IMPLEMENTED=false
RUNTIME_CREATED=false
AGENT_CREATED=false
ENTITY_CREATED=false
CAPABILITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_TRUTH_CHANGED=false
```
