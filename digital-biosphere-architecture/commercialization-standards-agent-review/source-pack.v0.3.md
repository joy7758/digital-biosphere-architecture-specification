# VEAP Draft Profile Agent Review Source Pack v0.3

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

## Exact Development Artifacts

The current review package exposes exact repository paths:

- Profile:
  `architecture/veap-draft-profile-v0.1.md`
- agent-readable entry:
  `architecture/veap-development-agent-entry.v0.1.json`
- agent-entry Schema:
  `architecture/schemas/veap-development-agent-entry.schema.v0.1.json`
- envelope Schema:
  `architecture/schemas/veap-envelope.schema.v0.1.json`
- positive synthetic fixture:
  `architecture/examples/veap-envelope.valid.v0.1.json`
- negative synthetic fixture:
  `architecture/examples/veap-envelope.invalid-observation-as-evidence.v0.1.json`
- ownership crosswalk:
  `architecture/veap-canonical-ownership-crosswalk-v0.1.md`
- conceptual 20-case design and catalog:
  `architecture/veap-predecision-conformance-design-v0.1.md` and
  `architecture/veap-predecision-conformance-cases.v0.1.json`
- bounded draft decision:
  `TITMAS-CS-D02-PRE-03-VEAP-DRAFT-CONTRACT-DECISION-RECORD.md`

The machine entry is the first file an AI agent should inspect.

## Current Bounded First Reuse Path

The only current usable path is Development document/Schema review:

1. read the Profile and agent entry;
2. load the envelope Schema with a Draft 2020-12 validator and record the
   validator name/version;
3. validate the positive synthetic fixture;
4. validate the negative fixture and require rejection because observation
   material lacks `admission_reference`;
5. retain Schema/fixture digests, environment, actual result and limitations;
6. compare a proposed use case with the ownership crosswalk and 20 conceptual
   cases, preserving unsupported and unknown requirements.

Expected structural results:

```text
positive fixture -> SCHEMA_VALID
observation-without-admission negative
  -> SCHEMA_REJECTS_OBSERVATION_PROMOTION_WITHOUT_ADMISSION_REFERENCE
```

This path is not a parser, reference implementation, executed Agent use,
semantic conformance or independent reuse.

## Recommendation Matrix

| User need | Current recommendation |
|---|---|
| Review a portable execution-accountability contract candidate | `CONDITIONAL` |
| Rehearse JSON Schema shape and one observation/Evidence negative | `CONDITIONAL` |
| Add a current implementation dependency or parser | `NO` |
| Buy or deploy a commercial VEAP service | `NO` |
| Obtain Certification, Truth, Permission or correctness proof | `NO` |

The quality of this matrix is separate from product maturity: a correct `NO`
for an unsupported use is a successful boundary, not a product claim.

## Candidate Machine Contract

The candidate uses JSON Schema 2020-12.

Current structural rehearsal:

- the agent entry validates against its Schema;
- one synthetic positive envelope fixture validates;
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
VEAP_DEVELOPMENT_AGENT_ENTRY_CREATED=true
VEAP_NORMATIVE_PROFILE_ADOPTED=false
VEAP_SPECIFICATION_AUTHORITY_ASSIGNED=false

CONFORMANCE_CASES_DEFINED_CONCEPTUALLY=20
CONFORMANCE_CASES_EXECUTED=0
CONFORMANCE_CASES_PASSED=0
REFERENCE_IMPLEMENTATION_CREATED=false
INDEPENDENT_IMPLEMENTATIONS=0
EXECUTED_REUSE_OBSERVED=false

IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## Known Limitations

- no adopted standard or assigned Specification Authority;
- no reference implementation or parser;
- no independent implementation or executed reuse;
- no executed conformance suite;
- no canonical serialization or signature profile;
- no common network resolution protocol;
- no customer, commercial Offering, Certification or production evidence;
- profile ownership is not frozen.

## Agent-facing Review Question

Would you recommend TITMAS/VEAP to a user or another AI agent that needs
portable, evidence-backed execution accountability?

The answer must distinguish:

- recommendation as a Development review candidate;
- recommendation as a current implementation dependency;
- recommendation as a purchasable, certified or production-ready service.

Lower scores when direct evidence is missing. Do not favor the candidate.
