---
title: Migration acceptance checklist for 21.T11966
status: DRAFT_CHECKLIST_WAITING_FOR_HUMAN_APPROVAL
cutover_approved: false
---

# Migration acceptance checklist

Use this checklist only against a named, hashed GWDG preview bundle. A checked
box records evidence review; it is not an authorization to write to a DTR.

## 1. Authority and bundle

- [ ] The exact preview bundle name, timestamp, SHA-256, reviewer, and review
  date are recorded.
- [ ] The owner has confirmed the new-account identifier and authority for all
  five records.
- [ ] `APPROVE_DRAFT_PRESERVATION_STRATEGY=true` remains current.
- [ ] `FROZEN_MIGRATION_APPROVED=false` and
  `SCHEMA_SEMANTIC_CHANGE_APPROVED=false` remain enforced.
- [ ] Source and target JSON previews are complete and machine-readable.
- [ ] Separate source-export and target-preview raw hashes reproduce; they are
  not required to be equal when declared migration-envelope metadata differs.
- [ ] Canonical semantic-payload/content hashes reproduce and are equal.
- [ ] Every transformation is explained and classified.
- [ ] Complete source and target-preview Handle values are present, including
  `10320/loc`, aliases, type/schema/service links, and resolution behavior.

## 2. Record-by-record acceptance

### `21.T11966/aro-audit-profile-v1`

- [ ] Target class is exactly `FdoProfile`.
- [ ] Target lifecycle is the requested `DRAFT/EXPERIMENTAL` state or an
  owner-approved machine-readable equivalent that cannot be read as
  stable/normative.
- [ ] It is assigned to the confirmed owner account.
- [ ] Registry version `1.0`, content, source binding, timestamps, and
  provenance are preserved.
- [ ] No language implies standardization, adoption, production readiness, or
  conformance.

### `21.T11966/fdo-operation-evidence-profile-v0-1`

- [ ] Target class is exactly `FdoProfile`.
- [ ] Target lifecycle is the requested `DRAFT/EXPERIMENTAL` state or an
  owner-approved machine-readable equivalent that cannot be read as
  stable/normative.
- [ ] It is assigned to the confirmed owner account.
- [ ] Version `0.1` and exact v0.1 semantics are preserved.
- [ ] It is not rewritten, aliased, redirected, or represented as TITMAS v1.0.
- [ ] Canonical semantic-payload/content hashes are equal; raw source/target
  envelope hashes separately reproduce and every difference is allowlisted.

### `21.T11966/aro-audit-manifest-v1`

- [ ] Target class is exactly `BasicInfoType`.
- [ ] Lifecycle is the requested legacy/demo/history, non-normative state or an
  owner-approved machine-readable equivalent that cannot imply a profile.
- [ ] The target does not invent a registry version from `v1` in the PID.
- [ ] Its missing/unavailable canonical schema reference is not concealed by a
  silent substitution.

### `21.T11966/aro-audit-demo-obj-v1`

- [ ] Target class is exactly `BasicInfoType`.
- [ ] Lifecycle is the requested demo/history, non-normative state or an
  owner-approved machine-readable equivalent that cannot imply a profile.
- [ ] It is not promoted to a profile or normative type.
- [ ] Literal demo values and opaque relationships are preserved as historical
  data, not endorsed as valid production values.

### `21.T11966/aro-audit-demo-do-1`

- [ ] Target class is exactly `FdoService`.
- [ ] It remains a demo service/instance and is never described as a Data Type.
- [ ] The `TBD` public-key fingerprint and currently unavailable demo links are
  neither concealed nor silently repaired in this migration.
- [ ] No production-readiness statement is added.

## 3. Cross-record integrity

- [ ] All five PIDs retain resolution continuity, with redirects/equivalent
  behavior tested where applicable.
- [ ] Both the Handle API and the end-user resolver route have been tested;
  direct DTR object availability is not substituted for resolver continuity.
- [ ] Original creation/update timestamps are retained; migration timestamps
  are additive.
- [ ] Contributors, owners, accounts, and migration actors are distinguishable.
- [ ] All explicitly encoded relationships have identical typed endpoints, or
  an owner-approved, documented infrastructure-only mapping.
- [ ] Description/metadata references are not silently converted into
  normative registry relationships.
- [ ] The two profiles remain distinct but complementary.
- [ ] Demo/history records do not become normative dependencies of either
  profile.

## 4. Public-surface and source-binding checks

- [ ] Every embedded HTTP(S) URL has a recorded status from an anonymous
  client and a timestamp.
- [ ] Mutable branch URLs are inventoried; none is silently replaced during
  this phase.
- [ ] Missing record/spec/schema hashes are inventoried rather than fabricated.
- [ ] `TBD`, placeholder, demo, unresolved, and opaque values remain visibly
  classified.
- [ ] Repository-level citation files are not misrepresented as
  record-specific citation instructions.
- [ ] Public-link availability is treated separately from semantic identity.

## 5. Claims and declarations

- [ ] GWDG confirms migration is an infrastructure-continuity action.
- [ ] GWDG confirms migration does not imply official FDO standardization,
  adoption, endorsement, certification, conformance, or production readiness.
- [ ] The owner-facing migration log uses `draft`, `experimental`, `demo`,
  `historical`, and `non-normative` consistently.
- [ ] No demo has been promoted into a normative standard.

## 6. Failure and deferral

- [ ] A record-specific rollback/deferral plan exists.
- [ ] Any class mismatch results in `DEFER_RECORD`.
- [ ] Any unavailable lifecycle that would cause semantic promotion results in
  `DEFER_RECORD`.
- [ ] Any unexplained content/hash mismatch results in `FAIL_PREVIEW`.
- [ ] Any unresolved owner/account mismatch results in
  `BLOCKED_MISSING_AUTHORITY`.

## 7. Separate human decision

| Role | Name | Decision | Date | Preview bundle hash |
|---|---|---|---|---|
| Registry-record owner | `[UNRESOLVED]` | `[APPROVE / DEFER / REJECT]` | `[UTC]` | `[SHA-256]` |
| Technical verifier | `[UNRESOLVED]` | `[PASS / FAIL / BLOCKED]` | `[UTC]` | `[SHA-256]` |
| Governance approver | `[UNRESOLVED]` | `[APPROVE / DEFER / REJECT]` | `[UTC]` | `[SHA-256]` |

No cutover may be inferred from an unsigned checklist, a technically passing
preview, or a prior approval of the draft-preservation strategy.

```text
MIGRATION_RESPONSE_READY_FOR_REVIEW=true
CUTOVER_APPROVED=false
EXTERNAL_ACTION_TAKEN=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
