---
document_id: DBA-TITMAS-VEAP-PROBLEM-VALIDATION-PREREQUISITE-PROFILE-0.1
title: VEAP Problem Validation Reviewer and Data Control Prerequisite Profile v0.1
title_zh: VEAP 问题验证 Reviewer 与数据控制前置条件画像 v0.1
version: 0.1.0
status: prerequisite-profile-defined-reviewers-and-store-unselected
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Prerequisite qualification and control profile only; no reviewer appointment, storage selection, implementation, data approval, execution, gate pass, commercial validation, certification, or release claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-prerequisite-profile
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
defined_at: 2026-07-25
---

# VEAP Problem Validation Reviewer and Data Control Prerequisite Profile v0.1

## 0. Purpose（目的）

本画像回答两个问题：

1. 什么样的自然人可以成为 CS-D02 的 Method、Security 或 Claim Reviewer？
2. 用于问题验证的私有存储必须满足哪些控制，才允许进入 CS-D02 人工决定？

```text
PREREQUISITE_PROFILE_DEFINED=true
REVIEWER_IDENTITIES_SELECTED=false
REVIEWER_ACCEPTANCES_RECORDED=0
STORE_BACKEND_SELECTED=false
STORE_IMPLEMENTED=false
DATA_HANDLING_APPROVED=false
CS_D02_DECISION_READY=false
```

机器入口：

- [profile record](veap-problem-validation-prerequisite-profile.v0.1.json)；
- [profile Schema](schemas/veap-problem-validation-prerequisite-profile.schema.v0.1.json)。

## 1. Reviewer Baseline（Reviewer 基线）

所有正式 Reviewer 必须：

- 是可识别并承担责任的自然人；
- 留下 acceptance timestamp、scope、identity reference 和 contact route reference；
- 披露与 `zhangbin`、TITMAS、待评记录创建者和来源组织的利益冲突；
- 明确自己审查的是 method/security/claim，不是批准 Runtime、产品、认证或发布；
- 能记录 `PASS_WITH_SCOPE`、`BLOCKED`、`REJECTED` 和 unknown；
- 保留负面、失败和异议，不以“帮助项目通过”为职责；
- 不依赖模型输出替代本人判断。

以下不能单独成为正式 Reviewer：

- AI Agent 或模型；
- 匿名、无法追责的账号；
- 该条问题记录的创建者；
- 仅提供商业、宣传或销售意见的人；
- 未披露利益冲突的人。

## 2. Method Reviewer（方法 Reviewer）

最低资格：

- 理解 sampling、source selection、independence、double counting 和 confirmation bias；
- 能检查 `5/3/3/2` 阈值是否被正确解释；
- 能区分 first-party report、third-party summary、agent advisory 和 customer evidence；
- 能复核 priority、continue-review-interest 与 rejection reasons；
- 与被审问题记录的创建者不同。

Method Reviewer 不得：

- 把公开 Issue 自动当成客户验证；
- 把同一组织多个条目自动当成多个 context；
- 把 Issue 未关闭推断为继续合作意向；
- 把智能体建议计入独立 human/organization 门槛。

## 3. Security Reviewer（安全 Reviewer）

最低资格：

- 能审查 storage、access、encryption、backup、deletion、incident 和 credential boundary；
- 能识别 PII、secret、regulated material、unsafe attachment 和 external fetch 风险；
- 能确认禁止项默认拒绝；
- 能定义 incident stop、containment、notification 和 recovery reference。

Security Reviewer 不得把：

- “公开可见”解释为“可以无限复制或永久保存”；
- storage category 解释为已部署 backend；
- encryption claim 解释为访问控制或合规证明；
- audit log 解释为 Evidence Truth。

## 4. Claim Reviewer（主张 Reviewer）

最低资格：

- 能区分 problem record、customer evidence、adoption、conformance、certification 和 Truth；
- 能检查公开表述的来源、限定词、时间和范围；
- 能拒绝 `industry standard`、`customer proven`、`certified`、`production proven` 等无证据表述；
- 与被审问题记录的创建者不同。

Claim Reviewer 不得把：

- agent recommendation 当成客户采用；
- source count 当成组织 count；
- validation threshold 当成市场规模；
- Gate PASS 当成产品或商业服务可用。

## 5. Role Separation（角色分离）

推荐最低配置：

```text
INDEPENDENT_HUMAN_REVIEWERS_MIN=2
METHOD_REVIEWER_DISTINCT_FROM_RECORD_CREATOR=true
CLAIM_REVIEWER_DISTINCT_FROM_RECORD_CREATOR=true
SECURITY_AND_CLAIM_COMBINATION_ALLOWED=true
COMBINATION_REQUIRES_CONFLICT_DISCLOSURE_AND_SCOPE_RECORD=true
AGENT_COUNTS_TOWARD_HUMAN_MINIMUM=false
```

Problem Validation Owner 与 Privacy/Data Steward 可由同一候选人担任，但必须披露角色重合，
且不能替代独立 Method/Claim Review。

## 6. Reviewer Acceptance Record（Reviewer 接受记录）

未来每个正式 Reviewer 记录必须包含：

- `reviewer_ref`；
- `role_id`；
- `accepted_at`；
- `scope`；
- `competence_basis_reference`；
- `independence_basis_reference`；
- `conflict_disclosure_reference`；
- `confidential_contact_route_reference`；
- `acceptance_reference`；
- `may_close_gate=false`；
- `creates_operational_authority=false`。

资格画像符合不等于 Reviewer 已接受。

## 7. Private Validation Store Requirements（私有验证存储要求）

候选类别：

> `PRIVATE_ACCESS_CONTROLLED_NON_GIT_VALIDATION_STORE`

必须满足：

### Location and isolation

- 不位于公开 Git 仓库；
- exact backend/path/service reference 可解析；
- 与 Runtime、DBOS canonical Evidence 和公开网站隔离；
- 只用于 `VEAP_PROBLEM_VALIDATION_ONLY`。

### Access

- 默认拒绝；
- 仅 Problem Validation Owner、Data Steward、已接受 Reviewer；
- 每个主体有独立 identity reference；
- 访问变化和失败保留；
- 不使用共享凭据。

### Content

- 只保存结构化字段和 public-safe paraphrase；
- 默认不保存 raw transcript、附件、直接标识符、secret 或 regulated data；
- public source 仅保存稳定引用和必要最小摘录；
- source 不再可用或被撤回时进入 `WITHDRAWN`。

### Integrity and history

- append-only activity history 或等价不可静默覆盖机制；
- 修改使用 supersession，不覆盖原记录；
- 失败、拒绝和 unknown 保留；
- hash/signature 只能证明内容一致性，不能创建 Truth。

### Retention and deletion

- working retention candidate 为 90 天；
- run end、withdrawal、expiry 和 incident 均触发 disposition review；
- 删除后只允许保留不含被删内容的 tombstone；
- legal hold 默认为 false，除非另有明确依据；
- deletion path 必须能够被测试并留下结果 reference。

### Incident

- 执行前必须有 human-owned confidential route；
- secret、PII、regulated data、unauthorized access、source-use challenge 均触发停止；
- containment、notification、deletion/revocation 和 restart 需独立记录；
- incident 未关闭时不得继续数据收集。

## 8. Store Readiness Evidence（存储就绪证据）

进入 CS-D02 决定前至少需要：

- exact storage reference；
- Owner 和 Data Steward；
- access-control policy reference；
- encryption-at-rest/in-transit applicability record；
- backup/restore or explicit no-backup decision；
- retention policy；
- withdrawal/deletion procedure；
- incident route；
- prohibited-data negative test；
- unauthorized-access negative test；
- overwrite/supersession negative test；
- deletion/tombstone test；
- expiry/stop test。

本画像不创建这些结果。

## 9. Fail-closed Rules（失败关闭规则）

```text
IF REVIEWER_IS_AGENT_ONLY:
    FORMAL_REVIEWER_ASSIGNED=false

IF METHOD_OR_CLAIM_REVIEWER == RECORD_CREATOR:
    INDEPENDENCE_PROVEN=false

IF EXACT_STORE_REFERENCE_MISSING:
    STORE_READY=false

IF ANY_ACCESS_RETENTION_DELETION_INCIDENT_CONTROL_MISSING:
    DATA_HANDLING_APPROVED=false

IF PROFILE_SCHEMA_VALID:
    REVIEWER_ASSIGNED=false
    STORE_IMPLEMENTED=false
    CS_D02_DECISION_READY=false
```

## 10. Current State（当前状态）

```text
VEAP_PREREQUISITE_PROFILE_DEFINED=true
REVIEWER_QUALIFICATION_DEFINED=true
STORE_CONTROL_REQUIREMENTS_DEFINED=true

REVIEWER_IDENTITIES_SELECTED=false
REVIEWER_ACCEPTANCES_RECORDED=0
INDEPENDENT_HUMAN_REVIEWERS_ASSIGNED=0
EXACT_STORE_REFERENCE_AVAILABLE=false
STORE_IMPLEMENTED=false
STORE_CONTROL_TESTS_EXECUTED=0
DATA_HANDLING_APPROVED=false
CS_D02_DECISION_READY=false

EXTERNAL_ACTION_AUTHORIZED=false
PUBLIC_WEB_REVIEW_AUTHORIZED=false
AGENT_API_CALL_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
