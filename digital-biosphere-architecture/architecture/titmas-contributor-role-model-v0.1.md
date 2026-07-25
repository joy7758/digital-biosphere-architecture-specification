---
document_id: DBA-TITMAS-CONTRIBUTOR-ROLE-MODEL-0.1
title: TITMAS Contributor Role Model v0.1
title_zh: TITMAS 贡献者角色模型 v0.1
status: candidate-no-roles-assigned
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-community-role-policy
architecture_domain: TITMAS
community_state: CONTRIBUTOR_ENTRY_PREPARED
role_assignment_effect: none
maintainer_assigned: false
reviewer_assigned: false
triager_assigned: false
agent_membership_created: false
authority_effect: none
---

# TITMAS Contributor Role Model v0.1

## 1. Purpose（目的）

本模型重度参考 OpenTelemetry 将 Member、Triager、Approver、Maintainer 的责任、进入条件和
代码库范围分开的机制，但不复制其 CNCF/GitHub 组织地位、委员会权力或现有角色名称所
代表的权限。

TITMAS 当前没有正式社区和角色。本模型只定义未来候选角色，防止“贡献一次就成为
Maintainer”“智能体输出就取得投票权”或“社区角色覆盖 DBA/DBOS/SAEE Authority”。

## 2. Candidate Role Ladder（候选角色阶梯）

| candidate role | 责任 | 最低进入证据 | 明确不拥有 |
|---|---|---|---|
| Participant | 提问、报告问题、参与讨论、提供使用反馈 | 遵守贡献和行为规范 | Assignment、merge、Decision、Authority |
| Contributor | 提交有来源、可验证且边界明确的文档、Proposal、mapping 或 test design | 至少一项被接受贡献；能解释项目边界 | 自动组织成员身份、approve、merge |
| Triager Candidate | 帮助分类问题、识别重复、补齐来源和路由 Owner | 持续贡献；有明确 scope；经记录提名和审查 | 改写优先级、关闭 Authority 问题 |
| Reviewer Candidate | 对限定表面提供技术、文档或领域审查 | 多项高质量 review；熟悉兼容、失败和非目标 | 最终采纳、跨域覆盖、implementation authorization |
| Maintainer Candidate | 维护一个已激活 Workstream 的方向、质量、响应和版本计划 | 真实持续工作；Charter；Reviewer 经验；明确任期和替代；DBA Decision | DBA Architecture Authority、DBOS operational authority、SAEE evolution authority |
| Emeritus Candidate | 保留历史贡献与知识连续性 | 曾任正式角色且退出记录完整 | 当前操作、审查、合并或决策权 |

这些名称后缀为 `Candidate` 的角色不能写入 GitHub 权限、CODEOWNERS、组织成员、SIG 或
发布系统，除非有后续独立决定和外部动作授权。

## 3. Role Scope（角色作用域）

未来角色必须绑定具体 scope，例如：

```text
role_scope=SPECIFICATION|MAPPING|CONFORMANCE|DOCUMENTATION|SECURITY_PRIVACY
workstream_reference=
effective_at=
review_at=
expires_at=
assigned_by_decision_ref=
```

一个 scope 的 Reviewer 或 Maintainer 不自动成为另一个 scope 的负责人。社区角色也不
改变以下权力：

```text
DBA_ARCHITECTURE_AUTHORITY_UNCHANGED=true
DBOS_OPERATIONAL_AUTHORITY_UNCHANGED=true
SAEE_EVOLUTION_AUTHORITY_UNCHANGED=true
HUMAN_RELEASE_AUTHORITY_UNCHANGED=true
```

## 4. Agent Participation（智能体参与）

受治理智能体可以：

- 发现和解释项目；
- 生成有来源的 Proposal candidate；
- 检查链接、结构、Schema、术语和边界；
- 生成或审查 test case candidate；
- 汇总 review input 和已知冲突。

受治理智能体不能：

- 成为法律意义或平台账号意义的 member；
- 自我提名、担保或批准角色；
- 作为唯一 Reviewer 采纳重大架构变化；
- 生成 Permission、Authority、Release、Adoption 或 scientific truth；
- 隐藏模型、工具、上下文、来源或人工责任方。

智能体贡献使用 `GOVERNED_AGENT`，人机共同完成使用
`HUMAN_WITH_AGENT_ASSISTANCE`。两者都必须有 `human_accountability_ref`。

## 5. Assignment and Removal（指派与撤回）

未来角色指派至少要求：

1. 可核验贡献与 review history；
2. 候选人明确接受；
3. scope、责任、任期、复核时间和冲突披露；
4. 指派者及 decision reference；
5. 公开可追溯记录；
6. inactivity、Conflict of Interest、行为或安全问题的暂停和撤回路径。

角色撤回保留历史，不删除原贡献，也不将先前 review 自动变为无效。是否重审由受影响
规范的 Owner 和 Architecture Decision 决定。

## 6. OpenTelemetry Reference Boundary（参考边界）

参考来源：

- OpenTelemetry community membership policy:
  `open-telemetry/community@d3d7cb3c1bc1104d8df7cf26dba9bf86cf354f26`；
- OpenTelemetry New Contributor Guide:
  同一 commit 下的 `guides/contributor/README.md`。

该参考只证明 TITMAS 采用“角色有责任、进入条件、scope 和可追溯指派”的设计思路，
不证明 TITMAS 已属于 OpenTelemetry/CNCF、已存在组织角色，或得到任何外部认可。

## 7. Current Status（当前状态）

```text
TITMAS_CONTRIBUTOR_ROLE_MODEL_DEFINED=true
TITMAS_PARTICIPANT_ASSIGNED=false
TITMAS_CONTRIBUTOR_ASSIGNED=false
TITMAS_TRIAGER_ASSIGNED=false
TITMAS_REVIEWER_ASSIGNED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_AGENT_MEMBER_CREATED=false
TITMAS_ROLE_ASSIGNMENT_AUTHORIZED=false
```
