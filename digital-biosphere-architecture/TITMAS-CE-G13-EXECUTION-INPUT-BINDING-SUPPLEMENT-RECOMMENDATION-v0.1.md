---
document_id: DBA-TITMAS-CE-G13-EXECUTION-INPUT-BINDING-SUPPLEMENT-RECOMMENDATION-0.1
title: TITMAS CE-G13 Execution Input Binding Supplement Recommendation v0.1
title_zh: TITMAS CE-G13 执行输入绑定补充契约建议 v0.1
version: 0.1.0
status: recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: ce-g13-offline-input-binding-and-output-allowlist-supplement-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
commercial_language: Exploration
authority_effect: none
---

# TITMAS CE-G13 Execution Input Binding Supplement Recommendation v0.1

## 1. Recommendation

Select **Option A — do not authorize CE-G13 execution yet; preserve the validated 28-file
offline contract package unchanged and prepare one bounded, offline input-binding supplement
contract**.

```text
CURRENT_EXECUTION_RECOMMENDATION=NOT_RECOMMENDED_INPUT_BINDING_INCOMPLETE
SUPPLEMENT_PREPARATION_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
CE_G13_EXECUTION_AUTHORIZED=false
PUBLIC_FETCHES=0
MODEL_REQUESTS=0
TECHNICAL_REUSE_RUNS=0
```

The supplement must bind the exact sanitized public content and every ordered upstream input to
each future model request. It must also freeze one complete execution-output allowlist. Only after
the supplement passes a separately authorized offline validation may a new Recommendation assess
whether CE-G13 execution is ready for an independent Human Decision.

This Recommendation is not that Decision and does not authorize preparation, validation or
execution of the supplement.

## 2. Agent-customer recommendation gate

If a potential AI-agent customer asked whether TITMAS should run the current CE-G13 public
discovery and reuse validation now, the answer would be:

`NOT_RECOMMENDED_INPUT_BINDING_INCOMPLETE`.

Reasons:

1. the public snapshot manifest records resource metadata and raw-content hashes but no persisted
   sanitized content that can reconstruct what a model saw;
2. the request-capture contract binds a prompt hash, snapshot-manifest hash and response hash, but
   not the exact assembled request body or its ordered input components;
3. S04 depends on the validated reuse-plan result and S05 depends on four prior responses, while
   those upstream inputs have no per-request binding in the current capture contract;
4. the future execution output list omits the five request-capture records required by the
   controller procedure and composite result;
5. a manifest hash alone cannot prove that two runs admitted identical text, ordering,
   normalization or response Schema bytes.

The current design remains valuable and is not rejected. The correct fix is a narrow supplement,
not a new platform, Runtime, Agent framework or replacement contract package.

## 3. Evidence inspected

The following current artifacts were inspected at governance commit
`8a8fc840def61cadef132ebc2d0219aba7a19a82`:

- `commercial-evaluation-ce-g13-offline-contract/public-snapshot-manifest.schema.v0.1.json`;
- `commercial-evaluation-ce-g13-offline-contract/request-capture-contract.schema.v0.1.json`;
- `commercial-evaluation-ce-g13-offline-contract/controller-procedure.v0.1.md`;
- `commercial-evaluation-ce-g13-offline-contract/execution-plan.candidate.v0.1.json`;
- five immutable role prompts and five role response Schemas;
- `commercial-evaluation-ce-g13-offline-contract/reuse-plan-validation-result.schema.v0.1.json`;
- `commercial-evaluation-ce-g13-offline-contract/technical-reuse-receipt.schema.v0.1.json`;
- `commercial-evaluation-ce-g13-offline-contract/composite-result.schema.v0.1.json`;
- `commercial-evaluation-ce-g13-offline-contract/scoring-rules.v0.1.json`;
- `TITMAS-CE-G13-PUBLIC-AGENT-CUSTOMER-DISCOVERY-AND-REUSE-VALIDATION-RECOMMENDATION-v0.1.md`.

The frozen package remains a valid offline contract baseline. This finding is about an execution
input-binding gap that was not covered by the package's existing 94 offline checks.

## 4. Options

### Option A — immutable base plus bounded supplement

Recommended.

- keep the 28-file package and its manifest digest unchanged;
- create a separately versioned offline supplement;
- bind sanitized public bytes, exact ordered request inputs and output paths;
- validate the supplement offline under a new Decision;
- reassess execution readiness only after a complete PASS.

### Option B — silently infer model inputs from the snapshot manifest

Rejected. Resource hashes without persisted admitted content and assembly rules do not reproduce
the actual model input.

### Option C — edit the validated 28-file package in place

Rejected. It would invalidate its package digest, remote baseline and R2 validation evidence.

### Option D — proceed and record only Provider request identifiers

Rejected. A Provider identifier does not prove the submitted prompt, public content, ordering,
Schema or prior-session inputs.

### Option E — store credentials or the unfiltered Provider envelope

Rejected. Reproducibility does not require secrets, hidden reasoning or credential-bearing
headers.

## 5. Required supplement contracts

A future supplement Recommendation and Decision should freeze at least these four data contracts.
Names are candidate names until that later Decision:

### 5.1 Sanitized Public Input Bundle

For every public resource admitted to any model input:

```text
resource_id
source_url
final_url
retrieval_request_id
raw_body_sha256
raw_byte_count
content_type
sanitization_profile
sanitized_text
sanitized_text_sha256
sanitized_byte_count
admission_order
```

Rules:

- `sanitized_text` is the exact UTF-8 text supplied to model-input assembly;
- hashes are computed over persisted file bytes without JSON reformatting after capture;
- no cookie, Authorization header, API key, raw IP, customer data, private file or hidden answer
  key is admitted;
- binary resources may be referenced for technical reuse but cannot be marked as model-input text;
- the aggregate raw retrieval budget remains `3000000` bytes and at most `16` HTTP GET requests;
- public content remains observation, not Evidence Truth.

### 5.2 Model Input Envelope

One envelope per session, with:

```text
session_id
role
provider
requested_model
prompt_reference
prompt_sha256
response_schema_reference
response_schema_sha256
ordered_input_components
sanitized_request_payload
sanitized_request_payload_sha256
source_snapshot_manifest_sha256
sanitized_public_input_bundle_sha256
upstream_result_hashes
```

`ordered_input_components` must bind the exact byte hash, reference and order for:

- S01: root seed, customer problem, cold prompt, response Schema and sanitized public bundle;
- S02: architecture prompt, response Schema and sanitized public bundle;
- S03: reuse-planning prompt, response Schema and sanitized public bundle;
- S04: recommender prompt, response Schema, sanitized public bundle and validated reuse-plan
  result;
- S05: boundary-auditor prompt, response Schema, sanitized public bundle and the exact S01–S04
  response files.

The envelope may persist the direct request JSON after secret removal. It must not persist API
keys, Authorization headers, hidden reasoning or private Provider metadata.

### 5.3 Execution Output Manifest

One non-recursive manifest must declare every permitted execution output path, byte count, SHA-256
and artifact kind. No undeclared result file may be committed.

The future exact output allowlist must include:

1. one execution README;
2. one execution-baseline receipt;
3. one public snapshot manifest;
4. one retrieval receipt;
5. one sanitized public input bundle;
6. five model-input envelopes;
7. five model request-capture records;
8. five direct session-response files;
9. one reuse-plan validation result;
10. one technical-reuse receipt, including `NOT_EXECUTED` when the optional run is not performed;
11. one append-only failure ledger;
12. one composite result;
13. one non-recursive execution-output manifest;
14. one human-readable validation report.

This produces an exact candidate total of `26` result files. A later supplement contract must
either freeze this exact count or explicitly reject this Recommendation with a corrected count
before any execution Decision.

### 5.4 Execution Outcome Policy

The existing composite Schema uses:

```text
NOT_EXECUTED
PASS
FAIL_CLOSED
```

The earlier Recommendation also mentioned
`CONDITIONAL_REMEDIATION_REQUIRED`. The supplement must remove ambiguity by declaring:

- runtime execution results remain only `PASS` or `FAIL_CLOSED`;
- `CONDITIONAL_REMEDIATION_REQUIRED` is a later governance interpretation of a preserved failed
  result, not a third execution status;
- no failed run may be edited, repaired or overwritten into PASS.

## 6. Controller and security rules

Any future execution Recommendation must keep:

```text
PUBLIC_ORIGIN=https://redcrag.cn/
HTTP_GET_REQUESTS_MAX=16
SAME_ORIGIN_ONLY=true
REDIRECTS_SAME_ORIGIN_ONLY=true
RAW_PUBLIC_BYTES_MAX=3000000
AGENT_SESSIONS=5
REQUESTS_PER_SESSION_MAX=1
REQUESTED_MODEL=qwen3.7-max
RETURNED_MODEL_REQUIRED=qwen3.7-max
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_EXTRACTIONS=0
JSON_REPAIRS=0
TECHNICAL_REUSE_RUNS_MAX=1
SYNTHETIC_INPUT_ONLY=true
```

Public retrieval must pass before the first model request. Any transport, same-origin, size,
sanitization, content-binding or output-manifest violation stops the run with zero subsequent
model requests.

For every attempted model session:

- persist its model-input envelope before the Provider call;
- make exactly one request;
- require exact returned model identity `qwen3.7-max`;
- accept only the direct JSON response body;
- validate against the frozen role Schema;
- persist the request-capture record and any failure;
- never retry, extract, repair, fall back or substitute.

The optional synthetic technical reuse run may occur only after S03 and deterministic reuse-plan
validation pass. It must create no Runtime, Agent, Entity, Permission or Evidence Truth.

## 7. Supplement offline validation requirements

Before any new execution-readiness Recommendation, an independently authorized offline validation
must prove:

1. the supplement file allowlist, counts and hashes are exact;
2. all supplement JSON rejects duplicate keys;
3. all Schemas pass Draft 2020-12 meta-validation and local-only reference resolution;
4. one positive and at least one wrong-order or wrong-hash negative instance validates for each
   model-input envelope role;
5. changed sanitized text, changed ordering, changed Schema, changed prior-session response and
   changed prompt each invalidate the bound envelope;
6. secret/header/customer/private-input mutations are rejected;
7. the output manifest rejects missing, extra, renamed, modified or self-hashed files;
8. S04 and S05 upstream dependencies are complete and ordered;
9. execution status mapping is unambiguous and failure-preserving;
10. network, credentials, Provider calls, technical reuse, Runtime, Agent, Entity, Permission and
    Evidence Truth effects remain zero.

## 8. Success and stop conditions

The supplement may qualify for later execution-readiness reassessment only when:

- all supplement contracts and instances pass;
- every model-visible byte is reconstructable from persisted public-safe files;
- every request payload is bound to exact prompt, Schema, snapshot, public bundle and upstream
  result hashes;
- the 26-file output inventory is exact and internally consistent;
- the frozen 28-file base package still matches
  `be7b0db4f0f349f8898f749e8ee0f4bd6a3407c79acbe33b415da081ff9ea9ed`;
- no authority or commercial claim is elevated.

Stop and preserve failure on any missing input, hash ambiguity, unordered dependency, secret
exposure, count mismatch, Schema failure or attempt to mutate the base package.

## 9. Required next governance sequence

```text
THIS_RECOMMENDATION
    ↓
ONE_EXACT_QWEN3.7-MAX_ADVISORY_REVIEW
    ↓
INDEPENDENT_HUMAN_DECISION_FOR_SUPPLEMENT_PREPARATION
    ↓
OFFLINE_SUPPLEMENT_CONTRACT_PREPARATION
    ↓
NEW_RECOMMENDATION_AND_DECISION_FOR_OFFLINE_VALIDATION
    ↓
OFFLINE_VALIDATION_RESULT
    ↓
NEW_EXECUTION_READINESS_RECOMMENDATION
```

No step automatically authorizes the next.

## 10. Non-authorizations and interpretation boundary

This Recommendation authorizes none of the following:

- mutation of the frozen 28-file package;
- supplement preparation or validation;
- HTTP fetch;
- model session;
- technical reuse run;
- Agent, Runtime, Entity, Capability or Permission;
- Evidence Truth;
- customer adoption, market demand or external endorsement;
- outreach, implementation, deployment, release or PR;
- commercial offering, price, contract, SLA, certification, Standard Ready or Production Ready;
- change of DBA, DBOS, SAEE, Governance Decision, Owner or Authority.

```text
Observation != Evidence
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```

## 11. Recommendation review contract

Use one exact `qwen3.7-max` request, direct JSON only, with no retry, fallback, model substitution,
JSON extraction or repair.

Required review keys:

```text
verdict
confidence
selected_option
would_recommend_current_execution
would_recommend_supplement_preparation
input_binding_gap_material
immutable_base_package_preserved
supplement_scope_bounded
sanitized_input_bundle_reproducible
model_input_envelope_complete
inter_session_dependencies_bound
execution_output_allowlist_complete
composite_status_mapping_sound
security_and_secret_boundary_complete
offline_validation_scope_complete
execution_decision_separation_sound
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

A qualifying review requires:

- `verdict=RECOMMENDED` or `CONDITIONALLY_RECOMMENDED`;
- `selected_option=A`;
- `confidence>=0.90`;
- `would_recommend_current_execution=false`;
- `would_recommend_supplement_preparation=true`;
- every other required boolean `true`;
- empty `blockers` and `corrections`;
- requested and returned model identities both exactly `qwen3.7-max`.
