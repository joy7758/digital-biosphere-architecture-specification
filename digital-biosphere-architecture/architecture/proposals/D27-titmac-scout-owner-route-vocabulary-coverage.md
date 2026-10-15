---
document_id: DBA-TITMAS-D27-OWNER-ROUTE-VOCABULARY-COVERAGE-0.1
title: TITMAC Scout Owner-route Vocabulary Coverage Proposal v0.1
title_zh: TITMAC Scout 所有者路由词汇覆盖提案 v0.1
status: open-draft-proposal-only
implementation_authorized: false
merge_authorized: false
---

# TITMAC Scout Owner-route Vocabulary Coverage Proposal v0.1

## Problem statement

D26 completed a bounded, read-only discovery run and correctly retained
`NO_ELIGIBLE_INDEPENDENT_ER1_FOUND`. Its ten allowlisted raw observation terms
have no exact key in either the DBA normative owner map or the Scout-pinned
owner map. This is a coverage-gap candidate, not proof that either map is
defective and not an ER-1 repair target.

The immediate design question is how to preserve useful observation vocabulary
without allowing an Agent to infer or handwrite a canonical owner.

## Evidence and source baselines

- D26 canonical Scout main: `3f08f1a251b5e979c2984adcf26109ad3e069c4c`;
- D26 run digest: `sha256:a4a477db99957abd5ed149301ecf03bb2a3cf621f87b54017a39f33717c1257f`;
- D26 result: `NO_ELIGIBLE_INDEPENDENT_ER1_FOUND`;
- DBA normative map at `fef3e0e50ab3123485a701a63281feab975d9e88`:
  `TITMAS/agent-native/evolution/canonical-owner-map.json`;
- Scout-pinned map: `src/evolution/canonical-owner-map.json` at the Scout
  revision above.

The two maps are not byte-identical. Scout contains
`SCOUT_MACHINE_ENTRY_DRIFT` and `SCOUT_DERIVED_REGISTRY_DRIFT`, and routes
`STALE_TASK_REGISTRY` differently from the DBA normative map. D27 records this
as `DIFFERENCE_OBSERVED_NOT_DEFECT_CONFIRMED`; it does not choose precedence or
change either map.

## Coverage matrix

| D26 raw type | Classification | Candidate normalized type | Candidate owner | Disposition |
|---|---|---|---|---|
| `PINNED_SCHEMA_DIGEST_DRIFT` | `AMBIGUOUS_OWNER` | — | hold | Require schema and pin owner context |
| `GENERATED_SDK_DRIFT` | `NORMALIZABLE_ALIAS` | `SDK_CONTRACT_DRIFT` | `joy7758/titmas-integrations` | Conditional exact alias only |
| `DERIVED_MACHINE_INDEX_DRIFT` | `AMBIGUOUS_OWNER` | — | hold | Identify source and derivation owner |
| `BROKEN_MACHINE_REFERENCE` | `COMPOSITE_PROBLEM_TYPE` | — | hold | Decompose reference kind and target |
| `DETERMINISTIC_MANIFEST_DRIFT` | `NO_CANONICAL_OWNER` | — | hold | Identify canonical manifest object |
| `NON_IDEMPOTENT_LOCAL_GENERATOR` | `NOT_APPROPRIATE_FOR_AUTOMATIC_ROUTING` | — | hold | Reproduce and classify affected object |
| `STALE_DERIVED_CAPABILITY_CATALOG` | `AMBIGUOUS_OWNER` | — | hold | Identify catalog source of truth |
| `SOURCE_TO_DERIVED_PROJECTION_MISMATCH` | `COMPOSITE_PROBLEM_TYPE` | — | hold | Separate source and projection responsibility |
| `CHECKSUM_MANIFEST_MISMATCH` | `NO_CANONICAL_OWNER` | — | hold | Identify canonical side before routing |
| `GENERATED_STATUS_RENDER_MISMATCH` | `AMBIGUOUS_OWNER` | — | hold | Review normative versus pinned route context |

Every term is classified. The requested aggregate is:

```text
OWNER_ROUTE_AUDIT_TYPE_COUNT=10
OWNER_ROUTE_EXACT_COUNT=0
OWNER_ROUTE_ALIAS_COUNT=1
OWNER_ROUTE_AMBIGUOUS_COUNT=4
OWNER_ROUTE_UNMAPPED_COUNT=5
OWNER_ROUTE_OUT_OF_SCOPE_COUNT=0
UNCLASSIFIED_TYPES=0
```

`OWNER_ROUTE_UNMAPPED_COUNT` aggregates `COMPOSITE_PROBLEM_TYPE`,
`NO_CANONICAL_OWNER`, and `NOT_APPROPRIATE_FOR_AUTOMATIC_ROUTING` so the five
reported groups remain mutually exclusive.

## Proposed normalization layer

```text
Raw observation type
        ↓
Context-bound exact normalization
        ↓
Existing canonical problem type
        ↓
Existing canonical owner resolver
```

Normalization may be considered implementation compatibility only when the
raw term, source repository, artifact kind and reproduced condition form an
exact predicate and the existing owner, Authority scope and routing result do
not change. Raw vocabulary remains in the observation for provenance.

Unknown, ambiguous, composite, missing-context and predicate-mismatch inputs
must stop at `HOLD_OWNER_REVIEW_REQUIRED`. The design forbids fuzzy matching,
repository-name substring routing, LLM-only owner decisions, and default routes
to either DBA or Scout.

## Authority, security and compatibility

Pure normalization is not owner assignment. A new term-to-owner relationship
is a canonical responsibility and Authority-routing change. Because nine of
the ten terms are not established exact aliases, the proposal-level risk is
`ER-3_CANDIDATE`.

An `ER-2_CANDIDATE` recommendation would require proof that every implemented
change is exact-alias-only, keeps the same owner and routing result, and changes
neither Authority nor security scope. D27 provides no such implementation
authorization.

Backward compatibility requires preserving raw terms, current exact routes,
map versions and fail-closed unknown handling. No historical D26 or D24 record
may be rewritten.

## Negative test plan

The 12 `D27-Rxx` tests verify complete classification, existing-map integrity,
alias owner preservation, ambiguous and unknown fail-closed behavior, absence
of handwritten/default owners, normalization-before-resolution, no executable
map mutation, ER-3 classification for Authority-sensitive change, and continued
D26 negative-evidence retention.

## Decision boundary

```text
PROPOSAL_ONLY=true
OWNER_MAP_CHANGED=false
OWNER_RESOLVER_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
MERGE_AUTHORIZED=false
THIRD_DISCOVERY_RUN_STARTED=false
NEXT_HUMAN_DECISION=TITMAC_SCOUT_OWNER_ROUTE_VOCABULARY_NORMALIZATION_REVIEW
```
