---
spec_id: DBA-ARCHITECTURE-AUTHORITY-MODEL-0.1
title: Digital Biosphere Architecture Authority Model v0.1
title_zh: 数字生物圈架构权力模型 v0.1
status: non-executable-authority-boundary-specification
authority_assignments_created: false
execution_authority_created: false
permission_effect: none
runtime_effect: none
---

# Digital Biosphere Architecture Authority Model v0.1

本模型把规则、运行和演化评价分为三种不可互相替代的 authority domain（权力责任域）。这里的 Authority 表示有限的规范责任，不表示本文件创建了真实授权主体、账号、Permission 或执行能力。

## 1. Architecture Authority（架构权力）

负责：Rules（规则）。

Architecture Authority 负责维护 Digital Biosphere Stack 的规范定义、边界、不变量、ADR 和架构变更记录。它只作用于 architecture truth（架构规范事实），不直接形成 operational truth（运行事实）或 evolution assessment（演化评价）。

它不能：

- 直接执行 DBOS 生命周期变化；
- 授予 Entity Capability、Permission 或 Runtime 权限；
- 修改 SAEE 算法、Fitness 模型或演化结论；
- 用规范文本声称代码、接口或集成已经实现。

## 2. Operational Authority（运行权力）

负责：Operation（运行）。

Operational Authority 属于 DBOS 的责任域：在另行有效的 Authorization、Capability Boundary、Context 和 Lifecycle control 下，管理 Identity、Capability records、Execution、Evidence、Verification、Federation 和 Lifecycle 的有界运行过程与记录。

Operational Authority 不表示 DBOS 是最终授权者。DBOS 可以因运行约束拒绝执行，但不能：

- 单方面修改 Architecture Specification；
- 发明或改写 SAEE 的 Fitness、Risk 或 Evolution conclusions；
- 把 Architecture Decision 或 Governance Decision 自动执行；
- 自动扩大 Capability 或 Permission。

## 3. Evolution Authority（演化权力）

负责：Evolution Evaluation（演化评价）。

Evolution Authority 属于 SAEE 的责任域：基于有来源、有范围的输入形成 Evidence Evaluation、Fitness Assessment、Risk Assessment、Evolution Modeling、Ecological Stability Analysis 与 Recommendation。

Evolution Authority 不能：

- 修改 DBOS Identity、Capability、Execution、Evidence 或 Lifecycle State；
- 将 Recommendation 直接升级为 Decision、Authorization 或 Execution；
- 单方面修改 Architecture Specification 或自身生态规则；
- 通过评价结果取得 Operational Authority。

## 4. 三权不可替代矩阵

| 事项 | Architecture Authority | Operational Authority / DBOS | Evolution Authority / SAEE |
|---|---|---|---|
| 维护规范规则与 ADR | 负责 | 提供领域约束，不单方面修改 | 提供领域约束，不单方面修改 |
| 形成运行记录 | 不负责 | 负责 | 读取和引用 |
| 形成演化评价 | 不负责 | 提供输入 | 负责 |
| 执行已授权变化 | 无执行权 | 在生命周期控制下负责 | 无执行权 |
| 修改 SAEE 内部算法 | 无权 | 无权 | SAEE 内部责任，但不得绕过架构变更流程修改跨域规则 |
| 改变架构边界 | 经显式架构变更流程维护 | 不能单方面决定 | 不能单方面决定 |

```text
Architecture Authority ≠ Operational Authority
Architecture Authority ≠ Evolution Authority
Architecture Authority ≠ Execution Authority
Operational Authority ≠ Evolution Authority
DBOS ≠ SAEE
```

## 5. Decision Authority（决策权力）边界

Governance Decision Layer 可以在项目映射中标记为 Decision Authority boundary（决策权力边界），但它的含义仅是规范和记录 Decision Object 的状态与追溯要求。它不自带最终授权者，也不是第四种可以取代上述三种权力的运行主体。

- 对 SAEE Recommendation 的采纳，需要明确的 decision authority reference（决策授权来源）；
- 对 Architecture Change Proposal 的接受，需要明确的 architecture decision record（架构决策记录）；
- 两者均不因记录为 `accepted` 或 `approved` 而成为 Execution；
- 具体授权者、角色指派和职责分离由本规范之外的治理制度定义。

## 6. 权力交接规则

```text
Architecture rule
  informs but does not execute
        ↓
Explicit Decision / Authorization
        ↓
DBOS operational gate
        ↓
Execution + Evidence + Verification
        ↓
SAEE optional evaluation
        ↓
Recommendation, not rule change
```

任一箭头都是责任交接，不是权力继承。下游不能反向改写上游记录；新信息需要通过新的记录和相应治理流程表达。

## 7. 非授权声明

```text
AUTHORITY_MODEL_DEFINED=true
ARCHITECTURE_AUTHORITY_ASSIGNED=false
OPERATIONAL_AUTHORITY_EXPANDED=false
EVOLUTION_AUTHORITY_EXPANDED=false
FINAL_DECISION_AUTHORITY_DEFINED=false
EXECUTION_AUTHORITY_CREATED=false
PERMISSION_GRANTED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
```
