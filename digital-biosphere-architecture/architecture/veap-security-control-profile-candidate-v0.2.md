---
document_id: DBA-VEAP-SECURITY-CONTROL-PROFILE-CANDIDATE-0.2
title: VEAP Security Control Profile Candidate v0.2
title_zh: VEAP 安全控制配置候选 v0.2
status: DEVELOPMENT_CANDIDATE_OFFLINE_REVIEW_INPUT_ONLY
maturity: Development
maturity_scope: entire-document
created_at: 2026-07-28T21:50:22+08:00
primary_repository: digital-biosphere-architecture
decision_reference: CS-G1-REMEDIATION-D02
implementation_effect: none
commercial_effect: none
authority_effect: none
---

# VEAP Security Control Profile Candidate v0.2

## 1. Scope

This profile specifies candidate contract requirements for the five frozen VEAP
Security risks. It does not implement, deploy or prove the effectiveness of any
control.

For every control:

```text
CONTROL_SPECIFICATION_STATE=DEFINED_CANDIDATE
IMPLEMENTATION_STATE=NOT_IMPLEMENTED_BY_THIS_SPEC
OPERATIONAL_EFFECTIVENESS=NOT_ASSESSED
CURRENT_STOP_STATE=NOT_ASSESSED
```

## 2. `VEAP-SEC-001` — integrity and source binding

Every portable digest or reference must bind:

- digest algorithm and algorithm version;
- referenced object/profile version;
- exact source namespace and source identifier;
- exact subject/entity reference;
- canonical-source status and observation time.

Digest mismatch, source ambiguity or subject conflict must return
`REJECTED_INTEGRITY_BINDING`. Silent repair, fallback substitution and
latest-timestamp selection are forbidden.

Future implementation evidence must include tamper, source-impersonation,
algorithm-confusion and silent-repair negative cases.

## 3. `VEAP-SEC-002` — replay and duplicate control

Every package must declare:

- globally scoped package identifier;
- issuer and namespace;
- creation and observed times;
- acceptance-time policy reference;
- replay/duplicate status;
- predecessor/successor or revocation reference when applicable.

Duplicate identity, expired acceptance window or unknown replay status must
return `REJECTED_REPLAY_OR_DUPLICATE_UNKNOWN`. A success record may not replace
or erase a prior duplicate/replay result.

Future implementation evidence must include first-use, exact replay,
cross-namespace duplicate, expired-window and immutable-failure tests.

## 4. `VEAP-SEC-003` — tenant and subject isolation

Every correlation must bind:

- tenant or operational-context namespace;
- subject/entity reference;
- authorization/decision reference;
- allowed correlation purpose and scope.

Missing authorization, cross-tenant conflict or subject mismatch must return
`REJECTED_TENANT_OR_SUBJECT_CONFLICT`. A correlation must not be inferred from
similar labels, timestamps or model output.

Future implementation evidence must include cross-tenant access, subject
substitution, missing-authorization and correlation-conflict tests.

## 5. `VEAP-SEC-004` — issuer and verifier currency

Every issuer/verifier reference must bind:

- identity and namespace;
- validity interval;
- status observation time;
- revocation-status reference;
- incident-response or compromise reference;
- rule/profile version.

Expired, revoked, conflicted, stale or unknown status must return
`NOT_CURRENT_OR_NOT_ASSESSED`; it must never be promoted to trusted.

Future implementation evidence must include expiry, revoked identity, stale
status, unavailable revocation source and incident-path tests.

## 6. `VEAP-SEC-005` — sensitive-content exclusion

Portable packages are reference-first and deny raw content by default. A raw
field requires:

- separate content-authorization reference;
- explicit field allowlist;
- data-class declaration;
- redaction declaration;
- secret-scan declaration and result;
- retention and recipient scope.

Credentials, secrets, direct identifiers, regulated data or unclassified raw
content must return `REJECTED_SENSITIVE_CONTENT`. Missing scanner or unknown
classification is fail closed.

Future implementation evidence must include credential, token, identifier,
regulated-data, obfuscated-secret and scanner-unavailable cases.

## 7. Conformance separation

Specification-stage conformance may verify only that required fields, statuses
and fail-closed rules exist and are internally consistent.

Implementation-stage conformance must separately prove that a concrete
implementation enforces those rules. Technical validation must separately
measure operational behavior and limitations.

```text
SCHEMA_VALID_NE_CONTROL_IMPLEMENTED=true
CONTROL_IMPLEMENTED_NE_CONTROL_EFFECTIVE=true
TEST_PASS_NE_PRODUCTION_PROOF=true
```

## 8. Non-effects

```text
SECURITY_CONTROLS_ADOPTED=false
SECURITY_CONTROLS_IMPLEMENTED=false
SECURITY_CONTROLS_EFFECTIVE=false
CURRENT_STOP_STATE=NOT_ASSESSED
RESIDUAL_RISK_ACCEPTED=false
MODEL_REVIEW_AUTHORIZED=false
PROVIDER_REQUESTS_AUTHORIZED=0
CS_G1_PASS=false
STANDARD_READY=false
```
