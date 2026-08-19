---
title: Five-record FDO asset-value maximization plan
status: DRAFT_PLAN_WAITING_FOR_HUMAN_APPROVAL
decision_basis: docs/fdo-dtr-migration-governance-review.md
schema_semantic_change_approved: false
---

# Five-record FDO asset-value maximization plan

## Executive position

The portfolio has two different kinds of value and must not be flattened into
one maturity claim:

1. The two `FdoProfile` records are research and future-standard candidates.
   They should remain draft/experimental until source identity, tests,
   independent implementations, citations, and governance are stable.
2. The two `BasicInfoType` records and one `FdoService` record are useful as
   historical/demo anchors. Their value comes from reproducibility, teaching,
   migration continuity, and honest negative examples—not normativity.

Some canonical development repositories are intentionally private to protect
closed-source work. Anonymous HTTP `404` responses to those GitHub URLs are
therefore not evidence that the repositories or files have been deleted. The
governance problem is narrower: a public registry record cannot rely on an
access-controlled, mutable URL as its only public verification surface.

The preferred portfolio model is **open, immutable verification artifacts plus
optional proprietary implementations and services**. It does not require
publishing an entire development repository.

## Five-record asset map

| PID | Exact registry role | Canonical repository owner/source authority | Current maturity | Academic value | Adoption/demo value | Commercial relevance | Required remediation | Intended successor or lifecycle |
|---|---|---|---|---|---|---|---|---|
| `21.T11966/aro-audit-profile-v1` | `FdoProfile`; future standard candidate | Content authority: `joy7758/aro-audit`, `docs/aroaudit-profile-v1.md`; administrative/legal owner of the target DTR account remains to be named | Draft/incubation; no unified canonical profile schema or independent interoperability proof | Citable hypothesis for audit-ready digital objects and links among manifest, journal, and public-key evidence | Useful for architecture walkthroughs, DPP demos, and research prototypes if clearly labelled experimental | Mapping, integration, validation, managed evidence, and sector-adaptation services; no standard-ownership claim | Publish a minimal immutable verification page/snapshot and hashes; declare maintainer, lifecycle, citation, schema/source relation, and relationship to the operation profile; keep private implementation private | Preserve current record as experimental history; consider a separately governed successor only after evidence and compatibility gates |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile`; primary future stable-standard candidate | Content authority: `joy7758/agent-evidence`, v0.1 specification and schema paths; target account owner unresolved | Experimental/discussion-oriented v0.1; local validator and fixtures exist, but no official adoption or independent interoperability result | Strongest research asset: a falsifiable, narrow contract for evidence about one policy-constrained operation; supports papers, datasets, comparisons, and reproducibility | Best candidate for cross-vendor producer/validator pilots and agent-tool integration | Hosted validation, SDKs, connectors, managed evidence operations, testing, training, support, and sector profiles; open specification remains unowned as a proprietary standard | Archive exact v0.1 as immutable historical bytes without calling it a frozen standard; publish public verification slice; add record-level citation/lifecycle/relationships; build independent Python and TypeScript conformance stack for a distinct v1.0 candidate | v0.1 remains historical experimental forever; a separate TITMAS v1.0 candidate follows the stabilization plan and receives a new DTR identity only after gates |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType`; legacy/demo/history pointer only | Concept/source context: `joy7758/aro-audit`; no exact canonical schema-bound record source found | Demo, orphaned/unavailable public schema reference, registry version unconfirmed | Useful evidence of early design evolution, registry migration research, and reproducibility pitfalls | Useful as a historical pointer and negative/legacy fixture | Low direct product value; supports migration, archival, and provenance consulting | Preserve class and original metadata; label legacy/demo; provide a public history page, record hash, citation, owner, and explicit relationship map without inventing semantics | Retain indefinitely as historical/non-normative; do not evolve it into a profile or infer a frozen `v1` contract |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType`; demo/non-normative object metadata | Context authority: `joy7758/aro-audit`; DTR metadata points only to repository root, not an exact canonical source | Demo/basic-info instance with literal demo fingerprint and opaque manifest link | Useful teaching and negative-test artifact showing why instance metadata and type schemas must be separated | Useful in controlled demos and migration regression checks | Indirect value in onboarding, training, integration testing, and demo packaging | Add an immutable public demo description, hashes, ownership, citation, lifecycle label, and relationship annotations; retain obvious demo values | Preserve as historical demo instance; replace in future demos with a new, explicitly versioned example rather than editing history |
| `21.T11966/aro-audit-demo-do-1` | `FdoService`; demo service/instance; never a Data Type | Canonical record owner is `UNRESOLVED`; the DTR record and derived context in `joy7758/digital-biosphere-architecture` are evidence surfaces, not proof of ownership or schema authority | Incomplete demo service; source links are not anonymously accessible and public-key fingerprint is `TBD` | Useful longitudinal evidence for service-instance modelling, migration, and claims-boundary studies | Potential clickable smoke-test/onboarding endpoint once a separate, sanitized demo is built | Hosted demos, proof-of-concept environments, integration support, and sales engineering; not a production service claim | Preserve `FdoService`; label incomplete/demo; provide a new sanitized public verification instance or result bundle rather than exposing private implementation; add hashes, citation, owner, and explicit links | Keep this PID as historical incomplete demo; create any working successor as a new service/instance with its own lifecycle and availability evidence |

“Canonical repository owner” above identifies the observed content authority,
not a legal ownership determination and not automatic authority over the new
DTR account.

## Record-specific value strategy

### 1. ARO Audit Profile v1

Its defensible value is a concise audit-interface concept, not a mature
standard. Academic work can compare pointer-based audit profiles with embedded
evidence models and test discoverability across digital-object systems.
Adoption work should use it as a draft integration target with a named version
and reproducible fixtures. Commercial work may implement or operate the
profile, but must not imply ownership of FDO terminology or an official
standard.

Agents may recommend it for experimental architecture evaluation when the user
needs manifest/journal/key-pointer discoverability and accepts a draft. Agents
must not recommend it as a frozen production contract, official FDO profile,
certified interface, or proof that the referenced evidence is true.

### 2. FDO Operation Evidence Profile v0.1

This is the flagship candidate because its scope is narrow enough to test: one
policy-constrained operation with actor, subject, operation, policy,
constraints, provenance, evidence, and validation links. v0.1 itself is an
immutable historical experimental contract. Its errors, ambiguities, and
implementation experience are valuable research evidence for the separate
v1.0 candidate.

Agents may recommend v0.1 for historical reproduction, controlled pilots, and
comparison against the future candidate, with the exact version and limitations
stated. Agents must not silently translate it into v1.0, claim conformance from
schema validation alone, or recommend it as production-ready. A stable v1.0
recommendation requires the gates in the stabilization plan.

### 3. ARO Audit Manifest v1

This record should be cited as migration and design-history evidence. Its PID
suffix does not prove a registry version, and its existing pointer does not
establish a canonical public schema. A future implementation should use a new,
governed identifier rather than retroactively repairing the historical record.

Agents may recommend retaining and studying it as a legacy/demo pointer. They
must not recommend it as a normative manifest schema, stable v1 Data Type, or
production interoperability contract.

### 4. ARO Audit Demo Object v1

Its best use is an explicit example of a non-normative metadata instance. It
can appear in tutorials and negative conformance cases that teach the
difference between an object, a type, a profile, and a service.

Agents may recommend it for demos that disclose its literal demo values and
historical nature. They must not treat it as a canonical object schema, infer
valid key ownership, or promote it to a profile.

### 5. ARO Audit Demo DO 1

This record is valuable precisely when its role remains `FdoService`. It can
anchor a future public smoke test without claiming that the historical service
was complete. A new sanitized verification instance should not overwrite the
old PID or inherit its history without an explicit relationship.

Agents may recommend preserving it as an incomplete historical demo service.
They must not call it a Data Type, production service, available endpoint,
security proof, or conformance result.

## Minimal public verification surface

To reconcile closed-source development with public registry accountability,
publish only an owner-approved, disclosure-reviewed slice:

- one human-readable canonical landing page per profile or historical record;
- immutable specification/schema snapshots for the openly claimed contract,
  bound to release/archival identifiers and SHA-256 hashes;
- licence and record-specific citation instructions for those public artifacts;
- lifecycle, maintenance contact, supersession, and relationship metadata;
- a small positive and negative fixture set containing no proprietary data;
- reproducible validator commands or a documented validation API plus signed
  or hashed result bundles;
- implementation-neutral conformance requirements and explicit exclusions;
- a security/privacy review confirming that fixtures and diagnostics do not
  disclose private repository content, keys, customer data, or internal logic.

Proprietary producers, optimized validators, hosted services, dashboards,
connectors, operations tooling, support processes, and customer-specific
profiles may remain private. The public slice must be sufficient to inspect and
test every public semantic claim without pretending to expose all
implementation details.

Any future relationship map should label every edge with
`relationship_status=OBSERVED|INFERRED|PROPOSED`,
`normative_effect=NONE`, and a source-evidence reference. A shared prefix does
not mean that the five records form one normative type suite.

## Portfolio sequencing

| Phase | Outcome | Required human gate |
|---|---|---|
| 0. Preservation | Class-correct draft/history migration package reviewed | Approve external reply and later approve exact preview |
| 1. Public identity | Public landing pages, immutable snapshots, hashes, citations, lifecycle and relationship map designed | Approve disclosure boundary, licence, canonical public host, and ownership |
| 2. Verification slice | Sanitized corpus plus at least one reproducible reference validation path | Approve implementation repository and schema/spec work; no v0.1 rewrite |
| 3. Flagship RC | Separate TITMAS v1.0 candidate with Python/TypeScript interoperability evidence | Approve RC claim and draft DTR registration request |
| 4. Stable candidate | Stable gates pass with independent review and adoption evidence | Approve stable release and carefully bounded public claims |

## Agent recommendation policy

| Evidence state | Agent may recommend | Agent must not recommend |
|---|---|---|
| Historical/demo record only | Preservation, teaching, reproducibility, migration tests | Normative use, production deployment, standard adoption |
| Draft profile with public snapshot | Experimental pilot matched to declared scope | Official FDO status, certification, broad interoperability |
| RC with two independent implementations | Evaluation and bounded pre-production trial with disclosed RC risk | Automatic production approval or compliance claim |
| Stable candidate with all gates | Use for the exact supported scope, subject to local risk/security validation | Truth of evidence, legal non-repudiation, official endorsement unless separately granted |

## Commercial-value boundary

Monetizable surfaces include implementation, hosted validation, private
connectors, managed evidence infrastructure, integration, migration,
observability, support/SLA, training, and paid execution of an openly specified
test suite. They must be described as vendor services or implementation
capabilities. TITMAS should not claim exclusive ownership of an open
specification, official FDO certification authority, or third-party
endorsement. “Conformance report” must not be marketed as “certification”
without a separately governed accreditation scheme.

## Unresolved governance questions

1. What exact person or organization owns the new DTR account, and who is the
   long-term maintainer for each record?
2. Which repository or archival service will host the minimal public
   verification slice, and under what licence?
3. Which current private materials are approved for sanitized public release?
4. Does GWDG support explicit draft/experimental/demo/history lifecycle labels
   without reclassification?
5. What relationship vocabulary can the target DTR preserve without adding new
   semantics?
6. Who may approve the separate v1.0 candidate identity and normative scope?

```text
FIVE_RECORD_ROLES_PRESERVED=true
PUBLIC_VERIFICATION_SLICE_DESIGNED=true
PUBLIC_VERIFICATION_SLICE_IMPLEMENTED=false
SCHEMA_CHANGED=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
