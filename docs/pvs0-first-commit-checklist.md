# PVS-0 first commit checklist

- Prepared: 2026-08-04
- Applies to: future local checkout of
  `joy7758/titmas-fdo-public-verification`
- Current authority: checklist preparation only

This checklist is not permission to create a remote, commit, push, tag,
release, or send an external message. Stop immediately if the candidate bytes,
file count, hashes, licences, or human approvals differ from this checklist.

```text
EXPECTED_FIRST_COMMIT_FILE_COUNT=43
FIRST_COMMIT_CREATED=false
REMOTE_CREATED=false
PUSHED=false
RELEASED=false
STATUS=WAITING_FOR_PUBLIC_REPOSITORY_CREATION_APPROVAL
```

## Preconditions

- [ ] Human approval for public repository creation is recorded against the
      exact repository identity and visibility.
- [ ] The final copyright holder and disclosure authority are confirmed.
- [ ] The candidate remains at exactly 43 files and passes
      `scripts/verify-all.sh` without modification.
- [ ] The future repository root will contain the **contents** of
      `out/pvs0-public-repository-candidate/`, not the staging directory name,
      cockpit repository, governance `docs/`, or private source history.
- [ ] Repository creation, first commit, public push, tag, and release are
      treated as separate decisions.

Do not proceed to commit preparation while repository creation approval is
unset.

## Exact 43 files eligible for the first commit

Paths below are relative to the future public repository root.

1. `README.md`
2. `STATUS.md`
3. `CITATION.cff`
4. `NOTICE`
5. `LICENSES/Apache-2.0.txt`
6. `LICENSES/CC-BY-4.0.txt`
7. `LICENSES/CC0-1.0.txt`
8. `DISCLOSURE_MANIFEST.yaml`
9. `SECURITY.md`
10. `GOVERNANCE.md`
11. `CHANGELOG.md`
12. `registry/five-record-identity-manifest.json`
13. `registry/five-record-relationship-map.md`
14. `registry/registry-observation-provenance.md`
15. `specification/historical-v0.1/README.md`
16. `specification/historical-v0.1/specification-snapshot.md`
17. `specification/historical-v0.1/schema-snapshot.json`
18. `specification/historical-v0.1/SOURCE_PROVENANCE.json`
19. `specification/historical-v0.1/SHA256SUMS`
20. `specification/v1-roadmap/README.md`
21. `fixtures/valid/minimal-valid-evidence.json`
22. `fixtures/invalid/missing-required-field.json`
23. `fixtures/invalid/semantic-integrity-mismatch.json`
24. `fixtures/expected-results.json`
25. `fixtures/README.md`
26. `runner/README.md`
27. `runner/pyproject.toml`
28. `runner/src/titmas_pvs0/__init__.py`
29. `runner/src/titmas_pvs0/cli.py`
30. `runner/src/titmas_pvs0/validator.py`
31. `runner/src/titmas_pvs0/hashing.py`
32. `runner/src/titmas_pvs0/result_model.py`
33. `runner/tests/test_valid_fixture.py`
34. `runner/tests/test_invalid_fixtures.py`
35. `runner/tests/test_offline_operation.py`
36. `runner/tests/test_deterministic_results.py`
37. `scripts/verify-all.sh`
38. `scripts/verify-disclosure-boundary.sh`
39. `scripts/verify-hashes.sh`
40. `scripts/build-release-manifest.sh`
41. `release/RELEASE_MANIFEST.json`
42. `release/SHA256SUMS`
43. `release/PUBLICATION_READINESS.md`

No other path is eligible under the current approval candidate.

## Files and content explicitly excluded

Do not copy, stage, or commit:

- `docs/pvs0-publication-approval-package.md`;
- `docs/pvs0-first-commit-checklist.md`;
- `out/pvs0-review-report.md`;
- the parent `out/pvs0-public-repository-candidate/` directory name;
- any other cockpit `docs/`, reports, decision packets, or `.DS_Store` files;
- `.git/`, Git worktree metadata, local branches, remotes, hooks, or reflogs
  from another repository;
- `.env`, `.env.*`, credentials, tokens, keys, provider configuration, or
  shell history;
- private repository files outside the two approved historical v0.1
  snapshots;
- real operational/customer/user data, logs, caches, test output, coverage,
  build products, wheels, archives, or temporary files;
- `__pycache__/`, `*.pyc`, virtual environments, editor settings, or OS
  metadata;
- any new v1 specification, schema, PID, implementation, or normative text;
  and
- any file not listed in the 43-path allowlist above.

If a `.gitignore` is desired for the future repository, it is a 44th file and
requires a regenerated disclosure manifest, release closure, review, and
explicit approval before inclusion. Do not add it opportunistically to the
first commit.

## Required source and Git status checks

Run these checks only in the future public-repository working directory after
repository-creation approval and before staging:

- [ ] `git rev-parse --show-toplevel` resolves to the intended new repository,
      not the TITMAS cockpit or a private source repository.
- [ ] `git remote -v` is empty unless remote creation has been separately
      approved and the exact target URL has been verified.
- [ ] `git branch --show-current` reports the intended initial branch.
- [ ] `git status --short --untracked-files=all` shows exactly the 43 expected
      paths and no deletion, rename, symlink, ignored payload, or unrelated
      file.
- [ ] `find . -type f` and the disclosure manifest enumerate the same 43
      canonical relative paths after excluding only `.git/` metadata.
- [ ] `find . -type l` returns no candidate symlink.
- [ ] No `.DS_Store`, `.env*`, `__pycache__`, `*.pyc`, archive, database,
      binary, key, or certificate file exists.
- [ ] File modes are expected: verification shell scripts are executable;
      no candidate file is group- or world-writable.

Do not use `git add .` or `git add -A`. Stage from a reviewed 43-path list so
that unrelated files cannot enter by convenience.

After staging, but before commit:

- [ ] `git diff --cached --name-only | LC_ALL=C sort` is byte-for-byte equal to
      the sorted 43-path allowlist.
- [ ] `git diff --cached --name-status` contains only `A` entries for the 43
      paths in an empty first-commit repository.
- [ ] `git diff --cached --check` returns success.
- [ ] `git status --short --untracked-files=all` shows no unstaged or extra
      file.
- [ ] `git ls-files --stage` reports exactly 43 regular tracked files and no
      submodule or symlink mode.
- [ ] A human compares the staged tree, not merely the working tree, with the
      approved manifest.

Any path mismatch is a fail-closed stop. Do not repair it by expanding the
allowlist during the commit operation.

## Required hash and test verification before commit

Run from the future public repository root against the exact unstaged or staged
bytes intended for the commit:

```bash
scripts/verify-disclosure-boundary.sh
scripts/build-release-manifest.sh --check
scripts/verify-hashes.sh
scripts/verify-all.sh
```

Required results:

```text
DISCLOSURE_BOUNDARY=PASS
RELEASE_CONTROLS_CURRENT=PASS
HISTORICAL_AND_RELEASE_HASHES=PASS
RUNNER_TESTS=10/10_PASS
TECHNICAL_READINESS=PASS
PVS0_PUBLICATION_READY=false
```

Verify the two top-level release-control fingerprints:

```bash
shasum -a 256 release/RELEASE_MANIFEST.json release/SHA256SUMS
```

Expected values for this approval candidate:

```text
53c845a410c1e00905c3dc0c7e9fe4798c9898ba2b5b38d6e9f7e8264e3a5b0a  release/RELEASE_MANIFEST.json
e585e15abbb549487e32a7a80ce33134ae2af15fd05ce1264ea069ac7b91711b  release/SHA256SUMS
```

Also verify the immutable historical snapshots:

```text
ba8fb0ae317d1474c60d7f77b8e8da1fab0eccb447213e2b669fe9e30413cd0e  specification/historical-v0.1/specification-snapshot.md
cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8  specification/historical-v0.1/schema-snapshot.json
```

If any byte changes, do not update the expected hash by hand. Return to the
candidate-generation process, regenerate all dependent controls, rerun the
disclosure review, and obtain a new human approval for the new exact bytes.

After staging, rerun the verification against a temporary export of the staged
index or otherwise prove that the staged bytes—not only the working tree—match
the approved release checksum set. No edit is allowed between final
verification and commit creation.

## Commit-message and authority checks

Before a future first commit is authorized:

- [ ] The commit message says `candidate` or `historical experimental` and
      does not claim stable standard, official FDO adoption, certification,
      full conformance, production readiness, or release.
- [ ] The author/committer identity is approved and is not treated as proof of
      copyright ownership.
- [ ] The commit contains no generated signature or signing-key operation
      unless separately authorized.
- [ ] The exact staged tree and proposed commit message receive human approval.

Creating the first commit is not authorized by the current task. If later
authorized, commit creation still does not authorize remote creation or push.

## Required human approvals before push

All items below must be explicit and refer to the exact commit hash that would
be pushed:

- [ ] Final copyright holder or holders confirmed.
- [ ] Disclosure authority for the two historical private-source snapshots
      confirmed.
- [ ] File-level `Apache-2.0`, `CC-BY-4.0`, and `CC0-1.0` policy approved,
      including required attribution/NOTICE treatment.
- [ ] Named repository owner and exact target repository identity approved.
- [ ] Public visibility approved.
- [ ] Remote creation completed under a separate authorization and the remote
      URL independently verified.
- [ ] Named maintainer and security contact accepted.
- [ ] Exact first commit hash reviewed and approved for public disclosure.
- [ ] Public push approved separately from repository creation and commit.
- [ ] Claim language and citation metadata approved.
- [ ] Rollback/disclosure-incident owner and private reporting path confirmed.

The following remain separately unauthorized even after a push approval unless
their own decisions are recorded:

- tag or GitHub release creation;
- package/DOI publication or public announcement;
- GWDG email or migration response;
- DTR/Handle changes; and
- any v1 semantic, schema, PID, or standardization action.

## Final stop gate

```text
PUBLIC_REPOSITORY_CREATION_APPROVED=false
FIRST_COMMIT_AUTHORIZED=false
PUBLIC_PUSH_AUTHORIZED=false
TAG_OR_RELEASE_AUTHORIZED=false
GWDG_EMAIL_SEND_AUTHORIZED=false
STATUS=WAITING_FOR_PUBLIC_REPOSITORY_CREATION_APPROVAL
```

Stop here until the public repository creation decision is recorded by the
authorized human.
