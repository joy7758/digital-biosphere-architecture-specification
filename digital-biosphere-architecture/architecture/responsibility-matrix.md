---
spec_id: DBA-RESPONSIBILITY-MATRIX-0.1
title: SAEE-DBOS-Digital Entity Responsibility Matrix v0.1
status: architecture-responsibility-matrix
implementation_claims: none
---

# Responsibility Matrix v0.1（职责矩阵 v0.1）

## 1. 读取规则

“负责”表示概念职责所有权，不表示当前代码已实现；“提供”表示提供输入或记录，不表示结论成立；“使用”表示只读消费，不表示获得写权限；“执行约束”只表示在另有授权时落实 DBOS 自身职责范围内的约束，不表示 DBOS 拥有演化策略。

## 2. 核心矩阵

| 能力或事项 | DBOS | SAEE | Digital Entity | 边界说明 |
|---|---|---|---|---|
| Registration（注册） | 负责注册记录与状态 | 可读取群体构成信息 | 提供候选主体材料 | 注册不等于验证、能力或授权 |
| Identity（身份） | 负责身份引用与状态 | 读取并引用 | 被标识，不自证 | SAEE 不创建或修改身份 |
| Capability（能力） | 负责 Capability Object、验证、边界、Permission gate 与生命周期记录 | 评价表现、风险和适应性 | 声明有边界的候选能力 | Capability 不等于 Authority 或 Permission；DBOS 不自动扩大能力 |
| Execution（执行） | 负责受约束的执行面语义和执行记录 | 不负责执行；读取历史 | 执行具体任务 | 本规范不声明执行能力已实现 |
| Execution History（执行历史） | 产生或登记有来源的记录 | 使用 | 是记录来源之一 | 记录存在不等于执行正确 |
| Evidence（证据） | 采集、登记或引用 Evidence Bundle | 评价 | 产生行为与任务结果材料 | DBOS 产生/管理证据材料，SAEE 评价证据；证据不自动等于真相 |
| Verification（验证） | 负责有界验证结果 | 使用并纳入评价 | 提供被验证对象或材料 | 验证结果不自动等于适应度 |
| Resource Usage（资源使用） | 记录或提供数据 | 解释为适应度/风险输入 | 在执行中消耗资源 | 用量本身不带价值判断 |
| Behavior Trace（行为轨迹） | 记录或引用 | 评价模式与风险 | 产生行为 | 轨迹不自动证明意图或因果 |
| Fitness（适应度） | 提供身份、运行、资源与验证数据 | 负责 Fitness Assessment | 被评价 | DBOS 不定义 SAEE 适应度算法 |
| Risk（风险） | 提供运行约束与历史输入 | 负责 Risk Assessment | 暴露任务情境与影响 | 风险评估不自动执行限制 |
| Ecological Stability（生态稳定性） | 提供群体与运行侧材料 | 负责分析 | 作为生态成员被观察 | 局部验证不能替代生态分析 |
| Selection（选择） | 提供可行性与存在约束 | 负责比较、建模与提出选择建议 | 不自选为优胜者 | 选择建议仍需独立授权 |
| Evolution（演化） | 在独立授权后执行自身职责内的约束或状态处理 | 负责建模、评价与建议 | 仅在另有授权时实现具体变化 | SAEE 负责演化；DBOS 不管理 SAEE 算法；建议不等于执行 |
| Digital Organism Qualification（数字有机体资格） | 提供并管理 Identity、History、Evidence、Lineage 与资格记录 | 负责 Adaptation、Fitness、Evolution 和生态评价 | 作为候选或被评价 Entity | Governance Decision 决定资格采纳；Entity、Agent 或 Capability 不自动成为 Organism |
| Governance Suggestion（治理建议） | 接收、记录并按独立 gate 处理 | 负责提出 | 可受治理影响 | 不自动成为 DBOS policy |
| Federation（联邦） | 负责存在与互操作边界语义 | 可评价跨域适应度和风险 | 可作为联邦参与者 | 本规范不声明联邦能力已实现 |
| Retirement（退役） | 负责生命周期状态记录与历史连续性 | 可提出风险或演化建议 | 被退役但历史记录保留 | 最终授权主体未在 v0.1 定义 |

## 3. 最小职责摘要

```text
Identity:      DBOS负责；SAEE读取
Evidence:      DBOS保留规范责任；Agent Evidence可提供可移植参考实现；SAEE评价
Audit:         ARO可提供审计投影与有界完整性验证；不取代DBOS规范Verification
Verification:  DBOS负责；SAEE使用
Fitness:       DBOS提供数据；SAEE负责
Evolution:     DBOS仅落实另行授权的运行/生命周期约束；SAEE负责建模与建议
Task Work:     Digital Entity负责；DBOS记录；SAEE评价
```

## 4. 跨层组件规则

POP、ARO、Agent Evidence、Token Governor 等相邻组件可以承担某个责任域的具体实现、适配或支持角色，但本矩阵不自动把它们并入 DBOS 或 SAEE。每个跨层关系必须在项目级 contract（契约）中说明：

- canonical data owner（规范数据责任方）；
- fact type（事实类型）；
- read/write boundary（读写边界）；
- authorization source（授权来源）；
- failure and unknown semantics（失败与未知语义）；
- 与既有能力的重复建设结论。

## 5. Evidence-to-Decision Chain Clarification（证据到决定责任链澄清）

本节只澄清 v0.1 已有责任，不创建新权力或实现。其 agent-readable（智能体可读）镜像见
[`program-source-and-responsibility-registry.json`](program-source-and-responsibility-registry.json)。

| stage | 规范架构 Owner | 支持或参考角色 | 明确不产生 |
|---|---|---|---|
| Version-pinned Runtime Record（版本固定运行记录） | DBOS 负责规范登记与引用 | 来源 Runtime 只发出有 provenance（来源）的记录；Dapr、Microsoft 等是外部来源候选 | Truth、充分性、授权 |
| Evidence Material / Reference（证据材料／引用） | DBOS | 外部 signature、attestation、telemetry | Verification、Evaluation、Permission |
| Portable Evidence Package（可移植证据包） | DBOS 保留规范 Evidence 责任 | Agent Evidence 独立参考实现 | 事件真实性、全局充分性、法律不可否认性 |
| Audit Projection / Integrity Check（审计投影／完整性检查） | DBOS 保留规范 Verification 责任 | ARO tamper-evident journal、receipt 与 bounded verifier | 全局 freshness、语义真相、身份授权 |
| Canonical Verification（规范验证） | DBOS | 可消费带 provenance（来源）的外部 verifier result | Fitness、Recommendation、Decision |
| Evidence Adequacy / Evaluation（证据充分性／评价） | SAEE | 消费有界 Evidence 与 Verification | Truth、Permission、Execution |
| Governance Decision（治理决定） | 独立 Human Decision / Authorization boundary | DBA 定义流程；SAEE 提供建议；DBOS 提供事实 | 自动执行、自动发布 |
| Authorized Execution（获授权执行） | DBOS + 具体 Digital Entity | 显式 Authorization Record | Release、Adoption、Certification |
| Release（发布） | Human Release Authority | source commits、验证、限制、试用结果和 `released_by_ref` | Production Readiness、Customer Adoption 的自动推导 |

### 5.1 Duplicate-build stop rule（重复建设停止规则）

出现以下任一情况时必须输出 `REVIEW_REQUIRED` 并停止实现：

- 为同一 fact type（事实类型）创建第二个 canonical owner；
- 在未审计 Agent Evidence 或 ARO 现有能力前新增 receipt、hash chain、Merkle 或 export stack；
- 把 ARO audit result 写成 DBOS Canonical Verification；
- 把 DBOS Verification 写成 SAEE Fitness / Recommendation；
- 把 SAEE Recommendation 写成 Human Decision、Permission、Execution 或 Release；
- 把外部 Runtime signature 写成事件真实性、证据充分性或身份授权。

```text
RESPONSIBILITY_CHAIN_CLARIFIED=true
CANONICAL_OWNER_CHANGED=false
ADJACENT_PROJECT_ADMITTED=false
NEW_RECEIPT_STACK_AUTHORIZED=false
NEW_HASH_CHAIN_AUTHORIZED=false
NEW_RUNTIME_AUTHORIZED=false
```
