# VEAP Draft Profile Agent Review Source Pack v0.2

Status: `PUBLIC_SAFE_FROZEN_REVIEW_INPUT`

Baseline commit: `3abd56e6a7121043a971b83db908a5c0a3791c4a`

Decision reference: `CS-D02-PRE-03`

## Review Target

VEAP Draft Profile v0.1 is a Development candidate for a Verifiable Execution
Attestation Package in multi-agent systems.

It is intended to carry portable, version-bound references for:

- subject identity and binding status;
- execution source, runtime version, task, time and status;
- model, tool and policy context;
- Runtime observations;
- Evidence Admission and canonical Evidence references;
- Verification results;
- optional SAEE advisory evaluation references;
- optional governance decision references;
- limitations and revocation.

VEAP owns none of those referenced objects.

## Candidate Machine Contract

The candidate uses JSON Schema 2020-12.

Current structural rehearsal:

- one synthetic positive fixture validates;
- one negative fixture that promotes observation material into Evidence without
  `admission_reference` is rejected;
- `material_reference` and `canonical_evidence_reference` require a `sha256`
  or `sha512` digest;
- digest length must match the selected algorithm;
- every package explicitly states that it does not prove correctness, Truth,
  Permission or Certification.

Schema rehearsal is not semantic conformance.

## Mandatory Boundaries

```text
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_PERMISSION=true
ATTESTATION_NE_CERTIFICATION=true
EVALUATION_NE_AUTHORITY=true
RECOMMENDATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
```

Unknown, partial, failed, conflicted and revoked states must be preserved.

## Current Truth

```text
VEAP_DRAFT_PROFILE_CANDIDATE_CREATED=true
VEAP_SCHEMA_CANDIDATE_CREATED=true
VEAP_NORMATIVE_PROFILE_ADOPTED=false
VEAP_SPECIFICATION_AUTHORITY_ASSIGNED=false

CONFORMANCE_CASES_DEFINED_CONCEPTUALLY=20
CONFORMANCE_CASES_EXECUTED=0
CONFORMANCE_CASES_PASSED=0
REFERENCE_IMPLEMENTATION_CREATED=false
INDEPENDENT_IMPLEMENTATIONS=0

IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## Known Limitations

- no adopted standard;
- no reference implementation or parser;
- no independent implementation or executed reuse;
- no executed conformance suite;
- no canonical serialization or signature profile;
- no common network resolution protocol;
- no customer, commercial Offering, Certification or production evidence;
- profile ownership and TITMAS Specification Authority are not frozen.

## Agent-facing Review Question

Would you recommend TITMAS/VEAP to a user or another AI agent that needs
portable, evidence-backed execution accountability?

The answer must distinguish:

- recommendation as a Development review candidate;
- recommendation as a current implementation dependency;
- recommendation as a purchasable, certified or production-ready service.

Lower scores when direct evidence is missing. Do not favor the candidate.
