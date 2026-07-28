---
document_id: DBA-TITMAS-CE-G13-EXECUTION-AUTHORIZATION-RECOMMENDATION-0.1
title: TITMAS CE-G13 Execution Authorization Recommendation v0.1
title_zh: TITMAS CE-G13 执行授权建议 v0.1
version: 0.1.0
status: recommendation-only-decision-required
maturity: Development
maturity_scope: one-bounded-agent-customer-validation-attempt
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Execution Authorization Recommendation v0.1

## 1. Recommendation

Select **Option A — authorize one staged, fail-closed CE-G13 public Agent-customer discovery and
bounded reuse validation attempt under a separate Human Decision**.

```text
RECOMMENDED_OPTION=A
RECOMMENDED_ACTION=AUTHORIZE_ONE_STAGED_CE_G13_EXECUTION_ATTEMPT
RECOMMENDATION_IS_DECISION=false
CE_G13_EXECUTION_AUTHORIZED=false
PUBLIC_FETCHES_EXECUTED=0
AGENT_SESSIONS_EXECUTED=0
TECHNICAL_REUSE_RUNS=0
```

The attempt is recommended because it tests the current commercial bottleneck: whether an AI Agent
that is not given internal repository context can discover TITMAS from its public website, understand
its architecture, produce a bounded reuse plan and recommend or reject it with correct authority
boundaries.

This is Agent-customer validation, not customer adoption. Model sessions are evaluation roles, not
customer accounts, Digital Entities or Agent instances.

## 2. Why execution is now eligible for a Decision

### 2.1 Prior design and Agent-customer gate

```text
CE_G13_RECOMMENDATION_REFERENCE=TITMAS-CE-G13-PUBLIC-AGENT-CUSTOMER-DISCOVERY-AND-REUSE-VALIDATION-RECOMMENDATION-v0.1.md
CE_G13_RECOMMENDATION_SHA256=07919fdb026f08d6e84da63c6b71060c2f519d607bdf3a1986253d560218ca75
PREDEVELOPMENT_AGENT_CUSTOMER_GATE=QUALIFYING
REVIEW_MODEL=qwen3.7-max
REVIEW_VERDICT=RECOMMENDED
REVIEW_CONFIDENCE=0.95
REVIEW_BLOCKERS=0
REVIEW_CORRECTIONS=0
```

The prior review concluded that the website-first delta, five-role separation, reuse validation and
fail-closed criteria were sound. It did not authorize execution.

### 2.2 Immutable base contract

```text
BASE_DIRECTORY=commercial-evaluation-ce-g13-offline-contract
BASE_FILES=28
BASE_PACKAGE_MANIFEST_SHA256=be7b0db4f0f349f8898f749e8ee0f4bd6a3407c79acbe33b415da081ff9ea9ed
BASE_PACKAGE_COMMIT=bdfdfb076aaa129af50d5e2ecdec7cc87adff487
BASE_PACKAGE_REMOTE_VERIFIED=true
BASE_R2_VALIDATION=PASS
BASE_R2_CHECKS=94
BASE_R2_SCHEMAS=14
BASE_R2_NEGATIVE_CASES=28
```

### 2.3 Immutable input-binding supplement

```text
SUPPLEMENT_DIRECTORY=commercial-evaluation-ce-g13-input-binding-supplement
SUPPLEMENT_FILES=16
SUPPLEMENT_PACKAGE_MANIFEST_SHA256=5a67190aef647c1881d764806b59e0d9b7ed3b9438145a9eed8c9eecc16a2b34
SUPPLEMENT_PACKAGE_COMMIT=853f86395ba687929da5f45024486f046866d01d
SUPPLEMENT_PACKAGE_REMOTE_VERIFIED=true
SUPPLEMENT_VALIDATION=PASS
SUPPLEMENT_CHECKS=16
SUPPLEMENT_SCHEMAS=6
SUPPLEMENT_INSTANCES=6
SUPPLEMENT_ROLE_SAMPLES=5
SUPPLEMENT_NEGATIVE_CASES=32
```

The supplement binds exact sanitized public text, exact secret-free request payloads, S04's
validated reuse-plan input, S05's ordered S01–S04 inputs and the exact 26-file future result surface.

### 2.4 Readiness conclusion

```text
CONTRACT_INPUTS_COMPLETE=true
OFFLINE_SCHEMA_AND_NEGATIVE_CONTROLS_PASS=true
EXECUTION_DECISION_CANDIDATE_ELIGIBLE=true
EXECUTION_ALREADY_AUTHORIZED=false
WEBSITE_AVAILABILITY_AT_EXECUTION_TIME=NOT_ASSESSED
AGENT_CUSTOMER_RESULT=NOT_ASSESSED
TECHNICAL_REUSE_RESULT=NOT_ASSESSED
```

Offline PASS proves contract readiness only. It does not predict the live result.

## 3. Options

### Option A — one staged execution attempt

Recommended. One Human Decision may authorize exactly one attempt with four stop-bound stages.

### Option B — run only the five model sessions against local website files

Rejected. This would not test public discovery, availability, same-origin lineage or website-only
reuse and could leak hidden local context.

### Option C — authorize repeated attempts until PASS

Rejected. Repetition would convert a validation into outcome shopping. Any failed attempt must be
preserved; a new attempt requires a new Recommendation and Decision.

### Option D — defer until the site is declared production-ready

Rejected. CE-G13 is explicitly a Development commercial-evaluation gate. It is designed to expose
public-entry failures before Production Ready, not after.

## 4. Exact attempt boundary

### 4.1 Frozen source and model

```text
INITIAL_URL=https://redcrag.cn/
INITIAL_URL_COUNT=1
SAME_ORIGIN_ONLY=true
SAME_ORIGIN_REDIRECTS_ONLY=true
REQUESTED_MODEL=qwen3.7-max
RETURNED_MODEL_MUST_EQUAL=qwen3.7-max
PROVIDER=ALIBABA_CLOUD_MODEL_STUDIO
CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
CREDENTIAL_VALUE_PERSISTED=false
```

The exact base execution plan still names `https://redcrag.cn/`. A redirect to another origin,
including a future `titmas.cn` migration, fails this attempt closed. Changing the origin requires a
new contract version and is not silently repaired during execution.

### 4.2 Caps

```text
HTTP_GET_REQUESTS_MAX=16
RAW_PUBLIC_BYTES_MAX=3000000
AGENT_SESSIONS=5
MODEL_REQUESTS_MAX=5
MODEL_REQUESTS_PER_SESSION_MAX=1
TECHNICAL_REUSE_RUNS_MAX=1
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_EXTRACTIONS=0
JSON_REPAIRS=0
RUNTIME_STARTS=0
AGENT_INSTANCES=0
ENTITY_INSTANCES=0
CAPABILITY_INSTANCES=0
PERMISSION_GRANTS=0
EVIDENCE_TRUTH_OBJECTS=0
```

### 4.3 Controller boundary

The Decision may authorize an ephemeral controller process to execute the frozen procedure. No
controller source, network client, Runtime or Agent framework is added to DBA. The controller may:

- read only the immutable base and supplement contracts;
- read `DASHSCOPE_API_KEY` only for the five exact model requests;
- fetch only the one root and discovered same-origin resources within the frozen budget;
- write only the exact attempt directory and its 26 declared output files;
- run at most one clean, synthetic, read-only technical reuse check if its preconditions pass.

It may not modify the website, GitHub, DBA canonical files, DBOS, SAEE, credentials or prior failure
records.

## 5. Staged execution

### Stage E0 — immutable baseline and public retrieval

1. Verify both package manifest hashes and their remote commits.
2. Verify exact model availability without making a model request.
3. Fetch `https://redcrag.cn/` and discovered same-origin resources.
4. Enforce identity encoding, MIME, strict UTF-8, byte ceiling, same-origin and lineage rules.
5. Persist retrieval receipt, public snapshot and sanitized public input bundle.

Stop before any model request if E0 fails.

### Stage E1 — three discovery and reuse sessions

Run, in order:

1. `CE-G13-S01` — cold discovery;
2. `CE-G13-S02` — architecture comprehension;
3. `CE-G13-S03` — website-only reuse planning.

Each uses its exact persisted input envelope and one exact `qwen3.7-max` request. Stop before S04 if
any response is not direct JSON, fails its Schema, mismatches the model, uses hidden context or
violates a hard boundary.

### Stage E2 — recommendation and non-match audit

1. Validate the S03 reuse plan deterministically.
2. Bind the persisted validation result into S04.
3. Run `CE-G13-S04` — Agent recommendation.
4. Bind exact S01–S04 response hashes into S05.
5. Run `CE-G13-S05` — boundary and non-match audit.

Stop before technical reuse if S04 or S05 fails.

### Stage E3 — optional synthetic technical reuse

Execute at most one technical reuse check only when:

- S03 selected a public-safe First Run;
- every selected reference was present in the frozen public snapshot;
- the deterministic reuse validation passed;
- no private repository, secret, Runtime or Agent framework is required.

A failed or unavailable technical check is preserved. It is never replaced by a model opinion.

## 6. Exact future output

The attempt output directory must contain exactly 26 files:

- one README;
- one execution-baseline receipt;
- public snapshot, retrieval receipt and sanitized public input bundle;
- five model-input envelopes;
- five request-capture records;
- five direct session responses;
- one reuse-plan validation result;
- one technical-reuse receipt, including `NOT_EXECUTED` when ineligible;
- one failure ledger;
- one composite result;
- one human-readable report;
- one output manifest that hashes the other 25 files and excludes itself.

No file may be deleted, renamed, overwritten or reformatted after hashing.

## 7. Outcome policy

Runtime execution statuses:

```text
NOT_EXECUTED
PASS
FAIL_CLOSED
```

Governance may later interpret a preserved `FAIL_CLOSED` result as
`CONDITIONAL_REMEDIATION_REQUIRED`; this is not an execution status and does not rewrite failure.

`PASS_AGENT_DISCOVERY_AND_BOUNDED_REUSE_VALIDATED` requires:

- E0 public snapshot and lineage PASS;
- `5/5` exact-model, direct-JSON, Schema-valid sessions;
- S01 identifies TITMAS without the name or filenames being provided;
- S02 separates DBA, DBOS, SAEE and Governance Decision;
- S03 produces all six required reuse elements without GitHub dependency;
- deterministic reuse validation PASS;
- S04 gives an evidence-linked bounded recommendation;
- S05 rejects production, certification, automatic authority and at least two non-matching cases;
- critical boundary failures `0`;
- no retry, fallback, substitution, extraction, repair or hidden dependency;
- optional E3 either PASS or correctly recorded `NOT_EXECUTED` under its frozen eligibility rule.

Any critical failure produces `FAIL_CLOSED`.

## 8. Valid commercial interpretation

If PASS:

> In one bounded, single-provider, website-first evaluation, isolated AI-agent roles discovered
> TITMAS, understood its responsibility boundaries and produced a technically valid public-safe
> reuse recommendation.

Even on PASS:

```text
REAL_CUSTOMERS=0
CUSTOMER_ADOPTION_VERIFIED=false
MARKET_DEMAND_VERIFIED=false
EXTERNAL_ENDORSEMENT=false
CROSS_PROVIDER_GENERALITY=false
GLOBAL_DISCOVERABILITY=false
CONTINUOUS_AVAILABILITY=false
COMMERCIAL_OFFERING=false
CONTRACT=false
SLA=false
CERTIFICATION=false
STANDARD_READY=false
PRODUCTION_READY=false
```

The commercial value is narrower: PASS would prove one machine-customer discovery and reuse path;
FAIL_CLOSED would identify the earliest public-entry, comprehension, reuse or boundary defect.

## 9. Decision prerequisites

A future Human Decision may authorize Option A only if:

1. this Recommendation receives one qualifying exact `qwen3.7-max` direct-JSON review;
2. requested and returned model identities match;
3. review verdict is `RECOMMENDED` or `CONDITIONALLY_RECOMMENDED`;
4. confidence is at least `0.90`;
5. blockers and required corrections are empty;
6. the Recommendation and review are committed and remote verified;
7. base and supplement hashes still match;
8. the Decision repeats every request, byte, output and side-effect cap;
9. the Decision names `zhangbin` as Human Decision Authority;
10. the Decision authorizes no retry and no commercial maturity elevation.

## 10. Stop conditions

Stop before a Decision if:

- either package or validation-result hash drifts;
- the Recommendation review is not exact `qwen3.7-max` direct JSON;
- review confidence is below `0.90`, or any blocker/correction remains;
- the public origin, model, request caps or output set would be relaxed;
- a Runtime, Agent, Entity, Capability, Permission or Evidence Truth would be created;
- a model session would be described as a customer, adoption, demand or endorsement;
- release, offering, certification, Standard Ready, Production Ready, Authority or Ownership would
  change.

## 11. Non-authorizations

This Recommendation does not authorize the Decision or the attempt. It does not authorize public
HTTP, credential access, model requests beyond its separately governed review, technical reuse,
Runtime, Agent, Entity, Capability, Permission, Evidence Truth, website/GitHub changes, DBOS/SAEE
changes, customer claims, outreach, implementation, deployment, release, offering, pricing,
contract, SLA, certification, Standard Ready, Production Ready, Authority or Ownership changes.

```text
Recommendation != Decision
Decision != Execution
Evidence != Truth
Evaluation != Authority
Capability != Permission
Contract != Implementation
```
