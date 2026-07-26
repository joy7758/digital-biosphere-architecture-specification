---
document_id: DBA-TITMAS-CS-D02-PRE-03-VEAP-DRAFT-CONTRACT-DECISION-RECORD-0.1
title: TITMAS CS-D02-PRE-03 VEAP Draft Contract Decision Record v0.1
title_zh: TITMAS CS-D02-PRE-03 VEAP 草案契约决定记录 v0.1
version: 0.1.0
status: decided-bounded-draft-contract-authorized
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_owner_ref: zhangbin
decision_reference: CS-D02-PRE-03
parent_decision_reference: CS-D02
standing_directive_reference: TITMAS-CS-STANDING-001
recommendation_reference: TITMAS-CS-KIMI-20260725-001
decision_result: AUTHORIZE_BOUNDED_VEAP_DRAFT_PROFILE_AND_SCHEMA
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Draft-contract authorization only; no adopted standard, implementation, conformance execution, commercial offering, certification, release, or production claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: human-program-governance-decision-record
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
decided_at: 2026-07-26T13:09:15+08:00
authority_effect: bounded-dba-draft-stewardship-only
---

# TITMAS CS-D02-PRE-03 VEAP Draft Contract Decision Record v0.1

## 1. Decision（决定）

Human Program Owner `zhangbin` 已持续要求推进 TITMAS 商业化标准路线，并已通过
[`TITMAS-CS-STANDING-001`](TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-v0.1.md)
允许对满足精确前置条件的推荐形成有界决定。

Kimi 主评审给出的最高优先建议是：

> 先形成 VEAP normative profile/schema，再进入一个可审计用例。

本决定将该建议拆分为两个不同动作，只批准第一个：

```text
CS-D02-PRE-03=AUTHORIZE_BOUNDED_VEAP_DRAFT_PROFILE_AND_SCHEMA

VEAP_DRAFT_PROFILE_CANDIDATE_AUTHORIZED=true
VEAP_SCHEMA_CANDIDATE_AUTHORIZED=true
SCHEMA_REHEARSAL_WITH_SYNTHETIC_FIXTURES_AUTHORIZED=true

CONFORMANCE_EXECUTION_AUTHORIZED=false
REFERENCE_IMPLEMENTATION_AUTHORIZED=false
```

机器记录：

- [decision record](TITMAS-CS-D02-PRE-03-VEAP-DRAFT-CONTRACT-DECISION-RECORD.v0.1.json)；
- [decision Schema](architecture/schemas/titmas-cs-d02-pre-03-veap-draft-contract-decision-record.schema.v0.1.json)。

## 2. Exact Authorized Artifacts（精确授权产物）

本决定只允许在 DBA 中创建：

1. `architecture/veap-draft-profile-v0.1.md`；
2. `architecture/schemas/veap-envelope.schema.v0.1.json`；
3. 一个结构有效的 synthetic fixture；
4. 一个必须被 Schema 拒绝的 synthetic negative fixture；
5. 与上述文件直接相关的 README、Decision Queue、roadmap 和 agent-readable 状态更新；
6. path-scoped validation、commit 和 push。

Draft steward（草案维护责任）暂由 DBA / `zhangbin` 承担。该安排只维护候选字节，
不创建 TITMAS 独立 Specification Authority，也不解决 `AF-D15`、`AF-D16` 或 Domain
Owner acceptance。

## 3. Preconditions（前置条件）

直接证据：

- [`CS-D01`](TITMAS-CS-D01-HUMAN-DECISION-RECORD.md) 已授权有界内部问题、范围与交叉映射工作；
- [`ADR-031`](architecture/ADR-031-agent-first-review-governance.md) 已采用智能体优先评审路线；
- [Kimi Lead Review](TITMAS-CS-D02-KIMI-LEAD-REVIEW.md) 明确推荐先补 Profile/Schema；
- [VEAP Ownership Crosswalk](architecture/veap-canonical-ownership-crosswalk-v0.1.md) 已定义
  VEAP 可以携带和禁止拥有的表面；
- 本次只处理 public-safe、synthetic、无客户和个人数据的规范材料。

## 4. Claim Boundary（主张边界）

本次允许使用：

```text
VEAP_DRAFT_PROFILE_CANDIDATE_CREATED
VEAP_SCHEMA_CANDIDATE_CREATED
SCHEMA_REHEARSAL_PASS_OR_FAIL
```

不得使用：

```text
VEAP_STANDARD_ADOPTED
VEAP_CONFORMANCE_PASS
VEAP_CERTIFIED
VEAP_PRODUCTION_READY
TITMAS_COMMERCIAL_OFFERING_AVAILABLE
```

Schema valid 只表示 JSON 结构符合候选 Schema，不表示来源真实、语义正确、Evidence
充分、执行成功、Permission 有效或系统可信。

## 5. Stop Conditions（停止条件）

遇到以下任一情况停止：

- 候选字段创建第二套 DBOS Identity、Execution、Evidence、Verification 或 Permission；
- 候选字段允许 VEAP 生成 Fitness、Decision、Certification 或 Truth；
- 需要调用 DBOS、SAEE、Runtime、外部服务或真实数据；
- 需要改变 `implementation_authorized=false`、`commercial_offer_authorized=false`、
  `certification_authorized=false` 或 `release_authorized=false`；
- Schema 不能拒绝缺少 admission reference 的 Evidence binding；
- 无法保留 partial、failure、unknown 或 revocation 状态。

## 6. Gate Effect（闸门效果）

```text
CS_D02_PRE_03_DECIDED=true
VEAP_DRAFT_PROFILE_CANDIDATE_AUTHORIZED=true
VEAP_SCHEMA_CANDIDATE_AUTHORIZED=true

CS_G0_PASS=false
CS_G1_PASS=false
CS_G2_PASS=false
VEAP_NORMATIVE_PROFILE_ADOPTED=false
VEAP_STANDARDIZATION_READY=false
```

本决定移除“没有可审查契约字节”的缺口，但不绕过问题验证、Owner/Authority 冻结和正式
Review。Draft candidate 可以存在，Gate 仍按 fail-closed 顺序保持未通过。

## 7. Non-effects（非效果）

```text
SPECIFICATION_CANDIDATE_NE_ADOPTED_STANDARD=true
SCHEMA_VALID_NE_SEMANTIC_CONFORMANCE=true
ATTESTATION_NE_CERTIFICATION=true
EVIDENCE_NE_TRUTH=true

IMPLEMENTATION_AUTHORIZED=false
CONFORMANCE_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false

AGENT_INSTANCE_CREATED=false
RUNTIME_CREATED=false
ENTITY_INSTANCE_CREATED=false
PERMISSION_GRANTED=false
CANONICAL_EVIDENCE_CREATED=false
```
