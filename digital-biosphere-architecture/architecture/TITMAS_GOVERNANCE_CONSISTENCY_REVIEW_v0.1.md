---
document_id: DBA-TITMAS-GOVERNANCE-CONSISTENCY-REVIEW-0.1
title: TITMAS Governance Consistency Review v0.1
title_zh: TITMAS 治理一致性审查 v0.1
status: REVISE
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
document_type: NON_EXECUTABLE_GOVERNANCE_CONSISTENCY_REVIEW
reviewed_at: 2026-07-28
architecture_consistency: REVISE
authority_consistency: BLOCK
evidence_first_consistency: REVISE
cockpit_consistency: PASS
attention_consistency: REVISE
centralization_risk: REVISE
management_cost_reduction: BLOCK
external_ecosystem_consistency: REVISE
implementation_gate: BLOCK
authority_effect: false
implementation_effect: false
schema_effect: false
api_effect: false
runtime_effect: false
repository_effect: false
external_action_effect: false
---

# TITMAS Governance Consistency Review v0.1

中文：TITMAS 治理一致性审查 v0.1。

## 0. Review boundary（审查边界）

本文件检查以下治理工件是否互相一致：

- [`TITMAS Architecture Decision Record v0.1`](TITMAS_ARCHITECTURE_DECISION_RECORD_v0.1.md)；
- [`TITMAS Constitution Revision Proposal v1.1`](TITMAS_CONSTITUTION_REVISION_PROPOSAL_v1.1.md)；
- [`TITMAS Interface Boundary Map v0.1`](TITMAS_INTERFACE_BOUNDARY_MAP_v0.1.md)；
- [`Adaptive Attention Allocation Principle Review v0.1`](ATTENTION_PRINCIPLE_REVIEW_v0.1.md)；
- 当前 worktree 中的
  [`ADR-033`](ADR-033-attention-principle-for-dynamic-coordination.md)、
  [`PROGRAM-CHARTER.md`](../PROGRAM-CHARTER.md) 和
  [`Open Infrastructure Strategy Constitution`](open-infrastructure-strategy-constitution.md)。

本审查不追求理论完整性，不新增 Architecture Layer、Component、Protocol、Schema、API、
Runtime 或 Implementation。它只判断：

> 当前治理结构是否能降低一个人管理多个仓库、程序、Agent、工具和外部服务时的认知与
> 运维成本，而不创建新的中心、重复服务或维护负担。

### 0.1 Allowed review statuses（允许的审查状态）

本文件只使用：

| 状态 | 含义 |
|---|---|
| `PASS` | 当前工件在审查范围内一致，不需要本轮修正 |
| `REVISE` | 方向可保留，但必须修正文义、顺序、边界或证据 |
| `BLOCK` | 在问题关闭前不得据此进入下一治理／实现 gate |

### 0.2 Overall verdict（总体结论）

```text
OVERALL=REVISE
IMPLEMENTATION_GATE=BLOCK
SELF_GOVERNANCE_EXPERIMENT_GATE=BLOCK
```

总体不是 `BLOCK`，因为 compositional scale（组合式规模）、Evidence First、Authority
Separation、DBOS/SAEE 分工和 Cockpit reference-only 定位仍然一致且可修正。

Implementation 与 Self-Governance Experiment 保持 `BLOCK`，因为：

- Attention adoption 顺序倒置；
- Program Charter 与战略宪法在 dirty worktree 中提前声明采纳；
- Attention 仍在 Human Attention Amplification 与 Agent participant selection 之间摇摆；
- 尚无直接 Evidence 证明它降低一个人的管理成本；
- 外部工具协调边界尚未转化为明确的“不替换、不重建”准入规则。

## 1. Mission Constraint（任务约束）

### 1.1 Primary objective（首要目标）

```text
The primary objective is not theoretical completeness.
The primary objective is reducing human cognitive and operational load when
managing many repositories, programs, agents, tools and services.
```

中文：

> 主要目标不是理论完整性，而是降低一个人在管理多个仓库、程序、Agent、工具和服务时的
> 认知成本与运维成本。

任何抽象必须回答：

1. 是否降低管理复杂度？
2. 是否减少人工监控？
3. 是否提高决策质量？
4. 是否避免产生新的维护负担？
5. 是否减少异构工具之间的集成复杂度？
6. 是否避免复制现有外部服务？

无法回答时：

```text
THEORETICAL_NOTE_ONLY=PASS
ENTER_IMPLEMENTATION=BLOCK
```

“保留为理论记录”不是失败；它是防止理论完整性驱动系统膨胀的主动边界。

### 1.2 Practical interpretation（实践解释）

TITMAS 的价值不在于拥有更多内部层，而在于把：

```text
many repositories
many agents
many programs
many external services
many status and risk signals
```

收敛为：

```text
source-bound observations
  -> bounded Evidence / Health / Evaluation references
    -> prioritized human attention
      -> explicit decision
        -> separately authorized execution
          -> new Evidence
```

Attention 的首要产品含义应是：

```text
Human Attention Amplification
```

不是：

```text
global Agent selection
central task scheduling
automatic best-agent routing
permission allocation
```

## 2. Current source state（当前来源状态）

### 2.1 Reviewed snapshots（审查快照）

| 工件 | SHA-256 |
|---|---|
| Architecture Decision Record | `29758017d5928b1673ba9633bbf219eb3930fd1ed9abd30c7351a61a96d70d78` |
| Constitution Revision Proposal | `dcc98d803e9e46f85ad5df69a6780072dedfe07acd7f7f13c546d9ba7629976e` |
| Interface Boundary Map | `241899a8a75b38471c827db8321e64f91dc2def04880f41dc9ddbdfdafe751be` |
| Attention Principle Review | `0c1e7db34dbdacd28aef0b2c2a56b4361acf4d43bb565b435a8ef92e7260d4bd` |
| ADR-033 worktree file | `7f38ccbb2a2e02f3701d350f1991299a5ebc36517cfe7219bbc34fdb474aedbb` |
| Program Charter worktree | `abf720c374155bcfded496c8b1a89f7abace7fd0d211d2cc590eb400e35b1b1c` |
| Strategy Constitution worktree | `c29b53849e6ff2b8d4dad24dca6c6ce2ff11825a75b6d9395d66bea77d7bf1a7` |

### 2.2 Git and decision-sequence observation（Git 与决定顺序观察）

观察时：

- `PROGRAM-CHARTER.md` 是 tracked modified；
- `open-infrastructure-strategy-constitution.md` 是 tracked modified；
- ADR-033、四份治理工件和 Attention Review 是 untracked；
- ADR-033 在 Attention Review 创建前已经声明 `ACCEPTED`；
- ADR-033 的 review reference 指向后来才创建的 Attention Review；
- 当前 HEAD 不包含这些 worktree Attention changes；
- 本审查不核验 remote/public adoption。

审查结果：

```text
WORKTREE_FACT_RECORDING=PASS
DECISION_SEQUENCE=BLOCK
REMOTE_OR_PUBLIC_ADOPTION_CLAIM=BLOCK
```

正确 Evidence chain 应是：

```text
Draft
  -> Review
    -> Human Decision
      -> Acceptance
        -> versioned governance update
```

当前 worktree 的 Attention amendment 呈现：

```text
Acceptance declaration
  -> later Review
```

该顺序不能用“现在补齐 Review”自动修复；需要 Human 明确处置 ADR-033。

## 3. Governance consistency scorecard（治理一致性评分）

| 检查项 | 状态 | 核心结论 |
|---|---|---|
| 1. Constitution 是否支持 Interface Boundary | `REVISE` | 基础边界支持；Attention extension 增加逻辑 Layer，但 Interface Map 不将其视为核心组件 |
| 2. Interface Boundary 是否支持 Attention | `REVISE` | 可支持 Human Attention projection；不支持新的 central Attention service |
| 3. Attention 是否产生 Authority 风险 | `REVISE` | 无正式 Authority，但候选排序与可见性形成 de facto power |
| 4. ADR-033 是否需要修订 | `REVISE` | 方向保留；participation、layer、mission、anti-lock-in 和 review sequence 必须修正 |
| 5. Program Charter 是否提前冻结 | `BLOCK` | dirty worktree 先声明 adopted，Review 与 Human disposition 未先完成 |
| 6. 是否存在 hidden authority | `REVISE` | Attention ranking、Evidence filtering、SAEE feedback 与 UI defaults 均可能形成隐性权力 |
| 7. 是否降低管理成本 | `BLOCK` | 尚无对比 Evidence；当前新增文档与抽象本身增加了管理面 |
| 8. 是否尊重外部生态 | `REVISE` | 方向可兼容，但必须明确不替换 GitHub、Codex、Render、Supabase、Context7、Linear 等服务 |

## 4. Architecture consistency（架构一致性）

### 4.1 Stable base（稳定基础）

以下关系为 `PASS`：

- DBA 继续是 non-executable Program Governance and Architecture Cockpit；
- DBOS 继续拥有 Identity、Capability、Execution、Evidence admission、Verification 和
  Lifecycle 的 canonical boundary；
- Agent Evidence 继续只处理 Evidence candidate capture/package/local validation/export；
- Agent Health 继续是本地静态 repository-health diagnosis；
- SAEE 继续只读、有界、advisory-only；
- Human Decision 与 Execution 分离；
- Cockpit 继续是 reference-only Situational Awareness Layer。

### 4.2 Attention extension conflict（Attention 扩展冲突）

状态：`REVISE`

Constitution Revision Proposal 当前增加：

```text
Principle 1A. Attention and Dynamic Coordination
```

ADR-033 与 Strategy Constitution v0.4 使用：

```text
Attention Layer
Coordination Layer
Evidence Layer
Memory / Evolution Layer
```

Attention Review 则明确：

```text
Attention = logical cross-cutting Architecture Pattern
Attention != new Layer or Component
```

Interface Boundary Map 的核心组件中没有 Attention Layer。这不是遗漏；它反映了“不新增
架构层”的正确约束。

一致性修正方向：

- 不在核心架构图中新增 Attention Layer；
- 不把 Coordination、Evidence、Memory/Evolution 重新包装成四个新组件；
- 把 Attention 收敛为 DBA Cockpit 内的 prioritization behavior（优先呈现行为）和
  cross-cutting Architecture Pattern；
- Agent participant selection 保持 theoretical/research note，直到证明它降低管理成本且
  不创建中心。

```text
BASE_ARCHITECTURE=PASS
ATTENTION_AS_NEW_LAYER=BLOCK
ATTENTION_AS_CROSS_CUTTING_PATTERN=REVISE
```

## 5. Authority boundary consistency（Authority 边界一致性）

状态：`BLOCK`

### 5.1 Formal authority（正式权力）

文档均声明：

```text
ATTENTION_NE_AUTHORITY_OR_PERMISSION=true
IMPLEMENTATION_AUTHORIZED=false
```

该文本方向为 `PASS`。

### 5.2 Procedural authority（程序权力）

冲突在于：

- Architecture Decision 仍建议 `REVISE`；
- Constitution Revision Proposal 仍要求 Human Decisions；
- Interface Freeze 尚未通过；
- Attention Review 建议保留方向并修订；
- ADR-033 与 Program Charter dirty changes 已声明 Attention adopted。

Program Charter 是高位治理工件。把未完成 Review disposition 的原则写成 adopted，会使
worktree narrative 超前于 Evidence chain。

```text
ATTENTION_NON_AUTHORITY_TEXT=PASS
ATTENTION_ADOPTION_SEQUENCE=BLOCK
PROGRAM_CHARTER_ATTENTION_AMENDMENT=BLOCK
```

这里的 `BLOCK` 只针对 Attention amendment，不否定 Program Charter 其他已采纳内容。

### 5.3 De facto authority（事实权力）

即使没有 Permission 字段，以下主体仍可能形成 hidden authority：

- 定义“什么值得看”的 ranking policy；
- 决定哪些 repository/service signals 进入 Cockpit；
- 选择哪些 Evidence 被显示；
- 配置默认隐藏、折叠或 suppress 的规则；
- 将 SAEE recommendation 自动转成 attention weight；
- 把 UI 默认排序当作 Human Decision；
- 通过连接数量成为所有工具的 mandatory gateway。

因此：

```text
FORMAL_NEW_AUTHORITY=PASS
HIDDEN_VISIBILITY_AUTHORITY=REVISE
HUMAN_AUTHORITY_GATE=PASS
```

## 6. Evidence First consistency（Evidence First 一致性）

状态：`REVISE`

### 6.1 Consistent chain（已一致链路）

Interface Boundary Map 已保持：

```text
Observation
  -> Evidence candidate
    -> Agent Evidence local validation
      -> DBOS admission, when applicable
        -> SAEE evaluation
          -> Human Decision
            -> separately authorized execution
              -> new Evidence
```

该关系为 `PASS`。

### 6.2 Attention-related elevation risk（Attention 相关抬升风险）

ADR-033 与 Strategy Constitution 使用 Evidence quality、history 和 reputation 作为候选
参与信号。若没有额外限制，可能形成：

```text
more Evidence
  -> more Attention
    -> more participation
      -> more Evidence
        -> persistent dominance
```

需要修订：

- Evidence 数量不等于 relevance；
- validator `PASS` 不等于 participation eligibility；
- Reputation 不等于 Permission；
- past success 不证明 current suitability；
- not selected 不形成 negative Evidence；
- Cockpit priority 不等于 Evidence quality；
- SAEE recommendation 不直接写回 Attention；
- feedback 形成新 Evidence、新 Review 和新 policy version。

```text
EVIDENCE_CHAIN=PASS
EVIDENCE_AS_ATTENTION_SIGNAL=REVISE
EVIDENCE_AS_TRUTH_OR_PERMISSION=BLOCK
```

## 7. Cockpit role consistency（Cockpit 定位一致性）

状态：`PASS`

Architecture Decision、Constitution Proposal、Interface Boundary 和 Attention Review
已经一致把 Cockpit 定位为：

```text
TITMAS Situational View within the DBA Cockpit
```

新的 mission 可以进一步用产品语言表达为：

```text
Cockpit = Human Attention Interface
```

含义：

> Cockpit 回答“现在什么最值得人看”，而不是“系统替人决定怎么做”。

该表达不创建新 Interface、Component 或 Layer。Cockpit 可以：

- 聚合带 source、version、freshness 和 limitation 的引用；
- 展示异常、风险、unknown、conflict 和 pending decision；
- 把大量状态收敛为少量需要人关注的候选；
- 链接回 GitHub、Linear、Render、Supabase 或其他 canonical external source；
- 显示 recommendation，但不显示为 command。

Cockpit 不可以：

- 写回 child truth；
- 执行命令；
- 授予 Permission；
- 自动关闭 gate；
- 成为 issue tracker、deployment console、database admin 或 coding agent；
- 因排序而声称选出了“最佳 Agent”。

辅助模型认为“只读 Cockpit 不能降本，必须写回”——本审查不采纳。减少监控、定位与
上下文切换本身就可以降低成本；执行保持分离正是 Authority Separation 的要求。

```text
COCKPIT_AS_SITUATIONAL_AWARENESS=PASS
COCKPIT_AS_HUMAN_ATTENTION_INTERFACE=PASS
COCKPIT_AS_COMMAND_CENTER=BLOCK
```

## 8. Attention boundary consistency（Attention 边界一致性）

状态：`REVISE`

### 8.1 Required reframing（必要重构）

当前 ADR-033 的首要问题是：

```text
Attention = candidate Agent participation selection
```

新的 mission 要求首要含义为：

```text
Attention = Human Attention Amplification
```

建议治理顺序：

1. 从现有 Observation、Evidence、Health、Evaluation 和 Risk 中找出需要人复核的候选；
2. 保留 source、reason、scope、freshness、unknown 和 limitation；
3. 向人展示少量高价值 attention candidates；
4. 人作决定；
5. 被授权 executor 在外部或项目本地系统中执行；
6. 结果形成新 Evidence。

Agent selection 不是当前首要产品目标，也没有降低管理成本的直接 Evidence。它应保持：

```text
THEORETICAL_OR_FUTURE_ARCHITECTURE_PATTERN=PASS
CURRENT_CONSTITUTIONAL_MECHANISM=BLOCK
CURRENT_IMPLEMENTATION_TARGET=BLOCK
```

### 8.2 No new component（不新增组件）

Human Attention Amplification 应复用：

- DBA Program Status；
- Decision Queue；
- Risk and Blocker Register；
- Integration Gates；
- Agent Evidence source references；
- Agent Health findings；
- SAEE recommendations；
- external service status references。

不创建：

- Attention service；
- central ranking database；
- global Agent registry；
- second Cockpit；
- universal task router；
- duplicate notification service；
- duplicate issue tracker。

## 9. Centralization and hidden-authority review（中心化与隐性权力）

状态：`REVISE`

| 风险 | 状态 | 原因 |
|---|---|---|
| 单一 mandatory Attention controller | `BLOCK` | 形成新的所有工具入口与单点权力 |
| 永久 global Agent ranking | `BLOCK` | Reputation/历史成功被固化为生态地位 |
| Cockpit 默认排序 | `REVISE` | 可以辅助人，但必须显示理由、来源和覆盖方式 |
| Evidence quality 作为唯一权重 | `BLOCK` | 会奖励 Evidence gaming 并抬升语义 |
| SAEE 自动更新 Attention | `BLOCK` | Evaluation 变成 writeback controller |
| external-tool adapter 变成 shadow database | `BLOCK` | 复制来源并增加同步成本 |
| local、task-scoped、expiring prioritization | `PASS` | 不成为全局 Authority，且失败可局部化 |
| Human override and source drill-down | `PASS` | 保留决定权和可核验来源 |

中心化风险不能因为 Cockpit 当前只读就判 `PASS`。排序和可见性本身可能产生
agenda-setting power（议程设置权）。

## 10. Management-cost review（管理成本审查）

状态：`BLOCK`

### 10.1 Current evidence（当前证据）

当前已经形成多份高质量治理文档，但尚无对比实验回答：

- 一个人能管理多少 repository/Agent/service；
- 找到最重要三个异常需要多久；
- 需要打开多少工具和页面；
- 需要手工核对多少状态；
- attention ranking 有多少 false positive/false negative；
- ranking policy 本身需要多少维护；
- source drift 和 stale projection 是否减少；
- 决策质量是否提高。

因此不能从文档完整性推导管理降本。

```text
THEORETICAL_COHERENCE=PASS
MANAGEMENT_COST_REDUCTION_EVIDENCE=BLOCK
DECISION_QUALITY_IMPROVEMENT_EVIDENCE=BLOCK
MAINTENANCE_BURDEN_REDUCTION_EVIDENCE=BLOCK
```

### 10.2 Minimum proof for future experiment（未来实验的最小证明）

后续 Self-Governance Experiment 至少应比较同一组仓库与服务在：

```text
baseline manual management
vs.
DBA Cockpit source-bound attention support
```

下的：

| 指标 | 为什么重要 |
|---|---|
| 找到前三个 actionable risks 的时间 | 直接测量人类注意力覆盖 |
| 跨工具 source hops / context switches | 测量认知切换成本 |
| 每个真实问题对应的 reviewed signals 数 | 测量监控噪声 |
| stale/conflicted state 被识别的比例 | 测量事实质量 |
| decision packet 完整度与准备时间 | 测量决策质量和效率 |
| false positive / false negative | 防止 attention ranking 误导 |
| ranking/configuration maintenance time | 防止减负工具成为新负担 |
| 需要人工 override 的比例和原因 | 发现 hidden authority 或模型偏差 |

本审查只定义未来验证问题，不设计实验、API 或实现。

### 10.3 Management-cost gate（管理成本闸门）

任何新增抽象、adapter 或组件必须证明：

```text
INTEGRATION_COMPLEXITY_REDUCED=PASS
HUMAN_MANAGEMENT_EFFORT_REDUCED=PASS
DECISION_QUALITY_IMPROVED=PASS
EXISTING_SERVICE_DUPLICATION_AVOIDED=PASS
NEW_MAINTENANCE_BURDEN_AVOIDED=PASS
```

任一项无法提供直接 Evidence：

```text
KEEP_AS_THEORETICAL_NOTE=PASS
CREATE_COMPONENT=BLOCK
```

## 11. External ecosystem consistency（外部生态一致性）

状态：`REVISE`

### 11.1 External Ecosystem Constraint（外部生态约束）

TITMAS 必须考虑 GitHub、Codex、Render、Supabase、Context7、Linear 和类似服务。外部工具
继续维护自身 capability、account、Permission、data、release 和 service truth。

本审查不核验这些服务当前的全部功能或商业状态；只定义“不替换、不重建”的边界。

| 外部服务／类别 | 继续由外部服务负责 | TITMAS 允许做 | TITMAS 禁止做 |
|---|---|---|---|
| GitHub | repository、commit、PR、Issue、CI 等项目本地事实 | 引用 source/status/risk，链接回 canonical surface | 新建代码托管、PR/Issue/CI 替代品或 shadow ledger |
| Codex | 经人类和环境授权的 coding/execution assistance | 提供有范围 context、decision ref 和待办；读取执行结果引用 | 重建 coding agent、模型、terminal 或自动执行权 |
| Render | 其托管／部署服务自身状态 | 引用 deployment/status/error source | 重建 deployment platform 或把 Cockpit 变成部署控制台 |
| Supabase | 其数据、身份或后端服务自身边界 | 引用允许公开的 service/status evidence | 重建 database/auth/backend，复制 secrets 或 customer data |
| Context7 | 其文档／上下文服务自身来源 | 引用有来源的 context/citation | 重建文档平台、复制整个索引或声称引用为 Truth |
| Linear | 其 work item、project planning 和 issue state | 映射 Decision/Work item reference，链接回 source | 新建第二 issue tracker、双写任务状态 |
| Similar services | 各自 canonical service responsibility | 通过最小、可替换、source-bound reference 协调 | 创建通用替代平台或不可替换 connector center |

### 11.2 Coordination, not replacement（协调而非替代）

TITMAS 应减少：

- 为理解同一问题反复打开多个工具；
- 手工复制状态；
- 在 GitHub Issue、Linear work item、Render deployment、Supabase service state 和
  Codex execution context 之间丢失 lineage；
- 重复判断哪个来源是 canonical；
- 对同一异常进行多次无来源解释。

TITMAS 不应：

- 同步所有外部数据到一个新数据库；
- 创建新的全能 integration hub；
- 统一接管外部账号与 Permission；
- 复制 notification、task、deployment、database、documentation 或 coding 功能；
- 要求所有服务必须通过 TITMAS 才能工作。

```text
TITMAS_COORDINATES_HETEROGENEOUS_TOOLS=PASS
TITMAS_REPLACES_EXTERNAL_TOOLS=BLOCK
TITMAS_REBUILDS_EXTERNAL_FUNCTIONS=BLOCK
TITMAS_BECOMES_MANDATORY_GATEWAY=BLOCK
```

### 11.3 New-component external-service test（新组件外部服务检查）

任何新组件提案必须回答：

1. 哪个现有外部服务已经提供相同功能？
2. 为什么 source reference、deep link、existing API 或人工 workflow 不能满足？
3. 它减少多少 integration complexity？
4. 它减少多少 human management effort？
5. 它是否创建新的同步、credential、privacy、availability 或 maintenance burden？
6. 外部服务不可用时，TITMAS 是否仍能 fail locally 而不覆盖事实？
7. 是否可以删除该组件而不影响 child canonical systems？

没有直接答案：

```text
EXTERNAL_ECOSYSTEM_FIT=BLOCK
NEW_COMPONENT=BLOCK
```

## 12. ADR-033 consistency review（ADR-033 一致性审查）

状态：`REVISE`

不建议删除 ADR-033。建议保留“有限主体通过动态关注形成临时组合”的战略启发，但在任何
后续 Human disposition 中处理：

1. 将首要目标从 Agent participant selection 改为 Human Attention Amplification；
2. 将 Agent selection 降为 theoretical/future Architecture Pattern；
3. 删除或降级 `Attention Layer` 的核心层外观；
4. 把 “Attention 决定谁参与” 改为“Attention 提出什么值得人关注，或在已授权候选中
   提出谁值得考虑”；
5. 增加 mission constraint 和 management-cost proof requirement；
6. 增加 external ecosystem non-replacement rule；
7. 增加 attention monopoly、visibility power、feedback lock-in 和 Evidence gaming；
8. 明确 SAEE Recommendation 不 direct writeback；
9. 保留 `IMPLEMENTATION_AUTHORIZED=false`；
10. 由 Human 明确处理 ADR 先 `ACCEPTED`、Review 后生成的顺序。

推荐处置：

```text
ADR_033=REVISE
DELETE_ADR_033=BLOCK
IMPLEMENT_ADR_033=BLOCK
```

## 13. Program Charter and Constitution timing review（提前冻结审查）

状态：`BLOCK`

当前 dirty worktree 在 Program Charter 中写入：

```text
ATTENTION_PRINCIPLE_ADOPTED=true
```

并把 Strategy Constitution 从 v0.3 修改为 v0.4。与此同时：

- ADR-033 未跟踪；
- Attention Review 后于 ADR 的 `ACCEPTED` 声明；
- Attention Review 建议 required revisions；
- Constitution Revision Proposal 仍要求 Human Decisions；
- 当前 HEAD 不包含 Attention amendment。

因此：

```text
PROGRAM_CHARTER_BASE=PASS
PROGRAM_CHARTER_ATTENTION_FREEZE=BLOCK
STRATEGY_CONSTITUTION_BASE=PASS
STRATEGY_CONSTITUTION_ATTENTION_FREEZE=BLOCK
```

正确下一步是 Human 对本审查和 Attention Review 作 disposition，而不是用本审查自动确认
已有 `ADOPTED` 文本。本文件不修改 Charter、Constitution 或 ADR。

## 14. Hidden authority register（隐性权力台账）

| Hidden authority source | 状态 | 必须保持的边界 |
|---|---|---|
| Cockpit ranking policy | `REVISE` | reasons、sources、freshness、override、no command |
| Attention candidate filtering | `REVISE` | unknown/new candidate path、no permanent exclusion |
| Evidence completeness score | `BLOCK` | 不能成为 Permission、Truth 或唯一 priority |
| Reputation/history | `REVISE` | contestable、time-bound、not Identity/Permission |
| SAEE feedback | `BLOCK` | recommendation -> Human/policy review，不 direct writeback |
| UI default action | `BLOCK` | default 不等于 Authorization |
| Cross-tool connector | `REVISE` | minimal、replaceable、no shadow source |
| Global integration hub | `BLOCK` | 不成为所有工具 mandatory gateway |
| Human override with source review | `PASS` | 保留最终决定与可核验来源 |

## 15. Required revisions and stop conditions（必要修订与停止条件）

### 15.1 Required revisions

| ID | 修订事项 | 状态 |
|---|---|---|
| `GC-01` | Human disposition ADR-033 的 review sequence 和当前状态 | `BLOCK` |
| `GC-02` | 收敛 Attention 为 Human Attention Amplification | `REVISE` |
| `GC-03` | 删除新 Attention Layer/central component 的暗示 | `REVISE` |
| `GC-04` | 保留 Agent selection 为理论／未来 pattern | `REVISE` |
| `GC-05` | Program Charter / Constitution attention amendment 与 Review 对齐 | `BLOCK` |
| `GC-06` | 增加外部工具不替换、不重建约束 | `REVISE` |
| `GC-07` | 定义未来管理成本验证问题 | `PASS` |
| `GC-08` | 在任何 implementation 前获得降本 Evidence | `BLOCK` |

### 15.2 Stop conditions

在以下事项关闭前：

```text
MODIFY_ADR=BLOCK
MODIFY_CONSTITUTION=BLOCK
MODIFY_PROGRAM_CHARTER=BLOCK
CREATE_SCHEMA=BLOCK
CREATE_API=BLOCK
CREATE_COMPONENT=BLOCK
IMPLEMENT_ATTENTION=BLOCK
IMPLEMENT_COCKPIT=BLOCK
START_SELF_GOVERNANCE_EXPERIMENT=BLOCK
COMMIT_OR_PUSH_THIS_REVIEW=BLOCK
```

这些 `BLOCK` 表示本审查不授权相应动作；Human 后续可以通过单独、明确、有限的决定改变
具体 gate。

## 16. Auxiliary agent review（辅助智能体审查）

本轮通过用户指定的安全环境变量路径调用 `qwen3.7-max`。没有读取、复制、记录或回显
API Key。

Qwen 支持：

- Architecture `REVISE`；
- Authority `BLOCK`；
- Evidence First `REVISE`；
- Attention `REVISE`；
- Management Cost `BLOCK`；
- ADR-033 增加降本理由并与 Attention Review 对齐。

未采纳：

- Cockpit 因只读而必须 `REVISE`，并需要写回／编排能力；
- centralization risk 因 Cockpit 只读即可 `PASS`；
- 把当前冲突称为已经发生的“非法授权”。

理由：

- reference-only triage 可以降低监控和上下文切换，不需要写回；
- 排序和可见性仍可能产生隐性中心权力；
- 当前是 dirty worktree 治理顺序冲突，尚无 Implementation 或 runtime authority 产生。

```text
AUXILIARY_REVIEW_USE=PASS
AUXILIARY_OUTPUT_AS_DECISION=BLOCK
AUXILIARY_OUTPUT_AS_AUTHORIZATION=BLOCK
```

## 17. Final decision（最终决定）

```text
ARCHITECTURE_CONSISTENCY=REVISE
AUTHORITY_CONSISTENCY=BLOCK
EVIDENCE_FIRST_CONSISTENCY=REVISE
COCKPIT_CONSISTENCY=PASS
ATTENTION_CONSISTENCY=REVISE
CENTRALIZATION_RISK=REVISE
MANAGEMENT_COST_REDUCTION=BLOCK
EXTERNAL_ECOSYSTEM_CONSISTENCY=REVISE

OVERALL=REVISE
IMPLEMENTATION_GATE=BLOCK
```

最小治理结论：

> 不新增层，不新增组件，不替换外部工具。保留 Attention 的理论方向，但把它收敛为
> Cockpit 对人类注意力的放大行为。只有当同一组仓库、Agent 和外部服务的对比 Evidence
> 证明它减少 source hops、监控时间和维护成本，并保持 Authority Separation 时，才可
> 进入 Self-Governance Experiment 的单独决定。

## 18. Non-effects（非效果）

```text
EXISTING_FILE_MODIFICATION=BLOCK
CODE_CREATION=BLOCK
SCHEMA_CREATION=BLOCK
API_CREATION=BLOCK
IMPLEMENTATION=BLOCK
COMMIT=BLOCK
PUSH=BLOCK

NEW_ARCHITECTURE_LAYER_CREATED=false
NEW_COMPONENT_CREATED=false
EXTERNAL_SERVICE_REPLACED=false
ADR_MODIFIED=false
CONSTITUTION_MODIFIED=false
PROGRAM_CHARTER_MODIFIED=false
CODE_MODIFIED=false
SCHEMA_MODIFIED=false
API_DEFINED=false
IMPLEMENTATION_AUTHORIZED=false
```
