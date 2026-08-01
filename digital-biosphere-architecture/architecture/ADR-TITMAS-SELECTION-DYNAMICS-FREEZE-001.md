---
adr_id: ADR-TITMAS-SELECTION-DYNAMICS-FREEZE-001
title: Freeze Selection Dynamics Foundation in TITMAS
title_zh: 冻结 TITMAS Selection Dynamics 基础
status: architecture-freeze-stable-foundation
decided_by_ref: zhangbin
decided_at: 2026-07-24
primary_repository: digital-biosphere-architecture
implementation_authorized: false
runtime_authorized: false
schema_authorization: false
external_action_authorized: false
release_authorized: false
non_executable: true
scope: technical-foundation-freeze-no-new-features
---

# ADR-TITMAS-SELECTION-DYNAMICS-FREEZE-001

## 1. Purpose（目的）

本 ADR 的目的是冻结当前 `TITMAS Selection Dynamics` 技术分支，明确其作为 DBL（Digital Biosphere Laboratory）理论框架下的稳定子系统边界。  
仅做技术边界冻结，不新增特性，不定义 API，不执行实现。

本文件不产生运行权限、不提供授权入口、不替代发布与运行决策。

## 2. Evolution History（演进历史）

Selection Dynamics 的当前技术分支演化链如下：

```text
Selection Pressure Engine
  -> AgentRank
  -> Decision Evidence
  -> Conformance Model
  -> Certification Model
  -> Registry Integration
```

### 2.1 解读

- **Selection Pressure Engine**：定义候选目标/行动竞争与压力表达机制。
- **AgentRank**：提供可解释的候选排序与选择偏好表示（非信任分）；
- **Decision Evidence**：将选择链路中的“为何如此建议”结构化为可重放的证据对象；
- **Conformance Model**：定义兼容性/边界一致性验证框架；
- **Certification Model**：定义执行能力层面的合规模型与可验证声明；
- **Registry**：提供规范、实现、验证与扩展项的公开索引与生命周期可观测性。

该链路目前稳定为技术基础，不要求在本层引入生存理论扩展。

## 3. Current Responsibilities（当前职责）

Selection Dynamics 当前承担三类职责：

1. **Explain agent target/action selection（解释 agent 目标/动作选择）**
   - 在可见上下文中说明候选生成与选择路径；
   - 明确说明选择范围、限制与替代项处理语义。

2. **Produce advisory evidence（产出建议性证据）**
   - 输出用于治理与评估层的建议证据对象；
   - 输出中必须保留来源、版本、限制、冲突和失败状态。

3. **Support replay and audit（支持回放与审计）**
- 提供可重放结构（包括失败路径与未知路径）；
- 支持跨层审计复核（不直接执行、不直接写生命周期）。

## 4. Explicit Non-goals（明确非目标）

Selection Dynamics 不是以下内容的责任域：

1. **Not survival theory（不是生存理论）**  
   生存理论由 `Digital Survival Dynamics` 承担，SD 是其测度与选择机制子层。

2. **Not execution authorization（不是执行授权）**  
   Selection 输出为建议，不构成 Permission、Capability grant、Command 或执行批准。

3. **Not policy authority（不是政策权限）**  
   不拥有治理裁决权，不取代 DBA/DBOS/人类决策层。

4. **Not trust scoring（不是信任评分）**  
   `AgentRank` 与排序值不等同 `trust`，不产生信誉、合规、可信身份或安全断言。

## 5. New Positioning（新定位）

冻结后的架构位置如下：

```text
Digital Survival Dynamics
  -> Selection Dynamics (subsystem)
     -> Selection Pressure Engine
     -> AgentRank
     -> Decision Evidence
     -> Conformance
     -> Certification
     -> Registry
```

- Selection Dynamics 成为 DBL 的测度级子系统，而非核心研究替代层；
- 它的唯一上行目标是可解释、可复核的选择机制输出；
- 不再承担生态生命周期总目标定义。

## 6. Future Dependency（未来依赖关系）

### 6.1 上游依赖

- `Digital Survival Dynamics` 提供高阶研究问题框架；
- 其任务是解释生态在动态环境下的长期生存能力、适应性与稳定性。

### 6.2 下游依赖

- Selection Dynamics 提供可测量的选择机制与证据链；
- 供 Evidence Architecture、TITMAS、SAEE、Registry 在各自边界内消费。

### 6.3 依赖边界

```text
digital-survival-research-questions -> selection-mechanism-models -> advisory-evidence -> governance review
```

任一层级不得将下层输出上升为授权或最终决策。

## 7. Freeze Specifications（冻结规范清单）

以下规范分支在本 ADR 下进入冻结状态（“定义层稳定，扩展需经 ADR 修订”）：

- **AgentRank**
  - 作为可解释候选排序机制被冻结；
  - 保留排序与解释分离语义，禁止用于 trust/permission 语义升级。

- **Selection Pressure**
  - 冻结为可选候选集合、压力分配、候选比较与替代项记录的框架。
  - 冻结核心语义为“selection pressure is advisory context enrichment”。

- **Decision Evidence**
  - 冻结为建议性证据对象生成规则与 provenance/failure-state 记录约束。
  - 不扩展为执行结果证明或执行许可。

- **Conformance Model**
  - 冻结为兼容性、边界、语义提升与负例行为的验证范围；
  - 继续要求 schema 与 boundary 兼容测试，但不引入执行控制。

## 8. Invariants（强制不变量）

```text
selection != authorization
score != trust
evidence != permission
recommendation != command
selection_output != decision_authority
selection_context != policy_enforcement
```

## 9. Governance and Maturity Status（治理与成熟状态）

```text
SELECTION_DYNAMICS_FREEZE_ACTIVE=true
SELECTION_DYNAMICS_IS_SUBSYSTEM_OF_SURVIVAL_DYNAMICS=true
NEW_FEATURES_FROZEN=true
IMPLEMENTATION_FREEZE=true
API_EXTENSION_FROZEN=true
ADVISORY_ONLY=true
AUTHORIZATION_EFFECT=false
POLICY_AUTHORITY_EFFECT=false
TRUST_SCORE_EFFECT=false
```

## 10. Required Update Flow（后续更新流程）

任何对本文件范围外的核心语义变更必须提交新 ADR：

1. 变更影响对象语义（如 decision evidence 的权责定义）；
2. 变更影响依赖关系（如与 Registry 的 ownership）；
3. 变更影响边界不变量（如 recommendation 语义扩展）。

新变更必须经过 DBA 架构层审核，不得通过文档补丁直接覆盖 freeze 边界。

## 11. Decision（决定）

确认 `TITMAS Selection Dynamics` 当前分支冻结为稳定技术基础。  
在未另行 ADR 修订前，禁止新增功能、禁止实现扩展、禁止将建议性输出转化为执行权限路径。

## 12. References（参考）

- Digital Survival Dynamics Theory ADR（`ADR-DIGITAL-SURVIVAL-DYNAMICS-THEORY-001.md`）
- Selection Dynamics 相关 ADR 与规范系列（本仓库已有 ADR-xxx、Schema 与 Conformance 路径）
- `open-infrastructure-strategy-constitution.md`
