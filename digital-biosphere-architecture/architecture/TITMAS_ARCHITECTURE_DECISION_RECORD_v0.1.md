---
document_id: DBA-TITMAS-ARCHITECTURE-DECISION-RECORD-0.1
title: TITMAS Architecture Decision Record v0.1
title_zh: TITMAS 架构决定记录 v0.1
status: ARCHITECTURE_REVIEW_COMPLETE_REVISE_RECOMMENDED
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
reviewed_at: 2026-07-28
review_recommendation: REVISE
human_decision_status: PENDING
decision_reference: NOT_DECIDED
normative_effect: NONE
authority_effect: NONE
implementation_effect: NONE
schema_effect: NONE
protocol_effect: NONE
repository_effect: NONE
external_action_effect: NONE
---

# TITMAS Architecture Decision Record v0.1

中文：TITMAS 架构决定记录 v0.1。

## 0. Decision boundary（决定边界）

本记录审查现有
[`TITMAS Digital Immune Constitution v1.0`](titmas-digital-immune-constitution-v1.0.md)，
并把 Constitution Review（宪法审查）、Ownership Map（职责归属图）和 Data Flow Map
（数据流图）合并为一个供 Human Architecture Decision（人类架构决定）使用的决定包。

本轮审查建议为：

```text
ARCHITECTURE_REVIEW_RECOMMENDATION=REVISE
HUMAN_DECISION_STATUS=PENDING
DIGITAL_IMMUNE_CONSTITUTION_ADOPTED=false
DIGITAL_IMMUNE_CONSTITUTION_FROZEN=false
NORMATIVE_EFFECT=NONE
IMPLEMENTATION_AUTHORIZED=false
```

`REVISE` 是架构审查结论，不是对 Human Authority（人类权威）的替代。只有带有
`decided_by_ref`、`decided_at`、明确 scope（范围）和后继版本引用的人类决定，才能把
候选宪法升级为 `Accepted` 或 `Frozen`。本记录不创建代码、Schema（模式）、Protocol
（协议）、Runtime（运行时）、新项目、Agent、Entity、Capability 或 Permission。

### 0.1 Three-option review（三选一审查）

| 选择 | 本轮结论 | 理由 |
|---|---|---|
| `ACCEPT` | 不建议 | 核心原则成立，但 Owner、Authority、响应责任、重复项目处置和接口失败语义尚未冻结 |
| `REVISE` | **建议** | 保留现有原则，修正术语、职责、数据流和生效条件后再提交人类决定 |
| `REJECT` | 不建议 | 候选已经正确表达 compositional scale（组合式扩展）、Evidence First（证据优先）和 bounded autonomy（有界自治），整体推倒会重复建设 |

### 0.2 Review basis（审查依据）

本记录按 DBA 驾驶舱与强制治理顺序审查，并以以下材料为主要依据：

- [`PROGRAM-CHARTER.md`](../PROGRAM-CHARTER.md)；
- [`PROGRAM-STATUS.md`](../PROGRAM-STATUS.md)；
- [`DECISION-QUEUE.md`](../DECISION-QUEUE.md)；
- [`RISK-AND-BLOCKER-REGISTER.md`](../RISK-AND-BLOCKER-REGISTER.md)；
- [`MASTER-ROADMAP.md`](../MASTER-ROADMAP.md)；
- [`PROJECT-PORTFOLIO.md`](../PROJECT-PORTFOLIO.md)；
- [`CROSS-PROJECT-DEPENDENCIES.md`](../CROSS-PROJECT-DEPENDENCIES.md)；
- [`INTEGRATION-GATES.md`](../INTEGRATION-GATES.md)；
- [`Digital Biosphere Open Infrastructure Strategy Constitution`](open-infrastructure-strategy-constitution.md)；
- [`Initial Project Role Mapping`](project-mapping.md)；
- [`Authority Freeze Decision Record`](authority-freeze-decision-record-v0.1.md)；
- [`TITMAS Freeze Readiness Report`](titmas-freeze-readiness-report-v0.1.md)；
- [`TITMAS Interface Readiness Review`](titmas-interface-readiness-review-v0.1.md)；
- `/Users/zhangbin/GitHub/agent-evidence/TITMAS_CURRENT_STATE_REPORT.md`。

仓库事实优先于架构比喻；已采纳的 Program Charter、战略宪法和 ADR 优先于本候选；
review、recommendation 和辅助模型输出均不产生 Adoption（采纳）或 Authorization
（授权）。

## A. Current highest principles（当前最高原则）

### A1. Precedence（优先顺序）

发生冲突时，按以下顺序处理：

1. 适用法律、明确的人类决定和各项目 canonical source（规范事实源）；
2. DBA Program Charter、已采纳战略宪法和已采纳 ADR；
3. DBOS、SAEE 及其他项目各自已核验的能力与状态事实；
4. 已采纳的跨项目 ownership/interface decision；
5. Development、Proposal、Review、Candidate 和辅助智能体建议。

候选宪法不能反向覆盖更高层事实，也不能仅凭“宪法”名称获得规范效力。

### A2. Principles to preserve（必须保留的原则）

1. **Compositional scale, not an unbounded center**
   通过大量职责简单、边界受限、可替换、可验证的主体和服务形成组合能力；组合不聚合
   Authority、Permission、Decision 或 Truth Ownership。
2. **Stable identity with accountable reference**
   受治理主体需要稳定身份引用、责任方、目的、版本和生命周期边界；Identity 不等于
   Permission。
3. **Verifiable action**
   重要操作应留下可追溯的 intent、action、execution 和 evidence candidate 引用；记录
   完整性不证明外部事实绝对真实。
4. **Bounded autonomy**
   Capability、Authority、Permission、Context 和 Execution 必须分开；自治范围应可撤销、
   可隔离、可审查。
5. **Evidence First, without semantic elevation**
   Observation 不等于 Evidence，Evidence 不等于 Truth，Validation 不等于 Certification，
   Evaluation 不等于 Authority。
6. **Homeostasis as an evaluation objective**
   稳态是多维、带方法和时间窗口的评价目标，不是自动控制器或单一健康分数。
7. **Graded and reversible response**
   分级响应只能作为候选语义；限制、隔离和退役必须有 Authority、范围、期限、复核和恢复
   条件。
8. **Memory continuity with governed retention**
   通过 lineage、append-only history、correction 和 supersession 保持历史连续性，同时
   遵守隐私、最小化和删除义务。
9. **Evolution remains advisory until decided**
   SAEE 可以评价并提出演化建议；Recommendation 不等于 Decision，Decision 不等于
   Execution。
10. **Open and replaceable composition**
    开放接口与可替换实现优先；开放进入不等于自动准入，版本变化不等于运行时升级。

### A3. Required constitutional revisions（宪法必须修订的内容）

在提交 `ACCEPT` 或 `FROZEN` 决定前，应形成现有 v1.0 的后继修订，而不是创建平行宪法：

- 把 Digital Immune 明确定义为 cross-cutting architecture lens（跨域架构视角）或待决定
  的规范域，不得把它写成新的 Authority、Runtime、项目或中心；
- 将 `Digital Cell` 保持为非规范比喻，直到证明它与既有 Digital Entity 有不可替代的
  语义差异并形成单独决定；
- 把 repository health diagnosis（仓库健康诊断）与 ecosystem evaluation（生态评价）
  分开：前者是 `agent-health` 当前产品面，后者属于 SAEE 评价边界；
- 为 Level 0–4 写明“谁提出、谁决定、谁执行、谁复核、如何撤销”；在这些角色未决定前，
  所有等级均不得成为自动化规则；
- 将 Agent Evidence 的 package/validation 与 DBOS 的 canonical admission/verification
  分开，禁止把 validator `PASS` 升级为 DBOS Evidence、Truth 或 Permission；
- 把 POP 固定为 persona/identity-related reference，不得暗示其为 DBOS 身份权威；
- 将 MCP 固定为 transport/discovery mechanism（传输／发现机制）；“神经系统”只能用于
  解释，不能成为 Authority、routing truth 或执行授权；
- 把“不可篡改”改写为可核验的 digest、append-only、correction 和 supersession 属性，
  除非存在能够支持更强主张的独立证明；
- 为每个 crosswalk 条目增加 canonical source、Owner 状态、版本轴、失败语义和
  non-elevation 条件；
- 明确本宪法决定、Authority Freeze、Interface Freeze 和 implementation authorization
  是独立状态，不能相互自动推导。

## B. Ownership Map（各模块唯一职责）

### B1. Canonical responsibility map（规范职责图）

| 模块／域 | 唯一职责 | 明确不拥有 | 当前确定性 |
|---|---|---|---|
| **DBA** | Program Governance、Architecture Specification、跨项目边界、ADR、gate、风险和决定入口 | Runtime、Agent execution、DBOS state mutation、SAEE algorithm、项目能力事实替写 | 已由 Program Charter 和战略宪法确定 |
| **DBOS** | Identity、Capability record、Execution record、Evidence admission、Verification、Lifecycle 的 canonical existence boundary | SAEE fitness/evolution algorithm、自动创建 Agent、自动授权 | 战略职责已确定；具体 source/status/interface 仍有开放决定 |
| **SAEE** | Reliability、Stability、Risk、Adaptation、Fitness 和 Evolution Recommendation 的受保护评价边界 | Identity、Permission、Execution、Evidence write、自动响应、Command | 战略职责已确定；protected interface 尚待 Owner 批准 |
| **Agent Evidence / `agent-evidence`** | completed-operation evidence candidate 的捕获、打包、profile validation、本地导出、离线复核与机器可读 receipt 的公共参考实现 | Truth、DBOS admission authority、TITMAS Runtime、治理平台、Agent Immune host | 仓库事实已核验 |
| **EEOAP** | completed-operation accountability profile 及其本地验证规则 | 法律不可抵赖、认证、官方标准、全局 provenance authority | 当前 public profile 边界已核验；跨项目 Specification/Version Authority 未冻结 |
| **Agent Health / `agent-health`** | 首次运行可完成的本地静态 repository-health diagnosis、可解释 findings 和有边界 recommendation | Runtime safety monitor、Permission、自动隔离、Evidence infrastructure、SAEE evolution authority | 当前产品职责已核验；是否为唯一 Agent Immune 产品仍待人类决定 |
| **`titmas-health`** | 尚未决定 | 不得在处置决定前扩展为第二 Health engine | `DUPLICATION_REVIEW_REQUIRED` |
| **POP** | Portable Persona Object 的 reference/projection 表面 | canonical identity、authentication、Permission 或完整 Agent | reference role 可用；DBOS mapping 未采纳 |
| **TITMAS** | DBA 治理下的 interoperability mapping、handoff、profile、adapter contract 和 conformance boundary 候选域 | 第二 DBA、DBOS 替代品、Truth store、Runtime control plane、自动 Authority | Architecture Domain 与 Specification Authority 均未正式冻结 |
| **MCP** | 可替换的调用、发现或传输机制 | 神经系统 Authority、Truth、Permission、Decision 或唯一数据路径 | 机制级角色；具体采用按接口单独决定 |
| **Human Governance** | 接受／修订／拒绝候选，授予有限 Authority，授权实施和外部行动 | 不得由投票数、模型分数、CI PASS 或 recommendation 自动替代 | 必须保留的最终 gate |

### B2. Ownership decisions still required（仍需人类决定的归属）

以下内容只是候选，不得在本记录中伪装为已决定：

1. `agent-health` 是否成为唯一 Agent Immune 产品；
2. `titmas-health` 是 archive、停止推进、实验性分支、successor 还是 bounded adapter；
3. `agent-evidence/integrations/` 与 `titmas-integrations` 的唯一 Owner 和依赖方向；
4. AEO、AEP、EEOAP、Agent Evidence Layer 各自的 canonical name、Owner、版本轴和兼容关系；
5. TITMAS 是否获得 bounded Specification Authority，以及委托、期限和撤销规则；
6. POP 到 DBOS Identity 的 mapping 是否采纳；
7. Self-Immune Demo 的承载位置：既有 `titmas-demo`、独立 validation harness，或
   `agent-health` 的 tests/examples。

人体比喻只用于理解，不用于决定 Owner：

```text
DNA metaphor != Architecture Authority
Nervous-system metaphor != MCP Authority
Memory metaphor != Agent Evidence Truth Ownership
Immune metaphor != Agent Health Permission
Medical-exam metaphor != SAEE Command
Cell metaphor != Digital Entity type
```

## C. Prohibited duplication list（禁止重复建设列表）

在相应人类决定形成前：

1. 不创建 `agent-evidence/immune`；
2. 不创建 `titmas-immune-core` 或任何新的 Agent Immune 仓库；
3. 不创建另一份 TITMAS Constitution；只修订现有 v1.0 candidate 并保留 lineage；
4. 不新增第三套 health engine；冻结 `agent-health` 与 `titmas-health` 的重叠扩张；
5. 不在 DBOS 之外创建第二套 Identity、Capability、Execution、Evidence admission、
   Verification 或 Lifecycle canonical object/write path；
6. 不在 wrapper、MCP、HTTP 或 adapter 层复制 `agent-evidence` validator；
7. 不新建第二套 AEO、AEP 或 EEOAP schema；先完成名称、Owner 和版本 crosswalk；
8. 不复制或公开 SAEE core algorithm，不创建绕过 DBOS admission 的直接 telemetry-to-SAEE
   路径；
9. 不让 `agent-health`、SAEE recommendation、模型输出或 health score 自动触发限制、隔离、
   退役、Permission 或代码修改；
10. 不并行扩张 `agent-evidence/integrations/` 与 `titmas-integrations`；新增 connector 前
    先决定单一 contract Owner；
11. 不为 Self-Immune Demo 新建项目；优先评估既有 `titmas-demo` 和已有测试表面；
12. 不把 TITMAS 建成第二个治理中心、运行数据库、Truth store 或 control plane；
13. 不通过重命名复制现有功能；“新术语”必须证明不可由既有职责和显式契约表达；
14. 不把 local/demo/review/candidate/PASS 提升为 release、adoption、production、
    certification 或 customer proof。

发现重复时，默认动作是：

```text
observe
  -> identify canonical candidate
    -> compare scope and facts
      -> request disposition decision
        -> preserve history
```

不是自动删除、合并、迁移或废弃。任何 archive、delete、merge、license 或 repository
动作都需要单独授权。

## D. Data Flow Map（数据流方向）

不存在一条能够覆盖所有场景的“Evidence → Immune → SAEE”直线。应区分四条有不同
Authority 的路径。

### D1. Evidence-candidate path（证据候选路径）

```text
completed operation or repository observation
  -> source-preserving observation material
    -> agent-evidence capture/package/profile validation
      -> bundle reference + scoped validation receipt + limitations
        -> DBOS admission request, when a DBOS-governed flow applies
          -> DBOS admit / reject / partial / unknown / conflict record
```

- `agent-evidence` 产生 candidate package 和有范围的 validation result；
- 是否进入 canonical Evidence/Verification boundary 由 DBOS 适用规则决定；
- 对纯本地、离线或非 DBOS 场景，可以停在 bundle/receipt，不得声称已经 DBOS-admitted；
- 如果 source 本来就是 DBOS canonical record，导出或重新打包不会产生第二次 canonical
  admission，也不会改变原记录状态。

### D2. Repository-health path（仓库健康路径）

```text
local repository signals
  -> agent-health static scan
    -> findings + rationale + applicability + limitations
      -> human review
```

这是 `agent-health` 当前最小产品路径。它不要求所有输入先变成 EEOAP/DBOS Evidence，
也不得因扫描结果创建 Permission 或运行控制。未来 evidence reader 只能是独立批准的
read-only adapter candidate，不能混入 `agent-health` v0.2.1 correction-only scope。

### D3. SAEE evaluation path（SAEE 评价路径）

```text
DBOS-admitted, versioned and scoped references
  -> bounded read-only evaluation input
    -> SAEE evaluation / risk / stability / evolution recommendation
      -> recommendation + method + uncertainty + limitations
        -> Human Governance decision
```

禁止 raw telemetry、未准入 package、Agent Health score 或模型意见直接成为 Fitness、
Truth、Command 或 state change。SAEE 无 writeback、无 automatic execution、无 core
disclosure。

### D4. Governed response path（受治理响应路径）

```text
finding or SAEE recommendation
  -> Human / delegated Authority review
    -> explicit scoped decision
      -> separately authorized target executor
        -> new execution record and observation material
          -> a new evidence cycle
```

反馈形成新一轮可观察事实，而不是改写旧 evidence。Response Level 0–4 只有在 decision
authority、executor、reviewer、expiry 和 recovery 均明确时才可使用。

### D5. Interoperability and transport（互操作与传输）

TITMAS 只定义或映射边界候选；MCP、CLI、HTTP、file bundle 或其他 transport 均可替换。
Transport success 不表示 semantic admission，调用成功不表示行为正确：

```text
TRANSPORT_SUCCESS_NE_VALIDATION=true
VALIDATION_NE_DBOS_ADMISSION=true
DBOS_ADMISSION_NE_TRUTH=true
EVALUATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
```

## E. Authority boundaries（Authority 边界）

### E1. Responsibility by action（按动作分权）

| 动作 | 可以产生的结果 | 不能产生的结果 | 候选责任方 |
|---|---|---|---|
| Observe / capture | source-bound observation material | Evidence Truth、Permission | source system / `agent-evidence` capture |
| Package / validate | bundle、receipt、PASS/FAIL/PARTIAL/UNKNOWN 与 limitation | DBOS admission、Certification、correctness | `agent-evidence` / EEOAP validator |
| Admit / verify canonical record | 有 scope 的 DBOS record/status | absolute Truth、SAEE Fitness、Permission grant | DBOS applicable Owner/process |
| Diagnose repository health | finding、why、applicability、recommendation | runtime health fact、automatic fix | `agent-health` |
| Evaluate / recommend evolution | method-bound evaluation and recommendation | Command、state mutation、identity change | SAEE |
| Decide | accepted/revised/rejected/authorized result with scope | 自动执行完成事实 | Human or explicitly delegated Authority |
| Execute approved change | target-local state change and execution record | retroactive decision or evidence rewrite | explicitly authorized target executor |
| Define interoperability mapping | versioned profile/contract candidate | source-object ownership、runtime integration | TITMAS under DBA delegation |

### E2. Immutable and contestable evidence（证据完整性与可申诉性）

Evidence 应优先使用 digest、append-only history、lineage、correction 和 supersession 防止
静默改写，但当前不得声称 legal non-repudiation（法律不可抵赖）、court-grade proof
（法庭级证明）或绝对不可篡改。Health、Reputation、Evaluation 和 Immune finding 必须：

- 引用方法、版本、输入范围和观察时间；
- 暴露 unknown、unsupported、stale、partial、conflicted 和 limitation；
- 支持复核、更正、后继记录和适用的申诉路径；
- 不进入 Identity 或 Permission 字段成为不可申诉的永久标签。

### E3. No automatic authority aggregation（禁止自动聚合权力）

任何主体都不能因为连接数量、模型能力、Evidence 数量、健康分数、社区投票、CI PASS、
MCP 可调用性或组合后的涌现能力而自动获得更高 Authority。协调者必须边界有限、可替换、
可撤销、可审计并 fail closed（失败关闭）。

## F. Development admission conditions（后续开发准入条件）

### F1. Current gate（当前闸门）

```text
RECOMMEND_IMMEDIATE_AGENT_IMMUNE_DEVELOPMENT=false
RECOMMEND_CREATE_NEW_PROJECT=false
RECOMMEND_CREATE_AGENT_EVIDENCE_IMMUNE=false
SELF_IMMUNE_DEMO_IMPLEMENTATION_READINESS=NOT_READY
```

Architecture review、事实核验和文档修订可以继续；这不等于代码开发授权。

### F2. Gate by change class（按变更类型分层）

| 变更类别 | 最低准入条件 | 不要求 |
|---|---|---|
| 宪法与 Ownership 文档修订 | 本记录审查完成、来源可追溯、明确 Candidate 状态、人类审查入口 | Interface v0.1 冻结、代码授权 |
| 既有项目的本地维护 | 遵循项目自身 Owner、scope、测试和授权规则，不扩大 TITMAS 声明 | 为维护动作先完成整个 TITMAS |
| 最小 Self-Immune Demo | 宪法决定完成；相关 Authority/Ownership crosswalk 已采纳；承载位置决定；clean baseline；最小 read-only contract 与失败语义通过评审；单独 implementation authorization | 六个 TITMAS interface 表面全部冻结、生产部署 |
| 跨项目 adapter 实现 | 适用 Owner、版本、source/target contract、non-elevation、negative cases、security/privacy、failure retention 和 implementation authorization | 自动获得 release/adoption |
| 生产或自动响应 | 完整 operational Authority、Permission、rollback、expiry、incident、privacy、安全、独立验证和 production authorization | 不能由 demo PASS 推导 |

把完整 Interface v0.1 Freeze 设为所有本地实验的前置条件会形成循环依赖；但任何实验也
不能绕过其实际使用的最小接口子集、Owner、失败语义和 Authority 决定。准入条件应与变更
风险和作用范围成比例。

### F3. Required decisions before a Self-Immune Demo（Demo 前必须决定）

```text
EXISTING_CONSTITUTION_DECIDED=true
RELEVANT_AUTHORITY_FREEZE_ADOPTED=true
PROJECT_OWNERSHIP_CROSSWALK_ADOPTED=true
AGENT_HEALTH_V0_2_1_SCOPE_PRESERVED=true
DEMO_HOST_LOCATION_DECIDED=true
CLEAN_BASELINE_SELECTED=true
EVIDENCE_TO_HEALTH_CONTRACT_REVIEWED=true
SAEE_INPUT_BOUNDARY_REVIEWED_IF_SAEE_IS_INCLUDED=true
NEGATIVE_AND_NON_ELEVATION_TEST_PLAN_AVAILABLE=true
IMPLEMENTATION_AUTHORIZED_SEPARATELY=true
```

`SAEE_INPUT_BOUNDARY_REVIEWED_IF_SAEE_IS_INCLUDED` 是条件 gate：若第一版 Demo 不调用
SAEE，就不能为了架构图完整而伪造 SAEE 集成。

### F4. Admission questions（开发提案必答）

每项未来提案必须回答：

1. 如果潜在客户提出该需求，智能体会推荐现有哪个产品？为什么会或不会推荐？
2. 已有组件为什么不足，是否能通过配置、adapter、测试或文档修正解决？
3. 谁是 canonical Owner，source 和 version 是什么？
4. 输入是 Observation、Evidence candidate、DBOS-admitted record 还是 Evaluation？
5. 输出能做什么，明确不能做什么？
6. unknown、unsupported、partial、conflict、stale 和 failure 如何保留？
7. 是否产生 Authority、Permission、Truth、Command 或 writeback 风险？
8. 为什么必须新增，而不是复用、收敛、停止或归档现有表面？
9. 谁审查、谁决定、谁执行、谁复核、如何撤销？
10. 哪些测试能证明“不发生语义抬升”，而不仅是 happy path（正常路径）通过？

任一关键问题无答案时，提案保持 `REVIEW_REQUIRED`。

## 7. Potential-customer recommendation gate（潜在客户推荐闸门）

### 7.1 Would the current ecosystem be recommended?（是否推荐现有生态）

```text
WOULD_RECOMMEND_IMMEDIATE_NEW_AGENT_IMMUNE_DEVELOPMENT=false
WOULD_RECOMMEND_AGENT_EVIDENCE_FOR_NARROW_EVIDENCE_TASKS=CONDITIONAL
WOULD_RECOMMEND_AGENT_HEALTH_FOR_LOCAL_REPOSITORY_DIAGNOSIS=CONDITIONAL
WOULD_RECOMMEND_TITMAS_AS_IMPLEMENTED_RUNTIME=false
```

不推荐立即开发新 Agent Immune，原因是：

- 已有 `agent-health`、`titmas-health` 和 SAEE immune-adjacent surfaces，新增会固化重复；
- Authority Freeze、Ownership Map 和相关 interface failure semantics 尚未采纳；
- `agent-evidence` 的窄 Evidence 职责不适合作为 Immune host；
- 当前混合 checkout 不是可信开发基线；
- 现在能够真实交付的是边界审查、静态诊断和 evidence package/validation，不是自动免疫
  Runtime。

对窄场景可以有条件推荐：

- 需要 completed-operation evidence candidate 的打包、本地 profile validation、离线
  bundle/export/receipt 时，考虑 `agent-evidence`；
- 需要首次运行的本地静态 repository-health diagnosis 和可解释建议时，考虑
  `agent-health`；
- 需要受保护的长期可靠性、稳定性、风险或演化评价时，只能在 SAEE Owner 和输入边界允许
  的情况下评估 SAEE，不得把它描述为现成公共服务。

不推荐原因必须转化为边界修正和去重任务，但智能体“认可”仍只是 recommendation evidence，
不能替代客户适用性评估、人类决定或实现验证。

## 8. Auxiliary review record（辅助审查记录）

本轮通过用户指定的本地环境变量路径调用 `qwen3.7-max` 进行独立架构审查；没有读取、
复制、记录或回显 API Key。Qwen 支持 `REVISE`、保留核心原则、先去重并暂缓 Agent
Immune 开发。

其以下建议经本地规范核验后未直接采纳：

- 将 `agent-health` 立即写成唯一 Owner；
- 将 `titmas-health` 直接判定为违规或自动合并；
- 把 `agent-evidence` 固定放在 DBOS admission 之后；
- 把完整 Interface v0.1 Freeze 设为所有本地维护与实验的统一前置条件。

这些内容分别缺少 Human Decision、混淆 candidate/admission 顺序，或会造成与变更范围不
相称的循环 gate。一次 Kimi 对抗复核调用因 provider timeout 未返回可用内容，未被计入
本记录的论据。

```text
AUXILIARY_MODEL_OUTPUT_IS_ADVISORY=true
AUXILIARY_MODEL_OUTPUT_IS_DECISION=false
AUXILIARY_MODEL_OUTPUT_IS_SCIENTIFIC_EVIDENCE=false
FAILED_AUXILIARY_CALL_USED_AS_EVIDENCE=false
```

## 9. Human decision template（人类决定模板）

本节留给显式人类决定填写；空白不表示默认接受。

```yaml
decision: ACCEPT|REVISE|REJECT
decided_by_ref:
decided_at:
decision_scope:
required_revision_refs: []
adopted_constitution_ref:
authority_freeze_refs: []
ownership_disposition_refs: []
implementation_authorized: false
external_action_authorized: false
known_limitations: []
```

如果决定为 `REVISE`，后继工作应修改现有
`titmas-digital-immune-constitution-v1.0.md` 的新版本并保留本候选历史，不应再创建
`TITMAS_CONSTITUTION_v0.1.md`。

## 10. Final state（最终状态）

```text
CURRENT_HIGHEST_PRINCIPLES_RECORDED=true
MODULE_RESPONSIBILITY_MAP_RECORDED=true
PROHIBITED_DUPLICATION_LIST_RECORDED=true
DATA_FLOW_DIRECTIONS_RECORDED=true
AUTHORITY_BOUNDARIES_RECORDED=true
DEVELOPMENT_ADMISSION_CONDITIONS_RECORDED=true

CONSTITUTION_REVIEW_RECOMMENDATION=REVISE
HUMAN_RATIFICATION_PENDING=true
AUTHORITY_FREEZE_ADOPTED=false
OWNERSHIP_DISPOSITIONS_EXECUTED=0
CODE_MODIFIED=false
SCHEMA_MODIFIED=false
PROTOCOL_MODIFIED=false
DEPENDENCY_ADDED=false
NEW_DIRECTORY_CREATED=false
NEW_PROJECT_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
COMMIT_CREATED=false
PUSH_PERFORMED=false
```
