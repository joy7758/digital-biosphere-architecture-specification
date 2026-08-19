# PVS-0 Zenodo final readiness review

```text
REVIEW_ID=TITMAS-PVS0-ZENODO-FINAL-READINESS-20260804
REVIEWED_ON=2026-08-04
FINAL_PUBLIC_COMMIT=fe7c1c2e0787fc753953209dfbc53b105406fad5
PUBLIC_REPOSITORY=https://github.com/joy7758/titmas-fdo-public-verification
PUBLIC_BRANCH=main
EXPECTED_ARTIFACT_COUNT=43
ZENODO_FINAL_READY=true
ZENODO_UPLOAD=false
DOI_CREATED=false
STATUS=WAITING_FOR_ZENODO_APPROVAL
```

## Final conclusion

The local Zenodo preparation package is technically aligned to public commit
`fe7c1c2e0787fc753953209dfbc53b105406fad5`. The commit is present on public
`origin/main`, contains exactly the approved four-file verification-environment
fix over the initial public commit, and retains the 43-file disclosure set.

Normal Git-clone verification and disclosure validation pass. The bounded
Runner remains `10/10 PASS`. The disclosure, historical-hash, and release-
control checks pass. The historical schema, fixtures, licenses, citation
metadata, record classifications, and v0.1 semantics were not changed by the
fix.

Technical readiness does not authorize upload or publication. No Zenodo draft
or file upload was created, no DOI was reserved or minted, and no GitHub
Release or tag was created.

## Publication scope

The proposed Zenodo record would archive the exact 43 tracked files at commit
`fe7c1c2e0787fc753953209dfbc53b105406fad5` as a bounded historical
experimental public-verification candidate. Its scope is limited to:

- identity and observed classification for five heterogeneous `21.T11966`
  records;
- lifecycle, provenance, relationship, citation, governance, security, and
  non-claim documentation;
- immutable historical experimental v0.1 specification and schema snapshots;
- three synthetic fixtures and machine-readable expected results;
- a deterministic offline Python structural/three-digest verifier and its ten
  bounded tests;
- fail-closed disclosure, hash, and release-control scripts; and
- a design-only future v1 roadmap that contains no v1 schema or normative v1
  semantics.

The record roles remain:

| Record | Preserved classification | Publication role |
|---|---|---|
| `21.T11966/aro-audit-profile-v1` | `FdoProfile` | Draft/experimental future candidate |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile` | Immutable historical experimental v0.1 |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType` | Legacy/demo/history preservation |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType` | Demo/non-normative preservation |
| `21.T11966/aro-audit-demo-do-1` | `FdoService` | Demo service/instance; never a Data Type |

## Included artifacts

The exact upload candidate is the repository's 43-path tracked tree, grouped
as follows:

- root metadata and governance: `README.md`, `STATUS.md`, `CITATION.cff`,
  `NOTICE`, `SECURITY.md`, `GOVERNANCE.md`, `CHANGELOG.md`, and
  `DISCLOSURE_MANIFEST.yaml`;
- license texts: Apache-2.0, CC-BY-4.0, and CC0-1.0;
- registry surfaces: the five-record identity manifest, relationship map, and
  registry-observation provenance;
- historical v0.1 surfaces: README, exact specification and schema snapshots,
  source provenance, and SHA-256 closure;
- future-work boundary: the design-only v1 roadmap;
- fixture surfaces: one positive fixture, two negative fixtures, expected
  results, and fixture documentation;
- verification software: Python runner package, CLI, hashing, result model,
  validator, and four test modules;
- verification controls: `verify-all.sh`, environment-aware disclosure
  verifier, hash verifier, and release-manifest builder; and
- release controls: `release/RELEASE_MANIFEST.json`, `release/SHA256SUMS`, and
  `release/PUBLICATION_READINESS.md`.

The authoritative exact path list remains in
`DISCLOSURE_MANIFEST.yaml` and is repeated in
`zenodo-release-checklist.md`.

## Reproducibility evidence

```text
GITHUB_COMMIT_VERIFIED=true
GITHUB_ORIGIN_MAIN=fe7c1c2e0787fc753953209dfbc53b105406fad5
TRACKED_FILE_COUNT=43
NORMAL_GIT_CLONE_DISCLOSURE_BOUNDARY=PASS
NORMAL_GIT_CLONE_RUNNER_TESTS=10/10_PASS
EXPORTED_TREE_DISCLOSURE_BOUNDARY=PASS
EXPORTED_TREE_RUNNER_TESTS=10/10_PASS
EXTRA_FILE_INJECTION=EXPECTED_FAIL
PRIVATE_PATH_INJECTION=EXPECTED_FAIL
CREDENTIAL_PATTERN_INJECTION=EXPECTED_FAIL
SCHEMA_CHANGED=false
FIXTURE_CHANGED=false
LICENSE_CHANGED=false
CITATION_METADATA_CHANGED=false
```

Integrity anchors:

- historical v0.1 specification SHA-256:
  `ba8fb0ae317d1474c60d7f77b8e8da1fab0eccb447213e2b669fe9e30413cd0e`;
- historical v0.1 schema SHA-256:
  `cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8`;
- environment-aware disclosure verifier SHA-256:
  `ee2a4cac17b7fd0dd1947c0c0c07d241d5fdb94509217532303ad0b985e531d3`;
- disclosure manifest SHA-256:
  `da3ba4147711569cf14c4f7b19b85a5c448baf18667b177d47c50072b66833dc`;
- release manifest SHA-256:
  `88db89b5ebd2b0892da57935a35c75ab1b006b1c5004260f601c2dcb8d733062`.

The final upload archive SHA-256 does not yet exist. It must be calculated
from an exact `git archive` payload only after the archive-building action is
separately authorized and must be included in the final upload approval.

## Explicitly excluded artifacts and effects

The proposed Zenodo payload excludes:

- `.git/` repository metadata, local branches, remotes, hooks, logs, and
  object history;
- this local Zenodo preparation directory and the local verification-fix test
  report, because neither belongs to the public repository's 43-file tree;
- private repository content outside the two approved historical snapshots;
- credentials, signing keys, customer/partner data, production evidence,
  provider responses, internal prompts, and private infrastructure details;
- any v1 schema, v1 specification bytes, or silent rewrite of historical
  v0.1;
- DTR/Handle mutations, migration actions, resolver changes, and GWDG
  communications;
- GitHub tags, GitHub Releases, packages, deployment artifacts, and
  announcements; and
- any claim or evidence of official FDO standardization, endorsement,
  certification, production readiness, adoption, community governance,
  complete conformance, or service availability.

## Remaining human decisions

The technical package is ready for a publication decision, but the following
human gates remain open:

1. Confirm the legal copyright holder or holders and authority to disclose and
   license the historical snapshots and newly created public-verification
   material.
2. Confirm creator name, ORCID, contributor treatment, and citation order.
3. Approve `dataset` as the Zenodo resource type or explicitly reconcile an
   alternative `software` classification with the source `CITATION.cff`.
4. Confirm Zenodo representation of the Apache-2.0, CC-BY-4.0, and CC0-1.0
   file-level license mapping without silently collapsing mixed rights.
5. Confirm title, description, keywords, language, version
   `PVS-0-candidate+fe7c1c2`, related identifiers, and publication date in the
   final Zenodo preview.
6. Decide whether the pre-publication candidate markers retained inside the
   exact public commit are acceptable as historical preparation evidence. If
   not, stop and require a separately authorized source update and complete
   re-review.
7. Authorize creation of the exact upload archive, record its SHA-256, and
   approve the precise archive bytes.
8. Separately authorize Zenodo draft creation/upload and then separately
   authorize pressing Publish after reviewing the final preview.
9. After publication only, verify the public record, DOI resolution, metadata
   export, and downloadable file hashes before making any DOI claim.

## Claims boundary

```text
OFFICIAL_FDO_STANDARD_CLAIMED=false
CERTIFICATION_CLAIMED=false
PRODUCTION_READINESS_CLAIMED=false
ADOPTION_CLAIMED=false
COMMUNITY_GOVERNANCE_CLAIMED=false
FULL_CONFORMANCE_CLAIMED=false
```

## Stop state

```text
ZENODO_FINAL_READY=true
ZENODO_UPLOAD=false
DOI_CREATED=false
GITHUB_RELEASE_CREATED=false
GIT_TAG_CREATED=false
GWDG_EMAIL_SENT=false
DTR_CHANGED=false
HANDLE_CHANGED=false
STATUS=WAITING_FOR_ZENODO_APPROVAL
```
