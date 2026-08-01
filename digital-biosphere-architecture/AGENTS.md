# AGENTS.md

## Repository Role（仓库角色）

本仓库是 Digital Biosphere（数字生物圈）的 non-executable Program Governance and Architecture Specification Hub（非执行项目群治理与架构规范中心），也是整个项目群的 cockpit（驾驶舱）。

它维护使命、项目组合、路线图、状态索引、跨项目依赖、决策、集成 gate（闸门）、风险、责任边界、数据契约、生命周期、战略和 ADR。它不授权或创建 Implementation、Agent、Runtime、Entity、Capability、Permission、Evidence、商业服务或认证。

```text
DIGITAL_BIOSPHERE_IS_ONE_PROGRAM=true
DBA_IS_PROGRAM_GOVERNANCE_HUB=true
DBA_IS_ARCHITECTURE_SPECIFICATION_HUB=true
DBA_IS_RUNTIME=false
PUBLIC_POSITIONING=TRUSTED_MULTI_AGENT_INFRASTRUCTURE
PROTOCOLIZATION_BEFORE_PLATFORM_EXPANSION=true
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

处理 TITMAS 或开发者社区工作时，还必须读取：

13. `CONTRIBUTING.md`（贡献入口与智能体披露）；
14. `TITMAS-CONTRIBUTOR-ENTRY-v0.1.json`（机器可读当前状态）；
15. `architecture/titmas-document-maturity-policy-v0.1.md`（文档级成熟度）；
16. `architecture/titmas-contribution-proposal-template-v0.1.md`（重大变化 Proposal）；
17. `architecture/titmas-architecture-charter-v0.2.md`（TITMAS 项目身份与边界的
    canonical Charter）。

进行 TITMAS 工作时，如 v0.2 Charter 不存在、不可读或状态含义不清，必须停止扩大
TITMAS scope 并报告。每次重大 TITMAS 任务的最终答复必须包含该 Charter 定义的
`TITMAS_DRIFT_CHECK`；本文件只引用 canonical Charter，不复制检查项。Drift Check 是
Human Review Gate，不是 automated enforcement，也不授权 Implementation 或响应动作。

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

## TITMAS Infrastructure Developer Community Guard（TITMAS 基础设施开发者社区护栏）

TITMAS 社区方向的规范名称是：

```text
English: TITMAS Infrastructure Developer Community
Chinese: TITMAS 可信多智能体基础设施开发者社区
Subtitle: Developer Community for Trusted Multi-Agent Infrastructure
```

首次接触说明必须让开发者理解：开发者负责构建 Agent；TITMAS 围绕开放规范、Adapter
contract、Conformance 和参考实现边界，帮助不同 Agent 通过易理解、可实现、可验证的
基础设施规则协作。

后续智能体必须读取
[`architecture/titmas-infrastructure-developer-community-strategy-v0.1.md`](architecture/titmas-infrastructure-developer-community-strategy-v0.1.md)
、[`CONTRIBUTING.md`](CONTRIBUTING.md)、
[`TITMAS-CONTRIBUTOR-ENTRY-v0.1.json`](TITMAS-CONTRIBUTOR-ENTRY-v0.1.json)
和 [`ADR-029`](architecture/ADR-029-titmas-infrastructure-developer-community-direction.md)，并保持：

- 重度参考 OpenTelemetry 的规范／实现／Contrib 分离、文档级成熟度、版本声明、公开贡献
  路径和符合性矩阵；
- Reference Adoption 不等于 TITMAS 获得 OpenTelemetry 品牌、组织地位、运行兼容或认可；
- 先有真实工作、参与者、Maintainer/Reviewer 和公开流程，才可提议正式 SIG；
- Community Review 不等于 Architecture Decision；
- 社区角色不自动取得 DBA、DBOS、SAEE 或连接项目 Authority；
- 智能体贡献必须披露模型／工具、来源、验证者和人工责任方；智能体不能自我批准或成为
  自动 Member、Maintainer 或 Architecture Authority；
- 成熟度属于单个文档；Document Stable 不传播为 Implementation、Community、Release、
  Adoption 或 Production Stable；
- TITMAS 不是普通 Agent 社区、Agent Framework、Agent Platform、基金会或第二个 DBA；
- 当前 `TITMAS_CURRENT_COMMUNITY_STATE=CONTRIBUTOR_ENTRY_PREPARED`，只表示本地贡献入口、
  模板、候选清单和机器可读文件已经准备；
- 当前 `TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false`，不得从战略文档升级状态；
- 正式 Code of Conduct、安全接收路径、角色、公开贡献表面、组织账号、仓库、Issue、PR、
  实现和发布仍需分别授权。

## Strategic and Authority Invariants（战略与权力不变量）

```text
DBA_NE_DBOS=true
DBA_NE_SAEE=true
DBOS_NE_SAEE=true
DBOS_NE_AGENT_APPLICATION=true
DBOS_NE_AGENT_FRAMEWORK=true
DBOS_NE_FOUNDATION_MODEL=true
DBOS_GOVERNS_EXISTENCE=true
SAEE_GOVERNS_EVOLUTION=true
SAEE_NE_CONTROLLER=true
PROGRAM_GOVERNANCE_NE_OPERATIONAL_AUTHORITY=true
PROGRAM_GOVERNANCE_NE_EVOLUTION_AUTHORITY=true
PROGRAM_DECISION_NE_EXECUTION=true
PROGRAM_STATUS_NE_CHILD_PROJECT_TRUTH=true
DEVELOPER_ECOSYSTEM_FIRST=true
OPEN_INFRASTRUCTURE_NE_FREE_PRODUCT=true
SPECIFICATION_NE_IMPLEMENTATION=true
STRATEGY_NE_COMMERCIAL_COMMITMENT=true
TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED=true
TITMAS_CONTRIBUTOR_ENTRY_PREPARED=true
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_FOUNDATION_IN_SCOPE=false
TELEMETRY_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
UNBOUNDED_CENTRAL_INTELLIGENCE_IS_NOT_TARGET=true
COMPOSITIONAL_SCALE_IS_STRATEGIC_DEFAULT=true
SIMPLE_ENTITY_NE_UNGOVERNED_ENTITY=true
COMPOSITION_NE_AUTHORITY_AGGREGATION=true
COORDINATION_NE_UNBOUNDED_CENTER=true
COVERAGE_NE_CORRECTNESS_OR_TRUTH=true
EMERGENT_CAPABILITY_NE_AUTOMATIC_PERMISSION=true
```

任何智能体提出架构或实现方向时，必须优先检查能否由职责简单、边界受限、可替换的
主体或服务通过显式契约组合完成。不得以“能力更强”作为建设无限强中心的理由，也不得
把组合规模、连接数量或涌现行为升级为 Authority、Permission、Decision、Truth 或
全局控制。有限治理和协调必须保留，但协调组件本身必须可审计、可撤销且边界有限。

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
