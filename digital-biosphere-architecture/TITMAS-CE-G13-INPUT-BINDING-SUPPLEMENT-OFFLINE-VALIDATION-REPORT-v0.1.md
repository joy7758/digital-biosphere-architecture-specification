---
document_id: DBA-TITMAS-CE-G13-INPUT-BINDING-SUPPLEMENT-OFFLINE-VALIDATION-REPORT-0.1
title: TITMAS CE-G13 Input Binding Supplement Offline Validation Report v0.1
title_zh: TITMAS CE-G13 输入绑定补充契约离线验证报告 v0.1
version: 0.1.0
status: pass-contract-validation-only
maturity: Development
owner_ref: zhangbin
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Input Binding Supplement Offline Validation Report v0.1

## Result

```text
VALIDATION_RESULT=PASS
VALIDATION_RUNS=1
SUPPLEMENT_FILES=16
JSON_DUPLICATE_KEY_CHECKS=14/14
SCHEMAS_META_VALID=6/6
CANDIDATE_AND_TEMPLATE_INSTANCES=6/6
ROLE_INPUT_ENVELOPES=5/5
NEGATIVE_CASES_REJECTED=32/32
CHECKS_PASS=16/16
CHECKS_FAIL=0
```

The exact supplement at commit `853f86395ba687929da5f45024486f046866d01d` conforms to its
frozen local offline contract.

## Integrity

```text
SUPPLEMENT_PACKAGE_MANIFEST_SHA256=5a67190aef647c1881d764806b59e0d9b7ed3b9438145a9eed8c9eecc16a2b34
BASE_PACKAGE_MANIFEST_SHA256=be7b0db4f0f349f8898f749e8ee0f4bd6a3407c79acbe33b415da081ff9ea9ed
BASE_PACKAGE_MUTATED=false
SUPPLEMENT_PACKAGE_MUTATED=false
```

The supplement contains 14 JSON files, two Markdown files, no executable, no symlink and no nested
file. Its non-recursive manifest covers the other 15 files with exact byte counts and SHA-256.

## Contract checks

- all six Schemas are Draft 2020-12 meta-valid;
- all six candidate/template instances validate;
- unknown Schema URIs are rejected by the local Registry;
- identity content encoding, strict UTF-8 and deterministic no-rewrite sanitization are preserved;
- raw and sanitized public text hashes, byte counts, profile binding and order are enforced;
- the future result surface contains 25 hash entries plus the excluded manifest, exactly 26 files;
- runtime result statuses remain `NOT_EXECUTED`, `PASS`, `FAIL_CLOSED`;
- `CONDITIONAL_REMEDIATION_REQUIRED` remains a governance interpretation;
- failures cannot be edited, overwritten or retried into PASS;
- all five ephemeral role envelopes validate with their exact component order;
- S04 requires the validated S03 reuse-plan result;
- S05 requires exact S01–S04 response bindings in order.

## Negative cases

All 32 declared mutations were rejected. The set covers immutable-base, exact-file, executable,
recursive-hash, duplicate-key, transport, charset, deterministic sanitization, public-text hash,
input-order, S04/S05 dependency, secret, model identity, exact-output and failure-retention
boundaries.

## Zero-effect boundary

```text
NETWORK_REQUESTS=0
DNS_REQUESTS=0
CREDENTIAL_READS=0
MODEL_REQUESTS=0
PUBLIC_FETCHES=0
TECHNICAL_REUSE_RUNS=0
RUNTIME_STARTS=0
AGENT_INSTANCES=0
ENTITY_INSTANCES=0
CAPABILITY_INSTANCES=0
PERMISSION_GRANTS=0
EVIDENCE_TRUTH_OBJECTS=0
```

One unknown Schema URI was intentionally submitted to the local Registry and rejected without
network or DNS access.

## Interpretation boundary

PASS proves only that the 16-file input-binding supplement conforms to its offline contract. It
does not authorize CE-G13 execution, public retrieval, five model sessions or technical reuse and
does not prove customer adoption, demand, offering, certification, Standard Ready or Production
Ready.

```text
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```
