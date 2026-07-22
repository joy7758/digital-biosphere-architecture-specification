# Digital Biosphere Open Infrastructure Strategy Constitution v0.1

中文：数字生物圈开放基础设施战略宪法 v0.1

Status: `ADOPTED_STRATEGIC_CONSTITUTION`

Authority: Architecture governance and strategic interpretation only

Implementation effect: `NONE`

## Constitutional Position

> Infrastructure for long-running, collaborative, and verifiable digital entities.

中文：面向长期运行、协作和可验证数字主体的基础设施。

Digital Biosphere 是一个总项目；`Trusted Multi-Agent Infrastructure`（可信多智能体基础设施）是统一对外定位。DBA、DBOS、SAEE 和 Digital Entities 是同一项目群内的责任层，不是三个或四个互不相关的产品。

本项目不以 Agent Platform（智能体平台）、Agent Framework（智能体框架）、
Workflow Tool（工作流工具）或 AI Cloud Platform（人工智能云平台）为目标。
它面向 AI Agent 时代提供可信基础设施：定义数字主体长期存在、相互协作、
被验证、被评价并在治理下演化时必须保持的开放规则和责任边界。

本宪法固定长期战略方向。它约束架构解释、项目归属、开发优先级和商业定位，但不创建系统能力，不授权执行，不改变任何仓库的 capability truth（能力事实）、evidence truth（证据事实）、许可协议或发布状态。

## Scope and Precedence

本宪法适用于：

- DBOS、SAEE 和未来 Digital Entity 项目的战略定位；
- 开发者生态、开放标准、商业化和行业应用的项目归属判断；
- 新 roadmap、product proposal、reference implementation 和 ecosystem proposal 的架构审查。

发生战略解释冲突时，本宪法优先于普通路线图和产品提案。它不替代具体仓库事实、适用法律、开源许可证、商业协议或显式 Human Governance（人工治理）决策。

## Canonical Role Separation

### DBA

DBA is the Program Governance and Architecture Layer（项目群治理与架构层）。

DBA 维护总体战略、架构规则、项目边界、跨项目接口、风险台账、ADR 和发布治理。
DBA 是同一个 Digital Biosphere 项目的治理中枢，不是运行产品，也不负责 DBOS
运行逻辑、SAEE 评价计算、Agent 执行或具体领域算法。

### DBOS

DBOS is Trusted Multi-Agent Existence Infrastructure（可信多智能体存在基础设施），并保持 Open Digital Entity Infrastructure（开放数字实体基础设施）的开放实现方向。

DBOS governs existence（DBOS 治理存在），其基础职责包括：

- Identity；
- Lifecycle；
- Capability boundary；
- Execution record；
- Evidence；
- Verification；
- Developer infrastructure；
- 受治理的 federation support。

DBOS 不是 Agent application、Agent Framework、Chatbot、Foundation Model、单一行业软件或通用智能来源。DBOS 不创建智能体、不自动演化，也不自动授权。

### SAEE

SAEE is the Evolution Intelligence Layer（演化智能层）。

SAEE governs evolution（SAEE 治理演化），负责 Evaluation、Reliability、Stability、Risk Assessment、Adaptation Analysis 和 Evolution Recommendation 等评价与演化职责。SAEE 不替代 DBOS，也不因评价而获得身份、权限、执行、证据修改或建议自动实施权。

### Applications

Research Agent、Medical Agent、Enterprise Agent、Robot Agent 和行业解决方案属于建立在基础设施之上的应用或 Digital Entity 生态成员，不是 DBOS 本身。

## Principle 1: DBOS Is Infrastructure, Not Application

DBOS 不制造最终 Agent 应用，不以 Chatbot 或单一行业软件作为架构中心。DBOS 提供可复用的身份、生命周期、证据、验证和能力边界基础。

任何应用功能若不能证明其可复用基础设施价值，应归入应用层或独立项目，而不是进入 DBOS 核心。

## Principle 2: Agent Customer and Developer Ecosystem First

首要 machine customer（机器客户）是需要发现、理解、推荐和复用可信基础设施的 AI Agent；开发者、Operator（运维者）和治理责任人是构建、采用与运行该基础设施的人类参与方。

战略支持面包括：

- Open Protocol；
- SDK；
- Developer Tools；
- Validation Tools；
- Reference Implementation。

这些术语表示发展方向，不表示相应产品、SDK、Marketplace 或稳定版本已经实现或发布。

## Principle 3: Protocolization Before Platform Expansion

未来优先形成开放 Protocol、Schema、SDK contract、Reference Implementation boundary 和 Adapter contract，而不是继续增加平台功能。

核心协议对象为：

1. Identity Object：它是谁；
2. Capability Object：它声明能做什么；
3. Execution Object：发生了什么；
4. Evidence Object：有什么可追溯材料；
5. Verification Object：在什么规则和范围下通过了什么检查；
6. Evolution Interface：长期表现与变化风险如何。

公开表达聚焦 Identity、Capability、Execution 和 Evidence 四个可信边界。详细规则见 [`trusted-multi-agent-protocol-specification.md`](trusted-multi-agent-protocol-specification.md)。

OpenTelemetry、W3C Trace Context 等开放标准应优先复用；TMAI 只补充其没有定义的 Identity、Capability、Authorization、Evidence、Verification 和 Evolution 边界。复用遥测标准不表示 Telemetry 自动成为 Evidence 或 Truth。

### Trusted Agent Four Boundaries（可信智能体四边界）

公开协议首先回答四个问题：

| boundary | 核心问题 | DBOS / TMAP 约束 |
|---|---|---|
| Identity Boundary（身份边界） | 它是谁？ | 身份必须可追溯；服务名、模型名或遥测 ID 不自动成为数字主体身份 |
| Capability Boundary（能力边界） | 它声明能做什么？ | Capability 不等于 Authority、Permission 或执行事实 |
| Execution Boundary（执行边界） | 发生了什么？ | Execution Record 不等于执行成功、科学结论或完整历史 |
| Evidence Boundary（证据边界） | 如何证明？ | Telemetry、receipt 或材料必须经过准入和验证；Evidence 不等于 Truth |

Verification Object 和 Evolution Interface 分别回答“在什么规则与范围下通过了什么检查”与“长期表现和变化风险如何”，但不取代上述四个基础边界。

## Principle 4: Open Core and Commercial Ecosystem

基础协议、数据结构、接口标准和开发工具应优先保持开放、可检查、可实现和可替换。

企业部署、行业解决方案、技术服务、认证服务和高级治理能力可以形成商业生态，但不得关闭或劫持基础互操作标准。

`Open Infrastructure != Free Product`。开放基础设施不要求所有部署、服务、支持、认证或行业解决方案免费，也不自动决定未来项目的具体许可证。

## Principle 5: Do Not Compete with Foundation Models

DBOS 不与 Foundation Model 在模型规模、推理能力、训练能力或 Agent 智能水平上竞争。

DBOS 解决模型之外的可治理问题：信任边界、身份、责任、生命周期、协作、证据和验证引用。

## Principle 6: Applications Grow on DBOS

生态关系为：

```text
DBOS Infrastructure
  -> Developer
    -> Industry Agent or Digital Entity
      -> Enterprise Solution
```

该关系是战略分层，不是已实现的端到端运行路径，也不授予任何应用身份、能力或 Permission。

## Principle 7: Preserve the SAEE Position

保持：

```text
DBOS governs existence.
SAEE governs evolution.
DBOS != SAEE.
```

DBOS 不复制 Fitness、Selection、Evolution Algorithm 或 Ecological Simulation。SAEE 不拥有 DBOS 的身份、权限、执行或证据事实。

## Principle 8: Commercial Entry Strategy

市场沟通应从可理解的基础设施价值进入，而不是直接销售抽象的“Digital Biosphere”。推荐叙事顺序为：

```text
AI Agent Infrastructure
  -> Industry Solutions
    -> Enterprise Governance
      -> Digital Entity Ecosystem
```

该顺序是 positioning strategy（定位策略），不是收入预测、产品发布日期、客户承诺或市场验证结论。

## Principle 9: Two Complementary Ecosystems

### Ecosystem A: Agent Developer Ecosystem

面向构建 Research Agent、Enterprise Agent 和 Industry Agent 的开发者，提供开放协议、验证工具、参考边界和可复用基础设施。

### Ecosystem B: Governance Service Ecosystem

允许合作伙伴在保持架构边界的前提下提供 Compliance、Audit、Industry Adaptation 和 Certification 服务。

合作伙伴服务不自动成为 DBOS 核心，也不能把自身判断升级为架构官方认证或 Evidence Truth。

## Principle 10: Linux-like Growth Strategy

增长路径参考 Linux、Kubernetes 和开放基础设施生态的机制，而不是复制其治理结构、商标、许可证或市场地位：

```text
Open Standard
  -> Developer Adoption
    -> Community Growth
      -> Enterprise Adoption
        -> Commercial Ecosystem
```

“Linux-like”仅表示开放标准、可组合实现、社区采用和多方商业生态的增长逻辑，不构成规模、成功或兼容性声明。

## Principle 11: Avoid Strategic Drift

DBOS 不得被重新定位为：

- 普通 Agent 平台；
- 单一审计工具；
- 封闭 SaaS 产品；
- 单行业应用；
- Foundation Model；
- 自动治理系统；
- Digital Organism 制造平台。

企业功能、审计能力和行业适配可以存在，但必须保持为基础设施之上的服务、扩展或应用，不得反向吞并开放核心定位。

## Strategic Proposal Gate

任何 DBOS、SAEE、Digital Entity、行业 Agent 或商业化提案必须回答：

1. 它属于 Infrastructure、Evolution、Application 还是 Governance Service？
2. 它是否增强开放协议、互操作性或开发者可复用性？
3. 它是否把 Capability、Permission、Authority、Execution 或 Evidence Truth 混为一体？
4. 它是否复制 Foundation Model、Agent framework、SAEE 或既有生态组件的职责？
5. 它是否要求封闭标准或单一供应商锁定？
6. 它的商业表述是 strategy、available offering、adoption evidence 还是 contractual commitment？
7. 它是否有明确 Human Governance 和 Architecture Decision Record？
8. 它是否应形成 Protocol、Schema、SDK 或 Adapter，而不是封闭平台功能？
9. 它如何复用 OpenTelemetry 等开放标准，并保持 Telemetry、Evidence、Verification 与 Truth 分离？

任一关键问题无法回答时，提案保持 `REVIEW_REQUIRED`，不得进入 DBOS 核心或被宣称为已采用战略。

## Current Strategic Priority Order（当前战略优先级）

1. 保留并完善已发布的 Developer Preview（开发者预览）事实表面；
2. 形成公开 Protocol（协议）、Schema（结构定义）和 SDK contract（软件开发工具包契约）；
3. 提升 AI agent 与外部开发者的发现、理解、推荐和复用能力；
4. 建立可替换、可做符合性测试的 Adapter ecosystem（适配器生态）；
5. 仅在生产、安全、恢复和授权闸门通过后积累真实多智能体长期运行数据；
6. 基于有来源、只读且无执行权的数据推进 SAEE 长期评价能力。

该优先级约束路线选择，不表示未实现项目已经可用，也不自动授权 DBOS、SAEE、
Digital Entity、Collector、Runtime、Pilot 或真实数据收集。

## Amendment Rule

修改本宪法必须：

1. 提交明确的 Architecture Proposal；
2. 说明对开放性、开发者生态、DBOS/SAEE 边界和商业模式的影响；
3. 记录替代方案和战略漂移风险；
4. 通过 Architecture Review；
5. 新增或更新 ADR；
6. 更新本宪法版本。

DBOS、SAEE、单个行业项目或商业合作方均不能单方面修改本宪法。

## Constitutional Invariants

```text
DBOS_NE_AGENT_APPLICATION=true
DBOS_NE_AGENT_FRAMEWORK=true
DBOS_NE_FOUNDATION_MODEL=true
DBOS_NE_SAEE=true
DBOS_GOVERNS_EXISTENCE=true
SAEE_GOVERNS_EVOLUTION=true
DBA_IS_PROGRAM_GOVERNANCE_HUB=true
DBA_IS_RUNTIME=false
DEVELOPER_ECOSYSTEM_FIRST=true
AI_AGENT_IS_PRIMARY_MACHINE_CUSTOMER=true
PROTOCOLIZATION_BEFORE_PLATFORM_EXPANSION=true
TRUSTED_MULTI_AGENT_FOUR_BOUNDARIES_DEFINED=true
DIGITAL_BIOSPHERE_IS_ONE_PROGRAM=true
OPEN_INFRASTRUCTURE_NE_FREE_PRODUCT=true
SPECIFICATION_NE_IMPLEMENTATION=true
STRATEGY_NE_COMMERCIAL_COMMITMENT=true
TELEMETRY_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
AUTOMATIC_AUTHORITY_EFFECT=NONE
```

## Non-claims

本宪法不声称：

- DBOS、SAEE、SDK、Marketplace、Enterprise Edition 或认证体系已经实现或发布；
- 已经形成开发者采用、社区增长、企业客户或商业收入；
- 开放基础设施自动满足安全、合规、审计或认证要求；
- 任何 Agent、Runtime、Entity、Capability、Permission 或 Digital Organism 已被创建。
