---
document_id: DBA-TITMAS-DIGITAL-IMMUNE-RESPONSE-PROTOCOL-0.1
title: Digital Immune Response Protocol v0.1
title_zh: 数字免疫响应协议 v0.1
status: development-conceptual-response-semantics-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
constitution_freeze_reference: NOT_PROVIDED
primary_repository: digital-biosphere-architecture
normative_effect: NONE
execution_effect: NONE
policy_effect: NONE
implementation_authorized: false
---

# Digital Immune Response Protocol v0.1（数字免疫响应协议 v0.1）

## 0. Status and Scope（状态与范围）

本文定义开放数字生态中分级、可追溯、可恢复的 immune response（免疫响应）概念语义。
它不定义 transport、endpoint、API、policy engine、自动执行器或 Runtime。

```text
DOCUMENT_MATURITY=Development
DECISION_STATUS=REVIEW_REQUIRED
CONSTITUTION_FREEZE_REFERENCE=NOT_PROVIDED
RESPONSE_AUTHORITY_CREATED=false
AUTOMATIC_ENFORCEMENT_DEFINED=false
IMPLEMENTATION_AUTHORIZED=false
```

本文使用用户提供的 Digital Immune Constitution 概念作为设计输入。当前仓库未发现其
可核验冻结记录，因此这些响应语义仍需 Architecture Review 和 Domain Owner 决策。

## 1. Purpose（目的）

Digital Immune Response Protocol 的目标是定义数字生态面对异常、风险、边界违反和持续
失效时，如何使用最小必要、范围受限、证据优先且保留恢复可能的响应语言。

```text
Response is ecological regulation.
Response is NOT centralized control.
```

协议不决定谁有权响应。每个实际响应必须由适用范围内的明确 Authority 决定，并绑定
Identity、Boundary、Evidence、时间、理由和恢复条件。

## 2. Response Principles（响应原则）

| Principle | Requirement |
|---|---|
| Evidence First | 响应前记录 observation、source、scope 和 uncertainty |
| Least necessary response | 使用足以控制已知风险的最低等级 |
| Scope boundedness | 响应只作用于被授权的主体、能力、时间和环境 |
| Reversibility first | 在可行时优先可撤销、可复核和可恢复措施 |
| History preservation | 不删除失败、争议、响应和恢复历史 |
| No automatic authority | Health、Reputation、score 或 model output 不自动授权响应 |
| Fail closed | Owner、证据、版本或边界冲突时不得扩大动作 |
| Localize failure | 优先隔离局部风险，避免全局连锁控制 |

## 3. Decision Inputs and Semantic Boundaries（决定输入与语义边界）

响应评估可以消费：

- 有来源的 Observation；
- DBOS-admitted Evidence reference；
- 有范围的 Verification reference；
- 带方法、版本和 limitation 的 Health assessment；
- 带上下文和偏差说明的 Reputation assessment；
- 当前 Boundary、Authority 和 lifecycle references。

响应评估不得推导：

```text
Observation != Evidence
Evidence != Permission
Verification != Authority
Health != Certification
Reputation != Authority
Evaluation != Decision
Recommendation != Execution
```

当输入不足时，允许进入 `Level 1: Observation`，但不得仅因未知而自动进入限制、隔离或
退休。

## 4. Response Level 0: Normal（正常）

| Element | Definition |
|---|---|
| Trigger | 当前行为位于有效 Boundary 内，未出现需要升级的有来源异常 |
| Evidence requirement | 当前 Identity、Boundary 和基础 observation references 可追溯 |
| Allowed action | 继续执行已独立授权且处于 Boundary 内的活动；保持常规记录 |
| Forbidden action | 因 `Normal` 状态扩大 Capability、Permission、Authority 或 retention |
| Recovery possibility | 不适用；状态必须持续复核而非永久认证 |

Level 0 不表示安全、正确、可信或永不失效，只表示当前没有足够依据触发更高响应。

## 5. Response Level 1: Observation（观察）

| Element | Definition |
|---|---|
| Trigger | 异常、数据缺失、漂移、轻度不稳定、来源冲突或风险信号需要进一步观察 |
| Evidence requirement | 至少记录 subject、source、time、scope、signal、uncertainty 和 limitation |
| Allowed action | 提高有边界的观察频率；请求补充 Evidence；标记 `UNKNOWN`、`STALE` 或 `CONFLICTED` |
| Forbidden action | 仅凭单个弱信号缩小 Permission；扩大监控到无关主体；把 observation 当 Evidence |
| Recovery possibility | 信号解除或得到合理解释后返回 Level 0，并保留观察历史 |

Level 1 的目的不是惩罚，而是降低不确定性。

## 6. Response Level 2: Restriction（限制）

| Element | Definition |
|---|---|
| Trigger | 有来源的重复异常、明确 Boundary violation、资源风险或可验证的不稳定需要缩小暴露面 |
| Evidence requirement | Evidence/Verification references、受影响范围、严重度、决定者 Authority、时间限制和恢复条件 |
| Allowed action | 在授权范围内降低速率、资源、工具、交互或持续时间；增加人工复核或额外验证 |
| Forbidden action | 修改 Identity 历史；删除 Evidence；扩大到无关主体；把限制变成永久全局 Permission 撤销 |
| Recovery possibility | 满足预先记录的恢复条件并完成复核后，可返回 Level 1 或 Level 0 |

Restriction 必须是最小必要措施，并具有明确期限或复核时间。

## 7. Response Level 3: Isolation（隔离）

| Element | Definition |
|---|---|
| Trigger | 高风险行为持续、完整性严重失败、正在发生的边界突破或局部传播风险无法由限制控制 |
| Evidence requirement | 可追溯 Evidence chain、Identity/Boundary version、原因、scope、决定者、开始时间、复核时间和 rollback 条件 |
| Allowed action | 暂停指定交互；隔离指定资源或连接；保留只读证据访问；启动有边界的恢复评估 |
| Forbidden action | 删除主体历史；全生态黑名单；无期限无复核隔离；将隔离决定传播为全局 Authority |
| Recovery possibility | 通过 Evidence 完整性复核、边界重建和有限恢复观察后，可降至 Level 2 或 Level 1 |

Isolation 必须局部化。协调组件可以传播带来源的隔离状态，但不能替所有生态参与者作出
新的 Authority decision。

## 8. Response Level 4: Retirement（退休）

| Element | Definition |
|---|---|
| Trigger | 生命周期终止条件满足，或持续不可接受风险在多次限制、隔离和恢复后仍不能被有界控制 |
| Evidence requirement | 完整响应 lineage、失败与恢复历史、适用 Authority decision、scope、理由、时间和 successor policy |
| Allowed action | 在授权范围内停止该身份版本的活动；撤销适用绑定；保存 tombstone、lineage、Evidence 和 archive references |
| Forbidden action | 删除或重写历史；声称普遍不可信；自动退休关联主体；把退休解释为数字生命终结 |
| Recovery possibility | 原身份版本不直接恢复；如允许继续，必须建立有来源的新版本或 successor identity，并声明差异 |

Retirement 是生命周期和风险管理动作，不是惩罚、意识判断或科学淘汰定律。

## 9. Response Evaluation Flow（响应评估流程）

```text
Observation
  -> Source and Scope Check
  -> Evidence Reference Assembly
  -> Boundary and Authority Check
  -> Proportionality Review
  -> Human or Bounded Owner Decision
  -> Response Record
  -> Re-evaluation
  -> Recovery, Continued Response, or Retirement
```

每个实际响应记录至少需要表达：

| Concept | Requirement |
|---|---|
| Response identity | 唯一 response reference 和版本 |
| Subject binding | `cell_id`、identity version 和 lineage |
| Level | `0` 至 `4` 中一个明确等级 |
| Trigger references | 不修改原始 observation 和 Evidence |
| Decision authority | 决定者、Authority scope 和有效时间 |
| Action scope | 主体、能力、资源、环境和时限 |
| Recovery conditions | 可验证条件和复核 Owner |
| Outcome | `ACTIVE`、`RECOVERED`、`ESCALATED`、`EXPIRED`、`RETIRED` 或失败状态 |
| Limitations | unknown、conflict、缺失和不可推导结论 |

这些是概念记录要求，不是 API 或序列化 Schema。

## 10. Escalation Rules（升级规则）

- 默认从当前等级进入相邻等级。
- 跨级升级必须记录为什么较低等级不足以控制当前风险。
- 紧急隔离可以跳过 Level 2，但必须有明确 Authority、有限时长和事后复核。
- 自动规则只能提出 candidate response，不得创造 Authority。
- Reputation 下降不能单独触发 Level 2 至 Level 4。
- 未知证据不能被解释为有罪或安全。
- 响应范围不得因网络连接或共同 Owner 自动扩散。

## 11. De-escalation and Recovery（降级与恢复）

- 每个 Level 2 至 Level 4 响应必须声明恢复可能性或明确说明为什么不允许直接恢复。
- 降级需要新 Evidence，不得删除原始触发记录。
- 恢复后必须保留限制、隔离、恢复条件和结果历史。
- 恢复不自动恢复旧 Permission、credential 或 resource allocation。
- 恢复失败必须被保留，不得从发布结果中选择性排除。
- Level 4 的后继主体必须使用新 identity version 或 successor identity。

## 12. Distributed Ecological Regulation（分布式生态调节）

### Principle of Distributed Complexity Generation（分布式复杂性生成原则）

> Do not create one infinitely powerful center. Generate large-scale capability
> through many simple, bounded, composable subjects.

中文：不创建一个无限强大的中心，而通过大量简单、受限、可组合的主体生成大规模能力。

Digital Immune Response 必须遵守：

| Principle | Response consequence |
|---|---|
| Evidence First | 先观察和保留历史，再形成有边界决定 |
| Bounded Autonomy | 主体自治和响应 Authority 都受 scope 限制 |
| Digital Homeostasis | 响应目标是恢复动态稳态，不是最大化控制 |
| Evolutionary Selection | 选择结果可以被观察，但 score 不自动决定存续 |
| Open Evolution | 恢复、取代和退休保留 lineage 与版本差异 |

分布式不等于无治理。有限协调可以存在，但必须可审计、可替换、可撤销，并且不能把局部
响应聚合为无限强中心。

## 13. Limitations and Recommendation Gate（限制与推荐闸门）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CONCEPTUAL_GRADED_RESPONSE_SEMANTICS
NOT_RECOMMENDED_AS=AUTOMATIC_ENFORCEMENT_OR_RUNTIME_CONTROL
IMPLEMENTATION_RECOMMENDED_NOW=false
```

不推荐实现的当前原因：

- Digital Immune Constitution 的 repository freeze reference 未提供；
- Response Authority、Boundary Owner 和 Health Owner 尚未冻结；
- TITMAS Interface v0.1 不具备冻结条件；
- 没有 response conformance cases、negative tests 或独立实现反馈；
- Level 2 至 Level 4 的法律、运营和跨域责任尚未定义。

## 14. Non-goals（非目标）

```text
NO_IMPLEMENTATION=true
NO_RUNTIME=true
NO_API=true
NO_CODE_CHANGE=true
NO_SIMULATOR_CHANGE=true
NO_NEW_EXPERIMENT=true
NO_TITMAS_DEPLOYMENT=true
NO_CENTRALIZED_CONTROL=true
NO_AUTOMATIC_ENFORCEMENT=true
NO_PERMISSION_AUTHORITY=true
```

本文不定义 AI consciousness（AI 意识）、digital life（数字生命）、自动惩罚、全局黑名单、
认证系统、生产隔离服务或数字主体消灭机制。
