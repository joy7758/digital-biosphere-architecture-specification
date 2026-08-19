---
title: Pre-cutover preview requirements for 21.T11966 migration
status: DRAFT_REQUIREMENTS_WAITING_FOR_HUMAN_APPROVAL
external_action_authorized: false
---

# Pre-cutover preview requirements

## Purpose

This document defines the evidence GWDG should provide before a separate human
decision on cutover. It is an acceptance design, not permission to modify the
Testbed or production DTR.

## Required preview bundle

GWDG should provide one immutable bundle with a generated manifest. The bundle
should contain:

```text
21.T11966-migration-preview-<UTC_TIMESTAMP>/
  manifest.json
  source/
    aro-audit-profile-v1.json
    fdo-operation-evidence-profile-v0-1.json
    aro-audit-manifest-v1.json
    aro-audit-demo-obj-v1.json
    aro-audit-demo-do-1.json
  target/
    aro-audit-profile-v1.json
    fdo-operation-evidence-profile-v0-1.json
    aro-audit-manifest-v1.json
    aro-audit-demo-obj-v1.json
    aro-audit-demo-do-1.json
  handles/
    source.json
    target-preview.json
  relationships.json
  resolver-plan.json
  account-map.json
  hashes.sha256
  transformations.json
  rollback-or-deferral-plan.md
```

The names are recommendations, not a protocol requirement. Equivalent
machine-readable packaging is acceptable if all content below is present.

`transformations.json` should contain one entry per changed field with at
least: `record_pid`, JSON Pointer `field_path`, `source_value_hash`,
`target_value_hash`, `change_class` (`serialization-only`,
`infrastructure-metadata`, or `semantic`), `justification`, `authorized`, and
`decision_ref`. Non-sensitive values may be included for review; sensitive
administrative values should remain redacted and hash-bound. Under the current
decision, every `semantic` entry and every unreferenced authorization must
produce `FAIL_PREVIEW`.

## Per-record evidence

For each record, the source and target previews must expose or accompany:

| Evidence | Requirement |
|---|---|
| Identity | Exact PID, source registry identifier, target registry identifier, and whether the PID itself changes |
| Registry role | Source and target class, preserving `FdoProfile`, `BasicInfoType`, or `FdoService` as applicable |
| Lifecycle | Explicit source observation and proposed target label; profiles are `DRAFT/EXPERIMENTAL`, others are demo/history only |
| Payload | Complete JSON, including extension/user metadata and null/empty values; no screenshot-only preview |
| Bytes and hashes | Raw source-export and raw target-preview bytes (or unambiguous encodings), separate SHA-256 values, and lengths; envelope hashes are not assumed equal |
| Canonical form | Algorithm name/version, canonical bytes or reproducible procedure, and a canonical semantic-payload/content SHA-256 that must remain equal |
| Version | Exact version field and its location; absence must remain absence rather than being inferred from a PID suffix |
| Provenance | Original creator/contributor/account, creation and update timestamps, migration actor, tool/version, and planned migration timestamp |
| Source binding | Every repository/specification/schema URL exactly as stored before and after migration |
| Relationships | Every outgoing/incoming relationship, relationship type, target identifier, and preservation result |
| Transformation | Field-level diff with reason and classification as serialization-only, infrastructure metadata, or semantic |

Hashes authenticate the preview bytes only. They do not prove semantic
correctness, authorship, endorsement, or registry conformance.

## Cross-record relationship manifest

The preview must not infer missing semantics, but it must make observed and
proposed links inspectable. `relationships.json` should distinguish:

- relationships explicitly encoded in the Testbed records;
- human-readable references embedded in descriptions or metadata;
- proposed target relationships;
- unresolved or opaque identifiers;
- inferred relationships, if any, clearly marked `inferred=true` and excluded
  from migration unless separately approved.

At minimum, reviewers must be able to test the complementarity reference
between the two profiles, the profile reference from the demo service, and all
manifest/journal/demo-object pointers without promoting those links to
normative semantics.

## PID and resolver plan

For each PID, `resolver-plan.json` must state:

1. the current resolution result and target;
2. the expected result immediately after cutover;
3. every redirect or equivalent resolver step, including status/behavior;
4. the maximum expected interruption, cache considerations, and monitoring
   window;
5. the rollback or record-specific deferral action;
6. how historical Testbed references remain interpretable.

The plan must support record-specific deferral. One incompatible record must
not force reclassification of the other four.

The source and target Handle exports must include every index, type,
permissions/TTL where available, and decoded value, including `10320/loc`,
`HS_ALIAS`, profile/schema/service links, and administrative values appropriate
for owner review. Reviewers must compare the full value set and test both the
Handle API and user-facing resolver path. A DTR object endpoint returning
success is not, by itself, proof that the PID resolver works.

## Account and authority mapping

`account-map.json` must identify the old account, proposed new owner account,
the migration operator, and the accountable human approver. It must state
whether the account change modifies ownership or only administration. The
preview remains blocked until the owner confirms the exact new-account
identifier.

## Required declarations from GWDG

The preview response should explicitly confirm:

- class preservation is supported for all three registry classes;
- draft/experimental and demo/history states remain distinguishable;
- absence of a version field is not replaced by a version inferred from an
  identifier suffix;
- v0.1 content will not be upgraded, aliased, or normalized into a successor;
- migration does not imply standardization, adoption, official endorsement,
  certification, conformance, or production readiness;
- inability to preserve class or lifecycle leads to deferral, not
  reclassification.

## Reproducible verification

Owner-side verification should run from a clean directory and produce a
signed-off report containing:

- bundle hash and each file hash;
- JSON parse result and duplicate-key detection result;
- separate raw envelope-hash reproduction, canonical semantic-payload hash
  equality, and an allowlisted explanation for every envelope difference;
- structural JSON diffs for all five source/target pairs;
- registry-class and lifecycle assertions;
- timestamp/provenance/account assertions;
- relationship-set comparison;
- PID resolution checks before and after any separately approved cutover;
- HTTP checks for embedded public links, recorded as availability evidence,
  not semantic approval.

## Preview outcomes

| Outcome | Meaning |
|---|---|
| `PASS_FOR_CUTOVER_DECISION` | Evidence is complete and no unauthorized change is found; a separate human cutover decision is still required |
| `FAIL_PREVIEW` | Content, role, provenance, PID, or relationship preservation failed |
| `BLOCKED_MISSING_EVIDENCE` | The bundle is incomplete or the new-account authority is unresolved |
| `DEFER_RECORD` | The target cannot preserve that record's class or lifecycle |

```text
PRE_CUTOVER_PREVIEW_RECEIVED=false
CUTOVER_AUTHORIZED=false
EXTERNAL_ACTION_TAKEN=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
