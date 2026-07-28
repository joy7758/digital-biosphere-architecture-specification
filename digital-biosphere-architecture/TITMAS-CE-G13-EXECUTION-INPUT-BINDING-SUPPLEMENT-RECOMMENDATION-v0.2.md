---
document_id: DBA-TITMAS-CE-G13-EXECUTION-INPUT-BINDING-SUPPLEMENT-RECOMMENDATION-0.2
title: TITMAS CE-G13 Execution Input Binding Supplement Recommendation v0.2
title_zh: TITMAS CE-G13 执行输入绑定补充契约建议 v0.2
version: 0.2.0
status: replacement-recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: ce-g13-offline-input-binding-and-output-allowlist-supplement-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
supersedes: TITMAS-CE-G13-EXECUTION-INPUT-BINDING-SUPPLEMENT-RECOMMENDATION-v0.1.md
preserves_failure: TITMAS-CE-G13-EXECUTION-INPUT-BINDING-SUPPLEMENT-RECOMMENDATION-QWEN-REVIEW-FAILURE-v0.1.json
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
commercial_language: Exploration
authority_effect: none
---

# TITMAS CE-G13 Execution Input Binding Supplement Recommendation v0.2

## Replacement Recommendation

Select **Option A — refuse current CE-G13 execution, preserve the validated 28-file base package
unchanged and prepare a separately governed offline input-binding supplement**.

```text
CURRENT_EXECUTION_RECOMMENDATION=NOT_RECOMMENDED_INPUT_BINDING_INCOMPLETE
SUPPLEMENT_PREPARATION_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
BASE_PACKAGE_MUTATION_RECOMMENDED=false
CE_G13_EXECUTION_AUTHORIZED=false
PUBLIC_FETCHES=0
MODEL_REQUESTS=0
TECHNICAL_REUSE_RUNS=0
```

The v0.1 review attempt produced no persisted Provider response. Its failure record is immutable,
non-qualifying and not retried. This v0.2 document is a new replacement Recommendation. One new
exact-model advisory review may assess v0.2; it cannot reinterpret the failed v0.1 attempt.

## Material gap

At governance commit `8a8fc840def61cadef132ebc2d0219aba7a19a82`, the frozen package records:

- each retrieved URL, byte count and raw-content hash;
- the prompt hash and snapshot-manifest hash for each role request;
- the expected role response Schema and direct-JSON boundary.

It does not yet persist and bind:

1. the exact sanitized public text admitted to model input;
2. the exact ordered request components and sanitized Provider request body;
3. the response Schema bytes used in each request;
4. S04's validated reuse-plan input;
5. S05's exact S01–S04 response inputs;
6. a complete execution-output allowlist containing all five request-capture records.

Therefore the same snapshot-manifest hash could still be assembled into different model-visible
requests. The current design is insufficient for strict reproduction and should not receive an
execution Decision.

## Option A bounded supplement

The supplement must be separate from
`commercial-evaluation-ce-g13-offline-contract/`. The existing 28 files, their R2 validation and
package manifest SHA-256
`be7b0db4f0f349f8898f749e8ee0f4bd6a3407c79acbe33b415da081ff9ea9ed`
remain unchanged.

The supplement must define four contracts:

### 1. Sanitized Public Input Bundle

For every model-admitted public resource:

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

`sanitized_text` must be the exact persisted UTF-8 text used by request assembly. Binary resources
may be referenced for the optional synthetic technical check but cannot be admitted as model text.
Cookies, Authorization headers, API keys, raw IPs, customer data, private files and hidden answer
keys remain forbidden.

### 2. Model Input Envelope

One envelope per S01–S05 request:

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

The envelope must bind exact persisted file bytes and order:

- S01: root seed, customer problem, cold prompt, response Schema, public bundle;
- S02: architecture prompt, response Schema, public bundle;
- S03: reuse-planning prompt, response Schema, public bundle;
- S04: recommender prompt, response Schema, public bundle, validated reuse-plan result;
- S05: boundary prompt, response Schema, public bundle, exact S01–S04 response files.

The secret-free direct request JSON may be persisted. Credentials, Authorization headers, hidden
reasoning and private Provider metadata may not be persisted.

### 3. Exact Execution Output Manifest

The future execution result must contain exactly 26 files:

| Group | Count |
|---|---:|
| execution README | 1 |
| execution-baseline receipt | 1 |
| public snapshot manifest | 1 |
| retrieval receipt | 1 |
| sanitized public input bundle | 1 |
| S01–S05 model-input envelopes | 5 |
| S01–S05 request-capture records | 5 |
| S01–S05 direct response files | 5 |
| reuse-plan validation result | 1 |
| technical-reuse receipt, including `NOT_EXECUTED` | 1 |
| append-only failure ledger | 1 |
| composite result | 1 |
| non-recursive output manifest | 1 |
| human-readable validation report | 1 |
| **Total** | **26** |

The non-recursive output manifest must bind each path, byte count, SHA-256 and artifact kind. It
must reject extra, missing, renamed, modified and self-hashed files.

### 4. Outcome Policy

The existing composite runtime statuses remain:

```text
NOT_EXECUTED
PASS
FAIL_CLOSED
```

`CONDITIONAL_REMEDIATION_REQUIRED` is permitted only as a later governance interpretation of a
preserved failed result. It is not a third execution status. A failed output cannot be repaired,
overwritten or rescored into PASS.

## Controller boundary

Any future execution must retain:

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

Retrieval and sanitization must pass before any model request. Persist each model-input envelope
before its one Provider request. Model mismatch, non-direct JSON, Schema failure, hash mismatch,
unbound upstream input, hidden input, secret exposure or output-manifest violation is
`FAIL_CLOSED` with no retry.

The optional technical reuse check may run only after S03 and deterministic reuse-plan validation
pass. It cannot start a Runtime or create an Agent, Entity, Permission or Evidence Truth.

## Required offline validation

After a separate Human Decision, a later supplement package and validation cycle must prove:

1. exact supplement allowlist, counts, paths, bytes and hashes;
2. duplicate-key rejection and Draft 2020-12 Schema validity;
3. local-only reference resolution with no network or Provider access;
4. positive and wrong-session negative instances for all five envelopes;
5. any prompt, Schema, sanitized text, input order or upstream-result mutation invalidates its
   envelope;
6. secrets, headers, customer data, private input and hidden answer keys are rejected;
7. the 26-file manifest rejects missing, extra, renamed, changed or self-hashed outputs;
8. S04 and S05 dependency bindings are complete and ordered;
9. runtime status mapping is unambiguous and failure-preserving;
10. network, credential, model, technical-run, Runtime, Agent, Entity, Permission and Evidence
    Truth effects remain zero.

Any failure is retained and stops the cycle. The supplement may not be silently patched and
revalidated.

## Alternatives rejected

- infer model input from resource hashes without persisted admitted text;
- edit the validated 28-file package in place;
- rely on a Provider request identifier instead of bound request bytes;
- persist credentials or an unfiltered Provider envelope;
- authorize live execution before the supplement passes offline validation.

## Governance sequence

```text
V0_2_RECOMMENDATION
    ↓
ONE_NEW_EXACT_QWEN3.7_MAX_ADVISORY_REVIEW
    ↓
INDEPENDENT_HUMAN_DECISION_FOR_SUPPLEMENT_PREPARATION
    ↓
OFFLINE_SUPPLEMENT_PREPARATION
    ↓
SEPARATE_RECOMMENDATION_AND_DECISION_FOR_OFFLINE_VALIDATION
    ↓
OFFLINE_VALIDATION_RESULT
    ↓
NEW_EXECUTION_READINESS_RECOMMENDATION
```

No step automatically authorizes the next.

## Non-authorizations

This Recommendation does not authorize:

- base-package mutation, supplement preparation or validation;
- HTTP fetch, model session or technical reuse;
- Agent, Runtime, Entity, Capability, Permission or Evidence Truth;
- outreach, implementation, deployment, release, PR or merge;
- customer adoption, market demand, endorsement, commercial offering, pricing, contract or SLA;
- certification, Standard Ready or Production Ready;
- ownership or DBA/DBOS/SAEE/Governance Decision Authority change.

```text
Observation != Evidence
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```

## v0.2 review contract

One new exact `qwen3.7-max` request may review this replacement document. It must return direct JSON
without retry, fallback, substitution, extraction or repair.

Required keys:

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
prior_review_failure_preserved
new_review_is_not_retry
execution_decision_separation_sound
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

Qualifying requires:

- `verdict=RECOMMENDED` or `CONDITIONALLY_RECOMMENDED`;
- `selected_option=A`;
- `confidence>=0.90`;
- `would_recommend_current_execution=false`;
- `would_recommend_supplement_preparation=true`;
- every other required boolean `true`;
- empty `blockers` and `corrections`;
- requested and returned model identities exactly `qwen3.7-max`.
