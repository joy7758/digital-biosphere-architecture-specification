---
document_id: DBA-TITMAS-CE-G13-OFFLINE-CONTRACT-PACKAGE-R2-REFERENCE-RESOLUTION-REMEDIATION-RECOMMENDATION-0.2
title: TITMAS CE-G13 Offline Contract Package R2 Reference Resolution Remediation Recommendation v0.2
title_zh: TITMAS CE-G13 离线契约包 R2 引用解析修复建议 v0.2
version: 0.2.0
status: replacement-recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: one-uri-alignment-and-fail-closed-offline-revalidation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
supersedes: TITMAS-CE-G13-OFFLINE-CONTRACT-PACKAGE-R2-REFERENCE-RESOLUTION-REMEDIATION-RECOMMENDATION-v0.1.md
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Offline Contract Package R2 Reference Resolution Remediation Recommendation v0.2

## Recommendation

Select **Option A — preserve both prior failures, align one base Schema `$id`, enforce a
no-remote local Registry and run one new R2 offline validation only after an independent Decision**.

This is a replacement Recommendation, not a retry of the v0.1 review.

```text
R1_VALIDATION_RESULT=FAIL_CLOSED_SCHEMA_REFERENCE_RESOLUTION_ATTEMPTED_REMOTE_FETCH
V0_1_RECOMMENDATION_REVIEW_RESULT=FAIL_CLOSED_NO_PERSISTED_PROVIDER_RESPONSE
R1_RETRY=false
V0_1_REVIEW_RETRY=false
R2_VALIDATION_AUTHORIZED=false
```

## Evidence and root cause

The R1 failure is recorded in
`TITMAS-CE-G13-OFFLINE-CONTRACT-PACKAGE-R1-FAILURE-REPORT-v0.1.md`.

The five role schemas resolve their relative common-schema reference to:

`https://titmas.cn/schemas/session-response.base.schema.v0.1.json`

The common schema declares:

`https://titmas.cn/schemas/ce-g13-session-response.base.schema.v0.1.json`

The mismatch caused a local-store miss. Deprecated resolver behavior attempted remote retrieval,
which violated the offline contract and failed through the proxy. The first v0.1 Recommendation
review then produced no persisted Provider response, so it is `UNKNOWN` and non-qualifying.

## Option A exact scope

After a qualifying review and independent Decision:

1. change only the common schema `$id` to the URI produced by the existing relative references;
2. update only that file's `bytes` and `sha256` in the non-recursive package manifest;
3. use an ephemeral Draft 2020-12 validator backed by an explicit local Registry;
4. configure Registry retrieval so every unknown URI raises locally and cannot use HTTP, HTTPS,
   DNS, Provider access or fallback;
5. execute exactly one new R2 validation;
6. commit and push the bounded package and governance evidence only on complete PASS.

## Alternatives rejected

- **Inline the common schema five times:** duplicates rules and expands drift.
- **Permit remote schema lookup:** violates the offline contract.
- **Skip role-instance validation:** fails to prove cross-file reference integrity.
- **Treat R1 or the unobserved review as passing:** violates evidence discipline.

## R2 required checks

- exact 28-file allowlist and 21 JSON / 2 Markdown / 5 prompt counts;
- no executable files;
- duplicate-key rejection for all JSON;
- Draft 2020-12 meta-validation for all 14 schemas;
- candidate/template validation;
- local-only cross-file resolution;
- positive and wrong-session negative samples for all five roles;
- direct-JSON prompts and cold-discovery answer-key absence;
- exact 27-entry manifest bytes and SHA-256;
- 100 scoring points and at least 24 unique REJECT cases;
- zero successful or attempted network, credential, model-session, technical-run or Runtime action.

Any failure is a new immutable `FAIL_CLOSED`; no patch or retry.

## Commit gate and non-authorizations

PASS may authorize only one bounded commit/push of:

- the exact 28-file package;
- the R1 failure report;
- both versioned Recommendations and the non-qualifying v0.1 review record;
- the qualifying v0.2 `qwen3.7-max` Recommendation review;
- the independent R2 Decision and its qualifying `qwen3.7-max` review.

No PR, merge, release or deployment is authorized.
No public fetch, CE-G13 role session, technical reuse run, Agent, Runtime, Entity, Capability,
Permission or Evidence Truth is authorized.
No customer adoption, demand, commercial offering, certification or production claim is authorized.

```text
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```
