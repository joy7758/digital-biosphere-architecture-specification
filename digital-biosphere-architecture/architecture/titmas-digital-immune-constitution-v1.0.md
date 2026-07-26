---
document_id: DBA-TITMAS-DIGITAL-IMMUNE-CONSTITUTION-1.0
title: TITMAS Digital Immune Constitution v1.0
title_zh: TITMAS 数字免疫宪法 v1.0
version: 1.0.0
status: design-baseline-not-adopted-as-stable-constitution
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: ADR-033
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development design baseline; no implementation, runtime, conformance, adoption, or compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-constitutional-design
architecture_domain: TITMAS
normative_precedence_created: false
implementation_authorized: false
runtime_effect: none
authority_effect: none
---

# TITMAS Digital Immune Constitution v1.0

中文：TITMAS 数字免疫宪法 v1.0。

## 1. Constitutional Status（宪法状态）

本文件是 Digital Immune Constitution（数字免疫宪法）的 `Development` 设计基线。它把
数字免疫方向组织为可审查的底层原则，但尚未升级为 Stable（稳定）规范，也不覆盖
[Digital Biosphere Open Infrastructure Strategy Constitution](open-infrastructure-strategy-constitution.md)、
DBA / DBOS / SAEE 现有职责边界或任何子项目的 canonical truth（规范事实）。

```text
DIGITAL_IMMUNE_CONSTITUTION_DESIGN_BASELINE_DEFINED=true
DIGITAL_IMMUNE_CONSTITUTION_STABLE_ADOPTED=false
SPECIFICATION_NE_IMPLEMENTATION=true
IMMUNE_METAPHOR_NE_RUNTIME_CONTROL=true
AUTHORITY_EFFECT=NONE
```

## 2. Preamble（序言）

未来人工智能生态可能由大量具有身份、能力边界、行为历史、记忆与适应潜力的自治或
半自治数字主体组成。TITMAS 不以制造单一、无限强大的中心智能为目标，而采用已经由
[ADR-032](ADR-032-compositional-scale-over-unbounded-center.md) 固定的组合式规模原则：

> 通过大量职责简单、边界受限、可替换、可验证主体之间的结构化组合，形成更广的系统
> 覆盖能力、适应能力和长期稳定性。

“数字免疫”是对身份识别、边界控制、执行证据、健康观察、风险评价、分级治理和历史
连续性之间关系的架构描述。它不是生物学等同声明，也不是自动控制、自动淘汰、自动
授权或自动演化机制。

## 3. Principle 1: Distributed Complexity Generation

中文：分布式复杂性生成原则。

```text
bounded entity A
  + bounded entity B
  + bounded entity C
  + explicit contracts
  + observable interactions
  -> compositional system capability
```

TITMAS 鼓励职责小、边界清楚、可组合、可替换的主体与服务，不鼓励无限增强单一 Agent、
无限扩大权限或把智能、控制、数据和治理集中到不可替换中心。

组合形成覆盖能力，不表示形成 Truth、正确性、Authority、Permission 或全局控制。

## 4. Principle 2: Digital Identity

中文：主体可识别原则。

任何被视为生态主体的对象都必须能够回答“它是谁”，并具有可追溯的 Identity reference
（身份引用）。身份描述可以包括名称、版本、Owner、目的、生命周期和历史引用，但：

- Repository、Runtime、Agent 名称和模型名不自动等于 Digital Entity Identity；
- Capability 不属于 Identity 的自动权限效果；
- Permission 不由身份自动产生；
- POP 目前只是 Identity / Persona adjacent candidate（身份／人格相邻候选），不是已经
  采纳的 TITMAS 身份权威。

Canonical Entity Identity 继续属于 DBOS existence governance（存在治理）边界。

## 5. Principle 3: Verifiable Action

中文：行为可证明原则。

重要行为应形成可追溯的 Evidence Chain（证据链）：

```text
Intent Reference
  -> Action / Execution Reference
  -> Observation or Record
  -> Evidence Admission
  -> Evidence Object
  -> Verification Result
```

链路中的 Observation、log、trace、receipt、signature 或 certificate candidate 不能绕过
Evidence Admission（证据准入）和 Verification（验证）。

> Evidence proves an execution history within a declared scope; it does not
> prove intelligence correctness or absolute truth.

中文：

> 证据在声明范围内证明执行历史，不证明智能结果正确或绝对真实。

## 6. Principle 4: Bounded Autonomy

中文：边界优先原则。

自治必须由明确边界支撑。每个主体或服务至少需要声明：

- allowed actions（允许行为）；
- limited actions（受限行为）；
- forbidden actions（禁止行为）；
- unknown or unsupported actions（未知或不支持行为）；
- required authorization and context（所需授权与上下文）。

Capability 描述“能够做什么类型的行为”；Authority 描述“有资格决定什么”；Permission
描述“当前上下文是否允许执行”；Execution 描述“实际发生了什么”。四者不得混淆。

## 7. Principle 5: Evidence First

中文：证据优先原则。

TITMAS 不从结果本身直接推导信任：

```text
Execution
  -> Evidence
  -> Verification
  -> bounded trust claim
```

这里的 trust claim（信任声明）必须包含范围、版本、来源、限制和失败状态。Evidence
完整也不等于科学有效、语义正确、合规、客户采用或 Truth。

Agent Evidence、AEO 或 VEC 等名称目前只能作为 candidate evidence / execution-proof
surface（候选证据／执行证明表面）讨论；具体 Owner、Schema、实现和采用状态必须另行
核验和决定。

## 8. Principle 6: Digital Homeostasis

中文：动态平衡原则。

长期生态不应只最大化效率、安全、自由、性能或单一 Fitness 指标。架构评价应显式处理：

- 可靠性与适应性的张力；
- 自由度与约束的张力；
- 局部优化与系统稳定性的张力；
- 资源效率与冗余／恢复能力的张力；
- 创新能力与变更风险的张力。

Homeostasis（稳态）是评价与治理目标，不是一个自动控制器，也不授予 SAEE 执行权。

## 9. Principle 7: Adaptive and Graded Response

中文：免疫响应分级原则。

异常响应不应被压缩成单一的“允许／禁止”。本设计基线定义以下语义级别：

| level | 语义 | 必需边界 |
|---|---|---|
| `L0 NORMAL` | 在当前授权和上下文内正常 | 不产生新权限 |
| `L1 OBSERVE` | 增加观察或复核 | Observation 不自动成为 Evidence |
| `L2 RESTRICT_RECOMMENDED` | 建议收紧范围、频率或资源 | Recommendation 不等于 Decision |
| `L3 ISOLATE_RECOMMENDED` | 建议隔离并进入显式治理审查 | Evaluation 不等于 Authority |
| `L4 RETIRE_RECOMMENDED` | 建议进入撤销／退役决策 | Recommendation 不得自动删除主体或历史 |

SAEE 可以形成风险评价和响应建议；Governance Decision 记录是否采纳；任何运行限制、
隔离、撤销或退役只能由 DBOS 在有效 Authorization（授权）和 Lifecycle（生命周期）
控制下执行并记录。

## 10. Principle 8: Memory Continuity

中文：历史连续性原则。

成功、失败、异常、修复、评价和被采纳的变化都应保留可追溯历史。历史连续性要求：

- 不静默删除失败结果；
- 不用新版本覆盖旧 Evidence 或 Decision；
- 记录版本、来源、时间、上下文和 supersession（取代）关系；
- 区分 Evidence History、Evaluation History、Lifecycle History 与 Reputation input；
- 支持撤销和归档，而不是通过“失忆”抹去责任。

Memory（记忆）不等于无限保存全部数据；数据最小化、隐私、retention（保留期）与合法
删除仍需要独立政策和证据。

## 11. Principle 9: Evolutionary Selection

中文：生态选择原则。

长期评价应基于有来源的表现、适应性、稳定性、Evidence quality 和风险，而不是单次输出
或中心主观声明。Fitness 和 Reputation 只能作为评价输入：

```text
long-term records
  -> SAEE evaluation
  -> Fitness / Risk / Stability / Recommendation
  -> Governance Decision
  -> authorized DBOS lifecycle action, if adopted
```

Fitness 不等于 Authority；Reputation 不等于 Identity、Permission 或 Truth；SAEE 不自动
决定谁被激活、隔离或退役。

## 12. Principle 10: Open Evolution

中文：开放演化原则。

生态必须允许受治理的新主体进入、旧主体退出、规则版本升级和能力迁移。开放演化要求：

- 开放且版本化的 Protocol、Schema 和 Adapter contract；
- 明确的 Admission、Registration、Deprecation、Revocation 和 Retirement 路径；
- 可替换实现与避免供应商锁定；
- 历史版本和失败记录保留；
- 每次 breaking change 都声明兼容、迁移和弃用影响。

“开放”不等于无审查、无边界、自动准入或自动获得 Permission。

## 13. Five-layer Interpretive Map（五层解释映射）

```text
Digital Biosphere Program
  -> Open Infrastructure Strategy Constitution
    -> TITMAS Digital Immune Constitution design baseline
      -> Identity | Boundary | Evidence | Health | Reputation inputs
        -> governed Agent / Digital Entity ecosystem
          -> read-only evaluation and governed evolution
```

这里的五个词是设计视角，不是五个已实现系统：

| design surface | 当前规范 Owner / 边界 |
|---|---|
| Identity | DBOS canonical existence boundary；POP 仅候选映射 |
| Boundary | Capability / Authorization / Permission / Context 分离 |
| Evidence | DBOS canonical Evidence boundary；外部证据组件需准入 |
| Health | Observation / evaluation interface candidate；不等于控制权 |
| Reputation | 长期评价输入；不等于身份、权限或 Truth |

## 14. Existing Project Crosswalk Candidate（现有项目交叉映射候选）

本表只用于后续 Architecture Review，不改变项目事实或 Portfolio admission（项目组合
准入）：

| project or term | candidate constitutional role | current truth boundary |
|---|---|---|
| POP | identity / persona input | `MAPPING_ONLY_REVIEW_REQUIRED` |
| Agent Evidence / AEO | evidence input / handoff | 不自动成为 DBOS canonical Evidence |
| VEC | execution proof candidate | 名称不证明实现、证书或认证已存在 |
| SAEE | health、risk、stability 与 evolution evaluation | 只读评价与建议；没有执行权 |
| Agent Health | health interface candidate | 具体仓库、Owner 和实现状态需独立核验 |
| ARO | audit / governance-response input candidate | Audit 不等于 Verification、Decision 或 Execution |
| TEK-Bench | stress / evaluation candidate | Benchmark 不自动形成产品或生态事实 |
| DBL | evolution experiment candidate | Experiment 需要独立授权；结果不能外推为生态规律 |

## 15. Minimum Digital Immune Subject Candidate（最小数字免疫主体候选）

未来 Digital Immune Cell Specification（数字免疫细胞规范）可以评审以下最小组合：

```text
Identity
  + Capability and Policy Boundary
  + Execution / Evidence Interface
  + Health Observation Interface
  + Memory Continuity
  + Reputation Input Boundary
```

该组合仍必须复用
[Digital Entity Specification](digital-entity-specification.md) 与
[Capability Boundary Specification](capability-boundary-specification.md)，不能创建第二套
Entity Identity、Capability、Evidence、Lifecycle 或 Permission 权威。

## 16. Proposal Gate（提案闸门）

任何数字免疫相关 Proposal 必须回答：

1. 它是观察、评价、建议、决策、授权还是执行？
2. 它的 canonical Owner 是 DBA、DBOS、SAEE、Governance Decision 还是应用层？
3. 它是否把 Evidence、Verification、Reputation 或 Fitness 提升为 Truth 或 Permission？
4. 它是否让 SAEE、Health service 或协调组件成为隐藏控制中心？
5. 它能否拆分为简单、受限、可替换、可单独验证的组件？
6. 分级响应的每一级由谁建议、决定、授权、执行和记录？
7. 如何保留失败、撤销、历史和隐私／retention 边界？
8. 是否重复现有 Digital Entity、Capability、Evidence、Lifecycle 或 Governance Decision？

任一问题未解决时保持 `REVIEW_REQUIRED`，不得创建实现任务或 runtime effect。

## 17. Non-claims（非声明）

本设计基线不声称：

- Digital Immune System、Digital Immune Cell、Agent Passport、Health Protocol、
  Reputation System、AEO 或 VEC 已实现或采纳；
- POP、Agent Evidence、ARO、Agent Health、TEK-Bench 或 DBL 已进入核心 Portfolio；
- SAEE 能够自动限制、隔离、淘汰、授权或修改 DBOS 状态；
- DBOS 能够自动扩大 Capability、Permission 或执行未授权响应；
- 任何 Agent、Entity、Runtime、Capability、Permission、Evidence Truth、Certificate、
  Certification、实验或生产系统被创建。

```text
DIGITAL_IMMUNE_SYSTEM_IMPLEMENTED=false
DIGITAL_IMMUNE_CELL_SPECIFICATION_DEFINED=false
DIGITAL_IMMUNE_CELL_CREATED=false
AGENT_PASSPORT_DEFINED=false
HEALTH_PROTOCOL_DEFINED=false
REPUTATION_SYSTEM_DEFINED=false
IMMUNE_RESPONSE_EXECUTION_AUTHORIZED=false
SAEE_AUTOMATIC_CONTROL_AUTHORITY=false
REPUTATION_GRANTS_PERMISSION=false
EVIDENCE_PROVES_INTELLIGENCE_CORRECTNESS=false
```
