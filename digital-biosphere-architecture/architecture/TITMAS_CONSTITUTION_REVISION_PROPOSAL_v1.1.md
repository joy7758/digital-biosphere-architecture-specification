---
document_id: DBA-TITMAS-CONSTITUTION-REVISION-PROPOSAL-1.1
title: TITMAS Constitution Revision Proposal v1.1
title_zh: TITMAS 宪法修订提案 v1.1
status: PROPOSAL_COMPLETE_HUMAN_DECISIONS_REQUIRED
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
proposal_type: DOCUMENTATION_AND_ARCHITECTURE_GOVERNANCE
source_constitution_ref: architecture/titmas-digital-immune-constitution-v1.0.md
source_constitution_status: DEVELOPMENT_CONSTITUTION_CANDIDATE
proposed_successor_version: 1.1
proposed_successor_title: HUMAN_DECISION_REQUIRED
created_at: 2026-07-28
human_decision_status: PENDING
decision_reference: NOT_DECIDED
normative_effect: NONE
authority_effect: NONE
implementation_effect: NONE
schema_effect: NONE
protocol_effect: NONE
runtime_effect: NONE
repository_effect: NONE
external_action_effect: NONE
---

# TITMAS Constitution Revision Proposal v1.1

中文：TITMAS 宪法修订提案 v1.1。

## 0. Proposal boundary（提案边界）

本文件只提出如何修订现有
[`TITMAS Digital Immune Constitution v1.0`](titmas-digital-immune-constitution-v1.0.md)。
它不是 v1.1 宪法正文，不修改 v1.0，不采纳新原则，不建立新层级、Cockpit（驾驶舱）、
Authority（权威）、Schema（模式）、Protocol（协议）、Runtime（运行时）或
Implementation（实现）。

本提案的目标是把已有思想转换为可审查、可约束后续设计的规则，同时防止候选宪法通过
标题、比喻或能力描述反向获得尚未被授予的权力。

```text
PROPOSAL_CREATED=true
SOURCE_CONSTITUTION_MODIFIED=false
CONSTITUTION_V1_1_CREATED=false
CONSTITUTION_V1_1_ADOPTED=false
CONSTITUTION_V1_1_FROZEN=false
HUMAN_DECISION_STATUS=PENDING
IMPLEMENTATION_AUTHORIZED=false
```

### 0.1 Proposal sources（提案来源）

主要来源：

- [`TITMAS Architecture Decision Record v0.1`](TITMAS_ARCHITECTURE_DECISION_RECORD_v0.1.md)；
- [`TITMAS Digital Immune Constitution v1.0`](titmas-digital-immune-constitution-v1.0.md)；
- [`Digital Biosphere Program Governance Charter`](../PROGRAM-CHARTER.md)；
- [`Digital Biosphere Open Infrastructure Strategy Constitution`](open-infrastructure-strategy-constitution.md)；
- [`ADR-016: Program Governance Cockpit`](ADR-016-program-governance-cockpit.md)；
- [`ADR-032: Compositional Scale Over an Unbounded Center`](ADR-032-compositional-scale-over-unbounded-center.md)；
- [`ADR-033: Attention Principle for Dynamic Coordination`](ADR-033-attention-principle-for-dynamic-coordination.md)；
- [`TITMAS Integrity Review`](titmas-integrity-review-v0.1.md)；
- [`Authority Freeze Decision Record`](authority-freeze-decision-record-v0.1.md)；
- [`TITMAS Interface Readiness Review`](titmas-interface-readiness-review-v0.1.md)；
- `/Users/zhangbin/GitHub/agent-evidence/TITMAS_CURRENT_STATE_REPORT.md`。

### 0.2 Change labels（修订标签）

| 标签 | 含义 |
|---|---|
| `KEEP` | 保留原意，只做必要澄清 |
| `PROMOTE` | 原意已存在，提升为更显式的前置原则 |
| `ADD` | 新增规范候选文本 |
| `REWRITE` | 保留目标，但替换可能越权、重复或虚构能力的表述 |
| `MOVE_TO_NON_NORMATIVE` | 只作为解释性附录或示意，不产生 Owner、Authority 或运行语义 |
| `DEFER` | 等待事实、Owner、接口或人类决定 |
| `REMOVE` | 建议从规范正文删除，不进入 v1.1 |
| `HUMAN_DECISION_REQUIRED` | 本提案不代替人类作出选择 |

## 1. Pre-development recommendation gate（开发前推荐闸门）

如果潜在用户需要“让多个自主智能体在没有超级中心的情况下保持边界、证据和治理秩序”，
本轮是否会推荐当前方向？

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CONSTITUTION_REVISION_AND_BOUNDARY_GOVERNANCE_PROPOSAL
NOT_RECOMMENDED_AS=IMPLEMENTED_TITMAS_RUNTIME_OR_AUTOMATIC_IMMUNE_SYSTEM
```

条件推荐的原因：

- 已采纳的 Program Charter、ADR-016 和 ADR-032 已提供 compositional scale
  （组合式规模）、单一 DBA Cockpit 和权力分离基础；
- v1.0 已覆盖 Identity、Evidence First、bounded autonomy、homeostasis、memory、
  adaptive response 和 evolution，不需要重新发明；
- 本提案可以把重复建设、语义抬升和自动响应风险变成显式停止条件。

当前不推荐实现的原因：

- v1.0 仍是 `DEVELOPMENT_CONSTITUTION_CANDIDATE`；
- `AUTHORITY_FREEZE_ADOPTED=false`；
- TITMAS Interface v0.1 尚未就绪；
- `agent-health`、`titmas-health` 和两套 integrations 的归属尚未决定；
- Agent Health 当前可核验能力是本地静态仓库诊断，不是行为／权限漂移的运行时检测系统；
- Cockpit 已由 ADR-016 归属 DBA，不允许形成第二驾驶舱。

推荐结论不产生实现授权。

## 2. Constitutional title and precedence（标题与位阶）

### 2.1 Identified conflict（已识别冲突）

用户建议将后继标题改为：

```text
TITMAS Digital Biosphere Constitution v1.1
```

该名称存在 material authority risk（实质权力风险）：

1. `Digital Biosphere Open Infrastructure Strategy Constitution v0.4` 已是
   `ADOPTED_STRATEGIC_CONSTITUTION`；
2. DBA Program Charter 已将 Digital Biosphere 定义为总项目，并把 TITMAS 定位为 DBA
   下的拟议互操作架构域；
3. 一份仍处于 Development 的 TITMAS 文件使用 `Digital Biosphere Constitution`，
   会产生同位“第二宪法”外观；
4. 标题扩大还可能被误读为 TITMAS 高于 DBA、DBOS 和 SAEE 的 canonical boundary。

### 2.2 Title options requiring human decision（标题选项）

| 选项 | 标题 | 影响 | 本提案建议 |
|---|---|---|---|
| `A` | `TITMAS Digital Immune Constitution v1.1` | 作为既有候选的直接后继，保持 scope 和 lineage | **推荐** |
| `B` | `TITMAS Digital Immune Governance Constitution v1.1` | 更强调治理约束，但仍需确认是否改变公开命名 | 可考虑 |
| `C` | `TITMAS Digital Biosphere Constitution v1.1` | 与已采纳战略宪法和 Digital Biosphere 总项目位阶冲突 | 当前不推荐 |
| `D` | 合并为单一 Digital Biosphere Constitution 新主版本 | 需要明确 supersession、迁移、ADR、全项目 Owner review | 不是本次 v1.1 增量修订 |

```text
PROPOSED_SUCCESSOR_TITLE=HUMAN_DECISION_REQUIRED
DEFAULT_RECOMMENDATION=OPTION_A
TITLE_CHANGE_DOES_NOT_CREATE_PRECEDENCE=true
```

若人类选择 `C` 或 `D`，必须先单独决定：

- 哪份宪法是 canonical；
- 哪份被 supersede、保留或降为附录；
- DBA、DBOS、SAEE、TITMAS 的适用 scope；
- amendment authority、版本和冲突规则；
- 是否需要修改 Program Charter 与既有 ADR。

这些决定不属于本提案。

## 3. Clause disposition matrix（条款处置矩阵）

| v1.0 内容 | v1.1 处置 | 说明 |
|---|---|---|
| Status and Interpretation | `KEEP + REWRITE` | 增加 precedence、标题 scope、Candidate/Adopted/Implementation 独立状态 |
| Preamble | `KEEP` | 保留大量有限主体组合的长期方向 |
| Distributed Complexity Generation | `PROMOTE + MERGE` | 提升为 Principle 0；避免与原 Principle 1 重复两次 |
| Attention Principle | `ADD_AS_BOUNDED_EXTENSION` | 继承父级 Constitution v0.4；动态选择候选参与者，不创建中央控制、Authority、Permission 或 Truth |
| Digital Identity | `KEEP + CLARIFY` | DBOS canonical；POP 仅 reference，不是身份 Authority |
| Verifiable Action | `KEEP + CLARIFY` | 区分 observation、candidate package、validation、DBOS admission 和 canonical verification |
| Bounded Autonomy | `KEEP` | 增加 Authority Separation 的引用 |
| Evidence First | `KEEP` | 增加 Cockpit observation 与 Truth 的非抬升规则 |
| Digital Homeostasis | `KEEP + CLARIFY` | 明确是评价目标，不是控制器 |
| Adaptive Response Level 0–4 | `REWRITE` | 归入 Adaptive Immune Capability candidate；增加 decide/execute/review/revoke 责任 |
| Memory Continuity | `KEEP + REWRITE` | 禁止新建第二 Immune Memory truth store；增加可申诉和更正 |
| Evolutionary Selection | `KEEP + CLARIFY` | SAEE recommendation、Human Decision、authorized execution、DBOS record 分离 |
| Open Evolution | `KEEP` | 保留版本、准入、权限和历史分离 |
| Constitutional Architecture Map | `REWRITE` | 替换为五层 constraint view；箭头不表示控制、代码依赖或 Authority 继承 |
| Existing Project Crosswalk | `KEEP + UPDATE` | 加入 DBA Cockpit view、Agent Health 当前能力和 Owner 状态 |
| Digital Cell normative implication | `MOVE_TO_NON_NORMATIVE` | 在差异与 Owner 未决定前只保留比喻 |
| Health / Reputation as equal surfaces | `DEFER + REWRITE` | Health 分为静态 diagnosis 与 SAEE evaluation；Reputation 继续保持 contestable candidate |
| Constitutional Review Gate | `KEEP + EXPAND` | 增加标题、Cockpit、重复组件和 capability-truth 检查 |
| Non-effects | `KEEP + EXPAND` | 明确 no code/schema/protocol/cockpit/runtime/implementation |

## 4. Proposed Principle 0: Ecological Self-Limitation

### 4.1 Classification（分类）

```text
CHANGE_CLASS=PROMOTE_AND_RESTATE
NEW_AUTHORITY_CREATED=false
SOURCE_PRINCIPLES=PROGRAM_CHARTER_2A+ADR_032+V1_0_PREAMBLE+V1_0_PRINCIPLE_1
```

Ecological Self-Limitation（生态自限）不是全新思想。它已经存在于 v1.0 序言和
Distributed Complexity Generation，并由 `ADR-032` 在 Digital Biosphere 层采纳。
v1.1 的价值是把它提升为所有后续条款的显式前置约束。

### 4.2 Proposed wording（候选文本）

> **Principle 0 — Ecological Self-Limitation**
>
> TITMAS does not pursue a single omnipotent control center. It achieves
> system-level complexity through the governed cooperation of limited,
> autonomous, replaceable, and verifiable entities and services.
>
> TITMAS specifications may define bounded observation, coordination,
> verification, and handoff contracts. They do not create an entity that
> controls all agents, aggregate Authority by composition, or become a
> canonical Truth source.

中文候选：

> **第一原则之前置原则——生态自限**
>
> TITMAS 不以建立单一、全能控制中心为目标，而通过有限、自治、可替换、可验证主体与
> 服务之间受治理的协作形成系统级复杂能力。
>
> TITMAS 规范可以定义有界的观察、协调、验证与交接契约；它不因此创建控制所有 Agent
> 的主体，不因组合而聚合 Authority，也不成为 canonical Truth source。

必须同时保留：

```text
SIMPLE_ENTITY_NE_UNGOVERNED_ENTITY=true
COMPOSITION_NE_AUTHORITY_AGGREGATION=true
COORDINATION_NE_UNBOUNDED_CENTER=true
COVERAGE_NE_CORRECTNESS_OR_TRUTH=true
EMERGENT_CAPABILITY_NE_AUTOMATIC_PERMISSION=true
```

“TITMAS 观察、协调、验证”只能表示规范定义了相应契约，不表示 TITMAS 已存在一个执行
这些动作的中心 Runtime。

## 5. Proposed five-layer life structure（五层生命结构提案）

### 5.1 Normative warning（规范警告）

五层结构适合作为 constraint and responsibility view（约束与职责视图），不应被写成：

- Runtime 调用栈；
- 仓库所有权树；
- 上层控制下层的 Authority 链；
- 数据必须逐层流经的 pipeline；
- 五个必须新建的软件系统。

建议在 v1.1 中标记为 `EXPLANATORY_WITH_NORMATIVE_BOUNDARIES`：层名用于解释，表中
Owner 和 non-effects 才是约束内容。

### 5.2 Revised five-layer view（修订后的五层视图）

```text
Layer 0 — Constitutional Constraint
  adopted DBA charter / strategic constitution / ADR
  + adopted TITMAS-domain constitution, if later decided

Layer 1 — Identity and Existence
  DBOS canonical identity / capability / lifecycle boundary
  + POP reference or projection, only if explicitly mapped

Layer 2 — Execution and Evidence
  DBOS canonical execution / evidence admission / verification
  + agent-evidence candidate capture / package / local validation / export

Layer 3 — Health and Evaluation
  agent-health bounded local repository diagnosis
  + SAEE protected evaluation / stability / risk / evolution recommendation
  (distinct responsibilities, not one merged engine)

Layer 4 — Governed Response and Evolution
  Human or explicitly delegated decision
  -> separately authorized executor
  -> DBOS lifecycle / execution record when applicable
  -> new observation and evaluation cycle
```

### 5.3 Non-normative biological crosswalk（非规范生命类比）

| 生命类比 | 可用于解释 | 不得推导 |
|---|---|---|
| DNA | 已采纳的宪法约束和版本化规则 | 代码自动执行、不可修改的绝对法、TITMAS 高于 DBA |
| 细胞身份 | DBOS existence/identity boundary；POP reference candidate | POP 是认证或 Permission Authority |
| 代谢记录 | execution observation、evidence candidate、lineage | 所有日志都是 Evidence、Evidence 是 Truth |
| 免疫系统 | bounded detection/memory/adaptation capability pattern | `agent-health` 已是运行时免疫系统或可自动杀伤 |
| 医生检查 | SAEE method-bound evaluation 的解释类比 | SAEE 能批准、治疗、执行或写回 |
| 进化 | recommendation、Human Decision、authorized change 和新证据循环 | 自动优化、自我改写、自动淘汰 |

```text
BIOLOGICAL_METAPHOR_NE_CANONICAL_OWNER=true
BIOLOGICAL_METAPHOR_NE_AUTHORITY=true
BIOLOGICAL_METAPHOR_NE_IMPLEMENTATION=true
LAYER_ORDER_NE_RUNTIME_CONTROL_FLOW=true
```

## 6. Proposed Authority Separation Principle（权力分离原则）

### 6.1 Proposed constitutional rule（候选宪法规则）

任何单一 Agent、模型、Cockpit、validator、health engine 或 evaluation system，不得仅因
技术上能够完成多个步骤，就同时获得 Observation、Evaluation、Authorization 和
Execution 的不受限权力。

用户提出的简化循环可以保留为：

```text
Observe
  -> Evaluate
    -> Authorize
      -> Execute
        -> Verify
```

规范正文应使用更精确的循环：

```text
Observe
  -> preserve source and limitations
    -> package / validate, when applicable
      -> admit / verify canonical record, when applicable
        -> evaluate and recommend
          -> authorize through explicit decision
            -> execute within granted scope
              -> record / independently verify result
                -> begin a new observation cycle
```

### 6.2 Responsibility separation（责任分离）

| 阶段 | 候选责任方 | 可产生 | 不可产生 |
|---|---|---|---|
| Observe | source system、`agent-evidence` capture、`agent-health` scan、DBA read-only view | source-bound observation | Truth、Permission、Decision |
| Package / validate | `agent-evidence` / EEOAP validator | candidate bundle、scoped receipt、limitations | DBOS admission、Certification |
| Admit / canonical verify | DBOS applicable Owner/process | canonical scoped record/status | absolute Truth、SAEE Fitness |
| Evaluate | SAEE；或 `agent-health` 对本地仓库的窄诊断 | method-bound finding/recommendation | Approval、Command、writeback |
| Authorize | Human Decision Authority 或显式、有限委托 | scope、reason、expiry、revocation 和 decision ref | 执行已经完成的事实 |
| Execute | Codex 或其他被明确授权的 target executor | 有界状态变化和 execution record | 扩大授权、改写旧 evidence |
| Verify / review | 与风险相称的独立 verifier/reviewer；适用时 DBOS record | scoped result、failure、unknown、new evidence | 自动关闭所有 gate |

Codex 只是可能的 executor example（执行者示例），不是宪法固定的唯一执行层。

### 6.3 Separation invariants（分权不变量）

```text
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VALIDATION_NE_DBOS_ADMISSION=true
EVALUATION_NE_AUTHORITY=true
RECOMMENDATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
EXECUTION_NE_VERIFIED_SUCCESS=true
VERIFICATION_NE_PERMISSION=true
```

## 7. Proposed Adaptive Immune Capability boundary（自适应免疫能力边界）

### 7.1 Definition status（定义状态）

Adaptive Immune Capability 应定义为 cross-component capability pattern（跨组件能力模式），
不是新产品、项目、Runtime、Authority 或 `agent-evidence` 子目录。

```text
ADAPTIVE_IMMUNE_CAPABILITY_STATUS=CONSTITUTIONAL_PATTERN_CANDIDATE
ADAPTIVE_IMMUNE_RUNTIME_IMPLEMENTED=false
AUTOMATIC_RESPONSE_AUTHORIZED=false
```

### 7.2 Detection（检测）

候选目标可以包括：

- repository configuration or dependency change；
- evidence absence、staleness、conflict 或 validation failure；
- observed behavior drift；
- capability、permission 或 authority drift。

能力事实必须分开：

| 检测类型 | 当前可核验状态 |
|---|---|
| 本地静态 repository-health diagnosis | `agent-health` 的当前窄产品面 |
| completed-operation evidence candidate validation | `agent-evidence` 的当前窄参考面 |
| behavior drift runtime detection | `NOT_ESTABLISHED_BY_THIS_PROPOSAL` |
| permission/authority drift runtime detection | `NOT_ESTABLISHED_BY_THIS_PROPOSAL` |
| ecosystem-wide anomaly detection | `NOT_ESTABLISHED_BY_THIS_PROPOSAL` |

宪法可以要求“未来检测必须保留来源、范围、方法和未知”，不能把候选目标写成现有能力。

### 7.3 Memory（记忆）

用户给出的：

```text
event / cause / response / result
```

可以作为 conceptual minimum（概念最小集），但不得在本提案中变成 JSON Schema。建议
v1.1 要求未来记录至少能够引用：

- event and observation reference；
- source、subject、time 和 version；
- hypothesized cause 与 confidence；
- decision and authorization reference；
- response and executor reference；
- result、verification scope 和 limitations；
- correction、supersession、retention 和 privacy status。

Memory 不建立第二 Truth store：

```text
observation/evidence lineage -> applicable DBOS or project-local canonical boundary
health finding             -> agent-health scoped artifact
evaluation result          -> SAEE scoped, versioned recommendation artifact
program projection         -> DBA reference-only Cockpit view
```

同一事件可以有相互引用的不同工件，但不能被一个新的 “Immune Memory” 数据库静默合并为
全局事实。

### 7.4 Adaptation（适应）

适应必须表示：

```text
detected condition
  -> scoped finding
    -> recommendation
      -> explicit authorization
        -> bounded change
          -> new execution/evidence
            -> later evaluation
```

它不表示模型自我修改、权限自我扩大、规则自动升级或主体自动淘汰。

### 7.5 No automatic harm（禁止自动杀伤）

```text
DETECTION_NE_RESTRICTION=true
DETECTION_NE_ISOLATION=true
DETECTION_NE_RETIREMENT=true
HEALTH_SCORE_NE_PERMISSION=true
SAEE_RECOMMENDATION_NE_COMMAND=true
AUTOMATIC_KILL_OR_DISABLE_AUTHORIZED=false
```

限制、隔离、关闭、撤权、退役或删除只有在存在明确 Authority、对象、理由、证据范围、
最小必要性、期限、rollback、复核和申诉条件时才可进入单独决定。当前宪法提案不创建
这种授权。

## 8. Proposed TITMAS Cockpit role（TITMAS 态势视图）

### 8.1 Existing canonical decision（既有规范决定）

`ADR-016` 已将 DBA 采纳为 Digital Biosphere Program Governance and Architecture
Cockpit。TITMAS Integrity Review 明确禁止 TITMAS 建立第二驾驶舱或状态 Truth source。

因此不建议在 v1.1 中创建名为 `TITMAS Cockpit` 的独立实体、项目、服务或 Authority。

### 8.2 Recommended wording（建议表述）

建议使用：

```text
TITMAS Situational View within the DBA Cockpit
DBA 驾驶舱中的 TITMAS 态势视图
```

候选定义：

> A bounded, reference-only situational awareness view for TITMAS-related
> Digital Biosphere governance within the DBA Cockpit.

中文：

> DBA 驾驶舱中面向 TITMAS 相关数字生物圈治理的有界、仅引用态势感知视图。

### 8.3 Allowed and prohibited responsibilities（允许与禁止职责）

| 可以 | 不可以 |
|---|---|
| 聚合带 source、observed_at、version 和 freshness 的引用 | 复制子项目 ledger 成为第二事实源 |
| 展示 `UNKNOWN`、`STALE`、`CONFLICTED`、失败和风险 | 隐藏失败或把旧观察显示为当前事实 |
| 展示 Agent Evidence、Agent Health、SAEE 等已核验状态摘要 | 把 observation 升级为 Evidence Truth |
| 展示 recommendation 和待决事项 | 批准、授权或关闭 gate |
| 支持人类定位 canonical source 和 decision queue | 修改 Agent、Permission、DBOS 或 SAEE |
| 提供 agent-readable discovery | 执行命令、成为 Runtime control plane |

推荐视图：

```text
DBA Cockpit
  |
  +-- TITMAS Situational View
        |
        +-- source-bound Evidence references
        +-- repository Health findings
        +-- SAEE evaluation references, if authorized and available
        +-- risks / unknowns / decisions required
```

这里不是 `Raw Facts -> Cockpit Truth`。所有数据继续由各 canonical source 所有，视图只做
reference-only aggregation。

```text
TITMAS_SECOND_COCKPIT_CREATED=false
TITMAS_COCKPIT_AUTHORITY_CREATED=false
DBA_REMAINS_SINGLE_PROGRAM_GOVERNANCE_COCKPIT=true
SITUATIONAL_VIEW_NE_TRUTH_SOURCE=true
SITUATIONAL_VIEW_NE_RUNTIME=true
```

本提案不设计 UI、API、database、dashboard schema 或同步 adapter。

## 9. Proposed No Duplicate Component Principle（禁止重复组件原则）

### 9.1 Constitutional rule（候选规则）

新增组件不是默认动作。任何新项目、模块、Schema、validator、adapter、Cockpit、memory
store、health engine 或 evaluation surface，必须先证明已有职责无法通过复用、扩展、映射
或有界适配满足。

### 9.2 Mandatory review questions（强制问题）

至少回答用户提出的五个问题：

1. 是否已有类似组件？
2. 是否产生新的 Authority？
3. 是否产生新的 Truth source？
4. 是否复制已有 Schema 或 validation logic？
5. 是否增加维护成本？

并补充：

6. canonical Owner、source、version 和 lifecycle 是什么？
7. 新能力增量能否由现有组件加 bounded adapter 实现？
8. 是否产生新的 secret、PII、security、privacy 或 supply-chain surface？
9. failure、unknown、partial、conflict、stale 和 rollback 如何处理？
10. 停止、替换、归档和迁移路径是什么？

### 9.3 Decision outcomes（审查结果）

```text
REUSE_EXISTING
EXTEND_EXISTING
CREATE_BOUNDED_ADAPTER_CANDIDATE
REQUEST_EXISTING_COMPONENT_DISPOSITION
CREATE_NEW_COMPONENT_CANDIDATE
REJECT
```

默认优先顺序：

```text
reuse
  -> clarify boundary
    -> extend
      -> bounded adapter
        -> new component candidate
```

“增加复杂度 > 增加能力”不能由没有定义的单一分数自动判定。提案必须列出 capability
delta、maintenance delta、authority delta、truth-source delta 和 exit cost，由适用 Owner
和 Human Architecture Decision 作有范围的决定。

审查结果不自动删除、合并、归档或迁移现有项目。

## 10. Proposed v1.1 outline（候选目录）

以下只提供后继文档结构，不创建 v1.1：

```text
0. Status, Scope and Precedence
Preamble
Principle 0. Ecological Self-Limitation
Principle 1. Distributed and Compositional Capability
Principle 1A. Attention and Dynamic Coordination
Principle 2. Digital Identity and Existence Boundary
Principle 3. Verifiable Action
Principle 4. Bounded Autonomy
Principle 5. Evidence First
Principle 6. Authority Separation
Principle 7. Digital Homeostasis
Principle 8. Adaptive Immune Capability Boundary
Principle 9. Memory Continuity
Principle 10. Governed Evolution
Principle 11. Open Evolution
Principle 12. No Duplicate Component
Five-Layer Constraint and Responsibility View
DBA Cockpit TITMAS Situational View
Existing Project Crosswalk
Constitutional Review and Amendment Gate
Non-effects
Non-normative Biological Metaphor Appendix
```

原 v1.0 Principle 1 与新的 Principle 0 内容重叠。正式起草时应让 Principle 0 规定
non-negotiable constraint（不可突破约束），Principle 1 只说明组合设计后果，避免同一原则
重复两次。

## 11. Suggested removals and deferrals（删除与延后建议）

### 11.1 Remove from normative body（建议从规范正文删除）

- 独立 `TITMAS Cockpit` 实体、项目或 Authority；
- `TITMAS -> controls all agents` 或等价层级图；
- 五层之间的强制运行时调用箭头；
- 固定的 Immune Memory JSON Schema；
- 把 `agent-health` 写成已实现的 runtime immune monitor；
- 把 SAEE 写成能够批准、治疗、修复或执行的“医生”；
- 把 POP 写成 canonical identity、authentication 或 Permission system；
- 把 `Digital Cell` 当作已采纳 Entity type；
- 把 Detection 直接连接到 automatic restrict/isolate/retire；
- 把 v1.1 文档采纳写成 Interface 或 Implementation authorization。

### 11.2 Defer pending decision or evidence（等待决定或证据）

- 是否改变宪法标题和顶层 scope；
- `Digital Cell` 是否有独立规范价值；
- `agent-health` 是否是唯一 Agent Immune 产品；
- `titmas-health` 的 archive/successor/adapter/stop disposition；
- behavior drift 和 permission drift 的真实检测 Owner；
- Memory 的 canonical storage、retention 和 privacy contract；
- Level 2–4 response 的决定、执行、复核与撤销 Authority；
- TITMAS situational view 是否需要未来只读 adapter；
- Reputation 是否进入后继宪法，及其申诉、纠正和去标记规则。

## 12. Human decisions required（需要人工决定）

| ID | 人工决定 | 推荐默认值 | 决定不自动授权 |
|---|---|---|---|
| `CR-D01` | v1.1 标题与 scope | 保持 `TITMAS Digital Immune Constitution v1.1` | 实现、发布 |
| `CR-D02` | Principle 0 是否按候选文本进入 v1.1 | `ACCEPT_WITH_REFINEMENT` | 新 Authority |
| `CR-D03` | 五层结构是规范层还是解释视图 | `EXPLANATORY_WITH_NORMATIVE_BOUNDARIES` | 五个系统 |
| `CR-D04` | Authority Separation 的角色与委托模型 | 接受分离原则，委托细节后续决定 | Permission、账号权 |
| `CR-D05` | Adaptive Immune 是 pattern、规范域还是产品名 | `CROSS_COMPONENT_CAPABILITY_PATTERN` | Runtime |
| `CR-D06` | Detection/Memory/Adaptation 的 canonical Owner | 分项决定，不创建 family-level Owner | 数据库、Schema |
| `CR-D07` | Cockpit 命名与归属 | DBA Cockpit 内的 TITMAS Situational View | 第二驾驶舱、UI/API |
| `CR-D08` | No Duplicate Component gate 的决定者和例外规则 | DBA review + applicable Owner + Human Decision | 自动删除／合并 |
| `CR-D09` | `agent-health` / `titmas-health` 处置 | `REVIEW_REQUIRED` | archive、merge、license change |
| `CR-D10` | v1.1 的 Accepted/Frozen/maturity 状态 | 证据齐备后单独决定 | Interface、Implementation |

所有决定必须记录：

```yaml
decision_id:
decision:
decided_by_ref:
decided_at:
scope:
source_refs: []
supersedes:
validity:
revocation:
implementation_authorized: false
external_action_authorized: false
```

本表不是 Decision Record。

## 13. Amendment and validation gate（修订与验证闸门）

只有在 `CR-D01` 至适用决定获得明确处理后，才建议起草 v1.1 正文。正文审查至少检查：

1. 与 Program Charter、Strategic Constitution、ADR-016、ADR-032、ADR-033 一致；
2. 不产生第二 Constitution、DBA、Cockpit 或 Truth source；
3. 不覆盖 DBOS canonical existence/evidence boundary；
4. 不暴露或复制 SAEE core，不创建 writeback；
5. 不把 `agent-evidence` validation 升级为 DBOS admission；
6. 不把 Agent Health 静态诊断升级为 runtime immunity；
7. 每项 capability 都标记 `CURRENT`、`CANDIDATE`、`NOT_ESTABLISHED` 或
   `NOT_ASSESSED`；
8. 所有生物类比都带 non-normative boundary；
9. 删除、重复、unknown、conflict 和反方意见得到保留；
10. 正文明确 `SPECIFICATION_NE_IMPLEMENTATION=true`。

通过文档审查仍不自动允许：

- Schema 或 Protocol 变化；
- Interface freeze；
- adapter、Cockpit、dashboard 或 Runtime 开发；
- Agent Health / SAEE / DBOS / Agent Evidence 改动；
- Self-Governance Experiment；
- commit、push、release、publication 或 public adoption claim。

## 14. Auxiliary agent review（辅助智能体审查）

本轮通过用户指定的安全环境变量路径调用：

- `qwen3.7-max`：主架构审查；
- `deepseek-v4-pro`：反方审查。

没有读取、复制、记录或回显 API Key。模型输出只作为 advisory review。

Qwen 正确支持：

- 保留 Principle 0、Authority Separation、候选能力标签和人工决定 gate；
- 不把未核验能力混入当前能力事实。

未采纳 Qwen 的以下建议：

- 认为改名 `Digital Biosphere Constitution` 无实质冲突；
- 把 `TITMAS Cockpit` 当作新实体；
- 对部分新增架构给出“有条件实现授权”。

这些建议与本地已核验的已采纳战略宪法、ADR-016 和
`AUTHORITY_FREEZE_ADOPTED=false` 冲突。

DeepSeek 正确识别：

- 第二宪法；
- 第二驾驶舱；
- Adaptive Immune 能力虚构；
- 通过比喻和界面产生隐性 Authority 漂移。

本提案对 DeepSeek 建议作一项收窄：不使用可能暗示 Runtime 的 `operational interface`
命名，而使用 DBA Cockpit 内的 `bounded reference-only situational view`。

```text
AUXILIARY_MODEL_OUTPUT_IS_ADVISORY=true
AUXILIARY_MODEL_OUTPUT_IS_DECISION=false
AUXILIARY_MODEL_OUTPUT_IS_AUTHORIZATION=false
LOCAL_CANONICAL_EVIDENCE_HAS_PRECEDENCE=true
```

## 15. Final proposal state（最终提案状态）

```text
CORE_V1_0_PRINCIPLES_PRESERVED=true
NEW_PRINCIPLES_MARKED=true
REWRITE_AND_REMOVAL_SUGGESTIONS_MARKED=true
HUMAN_DECISIONS_MARKED=true
TITLE_CONFLICT_IDENTIFIED=true
SECOND_COCKPIT_PREVENTED=true
FIVE_LAYER_VIEW_DEFINED_AS_NON_RUNTIME=true
AUTHORITY_SEPARATION_PROPOSED=true
ADAPTIVE_IMMUNE_BOUNDARY_PROPOSED=true
NO_DUPLICATE_COMPONENT_PRINCIPLE_PROPOSED=true

SOURCE_CONSTITUTION_MODIFIED=false
SCHEMA_MODIFIED=false
PROTOCOL_MODIFIED=false
CODE_MODIFIED=false
DEPENDENCY_ADDED=false
NEW_DIRECTORY_CREATED=false
NEW_PROJECT_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
AUTOMATIC_RESPONSE_AUTHORIZED=false
COMMIT_CREATED=false
PUSH_PERFORMED=false
```
