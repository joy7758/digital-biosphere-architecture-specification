---
document_id: DBA-AHRP-ARCHITECTURE-REVIEW-CLOSURE-0.1
title: AHRP Architecture Review v0.1 Closure
title_zh: AHRP 架构审计 v0.1 闭环报告
version: 0.1.0
status: REVIEWED
document_type: architecture-review-closure
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Architecture review closure document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [CLOSURE_IS_OBSERVATION_NOT_AUTHORIZATION, SPEC_ENTRY_REQUIRES_SEPARATE_HUMAN_APPROVAL]
architecture_domain: AHRP-on-TITMAS
authority_effect: NONE
implementation_authorization: false
implementation_effect: none
release_effect: none
last_reviewed: 2026-08-04
---

# AHRP Architecture Review v0.1 Closure（AHRP 架构审计 v0.1 闭环报告）

- Closure date: `2026-08-04`
- Authority effect: `NONE`
- Implementation authorization: `false`

## 0. Scope and Inputs（范围与输入）

本 Closure 对审计 v0.1 执行条件闭环复核（审计 Condition F1-1 触发的复核流程）。
以下三份输入在执行前已**重新完整读取**，所有对照基于文件原文：

| 文件 | 当前状态（原文） |
|---|---|
| `architecture/AHRP-architecture-review-v0.1.md` | `status: REVIEWED`；总体结论 `PASS_WITH_CONDITIONS_BOUNDED_BY_FINDING_1` |
| `adr/ADR-001-AHRP-architectural-position.md` | `status: APPROVED`；`Decided by: zhangbin`；`HUMAN_APPROVAL_OBTAINED=true` |
| `docs/constitution/AHRP_CONSTITUTION_v0.1.md` | `status: APPROVED`；`HUMAN_APPROVAL_FOR_CONSTITUTION_OBTAINED=true`；`AHRP_CANONICAL_DOCUMENT_LOCATED=true` |

本 Closure 是评审观察记录：不修改上述任一文件，不授权 SPEC，不创建任何工件。

## Correction Note（修正记录，2026-08-04）

本版对初版 Check 2 计数错误做最小修正，如实记录：

1. **总数与分项和不一致**：初版称"17 条 Condition：`CLOSED` 13、`CARRIED_TO_SPEC` 6、
   `OPEN` 1"，分项和 20 ≠ 17；且 17 中混入了 F1-1（Finding 1 补救项，非普通
   Condition）。
2. **修正后**：以审计 v0.1 原文编号清单为唯一依据，普通 Condition 共 **16 条**
   （C1-1~C1-5、C2-1~C2-4、C3-1~C3-4、C5-1~C5-3）；`CLOSED` **9** +
   `CARRIED_TO_SPEC` **6** + `OPEN` **1** = **16**。无重复编号、无双状态、无遗漏。
3. **双状态条目归类**：初版将 C2-3 / C3-1 / C3-2 标注为"CLOSED（宪法层）+ 字段级
   CARRIED_TO_SPEC"双状态，违反唯一状态原则；按其最终未尽事项（字段级落实）
   单归 `CARRIED_TO_SPEC`，宪法层已承接部分在表内单独注明。
4. **F1-1 单列**：F1-1 是 Finding 1 的补救条件（审计 v0.1 §4"Condition F1-1"、
   §13 Gate），不计入普通 Condition 总数，移入独立的 "Finding 1 Remediation"
   小节。

修正仅涉及计数、表格归属与表述，**不改变任何已批准的架构含义**；审计 v0.1、
ADR-001、Constitution 三份文件均未被修改。

## 1. 检查 1：ADR-001 Accepted Decisions → Constitution 承接核对

对照 ADR-001 §7 Accepted Decisions（7 条）与 Constitution 原文：

| # | ADR-001 Accepted Decision（原文摘要） | Constitution 承接位置 | 判定 | 证据（Constitution 原文） |
|---|---|---|---|---|
| 1 | AHRP 定位为 TITMAS 之上的独立协议层，上下层分离、命名独立 | §3 | `COVERED` | §3 约束 1"AHRP 位于 TITMAS 之上，是独立协议层"；约束 2 禁止 "AHRP = TITMAS v2" 与合并命名 |
| 2 | 问题域为"这个智能体过去经历过什么"，与身份、评价、信号层分工 | §1、§6 | `COVERED` | §1 Preamble"让未来智能体回答'这个智能体过去经历过什么'"；§6 Evaluation 层"不是 Historical Record 本身" |
| 3 | 核心对象冻结为 Experience Event（概念级，7 概念字段） | §5 | `COVERED` | §5 概念结构表 Agent/Task/Action/Result/Evidence/Verification/Time 与 ADR-001 §4 逐字段一致；"本宪法不进入字段级 Schema" |
| 4 | Evidence/Verification 引用式对接；身份来源沿用 "DBOS or explicitly named source" | §3、§5、§6 | `COVERED` | §3 约束 3"不内嵌证据本体"、约束 4 沿用该表述且 FDO 显式命名列为开放项；§5 Evidence/Verification 行均标注"引用" |
| 5 | 采纳三项 Agent First 原则（Machine Enumerability / Selective Disclosure / Prompt Injection Resistance） | §4 | `COVERED`（扩展承接） | §4 Principle 2/3/4 逐条对应 ADR-001 Principle A/B/C；Constitution 扩展为五原则（新增 Principle 1 Agent First、Principle 5 Evidence over Claim），均为加强而非改变边界（见检查 3 R4） |
| 6 | FDO 定位为对象基础；四条外部边界划定 | §7、§9 | `COVERED` | §7 表 FDO 行"FDO 定义对象如何存在，AHRP 定义对象如何拥有历史"；Passport/8004 边界见 §7 尾段；LinkedIn/Benchmark 语义由 §9 第 1、3 条与 §6 承接 |
| 7 | 后续文档继承审计 v0.1 §11 治理继承声明 | §11 | `COVERED` | §11 完整引用 No semantic elevation 8 条不等式、状态分离、修订须 ADR + 人工批准；宪法优先由文档定位"输入依据"声明 |

**检查 1 结论**：7/7 `COVERED`，无 `PARTIAL`、无 `MISSING`。ADR-001 已批准边界
未被改变（Constitution Non-claims `ADR_001_APPROVED_BOUNDARY_CHANGED=false` 与
原文核对一致）。

## 2. 检查 2：Review Conditions 承接状态表

状态语义：`CLOSED`=已在 ADR/Constitution 层闭环；`CARRIED_TO_SPEC`=约束已承接、
字段级落实移交 SPEC；`OPEN`=尚未闭环（含 cockpit 待决项）。每条 Condition 有且
仅有一个状态；宪法层已承接但字段级未尽的条目单归 `CARRIED_TO_SPEC` 并注明承接。

### Finding 1 Remediation（补救项，不计入 Condition 总数）

| 编号 | 性质 | 原要求（审计 v0.1 原文摘要） | 承接位置 | 状态 | 证据 |
|---|---|---|---|---|---|
| F1-1 | Finding 1 补救条件（§4 / §13 Gate），非普通 Condition | 正式 Constitution 发布后登记 stable 标识/Owner/maturity/决策引用，触发审计复核 | Constitution 头部元数据 + 本 Closure | `CLOSED`（附注） | `document_id: AHRP-CONSTITUTION-0.1`、`maturity: Development`、`decision_reference: HUMAN_APPROVAL_2026-08-04_ZHANGBIN` 已登记；`owner_ref: NOT_ASSIGNED`（按成熟度政策 §3 缺失时写 NOT_ASSIGNED 为合规登记）；本文件即触发的复核。附注：建议 SPEC 启动前指派 Owner |

### Condition 承接状态表（16 条，唯一状态）

| 编号 | 原要求（审计 v0.1 原文摘要） | 承接位置 | 状态 | 证据 |
|---|---|---|---|---|
| C1-1 | evidence 字段必须为引用，不内嵌证据本体 | Constitution §3 约束 3、§5、§6 | `CLOSED` | §5 Evidence 行"证据引用（不内嵌证据本体）" |
| C1-2 | verifier 引用 DBOS or named verifier；ARO 输入保持三分离 | Constitution §3 约束 3、§5 | `CLOSED` | §5 Verification 行"DBOS or named verifier"；ARO 三分离由 §6 五层语义承接 |
| C1-3 | 身份解析到既有来源，AHRP 不签发标识符；FDO 显式命名开放项 | Constitution §3 约束 3/4、§7 DID/VC 行 | `OPEN`（cockpit 待决） | §3 约束 4"显式命名 FDO 为身份来源须经 cockpit 侧决策"；Non-claims `FDO_EXPLICITLY_NAMED_AS_IDENTITY_SOURCE=false`。注：本条中"AHRP 不签发、不解析、不管理标识符"部分已由 §3 约束 3 与 §7 DID/VC 行承接，唯 FDO 显式命名部分未决，按未尽事项单归 `OPEN` |
| C1-4 | Experience Chain 与 Execution History/Behavior Trace 关系按依赖登记规则定义 | Constitution §3 约束 5 | `CARRIED_TO_SPEC` | §3 约束 5"须在 SPEC 阶段按跨项目依赖登记规则显式定义" |
| C1-5 | AHRP 不输出评价结论，评价权威保持 SAEE/named evaluator | Constitution §6 | `CLOSED` | §6"Evaluation 不是 Historical Record……AHRP 只存事实" |
| C2-1 | Agent Object 为身份锚点薄指针/解析器，不签发身份 | Constitution §5、§7 | `CLOSED` | §5"Agent Object（身份锚点薄指针）"；§7"AHRP 不签发、不解析、不管理标识符" |
| C2-2 | Experience Profile = record vs claim 显式声明 | Constitution §5、§4 P5 | `CLOSED` | §5"Experience Profile（记录投影，record 而非 claim）" |
| C2-3 | 身份连续性规则（继承/冻结/分叉/失效），防声誉洗白 | Constitution §8 → SPEC | `CARRIED_TO_SPEC` | 宪法层已承接：§8 四规则 + Identity Continuity Policy 框架四处置枚举（inherit/freeze/fork/invalidate）+ fail-closed 默认；字段级未尽：Non-claims `IDENTITY_CONTINUITY_POLICY_FIELD_LEVEL_DEFINED=false` |
| C2-4 | 不得由自身记录产生综合分/等级/授权 | Constitution §9、§8 | `CLOSED` | §9 第 1、2 条；§8"禁止利用连续性声明制造合并声誉" |
| C3-1 | 8004 feedbackURI 指向 AHRP 证据；AHRP 不反向消费数值 | Constitution §7 尾段 → SPEC | `CARRIED_TO_SPEC` | 宪法层已承接：§7"与 ERC-8004 的边界……继承审计 v0.1 Check 3（条件 C3-1 ~ C3-4）"；字段级 crosswalk 未尽，移交 SPEC |
| C3-2 | Experience Event 可引用 8004 agentId / A2A taskId | Constitution §7 A2A 行 → SPEC | `CARRIED_TO_SPEC` | 宪法层已承接：§7 A2A 行"可引用 A2A taskId 作为关联字段（审计条件 C3-2）"；字段级引用规范未尽，移交 SPEC |
| C3-3 | 不做 8004 式聚合/评分固化为 non-goal | Constitution §9 | `CLOSED` | §9 第 1、2 条 |
| C3-4 | 可转让 ERC-721 身份的连续性规则 | Constitution §8 | `CLOSED` | §8 规则 4 显式含"ERC-721 型可转让身份" |
| C5-1 | SPEC 逐项覆盖 Agent First 7 项并给机器可验收判据；#3/#6/#7 补齐 | Constitution §4 + SPEC 待办 | `CARRIED_TO_SPEC`（#3/#6/#7 宪法层已补齐） | #3→§4 P2、#6→§4 P3、#7→§4 P4；7 项逐项验收判据仍属 SPEC |
| C5-2 | SPEC 定义内容隔离/转义标记/消费方约定（安全红线） | Constitution §4 P4 + SPEC 待办 | `CARRIED_TO_SPEC` | §4 P4"消费方须隔离数据通道"；字段级机制属 SPEC |
| C5-3 | 人类可读视图为机器事实派生视图 | Constitution §4 P1 | `CLOSED` | §4 P1"HUMAN_VIEW_IS_DERIVED_VIEW=true" |

### Agent First 7 项清单承接去向（审计 §9 表逐行）

| # | 项 | 宪法承接 | SPEC 遗留 |
|---|---|---|---|
| 1 | well-known 发现机制 | 未逐字写入（属 Query Interface 机制） | 待落实 |
| 2 | JSON Schema + semver + `$schema` | §4 P2 方向约定 | 待落实 |
| 3 | enum 优先于自由文本 | §4 P2（已补齐） | 字段级判据待落实 |
| 4 | 哈希/内容寻址证据 | §10 第 4 条"哈希引用" | 具体算法待落实 |
| 5 | 过滤 + 分页查询 | §4 P3（过滤维度） | 分页与接口待落实 |
| 6 | capability-based 选择性披露 | §4 P3（已补齐） | 机制待落实 |
| 7 | 抗 prompt 注入 | §4 P4（已补齐） | 隔离/标记机制待落实 |

**检查 2 结论**：F1-1（Finding 1 补救项，不计入 Condition 总数）随宪法批准
闭环，附 Owner 指派附注。普通 Condition 共 **16 条**：`CLOSED` **9**（C1-1、C1-2、
C1-5、C2-1、C2-2、C2-4、C3-3、C3-4、C5-3）、`CARRIED_TO_SPEC` **6**（C1-4、C2-3、
C3-1、C3-2、C5-1、C5-2）、`OPEN`（cockpit 待决）**1**（C1-3，FDO 显式命名部分）。
校验：9 + 6 + 1 = 16。无重复编号、无双状态、无遗漏、无静默丢弃。

## 3. 检查 3：新边界风险识别

基于三份已批准文档重新评估，是否因宪法/ADR 表述引入新风险：

| # | 风险 | 等级 | 分析 | 缓解归属 |
|---|---|---|---|---|
| R1 | 宪法 §7 新增 OpenTelemetry / PROV / EEOAP 边界（ADR-001 与审计中未逐一列出），是否构成新依赖声明 | `LOW` | 宪法原文为"分工关系，不替代其中任何一个"的划界表述，未创建依赖或采用声明；OpenTelemetry 被明确降为 Observation 来源（"不是 Evidence"），PROV 为"应优先复用……而非另造"的方向建议 | SPEC（引用 PROV/OTel 语义时须注明来源与版本，不得写成采用声明） |
| R2 | 宪法 §8/§10 的 fail-closed 语义与 TITMAS interoperability surface 失败枚举（`INVALID`/`NOT_ASSESSED`/`UNSUPPORTED_VERSION`/`CONFLICTED`/`ERROR`）未显式映射 | `LOW` | fail-closed 是原则级表述，与 TITMAS 枚举方向一致（未知不强制为 PASS），但 SPEC 必须给出逐项映射，否则实现方会各自解释 | SPEC（Query Interface 失败语义节） |
| R3 | DATA != INSTRUCTION 是**消费方义务**，AHRP 协议本身无法强制执行消费方行为，存在执行缺口 | `MEDIUM` | 宪法 §4 P4 与 ADR-001 Principle C 均只定义约定；缺少机器可验证的内容标记与负例时，该原则停留在宣言层 | SPEC（定义数据通道标记、转义约定与"经验内容被当作指令执行"负例）；无法在 SPEC 内解决的部分升级 cockpit ADR |
| R4 | 宪法把 ADR-001 三原则扩展为五原则（新增 Agent First、Evidence over Claim），是否改变已批准边界 | `LOW` | 两项新增均可回溯至审计原文（Agent First=Check 5 前提；Evidence over Claim=证据不等式链），为加强与澄清，非边界变更；宪法 §11 修订流程本身禁止静默改变已批准边界 | 无需行动（已在本文检查 1 留痕） |
| R5 | 跨文档布尔键时间差：ADR-001 Non-claims 仍为 `AHRP_CONSTITUTION_CREATED=false`、`AHRP_CANONICAL_DOCUMENT_LOCATED=false`，与宪法批准后的事实不一致 | `LOW` | 符合"状态属于单个文档、不自动传播"纪律（宪法 §11），ADR-001 布尔块反映其写作时点事实；但后续引用者可能误读 | 无需行动（不修改 ADR-001；后续新 ADR/SPEC 引用状态时以各文档当前头部元数据为准） |
| R6 | 宪法 `owner_ref: NOT_ASSIGNED`：F1-1 要求登记 Owner，当前为政策合规的显式缺省，但长期无 Owner 会使修订流程（§11 须 Owner/人工批准）缺少执行锚点 | `LOW` | 成熟度政策 §3 允许 NOT_ASSIGNED；Unmaintained 风险尚未成立 | cockpit 决策（SPEC 启动前建议指派 Owner） |

**检查 3 结论**：无 `HIGH` 风险；`MEDIUM` 1 项（R3，SPEC 缓解）；其余 LOW。
宪法与 ADR 未引入新的权威、新的真相源或新的跨仓库执行路径。

## 4. 检查 4：SPEC 准入判定

**判定：`CONDITIONALLY_ALLOWED`**

依据：审计 v0.1 §13 Gate 要求"本审计通过（含条件登记）后才进入 SPEC"，且
Finding 1 补救（正式文档落地）与 Condition 登记已完成：审计五检查的
PASS_WITH_CONDITIONS 结论由 ADR-001（APPROVED）与 Constitution（APPROVED）
承接，本 Closure 完成条件闭环。

进入 SPEC 前必须满足 / 已知遗留：

1. **人工批准**：本 Closure 的 `CONDITIONALLY_ALLOWED` 不是 SPEC 授权；SPEC 起草
   启动以 Human Decision Authority 的显式批准为准（Constitution §11 修订流程与
   审计纪律"决策须经 ADR 流程"）；
2. **SPEC 必须承接的 CARRIED_TO_SPEC 项**：C1-4（依赖登记）、C2-3 字段级
   （Identity Continuity Policy 字段）、C3-1/C3-2 字段级（8004/8004-agentId/taskId
   crosswalk）、C5-1（7 项逐项机器可验收判据）、C5-2（内容隔离机制）；
3. **cockpit 待决不阻塞 SPEC**：C1-3 的 FDO 显式命名（R6 的 Owner 指派同）属
   cockpit 侧决策，SPEC 按 "DBOS or explicitly named source" 表述继续，不得
   自行命名；
4. **范围锁定**：SPEC 仅限四件套（Event Schema、Evidence Binding、Verification
   Model、Query Interface）；触碰 Constitution §9 七条 Non-goals 的任何内容保持
   `REVIEW_REQUIRED`。

## 5. 重点复核专节（用户指定七项）

| # | 复核项 | 审计 v0.1 | ADR-001 | Constitution | 判定 |
|---|---|---|---|---|---|
| 1 | TITMAS/AHRP 边界 | Check 1：引用式对接、无第二套 owner | §2 职责表 + 禁止 "TITMAS v2" | §3 职责表与约束 1~5（原文"继承 ADR-001 §2，不得改变"） | `CONSISTENT` |
| 2 | Experience Event 原子单位 | §3 审计对象摘要（设计层字段） | §4 概念级冻结 7 字段 | §5 概念结构表 7 字段，与 ADR-001 逐字段一致 | `CONSISTENT` |
| 3 | Agent First 五原则 | Check 5 七项清单（三原则缺项要求补齐） | §5 采纳三原则 A/B/C | §4 五原则（A/B/C → P2/P3/P4；新增 P1/P5 为加强） | `CONSISTENT`（扩展不冲突，见 R4） |
| 4 | DATA != INSTRUCTION | Check 5 #7 + C5-2 | §5 Principle C + `AHRP_DATA_NE_INSTRUCTION=true` | §4 Principle 4 + Invariants `AHRP_DATA_NE_INSTRUCTION=true` | `CONSISTENT`（执行缺口见 R3） |
| 5 | Identity Continuity | C2-3 / C3-4（开放项） | §7 Future Considerations（继承/冻结/分叉/失效） | §8 四规则 + Policy 框架（同四处置枚举） | `CONSISTENT`（宪法从"未来考虑"升级为"生效规则"，方向一致） |
| 6 | FDO/DID/VC/MCP/A2A 边界 | Check 1 C1-3、Check 3 C3-2 | §6 FDO Position；§3 外部边界 | §7 八行分工表（FDO/DID+VC/MCP/A2A 一致；新增 OTel/PROV/EEOAP 为扩展） | `CONSISTENT`（扩展项见 R1） |
| 7 | Non-goals | Check 4 六项固化要求 | Rejected Alternatives 7 项 | §9 七条不可妥协 | `CONSISTENT`（语义覆盖关系：宪法七条 ⊇ 审计六项固化要求，另含支付系统为新增明确化） |

**专节结论**：7/7 `CONSISTENT`，无 `INCONSISTENT`；两处扩展（五原则、八行协议表）
均判定为加强而非冲突，已分别留痕 R4 / R1。

## 6. Non-claims（非声明）

```text
REVIEW_CLOSURE_EXECUTED=true
CLOSURE_BASED_ON_FRESH_REREAD_OF_THREE_INPUTS=true
F1_1_REVIEW_TRIGGERED_BY_CONSTITUTION_APPROVAL=true
ADR_001_DECISIONS_COVERED_BY_CONSTITUTION=7_OF_7
CONDITIONS_TOTAL=16
CONDITIONS_CLOSED=9
CONDITIONS_CARRIED_TO_SPEC=6
CONDITIONS_OPEN_COCKPIT_PENDING=1
F1_1_COUNTED_AS_ORDINARY_CONDITION=false
CORRECTION_NOTE_RECORDED=true
NEW_BOUNDARY_RISKS_HIGH=0
NEW_BOUNDARY_RISKS_MEDIUM=1
NEW_BOUNDARY_RISKS_LOW=5
SEVEN_FOCUS_ITEMS_CONSISTENT=7_OF_7
SPEC_ENTRY_VERDICT=CONDITIONALLY_ALLOWED
SPEC_ENTRY_AUTHORIZED_BY_THIS_CLOSURE=false
AHRP_SPEC_EXISTS=false
AHRP_SCHEMA_DEFINED=false
AHRP_VALIDATOR_CREATED=false
AHRP_QUERY_API_DEFINED=false
AHRP_IMPLEMENTATION_EXISTS=false
AUDIT_V0_1_MODIFIED=false
ADR_001_MODIFIED=false
CONSTITUTION_MODIFIED=false
NEW_TRUTH_SOURCE_CREATED=false
AUTHORITY_EFFECT=NONE
IMPLEMENTATION_AUTHORIZED=false
```

说明：本 Closure 不构成 SPEC 授权；`SPEC_ENTRY_VERDICT=CONDITIONALLY_ALLOWED`
只是复核观察结论，SPEC 启动以人工批准为准。审计 v0.1、ADR-001、Constitution
三份文件均未被本 Closure 修改。

- 交叉引用（2026-08-04 追加）：`architecture/TITMAS-AHRP-verified-development-loop-review-v0.1.md`（TITMAS–AHRP 可验证发展闭环审计 v0.1，status: PROPOSED_RESEARCH_FINDING，authority_effect: NONE，implementation_authorization: false）
