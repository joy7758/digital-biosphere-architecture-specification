---
document_id: DBA-TITMAS-CE-G14-PROVIDER-B-EVIDENCE-BINDING-RECOMMENDATION-0.1
title: TITMAS CE-G14 Provider B Evidence-binding Recommendation v0.1
title_zh: TITMAS CE-G14 Provider B 证据绑定建议 v0.1
version: 0.1.0
status: recommendation-only
maturity: Development
owner_ref: zhangbin
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G14 Provider B Evidence-binding Recommendation v0.1

## 1. Question

Can existing immutable DBA evidence satisfy the CE-G14 prerequisite for one exact, distinct
Provider B candidate without issuing another live model request?

## 2. Parent Recommendation

```text
PARENT_REFERENCE=TITMAS-CE-G14-CROSS-PROVIDER-AND-CLEAN-TECHNICAL-REUSE-RECOMMENDATION-v0.1.md
PARENT_SHA256=5cd54f23e6150545a1b5c667faf51c2b63c21d15c4b4cf8d2376668dfbe3e603
PARENT_COMMIT=01812738eae7608417103a2ff91db1af303ad25d
PARENT_REMOTE_VERIFIED=true
CE_G14_EXECUTION_AUTHORIZED=false
```

The parent requires a distinct Provider B, one exact model, a recent availability receipt,
separate credential identifier and endpoint family, plus a fixed cost ceiling before any CE-G14
execution Decision.

## 3. Candidate evidence

PRE-72 provides the strongest current matching evidence:

```text
EVIDENCE_COMMIT=5894d589216877df9c7d3dba9145fe0b9f19d232
RECEIPT_REFERENCE=commercialization-standards-p0-security-and-platform-provider-capability-evidence/pre72-execution-receipt.v0.1.json
RECEIPT_SHA256=12c00a10d468f21f07088a0dd5620f7c33dbbd5146c516bacb3e204022b51e2e
SESSION_RESULTS_REFERENCE=commercialization-standards-p0-security-and-platform-provider-capability-evidence/pre72-sanitized-session-results.v0.1.json
SESSION_RESULTS_SHA256=60f4d44ab6aa01c460b4be166f68758f0575e375dda285bec6103d7aa6c5a2aa
RESULT_REFERENCE=commercialization-standards-p0-security-and-platform-provider-capability-evidence/PRE-72-BOUNDED-STRUCTURED-OUTPUT-PREFLIGHT-RESULT-v0.1.md
RESULT_SHA256=55f1b610d001582c7e786f054485a3d50474287700a5fa469e82fed33c734643
EXECUTED_AT=2026-07-27T15:06:50+08:00
```

Candidate binding:

```text
PROVIDER_B=BAIDU_QIANFAN
ENDPOINT_B=https://qianfan.baidubce.com/v2/chat/completions
MODEL_B=ernie-4.5-turbo-20260402
CREDENTIAL_IDENTIFIER_B=QIANFAN_API_KEY
```

The three Qianfan sessions each recorded:

- HTTP `200`;
- requested model exactly equals returned model `ernie-4.5-turbo-20260402`;
- direct single JSON object PASS;
- frozen response Schema PASS;
- exact session binding PASS;
- authority boundary PASS.

Aggregate evidence:

```text
QIANFAN_SESSIONS=3/3
EXACT_MODEL_MATCH=3/3
DIRECT_JSON=3/3
SCHEMA_PASS=3/3
SESSION_BINDING_PASS=3/3
AUTHORITY_BOUNDARY_PASS=3/3
RETRY=0
FALLBACK=0
SUBSTITUTION=0
EXTRACTION=0
REPAIR=0
SECRET_PRINT_PERSIST_EXPOSE=0
```

## 4. Crosswalk to CE-G14 prerequisites

| CE-G14 prerequisite | PRE-72 evidence | Disposition |
|---|---|---|
| distinct Provider | Baidu Qianfan versus Alibaba Cloud Model Studio | `PASS` |
| distinct endpoint family | `qianfan.baidubce.com/v2` versus Alibaba compatible endpoint | `PASS` |
| distinct credential identifier | `QIANFAN_API_KEY` versus `DASHSCOPE_API_KEY` | `PASS` |
| exact model binding | requested and returned `ernie-4.5-turbo-20260402`, 3/3 | `PASS` |
| direct JSON | 3/3 | `PASS` |
| frozen Schema | 3/3 | `PASS` |
| authority boundary | 3/3 | `PASS` |
| recent evidence | executed on 2026-07-27 | `PASS_IF_USED_WITHIN_48_HOURS` |
| actual CE-G14 prompt compatibility | not tested | `MUST_REMAIN_UNPROVEN_BEFORE_CE_G14` |
| current credential value availability | not checked and must not be read by this Recommendation | `DECISION_PRECONDITION` |
| four-session cost estimate | usage was intentionally not persisted | `DECISION_PRECONDITION` |

## 5. Options

### Option A — bind PRE-72 as the Provider B availability candidate

Recommended.

It reuses exact, recent, immutable evidence and avoids a redundant live preflight. It does not
claim that PRE-72 proves CE-G14 prompt success.

### Option B — issue a new Provider B availability request now

Rejected because the parent Recommendation has not authorized model requests and qualifying
evidence already exists.

### Option C — bind legacy DeepSeek evidence

Rejected because relevant records include requested/returned model drift
(`deepseek-chat` versus `deepseek-v4-flash`) or other scope-specific failures. They are useful
historical evidence but do not satisfy the exact-model prerequisite as cleanly as PRE-72.

### Option D — treat Provider A and B as the same Alibaba endpoint

Rejected because two models behind one provider family do not establish the required Provider
independence.

## 6. Exact recommendation

```text
RECOMMENDED_OPTION=A
PROVIDER_B_BINDING_CANDIDATE=BAIDU_QIANFAN
MODEL_B_BINDING_CANDIDATE=ernie-4.5-turbo-20260402
PROVIDER_B_EVIDENCE_MAX_AGE_HOURS=48
NEW_PROVIDER_B_PREFLIGHT_RECOMMENDED=false
NEW_MODEL_REQUEST_AUTHORIZED=false
CE_G14_EXECUTION_DECISION_READY=false
```

One future CE-G14 Decision packet may use this binding only if, at Decision time:

1. receipt, session-results and result hashes still match;
2. evidence commit exists in the local immutable commit graph;
3. elapsed time since `EXECUTED_AT` does not exceed 48 hours;
4. the `QIANFAN_API_KEY` identifier is configured, without recording or printing the value;
5. a four-session cost estimate is present and the total fixed cap is at most CNY 500;
6. the exact CE-G14 prompts, Schemas, input hash, request caps and no-retry rules are bound;
7. the Decision receives a separate qualifying review.

If the evidence is older than 48 hours before Decision, this binding expires. The next action is a
separate bounded Provider B availability-preflight Recommendation, not a silent live request.

## 7. Interpretation

The PRE-72 evidence proves only that three exact Qianfan requests satisfied a bounded structured
output preflight on `2026-07-27`. It does not prove:

- current or long-term Provider availability;
- CE-G14 prompt or Schema success;
- Provider support or service-level agreement;
- customer adoption, market demand or general provider support;
- commercial offering, certification, Standard Ready or Production Ready.

## 8. Non-authorizations

This Recommendation does not authorize:

- CE-G14 execution or Decision adoption;
- credential read, model request, public artifact fetch or technical reuse;
- Provider onboarding, account change or cost commitment;
- website, DBOS, SAEE or CE-G13 result changes;
- Runtime, Agent, Entity, Capability, Permission or Evidence Truth;
- PR, merge, release, deployment, offering, certification, Standard Ready or Production Ready;
- Authority or Ownership changes.

```text
Recommendation != Decision
Decision != Execution
Evidence != Truth
Evaluation != Authority
Capability != Permission
```
