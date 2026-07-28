---
document_id: DBA-TITMAS-ARCHITECTURE-CHARTER-1.0
title: TITMAS Architecture Charter v1.0
title_zh: TITMAS 架构章程 v1.0
status: accepted-bounded-charter-for-launch-ready-candidate
maturity: Development
owner_ref: zhangbin
decision_reference: USER_GOAL_2026-07-28
supersedes: titmas-architecture-charter-v0.1.md
public_launch_authorized: false
community_established: false
---

# TITMAS Architecture Charter v1.0

## Identity

TITMAS 是面向多智能体系统的开放可信互操作基础设施。DBA 管理 TITMAS 如何建设；
TITMAS 为外部开发者和系统提供规范、Binding、Crosswalk、Conformance 和参考实现。

Digital Immune、Agent Health、Jules/Codex/Qoder 修复闭环、VEAP/VEC 应用和 SAEE
Enterprise 是解释层、Profile、使用场景或上层产品，不是 TITMAS 本体。

## Permanent boundaries

```text
TITMAS_NE_DBA=true
TITMAS_NE_PROJECT_MANAGEMENT_SYSTEM=true
TITMAS_NE_AGENT_RUNTIME=true
TITMAS_NE_EXECUTOR=true
TITMAS_NE_CERTIFICATION_AUTHORITY=true
TITMAS_NE_CANONICAL_TRUTH_STORE=true
TITMAS_NE_SAEE_CORE=true
TITMAS_NE_REPOSITORY_FIXER=true
DIGITAL_IMMUNE_MODEL_IS_EXPLANATORY_LAYER=true
APPLICATION_SCENARIO_NE_CORE_ARCHITECTURE=true
COMMUNITY_GOVERNANCE_NE_PRODUCT_RUNTIME=true
```

不得通过后续 Profile 或实现创建第二套 Evidence、Verification、Authority、Identity 或
Evaluation owner。

## Canonical developer surfaces

- `TITMAS/README.md`：唯一开发者入口；
- `TITMAS/community/`：贡献与治理流程；
- `TITMAS/specifications/`：规范生命周期、注册表和提案；
- `TITMAS/conformance/`：机器验证与正负例；
- `TITMAS/reference/`：非权威、合成、最小参考实现；
- `TITMAS/adapters/`：Adapter 契约入口。

规范、实现、符合性、采用和发布状态分别记录，不能互相推导。

## Authority and truth

```text
AUTHORITY_NE_OWNERSHIP=true
SPECIFICATION_NE_IMPLEMENTATION=true
REFERENCE_IMPLEMENTATION_NE_STANDARD=true
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_AUTHORIZATION=true
RECOMMENDATION_NE_DECISION=true
MAPPING_NE_ADOPTION=true
EXPERIMENTAL_NE_STABLE=true
```

Human Owner 决定公共贡献、角色、发布和重大外部动作。模型、Contributor、Reviewer 或
Conformance PASS 均不能替代 Human Decision。

## Change process

规范变化按 `Proposal → Review → Decision → Versioned update → Conformance` 推进。
重大变更必须声明来源、Owner、Authority、成熟度、安全与隐私、兼容性、失败语义和
No Semantic Elevation。

## TITMAS drift check

每个重大 TITMAS 任务的最终答复必须输出：

```text
TITMAS_DRIFT_CHECK

CORE_INTEROPERABILITY_OBJECTIVE_PRESERVED=true|false
NEW_CONTROL_AUTHORITY_CREATED=true|false
NEW_TRUTH_SOURCE_CREATED=true|false
DUPLICATE_EVIDENCE_OR_VERIFICATION_CREATED=true|false
RUNTIME_OR_EXECUTOR_CREATED=true|false
CURRENT_CAPABILITY_OVERCLAIMED=true|false
PUBLIC_LAUNCH_AUTHORIZED=true|false
COMMUNITY_ESTABLISHED=true|false
```

任一越权字段为 `true` 时，状态为 `STOP_AND_HUMAN_REVIEW_REQUIRED`；否则为
`PASS_WITH_RECORDED_LIMITATIONS`。本检查只报告，不自动阻断、删除、回滚或改变
Permission。

```text
TITMAS_V1_CHARTER_DEFINED=true
TITMAS_STANDARD_COMMUNITY_INFRASTRUCTURE_IN_PROGRESS=true
TITMAS_PUBLIC_LAUNCH_AUTHORIZED=false
TITMAS_COMMUNITY_ESTABLISHED=false
TITMAS_FOUNDATION_CREATED=false
TITMAS_CERTIFICATION_AUTHORIZED=false
TITMAS_RELEASE_AUTHORIZED=false
```
