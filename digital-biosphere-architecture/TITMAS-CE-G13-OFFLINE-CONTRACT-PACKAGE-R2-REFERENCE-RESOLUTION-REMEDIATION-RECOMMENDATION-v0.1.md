---
document_id: DBA-TITMAS-CE-G13-OFFLINE-CONTRACT-PACKAGE-R2-REFERENCE-RESOLUTION-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G13 Offline Contract Package R2 Reference Resolution Remediation Recommendation v0.1
title_zh: TITMAS CE-G13 离线契约包 R2 引用解析修复建议 v0.1
version: 0.1.0
status: recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: one-uri-alignment-and-fail-closed-offline-revalidation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Offline Contract Package R2 Reference Resolution Remediation Recommendation v0.1

## 1. Recommendation

Select **Option A — preserve R1, align one base Schema `$id`, use a no-remote resolver and perform
one new R2 offline validation under a new independent Decision**.

```text
RECOMMENDED_OPTION=A
R1_RESULT=FAIL_CLOSED_SCHEMA_REFERENCE_RESOLUTION_ATTEMPTED_REMOTE_FETCH
R1_RETRY=false
R2_DECISION_RECORDED=false
R2_VALIDATION_AUTHORIZED=false
PUBLIC_FETCH_AUTHORIZED=false
MODEL_SESSION_EXECUTION_AUTHORIZED=false
TECHNICAL_REUSE_RUN_AUTHORIZED=false
```

## 2. Root cause

The role Schema relative reference resolves to:

`https://titmas.cn/schemas/session-response.base.schema.v0.1.json`

The target base Schema declares:

`https://titmas.cn/schemas/ce-g13-session-response.base.schema.v0.1.json`

This is a canonical URI identity mismatch. R1 additionally relied on deprecated resolver behavior
that may perform remote retrieval after a local-store miss.

## 3. Options

### Option A — URI alignment plus no-remote resolver

Recommended.

1. Keep the five relative `$ref` values unchanged.
2. Change only the base Schema `$id` to the URI produced by those references.
3. Update only its package-manifest byte count and SHA-256 entry.
4. Replace the ephemeral R1 validation mechanism with a local Registry whose retrieval callback
   always rejects unknown resources; do not use `RefResolver`.
5. Run exactly one new R2 offline validation after a qualifying Decision review.

This fixes the contract identity and independently prevents remote fallback.

### Option B — Inline the common Schema into five role Schemas

Rejected. It duplicates shared constraints, expands the mutation surface and weakens a single
canonical common definition.

### Option C — Permit network Schema retrieval

Rejected. It violates the offline contract and makes validation depend on mutable public state.

### Option D — Ignore role-instance validation

Rejected. Meta-valid Schemas alone do not prove cross-file references or role specialization.

## 4. Exact proposed mutation

Within `commercial-evaluation-ce-g13-offline-contract/`:

1. `session-response.base.schema.v0.1.json`
   - replace only the `$id` URI;
2. `package-manifest.candidate.v0.1.json`
   - update only the base Schema entry `bytes` and `sha256`.

No prompt, role Schema, scoring rule, negative case, execution plan, template or controller text
changes.

## 5. R2 validation contract

R2 must:

- assert the exact 28-file allowlist;
- reject duplicate JSON keys;
- meta-validate all 14 Draft 2020-12 Schemas;
- validate candidates and templates;
- resolve all cross-file references exclusively from an explicit local Registry;
- reject every unknown URI locally without HTTP, HTTPS, DNS or Provider access;
- validate one positive and one wrong-session negative sample per role;
- verify cold-discovery answer-key absence;
- verify the manifest covers and hashes exactly the other 27 files;
- verify 100 scoring points and 28 negative cases;
- produce console-only PASS or FAIL_CLOSED;
- perform no credential read, model request or technical reuse run.

The R2 validator may be ephemeral and outside the repository. It is validation tooling, not a DBA
Runtime or package artifact.

## 6. Commit gate

Only a complete R2 PASS may authorize one path-scoped commit and push containing:

- the exact 28-file package directory;
- the R1 failure report;
- this R2 Recommendation and its qualifying `qwen3.7-max` review;
- the independent R2 Decision and its qualifying `qwen3.7-max` review.

If R2 fails, preserve it as a distinct failure, commit nothing and do not patch or retry.

## 7. Non-authorizations

This Recommendation does not authorize:

- R2 mutation or validation before a Decision;
- public HTTP, DNS or Schema retrieval;
- credential reads;
- CE-G13 role sessions or any other model request after Decision review;
- a technical reuse run;
- Agent, Runtime, Entity, Capability, Permission or Evidence Truth creation;
- customer adoption, market demand, certification, commercial offering or production claims;
- release, deployment, PR, merge, Authority or Ownership changes.

```text
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```
