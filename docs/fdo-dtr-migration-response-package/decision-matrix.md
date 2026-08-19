---
title: FDO DTR migration decision matrix for 21.T11966
status: DRAFT_RESPONSE_PACKAGE_WAITING_FOR_HUMAN_APPROVAL
decision_date: 2026-08-03
authority: docs/fdo-dtr-migration-governance-review.md plus recorded human decision
external_send_approved: false
---

# FDO DTR migration decision matrix for `21.T11966`

## Decision boundary

This matrix converts the approved draft-preservation strategy into bounded
migration instructions. It authorizes preparation and review of a response to
GWDG. It does **not** authorize sending that response, changing a registry
record, changing a schema, creating a release, or representing any record as
an adopted standard.

```text
APPROVE_DRAFT_PRESERVATION_STRATEGY=true
FROZEN_MIGRATION_APPROVED=false
EXTERNAL_SEND_APPROVED=false
SCHEMA_SEMANTIC_CHANGE_APPROVED=false
```

## Record decisions

| PID | Registry class that must be preserved | Governance role | Target lifecycle | Requested migration action | Accept only if | Defer/reject if |
|---|---|---|---|---|---|---|
| `21.T11966/aro-audit-profile-v1` | `FdoProfile` | Future standard candidate; non-standard and non-production today | `DRAFT/EXPERIMENTAL` | Move into the owner's new account as a draft profile without altering its meaning | PID/resolution, class, version `1.0`, timestamps, provenance, payload, relationships, and source binding are preserved | Only a frozen lifecycle is available; the class would change; or content would be silently normalized |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile` | Primary future stable-standard candidate; exact v0.1 is historical experimental input, not v1.0 | `DRAFT/EXPERIMENTAL` | Move into the owner's new account as a draft profile and preserve exact v0.1 semantics | The source payload and hashes match the approved preview; v0.1 remains distinct from every successor | The target would rewrite, alias, replace, or infer v1.0 semantics from v0.1 |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType` | Legacy/demo/history pointer only | `LEGACY/DEMO/HISTORICAL`, non-normative | Preserve in its existing class for PID and history continuity | The missing canonical-schema limitation and unconfirmed registry version remain visible; no profile status is inferred from `v1` in the PID | The target promotes it, freezes it as a normative type, or cannot retain a demo/history lifecycle |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType` | Demo/non-normative object metadata | `DEMO/HISTORICAL`, non-normative | Preserve in its existing class as demonstration history | Demo values, opaque relationships, and lack of a canonical schema are not presented as normative | The target promotes it to `FdoProfile`, treats the suffix as a frozen version, or removes its demo status |
| `21.T11966/aro-audit-demo-do-1` | `FdoService` | Demo service/instance; never a Data Type | `DEMO/HISTORICAL/INCOMPLETE_SERVICE` | Preserve only as an `FdoService` demo reference | Its service/instance identity, incomplete link state, and `TBD` key fingerprint remain explicit | It would be reclassified as any Data Type, or the target cannot represent an incomplete demo service |

## Cross-record invariants

The migration is acceptable only when all of the following are true:

1. The registry classes `FdoProfile`, `BasicInfoType`, and `FdoService` are
   retained record by record; no common-class coercion is used.
2. The two profiles enter the owner's new account with the requested
   `DRAFT/EXPERIMENTAL` governance state, or an equivalent machine-readable
   target representation. That state permits a future successor process; it
   does **not** permit overwriting the historical v0.1 record, whose payload
   and semantics must remain exact.
3. The three other records remain preservation-only demo/history assets. They
   are not inputs to a claim of standardization.
4. Existing PIDs continue to resolve. Where infrastructure changes require a
   new route, redirects or equivalent resolver continuity are documented and
   tested.
5. Original creation/update timestamps, contributors, ownership/provenance,
   source identifiers, and cross-record relationships are retained. Migration
   timestamps are additive and distinguishable from original timestamps.
6. GWDG supplies pre-cutover JSON and Handle previews plus hashes before any
   write. Source-export and target-preview envelope hashes may differ because
   of declared migration metadata. The semantic payload/canonical content must
   match exactly, and every envelope difference must be explained; an
   unexplained mismatch fails acceptance.
7. If the target cannot preserve a lifecycle or class, the affected record is
   deferred. Reclassification is not a fallback.
8. GWDG explicitly confirms that the migration is an infrastructure and
   continuity operation. It does not imply standardization, adoption,
   endorsement, certification, conformance, production readiness, or fitness
   for a particular use.

## Change classification

| Proposed action | This package's disposition |
|---|---|
| Byte-preserving migration with class/lifecycle/provenance continuity | `CONDITIONALLY_ACCEPTABLE_AFTER_PREVIEW` |
| Adding migration-only provenance that is distinguishable and non-semantic | `REVIEW_IN_PREVIEW` |
| Repairing a link, adding a missing hash, adding a lifecycle label, or adding a relationship | `DESIRABLE_BUT_NOT_AUTHORIZED_IN_THIS_PHASE` |
| Changing field meanings, required fields, schema constraints, or profile scope | `REJECT_SEMANTIC_CHANGE_NOT_APPROVED` |
| Reclassifying a record because the target lacks its original class | `REJECT_AND_DEFER_RECORD` |
| Treating the migration as a standard release or adoption event | `REJECT_GOVERNANCE_OVERCLAIM` |

## Fail-closed decision rule

```text
IF class_is_preserved
AND lifecycle_is_preserved
AND handle_values_and_pid_resolution_are_preserved
AND canonical_payload_hash_is_equal
AND every_envelope_diff_is_declared
AND provenance_and_timestamps_are_preserved
AND relationships_are_preserved_or_explicitly_accounted_for
AND no_standardization_claim_is_created
THEN migration_candidate_status=READY_FOR_SEPARATE_CUTOVER_APPROVAL
ELSE migration_candidate_status=DEFER_AFFECTED_RECORD
```

Passing this rule is not cutover approval. A named human owner must separately
approve the exact preview and migration window.

## Package status

```text
FIVE_RECORD_ROLES_PRESERVED=true
MIGRATION_POLICY=CLASS_PRESERVING_DRAFT_AND_HISTORY_ONLY
FROZEN_MIGRATION_ALLOWED=false
EXTERNAL_ACTION_TAKEN=false
COMMIT_CREATED=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
