---
document_id: AHRP-ADR-001
title: AHRP Architectural Position and Boundary Decision
title_zh: AHRP 架构定位与边界决策（AHRP ADR-001）
version: 0.1.0
status: APPROVED
document_type: architecture-governance-adr
decision_series: AHRP decision records
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: HUMAN_APPROVAL_2026-08-04_ZHANGBIN
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Architecture decision record; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [AHRP_CANONICAL_DOCUMENT_NOT_LOCATED, CONTEXT_BASED_ON_ARCHITECTURE_REVIEW_V0_1]
architecture_domain: AHRP-on-TITMAS
authority_effect: NONE
implementation_authorization: false
implementation_effect: none
release_effect: none
last_reviewed: 2026-08-04
---

# ADR-001: AHRP Architectural Position and Boundary Decision

中文：AHRP 架构定位与边界决策

- Status: `APPROVED`（下一阶段进入 AHRP Constitution 阶段；批准不构成实现授权）
- Date: `2026-08-04`
- Decided by: `zhangbin`（Human Decision Authority，批准日期 2026-08-04，见 Approval Notes）
- Series: `AHRP decision records`（AHRP 自身决策序列首篇，见下方序列声明）
- Review reference: `architecture/AHRP-architecture-review-v0.1.md`
- Authority effect: `NONE`
- Implementation authorization: `false`

## Approval Notes（批准记录）

1. 本 ADR-001 获人工架构批准：批准人 `zhangbin`（Human Decision Authority），
   批准日期 `2026-08-04`；
2. 批准仅代表**架构决策有效**（AHRP 定位、边界、核心对象冻结与 Agent First
   三原则作为决策层结论生效）；
3. 批准**不代表** SPEC、实现或发布完成：`AHRP_CONSTITUTION_CREATED=false`、
   `AHRP_SPECIFICATION_CREATED=false`、`AHRP_SPEC_EXISTS=false`、
   `AHRP_IMPLEMENTATION_EXISTS=false`，任何后续工件仍须按其自身阶段独立
   授权与验收。

## Series Note（决策序列声明）

本文件是 **AHRP 自己的决策序列（Series: AHRP decision records）** 的第一篇，
编号从 AHRP-ADR-001 开始。cockpit 在 `architecture/` 下维护独立的 **cockpit 全局
ADR 序列**（本审计扫描范围内可见编号自 ADR-002 起；任务简报提及的
`ADR-001-saee-dbos-boundary-definition.md` 在本次扫描中未命中，其存在与否不影响
下述规则）。两个序列编号互不继承、互不覆盖：本 ADR-001 只约束 AHRP 协议方向
的定位与边界，不修改 cockpit 全局序列中任何既有决策；若 cockpit 全局序列存在
同号条目，两者并行、不得混淆；cockpit 全局序列的编号也不因本序列而改变。

## 1. Problem Statement（问题陈述）

未来 Agent Economy 中，智能体之间的协作决策需要回答两个不同层次的问题：

1. **这是谁？**（Identity）——由 DID / FDO / POP / A2A AgentCard 等既有身份与
   发现机制回答；
2. **它过去经历过什么？**（History）——目前没有任何开放协议以结构化、可验证、
   联邦化的方式回答。

"知道是谁"不足以支持"是否值得合作"：

- 身份只能证明标识符对应关系与声明者自述，不能证明声明者**实际发生过什么**；
- 自述能力（"它自己说自己会什么"）属于 claim，无法被第三方独立核验；
- 现有相邻机制各缺一块：Agent Passport 生态只做身份 / 来源 / 授权三件事；
  ERC-8004 只把事实压缩成数值信号；中心化市场只做人类可读的主观评价；
  单主体记忆迁移（如 arXiv 2605.11032 的 Portable Agent Memory）不做跨主体验证
  与第三方归属认定。

因此需要一个位于可信运行基础设施之上的**历史经验层**：让未来智能体回答
"这个智能体过去经历过什么"，而不是"它自己说自己会什么"。这就是 AHRP
（Agent History Record Protocol，智能体历史记录协议）的问题域。

本 ADR 的 Context 证据为已完成并通过的架构审计：
`/Users/zhangbin/Documents/New project/digital-biosphere-architecture/architecture/AHRP-architecture-review-v0.1.md`
（下称"审计 v0.1"）。审计基于交接简报的设计摘要，其 Finding 1 指出 AHRP 正式
协议文档在本机尚不存在，故本 ADR 的全部定位均为**设计层 / 决策层**表述。

## 2. Relationship with TITMAS（与 TITMAS 的关系）

**Decision**：AHRP 是位于 TITMAS 之上的独立协议层，与 TITMAS 是上下层关系，
不是同一项目。

| 层 | 职责域 | 核心对象 |
|---|---|---|
| TITMAS（可信运行基础设施） | Identity、Governance、Execution、Evidence、Audit、Policy | 身份引用、边界声明、证据绑定、验证结果引用、评价交接 |
| AHRP（历史经验层） | Experience Event、Historical Record、Experience Chain、Portable History | 经验事件、历史记录、经验链、可迁移历史 |

边界纪律（对齐审计 v0.1 Check 1 条件 C1-1 ~ C1-5）：

1. AHRP 的 Experience Event 以**引用**方式对接 TITMAS 侧的证据、验证与身份对象，
   不内嵌证据本体，不创建第二套 Evidence、Verification、Authority、Identity 或
   Evaluation owner（对齐 `architecture/titmas-architecture-charter-v1.0.md`
   Permanent boundaries）；
2. 身份来源依赖沿用 cockpit Object ownership 表表述：Identity 的 canonical owner
   为 **DBOS or explicitly named source**（对齐
   `TITMAS/specifications/proposals/titmas-core-developer-interoperability-surface-v0.1.md`）。
   cockpit 既有材料**未显式命名 FDO** 为身份来源，"显式命名 FDO"列为
   Future Consideration（见 §7，对齐审计条件 C1-3）；
3. AHRP 与 DEP-003 数据契约中 Execution History / Behavior Trace 的关系，必须在
   后续 SPEC 中按跨项目依赖登记规则显式定义（审计条件 C1-4）。

**禁止表述**：不得把 AHRP 描述为 "TITMAS v2"、"TITMAS 子系统替代品" 或
"TITMAS 的合并扩展"。两者命名保持独立（对齐宪法闸门第 3 条"不得与 TITMAS
合并命名"）。

## 3. External Boundary Analysis（外部边界分析）

### 3.1 Agent Passport：为什么 AHRP 不等同于 Agent Passport？

**Identity vs History。** Agent Passport 生态（Trulioo DAP、APort OAP、RNWY、
Skyfire KYA、DigiCert、Visa TAP 及 SAEE Agent Passport 概念档）的核心是
**身份、来源、授权**三件事，本质是"声明者当前声明自己是什么"（claim）；
AHRP 的核心是"这个智能体过去发生过什么"（record）。**record vs claim** 是
根本区分。

红线继承（对齐 `/Users/zhangbin/GitHub/SAEE/reports/SAEE_AGENT_PASSPORT_PROFILE_CONCEPT_V0_1.md`
与审计 v0.1 Check 2）：

- AHRP 的 Agent Object 必须是身份锚点的薄指针 / 解析器，不签发身份
  （`PROFILE_IS_IDENTITY_SYSTEM=false` 同理适用于 AHRP）；
- Experience Profile 是记录投影，不是 standing readiness badge、不是自我声明；
- `Evidence reference present != Evidence resolved != claim proven true`；
- 必须定义身份连续性规则，防止可转让身份导致的声誉洗白（审计条件 C2-3，
  列入 Future Considerations）。

### 3.2 ERC-8004：为什么 AHRP 不竞争 ERC-8004？

**信号层 vs 事实层。** ERC-8004（Trustless Agents，Draft）的 Reputation 注册表
是数值 + 标签的**反馈信号层**，Validation 是 0–100 裁决钩子，且明确把复杂聚合
留给链下；AHRP 是**结构化事实层**，存任务全貌与证据，不把事实压缩成单一数值。
8004 的 `getSummary` 聚合恰好是 AHRP 明确不做的事。

两者互补，互操作路径采纳审计 v0.1 Check 3 结论（条件 C3-1 ~ C3-4）：

- 8004 `feedbackURI` 可指向 AHRP 证据；Experience Event 可引用 8004 `agentId`
  与 A2A `taskId` 作为关联字段；
- AHRP 不反向消费 8004 数值沉淀为自身事实字段；
- 唯一重叠点（链下 feedback file 携带任务事实）按上述划界处理。

### 3.3 LinkedIn / Agent Profile：为什么 AHRP 不做 Agent 社交档案？

**Profile != Verified History。** LinkedIn 类档案是人类可读、平台持有、自我声明
且主观评价的社交档案；AHRP 是机器可读、联邦持有、证据绑定的历史记录协议。
AHRP 的 Experience Profile 只为"供其他 Agent 快速判断"而存在，是事件链的派生
视图，不是页面、不是主页、不是社交关系图。

把"不做 UI / 网站 / 社交"固化为不可妥协 non-goal（见 Non-goals 章节与宪法闸门
第 2 条）。

### 3.4 Benchmark System：为什么 AHRP 不做 Agent 排名和评分？

**Evaluation 不是 Historical Record。** 排名 / TOP 榜 / 综合信用分属于评价
（Evaluation）语义，评价权威在 SAEE 或 named evaluator，不在历史记录层。
能力具有领域属性，跨领域的单一数值比较在架构上不成立。

AHRP 只存事实；上层按任务计算推荐。把"不做评分平台"固化为不可妥协 non-goal
（对齐宪法闸门第 1 条、第 7 条与审计 v0.1 Check 4）。

## 4. Core Object Decision（核心对象决策）

**Decision**：AHRP 的核心对象**冻结为 Experience Event**。核心对象不是 Score、
不是 Ranking、不是 Profile Page。

Experience Event（概念级定义）至少包含：

| 概念字段 | 语义 |
|---|---|
| Agent | 事件归属的智能体（身份引用，薄指针，见 §2、§3.1） |
| Task | 所执行的任务 |
| Action | 采取的行动 |
| Result | 结果 |
| Evidence | 证据**引用**（对齐审计条件 C1-1，不内嵌证据本体） |
| Verification | 验证方引用（DBOS or named verifier，对齐审计条件 C1-2） |
| Time | 时间戳 |

**冻结级别声明**：这是**概念级冻结**（concept-level freeze）。字段级 Schema、
字段命名、类型与序列化属于后续 SPEC 阶段，本 ADR 不定义 Schema，也不授权任何
Schema 实现。Agent Object、Experience Chain、Experience Profile 保持为核心对象的
支撑结构，不升级为核心对象本身。

## 5. Agent First Design Decision（Agent First 设计决策）

审计 v0.1 Check 5 指出，以下三项工程约定在交接简报的设计摘要中未见显式声明，
须在 Constitution / SPEC 中补齐。本 ADR **正式采纳**它们为 AHRP 架构原则：

### Principle A: Machine Enumerability First（机器枚举优先）

结构化、可枚举字段优先于自然语言描述。enum 优先于自由文本；自由文本只能作为
补充字段存在，且不得承载机器判断所必需的语义。对齐 JSON Schema + semver +
`$schema` 自描述要求。

### Principle B: Selective Disclosure First（选择性披露优先）

Agent 不应一次读取全部历史。查询与呈现必须支持按 domain、时间窗、验证状态、
事件类型过滤，并支持 capability-based 选择性披露：消费方只获得完成当前判断所
必需的最小事实集。

### Principle C: Prompt Injection Resistance（抗提示注入）

AHRP 数据属于 **DATA**，不属于 **INSTRUCTION**。Experience Event 内容天然会被
消费方 Agent 注入 LLM 上下文，协议必须定义内容隔离与消费方约定：经验内容不得
被解释为指令；对齐 TITMAS interoperability surface 的 Security considerations
（"never execute values from the envelope"）。

```text
AHRP_PRINCIPLE_MACHINE_ENUMERABILITY_FIRST=true
AHRP_PRINCIPLE_SELECTIVE_DISCLOSURE_FIRST=true
AHRP_PRINCIPLE_PROMPT_INJECTION_RESISTANCE=true
AHRP_DATA_NE_INSTRUCTION=true
```

## 6. FDO Position（FDO 定位）

**FDO 是对象基础，不是 AHRP 替代品。**

- FDO 定义对象**如何存在**（对象模型、生命周期、可发现性）；
- AHRP 定义对象**如何拥有历史**（经验事件的产生、保存、交换与验证）。

两者是"存在"与"经历"的关系，不是竞争关系。AHRP 不创建新的对象模型替代 FDO，
也不创建新的身份协议替代 DID / FDO（对齐宪法闸门第 4 条）。FDO 作为 AHRP 对象
载体的具体映射，属于 SPEC 阶段的开放项。

## 7. Decision Summary（决策汇总）

### Accepted Decisions（采纳的决策）

1. AHRP 定位为 TITMAS 之上的独立协议层（历史经验层），与 TITMAS 上下层分离、
   命名独立；
2. AHRP 问题域为"这个智能体过去经历过什么"，与身份、评价、信号层明确分工；
3. 核心对象冻结为 Experience Event（概念级，至少含 Agent / Task / Action /
   Result / Evidence / Verification / Time）；
4. Evidence 与 Verification 一律引用式对接，不内嵌本体、不自设权威；身份来源
   沿用 "DBOS or explicitly named source" 表述；
5. 正式采纳三项 Agent First 架构原则：Machine Enumerability First、
   Selective Disclosure First、Prompt Injection Resistance；
6. FDO 定位为对象基础；AHRP 与 Agent Passport、ERC-8004、LinkedIn 类档案、
   Benchmark 系统的四条外部边界按 §3 划定；
7. AHRP 后续文档必须继承审计 v0.1 §11 的治理继承声明（宪法优先、状态分离、
   禁止语义升级、Non-claims 布尔量纪律、投影服从权威规范、决策经 ADR 流程）。

### Rejected Alternatives（被拒绝的替代方案）

| 替代方案 | 拒绝理由 |
|---|---|
| 把 AHRP 做成 TITMAS 子系统或 "TITMAS v2" | 违反上下层分离决策与宪法闸门第 3 条；TITMAS 永久边界禁止新增第二套 Evidence/Verification/Identity/Evaluation owner |
| 做评分 / 排名系统（TOP 榜、综合信用分） | Evaluation 不是 Historical Record；违反宪法闸门第 1、7 条 |
| 做中央数据库 | 违反 Federated 原则；cockpit 宪法禁止无限强中心（ADR-032 先例） |
| 自建身份协议替代 DID / FDO | 违反宪法闸门第 4 条；身份 owner 已有归属 |
| 自建工具调用协议替代 MCP / A2A | 违反宪法闸门第 5 条；超出 AHRP 问题域 |
| 把日志直接称为证据 | 违反宪法闸门第 6 条与 `OBSERVATION_NE_EVIDENCE=true` |
| 做 LinkedIn 类社交档案 / 网站 | Profile != Verified History；违反宪法闸门第 2 条 |

### Future Considerations（未来考虑项）

- **AHRP Constitution**：正式协议文档落地（本 ADR 获人工批准后的下一阶段）；
- **SPEC.md**：Event Schema、Evidence Binding、Verification Model、Query Interface
  字段级规范，逐项覆盖 Agent First 7 项验收清单；
- **Schema / Validator / Query API / Reference Implementation / Demo**：按审计
  v0.1 §13 路线顺序推进；
- **显式命名 FDO 为身份来源**：cockpit Object ownership 表目前为
  "DBOS or explicitly named source"，FDO 未被显式命名；需通过 cockpit 侧
  契约或决策完成命名（对齐审计条件 C1-3）；
- **身份连续性 / 声誉洗白规则**：针对可转让身份（如 ERC-721）的 Experience Chain
  归属语义（继承 / 冻结 / 分叉 / 失效）；
- **与 ERC-8004 的互操作细节**：字段级 crosswalk（agentId / taskId / feedbackURI）；
- **跨项目依赖登记**：AHRP 相关依赖按 `CROSS-PROJECT-DEPENDENCIES.md` §4 规则
  登记 dependency_id、类型、owner 与失败行为。

## Consequences（后果）

采纳本 ADR 后：

1. **AHRP 成为独立协议方向**：获得独立的决策序列（Series: AHRP decision records）、
   独立的文档路线（Constitution → SPEC → Schema → Validator → Query API →
   Reference Implementation → Demo）与独立的边界约束；
2. **后续闸门**：AHRP 一切后续文档必须通过审计 v0.1 §10 复核的 7 条宪法闸门
   （不得：改造成排名系统；改造成 LinkedIn 类网站；与 TITMAS 合并命名；创建新
   身份协议替代 DID/FDO；创建新工具调用协议替代 MCP/A2A；把日志直接称为证据；
   把评分称为信用），并继承其 §11 治理继承声明；
3. **对 cockpit 决策序列的影响**：本序列与 cockpit 全局 ADR 序列平行存在、
   编号互不继承；本 ADR 若需产生 cockpit 级效力（如依赖登记、Object ownership
   表命名变更），必须另行进入 cockpit 全局 ADR 流程；
4. **审计复核触发**：AHRP Constitution 正式发布后，必须触发对审计 v0.1 的复核
   （审计条件 F1-1）；
5. **状态边界**：本 ADR 已于 2026-08-04 获人工批准（批准人 zhangbin，见
   Approval Notes），状态为 `APPROVED`，下一阶段进入 AHRP Constitution 阶段。
   批准不构成实现授权：本 ADR 不得被引用为 Schema、Validator、Reference
   Implementation 或任何发布的授权证据。

## Non-goals（非目标）

本 ADR：

- 不定义字段级 Schema、序列化格式或 URI scheme；
- 不创建 Validator、Query API、Reference Implementation 或 Demo；
- 不修改 TITMAS 核心实现、规范注册表或任何既有文件；
- 不把 AHRP 合并进 TITMAS 主体或 cockpit 全局决策序列；
- 不产生 Runtime、Agent、Capability、Permission 或任何可执行工件。

## Non-effects（无效力声明）

本 ADR：

- 不创建 Agent、Entity、Runtime、Capability、Permission 或 Digital Organism；
- 不授权实现、部署、实验、发布或外部采用；
- 不修改 DBOS、SAEE、TITMAS 或任何子项目的能力事实、证据事实或责任边界；
- 不声称 AHRP 的任何能力、协议、Schema 或文档已经存在、完成或可用；
- 不替代 Human Decision；批准权属于 Human Decision Authority。

```text
AUTHORITY_EFFECT=NONE
IMPLEMENTATION_AUTHORIZED=false
AUTOMATIC_AUTHORITY_EFFECT=NONE
```

## Non-claims（非声明）

说明：`AHRP_ADR_001_ADOPTED=true` 仅表示本决策记录已建立并进入 AHRP 决策序列；
人工批准已于 2026-08-04 获得（`HUMAN_APPROVAL_OBTAINED=true`），批准效力边界
见 Approval Notes：仅架构决策有效，不延伸至 SPEC、实现或发布。

```text
AHRP_ADR_001_ADOPTED=true
AHRP_CONSTITUTION_CREATED=false
AHRP_SPECIFICATION_CREATED=false
AHRP_SPEC_EXISTS=false
AHRP_IMPLEMENTATION_EXISTS=false
AHRP_CANONICAL_DOCUMENT_LOCATED=false
HUMAN_APPROVAL_OBTAINED=true
AHRP_SCHEMA_DEFINED=false
AHRP_VALIDATOR_CREATED=false
AHRP_QUERY_API_DEFINED=false
NEW_TRUTH_SOURCE_CREATED=false
SECOND_EVIDENCE_OR_VERIFICATION_OWNER_CREATED=false
NEW_IDENTITY_PROTOCOL_CREATED=false
COCKPIT_GLOBAL_ADR_SEQUENCE_MODIFIED=false
TITMAS_CORE_MODIFIED=false
EXISTING_FILES_MODIFIED=false
CHILD_REPOSITORIES_MODIFIED=false
```
