---
document_id: DBA-TITMAS-CS-D02-INPUT-ASSIGNMENT-PACKET-0.1
title: TITMAS CS-D02 Input Assignment Packet v0.1
title_zh: TITMAS CS-D02 输入指派包 v0.1
version: 0.1.0
status: packet-defined-inputs-not-provided-not-decision-ready
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Input collection and role-acceptance contract only; no role acceptance, operational authority, decision, outreach, enrollment, data collection, execution, gate pass, implementation, commercialization, certification, or release claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-human-input-assignment-packet
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
prepared_at: 2026-07-25
---

# TITMAS CS-D02 Input Assignment Packet v0.1

## 0. Packet Status（包状态）

本包把 CS-D02 仍缺少的人工输入集中到一个失败关闭契约中：

```text
CS_D02_INPUT_ASSIGNMENT_PACKET_DEFINED=true
CS_D02_INPUTS_COMPLETE=false
CS_D02_DECISION_READY=false
CS_D02_DECISION_RECORDED=false

ROLE_ACCEPTANCES_RECORDED=0
REQUIRED_REVIEWERS_ASSIGNED=0
DATA_HANDLING_APPROVED=false
EXECUTION_ENVELOPE_COMPLETE=false

EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
```

它不是人员指派结果，也不是 CS-D02 决定。字段被填写后仍需单独验证、审查和形成 Human
Decision（人工决定）。

机器入口：

- [machine packet](TITMAS-CS-D02-INPUT-ASSIGNMENT-PACKET.v0.1.json)；
- [packet Schema](architecture/schemas/titmas-cs-d02-input-assignment-packet.schema.v0.1.json)。

## 1. Source and Scope（来源与范围）

直接来源：

- [CS-D01 decision](TITMAS-CS-D01-HUMAN-DECISION-RECORD.md)；
- [CS-D02 decision packet](TITMAS-CS-D02-VEAP-PROBLEM-VALIDATION-EXECUTION-DECISION-PACKET.md)；
- [problem-validation governance contract](architecture/veap-problem-validation-governance-contract-v0.1.md)；
- [preparation readiness v0.3](architecture/veap-commercialization-standard-readiness-audit-v0.3.md)。

允许：

- 记录角色候选；
- 记录明确接受、冲突披露和职责范围；
- 选择参与者来源与验证渠道；
- 记录数据处理、预算、timebox、expiry、stop 和 rollback 输入；
- 对完整性做 Schema 和人工 Review。

不允许：

- 自动接受角色；
- 用候选关系推断 Authority；
- 接触或招募参与者；
- 调用外部智能体、API 或验证渠道；
- 收集、复制或处理验证数据；
- 执行 Option A/B；
- 创建 Gate PASS 或市场/客户证据。

## 2. Role Acceptance Inputs（角色接受输入）

| Role | Current candidate | Current state | Required future proof |
|---|---|---|---|
| Human Decision Owner | `zhangbin` | `ASSIGNED_EXISTING` | existing Program Charter authority reference |
| Problem Validation Owner | `zhangbin` | `CANDIDATE_NOT_ACCEPTED` | acceptance timestamp、scope、conflict disclosure、reference |
| Privacy/Data Steward | `zhangbin` | `CANDIDATE_NOT_ACCEPTED` | acceptance timestamp、data duties、conflict disclosure、reference |
| Method Reviewer | `NONE` | `UNASSIGNED_REQUIRED` | reviewer identity、independence basis、acceptance、reference |
| Security Reviewer | `NONE` | `UNASSIGNED_REQUIRED` | reviewer identity、scope、acceptance、reference |
| Claim Reviewer | `NONE` | `UNASSIGNED_REQUIRED` | reviewer identity、independence basis、acceptance、reference |

约束：

```text
CANDIDATE_NE_ACCEPTED_OWNER
ROLE_ACCEPTANCE_NE_OPERATIONAL_AUTHORITY
RECORD_CREATOR_CANNOT_SOLELY_VALIDATE_OWN_RECORD
METHOD_OR_CLAIM_REVIEW_MUST_BE_EXTERNAL_TO_RECORD_CREATOR
AGENT_MAY_ADVISE_BUT_CANNOT_ACCEPT_ROLE_OR_CLOSE_GATE
```

`zhangbin` 作为候选不自动等于已接受。Problem Validation Owner 与 Data Steward 是否允许
由同一人担任，必须记录冲突评估；即使允许，也不能消除独立 Method/Claim Review。

## 3. Participant and Channel Inputs（参与者与渠道输入）

当前：

```text
PARTICIPANT_SOURCE=NOT_SELECTED
VALIDATION_CHANNEL=NOT_SELECTED
INDEPENDENCE_RULE=NOT_APPROVED
CONSENT_OR_SOURCE_BASIS=NOT_APPROVED
```

未来必须明确且只能选择经过审查的有界来源：

1. `DIRECT_RESPONSIBILITY_OWNER_INTERVIEW`；或
2. 经方法、隐私、主张和来源使用审查后的
   `PUBLIC_FIRST_PARTY_PROBLEM_REPORT_REVIEW`。

`GOVERNED_AGENT_ADVISORY_SESSION` 只能提供内部建议，不能单独计为独立组织、客户访谈或
CS-G0 有效记录。

## 4. Data Handling Inputs（数据处理输入）

最低必填：

| Input | Current |
|---|---|
| storage reference | `NOT_SELECTED` |
| access-control evidence | `NOT_AVAILABLE` |
| retention days | `null` |
| withdrawal path | `REQUIRED_NOT_CREATED` |
| deletion path | `REQUIRED_NOT_CREATED` |
| incident route | `REQUIRED_NOT_ASSIGNED` |
| privacy review reference | `NOT_RECORDED` |
| security review reference | `NOT_RECORDED` |
| claim review reference | `NOT_RECORDED` |

允许的数据候选边界保持：

```text
PURPOSE=VEAP_PROBLEM_VALIDATION_ONLY
COLLECTION_MODE=STRUCTURED_FIELDS_AND_PUBLIC_SAFE_PARAPHRASE
RAW_TRANSCRIPT_ALLOWED=false
DIRECT_IDENTIFIER_ALLOWED=false
SECRET_OR_CREDENTIAL_ALLOWED=false
REGULATED_DATA_ALLOWED=false
PUBLIC_OUTPUT=AGGREGATED_COUNTS_AND_PUBLIC_SAFE_PARAPHRASE_ONLY
```

## 5. Execution Envelope Inputs（执行包络输入）

在 Option A 可进入人工决定前，必须补齐：

- `max_problem_records`；
- budget currency 和 cap；
- `starts_at`；
- `expires_at`；
- revocation route；
- stop owner；
- rollback/containment reference；
- breach handling reference。

当前全部为空。输入完整也只产生 `DECISION_INPUT_COMPLETE` 候选状态，不产生执行授权。

## 6. Completion Rules（完整性规则）

```text
INPUTS_COMPLETE =
  ACCEPTED_PROBLEM_VALIDATION_OWNER
  AND ACCEPTED_PRIVACY_DATA_STEWARD
  AND ASSIGNED_METHOD_SECURITY_CLAIM_REVIEWERS
  AND APPROVED_PARTICIPANT_SOURCE_CHANNEL_INDEPENDENCE
  AND APPROVED_STORAGE_ACCESS_RETENTION_WITHDRAWAL_DELETION_INCIDENT
  AND DEFINED_RECORD_CAP_BUDGET_TIMEBOX_EXPIRY_REVOCATION_STOP_ROLLBACK
  AND FORMAL_METHOD_SECURITY_PRIVACY_CLAIM_REVIEW
```

即使 `INPUTS_COMPLETE=true`：

```text
CS_D02_DECISION_RECORDED=false
EXECUTION_AUTHORIZED=false
```

直到独立 CS-D02 Human Decision 被记录。

## 7. Stop Rules（停止规则）

遇到以下任一情况停止：

- 角色未接受或存在未处置冲突；
- Reviewer 仅由记录创建者本人承担；
- 参与者来源或独立性不清；
- storage/access/retention/withdrawal/deletion/incident 任一缺失；
- budget、record cap、timebox 或 expiry 缺失；
- 试图把 agent advisory 当成真实客户/组织；
- 试图把 input complete、packet valid 或 Review 当成 Decision；
- 试图把 Decision 当成 Execution 或 `CS-G0 PASS`。

## 8. Current State（当前状态）

```text
CS_D02_INPUT_ASSIGNMENT_PACKET_DEFINED=true
CS_D02_INPUTS_COMPLETE=false
CS_D02_DECISION_READY=false
CS_D02_DECISION_RECORDED=false
CS_D02_CURRENT_RECOMMENDATION=OPTION_C_CONTINUE_INTERNAL_PREPARATION

OWNER_ACCEPTANCES=0
REQUIRED_REVIEWERS_ASSIGNED=0
DATA_HANDLING_APPROVED=false
EXECUTION_ENVELOPE_COMPLETE=false
STANDING_DIRECTIVE_APPLICABLE_NOW=false

IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
