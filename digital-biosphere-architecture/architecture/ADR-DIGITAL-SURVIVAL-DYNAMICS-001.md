---
adr_id: ADR-DIGITAL-SURVIVAL-DYNAMICS-001
title: Digital Survival Dynamics Architecture Decision v0.1
title_zh: 数字生存动力学架构决策 v0.1
status: accepted-theoretical-foundation
decided_by_ref: zhangbin
decided_at: 2026-07-24
primary_repository: digital-biosphere-architecture
architecture_layer: theory-layer
implementation_authorized: false
external_action_authorized: false
evolution_authority_effect: none
selection_dynamics_position_fixed: true
---

# ADR: Digital Survival Dynamics v0.1（数字生存动力学 v0.1）

中文：数字生存动力学 ADR，定义 DBA 中“选择”问题从局部行为解释升级为长期生态稳定研究问题。

## 1. Problem Definition（问题定义）

### 1.1 现有问题

仅围绕“Agent 为什么选择这个目标而不是那个目标”无法回答：
- 环境持续变化时，生态是否可长期存在；
- 高适配策略是否导致单点脆弱；
- 多样性衰退如何影响中长期稳态；
- 失败后系统如何恢复与再平衡。

### 1.2 v0.2 研究问题

> 在持续变化、不确定和竞争环境中，数字智能体生态如何保持长期生存能力？

其中“生存”包括可持续运行、适应、资源动态平衡与复原能力，不等于收益最大化。

## 2. Why Agent Selection Becomes Infrastructure Problem（为什么选择变成基础设施问题）

`Selection` 在单 Agent 场景是局部策略问题；在多智能体生态中它会成为以下基础设施问题：

- 选择结果会改变资源流、失败率和协作拓扑；
- 局部优化可快速造成全局集中与脆弱性；
- 选择证据链可能被误用为“能力真值”；
- 长期效应无法由单一 runtime 组件独立解释。

因此选择不能只由应用层定义；必须有标准化的观测模型、边界对象和可验证证据链。

## 3. Relation to PageRank（与 PageRank 的关系）

PageRank 建模的是图中结构性影响扩散；Selection Dynamics 可借鉴其“传播权重”思想，但关系不同：

- PageRank：基于连接结构，通常关注静态图权重传递；
- Selection Dynamics：基于行为语义、能力边界、资源状态与时序语境；
- PageRank 输出不是授权，也不表达执行命令；
- Selection Dynamics 输出只能是可被解释和核验的 `Selection Evidence`（选择证据）。

可以使用 PageRank 作为候选参考模型之一，但不将其语义直接提升为生存结论。

## 4. Selection Dynamics Model（选择动力学模型）

### 4.1 角色与作用

- Selection Dynamics（子机制）回答“为何被选/未选”；
- Digital Survival Dynamics（父机制）回答“该选择模式是否促进长期生存”；
- SAEE 作为演化评价参与者提供演化指标，但不拥有执行权。

### 4.2 状态语义（信息与证据）

```text
Selection Trace = {target_candidates, candidate_scores, chosen_candidate, alternatives, decision_rationale, provenance}
Selection Evidence = {why_selected, why_rejected_or_competitive, confidence, failure_modes, governance_scope}
```

所有决策输出必须保留：`UNKNOWN`、`CONFLICTED`、`PARTIAL`、`HOLD` 类边界语义（沿用既有审核语义）。

## 5. AgentRank Theory（AgentRank 理论）

`AgentRank` 定义为“选择上下文中的可解释排序分数”，非信任分数，非权限分数，非最终决策分数。

基本含义：
- 可解释性高于绝对高分；
- 时间窗口是关键变量；
- 排名必须绑定 `provenance + context + policy_scope + failure_modes`；
- 排名下降条件包括拒绝、异常、冲突、缺失上下文。

**不变量**：

```text
AGENT_RANK != TRUST
AGENT_RANK != AUTHORIZATION
AGENT_RANK != EXECUTION_DECISION
```

## 6. Decision Evidence Philosophy（Decision Evidence 哲学）

Decision Evidence 的作用是“回答为什么做出选择建议”，不是“回答谁该执行”：

- 它说明证据链、替代项、限制、失败前提；
- 不能替代 Governance Decision；
- 不能替代 DBOS 的 Execution/Evidence 事实记录；
- 不能直接触发执行动作。

适用原则：`advisory evidence only`（仅供建议），并要求明确可追溯引用。

## 7. Integration with System Layers（与系统层关系）

### 7.1 与 TITMAS

TITMAS 提供互操作边界、对象类型映射与版本化交接，不做演化策略裁决。

### 7.2 与 DBOS

DBOS 保持生命体的身份与生命周期控制；Selection/Survival 输出仅作为输入证据，不产生状态写入。

### 7.3 与 EEOAP

EEOAP 负责执行与治理事件的证据规范映射，Selection 输出可引用其结果，但不能替代其执行真实性。

### 7.4 与 SAEE

SAEE 可基于 Selection/Survival证据形成 Evolutionary Recommendation（演化建议），仍为 advisory-only。

### 7.5 与 VEC/证书体系

VEC 可用于执行证据的可验证链路引用，但不得将证书解释为执行许可。

## 8. New Core Variables（核心变量定义）

1. **Adaptation（适应）**  
   衡量环境变化后恢复和重构策略的速度。
2. **Balance（平衡）**  
   衡量效率与稳定性的持续平衡程度，避免短期过度集中。
3. **Diversity（多样性）**  
   衡量策略/角色/资源分配分布的异质性与抗冲击冗余。
4. **Resilience（韧性）**  
   衡量故障或冲击后的恢复时间、损失曲线与再平衡能力。

### 8.1 生存适应度（概念性）

概念性表达：

```text
SurvivalFitness = g(AdaptationVelocity, BalanceStability, DiversityIndex, RecoveryTime, Horizon, DisturbanceProfile)
```

`g(...)` 为实验域定义且可替换的函数，禁止将任何单一变量作为唯一裁决标准。

## 9. Ecosystem Concept（生态系统概念）

生态稳定来自“生态位分配 + 选择压力 + 适应反馈 + 多样性维持”；  
研究对象是“数字生命系统”的动态平衡，而非单个 Agent 最大化能力的静态最优解。

## 10. Required Constraints（强制约束）

```text
selection != authorization
evidence != permission
recommendation != command
score != trust
selection_dynamics != governance_control_surface
```

## 11. Decision and Versioning（决定与版本化）

- 决定将本 ADR 作为 `v0.1` 理论冻结依据；
- 后续 `Selection Dynamics` API 方案必须在本 ADR 下提交；
- 新的 `v0.2` 或修订版本必须声明与 v0.1 的兼容策略；
- 所有未来实验与引用必须在实验对象中显式声明 `survival_scope` 与 `selection_scope`。

## 12. Consequences（影响）

- 将研究重点从“单次选择正确性”改为“长期生存有效性”；
- 为 DEB-001 及其后续试验提供统一解释框架；
- 强化边界纪律：选择输出 = 建议性证据；执行/授权仍由 DBOS 与治理决策负责；
- 降低单一指标治理风险，支持长期生态观察。

## 13. Non-implementation Commitment（非实现声明）

```text
DIGITAL_SURVIVAL_DYNAMICS_DECIDED=true
ARCHITECTURE_SPEC_DEFINED=true
ALGORITHMS_IMPLEMENTED=false
SCHEMA_IMPLEMENTED=false
API_IMPLEMENTED=false
RUNTIME_IMPLEMENTED=false
AUTHORITY_EFFECT=false
```

