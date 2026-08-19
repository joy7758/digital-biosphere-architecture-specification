# PVS-0 public repository creation approval package

- Prepared: 2026-08-04
- Decision scope: public repository creation only
- Target repository identity: `joy7758/titmas-fdo-public-verification`
- Candidate root: `out/pvs0-public-repository-candidate/`

## Decision requested

Decide whether the exact reviewed 43-file PVS-0 candidate may be used to
create an empty public repository under the selected target identity.

Approval of repository creation would not authorize copying bytes to the
remote, creating a commit, pushing, tagging, releasing, modifying DTR/Handle
records, or sending a GWDG response. Each later external action remains a
separate human gate.

```text
CANDIDATE_TREE_REVIEWED=true
EXACT_FILE_COUNT=43
TECHNICAL_VERIFICATION=PASS
PVS0_PUBLICATION_READY=false
REMOTE_CREATED=false
PUSHED=false
RELEASED=false
GWDG_EMAIL_SENT=false
DECISION_REQUESTED=PUBLIC_REPOSITORY_CREATION_ONLY
STATUS=WAITING_FOR_PUBLIC_REPOSITORY_CREATION_APPROVAL
```

## Reviewed candidate identity

The review was repeated against the exact local tree on 2026-08-04.

| Control | Reviewed value | Result |
|---|---|---|
| Actual candidate files | 43 | `PASS` |
| Disclosure manifest coverage | 43/43 | `PASS` |
| Release manifest accounting | 43/43 | `PASS` |
| Release checksum entries | 42; excludes only `release/SHA256SUMS` itself | `PASS` |
| Offline runner tests | 10/10 | `PASS` |
| Release manifest SHA-256 | `53c845a410c1e00905c3dc0c7e9fe4798c9898ba2b5b38d6e9f7e8264e3a5b0a` | `PASS` |
| Release checksum-index SHA-256 | `e585e15abbb549487e32a7a80ce33134ae2af15fd05ce1264ea069ac7b91711b` | `PASS` |
| Public publication authority | Not granted | `BLOCKED` |

The candidate preserves exactly two `FdoProfile` records, two
`BasicInfoType` records, and one `FdoService` record.
`21.T11966/aro-audit-demo-do-1` remains a demo service instance and is never
represented as a Data Type.

## Why publication is beneficial

Publication would create a narrow, inspectable trust surface without opening
the private TITMAS implementation.

- Independent humans and agents could identify the five registry records,
  their classifications, lifecycle labels, and non-normative status without
  private-repository access.
- Researchers could cite and reproduce the exact historical experimental
  v0.1 bytes and their hashes.
- Implementers could run a small offline structural and three-digest verifier
  against synthetic data without calling TITMAS services, model providers, or
  registry endpoints.
- The explicit negative fixtures and stable error codes improve teaching,
  regression testing, and tool interoperability discussions.
- The disclosure manifest, non-claims, provenance, and release closure make
  the boundary agent-readable and easier to audit than an informal archive.
- A public historical baseline can support future adoption evaluation and a
  separately governed v1 candidate without rewriting v0.1.
- Commercial value can arise from implementation, integration, support,
  validation tooling, and deployment services without claiming ownership of
  an open specification or converting the demo records into standards.

These benefits are prospective. Repository publication would not prove
adoption, demand, interoperability, standardization, certification,
production readiness, or commercial availability.

## What would be disclosed

Only the 43 files enumerated in `DISCLOSURE_MANIFEST.yaml` would be eligible
for the first public repository content review:

- lifecycle, governance, security, citation, notice, status, and non-claim
  documentation;
- a machine-readable identity manifest and human-readable relationship map for
  the five records;
- dated public registry/Handle observation provenance;
- byte-identical, owner-approved historical experimental v0.1 specification
  and schema snapshots;
- snapshot and package hashes;
- exactly three visibly synthetic fixtures and deterministic expected results;
- the bounded offline Python verifier and its ten tests;
- fail-closed disclosure/hash/release verification scripts;
- the three selected licence texts; and
- publication-readiness and release-manifest control files.

The historical source-to-snapshot comparison is owner-verified against private
source revision `09385f47a33273d8c72bbca9d3ae57aff0d5c0d9`. Public users can
independently verify disclosed bytes and hashes, but cannot independently
reproduce the private source comparison without separately authorized access.

## What is explicitly not disclosed

The public candidate excludes:

- all private repository contents outside the two approved historical v0.1
  snapshots;
- private producer, validator, service, deployment, authorization, policy,
  risk-scoring, or enterprise implementation logic;
- credentials, tokens, signing keys, private keys, provider configuration, or
  credential-bearing files;
- customer, partner, user, patient, financial, operational, or production
  data;
- internal filesystem paths, private endpoints, infrastructure topology, or
  operational evidence stores;
- model-provider prompts, hidden prompts, model responses, or model-provider
  credentials;
- internal governance deliberations not required to understand the public
  verification boundary;
- unpublished v1 normative semantics, a v1 schema, a v1 PID, or a claim that
  v1 exists;
- a full v0.1 conformance implementation, reference-closure verification,
  evidence-truth proof, authorization proof, or certification service;
- the cockpit approval documents, `out/pvs0-review-report.md`, unrelated
  `docs/` content, and any existing private repository history; and
- Git metadata, local caches, `.DS_Store`, `.env*`, logs, build artifacts,
  wheels, archives, or temporary files.

Repository identities retained in provenance are labels only. They do not
disclose the remaining repository contents or establish legal ownership.

## Copyright unresolved items

`COPYRIGHT_HOLDER_REQUIRES_HUMAN_CONFIRMATION=true` remains a blocking gate.
Before any public bytes are pushed, a human with appropriate authority must
resolve and record:

1. the legal copyright holder or holders for the historical v0.1
   specification and schema;
2. the authority to disclose those exact private-source snapshots publicly;
3. the authority to license the specification snapshot under `CC-BY-4.0` and
   the schema snapshot under `Apache-2.0`;
4. the copyright and licensing authority for the new runner, scripts,
   documentation, fixtures, and expected results;
5. whether the named CFF author is an authorship/citation statement only or
   also represents a copyright owner;
6. any attribution text that must appear in `NOTICE`, `CITATION.cff`, or
   individual files; and
7. the named maintainer, security contact, release authority, and publication
   authority after repository creation.

Repository ownership, Git authorship, ORCID metadata, or prior registration of
a PID must not be treated as sufficient evidence of copyright ownership or
licensing authority. This package records governance questions and is not
legal advice.

## Licensing decision points

The selected file-level policy is complete for 43/43 candidate files:

| Material | Selected licence | Human confirmation required |
|---|---|---|
| Runner, tests, scripts, `pyproject.toml`, machine schema | `Apache-2.0` | Confirm authority to grant the licence and required NOTICE/attribution treatment. |
| Specifications, documentation, governance/registry metadata, citation and readiness prose | `CC-BY-4.0` | Confirm copyright holder, attribution form, and authority to publish. |
| Synthetic fixtures, expected results, generated checksum/result material | `CC0-1.0` | Confirm authority to apply the waiver/dedication and acceptable jurisdictional treatment. |
| Included licence texts | Corresponding licence text | Preserve exact official text and its existing hash. |

Some files intentionally lack inline SPDX headers. The disclosure and release
manifests carry the authoritative 43/43 mapping. The immutable historical
snapshots must not be edited merely to add headers; any approved attribution
clarification should be made in separate metadata unless legal review requires
a new, separately reviewed disclosure candidate.

Changing any licence, attribution, snapshot byte, or file classification makes
the current hashes and approval package stale and requires full regeneration
and review.

## External communication restrictions

Until separate approval is recorded, no person or agent acting from this
package may:

- create or configure the GitHub remote;
- upload, push, mirror, publish, or otherwise transmit candidate bytes;
- create a tag, GitHub release, package publication, DOI, announcement, or
  public documentation link;
- send the prepared GWDG email or any migration instruction;
- modify DTR or Handle records, redirects, relationships, or account ownership;
- describe PVS-0 or any of the five records as officially adopted, endorsed,
  standardized, certified, conformant, production-ready, or commercially
  available; or
- treat model review, local tests, repository creation approval, or a first
  commit as push/release/publication authority.

Public repository creation approval, if granted, authorizes only creation of
the empty named repository with the separately approved visibility and owner.
It does not authorize the first commit or public exposure of content.

## Rollback considerations

Before any push, rollback is straightforward and recoverable: stop, preserve
the candidate and review evidence, and abandon or keep the empty local/remote
repository without uploading content.

After a public push, deletion or history rewriting cannot reliably retract
information already cloned, cached, indexed, mirrored, or archived. Therefore:

- treat the first public push as the irreversible disclosure boundary;
- rerun all checks against the exact staged bytes immediately before commit
  and again before push;
- never use force-push or history rewriting as the default incident response;
- if sensitive content is detected, stop publication, preserve evidence,
  privately notify the authorized owner/security contact, and rotate affected
  credentials through their owning system;
- do not alter the immutable v0.1 snapshot in place; use a separate erratum or
  successor candidate for explanatory corrections;
- use the release manifest and checksum index to identify the exact approved
  or last-known-good byte set; and
- require a new disclosure review, hashes, approval package, and push decision
  for any remediation candidate.

An empty repository can be deleted if separately authorized, but deletion is
not a substitute for a disclosure incident plan once content has been pushed.

## Approval record to be completed by a human

```text
APPROVE_PUBLIC_REPOSITORY_CREATION=true|false
APPROVED_REPOSITORY_IDENTITY=joy7758/titmas-fdo-public-verification|UNAPPROVED
APPROVED_VISIBILITY=PUBLIC|UNAPPROVED
COPYRIGHT_AND_DISCLOSURE_AUTHORITY_CONFIRMED=true|false
FIRST_COMMIT_AUTHORIZED=false
PUBLIC_PUSH_AUTHORIZED=false
TAG_OR_RELEASE_AUTHORIZED=false
GWDG_EXTERNAL_RESPONSE_AUTHORIZED=false
V1_SEMANTIC_CHANGE_AUTHORIZED=false
```

The approval record is intentionally unset. Current status:

```text
STATUS=WAITING_FOR_PUBLIC_REPOSITORY_CREATION_APPROVAL
```

## TITMAS drift check

```text
TITMAS_DRIFT_CHECK

CORE_INTEROPERABILITY_OBJECTIVE_PRESERVED=true
NEW_CONTROL_AUTHORITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
DUPLICATE_EVIDENCE_OR_VERIFICATION_CREATED=false
RUNTIME_OR_EXECUTOR_CREATED=false
CURRENT_CAPABILITY_OVERCLAIMED=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
RESULT=PASS_WITH_RECORDED_LIMITATIONS
```

The package proposes a future public projection of an existing bounded
candidate. It creates no runtime, executor, truth source, certification
authority, launch authority, or permission to publish.
