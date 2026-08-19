---
document_id: TITMAS-FDO-PVS0-ZENODO-PUBLICATION-OBSERVATION-v0.1
artifact_type: publication-governance-observation
status: ZENODO_PUBLICATION_COMPLETE_WITH_POST_PUBLICATION_RECONCILIATION_PENDING
observed_at: 2026-08-04T02:53:19+08:00
source_repository: joy7758/titmas-fdo-public-verification
source_branch: main
source_revision: 1dcca69d0bcc2ee94b7e3ef0c80f21536cd39d1c
source_policy: REFERENCE_ONLY
publication_authorization_decision_ref: NOT_CAPTURED_IN_COCKPIT
authority_effect: none
schema_effect: none
dtr_effect: none
handle_effect: none
---

# TITMAS FDO PVS-0 Zenodo Publication Observation

## Outcome

The approved bounded TITMAS FDO PVS-0 package is publicly archived as a Zenodo
Software record. This cockpit record synchronizes the externally verified
publication fact and the five preserved registry roles. It does not modify the
published package, the source repository, a DTR record or a Handle record.

```text
PVS0_PUBLIC_REPOSITORY_EXISTS=true
PVS0_PUBLIC_SOURCE_REVISION=1dcca69d0bcc2ee94b7e3ef0c80f21536cd39d1c
ZENODO_RECORD_PUBLISHED=true
ZENODO_RECORD_ID=21778954
ZENODO_RECORD_DOI=10.5281/zenodo.21778954
ZENODO_CONCEPT_DOI=10.5281/zenodo.21778953
DOI_RESOLUTION_VERIFIED=true
PUBLIC_ARCHIVE_FILE_COUNT=43
RUNNER_TESTS=10/10_PASS
DISCLOSURE_BOUNDARY=PASS
GITHUB_RELEASE_CREATED=false
GIT_TAG_CREATED=false
FIVE_RECORD_ROLES_PRESERVED=true
```

Publication means that the exact bounded archive is publicly citable and
retrievable. It does not mean official FDO standardization, adoption,
endorsement, certification, full conformance, interoperability, production
readiness or community governance.

## Source-pinned public facts

| Surface | Verified fact |
|---|---|
| Public source | <https://github.com/joy7758/titmas-fdo-public-verification> |
| Source revision | `1dcca69d0bcc2ee94b7e3ef0c80f21536cd39d1c` on `main`; local `HEAD` and `origin/main` agree; worktree clean |
| Zenodo record | <https://zenodo.org/records/21778954>; status `published` |
| Record DOI | <https://doi.org/10.5281/zenodo.21778954>; resolver returned the public record |
| Concept DOI | <https://doi.org/10.5281/zenodo.21778953>; resolver returned the public record |
| Resource metadata | Software; creator `Zhang, Bin`, ORCID `0009-0002-8861-1481`; version `PVS-0-candidate`; publication date `2026-08-04` |
| Zenodo timestamps | Created `2026-08-03T18:45:59.213739+00:00`; updated `2026-08-03T18:45:59.459402+00:00` |
| Zenodo record licence | Record-level metadata is `cc-by-4.0`; it does not replace the package's differentiated file licences |
| Public archive | `titmas-fdo-pvs0-candidate-1dcca69.zip`; 43 entries; 82,847 bytes |
| Archive integrity | SHA-256 `a5acbc2d42db540aa374c09906dad30869229fed482146628eabff0e46cdfcc4`; Zenodo MD5 `09defa9345bf5ff6c766c5efa88130e0` |
| GitHub release state | No tags and no GitHub Releases observed |

The public download was streamed again during this observation. Its SHA-256
matched the approved archive. The extracted archive and the clean pinned source
revision matched byte-for-byte for all 43/43 tracked files. The repository's
`scripts/verify-all.sh` completed with 10/10 runner tests, disclosure checks and
historical/release hash checks passing.

## Five preserved record roles

| Identifier | Exact registry class | Preserved lifecycle and role |
|---|---|---|
| `21.T11966/aro-audit-profile-v1` | `FdoProfile` | Draft/experimental future standard candidate; non-normative and not semantically frozen |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile` | Immutable historical experimental v0.1 and predecessor to a separate possible TITMAS v1 candidate; never rewritten as v1 |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType` | Legacy/demo/history preservation only; not a normative manifest standard |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType` | Demo and non-normative object metadata preservation only |
| `21.T11966/aro-audit-demo-do-1` | `FdoService` | Demo service/instance; never reclassified or recommended as a Data Type |

The shared prefix does not make the five records a normative suite. The source
identities `joy7758/aro-audit` and `joy7758/agent-evidence` are provenance
labels only; the fifth record's canonical repository owner remains unresolved.

## Publication/source status conflict retained

The exact published archive contains pre-publication status text and the
release-control check still reports:

```text
BLOCKED_PENDING_HUMAN_PUBLICATION_APPROVAL
```

The marker is a true pre-publication observation at source freeze time, but is
not the current external event state. The later Zenodo publication is a
separate, post-freeze observation. Both facts are retained with their temporal
scope; the embedded marker must not override the independently verified Zenodo
`published` state and must not be silently rewritten inside the existing
archival record.

```text
EMBEDDED_PREPUBLICATION_MARKERS_PRESENT=true
EMBEDDED_MARKER_SCOPE=SOURCE_FREEZE_TIME
EMBEDDED_MARKER_TRUE_AT_FREEZE_TIME=true
EMBEDDED_MARKER_IS_CURRENT_EXTERNAL_EVENT_STATE=false
ZENODO_PUBLICATION_OBSERVED_POST_FREEZE=true
TEMPORAL_CONFLICT_RESOLUTION=SEPARATE_SCOPED_OBSERVATIONS
ARCHIVE_REWRITE_REQUIRED=false
```

Any reconciliation should be a separately authorized, status-only source
commit. A corrected source state would not retroactively change the existing
record bytes; publishing corrected bytes would require an explicit decision on
a new Zenodo version. No such reconciliation, new version, tag or GitHub
Release is performed by this cockpit sync.

## Ownership and authority boundary

- `joy7758/titmas-fdo-public-verification@1dcca69…` remains the canonical source
  for the published PVS-0 bytes.
- Zenodo record `21778954` is the canonical public archival and DOI surface for
  this publication.
- DBA owns only this source-pinned governance observation and aggregation.
- DTR classification, PID resolution and Handle authority remain outside this
  cockpit record and are unchanged.
- `Zhang, Bin` is the verified Zenodo creator identity. The package's legal
  copyright-holder field remains `UNRESOLVED`; creator identity is not silently
  elevated into a legal ownership decision.

The archive preserves the package licence mapping: `Apache-2.0` for code and
schemas, `CC-BY-4.0` for documentation and specifications, and `CC0-1.0` for
fixtures and results. Zenodo currently exposes `cc-by-4.0` as its single
record-level licence metadata value. This observation does not interpret that
value as relicensing Apache-2.0 or CC0-1.0 files. Whether the record-level
metadata needs reconciliation remains a Human decision; no licence or Zenodo
metadata is changed here.

## Non-claims and effects

```text
OFFICIAL_FDO_STANDARD=false
FDO_ADOPTION=false
EXTERNAL_ENDORSEMENT=false
CERTIFICATION=false
FULL_CONFORMANCE=false
PRODUCTION_READINESS=false
COMMUNITY_GOVERNANCE=false
DTR_MIGRATION_COMPLETED=false

SOURCE_REPOSITORY_CHANGED_IN_THIS_SYNC=false
SCHEMA_CHANGED=false
FIXTURE_CHANGED=false
LICENCE_CHANGED=false
DTR_RECORD_CHANGED=false
HANDLE_RECORD_CHANGED=false
GWDG_EMAIL_SENT=false
EXTERNAL_ACTION_TAKEN_IN_THIS_SYNC=false
COMMIT_CREATED=false
PUSH_EXECUTED=false
PUBLICATION_AUTHORIZATION_DECISION_REF=NOT_CAPTURED_IN_COCKPIT
```

The already observed publication is not used to infer a durable Human decision
record that is absent from the cockpit.

## Next human decision

```text
NEXT_HUMAN_DECISION=REVIEW_POST_PUBLICATION_SOURCE_STATUS_AND_ZENODO_RECORD_LEVEL_LICENSE_METADATA_RECONCILIATION
```

This is not a blocker for DOI resolution or retrieval of the already published
exact archive. It is a provenance and current-status clarity issue for future
source consumers.

## TITMAS drift check

```text
TITMAS_DRIFT_CHECK=PASS_WITH_DISCLOSED_SOURCE_STATUS_MISMATCH
PROGRAM_MAINLINE_CHANGED=false
SPECIFICATION_PROMOTED=false
DEMO_PROMOTED_TO_NORMATIVE=false
RECOMMENDATION_ELEVATED_TO_DECISION=false
VERIFICATION_ELEVATED_TO_AUTHORIZATION=false
PUBLICATION_ELEVATED_TO_STANDARDIZATION=false
FIVE_RECORD_CLASSIFICATIONS_DRIFTED=false
NEW_CONTROL_AUTHORITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
CURRENT_CAPABILITY_OVERCLAIMED=false
```

Machine-readable projection:
[`TITMAS/publication-evidence/pvs0-zenodo-publication-observation-v0.1.json`](TITMAS/publication-evidence/pvs0-zenodo-publication-observation-v0.1.json).
