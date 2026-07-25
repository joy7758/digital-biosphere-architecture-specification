---
document_id: DBA-TITMAS-CONTRIBUTOR-MATURITY-MODEL-0.1
title: TITMAS Contributor Maturity Model v0.1
title_zh: TITMAS 贡献者成熟度模型 v0.1
version: 0.1.0
status: contributor-maturity-model-candidate-no-levels-assigned
maturity: Development
maturity_scope: entire-document
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-contributor-development-model-candidate
architecture_domain: TITMAS
document_maturity: Development
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
assigned_contributor_levels: 0
maintainer_assigned: false
authority_effect: none
---

# TITMAS Contributor Maturity Model v0.1

## 1. Principle（原则）

本模型描述未来贡献者可以证明的理解、贡献和维护能力，不分配账号权限、组织成员身份、
Reviewer/Maintainer role、Architecture Authority 或 Release Authority。

```text
CONTRIBUTOR_MATURITY_NE_ROLE_ASSIGNMENT=true
CONTRIBUTOR_MATURITY_NE_AUTHORITY=true
CONTRIBUTOR_MATURITY_NE_PERMISSION=true
CURRENT_ASSIGNED_LEVELS=0
```

Level 必须基于可核验的历史和明确人工决定，不能由贡献数量、模型评分、Star、组织身份或
自我声明自动升级。

## 2. Maturity Levels（成熟度层级）

### Level 0 — Explorer

能够：

- 找到 DBA cockpit、TITMAS 入口和 current truth；
- 用自己的话解释 DBA、TITMAS、DBOS、SAEE 与 Agent Framework 的区别；
- 区分 Specification、Implementation、Conformance、Adoption 和 Release。

不拥有：贡献接受、review、role、Authority 或 Permission。

### Level 1 — Contributor

能够：

- 使用 Proposal Template 提交有来源、有 scope、有 non-goals 的贡献；
- 披露 human/agent assistance；
- 保留 negative、unknown、unsupported 和 failure；
- 响应 review 并维护自己的贡献。

最低证据：至少一项被接受的有界贡献，以及对边界的正确解释。

不拥有：自动 Reviewer、merge、Decision 或社区成员身份。

### Level 2 — Integrator

能够：

- 设计 exact-version mapping、adapter contract、handoff 或 compatibility crosswalk；
- 识别 canonical Owner，避免第二事实/规范权威；
- 声明 supported、partial、unsupported 和 unknown；
- 设计 no-writeback、failure-retention 和 migration controls。

最低证据：多个被审查的 integration contribution 和跨域 Owner review。

不拥有：连接系统的 write access、Runtime、adoption 或 external-standard authority。

### Level 3 — Specification Contributor

能够：

- 编写规范性术语、对象、状态、版本、兼容和错误语义；
- 区分 normative/non-normative text；
- 提供安全、隐私、breaking change 与 conformance plan；
- 处理异议、替代方案和实现反馈。

最低证据：持续的高质量规范贡献、review history 和无 Authority elevation 记录。

不拥有：Specification Authority、Stable promotion 或 Architecture Decision。

### Level 4 — Reviewer

能够：

- 在明确 scope 内执行 Proposal、Architecture、Security、Compatibility 或 Breaking Review；
- 识别来源、重复、边界、实现反馈与未关闭风险；
- 给出有理由的 PASS/REVISE/REJECT/BLOCKED 结果；
- 回避 Conflict of Interest 并维护 review provenance。

最低证据：多项独立、高质量 review，明确候选 scope 和人工指派 Decision。

只有角色被另行指派后，Level 4 才能形成正式 Reviewer record。成熟度本身不授予 approve
或 merge 权。

### Level 5 — Maintainer

能够：

- 维护 exact specification/workstream scope、版本、errata、兼容与 deprecation；
- 路由 review、处理安全与 breaking change、维持响应和继任；
- 正确区分 community input、Domain Owner input、Architecture Decision 与 Release；
- 在无法维护时主动降级、移交或归档。

最低证据：长期贡献和 Reviewer 经验、真实工作、Charter、term、replacement/removal、
Code of Conduct、Security path、明确接受及 DBA Decision。

Level 5 不自动拥有 DBA Architecture Authority、DBOS Operational Authority、SAEE
Evolution Authority、Human Release Authority 或平台管理员权限。

## 3. Evaluation Dimensions（评估维度）

每次成熟度审查至少评估：

| Dimension | Evidence |
|---|---|
| Boundary understanding | 对 DBA/TITMAS/DBOS/SAEE、Evidence/Truth、Validation/Authorization 的正确解释 |
| Contribution quality | 来源、scope、维护性、negative/unknown/failure 处理 |
| Review quality | 可复核 findings、异议处理、independence、COI |
| Compatibility discipline | version、migration、deprecation、breaking classification |
| Security and privacy | threat、data minimization、secret/PII、disclosure routing |
| Human/Agent accountability | AI 披露、人工理解、验证和责任 |
| Sustained maintenance | response、errata、handoff、archive 和 replacement |

## 4. Promotion, Review and Regression（升级、复核与回退）

升级需要：

1. candidate self-assessment；
2. 可核验 contribution/review references；
3. scope-specific assessment；
4. Conflict of Interest 检查；
5. 明确 Human Decision；
6. role/permission/platform action 另行处理。

成熟度可因 inactivity、重复低质量贡献、安全/行为问题、边界误用或无法维护而降级。降级
保留历史和 attribution，不删除既有贡献。

## 5. Crosswalk to Candidate Roles（与候选角色交叉表）

| Maturity Level | Closest candidate role | Automatic role assignment |
|---|---|---|
| Level 0 Explorer | Participant | `false` |
| Level 1 Contributor | Contributor | `false` |
| Level 2 Integrator | scoped technical contributor | `false` |
| Level 3 Specification Contributor | Reviewer Candidate input | `false` |
| Level 4 Reviewer | Reviewer Candidate | `false` |
| Level 5 Maintainer | Maintainer Candidate | `false` |

本表不替代
[TITMAS Contributor Role Model](titmas-contributor-role-model-v0.1.md)。

## 6. Current Result（当前结果）

```text
TITMAS_CONTRIBUTOR_MATURITY_MODEL_DEFINED=true
TITMAS_CONTRIBUTOR_LEVELS_ASSIGNED=0
TITMAS_REVIEWER_ASSIGNED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_ROLE_ASSIGNMENT_AUTHORIZED=false
TITMAS_COMMUNITY_ESTABLISHED=false
```
