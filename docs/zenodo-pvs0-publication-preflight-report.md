# TITMAS FDO PVS-0 Zenodo draft-upload preflight report

```text
REPORT_ID=TITMAS-PVS0-ZENODO-PREFLIGHT-20260804
OBSERVED_AT=2026-08-04
PUBLIC_REPOSITORY=https://github.com/joy7758/titmas-fdo-public-verification
PINNED_COMMIT=fe7c1c2e0787fc753953209dfbc53b105406fad5
TARGET_RESOURCE_TYPE=Software
EXPECTED_FILE_COUNT=43
ZENODO_UPLOAD_AUTHORIZED=true
ZENODO_UPLOAD_EXECUTED=false
DOI_PUBLISH_APPROVED=false
DOI_CREATED=false
```

## Preflight conclusion

The exact public PVS-0 source at commit
`fe7c1c2e0787fc753953209dfbc53b105406fad5` passes the technical and
disclosure checks required for a future bounded Zenodo draft upload. This
report verifies the intended upload metadata and source scope; it does not
create a Zenodo draft, build or upload an archive, reserve or create a DOI, or
publish a record.

The current task explicitly prohibits upload even though upload authorization
has been recorded. Therefore the result is a completed preflight and a stop at
the separate human publish-approval boundary.

## Required metadata verification

| Field | Required value | Evidence | Result |
|---|---|---|---|
| Creator | `Bin Zhang` | Exact commit `CITATION.cff`: `given-names: Bin`, `family-names: Zhang`; ORCID `0009-0002-8861-1481` | `PASS` |
| Zenodo resource type | `Software` | Current explicit human selection for the future Zenodo draft | `PASS_HUMAN_SELECTED` |
| Code and schema license | `Apache-2.0` | `DISCLOSURE_MANIFEST.yaml` and exact included license text | `PASS` |
| Documentation and specification license | `CC-BY-4.0` | `DISCLOSURE_MANIFEST.yaml` and exact included license text | `PASS` |
| Fixtures and generated-results license | `CC0-1.0` | `DISCLOSURE_MANIFEST.yaml` and exact included license text | `PASS` |
| Repository revision | `fe7c1c2e0787fc753953209dfbc53b105406fad5` | Local `HEAD`, local `origin/main`, remote branch, and GitHub commit API agree | `PASS` |
| Included file count | `43` | Git tree and disclosure-manifest artifact paths are identical | `PASS` |
| Package identity | PVS-0 verification package only | Fixed disclosure allowlist and repository purpose | `PASS` |

### Resource-type decision note

`Software` is the authoritative resource-type choice for the future Zenodo
draft under the current human instruction. The source repository's historical
`CITATION.cff` still says `type: dataset`, and the earlier local preparation
metadata recommended `dataset`. This report-only task does not modify either
surface. The future upload operator must use `Software` in the Zenodo draft and
must not describe the differing source value as already reconciled.

```text
ZENODO_RESOURCE_TYPE=Software
RESOURCE_TYPE_DECISION_SOURCE=CURRENT_EXPLICIT_HUMAN_INSTRUCTION
SOURCE_CITATION_TYPE=dataset
SOURCE_CITATION_CHANGED=false
```

This recorded divergence does not change the repository bytes or any PVS-0
semantics. If complete cross-surface metadata identity is required before
publication, it requires separate authorization and a new source/preparation
review.

## GitHub source-state verification

```text
LOCAL_HEAD=fe7c1c2e0787fc753953209dfbc53b105406fad5
LOCAL_ORIGIN_MAIN=fe7c1c2e0787fc753953209dfbc53b105406fad5
REMOTE_MAIN=fe7c1c2e0787fc753953209dfbc53b105406fad5
WORKTREE_CLEAN=true
TRACKED_FILE_COUNT=43
LOCAL_TAG_COUNT=0
REMOTE_TAG_COUNT=0
GITHUB_RELEASE_COUNT=0
GITHUB_STATE_UNCHANGED_BY_PREFLIGHT=true
```

The pinned commit is the verification-environment fix commit. Its parent-to-
commit diff contains only:

1. `scripts/verify-disclosure-boundary.sh`;
2. `DISCLOSURE_MANIFEST.yaml`;
3. `release/RELEASE_MANIFEST.json`; and
4. `release/SHA256SUMS`.

That commit contains no schema, fixture, license-text, or `CITATION.cff`
change.

## Verification results

The aggregate command `scripts/verify-all.sh` was executed in the normal Git
working repository at the pinned commit.

```text
DISCLOSURE_BOUNDARY=PASS
RELEASE_CONTROLS=PASS_BLOCKED_PENDING_HUMAN_PUBLICATION_APPROVAL
DISCLOSURE_HISTORICAL_RELEASE_HASHES=PASS
RUNNER_TESTS=10/10_PASS
PUBLICATION_AUTHORIZATION_INFERRED_FROM_TESTS=false
```

The ten bounded tests covered exact result fields, fixture inventory and
oracles, path-independent deterministic output, both negative fixtures,
offline/no-network behavior, the valid fixture, and historical snapshot hash
binding. A test or disclosure PASS is limited to this package and does not
prove evidence truth, official conformance, certification, adoption,
production readiness, or fitness for use.

## Included artifact scope

Only the exact 43 tracked files at the pinned commit are eligible for the
future PVS-0 draft upload:

```text
CHANGELOG.md
CITATION.cff
DISCLOSURE_MANIFEST.yaml
GOVERNANCE.md
LICENSES/Apache-2.0.txt
LICENSES/CC-BY-4.0.txt
LICENSES/CC0-1.0.txt
NOTICE
README.md
SECURITY.md
STATUS.md
fixtures/README.md
fixtures/expected-results.json
fixtures/invalid/missing-required-field.json
fixtures/invalid/semantic-integrity-mismatch.json
fixtures/valid/minimal-valid-evidence.json
registry/five-record-identity-manifest.json
registry/five-record-relationship-map.md
registry/registry-observation-provenance.md
release/PUBLICATION_READINESS.md
release/RELEASE_MANIFEST.json
release/SHA256SUMS
runner/README.md
runner/pyproject.toml
runner/src/titmas_pvs0/__init__.py
runner/src/titmas_pvs0/cli.py
runner/src/titmas_pvs0/hashing.py
runner/src/titmas_pvs0/result_model.py
runner/src/titmas_pvs0/validator.py
runner/tests/test_deterministic_results.py
runner/tests/test_invalid_fixtures.py
runner/tests/test_offline_operation.py
runner/tests/test_valid_fixture.py
scripts/build-release-manifest.sh
scripts/verify-all.sh
scripts/verify-disclosure-boundary.sh
scripts/verify-hashes.sh
specification/historical-v0.1/README.md
specification/historical-v0.1/SHA256SUMS
specification/historical-v0.1/SOURCE_PROVENANCE.json
specification/historical-v0.1/schema-snapshot.json
specification/historical-v0.1/specification-snapshot.md
specification/v1-roadmap/README.md
```

The upload payload must be created from the exact Git tree, exclude `.git/`,
contain no preparation reports from the surrounding cockpit workspace, and be
hashed and reverified before any later upload action.

## Explicit exclusions

The future draft upload must exclude:

- all private implementation repositories and private source content outside
  the two approved historical v0.1 snapshots;
- all unpublished v1 schema or normative semantics; the included v1 roadmap is
  design-only and non-normative;
- all DTR mutations, migration operations, registry writes, account changes,
  and reclassifications;
- all Handle mutations, resolver changes, redirects, and PID updates;
- all credentials, keys, customer/partner data, production evidence, internal
  prompts, model-provider responses, and private infrastructure information;
- `.git/`, local branches, hooks, remotes, logs, object history, untracked
  files, and cockpit preparation documents;
- GitHub Release, Git tag, deployment, package-distribution, or service
  artifacts; and
- production-service, official FDO standard, endorsement, certification,
  adoption, community-governance, complete-conformance, or production-
  readiness claims.

```text
PRIVATE_IMPLEMENTATION_INCLUDED=false
V1_SEMANTICS_INCLUDED=false
DTR_MODIFICATION_INCLUDED=false
HANDLE_MODIFICATION_INCLUDED=false
PRODUCTION_SERVICE_CLAIMED=false
OFFICIAL_FDO_STANDARD_CLAIMED=false
CERTIFICATION_CLAIMED=false
ADOPTION_CLAIMED=false
COMMUNITY_GOVERNANCE_CLAIMED=false
```

## Remaining human boundary

Before any future draft upload, the operator must still bind the exact archive
SHA-256 and final Zenodo form preview to the approved 43-file tree. Before
publication, a separate human decision must explicitly approve the final
uploaded bytes, creator display, `Software` resource type, three-license
mapping, title, description, related identifiers, and publication date.

`DOI_PUBLISH_APPROVED=false` remains controlling. A draft upload, if later
executed, must not be described as a published record or a created DOI.

## Stop state

```text
ZENODO_PREFLIGHT_COMPLETE=true
ZENODO_UPLOAD_APPROVED=true
ZENODO_UPLOAD_EXECUTED=false
DOI_PUBLISH_APPROVED=false
DOI_CREATED=false
GITHUB_RELEASE_CREATED=false
GIT_TAG_CREATED=false
GWDG_EMAIL_SENT=false
DTR_CHANGED=false
HANDLE_CHANGED=false
STATUS=WAITING_FOR_HUMAN_PUBLISH_APPROVAL
```
