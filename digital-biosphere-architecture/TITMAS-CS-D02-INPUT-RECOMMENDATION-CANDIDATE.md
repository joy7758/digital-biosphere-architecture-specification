---
document_id: DBA-TITMAS-CS-D02-INPUT-RECOMMENDATION-CANDIDATE-0.1
title: TITMAS CS-D02 Input Recommendation Candidate v0.1
title_zh: TITMAS CS-D02 输入推荐候选 v0.1
version: 0.1.0
status: recommendation-candidate-prepared-human-input-and-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Recommended bounded input configuration only; no role acceptance, reviewer appointment, method approval, external access, outreach, data processing, execution, gate pass, commercial validation, certification, or release claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-input-recommendation-candidate
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
prepared_at: 2026-07-25
---

# TITMAS CS-D02 Input Recommendation Candidate v0.1

## 0. Recommendation（推荐结论）

推荐采用：

> **Bounded Two-Stream Problem Validation（有界双流问题验证）**

```text
Stream A: Public First-party Problem Report Review
          公开一手问题报告审查

Stream B: Governed Agent Recommendation Review
          受治理智能体推荐审查
```

两条流的证明力严格不同：

```text
PUBLIC_FIRST_PARTY_REPORT
  -> may become a problem record only after method/source/privacy/claim review

GOVERNED_AGENT_ADVISORY
  -> recommendation and discoverability input only
  -> never counts as customer, organization, market adoption, or CS-G0 context by itself
```

当前状态：

```text
CS_D02_INPUT_RECOMMENDATION_PREPARED=true
RECOMMENDATION_RESULT=CONDITIONALLY_RECOMMENDED
HUMAN_INPUT_ACCEPTED=false
FORMAL_REVIEW_COMPLETE=false
CS_D02_DECISION_READY=false
EXTERNAL_ACTION_AUTHORIZED=false
```

机器入口：

- [machine candidate](TITMAS-CS-D02-INPUT-RECOMMENDATION-CANDIDATE.v0.1.json)；
- [candidate Schema](architecture/schemas/titmas-cs-d02-input-recommendation-candidate.schema.v0.1.json)。

## 1. Why This Candidate（为什么推荐该候选）

它同时回应两项现实：

1. TITMAS 的核心使用者和推荐者包括智能体，因此需要测量 Agent discovery、
   comprehension、recommendation 和 reuse；
2. 智能体评价不能冒充实际承担责任的客户、组织或人类决策者，因此 CS-G0 仍需可归因的
   真实一手问题来源和独立 Review。

不推荐立即进行直接访谈，原因是参与者来源、联络授权、consent 和 Reviewer 尚未就绪。
不推荐只调用模型 API，原因是模型意见无法证明市场采用或真实组织问题。

## 2. Recommended Role Configuration（推荐角色配置）

| Role | Recommendation | Current effect |
|---|---|---|
| Human Decision Owner | 保持 `zhangbin` | existing only |
| Problem Validation Owner | 推荐 `zhangbin` 接受有界职责 | candidate; not accepted |
| Privacy/Data Steward | 推荐 `zhangbin` 接受有界职责并披露角色重合 | candidate; not accepted |
| Method Reviewer | 至少一名非 `zhangbin` 的独立 human reviewer | unassigned |
| Security Reviewer | 至少一名 human reviewer；可与 Claim Reviewer 合并但须披露 | unassigned |
| Claim Reviewer | 至少一名非记录创建者的 human reviewer | unassigned |

最小独立性：

```text
INDEPENDENT_HUMAN_REVIEWERS_MIN=2
METHOD_REVIEWER_NE_PROBLEM_RECORD_CREATOR
CLAIM_REVIEWER_NE_PROBLEM_RECORD_CREATOR
SECURITY_AND_CLAIM_ROLE_COMBINATION_ALLOWED_ONLY_WITH_DISCLOSED_CONFLICT=true
AGENT_REVIEWER_COUNTS_TOWARD_HUMAN_MINIMUM=false
```

该建议不自动接受角色。角色接受必须由相应自然人留下精确 reference、timestamp、scope 和
conflict disclosure。

## 3. Stream A Candidate（公开一手问题报告流）

### Source boundary

只允许未来经决定批准后审查：

- 官方项目或组织公开维护的 Issue、Incident、Postmortem、Security Advisory；
- 原始发布者公开发布、可以归因、带稳定 URL 和日期的材料；
- 明确描述 Agent execution accountability、evidence、verification、长期可靠性或治理问题的
  一手材料。

拒绝：

- 搜索结果摘要或第三方转述；
- 无法确认原始发布者的内容；
- 登录后、私有、付费墙或访问控制材料；
- 泄漏数据、凭据、个人敏感信息或受监管数据；
- 将功能需求自动解释为购买意愿。

### Record fields

仅保留：

- stable public source reference；
- source owner / project；
- published/observed date；
- public-safe problem paraphrase；
- affected responsibility context；
- priority rationale；
- source and method review result；
- withdrawal/removal status。

不复制完整正文，不保存附件，不把公开内容自动变成 Truth、Evidence 或 testimonial。

### Counting

同一组织的多个 Issue 默认只算一个独立 context，除非 Method Reviewer 证明责任域独立。
`continue_review_interest` 只能来自原始发布者明确的后续意向，不能从 issue 仍开放推断。

## 4. Stream B Candidate（智能体推荐流）

未来只有在 API/network 和预算被单独授权后，才允许执行：

- 给不同模型相同、版本化的潜在客户问题；
- 记录模型标识、provider、prompt digest、时间、输出 reference 和失败；
- 评价是否发现 TITMAS、是否理解边界、是否推荐、为什么不推荐；
- 把不推荐原因分解为文档、接口、可信度、生态和证据缺口。

限制：

```text
AGENT_ADVISORY_NE_CUSTOMER_INTERVIEW
AGENT_RECOMMENDATION_NE_MARKET_ADOPTION
MODEL_COUNT_NE_ORGANIZATION_COUNT
API_OUTPUT_NE_CS_G0_PASS
AGENT_CANNOT_ACCEPT_REVIEW_ROLE_OR_HUMAN_AUTHORITY
```

## 5. Recommended Data Controls（推荐数据控制）

候选值：

| Input | Recommended candidate |
|---|---|
| storage class | `PRIVATE_ACCESS_CONTROLLED_NON_GIT_VALIDATION_STORE` |
| access | Owner、Data Steward、assigned Reviewers only |
| record cap | `20` |
| working retention | `90 days after run end` |
| public output | aggregate counts + public-safe paraphrase |
| raw transcript | prohibited |
| direct identifier | prohibited |
| secrets/credentials | prohibited |
| regulated data | prohibited |
| source removal | mark withdrawn; remove copied paraphrase if required |
| deletion proof | retain content-free tombstone only |
| incident route | confidential human-owned route required before execution |

`PRIVATE_ACCESS_CONTROLLED_NON_GIT_VALIDATION_STORE` 是架构类别，不是已选中的实际路径、
service 或 implementation。必须在未来决定中绑定 exact storage reference 和访问证据。

## 6. Recommended Execution Envelope（推荐执行包络）

```text
MAX_PROBLEM_RECORDS=20
MAX_AGENT_ADVISORY_SESSIONS=12
TIMEBOX_DAYS=14
BUDGET_CURRENCY=CNY
BUDGET_CAP=0_FOR_PUBLIC_REPORT_REVIEW
AGENT_API_BUDGET=SEPARATE_DECISION_REQUIRED
DIRECT_PARTICIPANT_CONTACT=false
NETWORK_ALLOWLIST=EXACT_FIRST_PARTY_PUBLIC_DOMAINS_REQUIRED
```

`CNY 0` 只适用于不购买服务的公开报告审查候选，不授权网络访问，也不自动覆盖未来 API
费用。Agent API 流必须另有 exact provider、model、data handling 和 budget 输入。

## 7. Human Input Token Template（人工输入模板）

以下只是未来模板，当前不得解释为已提交决定：

```text
decided_by_ref=zhangbin
CS-D02-INPUTS=ACCEPT_BOUNDED_TWO_STREAM_RECOMMENDATION_FOR_REVIEW

problem_validation_owner_ref=zhangbin
problem_validation_owner_acceptance_ref=<exact-reference>
privacy_data_steward_ref=zhangbin
privacy_data_steward_acceptance_ref=<exact-reference>
role_overlap_conflict_disclosure_ref=<exact-reference>

method_reviewer_ref=<independent-human-reference>
method_reviewer_acceptance_ref=<exact-reference>
security_reviewer_ref=<human-reference>
security_reviewer_acceptance_ref=<exact-reference>
claim_reviewer_ref=<independent-human-reference>
claim_reviewer_acceptance_ref=<exact-reference>

storage_reference=<exact-private-non-git-reference>
access_control_evidence=<exact-reference>
retention_days=90
withdrawal_path_reference=<exact-reference>
deletion_path_reference=<exact-reference>
incident_route_reference=<exact-confidential-reference>

max_problem_records=20
timebox_days=14
starts_at=<RFC3339>
expires_at=<RFC3339>
revocation_route_reference=<exact-reference>
stop_owner_ref=<human-reference>

public_first_party_review_authorized=<true-or-false>
agent_api_advisory_authorized=<true-or-false>
direct_participant_contact_authorized=false
```

缺少任一 `<...>` 时，不能形成 execution-ready 决定。

## 8. Required Reviews Before Decision（决定前审查）

- Method Review：source eligibility、counting、independence、priority 和拒绝规则；
- Security/Privacy Review：访问、最小化、retention、withdrawal、deletion、incident；
- Claim Review：不得声称 customer、market adoption、truth、certificate 或 production；
- Human Decision Review：只批准 exact stream、scope、budget、timebox 和 stop rules。

## 9. Current State（当前状态）

```text
CS_D02_INPUT_RECOMMENDATION_PREPARED=true
CS_D02_RECOMMENDED_METHOD=BOUNDED_TWO_STREAM_PROBLEM_VALIDATION
CS_D02_RECOMMENDATION_RESULT=CONDITIONALLY_RECOMMENDED

ROLE_ACCEPTANCES_RECORDED=0
INDEPENDENT_HUMAN_REVIEWERS_ASSIGNED=0
STORAGE_IMPLEMENTATION_SELECTED=false
FORMAL_REVIEW_COMPLETE=false
HUMAN_INPUT_ACCEPTED=false
CS_D02_DECISION_READY=false

EXTERNAL_OUTREACH_AUTHORIZED=false
PUBLIC_WEB_REVIEW_AUTHORIZED=false
AGENT_API_CALL_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
