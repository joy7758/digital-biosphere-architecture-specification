---
adr_id: ADR-043
title: DBA and TITMAS constitutional coherence for unified entry and DCell modules
title_zh: DBA与TITMAS统一入口和DCell模块宪法一致性
status: proposed_draft_awaiting_human_review
decision_id: DBA-TITMAS-CONSTITUTION-COHERENT-UPGRADE-v0.1
decided_by_ref: NOT_DECIDED
proposed_at: 2026-08-13
implementation_authorized: false
merge_authorized: false
release_or_deployment_authorized: false
---

# ADR-043: DBA and TITMAS Constitutional Coherence

## Context

DBA 已有组合式规模、动态注意力、执行上下文连续性和商业私有基础设施边界；TITMAS 已有
四产品、Observer 入口、Agent-first 与私有核心边界。DCell 相关叙事尚缺父子宪法继承、
模块最小契约、权限交集、组合重新评价和产品非扩张的统一机器表达。

若直接把“统一入口”实现为一个全局 Gateway，或把 DCell 当作自由激活的 Skill，会与
ADR-032、DBOS/SAEE 边界、Capability/Permission 分离及 C-01 四产品冻结冲突。

## Proposed decision

1. 以版本化修正案扩展，不改写历史宪法和已接受 ADR；
2. 建立父级原则机器契约、TITMAS 子级机器契约和 DCell 模块治理 Profile；
3. 将统一入口定义为逻辑机器契约，不定义全局强制或物理单一 Gateway；
4. 将执法保留为各规范 Owner 接入点的分布式有界行为；
5. 将 DCell 定义为 skill-like selection + cell-grade governance；
6. 保留 Gate、Receipt、Audit、Health 四产品，Observer 与 DCell 均不增加产品数；
7. 在 Human Review 前保持所有新契约 `authority_effect=NONE`。

## Alternatives considered

### Directly edit the adopted constitutions

Rejected. 直接覆盖会破坏版本历史并模糊候选与已采纳事实。

### Build a global TITMAS controller

Rejected. 它会重复 Gateway、OPA/OPAL、Runtime 或 Agent framework 能力，并形成隐藏的
Authority aggregation。

### Treat DCell as a renamed skill

Rejected. 普通技能描述不足以表达 Permission intersection、Evidence、side effect、
lifecycle、composition accountability 和 change revalidation。

### Versioned parent-child contracts

Proposed. 该方案保持历史、所有权和产品边界，同时让 Agent 可以验证继承与冲突。

## Consequences if later accepted

- 新 TITMAS / DCell 提案必须先证明父级一致性与复用审计；
- 模块组合变化必须重新核验，不允许自动继承 PASS；
- 统一入口的实现仍需未来单独授权和真实环境验证；
- 外部项目只能作为兼容或采纳候选，不能因本 ADR 自动成为依赖。

## Current decision state

```text
ADR_043_STATUS=PROPOSED_DRAFT_AWAITING_HUMAN_REVIEW
HUMAN_DECISION_RECORDED=false
CONSTITUTION_AMENDMENT_ADOPTED=false
IMPLEMENTATION_AUTHORIZED=false
MERGE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
```
