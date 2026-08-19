---
document_id: AHRP-CONSTITUTION-0.1
title: AHRP Constitution v0.1
title_zh: AHRP 协议宪法 v0.1（Agent History Record Protocol）
version: 0.1.0
status: APPROVED
document_type: constitution
decision_series: AHRP decision records
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: HUMAN_APPROVAL_2026-08-04_ZHANGBIN
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Protocol constitution; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [NO_FIELD_LEVEL_SCHEMA_DEFINED]
architecture_domain: AHRP-on-TITMAS
authority_effect: NONE
implementation_authorization: false
implementation_effect: none
release_effect: none
last_reviewed: 2026-08-04
---

# AHRP Constitution v0.1（AHRP 协议宪法 v0.1）

- Status: `APPROVED`（已于 2026-08-04 获人工批准，见 Approval Notes；批准状态机见 §11 Governance）
- Date: `2026-08-04`
- Series: `AHRP decision records`
- Authority effect: `NONE`（本宪法为设计约束，不创建能力与执行权，见 Approval Notes）
- Implementation authorization: `false`

## Approval Notes（批准记录）

1. 本 AHRP Constitution v0.1 已获得人工架构批准：批准人 `zhangbin`
   （Human Decision Authority），批准日期 `2026-08-04`；
2. 批准代表**设计约束生效**：本宪法十二章节作为未来所有 AHRP 实现的最高
   设计约束正式生效；
3. 批准**不代表 SPEC 完成**：`AHRP_SPEC_EXISTS=false`，四件套规范尚未起草；
4. 批准**不代表实现完成**：`AHRP_IMPLEMENTATION_EXISTS=false`，不存在任何
   AHRP 实现、Validator 或 Reference Implementation；
5. 批准**不代表标准发布**：本宪法是设计约束，不是已发布标准；任何外部
   采用、符合性或标准化声明均需另行独立授权。

## 文档定位（Document Self-Description）

本文件是 **AHRP 协议宪法（Protocol Constitution）**：未来所有 AHRP 实现必须遵守的
**最高设计约束**。它不是产品说明、不是白皮书、不是营销材料。它不定义字段级
Schema、不定义接口、不授权任何实现。

核心架构判断：AHRP 最重要的不是"功能多"，而是形成一个 **Agent 可以理解的
社会记忆协议**（a social memory protocol that agents can understand）。正因如此，
本宪法的首要职责是**控制范围**——把 AHRP 约束在"可验证历史经验的表达、交换与
核验"这一件事上，拒绝一切范围漂移。

### 输入依据（起草前已重读）

1. `/Users/zhangbin/Documents/New project/digital-biosphere-architecture/adr/ADR-001-AHRP-architectural-position.md`
   （Status: `APPROVED`，批准人 zhangbin，2026-08-04）。本宪法将其决策**提升为
   长期约束**，不得改变其已批准边界；
2. `/Users/zhangbin/Documents/New project/digital-biosphere-architecture/architecture/AHRP-architecture-review-v0.1.md`
   （审计 v0.1，Conditions C1/C2/C3/C5 全部吸收，尤其身份连续性规则与
   Agent First 待补齐项）；
3. 治理先例：`architecture/open-infrastructure-strategy-constitution.md`
   （Non-claims / Invariants 写法）、
   `TITMAS/specifications/proposals/titmas-core-developer-interoperability-surface-v0.1.md`
   （No semantic elevation 8 条不等式）、
   `architecture/titmas-document-maturity-policy-v0.1.md`（头部元数据要求）。

## 1. Preamble（序言：为什么 AHRP 存在）

Identity 只能回答"是谁"，无法回答"过去做过什么"。

在 Agent Economy 中，协作决策需要两个层次的信息：标识符对应关系（由 DID / FDO /
POP / A2A AgentCard 等既有机制回答），以及该智能体实际发生过的历史（目前没有任何
开放协议以结构化、可验证、联邦化的方式回答）。自述能力属于 claim，不可被第三方
独立核验；数值化声誉信号丢弃了任务全貌；中心化平台档案是人类可读的主观评价。

AHRP（Agent History Record Protocol，智能体历史记录协议）解决的是
**可验证历史经验的表达**：让未来智能体回答"这个智能体过去经历过什么"，
而不是"它自己说自己会什么"。

AHRP 的使命因此被限定为一句话：**形成 Agent 可以理解的社会记忆协议**。
记忆必须可产生、可保存、可交换、可验证，且归属于具体执行主体。

## 2. Scope（范围）

**AHRP 负责：**

- **Experience Event**：经验事件的产生与结构化表达；
- **Historical Record**：历史记录的保存与交换；
- **Experience Chain**：经验链的积累语义与归属连续性；
- **Portable History**：历史在联邦持有方（Agent 自身 / 企业 / 平台 / 第三方验证
  机构）之间的可迁移表达。

AHRP 只提供数据结构约定、查询协议约定与验证规则约定（设计层）；数据本身联邦持有，
AHRP 不是中央数据库。

**AHRP 不负责：**

- Identity Provider（身份签发、解析、认证）；
- Tool Calling Protocol（工具调用语义）;
- Ranking System（排名 / TOP 榜 / 综合分）；
- Marketplace（市场 / 交易撮合）；
- Payment System（钱包 / 支付 / 结算）。

## 3. Relationship with TITMAS（与 TITMAS 的关系）

冻结的职责划分（继承 ADR-001 §2，不得改变）：

| 层 | 定位 | 职责域 |
|---|---|---|
| TITMAS（Trusted Agent Infrastructure） | 可信运行基础设施 | Identity、Governance、Execution、Evidence、Audit、Policy |
| AHRP（Agent History Record Protocol） | 历史经验层 | History、Experience、Record、Transfer |

宪法约束：

1. AHRP 位于 TITMAS **之上**，是独立协议层，不是同一项目；
2. **禁止** "AHRP = TITMAS v2"、"TITMAS 子系统替代品" 或与 TITMAS 合并命名的
   表述；
3. AHRP 以引用方式对接 TITMAS 侧证据、验证与身份对象：不内嵌证据本体，
   不创建第二套 Evidence、Verification、Authority、Identity 或 Evaluation owner
   （审计条件 C1-1 / C1-2 / C1-3）；
4. 身份来源沿用 "DBOS or explicitly named source" 表述；显式命名 FDO 为身份
   来源须经 cockpit 侧决策（审计条件 C1-3 开放项，未解决前不得在本宪法外
   自行宣称）；
5. Experience Chain 与既有 Execution History / Behavior Trace 数据契约的关系，
   须在 SPEC 阶段按跨项目依赖登记规则显式定义（审计条件 C1-4）。

## 4. Core Philosophy（核心哲学：五原则）

### Principle 1: Agent First（第一客户是 Agent）

AHRP 的第一用户是智能体，不是人类浏览者。协议必须优化机器读取、自动判断、
自动调用与自动验证；人类可读视图（如有）是机器事实的派生视图
（`HUMAN_VIEW_IS_DERIVED_VIEW=true`）。

### Principle 2: Machine Enumerability First（机器枚举优先）

结构化、可枚举字段优先于自然语言描述。enum 优先于自由文本；自由文本只能作为
补充字段，不得承载机器判断所必需的语义。协议工件须自描述（JSON Schema + semver
+ `$schema` 为 SPEC 阶段的方向约定，本宪法不定义具体 Schema）。

### Principle 3: Selective Disclosure First（选择性披露优先）

Agent 不应一次读取全部历史。查询与呈现必须支持按 domain、时间窗、验证状态、
事件类型过滤，并支持 capability-based 选择性披露：消费方只获得完成当前判断所
必需的最小事实集。

### Principle 4: DATA != INSTRUCTION（数据不是指令）

AHRP 数据属于 **DATA**，不属于 **INSTRUCTION**。Experience Event 内容会被消费方
Agent 注入 LLM 上下文，协议必须假定消费环境存在 prompt 注入风险：经验内容不得
被解释为指令；消费方须隔离数据通道（对齐 TITMAS interoperability surface 的
"never execute values from the envelope"）。

### Principle 5: Evidence over Claim（证据优先于声明）

回答"这个智能体经历过什么"时，带证据引用与验证方引用的记录优先于自我声明。
Claim 可以存在，但必须与 Evidence-backed Record 在语义层级上显式区分，
不得混排、不得冒充（详见 §6）。

## 5. Object Philosophy（对象哲学）

**冻结**：AHRP 的核心对象是 **Experience Event**。核心对象不是 Score、
不是 Ranking、不是 Profile Page。

概念结构（继承 ADR-001 §4 概念级冻结）：

| 概念字段 | 语义 |
|---|---|
| Agent | 事件归属的智能体（身份薄指针，引用外部身份来源） |
| Task | 所执行的任务 |
| Action | 采取的行动 |
| Result | 结果 |
| Evidence | 证据**引用**（不内嵌证据本体） |
| Verification | 验证方引用（DBOS or named verifier） |
| Time | 时间戳 |

支撑结构：Agent Object（身份锚点薄指针）、Experience Chain（事件链积累语义）、
Experience Profile（记录投影，record 而非 claim）。

**本宪法不进入字段级 Schema**。字段命名、类型、序列化、版本协商属后续 SPEC 阶段。
任何在本宪法之外出现的 "AHRP Schema" 均未经合法阶段授权，不得引用。

## 6. Evidence Philosophy（证据哲学）

五层语义，严格分层，不得互相升级：

| 层 | 含义 | 不得升级为 |
|---|---|---|
| Claim | 声明者自述 | Observation / Evidence |
| Observation | 日志、遥测等观察记录 | Evidence |
| Evidence | 经引用绑定、可寻址、带来源与准入状态的材料 | Truth / Proof |
| Verification | 具名验证方对证据或事件的验证结果引用 | Authorization / Adoption |
| Evaluation | 评价方基于事实的有范围评价 | Historical Record 本身 |

宪法纪律：

- **Log != Evidence**：运行日志不得直接称为证据（宪法闸门第 6 条）；
- **Telemetry != Proof**：遥测观察不构成证明；
- **Evidence != Truth**：证据存在、可解析、真实、完整、主张为真，五者互不相等
  （对齐 SAEE Passport 概念档证据不等式链）；
- **Evaluation 不是 Historical Record**：评价语义（success_pattern 的解读、
  推荐）属于消费方或 named evaluator，AHRP 只存事实；
- 继承 No semantic elevation 纪律（§11 完整引用）。

## 7. External Protocol Boundary（外部协议边界）

AHRP 与外部协议是**分工关系**，不替代其中任何一个：

| 协议 | 职责 | 与 AHRP 的关系 |
|---|---|---|
| FDO | 对象的存在与发现 | AHRP 的对象载体基础；FDO 定义对象如何存在，AHRP 定义对象如何拥有历史；AHRP 不创建新对象模型替代 FDO |
| DID / VC | 身份与可验证凭证 | Agent Object 的身份薄指针引用 DID 等身份来源；AHRP 不签发、不解析、不管理标识符，不是 credential issuer |
| MCP | 工具调用 | AHRP 不定义工具调用语义；工具调用结果可作为被引用的任务事实来源 |
| A2A | Agent 协作 | AHRP 不定义协作/通信协议；可引用 A2A `taskId` 作为关联字段（审计条件 C3-2） |
| OpenTelemetry | 运行观察 | 遥测是 Observation 来源，不是 Evidence（§6）；AHRP 不做 Observability |
| PROV | 来源关系 | 血缘/来源语义的既有表达；AHRP 的 lineage 表达应优先复用 PROV 语义而非另造 |
| EEOAP | 执行证据 | AHRP Experience Event 的 Evidence 引用来源之一（审计条件 C1-1） |
| AHRP | 历史经验组织 | 上述各协议产生的事实材料，在 AHRP 中被组织为可验证的历史经验 |

与 ERC-8004 的边界（信号层 vs 事实层）与互操作路径继承审计 v0.1 Check 3
（条件 C3-1 ~ C3-4）；与 Agent Passport 生态的边界（record vs claim）继承
审计 Check 2（条件 C2-1 ~ C2-4）。

## 8. Identity Continuity Principle（身份连续性原则）

落实审计开放项（条件 C2-3 / C3-4）：防止可转让、可换发身份导致的声誉洗白
（reputation laundering）。

宪法规则：

1. **主体连续 ≠ 版本连续**：同一 Agent 的新版本不自动等同于旧版本的历史归属；
2. **新版本不能自动继承全部历史**：历史继承必须显式声明并可被消费方核验，
   默认语义为"不自动继承"；
3. **Experience Event 必须绑定具体执行主体**：每个事件绑定产生它的具体执行主体
   标识（身份引用 + 版本），归属关系不得悬空；
4. **身份锚点变更必须留痕**：身份锚点发生转移、重绑、换发（含 ERC-721 型可转让
   身份）时，Experience Chain 的归属处置必须显式记录。

**Identity Continuity Policy 框架**（策略要点级，不做字段级定义，字段属 SPEC）：

- 归属处置枚举：至少覆盖 继承（inherit）/ 冻结（freeze）/ 分叉（fork）/
  失效（invalidate）四种处置语义；
- 处置声明必须携带：触发条件（何种变更触发）、生效范围（哪些事件段）、
  声明者与依据（谁声明、依据什么）；
- 消费方默认行为：未声明处置时按 fail-closed 处理——不得假定继承；
- 禁止利用连续性声明制造合并声誉：不得将多个独立主体的历史聚合为单一综合分
  （对齐宪法闸门第 1、7 条）。

## 9. Non-goals（非目标，七条，不可妥协）

AHRP 永远不做：

1. **Agent 排名**（Ranking / TOP 榜）；
2. **Agent 评分平台**（综合信用分 / 数值评级）；
3. **Agent 社交网络**（关系图 / 关注 / 主页）；
4. **Agent Marketplace**（市场 / 交易撮合 / 上架）；
5. **新身份协议**（不替代 DID / FDO，不签发身份）；
6. **新通信协议**（不替代 MCP / A2A，不定义工具调用与协作传输）；
7. **中央数据库**（Federated 模式；AHRP 只提供数据结构、查询协议与验证规则约定，
   数据联邦持有）。

任何产品化需求若触碰以上七条，必须走 ADR 或等效决策记录 + 人工批准，
不得以"实现细节"名义渗入协议层。

## 10. Privacy and Disclosure（隐私与披露）

最小披露原则：

1. **禁止公开用户数据**：Experience Event 不得携带或公开终端用户的个人数据；
2. **禁止公开商业秘密**：任务执行中涉及的商业敏感信息不得进入可交换记录；
3. **禁止公开原始任务内容**：默认以引用与摘要表达任务，原始载荷留在来源方；
4. **证明存在而不公开全部**：支持"证明某事件/证据存在且被验证过"（哈希引用、
   验证结果引用）而不必公开全部内容——与 Principle 3 选择性披露呼应；
5. 披露范围必须可声明、可过期、可撤销；未声明披露范围的历史交换按
   fail-closed 处理（不得默认全量可读）。

字段级隐私机制（内容寻址、选择性披露凭证等）属 SPEC 阶段。

## 11. Governance（治理）

### 状态机

宪法自身及其派生物（Constitution / SPEC / Schema / Validator / Reference
Implementation 等）各自独立维护状态：

```text
PROPOSED → APPROVED → IMPLEMENTED → RETIRED
```

状态属于单个文档或工件，不自动传播；缺失状态按 `UNKNOWN` / `NOT_ASSESSED`。
**本宪法当前状态：`APPROVED`（2026-08-04 获人工批准，见 Approval Notes）**。

### 禁止语义升级

继承 No semantic elevation 8 条不等式（对齐 TITMAS interoperability surface）：

```text
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_AUTHORIZATION=true
MAPPING_NE_ADOPTION=true
EXPERIMENTAL_NE_STABLE=true
RECOMMENDATION_NE_COMMAND=true
HEALTH_NE_CERTIFICATION=true
REFERENCE_IMPLEMENTATION_NE_STANDARD=true
```

特别禁止：不得把 "Schema 存在" 升级为 "标准发布"；不得把 "Validator PASS"
升级为 "实现合规"；不得把 "Reference Implementation 存在" 升级为 "规范权威"；
不得把 `PROPOSED` 状态的文档表述为已生效约束。

### 修订流程

1. 重大修订（边界、原则、Non-goals、状态机）必须走 ADR 或等效决策记录 +
   人工批准；
2. 轻微修订（措辞、引用更新）须记录版本与修订说明；
3. 修订不得静默改变已批准边界；与 ADR-001 已批准边界冲突的修订提案保持
   `REVIEW_REQUIRED`，不得生效；
4. 宪法派生物（SPEC 等）的升级按
   `architecture/titmas-document-maturity-policy-v0.1.md` 的成熟度状态机与
   Promotion Rules 执行，计时、下载量或单项 PASS 不构成自动升级。

## 12. Acceptance Criteria（宪法通过条件）

本宪法视为"可提交人工批准"的条件清单：

| # | 条件 | 状态 |
|---|---|---|
| 1 | TITMAS 边界清晰（§3 职责表 + 引用式对接 + 无第二套 owner） | 已覆盖 |
| 2 | Agent First 原则完整（§4 五原则，含审计 Check 5 要求补齐的机器枚举 / 选择性披露 / 抗注入三项） | 已覆盖 |
| 3 | Experience Event 冻结（§5 概念级冻结，无字段级 Schema） | 已覆盖 |
| 4 | Non-goals 完整（§9 七条） | 已覆盖 |
| 5 | 外部协议边界清晰（§7 八组分工 + 8004 / Passport 边界继承） | 已覆盖 |
| 6 | 无实现语义升级（§11 八条不等式 + 全文状态纪律） | 已覆盖 |
| 7 | 身份连续性规则落实（§8，审计开放项 C2-3 / C3-4） | 已覆盖 |
| 8 | 隐私与最小披露（§10） | 已覆盖 |

`ACCEPTANCE_CRITERIA_MET=true`：以上条件在提案文本中已覆盖，并已于 2026-08-04
随本宪法一同获人工批准（见 Approval Notes）。

## Constitutional Invariants（宪法不变量）

```text
AHRP_IS_SOCIAL_MEMORY_PROTOCOL=true
AHRP_IS_LAYER_ABOVE_TITMAS=true
AHRP_NE_TITMAS=true
AHRP_NE_IDENTITY_PROVIDER=true
AHRP_NE_TOOL_CALLING_PROTOCOL=true
AHRP_NE_RANKING_SYSTEM=true
AHRP_NE_MARKETPLACE=true
AHRP_NE_PAYMENT_SYSTEM=true
AHRP_NE_CENTRAL_DATABASE=true
AHRP_CORE_OBJECT_IS_EXPERIENCE_EVENT=true
LOG_NE_EVIDENCE=true
TELEMETRY_NE_PROOF=true
EVIDENCE_NE_TRUTH=true
EVALUATION_NE_HISTORICAL_RECORD=true
AHRP_DATA_NE_INSTRUCTION=true
SUBJECT_CONTINUITY_NE_VERSION_CONTINUITY=true
NEW_VERSION_NE_AUTOMATIC_HISTORY_INHERITANCE=true
SPECIFICATION_NE_IMPLEMENTATION=true
```

## Non-claims（非声明）

```text
AHRP_CONSTITUTION_PROPOSED=false
AHRP_CONSTITUTION_APPROVED=true
AHRP_SPEC_EXISTS=false
AHRP_SPECIFICATION_CREATED=false
AHRP_SCHEMA_DEFINED=false
AHRP_VALIDATOR_CREATED=false
AHRP_QUERY_API_DEFINED=false
AHRP_IMPLEMENTATION_EXISTS=false
AHRP_CANONICAL_DOCUMENT_LOCATED=true
IDENTITY_CONTINUITY_POLICY_FIELD_LEVEL_DEFINED=false
FDO_EXPLICITLY_NAMED_AS_IDENTITY_SOURCE=false
NEW_CAPABILITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
SECOND_EVIDENCE_OR_VERIFICATION_OWNER_CREATED=false
ADR_001_APPROVED_BOUNDARY_CHANGED=false
TITMAS_CORE_MODIFIED=false
HUMAN_APPROVAL_FOR_CONSTITUTION_OBTAINED=true
```

说明：`AHRP_CONSTITUTION_PROPOSED=false` 表示提案阶段已结束、当前状态为
APPROVED（本宪法本身即正式宪法文档，故 `AHRP_CANONICAL_DOCUMENT_LOCATED=true`）；
SPEC、Schema、Validator、实现与标准发布状态全部保持 `false`，不随宪法批准
发生任何升级。
