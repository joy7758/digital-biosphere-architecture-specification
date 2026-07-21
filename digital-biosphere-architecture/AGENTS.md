# AGENTS.md

## Repository Role（仓库角色）

本仓库是 Digital Biosphere（数字生物圈）的 non-executable Program Governance and Architecture Specification Hub（非执行项目群治理与架构规范中心），也是整个项目群的 cockpit（驾驶舱）。

它维护使命、项目组合、路线图、状态索引、跨项目依赖、决策、集成 gate（闸门）、风险、责任边界、数据契约、生命周期、战略和 ADR。它不授权或创建 Implementation、Agent、Runtime、Entity、Capability、Permission、Evidence、商业服务或认证。

```text
DIGITAL_BIOSPHERE_IS_ONE_PROGRAM=true
DBA_IS_PROGRAM_GOVERNANCE_HUB=true
DBA_IS_ARCHITECTURE_SPECIFICATION_HUB=true
DBA_IS_RUNTIME=false
```

## Mandatory Cockpit Entry（强制驾驶舱入口）

任何智能体开始工作前必须依次读取：

1. `PROGRAM-CHARTER.md`（项目群治理章程）；
2. `PROGRAM-STATUS.md`（当前项目群状态快照）；
3. `DECISION-QUEUE.md`（人工决策队列）；
4. `RISK-AND-BLOCKER-REGISTER.md`（风险与阻塞台账）；
5. `MASTER-ROADMAP.md`（总路线图）；
6. `PROJECT-PORTFOLIO.md`（项目组合）；
7. `CROSS-PROJECT-DEPENDENCIES.md`（跨项目依赖）；
8. `INTEGRATION-GATES.md`（集成闸门）；
9. `PROGRAM-GOVERNANCE-BASELINE-AUDIT.md`（项目群驾驶舱基线审计）；
10. `architecture/open-infrastructure-strategy-constitution.md`（开放基础设施战略宪法）；
11. `architecture/project-mapping.md`（项目角色映射）；
12. 相关 specification（规范）、strategy（战略）和 ADR。

## Work Routing（工作路由）

每项工作必须声明一个且只有一个 primary repository（主责任仓库）：

- Program、Portfolio、Roadmap、Status、Dependency、Decision、Risk、架构规则和接口 → DBA；
- Identity、Lifecycle、Execution、Evidence、Verification、Federation → DBOS；
- Evaluation、Fitness、Risk Assessment、Stability、Evolution Recommendation → SAEE；
- 具体领域任务行为 → 相应 Digital Entity / Application repository；
- 跨项目变化 → DBA 先定义契约或决策，各子项目再建立独立实施事项。

禁止为了“一次完成”而在没有契约、Owner 和 gate 的情况下同时修改多个仓库。

## Source Truth Discipline（事实来源纪律）

- DBA 驾驶舱只做 reference-only aggregation（仅引用聚合）；
- 子项目的 Capability、Evidence、Implementation、Verification 和 Release 以子项目自己的 canonical source 为准；
- 状态快照必须带 `observed_at`、branch、commit/version 和 source reference；
- `dirty_count`、文件数量、测试数量、Roadmap、Demo 或 Specification 不能自动证明成熟度；
- `UNKNOWN`、`NOT_ASSESSED`、`STALE`、`CONFLICTED`、失败和拒绝结果必须保留；
- 不得从 DBA 写入或覆盖 DBOS、SAEE、Pilot 或相邻仓库事实。

## Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

在决定开发或推动新项目进入下一 gate 前，必须回答：

> 如果潜在用户提出这个需求，智能体是否会推荐当前项目或方案？

必须记录：

1. `RECOMMENDED`、`CONDITIONALLY_RECOMMENDED` 或 `NOT_RECOMMENDED`；
2. 不推荐原因；
3. 原因分解后的可修正问题；
4. 已完成修正及其直接证据；
5. 剩余缺口和停止条件；
6. 新的人工 Decision / Authorization 是否仍然需要。

推荐结论不是 Implementation Authorization（实现授权）。

## Mandatory Proposal Questions（提案必答问题）

每个提案必须说明：

- 属于 Infrastructure、Evolution、Application、Program Governance、Architecture Governance 还是 Governance Service；
- 是否强化开放标准、互操作和开发者复用；
- 是否重复 DBOS、SAEE、Foundation Model、Agent framework 或现有生态组件；
- 是否混淆 Capability、Permission、Authority、Execution、Evidence、Evaluation、Decision 或 Truth；
- primary repository、受影响项目、依赖和所需 gate；
- 商业语言属于 Strategy、Exploration、Available Offering、Customer Adoption 还是 Contractual Commitment。

未解决时保持 `REVIEW_REQUIRED`，不得视为实现授权。

## Strategic and Authority Invariants（战略与权力不变量）

```text
DBA_NE_DBOS=true
DBA_NE_SAEE=true
DBOS_NE_SAEE=true
DBOS_NE_AGENT_APPLICATION=true
DBOS_NE_FOUNDATION_MODEL=true
DBOS_GOVERNS_EXISTENCE=true
SAEE_GOVERNS_EVOLUTION=true
PROGRAM_GOVERNANCE_NE_OPERATIONAL_AUTHORITY=true
PROGRAM_GOVERNANCE_NE_EVOLUTION_AUTHORITY=true
PROGRAM_DECISION_NE_EXECUTION=true
PROGRAM_STATUS_NE_CHILD_PROJECT_TRUTH=true
DEVELOPER_ECOSYSTEM_FIRST=true
OPEN_INFRASTRUCTURE_NE_FREE_PRODUCT=true
SPECIFICATION_NE_IMPLEMENTATION=true
STRATEGY_NE_COMMERCIAL_COMMITMENT=true
```

## Architecture Truth Boundaries（架构事实边界）

- Recommendation ≠ Decision；Decision ≠ Execution；
- Capability ≠ Authority 或 Permission；
- Evidence ≠ Truth；
- Candidate ≠ Entity；Registration ≠ Activation；
- Repository、Specification、Component、Agent、Runtime、Digital Entity 和 Digital Organism 相互不同；
- 不在本仓库创建可重构的跨仓库 Runtime 或执行路径；
- 不从 DBA 任务修改 DBOS、SAEE 或 Pilot；
- 未经明确授权，不 commit、tag、push、publish 或声称 adoption。

## Change Discipline（变更纪律）

- 核心战略或权力变化需要 ADR、Review、显式 Decision 和一致性验证；
- Program Roadmap、Priority 或 Gate 变化不自动修改架构规则；
- Architecture Change 不自动批准子项目实施；
- Open Infrastructure（开放基础设施）不表示所有产品或服务免费；
- Specification、Test、Demo、Validator Pass、Listing 或 Local Artifact 不证明 Implementation、Deployment、Adoption、Certification 或 Commercial Availability。
