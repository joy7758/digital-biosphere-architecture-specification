---
document_id: DBA-TITMAS-DIGITAL-CELL-SPECIFICATION-0.1
title: Digital Cell Specification v0.1
title_zh: 数字细胞规范 v0.1
status: development-conceptual-specification-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
constitution_freeze_reference: NOT_PROVIDED
primary_repository: digital-biosphere-architecture
normative_effect: NONE
canonical_object_effect: NONE
implementation_authorized: false
execution_authorized: false
---

# Digital Cell Specification v0.1（数字细胞规范 v0.1）

## 0. Status and Scope（状态与范围）

本文定义 TITMAS 语境下 Digital Cell（数字细胞）的最小概念画像。它是
Specification Phase 1（规范阶段第一阶段）的 `Development` 文档，不是已采纳标准、
canonical schema（规范对象模式）、API、Runtime 或实现授权。

```text
DOCUMENT_MATURITY=Development
DECISION_STATUS=REVIEW_REQUIRED
CONSTITUTION_FREEZE_REFERENCE=NOT_PROVIDED
TITMAS_INTERFACE_V0_1_FROZEN=false
IMPLEMENTATION_AUTHORIZED=false
```

本文使用用户提供的 Digital Immune Constitution（数字免疫宪法）概念作为设计输入，
但当前仓库中没有可核验的冻结引用。因此，本文不得被解释为该宪法已经被 DBA 采纳或
冻结。

本规范的唯一主责任仓库是 DBA。Identity、Execution、Evidence、Verification 和
Lifecycle 的 canonical ownership（规范所有权）继续受 DBOS 边界约束；Evaluation、
Stability、Risk 和 Adaptation 的评价职责继续受 SAEE 边界约束。

## 1. Definition（定义）

```text
Digital Cell = Agent + Immune Structure
```

Digital Cell 是一个可识别、边界受限、历史可追溯、健康可观察且能够接受分级生态响应的
数字主体概念。这里的 `Agent` 表示外部拥有和实现的行动主体；`Immune Structure`
表示围绕该主体组织的六类概念对象及约束。

Digital Cell 不创建智能，不证明主体具有意识，也不自动授予 Capability、Permission、
Authority 或生存资格。

最小结构：

```text
Digital Cell
  = Identity Object
  + Boundary Object
  + Evidence Object
  + Health State Object
  + Memory Object
  + Reputation Object
```

这些名称是概念角色。除非未来 Owner 决策另有规定，TITMAS 只定义 reference、mapping、
handoff 和 relationship semantics，不创建第二套 DBOS 或 SAEE canonical object。

## 2. Common Object Rules（通用对象规则）

每个对象概念必须能够表达：

| Property | Requirement |
|---|---|
| `object_id` | 在所属版本和 Owner 范围内唯一 |
| `object_type` | 明确对应六类对象之一 |
| `version` | 绑定对象语义版本，不使用未约束的 `latest` |
| `owner_ref` | 指向规范 Owner 或事实 Owner，不推断所有权 |
| `source_ref` | 指向 canonical source 或明确标记 `UNKNOWN` |
| `observed_at` | 带时区的观察时间 |
| `status` | 保留 `UNKNOWN`、`STALE`、`CONFLICTED` 和 `UNSUPPORTED` |
| `limitations` | 记录缺失、范围和不可推导结论 |

对象之间只通过显式引用形成关系。关联、共现或相同标识符不自动证明它们属于同一事实、
同一 Owner 或同一生命周期。

## 3. Identity Object（身份对象）

### 3.1 Purpose（目的）

Identity Object 描述“这个数字主体被声明为何物、由谁负责、以哪个版本和来源被识别”。
它不是账户凭据、Permission 或 Capability grant。

| Field | Conceptual meaning | Stability |
|---|---|---|
| `cell_id` | 数字细胞在指定身份域中的稳定标识 | Immutable within one identity version |
| `owner` | 对主体承担责任的 Owner reference | Change requires a new attributed event |
| `version` | 身份声明或主体版本 | Immutable for the referenced version |
| `purpose` | 有边界的用途声明 | Versioned mutable declaration |
| `capability` | 对可声称能力的有来源引用 | Mutable reference; never Permission |
| `identity_provenance` | 发行者、来源、时间和完整性链 | Append-only |

### 3.2 Rules（规则）

- `cell_id` 必须在声明的 identity namespace（身份命名空间）中唯一。
- `owner` 必须是可追溯引用，不得由代码仓库、模型输出或 Reputation 自动推断。
- `capability` 必须保留来源、版本、范围和状态。
- Capability 声明不得自动转化为 Authority、Permission 或执行批准。
- 身份冲突必须记录为 `CONFLICTED`，不得静默选择更高权限身份。
- TITMAS 不成为 DBOS Identity 的第二 canonical Owner。

## 4. Boundary Object（边界对象）

### 4.1 Purpose（目的）

Boundary Object 描述数字细胞在一个明确范围内可以做什么、不得做什么以及谁有权改变
边界。边界限制自治，但不由 TITMAS 自动执行。

| Field | Conceptual meaning |
|---|---|
| `allowed_actions` | 在有效 Authority 和 Permission 下可考虑的动作集合 |
| `forbidden_actions` | 明确禁止的动作集合 |
| `capability_limits` | 速率、资源、范围、时间或工具限制 |
| `policy_boundary` | 适用政策、版本、优先级和失败语义 |
| `authority_boundary` | 哪个 Authority 可以决定、修改、撤销或复核边界 |

### 4.2 Rules（规则）

- Allowed action 不等于已经获得 Permission。
- 未声明、冲突、过期或不支持的边界必须失败关闭。
- 边界变更必须有 Owner、时间、理由、前后版本和 Evidence reference。
- 边界不得因组合规模、Reputation、Health score 或紧急叙事而自动扩大。
- Boundary Object 不创建集中式全局控制器。

## 5. Evidence Object（证据对象）

### 5.1 Purpose（目的）

Evidence Object 在本规范中是对 DBOS canonical Evidence 或受治理 evidence material 的
引用角色。它描述执行历史如何被关联、验证和保留，不创建新的 Evidence truth store。

| Field | Conceptual meaning |
|---|---|
| `intent` | 动作前可追溯的目标、请求或授权上下文 |
| `action` | 被选择或请求的动作及其范围 |
| `execution` | 执行来源、版本、时间、结果和失败状态 |
| `evidence` | 证据材料或 canonical Evidence reference |
| `verification` | 有范围、版本和限制的 Verification reference |

### 5.2 Rules（规则）

```text
Evidence proves execution history.
Evidence does NOT prove intelligence correctness.
```

- Evidence 不等于 Truth、Permission、Certification 或科学结论。
- Observation、trace、log、receipt 或 validator result 不得自动升级为 Evidence。
- 验证结果必须保留验证器版本、输入范围、结果和 limitations。
- 摘要不匹配、来源未知或语义冲突时必须记录失败或 `CONFLICTED`。
- TITMAS 只定义 Evidence reference 和 handoff 关系，不取得 DBOS Evidence ownership。

## 6. Health State Object（健康状态对象）

### 6.1 Purpose（目的）

Health State Object 提供数字细胞在指定时间、来源和评价范围内的状态观察。它不是医疗
类比下的诊断，也不是合格证书。

| Field | Conceptual meaning |
|---|---|
| `identity_health` | 身份完整性、来源一致性和有效性观察 |
| `evidence_health` | Evidence 完整性、连续性、缺失和冲突观察 |
| `execution_stability` | 执行成功、失败、波动和恢复的范围化观察 |
| `adaptation` | 环境变化后行为或状态调整的有来源评价 |
| `risk_state` | 已观察风险、严重度、不确定性和适用范围 |

### 6.2 Rules（规则）

- 每个健康结论必须绑定 evaluator、方法版本、输入范围、时间和不确定性。
- Health 不等于 Certification、Permission、Authority 或普遍安全。
- 缺少输入时使用 `UNKNOWN` 或 `INSUFFICIENT_EVIDENCE`，不得推定健康。
- SAEE 的评价和建议保持只读、可追溯和 advisory-only（仅建议）。
- Health 状态不得直接改变 Identity、Evidence 或 Boundary。

## 7. Memory Object（记忆对象）

### 7.1 Purpose（目的）

Memory Object 维护数字细胞可追溯的连续性引用，使后续观察能够区分当前状态、历史失败、
恢复路径和版本演化。

| Field | Conceptual meaning |
|---|---|
| `execution_history` | 有来源的执行与结果引用 |
| `failure_history` | 失败、未知、冲突和中止记录 |
| `recovery_history` | 恢复尝试、条件、结果和复核记录 |
| `evolution_history` | 版本、策略、边界和谱系变化记录 |

### 7.2 Rules（规则）

- 历史记录必须追加，不得因当前状态更好而删除失败。
- Memory 可以被分层保留或依法删除，但删除事件和范围必须可追溯。
- Memory 不等于 Truth；它是带来源、范围和限制的历史材料。
- 新版本不得覆盖旧版本的 lineage（谱系）和 supersession（取代）关系。
- 退休主体的历史必须继续可引用。

## 8. Reputation Object（声誉对象）

### 8.1 Purpose（目的）

Reputation Object 汇总指定评价者、时间窗口和上下文中的历史表现。它提供选择输入，不是
权力、身份或全局排名。

| Field | Conceptual meaning |
|---|---|
| `reliability` | 在声明样本和时间窗口内的可靠性观察 |
| `evidence_quality` | Evidence 完整性、来源和限制的评价 |
| `adaptation` | 在环境变化中的调整表现 |
| `contribution_history` | 对协作目标的可归因贡献记录 |

### 8.2 Rules（规则）

- Reputation 必须绑定评价者、方法、数据范围、时间窗口和不确定性。
- Reputation 不得成为 Authority、Permission、Identity 或 Certification。
- 不同上下文的 Reputation 不得无映射地聚合。
- 缺失数据、选择偏差和评价者冲突必须显式保留。
- 低 Reputation 不自动触发 Isolation 或 Retirement。

## 9. Object Relationships（对象关系）

```text
Identity
  -> identifies the subject

Boundary
  -> constrains possible behavior

Evidence
  -> records attributable execution history

Health
  -> evaluates bounded current condition

Memory
  -> preserves historical continuity

Reputation
  -> summarizes contextual historical assessment
```

核心依赖规则：

| Relationship | Constraint |
|---|---|
| Identity to Boundary | 边界必须绑定明确身份版本 |
| Boundary to Evidence | 边界变更和越界事件必须留下 Evidence reference |
| Evidence to Health | Health 只能消费有来源、范围明确的输入 |
| Memory to Evidence | Memory 保存引用，不重写 Evidence |
| Reputation to Memory | Reputation 必须声明使用的历史窗口和过滤规则 |
| Health to Response | Health 只能形成响应输入，不能自行授权响应 |
| Reputation to Response | Reputation 不能单独触发限制、隔离或退休 |

## 10. Lifecycle and State Transitions（生命周期与状态迁移）

候选生命周期：

```text
PROPOSED
  -> IDENTIFIED
  -> BOUNDED
  -> OBSERVABLE
  -> ACTIVE
  -> DEGRADED
  -> RECOVERING
  -> ACTIVE

ACTIVE or DEGRADED
  -> RESTRICTED
  -> ISOLATED
  -> RETIRED
```

| Transition rule | Requirement |
|---|---|
| Entry | Identity、Owner 和 version 必须明确 |
| Activation | Boundary 与 observation references 必须存在 |
| Degradation | 必须记录观察来源和不确定性 |
| Restriction | 必须有有权决定者、范围和 Evidence basis |
| Isolation | 必须保留历史、恢复条件和复核入口 |
| Retirement | 必须保留 Identity、lineage、Evidence 和决定记录 |
| Recovery | 不覆盖失败历史，不静默恢复旧 Permission |

这些状态是规范词汇，不代表当前存在状态机、执行器或自动转换机制。

## 11. Governing Principles（治理原则）

### Principle of Distributed Complexity Generation（分布式复杂性生成原则）

> Do not create one infinitely powerful center. Generate large-scale capability
> through many simple, bounded, composable subjects.

中文：不创建一个无限强大的中心，而通过大量简单、受限、可组合的主体生成大规模能力。

| Principle | Required interpretation |
|---|---|
| Evidence First | 先保留可追溯观察和证据，再评价或响应 |
| Bounded Autonomy | 自治始终受 Identity、Boundary、Authority 和 scope 约束 |
| Digital Homeostasis | 目标是动态稳态、可恢复和局部化失败，不是静态不变 |
| Evolutionary Selection | 选择是观察到的差异机制，不等于最高分或自动淘汰 |
| Open Evolution | 允许有版本、有谱系、可比较的变化，不允许静默改写历史 |

组合不得自动产生 Authority、Permission、Decision 或 Truth Ownership。

## 12. Limitations and Recommendation Gate（限制与推荐闸门）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CONCEPTUAL_DIGITAL_SUBJECT_PROFILE
NOT_RECOMMENDED_AS=DEPLOYABLE_DIGITAL_CELL_OR_CANONICAL_DBOS_OBJECT
IMPLEMENTATION_RECOMMENDED_NOW=false
```

不推荐立即实现的原因：

- Digital Immune Constitution 的仓库冻结引用未提供；
- TITMAS Authority Freeze 尚未采纳；
- object ownership crosswalk 尚未采纳；
- `TITMAS Interface v0.1` 尚未达到冻结条件；
- Health、Memory 和 Reputation 的 canonical Owner 尚未由相关 Domain Owner 决定；
- 尚无 conformance cases 或独立实现反馈。

## 13. Non-goals（非目标）

```text
NO_IMPLEMENTATION=true
NO_RUNTIME=true
NO_API=true
NO_CODE_CHANGE=true
NO_SIMULATOR_CHANGE=true
NO_NEW_EXPERIMENT=true
NO_TITMAS_DEPLOYMENT=true
NO_AGENT_CREATED=true
NO_PERMISSION_GRANTED=true
NO_CANONICAL_OBJECT_CREATED=true
```

本文不定义 AI consciousness（AI 意识），不声称 digital life（数字生命）存在，也不创建
认证、全局 Reputation、中心控制器或生产服务。
