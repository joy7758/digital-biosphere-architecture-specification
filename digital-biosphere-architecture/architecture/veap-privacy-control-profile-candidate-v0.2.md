---
document_id: DBA-VEAP-PRIVACY-CONTROL-PROFILE-CANDIDATE-0.2
title: VEAP Privacy Control Profile Candidate v0.2
title_zh: VEAP 隐私控制配置候选 v0.2
status: DEVELOPMENT_CANDIDATE_HUMAN_ADJUDICATION_REQUIRED
maturity: Development
maturity_scope: entire-document
created_at: 2026-07-28T17:56:40+08:00
primary_repository: digital-biosphere-architecture
decision_reference: CS-G1-REMEDIATION-D01
implementation_effect: none
commercial_effect: none
authority_effect: none
---

# VEAP Privacy Control Profile Candidate v0.2

## 1. Scope

This document is a Development-only remediation overlay for the four Privacy
risks in the frozen VEAP risk register. It preserves all v0.1 sources. It is
not an adopted specification, legal opinion, compliance claim, data-processing
authorization or implementation requirement.

## 2. Control candidates

### `VEAP-PRIV-001` — purpose, recipient and secondary-use binding

Every exchange must bind one or more declared purpose classes:

- `EXECUTION_ACCOUNTABILITY`;
- `EVIDENCE_VERIFICATION`;
- `GOVERNANCE_REVIEW`.

Every recipient must belong to an explicit recipient class:

- `SUBJECT_OWNER`;
- `AUTHORIZED_VERIFIER`;
- `AUTHORIZED_GOVERNANCE_REVIEWER`.

Secondary use is forbidden by default. Any secondary use requires a separate,
explicit `secondary_use_decision_reference`; an absent or unresolved reference
triggers fail-closed handling.

### `VEAP-PRIV-002` — field-level minimization

Reference-first exchange is mandatory. Raw prompt, response and tool content is
forbidden by default. Each retained reference field must have a declared
purpose and an authorization requirement:

| Field category | Allowed purpose | Required authority |
|---|---|---|
| Entity identity reference | accountability | authorized subject scope |
| Execution reference | accountability | authorized execution scope |
| Evidence reference | verification | authorized evidence scope |
| Verification reference | verification | authorized verification scope |
| Evaluation reference | governance review | authorized evaluation scope |
| Governance decision reference | governance review | authorized decision scope |
| Limitation/failure reference | accountability, review | authorized case scope |

Raw content requires a separate content-authorization reference, an explicit
field allowlist, redaction and secret scanning. Missing field justification or
content authorization triggers fail-closed handling.

### `VEAP-PRIV-003` — retention, deletion proof and legal hold

Every retained item must declare one retention class:

- `REFERENCE_ONLY`;
- `RESTRICTED_REFERENCE`;
- `PUBLIC_SAFE_EXTRACT`;
- `CONTENT_AUTHORIZED`.

Each class must resolve to a retention-policy reference. Deletion creates a
content-free tombstone and a deletion-proof reference. A legal hold requires a
separate legal-hold reference and cannot be inferred. Immutable accountability
history preserves only the permitted reference/tombstone lineage, not deleted
content. Missing policy, proof or hold boundary triggers fail-closed handling.

### `VEAP-PRIV-004` — namespace separation and linkability

Every pseudonymous or indirect identifier must bind its source namespace,
target namespace and access scope. Cross-namespace correlation requires a
documented `linkability_assessment_reference`. Public-safe extraction forbids
correlating identifiers. Missing namespace separation or linkability
assessment triggers fail-closed handling.

## 3. Non-effects

These candidates do not establish legal sufficiency, compliance, privacy
acceptance, residual-risk acceptance, canonical ownership or implementation.

```text
PRIVACY_CONTROLS_ADOPTED=false
PRIVACY_COMPLIANCE_CLAIMED=false
DATA_PROCESSING_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
CS_G1_PASS=false
HUMAN_ADJUDICATION_REQUIRED=true
```
