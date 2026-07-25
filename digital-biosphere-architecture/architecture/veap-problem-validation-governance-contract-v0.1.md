---
document_id: DBA-TITMAS-VEAP-PROBLEM-VALIDATION-GOVERNANCE-CONTRACT-0.1
title: VEAP Problem Validation Governance Contract v0.1
title_zh: VEAP 问题验证治理契约 v0.1
version: 0.1.0
status: contract-defined-roles-unassigned-execution-not-authorized
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: CS-D01
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Internal governance contract only; no participant enrollment, outreach, data collection, market validation, customer adoption, implementation, commercial availability, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-problem-validation-governance-contract
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
defined_at: 2026-07-25
contract_defined: true
roles_assigned: false
data_handling_approved: false
validation_execution_authorized: false
external_outreach_authorized: false
authority_effect: none
---

# VEAP Problem Validation Governance Contract v0.1

## 0. Purpose（目的）

本契约补齐 [VEAP Problem Validation Protocol](veap-problem-validation-protocol-v0.1.md)
从“问题记录格式”到“谁负责、处理什么数据、何时停止”的治理边界。

```text
CONTRACT_DEFINED=true
ROLE_SLOTS_DEFINED=true
ROLES_ASSIGNED=false
DATA_HANDLING_APPROVED=false
VALIDATION_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
```

它是 `CS-D01` 允许的内部准备材料，不产生参与者、客户、Prospect（潜在客户）、市场记录、
实现、网络调用、Evidence Truth 或商业服务。

机器入口：

- [governance contract](veap-problem-validation-governance-contract.v0.1.json)；
- [contract Schema](schemas/veap-problem-validation-governance-contract.schema.v0.1.json)。

## 1. Responsibility Slots（责任角色槽位）

| Role | Current state | Candidate | Required responsibility | Does not gain |
|---|---|---|---|---|
| Human Decision Owner | `ASSIGNED_EXISTING` | `zhangbin` | 对 exact scope 决定接受、退回或拒绝 | 运行、数据处理或自证通过 |
| Problem Validation Owner | `CANDIDATE_NOT_ACCEPTED` | `zhangbin` | 管理协议、来源、计数、失败和报告 | 自动外联、客户或 `CS-G0 PASS` |
| Privacy/Data Steward | `CANDIDATE_NOT_ACCEPTED` | `zhangbin` | purpose、字段、访问、保留、撤回和删除 | 法律结论或公开披露权 |
| Method Reviewer | `UNASSIGNED_REQUIRED` | `NONE` | 独立性、问题中立性、有效记录判定 | Architecture Decision |
| Security Reviewer | `UNASSIGNED_REQUIRED` | `NONE` | secret、PII、存储、传输和 incident route | Certification Authority |
| Claim Reviewer | `UNASSIGNED_REQUIRED` | `NONE` | Market、Customer、Adoption、Certificate 和公开措辞 | Release Authority |

`zhangbin` 已是 Human Program Owner，但这不会自动接受其他候选角色。任一候选必须以
独立 assignment record（指派记录）确认有效期、替代、撤销和冲突处理。

### Minimum separation

- 执行记录的创建者不能单独判定自己的记录 `VALID`；
- Human Decision Owner 可以承担小规模项目的一个 operational role，但必须披露冲突；
- 至少一个 Method/Claim review input 必须来自记录创建者之外；
- governed agent 可以提供 advisory review input，但不能成为最终 Human Reviewer 或自行
  关闭 Gate。

## 2. Validation Channels（验证渠道）

| Channel | Purpose | Current status | `CS-G0` counting |
|---|---|---|---|
| `DIRECT_RESPONSIBILITY_OWNER_INTERVIEW` | 获取近期实例、workaround、成本和优先级 | `NOT_AUTHORIZED` | 满足完整契约时可以 |
| `PUBLIC_FIRST_PARTY_PROBLEM_REPORT_REVIEW` | 查找公开 issue、incident 或维护者一手问题报告 | `DESIGN_ONLY_NOT_AUTHORIZED` | 当前不能；需独立 method amendment 和 Claim/Privacy Review |
| `GOVERNED_AGENT_ADVISORY_SESSION` | 验证可理解性、反对意见和字段缺口 | `INTERNAL_ADVISORY_ALLOWED` | 不能，除非绑定真实独立组织问题和人类责任方 |

模型、prompt、persona 或 Provider 数量不增加组织独立性。公开文章推断、搜索结果或模型
赞扬不能被包装成问题记录。

## 3. Data Classes（数据类别）

### Candidate minimum data

- pseudonymous `observer_ref`；
- coarse `organization_or_context_ref`；
- observer class 和 independence basis；
- public-safe recent example summary；
- workaround、limitations、priority reason；
- consent/source reference；
- structured rejection、withdrawal 和 known limitations。

### Prohibited

```text
CREDENTIALS_OR_SECRETS
RAW_CUSTOMER_EVIDENCE
REGULATED_OR_SPECIAL_CATEGORY_DATA
UNNECESSARY_DIRECT_IDENTIFIERS
RAW_PROMPT_RESPONSE_MEMORY_OR_TOOL_PAYLOAD
CHAIN_OF_THOUGHT
PRIVATE_SOURCE_CODE_OR_DATABASE_CONTENT
UNCONSENTED_AUDIO_VIDEO_OR_TRANSCRIPT
```

`RAW_TRANSCRIPT_CAPTURE_ALLOWED=false`。如果不能在不采集禁止数据的情况下理解近期实例，
该记录必须停止并保持 `INVALID` 或 `WITHDRAWN`。

## 4. Data Handling Candidate（数据处理候选）

以下是待 `CS-D02` 审查的最小候选，不是已执行机制：

```yaml
purpose: VEAP_PROBLEM_VALIDATION_ONLY
collection_mode: STRUCTURED_FIELDS_AND_PUBLIC_SAFE_PARAPHRASE
raw_transcript_capture_allowed: false
direct_identifier_collection_allowed: false
secret_or_credential_collection_allowed: false
default_public_output: AGGREGATED_COUNTS_AND_PUBLIC_SAFE_PARAPHRASE_ONLY
private_record_access: ASSIGNED_OWNER_DATA_STEWARD_AND_REVIEWER_ONLY
storage_location: NOT_SELECTED
access_control_evidence: NOT_AVAILABLE
retention_period: NOT_DECIDED
withdrawal_path: REQUIRED_NOT_CREATED
deletion_path: REQUIRED_NOT_CREATED
incident_route: REQUIRED_NOT_ASSIGNED
```

Storage、retention、withdrawal、deletion 和 incident route 任一为 `NOT_*` 时，数据收集必须
保持未授权。

## 5. Record Review Lifecycle（记录审查生命周期）

```text
DRAFT
  -> SOURCE_AND_CONSENT_CHECK
  -> PRIVACY_AND_PROHIBITED_DATA_CHECK
  -> INDEPENDENCE_AND_METHOD_REVIEW
  -> VALID | PARTIAL | INVALID
  -> COUNTED | NOT_COUNTED
  -> WITHDRAWN | RETAINED_UNDER_APPROVED_POLICY
```

规则：

- 创建者不能单独完成 `VALID`；
- `PARTIAL`、`INVALID`、`WITHDRAWN` 和 negative results 必须保留最小 provenance；
- withdrawal 删除内容后，只允许保留不含被删除内容的 tombstone；
- `VALID` 不等于 Customer、Design Partner、Adoption、Contract 或 Commercial Commitment；
- 计数器由经过 review 的记录确定，不能由模型自报。

## 6. Stop Conditions（停止条件）

任一条件出现即停止：

- Owner、Data Steward 或 required Reviewer 未被接受；
- storage、retention、withdrawal、deletion 或 incident route 未批准；
- consent/source basis 缺失；
- 独立性无法证明；
- 出现 secret、credential、PII、客户 Evidence 或受监管数据；
- 观察者撤回；
- 诱导、改写或将负面反馈升级为客户证言；
- 试图从 advisory Agent session 生成独立组织记录；
- 试图从记录或阈值自动生成 Gate PASS。

## 7. Required Decision Inputs（所需决定输入）

`CS-D02` 可决定前必须补齐：

1. 接受的 Problem Validation Owner；
2. 接受的 Privacy/Data Steward；
3. Method Reviewer 和 Claim Reviewer；
4. exact participant source/channel；
5. storage、access、retention、withdrawal、deletion 和 incident route；
6. outreach、network processing、data classes 和预算范围；
7. stop/rollback 和 breach handling；
8. decision expiry/revocation。

当前推荐：

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CS_D02_DECISION_INPUT_AND_FAIL_CLOSED_DATA_GOVERNANCE
NOT_RECOMMENDED_AS=EXECUTION_AUTHORIZATION_OR_MARKET_VALIDATION_RESULT
```

## 8. Current State（当前状态）

```text
VEAP_PROBLEM_VALIDATION_GOVERNANCE_CONTRACT_DEFINED=true
VEAP_PROBLEM_VALIDATION_ROLE_SLOTS_DEFINED=true
VEAP_PROBLEM_VALIDATION_ROLES_ASSIGNED=false
VEAP_PROBLEM_VALIDATION_DATA_HANDLING_APPROVED=false

PROBLEM_VALIDATION_OWNER_ASSIGNED=false
PRIVACY_DATA_STEWARD_ASSIGNED=false
METHOD_REVIEWER_ASSIGNED=false
SECURITY_REVIEWER_ASSIGNED=false
CLAIM_REVIEWER_ASSIGNED=false

VALIDATION_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
NETWORK_PROCESSING_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
PUBLIC_CLAIM_AUTHORIZED=false

VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
CS_G1_PASS=false
```
