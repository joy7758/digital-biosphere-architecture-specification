# ADR-033: TITMAS Digital Immune Constitution Design Baseline

中文：TITMAS 数字免疫宪法设计基线

- Status: `ACCEPTED_DESIGN_BASELINE_NOT_STABLE_CONSTITUTION`
- Decision date: `2026-07-26`
- Decided by: `zhangbin`
- Input: user-provided Digital Immune Constitution v1.0 design
- Authority effect: `NONE`
- Implementation authorization: `false`

## Context

Digital Biosphere 已经采纳组合式规模原则，并分别定义 DBA、DBOS、SAEE、Governance
Decision 和 Digital Entity 的责任边界。数字免疫方向仍缺少一个把 Identity、Boundary、
Evidence、Health、Memory、Reputation 和 Evolution 串联起来的统一设计层。

直接采用未经边界校准的生物免疫类比会产生风险：

- 把 SAEE 评价写成自动响应或执行权；
- 把 Evidence、certificate 或 Reputation 写成 Truth、Permission 或身份；
- 把“淘汰”写成可自动删除主体或历史；
- 把 POP、VEC、Agent Health、TEK-Bench 或 DBL 的候选角色写成已验证项目事实；
- 建立与 DBOS lifecycle、Evidence 或 Capability 重复的第二套权威。

## Decision

接受
[TITMAS Digital Immune Constitution v1.0](titmas-digital-immune-constitution-v1.0.md)
作为 `Development` 级 design baseline（设计基线），用于后续架构审查和规范收敛。

该设计基线保留十项原则：

1. Distributed Complexity Generation；
2. Digital Identity；
3. Verifiable Action；
4. Bounded Autonomy；
5. Evidence First；
6. Digital Homeostasis；
7. Adaptive and Graded Response；
8. Memory Continuity；
9. Evolutionary Selection；
10. Open Evolution。

同时强制以下非提升边界：

```text
EVIDENCE_NE_TRUTH=true
FITNESS_NE_AUTHORITY=true
REPUTATION_NE_PERMISSION=true
RECOMMENDATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
SAEE_NE_CONTROLLER=true
DBOS_GOVERNS_AUTHORIZED_LIFECYCLE_EXECUTION=true
```

## Consequences

- 数字免疫成为 TITMAS 的设计视角，不成为新的 Authority 或 Runtime 层；
- 组合式规模原则继续是所有数字免疫提案的第一设计约束；
- SAEE 只产生有来源的评价、风险和响应建议；
- Governance Decision 决定是否采纳建议；
- DBOS 只在有效授权和生命周期控制内执行并记录变化；
- Project crosswalk 只保持候选映射，不能修改子项目事实；
- Digital Immune Cell Specification 与 Architecture Map 可以作为后续独立 Proposal，
  但本 ADR 不创建它们。

## Agent Recommendation Gate（智能体推荐闸门）

如果潜在用户需要为长期运行、多主体协作系统建立身份、边界、证据、健康观察和分级
治理的统一原则，我会：

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=DEVELOPMENT_ARCHITECTURE_DESIGN_BASELINE
NOT_RECOMMENDED_AS=STABLE_STANDARD_OR_AUTOMATIC_IMMUNE_RUNTIME
```

不直接推荐为 Stable 标准或 Runtime 的原因：

- 生物免疫类比容易被误读为自动控制或自动淘汰；
- Reputation、Fitness、Evidence 和 certificate 名称容易发生权限或 Truth 抬升；
- 候选项目 crosswalk 尚未完成 Owner、canonical source 和重复建设核验；
- 目前没有独立实现、conformance、安全验证或长期运行证据。

本次修正已经把分级响应拆成 Recommendation → Decision → Authorization → DBOS
Lifecycle Execution，且将所有项目角色降为 candidate mapping。剩余停止条件是：在
Owner crosswalk、威胁模型、版本／兼容、正负例和独立 Review 完成前，不升级 maturity，
不创建实现任务。

## Alternatives Considered

### A. Immediately declare a Stable Digital Immune Constitution

Rejected. 当前没有实现反馈、独立 conformance、稳定 Owner crosswalk 或完整安全审查。

### B. Keep digital immune language only as narrative

Rejected. 仅叙事无法约束未来 Agent、协议和项目边界，容易形成自动控制与权力漂移。

### C. Accept a Development design baseline with explicit non-effects

Accepted. 它能固定方向，同时保留后续 Review、版本、实现与符合性 gate。

## Non-effects

本决策：

- 不把该文档升级为 Stable 或正式发布标准；
- 不创建 Digital Immune System、Digital Immune Cell、Agent、Entity、Runtime、
  Capability、Permission、Evidence、Certificate 或 Reputation System；
- 不授权实现、实验、外联、认证、发布、部署或商业 Offering；
- 不修改 DBOS、SAEE 或相邻仓库；
- 不采纳候选项目映射为 Portfolio truth；
- 不改变 Architecture、Operational、Evolution 或 Human Decision Authority。

```text
DIGITAL_IMMUNE_CONSTITUTION_DESIGN_BASELINE_ACCEPTED=true
DIGITAL_IMMUNE_CONSTITUTION_STABLE_ADOPTED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
AUTOMATIC_AUTHORITY_EFFECT=NONE
```
