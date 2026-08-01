---
document_id: DBA-ATTENTION-PRINCIPLE-REVIEW-20260728-001
title: Adaptive Attention Allocation Principle Review v0.1
title_zh: 自适应注意力分配原则审查 v0.1
status: REVIEW_COMPLETE_PASS_WITH_REQUIRED_BOUNDARIES
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
document_type: NON_EXECUTABLE_CONSTITUTION_REVISION_REVIEW
reviewed_at: 2026-07-28
review_sequence: RETROSPECTIVE_DIRTY_WORKTREE_REVIEW
concept_alignment: PASS_WITH_REQUIRED_BOUNDARIES
standalone_constitution_principle: NOT_RECOMMENDED
constitutional_guardrail: CONDITIONALLY_RECOMMENDED
architecture_pattern: RECOMMENDED
capability_pattern: OPTIONAL_FUTURE_CANDIDATE
human_decision_status: PENDING_FOR_REVIEW_DISPOSITION
authority_effect: NONE
implementation_effect: NONE
schema_effect: NONE
protocol_effect: NONE
runtime_effect: NONE
repository_effect: NONE
external_action_effect: NONE
---

# Adaptive Attention Allocation Principle Review v0.1

中文：自适应注意力分配原则审查 v0.1。

## 0. Review boundary and current-state correction（审查边界与当前状态纠正）

本文件审查 Adaptive Attention Allocation Principle（自适应注意力分配原则）是否适合进入
Digital Biosphere 的 constitutional layer（宪法约束层）。它只审查概念、Authority、
架构定位、Evidence/Health/Evaluation 关系与建议位置。

本文件：

- 不创建 Attention Layer、Coordination Layer、allocator、router、Runtime 或 Agent；
- 不定义字段、权重算法、评分模型、Schema、API、Protocol 或实现；
- 不修改任何现有文件；
- 不授权实验、开发、部署、自动路由、自动选择或真实数据收集；
- 不替代 Human Architecture Decision。

### 0.1 Observed worktree sequence（观察到的工作树顺序）

在本审查文件创建前，当前 dirty worktree（脏工作树）已经出现：

- `architecture/ADR-033-attention-principle-for-dynamic-coordination.md`，文件内声明
  `Status: ACCEPTED` 和 `ATTENTION_PRINCIPLE_ADOPTED=true`；
- `PROGRAM-CHARTER.md` 的未提交 Attention amendment；
- `architecture/open-infrastructure-strategy-constitution.md` 从 v0.3 到 v0.4 的未提交修订；
- `TITMAS_CONSTITUTION_REVISION_PROPOSAL_v1.1.md` 中的
  `Principle 1A. Attention and Dynamic Coordination`；
- ADR-033 将 `DBA-ATTENTION-PRINCIPLE-REVIEW-20260728-001` 写为 review reference，
  但本审查工件当时尚不存在。

Git 核验显示：

```text
ADR_033_TRACKED=false
PROGRAM_CHARTER_ATTENTION_CHANGE=MODIFIED_WORKTREE
STRATEGY_CONSTITUTION_V0_4_CHANGE=MODIFIED_WORKTREE
CURRENT_HEAD=6cc94b5bca6bcee7e3c6651321915ffb4ad6133f
CURRENT_BRANCH=codex/production-observability-baseline
CURRENT_BRANCH_AHEAD=1
CURRENT_BRANCH_BEHIND=360
REMOTE_OR_PUBLIC_ATTENTION_ADOPTION_VERIFIED=false
```

因此，本审查不能把当前 worktree 的 `ACCEPTED` 字样自动升级为已提交、已发布或已完成
先行审查的 canonical adoption。准确状态是：

```text
WORKTREE_DECLARATION_ATTENTION_PRINCIPLE_ADOPTED=true
PRE_DECISION_REVIEW_SEQUENCE_SATISFIED=false
THIS_REVIEW_RETROACTIVELY_AUTHORIZES_ADR_033=false
HUMAN_REVIEW_DISPOSITION_STILL_REQUIRED=true
```

这不否定 Principle 的概念价值；它要求把“概念适配性”和“程序有效性”分开。

### 0.2 Overall verdict（总览结论）

```text
CONCEPT_FIT=PASS_WITH_REQUIRED_BOUNDARIES
CONSTITUTIONAL_GUARDRAIL=CONDITIONALLY_RECOMMENDED
PRIMARY_PLACEMENT=ARCHITECTURE_PATTERN
OPTIONAL_IMPLEMENTATION_FORM=CAPABILITY_PATTERN_CANDIDATE
STANDALONE_TOP_LEVEL_CONSTITUTION_PRINCIPLE=NOT_RECOMMENDED
IMPLEMENTATION_AUTHORIZED=false
```

建议保留 Attention 的 constitutional guardrail（宪法护栏）：

> 注意力分配必须分布式、有界、可解释、可质疑、可撤销、会过期，并不得产生
> Permission、Authority、Truth、Decision 或 Execution。

候选优先级、资源分配、探索机制和反馈更新属于 Architecture Pattern；任何实际
attention allocator 属于未来 Capability Pattern。把三者都写成一个“宪法原则”会让
工程机制获得过高位阶，并产生隐藏调度权。

## 1. Concept Alignment

### 1.1 Ecological Self-Limitation（生态自限）

**Alignment: `STRONG_WITH_GUARDS`**

Attention 与 Ecological Self-Limitation 高度一致，因为注意力、算力、时间、带宽和人类
复核能力都是有限资源。对相关主体临时提高关注、对无关连接降低资源消耗，有助于避免：

- 所有 Agent 永久连接；
- 所有事件都进入同一中心；
- 单一强主体吞并全部任务；
- 无边界扩张造成资源耗尽。

但它只有在以下条件下才保持自限：

- 不存在必须经过的单一全局 allocator；
- 分配范围绑定 task、context、budget 和 expiry；
- 不把历史高权重转化为永久地位；
- 不把低权重或未选中解释为失去生态资格；
- local failure 不扩散为全局 attention failure；
- 协调机制可替换、可撤销且不成为唯一入口。

如果一个 Attention 组件掌握所有候选可见性、任务入口和资源预算，它会成为 ADR-032
禁止的隐藏无限强中心，即使它声称输出只是 recommendation。

### 1.2 Agent Autonomy（Agent 自治）

**Alignment: `CONDITIONAL`**

Attention 可以帮助 Agent 在自身 Capability、Authorization、资源和目标边界内决定关注
什么，也可以帮助多个 Agent 协商临时协作。但 Agent Autonomy 要求：

- Agent 可以在适用规则内接受、拒绝或退出 attention proposal；
- Attention 不得强制主体参与；
- Attention 不得扩大 Agent 的 Capability 或 Permission；
- 未被选中不改变 Identity、Lifecycle 或未来参与资格；
- Agent 的本地资源策略不被一个隐藏全局分数永久覆盖；
- 高风险协作继续受 Human Authority Gate 和适用 Authorization 约束。

必须把以下两句话分开：

```text
Attention proposes who should be considered among eligible candidates.
Attention does not decide who is authorized to participate.
```

中文：

```text
Attention 在已具备候选资格的集合中提出优先考虑建议。
Attention 不决定谁获得实际参与授权。
```

### 1.3 Evidence First（证据优先）

**Alignment: `STRONG_WITH_NON_ELEVATION`**

Attention 可以使用 source-bound（带来源）、scoped（有范围）、time-bound（有时间边界）
的 Evidence/Verification reference 作为候选相关性信号。它也应记录：

- 哪些候选被考虑；
- 使用了哪些来源与版本；
- 为什么提高或降低优先级；
- 哪些 unknown、limitation 和 conflict 被保留；
- proposal 何时过期或被撤销。

但 Evidence First 不表示 Evidence 必须成为 Attention 的唯一输入，也不表示 Evidence
越多的 Agent 就越重要。必须防止：

- Evidence 数量变成声誉或权限；
- validator `PASS` 变成候选参与资格；
- 格式完整度替代任务相关性；
- 为获得注意力而产生表演式、低信息量 Evidence；
- 难以结构化的新信息被永久忽视；
- Attention priority 被当成 Evidence quality。

```text
EVIDENCE_CAN_INFORM_ATTENTION=true
EVIDENCE_DOES_NOT_COMMAND_ATTENTION=true
ATTENTION_PRIORITY_NE_EVIDENCE_QUALITY=true
ATTENTION_SELECTION_NE_EVIDENCE_TRUTH=true
```

### 1.4 Bounded Autonomy（有界自治）

**Alignment: `REQUIRED_PARENT_BOUNDARY`**

Adaptive Attention 只有作为 Bounded Autonomy 的从属机制才安全。最低约束包括：

- 输入来源有界；
- 候选集合有界；
- 资源预算有界；
- 输出范围有界；
- 建议有效期有界；
- 影响对象有界；
- 失败影响局部化；
- 允许 override、appeal、revocation 和 expiry；
- policy 和 method version 可追溯；
- 不因模型连接更多而自动扩大权限。

Attention proposal 不能越过：

```text
Capability + Authorization + Context + Current Constraints
```

它只能在该边界内部帮助排序或协商，不能创造该边界。

### 1.5 Evolution Through Feedback（通过反馈演化）

**Alignment: `CONDITIONAL_WITH_ANTI_LOCK_IN`**

Attention outcome 可以产生新 observation，后续 Evidence 和 SAEE evaluation 可以帮助
Human Governance 判断是否调整 attention policy。但正确反馈路径是：

```text
attention proposal
  -> authorized coordination
    -> execution
      -> new observation / evidence candidate
        -> DBOS admission, when applicable
          -> SAEE method-bound evaluation
            -> recommendation
              -> Human policy decision, when required
                -> new versioned attention policy
```

禁止：

```text
SAEE recommendation -> direct attention weight writeback
historical success  -> permanent priority
attention selection -> more evidence -> higher attention -> monopoly
```

为了避免 feedback lock-in（反馈锁定），Architecture Pattern 应保留：

- time decay（时间衰减）；
- exploration capacity（探索容量）；
- new/unknown candidate channel（新／未知候选通道）；
- diversity and anomaly review（多样性与异常复核）；
- negative and disputed outcome retention（负面与争议结果保留）；
- method/version change review（方法／版本变化审查）。

本审查不定义具体算法或阈值。

### 1.6 Alignment summary（对齐总结）

| 既有原则 | 对齐程度 | 必须增加的边界 |
|---|---|---|
| Ecological Self-Limitation | `STRONG` | 无单一全局 allocator、可替换、局部失效 |
| Agent Autonomy | `CONDITIONAL` | 接受／拒绝／退出、不得强制参与 |
| Evidence First | `STRONG_WITH_GUARDS` | Evidence 不是排名、权限或唯一信号 |
| Bounded Autonomy | `FOUNDATIONAL` | scope、budget、expiry、revocation、appeal |
| Evolution Through Feedback | `CONDITIONAL` | 新记录、新版本、无 SAEE direct writeback、反锁定 |

## 2. Authority Impact Review

### 2.1 Does Attention create new Authority?（是否产生新 Authority）

**Formal result: `NO`, if kept as a bounded proposal pattern.**

Attention 不产生正式 Authority 的条件是：

- 输出只能是 candidate participation proposal（候选参与建议）；
- 输入不扩大 Capability、Permission 或 eligibility；
- 实际参与需要适用 Authorization；
- 高影响 policy change 继续经过 Human Authority；
- 任何 override、expiry、revocation 和 appeal 均可用；
- Attention provider 不拥有 Identity、Evidence admission、Evaluation 或 Decision。

但 Attention 会形成 **de facto visibility power（事实可见性权力）**：

> 控制谁被看见、谁被邀请、谁获得计算资源，即使不授予 Permission，也可能实质影响结果。

因此“没有 Authority 字段”不足以证明没有权力。必须审查：

- 谁定义相关性；
- 谁选择输入；
- 谁调整 method/weight；
- 谁能被系统看见；
- 谁长期未被选择；
- 是否存在默认自动接受；
- 是否允许多种 allocator/policy 并存；
- 是否能发现 attention capture 和 starvation。

### 2.2 Central-control review（中心控制审查）

以下形态与去中心化原则冲突：

- 一个全局、不可替换的 Attention controller；
- 所有任务必须经过同一排序器；
- 一个永久 global agent ranking；
- 一个同时拥有 candidate eligibility、priority、Permission 和 execution 的组件；
- 一个由 SAEE 自动更新、不可人工复核的全局权重；
- 一个将 Cockpit 可见性直接转换为任务资源的中心；
- 一个因掌握更多连接而自动取得架构权力的协调服务。

安全定位应是：

```text
local or federated attention proposals
  + explicit task scope
  + bounded resource budgets
  + optional negotiation
  + expiring relationships
  + independent authorization
  + traceable outcomes
```

“去中心化”不要求取消协调，但协调必须有限、可替换、可拒绝、可撤销和可审计。

### 2.3 Human Authority Gate（人类权威闸门）

Attention Principle 不改变 Human Authority Gate。

可以在既有授权范围内由 Agent 本地进行低风险 prioritization（优先级安排），但以下事项
仍需适用 Human/Delegated Authority：

- 新增或扩大 Permission；
- 改变全局或跨项目 policy；
- 强制某 Agent 参与；
- 限制、隔离、撤权或退役；
- 将 candidate proposal 自动转为 execution；
- 修改 Evidence admission 或 SAEE evaluation rule；
- 部署一个强制全局 Attention service；
- 使用敏感、受限或个人数据作为 attention signal。

```text
ATTENTION_DOES_NOT_CHANGE_HUMAN_AUTHORITY_GATE=true
ATTENTION_PROPOSAL_NE_HUMAN_DECISION=true
HUMAN_DECISION_NE_AUTOMATIC_EXECUTION=true
```

Human 频繁无审查接受 Attention 默认建议，会造成 gate 的事实弱化。因此任何未来高影响
使用都应保留 meaningful override（有意义的覆盖）、reason 和 non-default review；
本审查不规定具体 UI 或流程。

### 2.4 Authority verdict（权力结论）

```text
NEW_FORMAL_AUTHORITY_REQUIRED=false
DE_FACTO_VISIBILITY_POWER_RISK=HIGH
CENTRAL_CONTROLLER_ALLOWED=false
HUMAN_AUTHORITY_GATE_CHANGED=false
AUTOMATIC_SELECTION_AUTHORIZED=false
AUTOMATIC_EXECUTION_AUTHORIZED=false
```

## 3. Architecture Impact

### 3.1 Classification decision（分类决定）

| 选项 | 结论 | 适用内容 |
|---|---|---|
| **A. Constitution Principle** | `CONDITIONALLY_RECOMMENDED_AS_GUARDRAIL_ONLY` | 分布式、有界、非抬升、反垄断、可撤销、会过期 |
| **B. Architecture Pattern** | **`RECOMMENDED_PRIMARY_CLASSIFICATION`** | 候选形成、优先建议、协商、资源预算、失败和反馈边界 |
| **C. Capability Pattern** | `OPTIONAL_FUTURE_CANDIDATE` | 某 Agent/服务的本地 allocator 或 negotiation capability |

不建议将“Adaptive Attention Allocation”整体作为独立顶级宪法原则。宪法只需要规定
不可突破的 guardrail；具体动态分配机制是 Architecture Pattern；实现才是 Capability
Pattern。

### 3.2 Attention Layer（注意力层）

**Recommended status: `LOGICAL_CROSS_CUTTING_PATTERN`, not a new layer.**

Attention Layer 可以用于解释：

- 根据 task/context 形成候选相关性；
- 在已具备 eligibility 的集合中产生可解释优先建议；
- 管理有限关注预算和 proposal expiry。

它不应成为：

- 新 Portfolio component；
- 所有 Agent 必须连接的 central service；
- Identity/Capability registry；
- global ranking database；
- Permission allocator；
- Evidence admission service；
- SAEE controller。

### 3.3 Coordination Layer（协调层）

**Recommended status: `ARCHITECTURE_PATTERN`.**

Coordination 只接收已具备适用 Capability/Authorization/Context 的候选建议，并负责形成
有范围、临时、可退出的协作。它必须区分：

```text
eligible
  != prioritized
  != invited
  != accepted
  != authorized
  != executed
  != verified successful
```

Attention 不得把这些状态压成单一“selected”。

### 3.4 Evidence Layer（证据层）

**Recommended status: `INDEPENDENT_CANONICAL_BOUNDARY`.**

Attention 可以读取允许使用的 source-bound evidence/verification reference，也可以产生
关于 proposal、invite、accept/decline、coordination 和 execution 的新 observation。

但：

- Attention 不决定材料是否成为 canonical Evidence；
- Agent Evidence 只负责 candidate capture/package/local validation；
- DBOS 保持 Evidence admission/Verification canonical boundary；
- priority 不证明 Evidence quality；
- not selected 不证明主体不可靠；
- Attention trace 可以成为 Evidence candidate，不自动成为 Truth。

### 3.5 Memory / Evolution Layer（记忆／演化层）

**Recommended status: `FEEDBACK_SOURCE_PATTERN`, not a controller.**

Memory/Evolution 可以保存有治理、带版本、带争议和带时间的 outcome reference。SAEE 可以
对 admitted inputs 形成只读评价和演化建议。但：

- 历史成功不是永久 priority；
- Reputation 不是 Identity、Permission 或 Truth；
- SAEE 不直接更新 Attention weight；
- Attention 不直接训练／修改自身 policy；
- policy change 形成新版本和新决定，不静默覆盖历史；
- negative、unknown 和 never-selected candidates 不能从历史中消失。

### 3.6 Architecture projection（架构投影）

推荐：

```text
task/context + eligible candidate references + bounded signals
                     |
                     v
       Distributed Attention Pattern
       (advisory, scoped, expiring)
                     |
                     v
       candidate participation proposal
                     |
                     v
     authorized temporary coordination
                     |
                     v
                  execution
                     |
                     v
       observation / Evidence candidate
                     |
                     v
       DBOS admission, when applicable
                     |
                     v
        SAEE evaluation / recommendation
                     |
                     v
      Human policy decision, when required
                     |
                     v
       new versioned attention policy
```

最后一条反馈必须经过新版本和适用决定，不能画成 `SAEE -> Attention controller`
直接 writeback。

## 4. Non-Elevation Rules

### 4.1 Required constitutional invariants（必须保留的不变量）

```text
ATTENTION_NE_PERMISSION=true
ATTENTION_NE_AUTHORITY=true
ATTENTION_NE_TRUTH=true
ATTENTION_NE_DECISION=true
ATTENTION_NE_EXECUTION=true
```

### 4.2 Extended non-elevation rules（扩展非抬升规则）

```text
ATTENTION_PRIORITY_NE_BEST_AGENT_PROOF=true
ATTENTION_WEIGHT_NE_CAPABILITY=true
ATTENTION_SELECTION_NE_AUTHORIZATION=true
ATTENTION_PROPOSAL_NE_COMMAND=true
ATTENTION_VISIBILITY_NE_ECOLOGICAL_VALUE=true
HIGH_ATTENTION_NE_HIGH_TRUST=true
LOW_ATTENTION_NE_LOSS_OF_IDENTITY=true
NOT_SELECTED_NE_UNQUALIFIED=true
EVIDENCE_VOLUME_NE_ATTENTION_ENTITLEMENT=true
EVIDENCE_QUALITY_NE_AUTHORITY=true
REPUTATION_NE_PERMISSION=true
SAEE_RECOMMENDATION_NE_ATTENTION_WRITEBACK=true
```

### 4.3 Forbidden descriptions（禁止描述）

Attention 不得被描述为：

- 总控智能；
- 中央调度器；
- 自动选择最佳 Agent；
- 权限分配系统；
- 全局信誉排名；
- DBOS admission gate；
- SAEE 的执行器；
- Cockpit 的命令面；
- 自动优化、自我演化或自动淘汰系统；
- Transformer、生物神经系统或意识的已实现等价物。

推荐用语：

```text
bounded candidate prioritization
distributed attention proposal
temporary coordination signal
contestable and expiring relevance suggestion
```

避免：

```text
best-agent selection
global attention authority
central intelligence router
automatic participant decision
```

## 5. Agent Evidence Relationship

### 5.1 Corrected three-part relationship（修正后的三方关系）

用户提出：

```text
Attention: 决定谁参与
Evidence: 证明发生什么
SAEE: 评价是否继续演化
```

建议修订为：

```text
Attention:
  在已经具备适用 eligibility、Capability、Authorization 和 Context 的候选中，
  提出谁应被优先考虑的有界建议。

Agent Evidence:
  捕获、打包和本地验证关于 proposal、participation、execution 与 result 的
  Evidence candidate；不决定 canonical Evidence 或 Truth。

DBOS:
  在适用规则下处理 Evidence admission、Verification 和 canonical record reference。

SAEE:
  对已接纳、有来源、有范围且带限制的输入进行只读评价，
  建议某种 coordination/evolution policy 是否值得继续、修订或停止。

Human Authority:
  在需要时决定 policy、授权和高影响变化。
```

Attention 不决定实际参与。实际参与至少需要：

```text
eligible candidate
  + applicable authorization
  + candidate acceptance or valid coordination rule
  + current context and constraints
```

### 5.2 Evidence directions（Evidence 方向）

允许：

```text
Evidence/Verification reference
  -> bounded attention signal

Attention proposal + coordination outcome
  -> new observation material
    -> Agent Evidence candidate package
      -> DBOS admission request, when applicable
```

禁止：

```text
Agent Evidence PASS -> attention entitlement
attention priority  -> Evidence Truth
not selected        -> negative Evidence
SAEE recommendation -> direct attention weight update
```

### 5.3 Health relationship（Health 关系）

Agent Health 当前职责是本地静态 repository-health diagnosis，不是 Attention provider。
未来 Health finding 如果被用作 attention signal，必须：

- 绑定 repository snapshot、method、version 和 time；
- 保留 applicability 和 limitation；
- 不升级为 Permission、Fitness 或 runtime safety；
- 不因低 Health score 自动排除 Agent；
- 经过单独 Owner/interface review。

本审查不建立该接口。

### 5.4 Cockpit relationship（Cockpit 关系）

DBA Cockpit 内的 TITMAS Situational View 可以展示：

- attention concentration risk；
- candidate starvation；
- stale or disputed signals；
- proposal expiry；
- related Evidence/Health/Evaluation references；
- Human decision required。

它不排序 Agent、不分配任务、不修改 priority，也不执行 recommendation。

## 6. Recommended Placement

### 6.1 Should it enter the Constitution?（是否加入 Constitution）

**Recommendation: `YES_AS_A_BOUNDED_GUARDRAIL; NO_AS_A_COMPLETE_ALLOCATION_MECHANISM`.**

建议宪法保留：

1. Attention 必须去中心化、有界、可解释、可质疑、可撤销且会过期；
2. Attention 不产生 Permission、Authority、Truth、Decision 或 Execution；
3. 未选中不影响 Identity、Capability、Permission 或生态资格；
4. 不允许永久 global ranking、单一 mandatory allocator 或 attention monopoly；
5. feedback 必须形成新记录、新评价和新 policy version，禁止 direct writeback；
6. Human Authority Gate 不变。

不建议宪法定义：

- candidate scoring formula；
- feature/weight；
- queue、router 或 allocator topology；
- exploration percentage；
- data structure 或 Schema；
- Runtime、API 或 implementation；
- “最佳 Agent”标准。

### 6.2 Recommended chapter position（建议章节位置）

如果 Human Decision 决定保留本原则，推荐在父级 Digital Biosphere 战略宪法中继续作为
Compositional Scale 的从属条款，而不是独立于所有原则之上的新中心：

```text
Principle 5A — Compositional Scale, Not an Unbounded Center
Principle 5B — Bounded Distributed Attention
```

在 TITMAS v1.1 candidate 中，推荐位置：

```text
Principle 0. Ecological Self-Limitation
Principle 1. Distributed and Compositional Capability
Principle 1A. Bounded Distributed Attention and Coordination
Principle 2. Digital Identity and Existence Boundary
...
Principle 4. Bounded Autonomy
Principle 5. Evidence First
Principle 6. Authority Separation
```

`Principle 1A` 必须显式从属于 Bounded Autonomy、Evidence First 和 Authority Separation，
不能单独定义 participation eligibility 或 authorization。

### 6.3 Does the architecture map need modification?（是否需要修改架构图）

**Recommendation: `NO_NEW_CORE_LAYER_OR_COMPONENT`.**

如果未来修订架构图，只建议增加一条虚线 cross-cutting annotation：

```text
eligible agents / task context
  -- bounded distributed attention proposal -->
authorized coordination
```

不要增加：

- 一个居中的 `Attention Layer` 方框；
- 一个所有组件都必须依赖的 Attention service；
- `SAEE -> Attention` 自动反馈箭头；
- `Evidence -> best-agent selection` 箭头；
- `Cockpit -> Attention control` 箭头。

具体 Architecture Pattern 应在后续独立文档中定义；本审查不创建该文档。

### 6.4 Required revisions to current worktree wording（当前工作树措辞修订建议）

当前 dirty worktree 的 ADR-033 和 Strategy Constitution v0.4 方向基本一致，但在任何人类
复核／提交前建议处理：

1. 将 “Attention 决定候选谁参与” 改为“Attention 提出在 eligible candidates 中谁应被
   优先考虑”；实际参与仍需 Authorization 和 acceptance；
2. 将 “Intelligence does not emerge...” 从可能被误读为科学事实的断言，收窄为
   Digital Biosphere 的 architecture design position；
3. 增加 de facto visibility power、attention monopoly 和 agenda-setting risk；
4. 增加 exploration、diversity、unknown/new candidate 和 starvation review；
5. 增加 `NOT_SELECTED_NE_UNQUALIFIED` 与 `HIGH_ATTENTION_NE_HIGH_TRUST`；
6. 禁止 SAEE recommendation direct writeback，反馈必须形成新 policy version；
7. 明确 `Attention Layer` 是 non-runtime logical projection，不是新增 layer/component；
8. 保留 `IMPLEMENTATION_AUTHORIZED=false`；
9. 由 Human 决定现有 ADR-033 `ACCEPTED` 是否保持、修订或退回 Proposal；
10. 不用本审查的存在掩盖“ADR 先写 ACCEPTED、Review 后生成”的时间顺序。

本文件只记录建议，不修改上述文件。

### 6.5 Final placement verdict（最终位置结论）

```text
ADD_TO_CONSTITUTION=CONDITIONAL_GUARDRAIL_ONLY
RECOMMENDED_CONSTITUTION_NAME=BOUNDED_DISTRIBUTED_ATTENTION
PRIMARY_ENGINEERING_CLASS=ARCHITECTURE_PATTERN
OPTIONAL_RUNTIME_CLASS=CAPABILITY_PATTERN_CANDIDATE
ADD_NEW_ARCHITECTURE_LAYER=false
ADD_NEW_CORE_COMPONENT=false
CHANGE_HUMAN_AUTHORITY_GATE=false
```

## 7. Risk and stopping conditions（风险与停止条件）

| 风险 | 触发信号 | 停止条件 |
|---|---|---|
| 隐性 Authority | 单一算法控制可见性、邀请和资源 | 退回 Architecture Review，禁止 adoption/implementation |
| Attention monopoly | 少数主体长期占据大部分机会 | 要求 diversity、exploration、expiry 和 starvation review |
| Feedback lock-in | 历史成功自动累积永久权重 | 禁止 direct writeback，要求新版本与复核 |
| Evidence gaming | Evidence 数量或格式成为 attention entitlement | 删除该信号或降低 scope，保留反方结果 |
| New-agent starvation | unknown/low-history 主体无法进入候选 | 保留 exploration/unknown channel |
| Central scheduler drift | 所有任务必须通过一个 service | 判定与 ADR-032 冲突 |
| Permission drift | priority 被执行器当作授权 | fail closed，要求 explicit authorization |
| Stale context | 过期权重继续参与当前任务 | expiry、freshness 和 re-evaluation required |
| Privacy leakage | attention reason 暴露敏感 Evidence | 最小化输入／展示，进入 privacy review |
| Human rubber-stamping | 默认建议持续无审查转为执行 | 恢复 meaningful override 和高影响人工复核 |

任一核心边界无法回答时：

```text
ATTENTION_PRINCIPLE_IMPLEMENTATION_READINESS=NOT_READY
ATTENTION_INTERFACE_FREEZE_READY=false
```

## 8. Auxiliary agent review（辅助智能体审查）

本轮通过用户指定的安全环境变量路径调用：

- `qwen3.7-max`；
- `deepseek-v4-pro`。

没有读取、复制、记录或回显 API Key。

Qwen 建议把 Adaptive Attention Allocation 的主要定位放在 Architecture Pattern，而不是
完整 Constitution Principle，并识别：

- hidden agenda-setting Authority；
- incumbent/attention monopoly；
- feedback lock-in；
- Evidence gaming 和格式化 Evidence 过度生产；
- new/unknown candidate starvation。

本审查采纳这些风险，但对 Qwen 结论作一项分层修正：Attention 的非中心、非抬升、
可撤销、反垄断 guardrail 具有宪法价值；具体分配机制仍属于 Architecture Pattern。

Qwen 提出的“SAEE 评价应转为 Attention 撤销信号接口”未被直接采纳，因为这可能形成
SAEE writeback。正确路径是 SAEE Recommendation -> Human/Policy Decision -> new
versioned Attention policy。

`deepseek-v4-pro` 两次调用均未返回可用正文：

```text
DEEPSEEK_CURRENT_VERDICT=NO_CURRENT_VERDICT_EMPTY_RESPONSE
FAILED_OR_EMPTY_AUXILIARY_OUTPUT_USED_AS_EVIDENCE=false
```

辅助模型输出不产生 Decision、Authority 或 Authorization。

## 9. Human review disposition（人工复核处置）

由于当前 worktree 已先行写入 `ADR-033 ACCEPTED`，Human Architecture Decision 应明确选择：

```yaml
review_disposition: KEEP_ACCEPTED_WITH_REVISIONS|RETURN_TO_PROPOSAL|REJECT
decided_by_ref:
decided_at:
scope:
adr_033_status_after_review:
strategy_constitution_version_after_review:
program_charter_attention_amendment_after_review:
required_revision_refs: []
implementation_authorized: false
external_action_authorized: false
```

推荐：

```text
REVIEW_RECOMMENDATION=KEEP_DIRECTION_RETURN_WORDING_FOR_REQUIRED_REVISIONS
```

含义：

- 保留 bounded distributed attention 的战略方向；
- 不否定 ADR-033 的概念目标；
- 在把当前 worktree 声明视为正式、可提交的 adoption 前，修正 participation、visibility
  power、anti-monopoly、anti-lock-in 和 review sequence；
- 不授权实现。

## 10. Final non-effects（最终非效果）

```text
CONCEPT_ALIGNMENT_REVIEWED=true
AUTHORITY_IMPACT_REVIEWED=true
ARCHITECTURE_PLACEMENT_REVIEWED=true
NON_ELEVATION_RULES_DEFINED=true
AGENT_EVIDENCE_RELATIONSHIP_REVIEWED=true
RECOMMENDED_PLACEMENT_DEFINED=true

ATTENTION_NE_PERMISSION=true
ATTENTION_NE_AUTHORITY=true
ATTENTION_NE_TRUTH=true
ATTENTION_NE_DECISION=true
ATTENTION_NE_EXECUTION=true
ATTENTION_NE_CENTRAL_CONTROL=true
ATTENTION_NE_BEST_AGENT_SELECTOR=true
HUMAN_AUTHORITY_GATE_CHANGED=false

EXISTING_FILE_MODIFIED=false
CODE_CREATED=false
CODE_MODIFIED=false
SCHEMA_CREATED=false
SCHEMA_MODIFIED=false
PROTOCOL_CREATED=false
PROTOCOL_MODIFIED=false
DEPENDENCY_ADDED=false
IMPLEMENTATION_AUTHORIZED=false
COMMIT_CREATED=false
PUSH_PERFORMED=false
```
