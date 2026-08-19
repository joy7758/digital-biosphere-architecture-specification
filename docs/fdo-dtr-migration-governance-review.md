---
document_id: TITMAS-FDO-DTR-MIGRATION-GOVERNANCE-REVIEW-20260803
title: FDO DTR Migration Governance Review for TITMAS
status: DRAFT_GOVERNANCE_REVIEW_WAITING_FOR_HUMAN_APPROVAL
observed_at: 2026-08-03
timezone: Asia/Shanghai
primary_repository: joy7758/digital-biosphere-architecture-specification
cockpit_content_root: digital-biosphere-architecture/
review_type: read-only-cross-repository-governance-audit
schema_modified: false
child_repositories_modified: false
commit_created: false
migration_authorized: false
freeze_authorized: false
---

# FDO DTR Migration Governance Review for TITMAS

## Executive summary

GWDG intends to migrate five records under prefix `21.T11966` from the FDO
Testbed DTR to the new production DTR. This review recommends preserving the
identifiers and registry history, but **does not recommend freezing any of the
five records as a production-stable Data Type**.

```text
GOVERNANCE_RECOMMENDATION=CONDITIONALLY_RECOMMEND_DRAFT_PRESERVATION_MIGRATION_ONLY
FROZEN_MIGRATION_RECOMMENDED_COUNT=0
DRAFT_PROFILE_MIGRATION_RECOMMENDED_COUNT=2
PRESERVATION_ONLY_CONDITIONAL_COUNT=3
MIGRATION_AUTHORIZED=false
HUMAN_APPROVAL_REQUIRED=true
```

The five records are not homogeneous Data Types in the Testbed DTR:

- `aro-audit-profile-v1` and `fdo-operation-evidence-profile-v0-1` are
  `FdoProfile` records;
- `aro-audit-manifest-v1` and `aro-audit-demo-obj-v1` are `BasicInfoType`
  demo/pointer records whose declared schema type is only `String`;
- `aro-audit-demo-do-1` is an `FdoService` demo record, not a Data Type or
  profile.

The two profile records have repository sources, but both remain experimental
or draft. The three demo/pointer records lack a versioned, canonical schema
contract. The `FdoService` record also contains `pubkey_fingerprint: TBD` and
links to two `aro-audit/main/demo/*` resources that returned anonymous HTTP
`404` during this audit. The profile specification URLs also returned
anonymous HTTP `404`, although the referenced files exist in the locally
observed Git `origin/main` refs. A production DTR migration must not turn these
source-access and maturity gaps into an implied standard, adoption, or semantic
freeze.

The recommended response to GWDG is therefore: migrate the two profiles as
mutable `DRAFT/EXPERIMENTAL` records; migrate the two `BasicInfoType` demo
records only as clearly labelled legacy/demo preservation records; migrate
`aro-audit-demo-do-1` only if its original `FdoService` classification can be
preserved. If the production DTR cannot represent these lifecycle and type
boundaries, defer the affected records rather than freeze or reclassify them.

## Scope, authority, and evidence boundary

This is a Program/Architecture Governance review. The primary repository is
the TITMAS cockpit, `joy7758/digital-biosphere-architecture-specification`.
Child repositories remain the canonical owners of their implementation and
schema facts.

The review used:

1. the user-provided GWDG migration context;
2. live, read-only Testbed DTR API queries for the five exact identifiers on
   2026-08-03;
3. local Git repository identity, branches, commits, remote URLs, tracked
   sources, file histories, and schema hashes;
4. the TITMAS cockpit Portfolio, dependency, gate, risk, decision, and
   architecture-boundary documents; and
5. anonymous HTTP checks of the source URLs embedded in the DTR records.

The GWDG plan is treated as an incoming migration request, not proof that a
migration, production registration, freeze, or release has occurred. This
review does not modify a schema, DTR record, child repository, remote, branch,
or commit.

### Reproducible Testbed DTR observation

The five Testbed records can be opened through the UI pattern:

```text
https://typeregistry.testbed.pid.gwdg.de/#objects/21.T11966/<record-name>
```

The live JSON classification used in this review can be reproduced without a
write or login:

```bash
record_name=aro-audit-profile-v1
curl -sS --get \
  --data-urlencode "query=id:\"21.T11966/${record_name}\"" \
  --data-urlencode "pageSize=5" \
  'https://typeregistry.testbed.pid.gwdg.de/objects/'
```

Repeat with each of the five exact record names. A later response is new live
state and must not be represented as the 2026-08-03 observation without a new
timestamp.

## Repository and reference inventory

| Repository / surface | Observed source | Role in this review | Canonicality finding |
| --- | --- | --- | --- |
| TITMAS cockpit | `joy7758/digital-biosphere-architecture-specification`; local Git root `/Users/zhangbin/Documents/New project`; branch `docs/aael-gbz185-part8-admission-review`; HEAD `9f589e3eacb11eceac004a42e43f695892098a5b` | Primary governance owner and report destination | Canonical for this governance review; not the schema or DTR execution owner |
| `aro-audit` | `joy7758/aro-audit`; branch `audit-scope-alignment-v1`; HEAD `74a7f584b8cb18ca2655a0dac30e77e41e582c43`; locally observed `origin/main` `0d2782e13056521a0862a52dd7bff4ff53b34879` | Source for the ARO profile and related manifest/journal/evidence concepts | Canonical repository source for ARO material; four ARO DTR records do not share one versioned schema contract |
| `agent-evidence` | `joy7758/agent-evidence`; branch `codex/organize-legacy-worktree-20260729`; HEAD `911db6650547617c71331ddd9506811f04191656`; locally observed `origin/main` `09385f47a33273d8c72bbca9d3ae57aff0d5c0d9` | Source for the registered operation-evidence profile, schema, examples, and validator | Canonical source for the registered v0.1 spec/schema. A newer FDO-facing Stage 1 package is on a separate branch and explicitly is not an alias of the registered profile |
| `verifiable-agent-demo` | `joy7758/verifiable-agent-demo`; branch `docs/mvk-aep-bridge-demo`; HEAD `e5bd3fa113aa2480f2bdb283bf5e32658933b958` | Toy receipt-validation and MVK-to-evidence walkthrough | Supporting demo only. No direct reference to any of the five exact handles was found outside archived/submission material; it is not a schema source |
| DBA public meaning/demo surface | `joy7758/digital-biosphere-architecture`; branch `main`; HEAD `1d0c3ba2d750b6a1d0606b49250960b3584bb478`; locally observed `origin/main` `ef599b07c453ccf2129e494c4bcaf1ac7243a34b` | Verifiable DPP demo, poster, QR, and public evidence summary referencing `aro-audit-profile-v1` and `aro-audit-demo-do-1` | Derived demonstration/communication surface, not a schema owner. Its canonical relationship with the cockpit remains unresolved under `DQ-008` |
| `fdo-kernel-mvk` | `joy7758/fdo-kernel-mvk`; `main@b28f870ee790aca2c3d38160256a7f30cd839916` | Supporting deterministic execution-integrity reference used by demos | No exact handle references found; not a DTR type owner |
| Duplicate local snapshots | `digital-biosphere-architecture-clean`, `_outward-pass/digital-biosphere-architecture`, `_surface-pass/digital-biosphere-architecture`, and `digital-biosphere-architecture-mci-admission` | Contain copies of the profile/demo references | Excluded as canonical sources because they point to the same `joy7758/digital-biosphere-architecture` remote and represent branches/snapshots |

Cockpit governance currently lists ARO and Agent Evidence as
`MAPPING_ONLY_REVIEW_REQUIRED`, with formal Portfolio treatment still open in
`DQ-006`. The cockpit/public-meaning relationship is separately unresolved in
`DQ-008`. Repository discovery and mapping therefore do not establish
integration, adoption, or freeze authority.

## Data Type mapping table

| DTR identifier | Live Testbed classification and current version | Purpose | Repository source | Schema location / status | Maturity | Draft migration recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| `21.T11966/aro-audit-profile-v1` | `FdoProfile`; registry version `1.0` | Declares that a digital object exposes manifest, journal, and public-key-fingerprint audit pointers | `aro-audit/docs/aroaudit-profile-v1.md`; expanded draft at `aro-audit/docs/FDO-Audit-Profile_v1_DraftSpec.md` | **No unified canonical profile schema found.** Related component schemas are `aro-audit/spec/AAR_v1.0.schema.json` and `aro-audit/schema/evidence.schema.json`; the DPP example manifest is an instance, not a versioned profile schema | `DRAFT / INCUBATION`; the document title is Draft, repository machine status is Incubation, and no independent interoperability evidence was found | **YES — `MIGRATE_AS_DRAFT_PROFILE`**. Preserve `FdoProfile`, PID, version `1.0`, provenance, and non-official status; do not freeze |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile`; registry version `0.1` | Represents verifiable evidence and accountability links for exactly one policy-constrained agent or service operation | `agent-evidence/spec/execution-evidence-operation-accountability-profile-v0.1.md` | `agent-evidence/schema/execution-evidence-operation-accountability-profile-v0.1.schema.json`; installable mirror `agent_evidence/schema/execution-evidence-operation-accountability-profile-v0.1.schema.json`; both observed with SHA-256 `cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8` | `EXPERIMENTAL / DISCUSSION-ORIENTED`, with a locally frozen v0.1 package and validator but no official FDO standard/adoption status. The newer `docs/fdo-profile/` Stage 1 profile is a distinct, unregistered candidate and not an alias | **YES — `MIGRATE_AS_DRAFT_PROFILE`**. Preserve exact v0.1 semantics and source binding; do not redirect it to or silently replace it with the newer Stage 1 package |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType`; `Schema.Type=String`; no registry `versioning.version` field. `v1` exists only in the identifier/name | Demo pointer/summary for an ARO audit packet, with trace/checkpoint counts and a journal digest in `userMetadata` | Concept appears in the ARO draft profile and `aro-audit/examples/dpp-battery/manifest.json`, but the exact handle is not referenced in the audited repositories | **No canonical schema found for this DTR record.** The DTR points to `https://aro-audit.org/manifest/v1.0`, which was not resolvable during the audit; the example manifest does not satisfy all fields named by the expanded draft | `DEMO / ORPHANED_SCHEMA_REFERENCE / VERSION_UNCONFIRMED` | **CONDITIONAL — `MIGRATE_AS_LEGACY_DEMO_RECORD`** only to preserve history and PID. If the target cannot mark it demo/draft and mutable, defer it. Never freeze from the handle suffix alone |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType`; `Schema.Type=String`; no registry `versioning.version` field. `v1` exists only in the identifier/name | Demo object declaring journal, manifest, and key-fingerprint support | DTR `audit_schema` points only to the `aro-audit` repository root; no exact source document or schema is bound | **No exact canonical schema found.** It is a demo metadata instance with a literal demo fingerprint and an opaque manifest handle | `DEMO / BASIC_INFO / NON-NORMATIVE` | **CONDITIONAL — `MIGRATE_AS_LEGACY_DEMO_RECORD`**. Preserve `BasicInfoType` and demo labelling; do not promote it into a profile or frozen Data Type |
| `21.T11966/aro-audit-demo-do-1` | `FdoService`; no registry version field | Demo repository/data-service record carrying ARO profile, manifest, journal, and key pointers; the public DBA demo treats it as a demo instance | DTR record plus derived references in `digital-biosphere-architecture/demo/verifiable-dpp-agent-demo/` and poster/QR material | **Not a schema source and not a Data Type.** Its manifest and journal URLs under `aro-audit/main/demo/` returned anonymous HTTP `404`; `pubkey_fingerprint` remains `TBD` | `INCOMPLETE DEMO SERVICE / INSTANCE` | **NO as a Data Type. CONDITIONAL as `MIGRATE_AS_FDO_SERVICE_DEMO_REFERENCE`** only if the original `FdoService` class and incomplete/demo status are preserved. Otherwise defer |

### Important identity and version distinctions

1. A handle suffix such as `v1` is not sufficient evidence of a governed
   version or frozen schema. Three records do not expose a registry version
   field.
2. The ARO profile's v1.0 draft, the AAR journal-record schema, the ARO
   Evidence Object schema, and the demo manifest are related but not the same
   contract.
3. The registered operation-evidence profile v0.1 is the EEOAP-oriented spec
   linked by the DTR. The newer `Verifiable Execution Evidence Profile for
   Digital Objects` v0.1.0 explicitly states that it is a distinct Stage 1
   experimental profile with placeholder identifiers; it must not silently
   replace the registered record during migration.
4. A production registry location does not itself create official FDO status,
   interoperability, adoption, certification, or TITMAS Portfolio admission.

## Draft versus frozen recommendation

| Migration class | Records | Recommendation | Required production-DTR treatment |
| --- | --- | --- | --- |
| Draft profile migration | `aro-audit-profile-v1`; `fdo-operation-evidence-profile-v0-1` | Accept only as draft/experimental profile preservation | Preserve PID, `FdoProfile` class, current version, provenance, source reference, and explicit `not official / not frozen` lifecycle metadata; allow later versioned correction |
| Legacy/demo preservation | `aro-audit-manifest-v1`; `aro-audit-demo-obj-v1` | Conditional acceptance | Preserve `BasicInfoType`; label `DEMO`, `NON_NORMATIVE`, and `SCHEMA_REVIEW_REQUIRED`; do not infer a version from the name or expose the records as recommended production types |
| Service/demo preservation | `aro-audit-demo-do-1` | Do not migrate as a Data Type; conditional migration in its original class | Preserve `FdoService`, demo/instance semantics, broken-link and `TBD` limitations; otherwise defer |
| Frozen/stable migration | None | **Not recommended** | Freeze only after a separate governance decision and all freeze gates below pass |

Minimum future freeze gates:

1. one owner-approved canonical repository, source path, immutable revision,
   and publicly/resolvably accessible specification URI per record;
2. a byte-pinned, versioned machine schema for the exact record semantics;
3. versioning, compatibility, deprecation, replacement, and maintenance policy;
4. resolved conflict between profile, manifest, journal, evidence object, demo
   service, and newer FDO-facing profile boundaries;
5. at least two independent producers/validators or an equivalent scoped
   interoperability exercise with retained positive and negative results;
6. review by the relevant FDO/community governance process without rewriting
   testbed registration as adoption;
7. TITMAS `G1` Source Truth, `G2` Architecture Contract, `G3` Implementation
   Mapping, and `G4` Conformance evidence for the declared scope;
8. explicit Human Decision identifying which exact bytes and DTR metadata are
   frozen; and
9. a GWDG migration preview showing source/target record equivalence, PID
   continuity or redirects, rollback, and correction behavior.

## Risks of premature freezing

### 1. Registry-class semantic corruption — HIGH

Treating all five records as Data Types would erase the observed distinction
between `FdoProfile`, `BasicInfoType`, and `FdoService`. In particular,
`aro-audit-demo-do-1` would be promoted from an incomplete demo service/instance
into a normative type.

### 2. Broken or inaccessible canonical source — HIGH

The source URLs embedded in the DTR records returned anonymous HTTP `404` for
both profile documents and for the demo service's manifest/journal. The local
Git refs contain the two profile documents, but a production registry should
not freeze a contract whose normative URI cannot be resolved by an independent
consumer.

### 3. Schema ambiguity and drift — HIGH

The ARO profile has multiple related schemas but no single schema for the exact
DTR profile. The expanded draft names manifest fields that are absent from the
tracked DPP manifest example. The operation-evidence repository also has a
newer Stage 1 FDO-facing profile that is explicitly different from the
registered v0.1 profile. Freezing now would make later consolidation either a
breaking change or a silent semantic substitution.

### 4. Demo material becoming normative — HIGH

Demo digests, opaque handles, `ed25519-demo-key-fingerprint`, and
`pubkey_fingerprint: TBD` are suitable for testbed demonstrations, not frozen
production contracts. Registry promotion could cause agents to recommend or
generate against placeholders.

### 5. Version and maintenance authority gap — HIGH

Three records do not carry a registry version field. No complete owner,
maintenance, compatibility, deprecation, or conflict-resolution contract was
found for all five records as a set. `DQ-006` and `DQ-008` remain open in the
cockpit.

### 6. External-status overclaim — HIGH

Production DTR placement may be read by humans and agents as official FDO
standardization, community adoption, production readiness, or TITMAS
integration. The repositories explicitly reject those claims. Registration,
migration, validation, publication, and adoption must remain separate states.

### 7. Loss of correction path — MEDIUM/HIGH

The ARO expanded draft states that a manifest must be immutable once
published. Freezing the surrounding type/profile before manifest semantics,
canonicalization, signature/key binding, and migration update rules are
settled could prevent safe correction or force a new identifier lineage.

## Recommended response strategy to GWDG

### Strategy

Respond promptly, welcome PID/history preservation, and ask GWDG to treat the
request as a **draft-preservation migration**, not a semantic freeze. Provide
an exact per-record classification matrix and request a target preview before
cutover.

Required confirmations from GWDG:

1. whether the production DTR supports `DRAFT`, `EXPERIMENTAL`, `DEMO`,
   `NON_NORMATIVE`, or equivalent lifecycle metadata;
2. whether original Cordra types (`FdoProfile`, `BasicInfoType`, `FdoService`)
   will be preserved without normalization;
3. how original PIDs, handle resolution, redirects, provenance, timestamps,
   and relationships will be retained;
4. whether draft records remain correctable/versionable after migration;
5. how a source/target JSON export and content hash can be reviewed before
   production cutover;
6. rollback or defer behavior for records that cannot retain their original
   classification; and
7. confirmation that migration does not imply endorsement, standardization,
   adoption, or conformance.

### Proposed response text

> Subject: TITMAS governance classification for 21.T11966 DTR migration
>
> Thank you for preserving the five `21.T11966` records during the move from
> the FDO Testbed DTR. Our governance review supports migration only as
> draft/experimental or demo-history preservation; it does not authorize a
> frozen/stable classification.
>
> Please preserve the Testbed record classes exactly: two `FdoProfile`
> records, two `BasicInfoType` demo/pointer records, and one `FdoService` demo
> record. In particular, `21.T11966/aro-audit-demo-do-1` must not be migrated
> or presented as a Data Type.
>
> We request a pre-cutover JSON preview for all five records, including target
> identifiers, original identifier/redirect handling, type, version fields,
> provenance, lifecycle labels, source links, and content hashes. Please mark
> the two profiles `DRAFT/EXPERIMENTAL` and the other three records
> `DEMO/NON_NORMATIVE/SCHEMA_REVIEW_REQUIRED`, or defer any record if those
> boundaries cannot be represented.
>
> Migration must not be described as profile freeze, official FDO adoption,
> conformance, or production readiness. We will provide a separate human
> decision if and when exact schemas and versions are approved for freezing.

This text is a draft strategy only. Sending it is an external action and
requires separate human approval.

## Pre-development agent recommendation gate

If a potential user asked whether these records should be recommended for
production DTR use today:

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_FOR=DRAFT_NAMESPACE_AND_HISTORY_PRESERVATION
NOT_RECOMMENDED_FOR=FROZEN_TYPE_SEMANTICS_OR_PRODUCTION_CONFORMANCE
```

Non-recommendation reasons are the heterogeneous registry classes, source URL
failures, schema gaps, demo placeholders, missing maintenance/version policy,
and absence of independent interoperability evidence. The corrective work is
separable, but it would require later schema/source changes in canonical child
repositories and new governance decisions; none is authorized by this review.

## Human approval gate and stop condition

Recommended human decision:

```text
DECISION_CANDIDATE=APPROVE_DRAFT_PRESERVATION_MIGRATION_WITH_GWDG_CONFIRMATIONS
FROZEN_MIGRATION_APPROVED=false
SCHEMA_CHANGE_APPROVED=false
EXTERNAL_RESPONSE_SEND_APPROVED=false
CURRENT_STATUS=WAITING_FOR_HUMAN_APPROVAL
```

After approval, the next action should be the bounded GWDG response and
pre-cutover record preview. Any schema edit, record freeze, DTR write,
production cutover approval, public claim, commit, or push remains outside this
report and requires its own authorization.

## TITMAS drift check

```text
TITMAS_DRIFT_CHECK

CORE_INTEROPERABILITY_OBJECTIVE_PRESERVED=true
NEW_CONTROL_AUTHORITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
DUPLICATE_EVIDENCE_OR_VERIFICATION_CREATED=false
RUNTIME_OR_EXECUTOR_CREATED=false
CURRENT_CAPABILITY_OVERCLAIMED=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false

RESULT=PASS_WITH_RECORDED_LIMITATIONS
```
