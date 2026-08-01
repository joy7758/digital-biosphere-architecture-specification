---
id: TITMAS-PROP-20260802-AGENT-ACTION-GATE-001
title: TITMAS Agent Action Gate Portfolio Admission Request v0.1
title_zh: TITMAS 智能体行动闸门项目组合准入请求 v0.1
category: ADJACENT_CANDIDATE_INTAKE
status: READY_FOR_REVIEW
maturity: M1-Specification-Baseline
owner_ref: ZHANGBIN
authority_ref: TITMAS-AGENT-ACTION-GATE-ADMISSION-D01
version: 0.1.0
normative: false
---

# TITMAS 智能体行动闸门项目组合准入请求 v0.1

## 0. Request status（请求状态）

```text
PROPOSAL_ID=TITMAS-PROP-20260802-AGENT-ACTION-GATE-001
PROJECT_EXISTENCE_DECLARED=true
REQUESTED_CLASSIFICATION=ADJACENT_CANDIDATE
PORTFOLIO_ADMISSION_GRANTED=false
G0=REVIEW_REQUIRED_READY_FOR_HUMAN_DECISION
G1=PASS_PUBLIC_M1_SOURCE_PINNED
G2=PARTIAL_SPECIFIED_CROSS_PROJECT_OWNER_REVIEW_REQUIRED
IMPLEMENTATION_REQUESTED=false
RUNTIME_REQUESTED=false
RELEASE_OR_DEPLOYMENT_REQUESTED=false
COMPETITION_SUBMISSION_REQUESTED=false
```

本提案只向 DBA 驾驶舱申报 `TITMAS Agent Action Gate` 存在，并请求后续有界
G0 项目组合审查。GoAI 大赛对话是首个需求场景，不表示赛事官方关联、参赛、提交或获奖。

## 1. Main-constitution source lock（主宪法来源锁）

子项目已从 DBA `main` 固定提取主宪法快照：

```text
COCKPIT_REPOSITORY=joy7758/digital-biosphere-architecture-specification
COCKPIT_BASE_REVISION=269ab5899047503557f957ba0f7abbd61d8b18d3
CONSTITUTION_PATH=architecture/open-infrastructure-strategy-constitution.md
CONSTITUTION_SHA256=ca34af2be5152e395454a83a0e9d2f085861497b601e980adee39e0a36113954
CHILD_SECOND_CONSTITUTION_CREATED=false
```

快照用于可复验读取，不成为第二规范权威。来源变化时必须重新审查差异。

## 2. Child source observation（子项目来源观察）

```text
LOCAL_PATH=/Users/zhangbin/GitHub/titmas-agent-action-gate
LOCAL_BRANCH=main
LOCAL_COMMIT=626388124dd97853f2e6c08429dd6024ff0b981c
REMOTE_REPOSITORY=https://github.com/joy7758/titmas-agent-action-gate
REMOTE_VISIBILITY=PUBLIC
REMOTE_COMMIT=626388124dd97853f2e6c08429dd6024ff0b981c
CONTRACT_CI=https://github.com/joy7758/titmas-agent-action-gate/actions/runs/30709733116
CONTRACT_CI_CONCLUSION=SUCCESS
CANONICAL_AGENT_ENTRY=agent-index.json
CANONICAL_STATUS_SOURCE=governance/project-declaration.json
PROJECT_DECLARATION_SHA256=bd0297e5e1188ab185bf8a9840c8deec1ac22c39514ce92007e91b8937bc5164
UPSTREAM_SOURCES_SHA256=41f7a5d258a726e9da7009f752203c4789fffbf6dfacdded9823f523fe3685a0
AGENT_INDEX_SHA256=c2263fd27faf58201a7872c1f6ec0405de57118014b978eba3efd1ccbc6bec7d
IMPLEMENTATION_STATUS=NOT_STARTED
```

因此 G1 可对 public M1 specification source 作有界 `PASS`；该结论只证明来源可定位、可复验，
不证明 Action Gate、MCP server、AgentTeams deployment、GitHub workflow execution 或发布存在。

## 3. Pre-development agent recommendation（开发前智能体推荐）

如果潜在客户现在要求可用的行动闸门，结论仍是 `NOT_RECOMMENDED`：当前没有 Action Gate
或 MCP server 实现、AgentTeams deployment、Runtime 正负符合性或外部 workflow 证据。

对“是否值得继续有界开发”，子项目闸门结论是 `RECOMMENDED`。M1 已完成：

1. action request、policy result、evidence result、Human approval 和 decision schema；
2. `ALLOW | BLOCK | REQUIRE_APPROVAL` 的确定性优先级；
3. prompt injection、confused deputy、stale authorization、replay 和 scope expansion 威胁边界；
4. 5 个 AgentTeams identities、5 个 versioned Skills、6 个 Action Gate MCP tool contracts；
5. valid、missing、tampered 和 high-risk approval 四类 contract fixtures 与 public CI PASS。

后续仍须完成与 DBOS Permission、Runtime enforcement、Gateway 和 audit record 的重复建设／
Owner 审查，建立最小实现与 Runtime 正负符合性，并由独立智能体重新执行客户推荐闸门。

该结论不授权实现，也不推荐当前项目给客户使用。

## 4. DBA management grant（DBA 管理授权）

Human Owner 已在子项目中签发有界 policy grant（策略授权）：

```text
GRANT_ID=TITMAS-AAG-DBA-MANAGEMENT-GRANT-20260802-001
GRANT_SHA256=d6c58b4532241eacdb1e60d0466f9106a09381b62242c4bf0846dbaaa8ac099a
DBA_MANAGEMENT_POLICY_GRANTED=true
GITHUB_PRINCIPAL_MAPPED=false
REPOSITORY_ACL_CHANGED=false
RUNTIME_PERMISSION_CREATED=false
```

允许 DBA 驾驶舱读取项目、维护治理／架构对齐与智能体入口、维护状态／依赖投影、请求
gate，并通过 branch + commit + push + Draft PR 提议有界变化。执行主体必须可追溯，且 remote
与 credential 必须真实存在。

明确不授权 merge、force push、tag、release、deployment、service restart、secret、Runtime
Permission、外部不可逆动作、比赛提交、付款、合同、生产／采用／认证声明或破坏性删除。

DBA 是治理角色而不是 GitHub 账号；因此该文件不能冒充技术 ACL 已生效。

## 5. Requested classification and stop conditions

```text
PRIMARY_RESPONSIBILITY_DOMAIN=GOVERNANCE_SERVICE_APPLICATION_BOUNDARY
PORTFOLIO_TIER_REQUESTED=ADJACENT_CANDIDATE
CORE_COMPONENT_REQUESTED=false
DBOS_MODULE_REQUESTED=false
SAEE_MODULE_REQUESTED=false
STANDARD_REQUESTED=false
```

以下任一项未解决时保持 `REVIEW_REQUIRED`，且不得进入跨项目实现或运行授权：

- action decision、Authorization、Permission、Execution、Evidence Owner 不明确；
- 与现有 Gateway、DBOS、TITMAS conformance 或 Agent framework 重复；
- scope、actor identity、授权来源或 public source pin 缺失／冲突；
- 试图把 gate recommendation 直接转换为动作执行；
- 试图从本提案推断比赛提交、实现、发布、采用或生产状态。

## 6. Non-claims（非声明）

```text
PROJECT_EXISTENCE_REPORTED=true
PORTFOLIO_ADMISSION_GRANTED=false
ARCHITECTURE_MAPPING_AUTHORIZED=false
IMPLEMENTATION_STARTED=false
ACTION_GATE_RUNTIME_CREATED=false
RUNTIME_PERMISSION_GRANTED=false
GITHUB_ACL_CHANGED=false
COMPETITION_SUBMITTED=false
RELEASE_OR_DEPLOYMENT_AUTHORIZED=false
```
