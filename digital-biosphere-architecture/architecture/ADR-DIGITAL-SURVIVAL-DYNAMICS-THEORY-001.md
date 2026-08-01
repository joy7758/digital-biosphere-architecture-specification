---
adr_id: ADR-DIGITAL-SURVIVAL-DYNAMICS-THEORY-001
title: Digital Biosphere Laboratory Theoretical Charter on Digital Survival Dynamics
title_zh: 数字生物圈实验室数字生存动力学理论章程
status: accepted-theoretical-foundation
decided_by_ref: zhangbin
decided_at: 2026-07-24
primary_repository: digital-biosphere-architecture
architecture_layer: theory-layer
document_type: research-theory-adr
implementation_authorized: false
schema_authorized: false
runtime_authorized: false
external_action_authorized: false
release_authorized: false
---

# ADR-DIGITAL-SURVIVAL-DYNAMICS-THEORY-001

## 1. Core Research Question（核心研究问题）

### 1.1 From（变化）

从：

> How does an agent select actions?

到：

> How do autonomous digital ecosystems survive, adapt, and evolve under changing environments?

中文：在持续变化与不确定环境中，数字智能生态如何保持长期生存、适应与演化？

### 1.2 研究转向原则

该 ADR 将研究目标从“单一代理决策准确性”升级为“生态长期稳定性”。  
其核心不变量为：

- 选择行为不是终点，生存稳定是目标；
- 证据优先于解释，结论必须可重放；
- 生存研究优先于规模扩张；
- 本 ADR 只定义理论边界，不定义执行机制、授权、权限系统或运行实现。

## 2. System Relationship（系统关系）

### 2.1 关系图（概念）

```text
Digital Biosphere Laboratory
  -> Digital Survival Dynamics
     -> Selection Dynamics
     -> Adaptation
     -> Balance
     -> Diversity
     -> Resilience
  -> Digital Ecology Box（实验单元）
  -> Observed Findings（观察发现）
  -> Guidance Inputs（治理与实现输入）

Guidance Inputs
  -> Evidence Architecture（证据架构）
  -> TITMAS（互操作与边界映射）
  -> SAEE（演化评价输入）
  -> Registry（规范/实现/验证可见性）
```

### 2.2 组件作用定义

- **Digital Biosphere Laboratory（DBL）**  
  负责定义开放研究问题、实验范式与可复现方法论；不创造执行权限或调度控制。

- **Digital Survival Dynamics（DSD）**  
  最高级理论层，定义“在变化环境中生态能否长期存在”的机制框架。

- **Selection Dynamics（SD）**  
  DSD 的子机制之一，解释在给定约束与上下文中的选择过程与候选排序逻辑。

- **TITMAS**  
  作为 Evidence Architecture 的互操作映射层，约束 ID、Execution、Evidence、Verification 的边界交接。

- **Evidence Architecture（证据架构）**  
  提供观测、溯源、重放和边界状态（unknown/partial/conflicted/failed）的一致管理。

- **SAEE**  
  提供演化评价输入与建议性输出，不是命令来源。

- **Registry**  
  作为索引与发现层，记录规范、实现、验证方法与扩展项状态，不赋予执行权限。

### 2.3 约束对齐

```text
selection != authorization
evidence != permission
recommendation != command
capability score != trust score
selection output != execution right
```

## 3. DSD 作为父理论（Parent Theory）

Digital Survival Dynamics 由五个核心子机制组成：

- **Selection（选择）**：为何某策略、目标或动作被优先考虑。
- **Adaptation（适应）**：环境变化后恢复与调整能力。
- **Balance（平衡）**：效率、稳定与长期风险之间的张力平衡。
- **Diversity（多样性）**：策略、角色与行为分布的异质性。
- **Resilience（韧性）**：扰动后恢复和再平衡能力。

五者联合产生生存相关结论：  
短期表现不能替代长期生存力；稳定性与可恢复性必须与适应行为共同考量。

## 4. Capability Optimization vs Survival Optimization vs Ecosystem Stability

### 4.1 Capability optimization（能力优化）

优化个体或子系统在给定任务上的执行质量（吞吐、准确、响应等），通常是局部指标。

- 风险：可能在高压情景中放大集中和脆弱性。

### 4.2 Survival optimization（生存优化）

优化系统在长期环境变化中的持续存在概率，关注鲁棒性、恢复能力、资源循环和协作维持。

- 特点：允许短期代价换取长期不确定性缓冲。

### 4.3 Ecosystem stability（生态稳定）

生态层面上，群体行为、资源分配和规则变化下的系统平衡状态与退化阻力。

- 与生存优化相关，但更强调群体层耦合与系统边界健康度，而非单体表现。

### 4.4 关系

```text
Capability optimization (局部) ⊄ Survival optimization (系统)
Survival optimization + Diversity + Balance -> Ecosystem stability
```

## 5. Biological Analogy（生物类比）

本 ADR 采用**bio-inspired system dynamics**（生物启发系统动力学）作类比，而不将数字智能体当作生物体或生命体宣告。

### 5.1 类比概念

- **adaptation（适应）**：环境边界变化时的行为重构能力；
- **ecological niche（生态位）**：在资源、规则与交互空间中的可行生存区域；
- **selection pressure（选择压力）**：环境条件、竞争和约束对行为分布施加的压力；
- **resilience（韧性）**：系统遭扰动后的反弹与复归能力；
- **extinction（灭绝）**：在实验语境中指生态角色长期失活或退出竞争过程。

### 5.2 谨慎边界

这些类比仅用于模型启发：
- 不等价于生物学定理；
- 不支持把数字对象视作生物生命；
- 不用于替代统计或系统验证结果。

## 6. Core Research Metrics（核心研究指标）

### 6.1 Adaptation Velocity（适应速度）
单位时间内从环境变化到策略重构/行为校正的可测速率。

### 6.2 Diversity Index（多样性指数）
度量候选策略、行为类别、资源占用方式或决策风格的异质程度。

### 6.3 Resource Concentration（资源集中度）
度量资源对少数策略/主体的集中程度，关联系统脆弱性。

### 6.4 Resilience（韧性）
系统在扰动出现后维持关键功能与可用性的能力，通常以恢复轨迹与损失幅度描述。

### 6.5 Recovery Time（恢复时间）
从故障/冲击识别到关键指标回归可接受区间的时长。

### 6.6 Ecosystem Stability（生态稳定性）
长期序列中指标波动幅度、失衡风险与重分配恢复能力的综合量度。

## 7. First Research Hypothesis（首个研究假设）

> Under dynamic environments, systems optimized only for short-term performance may show lower long-term survival robustness than systems balancing performance, diversity, and adaptability.

中文表述：在动态环境中，只优化短期性能的系统，可能在长期生存韧性上不如在性能、策略多样性与适应性之间保持平衡的系统。

该假设将通过 DEB 系列实验与可复现证据进行反复检验。

## 8. Future Experiment Principles（未来实验原则）

1. **Observation before governance（观察先于治理）**  
   先建立可观测事实，再进行治理层解释。

2. **Evidence before conclusion（证据先于结论）**  
   先确认 provenance、replayability、failure state，再作理论归纳。

3. **Reproducibility before optimization（复现先于优化）**  
   任何实验结果在优化方向前，先形成至少一个独立复现验证。

4. **Survival before scale（生存先于规模）**  
   优先验证长期稳定性，再讨论规模扩展与工程化。

## 9. Relationship with Human Civilization Knowledge（文明知识映射）

### 9.1 Yin-Yang（阴阳）与动态平衡

阴阳可作为“非线性动态平衡”隐喻：系统稳定并非静止，而是通过张力平衡保持可持续。

### 9.2 Zhongyong（中庸）与过度优化

中庸可作为“不过度偏移”原则：避免将单一指标极端化，保留调整空间和调和路径。

### 9.3 Complex systems theory（复杂系统理论）

与复杂系统理论一致地强调涌现、反馈、局部—整体耦合和相变风险，但不将其与哲学命题混同。

### 9.4 Evolutionary computation（进化计算）

进化计算中强调适应性与群体搜索机制，本框架只借鉴其方法性，不将其结果直接外推为数字生态长期真理。

## 10. Theoretical Non-goals（理论非目标）

- 不把 Selection Dynamics 再次定义为 AI 安全、政策执行或授权系统；
- 不把 Recommendation、Score、Evidence 等概念提升为授权、权限或执行命令；
- 不把“生存研究”理解为价值判断的终极解释，仅作为治理/设计输入之一；
- 不承诺本理论对应任何产品、发布版本或商业合规能力。

## 11. Required Invariants（强制不变量）

```text
selection != authorization
evidence != permission
recommendation != command
score != trust
performance_only != survival
survival_evidence != governance_decision
```

## 12. Governance Statement（治理声明）

本 ADR 是 Digital Biosphere Laboratory 的最高理论框架提案。  
它不变更任何实现权限，不授予运行时控制，不定义 API 或模式语法。  
后续实现、schema、adapter、实验脚本与评估报告必须引用并对齐本理论前提。

```text
DBL_DSD_THEORY_ADOPTED=true
SD_AS_SUBTHEORY_FIXED=true
TITMAS_RUNTIME_AUTHORITY_UNCHANGED=true
SAEE_RECOMMENDATION_ONLY=true
REGISTRY_ROLE=metadata_index
THEORY_ONLY=true
IMPLEMENTATION=false
SCHEMA=false
API=false
```
