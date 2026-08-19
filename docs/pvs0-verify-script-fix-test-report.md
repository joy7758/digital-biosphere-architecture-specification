# PVS-0 verification-script environment fix test report

```text
REPORT_ID=TITMAS-PVS0-VERIFY-ENV-FIX-20260804
OBSERVED_AT=2026-08-04
BASE_PUBLIC_COMMIT=987ece538668cf41b904a82891ddc7553ef5f231
PRIMARY_IMPLEMENTATION_REPOSITORY=joy7758/titmas-fdo-public-verification
IMPLEMENTATION_WORKTREE=/Users/zhangbin/Documents/New project/out/titmas-fdo-public-verification
AUTHORIZATION=APPROVE_VERIFY_SCRIPT_FIX=true
COMMIT_CREATED=false
PUSHED=false
```

## Outcome

The environment-handling defect is fixed in the local public-repository
worktree. `scripts/verify-all.sh` itself remains the aggregate entry point; the
fault was in the delegated disclosure inventory implemented by
`scripts/verify-disclosure-boundary.sh`.

The boundary verifier now selects one of two fail-closed inventory modes:

| Environment | Inventory source | `.git` treatment | Extra-file treatment |
|---|---|---|---|
| Candidate root is the exact Git top-level | NUL-delimited `git ls-files` inventory | Repository metadata is allowed and excluded from candidate bytes | Any additional tracked path fails the fixed 43-file allowlist; untracked working files are outside the candidate inventory |
| Candidate root is not the exact Git top-level | Recursive filesystem inventory | No repository-metadata exception is inferred | Every extra file or directory fails the fixed allowlist |

The Git mode also rejects non-UTF-8, non-canonical, duplicate/case-colliding,
symlink, missing, directory, submodule, or other non-regular tracked paths.
An exported tree nested under an unrelated parent repository is not treated as
the repository top-level and therefore remains in recursive fail-closed mode.

## Changed public-candidate files

Exactly four existing files changed; no new file was added to the 43-file
candidate:

1. `scripts/verify-disclosure-boundary.sh` — environment-aware inventory code.
2. `DISCLOSURE_MANIFEST.yaml` — refreshed byte count and SHA-256 for the changed
   script only.
3. `release/RELEASE_MANIFEST.json` — regenerated closure for the changed script
   and disclosure manifest.
4. `release/SHA256SUMS` — regenerated derived hashes.

The implementation did not modify `scripts/verify-all.sh`; it corrected the
inventory component that `verify-all.sh` calls.

## Integrity impact

Because executable bytes changed, retaining the old executable hash would have
made verification false. The changed code hash and its derived manifest
closure were therefore regenerated. All unaffected artifact hashes, all
historical snapshot hashes, and all manifest policies remain unchanged.

| Integrity item | Before | After | Reason |
|---|---|---|---|
| `scripts/verify-disclosure-boundary.sh` bytes | `17240` | `19186` | Authorized code fix |
| `scripts/verify-disclosure-boundary.sh` SHA-256 | `88b1839d90d583f7ab8d7523dcc2033290c0c6607205e296ee3e832125392ee9` | `ee2a4cac17b7fd0dd1947c0c0c07d241d5fdb94509217532303ad0b985e531d3` | Authorized code fix |
| `DISCLOSURE_MANIFEST.yaml` SHA-256 | `40d7a2c4d439c7f523b410f9d46f669960e938d8df62df5f637348b247fc396f` | `da3ba4147711569cf14c4f7b19b85a5c448baf18667b177d47c50072b66833dc` | Derived closure |
| `release/RELEASE_MANIFEST.json` SHA-256 | `53c845a410c1e00905c3dc0c7e9fe4798c9898ba2b5b38d6e9f7e8264e3a5b0a` | `88db89b5ebd2b0892da57935a35c75ab1b006b1c5004260f601c2dcb8d733062` | Derived closure |
| Historical v0.1 specification SHA-256 | `ba8fb0ae317d1474c60d7f77b8e8da1fab0eccb447213e2b669fe9e30413cd0e` | unchanged | Historical bytes preserved |
| Historical v0.1 schema SHA-256 | `cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8` | unchanged | Schema bytes preserved |

Structured before/after comparison confirmed:

```text
APPROVED_FILE_COUNT=43
DISCLOSURE_POLICY_FIELDS_CHANGED=false
DISCLOSURE_CHANGED_ARTIFACTS=scripts/verify-disclosure-boundary.sh
RELEASE_POLICY_FIELDS_CHANGED=false
RELEASE_CHANGED_FILE_ENTRIES=DISCLOSURE_MANIFEST.yaml,scripts/verify-disclosure-boundary.sh
DERIVED_SUMS_CHANGED=DISCLOSURE_MANIFEST.yaml,release/RELEASE_MANIFEST.json,scripts/verify-disclosure-boundary.sh
UNCHANGED_ARTIFACT_HASHES_PRESERVED=true
```

## Required test results

| Test | Environment and injection | Expected | Observed | Result |
|---|---|---|---|---|
| Normal Git working repository | Local public clone with `.git/`; four authorized tracked changes present | Aggregate verification passes using tracked inventory | Disclosure, release-control, hash checks and Runner passed | `PASS` |
| Fresh normal Git clone | Fresh local clone of base commit with the same four tracked worktree changes overlaid | Aggregate verification passes with `.git/` present | Aggregate verification passed | `PASS` |
| Clean exported publication tree | Exact 43 current tracked files copied without `.git/` | Recursive fail-closed verification passes | Aggregate verification and 10 Runner tests passed | `PASS` |
| Injected extra file | Exported tree plus `UNAPPROVED.txt` | Reject | `FAIL CANDIDATE_TREE_MISMATCH: missing=[]; extra=['UNAPPROVED.txt']` | `PASS_EXPECTED_FAILURE` |
| Injected tracked extra file | Git clone plus tracked `UNAPPROVED_TRACKED.txt` | Reject | `FAIL CANDIDATE_TREE_MISMATCH: missing=[]; extra=['UNAPPROVED_TRACKED.txt']` | `PASS_EXPECTED_FAILURE` |
| Injected private path | Exported tree with `/Users/example/private-repository` appended to an approved file | Reject before hash comparison | `FAIL PRIVATE_ABSOLUTE_PATH: README.md` | `PASS_EXPECTED_FAILURE` |
| Injected credential pattern | Exported tree with a synthetic `api_key=` pattern appended to an approved file | Reject before hash comparison | `FAIL CREDENTIAL_PATTERN: README.md` | `PASS_EXPECTED_FAILURE` |

The normal Git and exported-tree positive runs both reported all ten bounded
Runner tests passing. The negative values were synthetic test strings created
only in temporary trees and removed after testing; no credential or private
path was added to the repository.

## Preservation audit

```text
APPROVED_DISCLOSURE_FILE_COUNT=43
DISCLOSURE_MANIFEST_SEMANTICS_PRESERVED=true
RELEASE_MANIFEST_SEMANTICS_PRESERVED=true
UNCHANGED_HASHES_PRESERVED=true
HASH_CLOSURE_REGENERATED_FOR_CHANGED_CODE=true
RUNNER_BEHAVIOR_PRESERVED=true
RUNNER_TESTS_PASS=10
SCHEMA_CHANGED=false
FIXTURE_CHANGED=false
LICENSE_CHANGED=false
CITATION_METADATA_CHANGED=false
ZENODO_METADATA_CHANGED=false
DTR_CHANGED=false
HANDLE_CHANGED=false
```

## Authority and stop boundary

The worktree changes are not committed or pushed. The public remote still
points to base commit `987ece538668cf41b904a82891ddc7553ef5f231`; therefore
the fix is ready for review but is not yet present on GitHub. Commit, push,
Release, tag, Zenodo upload, DOI publication, DTR/Handle mutation, and external
communication require separate authorization.

```text
VERIFY_SCRIPT_FIX_READY=true
ZENODO_UPLOAD=false
RELEASE=false
STATUS=WAITING_FOR_ZENODO_APPROVAL
```
