---
document_id: DBA-TITMAS-VEAP-PREDECISION-CONFORMANCE-DESIGN-0.1
title: VEAP Pre-decision Conformance Design v0.1
title_zh: VEAP 决策前符合性设计 v0.1
version: 0.1.0
status: design-only-all-cases-not-executed
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: CS-D01_NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Pre-decision case design only; no normative profile, implementation, executed conformance, certification, commercial, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-conceptual-conformance-design
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
designed_at: 2026-07-25
case_count: 20
executed_cases: 0
passed_cases: 0
implementation_authorized: false
authority_effect: none
---

# VEAP Pre-decision Conformance Design v0.1

## 0. Purpose and Verdict（目的与结论）

本设计把 CS-D01 智能体评审提出的主要反对理由——“边界只写在文档里，尚未由失败用例
证明”——转化为 20 个可审查 case candidate（用例候选）。

```text
VEAP_PREDECISION_CONFORMANCE_DESIGN_DEFINED=true
VEAP_CONCEPTUAL_CASE_COUNT=20
VEAP_CONFORMANCE_CASES_EXECUTED=0
VEAP_CONFORMANCE_CASES_PASSED=0
CS_D01_DECIDED=false
```

这些 case 只用于审查未来 Profile 是否有足够失败语义。它们不是 normative requirements、
测试实现、Validator、Certification 或 Conformance PASS。

## 1. Inputs（输入）

- [Commercialization Standards Roadmap](titmas-commercialization-standards-roadmap-v0.1.md)；
- [CS-D01 Decision Packet](../TITMAS-CS-D01-VEAP-PROBLEM-SCOPE-DECISION-PACKET.md)；
- [CS-D01 Agent Review](../TITMAS-CS-D01-AGENT-CUSTOMER-REVIEW.md)；
- [VEAP Canonical Ownership Crosswalk](veap-canonical-ownership-crosswalk-v0.1.md)；
- [Interface Boundary Rules](interface-boundary-rules.md)；
- [SAEE–DBOS Contract](saee-dbos-contract.md)。

机器目录：

- [case catalog](veap-predecision-conformance-cases.v0.1.json)；
- [catalog schema](schemas/veap-predecision-conformance-case-catalog.schema.v0.1.json)。

## 2. Design Groups（设计分组）

| Group | Count | Question |
|---|---:|---|
| `OWNERSHIP` | 4 | 是否建立第二 canonical Owner 或隐藏写权？ |
| `PROVENANCE` | 5 | subject、execution、observation、admission 和 digest 能否追溯？ |
| `SEMANTIC_NON_ELEVATION` | 5 | Evidence/Verification/Evaluation/Recommendation/Attestation 是否被越权提升？ |
| `LIFECYCLE_FAILURE` | 4 | replay、partial、revocation 和 unknown version 是否失败关闭？ |
| `BOUNDED_POSITIVE` | 2 | 完整引用和 SAEE unavailable 时能否保持有界、可解释状态？ |

## 3. Result Vocabulary（结果词汇）

| Expected result | Meaning |
|---|---|
| `REJECT` | 缺少强制来源、出现越权声明或 integrity mismatch，不生成 success candidate |
| `BLOCKED` | 所需 Owner/Decision/source 尚未冻结，停止推进 |
| `CONFLICTED` | 多个来源争夺同一权属或状态，保留冲突 |
| `NOT_ASSESSED` | 输入不足，不能作结论 |
| `UNSUPPORTED` | profile/version/feature 未知或不支持 |
| `ACCEPT_CANDIDATE` | 只表示若未来规范采用，可进入后续检查；不创建 DBOS record 或 Truth |
| `ACCEPT_PARTIAL_CANDIDATE` | 有界引用成立但某可选下游不可用，必须显式保留缺失 |

## 4. Mandatory Cross-cutting Assertions（强制横向断言）

未来若获准实现，每个 case 都必须检查：

```text
OBSERVATION_NE_EVIDENCE
EVIDENCE_NE_TRUTH
VERIFICATION_NE_PERMISSION
ATTESTATION_NE_CERTIFICATION
EVALUATION_NE_AUTHORITY
RECOMMENDATION_NE_DECISION
DECISION_NE_EXECUTION
PAYMENT_NE_PERMISSION
```

任何 case 不得因 `ACCEPT_CANDIDATE` 自动产生：

- Entity/Agent/Runtime；
- Evidence Object；
- Verification Truth；
- Fitness；
- Permission；
- Decision；
- Certificate；
- Commercial Offering。

## 5. Catalog Summary（目录摘要）

### Ownership

- profile claims DBOS object ownership；
- EEOAP version/Owner unresolved；
- commercial implementation claims Specification Authority；
- two sources claim the same canonical Owner.

### Provenance

- missing subject reference；
- framework-local agent ID presented as DBOS entity；
- missing execution source/version；
- observation without admission；
- evidence digest mismatch.

### Semantic non-elevation

- Evidence treated as Truth；
- Verification PASS grants Permission；
- VEAP generates Fitness；
- SAEE Recommendation becomes Decision；
- attestation marketed as Certificate.

### Lifecycle and failure

- duplicate/replay；
- partial observation hidden；
- revoked attestation used as current；
- unknown profile version.

### Bounded positive

- complete version-bound reference envelope；
- SAEE unavailable while DBOS references remain valid and evaluation stays absent.

## 6. Execution Gate（执行闸门）

case implementation/execution 至少需要：

1. `CS-D01` accepted；
2. TITMAS bounded Specification Authority assigned；
3. object ownership crosswalk accepted by Domain Owners；
4. VEAP Draft Profile and Schema separately authorized；
5. test Owner、implementation ref、fixtures 和 result-set contract；
6. security/privacy/claim review；
7. explicit implementation and execution authorization。

```text
CASE_DESIGN_NE_TEST_IMPLEMENTATION=true
CATALOG_SCHEMA_VALID_NE_CASE_EXECUTION=true
EXPECTED_RESULT_NE_ACTUAL_RESULT=true
```

## 7. Current State（当前状态）

```text
VEAP_PREDECISION_CONFORMANCE_DESIGN_DEFINED=true
VEAP_CONCEPTUAL_CASES_DEFINED=20
VEAP_CONCEPTUAL_CASE_GROUPS=5
VEAP_CONFORMANCE_TESTS_IMPLEMENTED=0
VEAP_CONFORMANCE_CASES_EXECUTED=0
VEAP_CONFORMANCE_CASES_PASSED=0
VEAP_CONFORMANCE_RESULT_SET_CREATED=false

CS_D01_DECIDED=false
NORMATIVE_PROFILE_AUTHORIZED=false
SCHEMA_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
EXECUTION_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```
