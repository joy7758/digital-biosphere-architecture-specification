---
title: Draft reply to GWDG on migration of 21.T11966 records
status: UNSENT_DRAFT_WAITING_FOR_HUMAN_APPROVAL
external_send_approved: false
---

# Draft reply to GWDG

> **Send gate:** This is a review draft only. `EXTERNAL_SEND_APPROVED=false`.
> Do not send, paste into an external ticket, or treat it as migration
> authorization until a human owner approves the exact text.

**Subject:** Governance requirements for migration of five `21.T11966` records

Dear GWDG DTR team,

Thank you for arranging continuity from the FDO Testbed DTR to the new
production DTR. We have completed an owner-side governance review of the five
records registered under prefix `21.T11966`.

We would like the migration to preserve the records and their history without
prematurely freezing their semantics. Please use the following treatment:

| Record | Preserve as | Requested lifecycle/treatment |
|---|---|---|
| `21.T11966/aro-audit-profile-v1` | `FdoProfile` | Migrate into the owner's new account as `DRAFT/EXPERIMENTAL`; future standard candidate, not a standard today |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile` | Migrate into the owner's new account as `DRAFT/EXPERIMENTAL`; preserve exact v0.1 semantics and identity |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType` | Preserve for legacy/demo/history only; non-normative |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType` | Preserve as demo/non-normative history only |
| `21.T11966/aro-audit-demo-do-1` | `FdoService` | Preserve as a demo service/instance; never reclassify it as a Data Type |

For all five records, please preserve existing PID resolution (including any
needed redirect or resolver-continuity behavior), original timestamps,
provenance and contributor information, ownership/account history, payloads,
and relationships. A migration timestamp may be added as separate provenance,
but it should not replace the original record timestamps.

Before cutover, please provide:

- a complete source and proposed-target JSON preview for each record;
- a complete source and proposed-target Handle-value export for each PID,
  including `10320/loc`, aliases, type/schema/service links, and resolution
  behavior;
- separate raw-byte SHA-256 hashes for each source export and target preview,
  plus the canonicalization method and canonical payload/content hash;
- a field-level explanation for every allowed envelope difference, such as an
  additive migration timestamp or target account field, while preserving exact
  semantic payload/content;
- the source-to-target account mapping and the identifier of the owner's new
  account;
- the proposed registry class and lifecycle status for each record;
- a relationship manifest covering links among the five records and any
  underlying profile or service identifiers;
- the planned PID-resolution/redirect behavior and a rollback or deferral
  procedure.

If the target system cannot preserve a record's current registry class or the
requested draft/demo/history lifecycle, please **defer that record** and tell
us which capability is unavailable. Please do not reclassify it as a
workaround. In particular, `21.T11966/aro-audit-demo-do-1` must remain an
`FdoService` and must not become a Data Type.

Please also explicitly confirm that this infrastructure migration does not, by
itself, imply standardization, adoption, official FDO endorsement,
certification, conformance, production readiness, or fitness for a particular
use. The two profiles remain draft/experimental and the remaining three
records remain non-normative demo/history artifacts.

No schema semantic change or record-content correction is authorized as part
of this migration request. Any proposed transformation should be identified
in the preview and held for separate owner review.

Identifier continuity preserves history; it does not validate the referenced
schema/source contracts or cure current public-verifiability gaps.

Once we receive the previews and confirmations, we will perform an owner-side
acceptance review and respond with a separate cutover decision.

Kind regards,

`[OWNER NAME]`
`[OWNER ACCOUNT / ORGANIZATION]`
`[CONTACT ADDRESS]`

## Human completion items before any send

- Replace all three bracketed signature fields.
- Confirm the exact new-account identifier and whether all five records have
  the same legal/operational owner.
- Confirm the requested GWDG contact and channel.
- Decide whether to attach the decision matrix and preview requirements.
- Re-check that no GWDG migration window has made the wording stale.
- Record a new explicit decision: `EXTERNAL_SEND_APPROVED=true`.

```text
EMAIL_STATE=UNSENT_DRAFT
EXTERNAL_ACTION_TAKEN=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
