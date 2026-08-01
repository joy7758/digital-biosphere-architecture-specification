---
document_id: DBA-TITMAS-OBJECT-MODEL-0.1
title: TITMAS Object Model v0.1
title_zh: TITMAS 对象模型 v0.1
status: development-conceptual-object-crosswalk-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
constitution_freeze_reference: NOT_PROVIDED
primary_repository: digital-biosphere-architecture
normative_effect: NONE
schema_effect: NONE
canonical_object_effect: NONE
implementation_authorized: false
---

# TITMAS Object Model v0.1（TITMAS 对象模型 v0.1）

## 0. Status and Interpretation（状态与解释）

本文定义 Digital Cell（数字细胞）六类对象的概念关系、所有权边界和生命周期要求。它是
object ownership crosswalk candidate（对象所有权交叉表候选），不是 JSON Schema、数据
模型实现、API 或新的 canonical truth layer（规范事实层）。

```text
DOCUMENT_MATURITY=Development
DECISION_STATUS=REVIEW_REQUIRED
OBJECT_OWNERSHIP_CROSSWALK_ADOPTED=false
TITMAS_INTERFACE_V0_1_FROZEN=false
CANONICAL_SCHEMA_DEFINED=false
IMPLEMENTATION_AUTHORIZED=false
```

用户提供的 Digital Immune Constitution 概念是本文件的设计输入，但没有随本任务提供
可核验的 DBA freeze reference。本文不能补造该冻结事实。

## 1. Purpose（目的）

TITMAS Object Model 建立一套 agent-readable（智能体可读）的概念语言，使不同实现能够
讨论一个数字主体的身份、边界、证据、健康、记忆和声誉，而不把 mapping、reference 或
评价结果升级为 Permission、Authority 或 Truth。

核心关系：

```text
Digital Cell
  = Identity
  + Boundary
  + Evidence
  + Health
  + Memory
  + Reputation
```

这里的加号表示结构组合，不表示对象所有权合并、数据库聚合或 Authority 聚合。

## 2. Ownership Principles（所有权原则）

每种对象必须只有一个明确的 canonical Owner 或明确状态 `NOT_DECIDED`。TITMAS 默认只
拥有其自身的 mapping、reference、handoff 和 interoperability profile（互操作画像）
语义。

| Principle | Requirement |
|---|---|
| One canonical owner | 同一对象类型不得由 TITMAS 建立第二规范来源 |
| Source preservation | 映射必须保留原始类型、版本、Owner 和 limitations |
| No semantic elevation | Observation、mapping 或 score 不升级为域对象事实 |
| Version separation | 对象版本、映射版本和实现版本必须分开 |
| Fail closed | Owner、版本或来源冲突时使用 `UNKNOWN`、`CONFLICTED` 或 `UNSUPPORTED` |
| No authority inheritance | 对象关系不传播 Permission、Authority 或 Decision |

## 3. Core Object Model（核心对象模型）

### 3.1 Identity（身份）

| Attribute | Definition |
|---|---|
| Purpose | 识别数字主体及其责任、来源、用途和版本 |
| Canonical ownership | DBOS 或明确的外部 identity authority；TITMAS 只引用和映射 |
| Immutable fields | `cell_id`、identity namespace、issuer、identity version、provenance root |
| Mutable fields | purpose declaration、capability references、display metadata、status |
| Evidence relationship | 身份创建、变更、冲突、撤销和 supersession 必须有 Evidence reference |
| Lifecycle | `DECLARED -> VERIFIED_OR_UNKNOWN -> CURRENT -> SUPERSEDED_OR_REVOKED` |

Identity 不等于 Credential、Capability、Permission 或 Reputation。

### 3.2 Boundary（边界）

| Attribute | Definition |
|---|---|
| Purpose | 表达 allowed、forbidden、limit、policy 和 authority scope |
| Canonical ownership | 明确的 policy/authority Owner；TITMAS 只定义边界关系语义 |
| Immutable fields | boundary ID、issuer、scope root、initial policy reference |
| Mutable fields | allowed actions、forbidden actions、limits、effective period、revocation state |
| Evidence relationship | 每次变更必须保留原因、决定者、前后版本和 Evidence reference |
| Lifecycle | `PROPOSED -> EFFECTIVE -> RESTRICTED -> REVOKED_OR_SUPERSEDED` |

Boundary 不等于 Permission。Allowed action 仍需适用范围内的有效 Permission 和执行决定。

### 3.3 Evidence（证据）

| Attribute | Definition |
|---|---|
| Purpose | 关联 intent、action、execution、evidence material 和 verification history |
| Canonical ownership | DBOS 保持 canonical Evidence/Verification ownership |
| TITMAS scope | `EvidenceMaterialHandoff`、`EvidenceObjectReference` 和 mapping |
| Immutable fields | evidence ID、source digest、source reference、event time、producer、scope |
| Mutable fields | admission status、verification references、limitations、supersession references |
| Evidence relationship | Evidence 自身必须有来源、完整性材料和验证范围 |
| Lifecycle | `MATERIAL_OBSERVED -> SUBMITTED -> ADMITTED_OR_REJECTED -> VERIFIED_OR_DISPUTED -> ARCHIVED` |

```text
Evidence != Permission
Evidence != Truth
Evidence != Intelligence Correctness
```

### 3.4 Health（健康）

| Attribute | Definition |
|---|---|
| Purpose | 表达身份、证据、执行稳定、适应和风险的有界状态评价 |
| Canonical ownership | `NOT_DECIDED`; 评价来源可能属于 SAEE 或其他明确 evaluator |
| TITMAS scope | 评价输入/输出 reference、方法版本和限制映射 |
| Immutable fields | assessment ID、evaluator、method version、input-scope digest、observed time |
| Mutable fields | current assessment、confidence、limitations、supersession reference |
| Evidence relationship | 每个结论必须指向输入 Evidence、评价方法和不确定性 |
| Lifecycle | `REQUESTED -> ASSESSED_OR_INSUFFICIENT -> CURRENT -> STALE_OR_SUPERSEDED` |

```text
Health != Certification
Health != Permission
Health != Universal Safety
```

### 3.5 Memory（记忆）

| Attribute | Definition |
|---|---|
| Purpose | 维护 execution、failure、recovery 和 evolution 的连续历史引用 |
| Canonical ownership | `NOT_DECIDED`; 每个 source domain 保留自身历史事实 |
| TITMAS scope | lineage、reference、retention 和 continuity relationship |
| Immutable fields | memory event ID、subject version、event type、source reference、recorded time |
| Mutable fields | retention state、redaction reference、index metadata、supersession reference |
| Evidence relationship | Memory 引用 Evidence，不复制或替代 Evidence truth |
| Lifecycle | `RECORDED -> RETAINED -> REDACTED_OR_SUPERSEDED -> ARCHIVED` |

Memory 不等于 Truth。删除或更正不能静默擦除曾存在的历史关系。

### 3.6 Reputation（声誉）

| Attribute | Definition |
|---|---|
| Purpose | 汇总指定评价者、上下文和时间窗口中的历史可靠性与贡献 |
| Canonical ownership | `NOT_DECIDED`; 每个 evaluator 或 registry 必须声明自己的 scope |
| TITMAS scope | reputation reference、comparison limitation 和 provenance mapping |
| Immutable fields | assessment ID、evaluator、method version、window、subject version |
| Mutable fields | score/category、confidence、limitations、current/superseded state |
| Evidence relationship | 必须引用输入历史、过滤规则、样本范围和偏差说明 |
| Lifecycle | `REQUESTED -> COMPUTED_OR_INSUFFICIENT -> CURRENT -> STALE_OR_SUPERSEDED` |

```text
Reputation != Authority
Reputation != Identity
Reputation != Permission
Reputation != Universal Ranking
```

## 4. Normative Ownership Map Candidate（规范所有权映射候选）

| Object | Domain truth owner | TITMAS role | Status |
|---|---|---|---|
| Identity | DBOS or explicit external identity authority | Reference and mapping | Existing boundary; crosswalk not adopted |
| Boundary | Explicit policy/authority Owner | Relationship and profile semantics | Owner decision required |
| Evidence | DBOS | Material handoff and object reference | Existing boundary |
| Health | SAEE or explicit evaluator, subject to Owner decision | Bounded assessment reference | Owner not decided |
| Memory | Source domain or explicit memory Owner | Lineage and continuity mapping | Owner not decided |
| Reputation | Explicit evaluator/registry | Contextual assessment reference | Owner not decided |

本文不解决表中 `Owner not decided` 项。未决对象不得因本文件出现而默认归 TITMAS。

## 5. Relationship Model（关系模型）

```text
Identity --binds--> Boundary
Identity --subjects--> Evidence
Evidence --supports bounded input for--> Health
Evidence --is referenced by--> Memory
Memory --supports bounded input for--> Reputation
Health --may inform--> Immune Response Review
Reputation --may inform--> Immune Response Review
Boundary --constrains--> Immune Response Action
```

关系约束：

| Relationship | Required rule |
|---|---|
| Identity to Boundary | 两者必须绑定兼容 subject version |
| Identity to Evidence | correlation ID 不得替代 Identity |
| Evidence to Health | 输入必须有来源、版本、scope 和 limitation |
| Evidence to Memory | Memory 只能引用，不得修改源 Evidence |
| Memory to Reputation | 必须披露时间窗口、排除规则和偏差 |
| Health to Response | Health 是输入，不是响应授权 |
| Reputation to Response | Reputation 不能单独触发惩罚性响应 |
| Boundary to Response | 响应动作不得超出决定者 Authority |

## 6. Immutability and Mutability Rules（不可变与可变规则）

- Immutable field 的更正必须创建新版本或 superseding record，不得原地静默改写。
- Mutable field 的变化必须记录 updater、time、reason、previous reference 和 new reference。
- `UNKNOWN` 不得转换为 `PASS` 或 `CURRENT`，除非出现新的直接证据。
- `STALE` 表示已知来源超过声明 freshness，不表示 false。
- `CONFLICTED` 必须保留所有冲突来源，不得按 Reputation 自动选边。
- 对象删除不得删除 lineage、decision 或 tombstone reference。

## 7. Combined Digital Cell Lifecycle（组合生命周期）

Digital Cell 的组合状态必须由对象状态和明确规则导出，不能由单一分数声明。

| Cell state | Minimum conceptual condition |
|---|---|
| `PROPOSED` | 只有主体提议，没有有效对象集合 |
| `IDENTIFIED` | Identity 有来源，其他对象可不完整 |
| `BOUNDED` | Boundary 已绑定 Identity version |
| `OBSERVABLE` | Evidence reference 路径已声明 |
| `ACTIVE` | 适用 Authority 明确允许在 Boundary 内运行 |
| `DEGRADED` | Health 或 Evidence 显示局部异常或不确定性 |
| `RESTRICTED` | 有权决定者缩小 Boundary |
| `ISOLATED` | 有权决定者暂停指定交互范围 |
| `RETIRED` | 生命周期结束且历史被保留 |

对象状态与 Cell 状态冲突时，组合状态必须是 `CONFLICTED` 或进入人工/Owner 复核，不得
自动选择更宽松状态。

## 8. Failure and Unknown Semantics（失败与未知语义）

| Condition | Required result |
|---|---|
| Owner missing | `UNKNOWN_OWNER` |
| Version unsupported | `UNSUPPORTED` |
| Source unavailable | `UNKNOWN` or `STALE` |
| Digest mismatch | `INVALID` |
| Competing canonical claims | `CONFLICTED` |
| Insufficient assessment input | `INSUFFICIENT_EVIDENCE` |
| Mapping loses source semantics | `REJECT_MAPPING` |
| Object used to elevate authority | `REJECT_SEMANTIC_ELEVATION` |

失败状态必须作为一等历史记录保留。

## 9. Governing Principles（治理原则）

### Principle of Distributed Complexity Generation（分布式复杂性生成原则）

> Do not create one infinitely powerful center. Generate large-scale capability
> through many simple, bounded, composable subjects.

中文：不创建一个无限强大的中心，而通过大量简单、受限、可组合的主体生成大规模能力。

| Principle | Object-model consequence |
|---|---|
| Evidence First | 关系和状态变化必须有来源，不从叙事推定 |
| Bounded Autonomy | Boundary 和 Authority 不随组合自动扩大 |
| Digital Homeostasis | Health 和恢复表示动态稳态，不是永久合格 |
| Evolutionary Selection | 评价可以形成选择输入，但不自动执行淘汰 |
| Open Evolution | 新版本保留 lineage、差异和旧历史 |

## 10. Recommendation and Open Decisions（推荐与待决事项）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CONCEPTUAL_OBJECT_OWNERSHIP_CROSSWALK_INPUT
NOT_RECOMMENDED_AS=CANONICAL_SCHEMA_OR_IMPLEMENTATION_MODEL
IMPLEMENTATION_RECOMMENDED_NOW=false
```

后续必须单独决定：

- Digital Immune Constitution 的 canonical freeze reference；
- TITMAS Specification Authority；
- Boundary、Health、Memory 和 Reputation 的 canonical Owner；
- DBOS 和 SAEE Domain Owner 对 crosswalk 的接受；
- failure semantics 和 conformance obligations；
- 是否允许进入独立的 Interface Schema Draft gate。

## 11. Non-goals（非目标）

```text
NO_IMPLEMENTATION=true
NO_RUNTIME=true
NO_API=true
NO_CODE_CHANGE=true
NO_SIMULATOR_CHANGE=true
NO_NEW_EXPERIMENT=true
NO_TITMAS_DEPLOYMENT=true
NO_CANONICAL_SCHEMA=true
NO_PERMISSION_AUTHORITY=true
NO_CERTIFICATION=true
```

本文不创建数据库、registry、全局 health score、统一 reputation service、policy engine 或
中央控制平面。
