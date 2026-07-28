---
document_id: DBA-TITMAS-CE-G14-CROSS-PROVIDER-AND-CLEAN-TECHNICAL-REUSE-RECOMMENDATION-0.1
title: TITMAS CE-G14 Cross-provider and Clean Technical-reuse Recommendation v0.1
title_zh: TITMAS CE-G14 跨供应商与干净技术复用建议 v0.1
version: 0.1.0
status: recommendation-only
maturity: Development
owner_ref: zhangbin
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G14 Cross-provider and Clean Technical-reuse Recommendation v0.1

## 1. Recommendation question

If an AI Agent developer or recommending Agent asks whether TITMAS can be discovered, correctly
bounded and technically reused outside one model-provider path, should a bounded follow-up
validation be recommended?

## 2. Current evidence

CE-G13 is preserved at immutable result commit:

```text
CE_G13_RESULT_COMMIT=7a20c77bff931380fe109987972d3e43c9774bd3
CE_G13_OUTPUT_FILES=26
CE_G13_OUTPUT_MANIFEST_SHA256=f3abd3fc3cb29ec52e2920639e220af3900cfb91d96bd083fc4c7702ee1e4700
CE_G13_COMPOSITE_RESULT_SHA256=a9c7b5726fe8ebcc221046863a239be13f3eab959f5c9cb9867172a63400bed7
CE_G13_SCORE=100/100
CE_G13_AGENT_SESSIONS=5/5
CE_G13_PROVIDER=ALIBABA_CLOUD_MODEL_STUDIO
CE_G13_MODEL=qwen3.7-max
CE_G13_REUSE_PLAN_VALIDATION=PASS_7_OF_7
CE_G13_TECHNICAL_REUSE_STATUS=NOT_EXECUTED
CE_G13_TECHNICAL_REUSE_RUNS=0
```

CE-G13 proves one exact machine-customer discovery, comprehension and bounded reuse-planning path.
It does not prove cross-provider generality. It also does not prove the published wheel and
synthetic fixture can be acquired and used in a clean environment because the 16-GET public
snapshot budget was exhausted before both technical artifacts were separately captured.

## 3. Gaps that matter to an Agent customer

### G1 — provider dependence

All five CE-G13 sessions used exact `qwen3.7-max`. An Agent recommender still cannot distinguish
TITMAS-specific discoverability from one provider/model's interpretation behavior.

### G2 — plan versus reuse

The CE-G13 reuse plan passed seven deterministic checks, but no wheel was installed and no
validator command ran. Planning evidence is not execution evidence.

### G3 — public artifact acquisition

The public instructions name:

```text
WHEEL_URL=https://github.com/joy7758/digital-biosphere-architecture-specification/releases/download/v0.1-developer-preview/digital_biosphere_os_preview-0.1.0.dev0-py3-none-any.whl
DOCUMENTED_WHEEL_SHA256=edf92e548860384b1416a612a7e319e0d994bb324f8621847d0d154624ae8f09
FIXTURE_URL=https://redcrag.cn/examples/titmas-first-run/entity-object.synthetic.v0.1.json
```

CE-G14 must acquire both as explicit public inputs. It may not substitute a hidden local wheel,
repository file, cache or unrecorded fixture.

## 4. Options

### Option A — one paired provider-consistency gate plus one clean synthetic reuse gate

Recommended.

It directly tests the two unresolved CE-G13 gaps without expanding TITMAS into an Agent platform,
Runtime, certification system or commercial product.

### Option B — provider-consistency review only

Rejected because it would leave `TECHNICAL_REUSE_STATUS=NOT_EXECUTED`.

### Option C — clean technical reuse only

Rejected because it would leave `CROSS_PROVIDER_GENERALITY=false`.

### Option D — add more TITMAS features first

Rejected because current uncertainty concerns discoverability and reuse of the existing public
surface, not missing platform features.

## 5. Exact recommended candidate

```text
RECOMMENDED_OPTION=A
RECOMMENDED_ACTION=PREPARE_ONE_BOUNDED_CE_G14_EXECUTION_DECISION_PACKET
CE_G14_EXECUTION_AUTHORIZED=false
PROVIDER_B_EXACT_BINDING_REQUIRED=true
PUBLIC_ARTIFACT_FETCH_AUTHORIZED=false
MODEL_REQUESTS_AUTHORIZED=false
TECHNICAL_REUSE_AUTHORIZED=false
```

This Recommendation prepares a candidate only. It does not authorize the candidate execution.

## 6. Candidate validation design

### 6.1 Frozen model input

Reuse the exact sanitized public bundle already preserved by CE-G13:

```text
INPUT_REFERENCE=commercial-evaluation-ce-g13-execution-attempt-001/sanitized-public-input-bundle.v0.1.json
INPUT_SHA256=fa2786883e58f02df6e9677de5d215a623493932664e47be2a55a6e7ac8f328b
PUBLIC_RESOURCES=16
SANITIZED_BYTES=440364
```

No website re-fetch is required for model sessions. Both providers must receive the same frozen
input bytes, the same role prompts and the same output Schemas.

### 6.2 Provider binding

The future Decision must bind:

```text
PROVIDER_A=ALIBABA_CLOUD_MODEL_STUDIO
MODEL_A=qwen3.7-max
PROVIDER_B=TO_BE_BOUND_TO_A_DISTINCT_PROVIDER
MODEL_B=TO_BE_BOUND_TO_ONE_EXACT_AVAILABLE_MODEL
```

Provider B must use a different provider, credential identifier and endpoint family. Provider B
availability must be verified before execution authorization. No model alias, silent fallback or
provider substitution is allowed.

The future Decision must bind a recent exact-model availability receipt for Provider B, including
provider, exact model, endpoint family, observed time, HTTP/direct-JSON result and zero
substitution. If no qualifying receipt exists, CE-G14 remains blocked and needs a separate bounded
preflight Recommendation; the CE-G14 execution may not create an undeclared availability request.

The future Decision must also bind one exact monetary ceiling no greater than:

```text
MAX_TOTAL_PROVIDER_COST_CNY=500
```

or an explicitly converted equivalent fixed before execution. If the estimated four-session cost
exceeds the bound, execution stops before the first model request. Provider onboarding,
credentialing and account changes are outside CE-G14.

### 6.3 Four sequential Agent-customer sessions

Each provider runs the same two bounded roles:

1. `COLD_DISCOVERY_AND_POSITIONING`
2. `BOUNDARY_AND_REUSE_RECOMMENDATION`

Candidate cap:

```text
PROVIDERS=2
SESSIONS_PER_PROVIDER=2
TOTAL_MODEL_REQUESTS_MAX=4
SEQUENTIAL_EXECUTION=true
DIRECT_JSON_REQUIRED=true
EXACT_MODEL_RETURN_REQUIRED=true
MAX_INPUT_BYTES_PER_SESSION=600000
MAX_OUTPUT_TOKENS_PER_SESSION=4096
MAX_TOTAL_REPORTED_INPUT_TOKENS=1000000
MAX_TOTAL_REPORTED_OUTPUT_TOKENS=16384
REQUEST_TIMEOUT_SECONDS=180
MODEL_SESSION_STAGE_WALL_CLOCK_SECONDS=900
RETRY=0
FALLBACK=0
SUBSTITUTION=0
EXTRACTION=0
REPAIR=0
```

Both providers must:

- identify TITMAS as trustworthy multi-agent infrastructure rather than an Agent framework;
- distinguish DBA, DBOS, SAEE, Governance Decision and Digital Entity roles;
- preserve `Evidence != Truth`, `Evaluation != Authority` and `Capability != Permission`;
- recognize technical validator PASS as bounded structural/governance evidence;
- refuse to interpret the public materials as customer adoption, certification, production
  readiness or a purchasable offering;
- state whether they would recommend a bounded offline evaluation to a matching Agent developer.

Cross-provider consistency is PASS only if all four responses are direct JSON, Schema valid and
boundary valid, and both providers reach a compatible bounded recommendation. Compatible does not
require identical wording or an identical confidence score.

### 6.4 Two public technical artifact GETs

The future execution may request exactly:

1. the public-safe wheel URL;
2. the same-origin synthetic fixture URL.

These two GETs are also the only artifact liveness checks. No HEAD request, probe request, mirror,
cached replacement or third GET is allowed. A non-200 response, an unapproved redirect, a wheel
hash mismatch, invalid fixture JSON or unavailable URL stops closed and requires a new
Recommendation rather than silent substitution.

For each request it must preserve:

- source URL and final URL;
- HTTP status and redirect chain;
- content type, byte count and SHA-256;
- retrieval time and request identifier;
- absence of Authorization headers, cookies and customer data.

The wheel bytes must match the documented SHA-256. The fixture hash must be frozen from the newly
captured public bytes before validation begins.

### 6.5 Clean technical reuse

Only after both artifacts are captured:

```text
create fresh temporary directory
create fresh Python >=3.11 virtual environment
install the captured local wheel with --no-index
copy the captured synthetic fixture into the temporary directory
record the fixture pre-run SHA-256
execute dbos-validate entity.json exactly once
record exit code and sanitized stdout/stderr
record the fixture post-run SHA-256
destroy the temporary environment after receipt creation
```

The clean technical stage has a 600-second wall-clock cap. The total CE-G14 execution wall-clock
cap is 1800 seconds, including artifact capture, four model sessions and the technical stage.

PASS requires:

- installation exit code `0`;
- `dbos-validate` exit code `0`;
- pre-run and post-run fixture hashes are identical;
- output contains no credential or local private path;
- no network access occurs after the two captured artifacts;
- no Runtime, Agent, Entity instance, Capability instance, Permission, Evidence Truth or customer
  workload is created.

The clean run validates only one synthetic local structural/governance reuse path.

## 7. Candidate success criteria

```text
PUBLIC_ARTIFACT_GETS=2/2
PROVIDER_MODEL_SESSIONS=4/4
DIRECT_JSON_AND_SCHEMA_VALID=4/4
BOUNDARY_VALID=4/4
DISTINCT_PROVIDERS_WITH_PASS=2/2
CROSS_PROVIDER_BOUNDED_RECOMMENDATION_CONSISTENT=true
CLEAN_TECHNICAL_REUSE_RUNS=1
CLEAN_TECHNICAL_REUSE_STATUS=PASS
RETRY_FALLBACK_SUBSTITUTION_EXTRACTION_REPAIR=0
CRITICAL_BOUNDARY_FAILURES=0
```

Any failure must remain visible and stop closed. Provider-session PASS must not compensate for
technical-reuse failure, and technical-reuse PASS must not compensate for provider inconsistency.

## 8. Result meaning

If all candidate gates pass, the strongest allowed claim is:

> Two independently bound model providers consistently discovered and bounded the same frozen
> TITMAS public materials, and one newly captured public wheel/fixture pair completed one clean,
> synthetic, offline validator reuse path.

It would still not prove:

```text
CUSTOMER_ADOPTION_VERIFIED=false
MARKET_DEMAND_VERIFIED=false
GENERAL_PROVIDER_SUPPORT=false
REAL_CUSTOMER_WORKLOAD_VERIFIED=false
CONTINUOUS_AVAILABILITY_VERIFIED=false
COMMERCIAL_OFFERING=false
CERTIFICATION=false
STANDARD_READY=false
PRODUCTION_READY=false
```

## 9. Required future governance

Before any CE-G14 execution:

1. exact Provider B and model availability must be bound;
2. exact Provider B availability evidence and the no-greater-than-CNY-500 total cost ceiling must
   be bound;
3. this Recommendation needs one independent Agent-customer review;
4. a separate Human Decision by `zhangbin` must bind exact inputs, prompts, Schemas, request caps,
   public URLs, hash rules, clean-environment procedure, outputs and fail-closed conditions;
5. that Decision needs a qualifying independent review;
6. execution must use a new isolated worktree and a new output directory;
7. results and failures must be immutable and committed separately from later status reconciliation.

## 10. Non-authorizations

This Recommendation does not authorize:

- CE-G14 execution, public fetch, model request or technical run;
- selection or onboarding of Provider B;
- changes to the website, DBOS, SAEE or the CE-G13 result package;
- Runtime, Agent, Entity, Capability, Permission or Evidence Truth;
- customer outreach, customer adoption, market-demand claims or a commercial offer;
- PR, merge, release, deployment, certification, Standard Ready or Production Ready;
- Authority or Ownership changes.

```text
Recommendation != Decision
Decision != Execution
Evidence != Truth
Evaluation != Authority
Capability != Permission
```
