---
document_id: DBA-TITMAS-REVIEW-MAINTENANCE-MODEL-0.1
title: TITMAS Review and Maintenance Model v0.1
title_zh: TITMAS 审查与维护模型 v0.1
version: 0.1.0
status: review-model-candidate-no-roles-assigned
maturity: Development
maturity_scope: entire-document
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-review-and-maintenance-policy-candidate
architecture_domain: TITMAS
document_maturity: Development
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
reviewer_assigned: false
maintainer_assigned: false
public_review_enabled: false
authority_effect: none
---

# TITMAS Review and Maintenance Model v0.1

## 1. Purpose（目的）

本模型定义未来 TITMAS 贡献需要哪些 review（审查）、review 产生什么结果、谁承担维护
责任，以及这些活动不能产生什么权力。当前没有被指派的 Reviewer、Maintainer、SIG 或
公共 review channel。

```text
REVIEW_MODEL_DEFINED=true
REVIEWER_ASSIGNED=false
MAINTAINER_ASSIGNED=false
PUBLIC_REVIEW_ENABLED=false
```

## 2. Review Types（审查类型）

| Review Type | Trigger | Required Inputs | Valid Outputs | Does Not Create |
|---|---|---|---|---|
| **Proposal Review** | 所有非纯编辑贡献 | problem、scope、non-goals、source、human accountability、duplicate check | `ACCEPT_FOR_DRAFT`、`REVISE`、`REJECT`、`BLOCKED` | Architecture Decision、role、implementation |
| **Architecture Review** | 对象、Owner、Authority、lifecycle、cross-project interface 变化 | proposal、ownership matrix、affected domains、negative authorities | `PASS_TO_DECISION`、`REVISE`、`REJECT`、`BLOCKED` | Human Decision、DBOS/SAEE write authority |
| **Security Review** | credential、PII、network、supply chain、code execution、evidence、high-risk capability | threat model、data flow、retention、failure、disclosure path | risk findings、required controls、`PASS_WITH_SCOPE`、`BLOCKED` | certification、production safety、permission |
| **Compatibility Review** | schema/field/status/version/deprecation/mapping 变化 | old/new contract、implementer impact、migration、unknown/unsupported | compatibility classification、migration duties、version recommendation | adoption、release、implementation success |
| **Breaking Change Review** | 任何可能改变现有实现或解释的 substantive change | exact affected versions、alternatives、impact、rollback/deprecation plan | `BREAKING_CONFIRMED`、`NON_BREAKING_CONFIRMED`、`UNKNOWN_BLOCKED` | 自动 major version、自动迁移或删除历史 |

任何 review 都必须记录：

```yaml
review_id:
review_type:
scope:
reviewer_ref:
reviewer_role_state: CANDIDATE|ASSIGNED
inputs: []
findings: []
unresolved_objections: []
result:
reviewed_at:
human_accountability_ref:
agent_assistance_ref:
authority_effect: none
```

## 3. Review Routing（审查路由）

- 涉及 DBA/TMAP 跨域规则：DBA Architecture Review；
- 涉及 DBOS canonical object 或 operational record：DBOS Domain Owner input；
- 涉及 SAEE Evaluation/Evolution contract：SAEE Domain Owner input；
- 涉及 evidence-layer package、receipt 或 profile：对应 canonical source Owner input；
- 涉及外部规范：精确版本来源与 mapping-only review；
- 涉及高风险数据或执行：Security Review；
- 涉及字段、状态或版本：Compatibility Review；
- 涉及稳定规范的 substantive change：Breaking Change Review + Human Architecture Decision。

Owner input、Review 和 Decision 是三个不同记录。

## 4. Future Role Model（未来角色模型）

### Contributor

负责提出有来源、边界明确、可维护的贡献，并响应 review。Contributor 不拥有 approve、
merge、Decision、Authority 或 Permission。

### Reviewer

在指定 scope 内检查技术、架构、Security、Compatibility 或文档质量。未来只有经明确
指派的 Reviewer 才能形成正式 review record；Reviewer 不自动获得 Maintainer 或
Architecture Authority。

### Maintainer Candidate

具有持续贡献和 review 证据、准备承担版本计划与维护责任的候选人。Candidate 不获得平台
权限、merge 权或决策权。

### Maintainer

未来在 exact scope、term、review date、replacement/removal path 和 Decision ref 下维护
artifact。Maintainer Review 仍不能覆盖 DBA Architecture Decision、DBOS Operational
Authority、SAEE Evolution Authority 或 Human Release Authority。

这些角色与
[TITMAS Contributor Role Model](titmas-contributor-role-model-v0.1.md) 一致；本文件不做
任何角色指派。

## 5. Maintenance Duties（维护职责）

未来已指派 Maintainer 的最低职责：

- 维护 canonical source、version、status、errata 和 known limitations；
- 及时路由 Proposal、Security、Compatibility 与 breaking change；
- 保留 rejected、failed、deprecated 和 superseded history；
- 明确 implementation feedback 与 specification decision 的差异；
- 监测外部 reference version drift，不自动跟随 `latest`；
- 按期复核 Owner、scope、activity、conflict of interest 与 replacement path；
- 在无法维护时标记 `Unmaintained` 或提出 archive/deprecation Decision。

## 6. Assignment and Removal Gate（指派与撤回闸门）

角色指派至少需要：

1. 真实、可核验的持续贡献与 review history；
2. candidate 明确接受责任；
3. exact scope、term、review date、backup 和 removal path；
4. Code of Conduct、Conflict of Interest 与 Security Disclosure 路径；
5. 公共贡献表面已获授权（若角色面向公共流程）；
6. 可追溯 Human Architecture Decision；
7. 平台权限另行执行，不由文档自动创建。

撤回保留历史和已有 review provenance，不静默删除失败或异议。

## 7. AI-assisted Review Boundary（AI 辅助审查边界）

智能体可以检查来源、术语、Schema、链接、测试覆盖、兼容风险和潜在冲突，但不能：

- 作为唯一 Reviewer 通过重大架构变化；
- 自己审查并批准自己生成的内容；
- 伪造人类 review、共识、采用或 Maintainer 活动；
- 将模型分数写成 Architecture Decision 或 Security certification。

## 8. Current Result（当前结果）

```text
TITMAS_REVIEW_MODEL_DEFINED=true
TITMAS_MAINTENANCE_DUTIES_DEFINED=true
TITMAS_REVIEWER_ASSIGNED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_ROLE_ASSIGNMENT_AUTHORIZED=false
TITMAS_PUBLIC_REVIEW_ENABLED=false
TITMAS_SIG_CREATED=false
TITMAS_AUTHORITY_CHANGED=false
```
