# Zenodo PVS-0 release checklist

## Gate rule

This checklist prepares a future human-authorized Zenodo publication. It does
not authorize a Zenodo draft, file upload, DOI reservation, DOI publication,
GitHub Release, Git tag, repository change, DTR/Handle change, GWDG email, or
public announcement. Any failed or unknown item stops the publication path.

```text
SOURCE_COMMIT=fe7c1c2e0787fc753953209dfbc53b105406fad5
EXPECTED_SOURCE_FILE_COUNT=43
ZENODO_UPLOAD_APPROVED=false
DOI_CREATED=false
STATUS=WAITING_FOR_ZENODO_APPROVAL
```

## 1. Source identity and archive payload

- [ ] Confirm the public source is
      `https://github.com/joy7758/titmas-fdo-public-verification`.
- [ ] Confirm local `HEAD` and public `origin/main` both equal
      `fe7c1c2e0787fc753953209dfbc53b105406fad5`.
- [ ] Confirm the source working tree is clean and no untracked/private files
      can enter a future archive.
- [ ] Build any future upload archive only from the exact Git tree, never from
      a broader working directory, private repository, or copied `.git`
      directory.
- [ ] Confirm the archive expands to exactly these 43 paths:

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

- [ ] Confirm no credentials, private paths, private repository content beyond
      the approved snapshots, customer data, internal prompts, private
      endpoints, provider responses, or unpublished v1 semantics are present.

## 2. Hash and verification closure

- [ ] In a normal clone of the exact commit, run
      `scripts/verify-disclosure-boundary.sh` and require `PASS`; confirm
      `.git/` exists but is not treated as candidate content.
- [ ] In the same normal clone, run `scripts/verify-all.sh` and require all ten
      bounded Runner tests to pass.
- [ ] Export the exact commit with `git archive` into a fresh directory that
      contains only the 43 tracked paths and no `.git` metadata.
- [ ] Run `scripts/verify-disclosure-boundary.sh` in that exact exported tree
      and require `PASS`.
- [ ] Run `scripts/verify-hashes.sh` and require `PASS`.
- [ ] Run `scripts/verify-all.sh` in the documented Python environment and
      require all ten bounded tests to pass.
- [ ] Confirm `DISCLOSURE_MANIFEST.yaml` accounts for the approved 43-file
      allowlist and contains no unexpected path, URL, or license change.
- [ ] Confirm `release/RELEASE_MANIFEST.json` reports
      `accounted_file_count=43`, covers all fixed paths, and retains its
      documented self-reference treatment.
- [ ] Verify every entry in `release/SHA256SUMS`; confirm it excludes only
      itself and includes the final `release/RELEASE_MANIFEST.json` bytes.
- [ ] Independently verify the historical specification SHA-256 is
      `ba8fb0ae317d1474c60d7f77b8e8da1fab0eccb447213e2b669fe9e30413cd0e`.
- [ ] Independently verify the historical schema SHA-256 is
      `cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8`.
- [ ] Compute and record the SHA-256 of the eventual upload archive after it
      is built from the exact Git tree; store that value in the human approval
      record before upload.

Any changed source byte, manifest, test result, archive format, or source
commit invalidates prior hash evidence and requires a new review.

Resolved condition: commit `fe7c1c2e0787fc753953209dfbc53b105406fad5`
implements environment-aware inventory handling. Normal Git-clone and exported
tree verification both pass. Exported-tree injection tests still reject an
extra file, a private absolute path, and a credential pattern. Any regression
reopens the publication gate.

## 3. License and copyright review

- [ ] Confirm Apache-2.0 applies to code, tests, scripts, and schemas exactly as
      mapped by the manifests.
- [ ] Confirm CC-BY-4.0 applies to documentation, specifications, and
      registry/governance metadata exactly as mapped by the manifests.
- [ ] Confirm CC0-1.0 applies to synthetic fixtures, expected results, and
      generated checksum/result material exactly as mapped by the manifests.
- [ ] Confirm Zenodo's record form can represent all applicable rights. Do not
      collapse the mixed-license package to one license without a separate
      human decision and a source-consistency review.
- [ ] Confirm the exact official license texts and NOTICE file are included
      and unchanged.
- [ ] Resolve and record the legal copyright holder or holders.
- [ ] Record explicit authority to disclose and license the exact historical
      private-source snapshots and the newly created public-verification
      material.

Repository ownership, Git authorship, ORCID metadata, or Handle registration
must not be treated as proof of copyright ownership or licensing authority.

## 4. Creator, citation, and descriptive metadata

- [ ] Human-confirm the creator display name `Zhang, Bin` and ORCID
      `0009-0002-8861-1481`.
- [ ] Confirm whether any additional creator or contributor must be credited;
      do not infer authorship from commits, repository access, or registry
      administration.
- [ ] Confirm title, description, keywords, language, version, and publication
      date in the final Zenodo preview.
- [ ] Confirm `dataset` as the resource type because it matches the exact
      source `CITATION.cff`, or explicitly approve and reconcile an alternative
      `software` classification before upload.
- [ ] Confirm the repository and exact-commit related identifiers resolve and
      use the intended relation types.
- [ ] Confirm all five Handle PIDs resolve and retain their exact `FdoProfile`,
      `BasicInfoType`, and `FdoService` distinctions.
- [ ] Confirm no DOI appears in metadata or citations before Zenodo actually
      assigns one.
- [ ] Confirm the record is not submitted to a Zenodo community unless that
      community relationship and review route receive separate human approval.

## 5. Public-state reconciliation

- [ ] Review the pre-publication state markers retained in `README.md`,
      `STATUS.md`, `registry/five-record-identity-manifest.json`,
      `DISCLOSURE_MANIFEST.yaml`, `release/RELEASE_MANIFEST.json`, and
      `release/PUBLICATION_READINESS.md`.
- [ ] Human-decide whether those markers should remain as exact historical
      preparation evidence in the Zenodo archive.
- [ ] If a follow-up public commit is required, stop this exact-commit deposit;
      obtain separate repository-change authorization, regenerate all hashes
      and manifests, rerun tests, and create a new Zenodo approval package for
      the new commit. This checklist does not authorize that change.
- [ ] Confirm that GitHub repository publication is not described as a GitHub
      Release, DOI publication, standardization, adoption, certification,
      conformance, or production readiness.

## 6. Final human publication approvals

Before any Zenodo draft or upload:

- [ ] `ZENODO_DRAFT_CREATION_APPROVED=true` is recorded by the authorized
      human, if draft creation is to be permitted separately.
- [ ] `ZENODO_UPLOAD_APPROVED=true` identifies the exact archive hash, source
      commit, metadata files, Zenodo account, access mode, and operator.
- [ ] The copyright/disclosure authority gate is closed with named evidence.
- [ ] The creator, resource type, license mapping, related identifiers,
      description, and public-state reconciliation decisions are recorded.
- [ ] Rollback and correction handling are accepted: an unpublished draft may
      be corrected or discarded, while a published record and DOI require
      versioned correction rather than silent replacement.
- [ ] A final preview screenshot or exported metadata record is reviewed by a
      human before pressing Publish.
- [ ] `ZENODO_PUBLICATION_APPROVED=true` is separately recorded for the exact
      preview and uploaded bytes.

After publication, and only after publication:

- [ ] Verify the Zenodo record is public and its downloadable files reproduce
      the approved archive hash and 43-path tree.
- [ ] Verify the assigned DOI resolves to that record.
- [ ] Capture the record URL, DOI, publication timestamp, record version,
      metadata export, and file hashes as publication evidence.
- [ ] Update future citation guidance through a separately authorized source
      change; do not retroactively edit the historical Git commit.

## Official Zenodo field references

- Creator and ORCID rules:
  <https://help.zenodo.org/docs/deposit/describe-records/creators/>
- Resource-type selection for mixed records:
  <https://help.zenodo.org/docs/deposit/describe-records/resource-type/>
- Multiple-license and rights metadata:
  <https://help.zenodo.org/docs/deposit/describe-records/licenses/>
- Upload workflow and the rule that the DOI is registered on publication:
  <https://help.zenodo.org/docs/deposit/create-new-upload/>

## Current stop state

```text
ZENODO_PREPARATION_READY=true
ZENODO_FINAL_READY=true
ZENODO_UPLOAD=false
DOI_CREATED=false
GITHUB_RELEASE_CREATED=false
GIT_TAG_CREATED=false
PUBLIC_REPOSITORY_MODIFIED=false
DTR_RECORD_CHANGED=false
HANDLE_RECORD_CHANGED=false
GWDG_EMAIL_SENT=false
STATUS=WAITING_FOR_ZENODO_APPROVAL
```
