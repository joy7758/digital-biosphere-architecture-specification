---
title: FDO public-surface remediation inventory for 21.T11966
status: DRAFT_INVENTORY_WAITING_FOR_HUMAN_APPROVAL
observation_date: 2026-08-03
schema_or_record_change_authorized: false
---

# FDO public-surface remediation inventory

## Scope and interpretation

This inventory covers the five Testbed DTR records, the URLs stored in them,
and references observed in `aro-audit`, `agent-evidence`,
`verifiable-agent-demo`, and `digital-biosphere-architecture`. It records
availability and governance defects without changing a schema, DTR record, or
repository.

The review used anonymous HTTP checks for the public user experience and
authenticated, read-only GitHub metadata where needed to distinguish a missing
file from an intentionally private repository. Results are a dated observation,
not a permanent claim about availability.

## Privacy correction

Some development repositories are intentionally private because they contain
closed-source work. For those repositories:

- an anonymous GitHub `404` is an expected privacy behavior, not proof that the
  repository or referenced file is lost;
- making the entire repository public is **not** a remediation requirement;
- the public-governance defect is that a public DTR record uses a private,
  mutable URL as its only apparent specification or source entry point;
- the preferred correction is a disclosure-reviewed, immutable public
  verification artifact hosted separately from private implementation.

This distinction matters: public verification of a public semantic claim and
publication of proprietary implementation are different requirements.

## Availability observations

| Reference embedded in or relevant to a record | Anonymous observation on 2026-08-03 | Authenticated/source observation | Classification |
|---|---|---|---|
| `https://github.com/joy7758/aro-audit/blob/main/docs/aroaudit-profile-v1.md` | HTTP `404` | The file exists in the intentionally private `joy7758/aro-audit` repository | `INTENTIONAL_PRIVATE_SOURCE` plus `MUTABLE_BRANCH_URL`; public verification gap, not repository loss |
| `https://github.com/joy7758/agent-evidence/blob/main/spec/execution-evidence-operation-accountability-profile-v0.1.md` | HTTP `404` | The file exists in the intentionally private `joy7758/agent-evidence` repository | `INTENTIONAL_PRIVATE_SOURCE` plus `MUTABLE_BRANCH_URL`; public verification gap |
| `https://aro-audit.org/manifest/v1.0` | TLS/connection failure during the check; no retrievable source | No canonical replacement was established by this audit | `PUBLIC_CANONICAL_REFERENCE_UNAVAILABLE` |
| `https://github.com/joy7758/aro-audit` | HTTP `404` anonymously | Repository exists and is intentionally private | `INTENTIONAL_PRIVATE_REPOSITORY`; the URL is also too broad to bind one exact record/schema |
| `https://raw.githubusercontent.com/joy7758/aro-audit/main/demo/manifest.json` | HTTP `404` | The path was also absent from authenticated `main` contents during this audit | `STALE_OR_MISSING_MUTABLE_PATH`, not explained solely by privacy |
| `https://raw.githubusercontent.com/joy7758/aro-audit/main/demo/journal.jsonl` | HTTP `404` | The path was also absent from authenticated `main` contents during this audit | `STALE_OR_MISSING_MUTABLE_PATH`, not explained solely by privacy |
| `https://typeapi.lab.pidconsortium.net/v1/types/schema/21.T11966/aro-audit-profile-v1` | No HTTP response before the audit timeout (`000`) | Referenced from the profile's Handle `21.T11966/JsonSchema` value | `UNKNOWN_RECHECK_REQUIRED`, not proven broken |
| `https://typeapi.lab.pidconsortium.net/v1/types/schema/21.T11966/fdo-operation-evidence-profile-v0-1` | No HTTP response before the audit timeout (`000`) | Referenced from the profile's Handle `21.T11966/JsonSchema` value | `UNKNOWN_RECHECK_REQUIRED`, not proven broken |

## PID resolution observation

On 2026-08-03, the public Handle API returned HTTP `200` and a Handle record
for all five PIDs. Four user-facing `hdl.handle.net` resolver requests returned
HTTP `200`. The request for
`21.T11966/aro-audit-demo-do-1` returned HTTP `404`, although its Handle record
existed and contained a self-referential `HS_ALIAS` value pointing to the same
PID. This is recorded as `RESOLVER_DEFECT_OR_CONFIGURATION_UNKNOWN`; the audit
does not claim that the alias caused the failure. A direct DTR object page
working is not equivalent to PID resolution continuity.

Search-engine or browser caches may still display earlier GitHub content. A
cached page is not a current canonical source and must not override the live
anonymous and authenticated observations.

## Record inventory

| PID | HTTP/public source | Mutable URL | Canonical source page | Hash coverage | Placeholder/demo values | Ownership | Citation | Lifecycle | Relationships |
|---|---|---|---|---|---|---|---|---|---|
| `21.T11966/aro-audit-profile-v1` | Private GitHub file returns anonymous `404` | Yes, `blob/main` | Missing a public record-level landing page and immutable public snapshot | DTR does not bind a source spec/schema SHA-256; no unified canonical profile schema found | No `TBD` found in the inspected profile documents; draft wording is intentional | Contributor is recorded, but target-account owner and long-term maintainer are not explicitly bound | Repository-level `CITATION.cff` exists; record/profile-specific citation missing | Draft/incubation is not reliably machine-visible in the record | Intended manifest/journal/key roles are descriptive; no complete typed relationship to the other four records |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | Private GitHub file returns anonymous `404` | Yes, `blob/main` | Missing a public record-level page/snapshot; private canonical content exists | DTR does not carry the observed schema SHA-256 `cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8`; spec hash is not registry-bound | No placeholder token found in inspected v0.1 spec/schema | Contributor is recorded; target account and profile maintainer authority need explicit confirmation | Repository citations/DOIs exist, but there is no record-specific citation identifying exact v0.1 bytes | Experimental/discussion-oriented status is not a robust machine lifecycle field | “Complementary to ARO” appears in descriptive use, but there is no explicit typed peer/successor relationship; newer candidate must not be treated as an alias |
| `21.T11966/aro-audit-manifest-v1` | `aro-audit.org` reference was unavailable | No branch URL, but target is unavailable | Missing exact public schema/source and record page | Has a journal digest in user metadata, but lacks hashes for the DTR record, claimed schema, and canonical source | `trace-demo-001` and demo counts are example data, not a stable schema contract | No explicit maintainership/account binding was found | Record-specific citation missing | No registry version field; legacy/demo/history status missing or unclear | Exact handle was not found in audited repo references; no typed link to the profile/demo object/service |
| `21.T11966/aro-audit-demo-obj-v1` | Repository-root URL is private and anonymously `404` | Repository root follows mutable default-branch state and is not a file binding | Missing exact source/schema/record page | Journal digest is present, but record/source/schema hashes are missing | Literal `ed25519-demo-key-fingerprint` and demo metadata must remain visibly non-production | No explicit owner/maintainer/account binding was found | Record-specific citation missing | Demo/non-normative status is not robustly machine-visible; PID suffix is not a registry version | `manifest_handle=21.T11966/3e197dba0a7d55e2af6` is not the listed manifest PID and returned no Testbed record/Handle; profile/service links are not typed |
| `21.T11966/aro-audit-demo-do-1` | Both raw demo file URLs return `404` and were absent from authenticated `main`; Handle exists but the user-facing resolver returned `404` | Yes, `raw/.../main` | Missing stable public service-instance page and verification result | No record, manifest, journal, or public-key binding hash in the record | `pubkey_fingerprint=TBD`; the description uses `AROAUDIT_PROFILE_V1`; demo/incomplete values are explicit risks | No explicit owner, operator, service-SLA, or maintenance authority was found | Record-specific citation missing | Demo/incomplete/historical service state is not robustly machine-visible | `content.audit_profile` uses exact PID `21.T11966/aro-audit-profile-v1`, while `content.profile` separately targets the generic `FdoServiceProfile`; no exact link to the named manifest/demo object; self-referential Handle alias needs diagnosis |

## Repository-reference inventory

| Repository/surface | Observed role | Public-surface issue | Remediation boundary |
|---|---|---|---|
| `joy7758/aro-audit` | Content authority for ARO profile drafts and related schemas/examples | Intentionally private; public DTR links cannot anonymously establish the claimed contract; DTR demo paths are absent on `main` | Keep private implementation private. Export only approved spec/schema snapshots, hashes, fixtures, lifecycle, citation, and relationship metadata to a public canonical surface |
| `joy7758/agent-evidence` | Content authority for operation-evidence v0.1 spec/schema and implementation evidence | Intentionally private; public record has a mutable private URL; repository citation does not uniquely cite the DTR profile | Publish an immutable v0.1 historical verification bundle and distinct v1 candidate materials after disclosure review; keep proprietary implementation optional/private |
| `joy7758/verifiable-agent-demo` | Public demonstration repository | No exact binding to the five DTR records was established as a canonical schema/source authority | Use only as a derived demo unless a future, explicit versioned relationship is approved; do not make it normative by proximity |
| `joy7758/digital-biosphere-architecture` | Governance/meaning and derived DPP demonstration surface | Repository is intentionally private in the live check; references ARO profile/demo service but is not their schema owner. Any separately printed/derived public material is not the same as a public canonical repository | Keep private content private; publish only approved relationship/claims-boundary material. Retain DBA as governance/specification context, not implementation or evidence truth |
| Testbed DTR | Registry of the five observed records | Lifecycle, public source integrity, citations, ownership, and relationships are incomplete or mostly human-readable | Preserve bytes/classes now; request previews. Remediate metadata only in a separately approved phase that distinguishes non-semantic governance metadata from schema semantics |

## Remediation backlog

No backlog item below is implementation authorization.

| ID | Priority | Affected records | Proposed correction | Acceptance evidence | Semantic risk |
|---|---|---|---|---|---|
| `PSR-001` | P0 | All five | Name the legal/administrative DTR owner, technical maintainer, and canonical contact | Owner-approved authority matrix and account identifier | Low if kept outside payload; must not infer authority from contributor metadata |
| `PSR-002` | P0 | Two profiles | Create disclosure-reviewed public landing pages with immutable spec/schema snapshots and SHA-256 hashes | Anonymous HTTP `200`, immutable identifier, byte-reproducible hashes, licence, security review | Medium; snapshot must match the claimed version without rewriting it |
| `PSR-003` | P0 | Operation profile | Archive exact v0.1 bytes as historical experimental; bind record, spec, schema, and citations | Manifest with hashes, immutable revision/archive ID, v0.1 lifecycle label | High if content is normalized or replaced; byte preservation required |
| `PSR-004` | P0 | Demo service | Stop presenting absent `main/demo` files as available public endpoints; preserve original record during migration and design a new sanitized verification instance | Recorded historical URLs plus a separately identified working successor/result bundle | High if the historical record is silently edited or a successor is conflated |
| `PSR-004A` | P0 | Demo service | Ask GWDG to diagnose the observed user-facing resolver `404` and self-referential `HS_ALIAS`; preserve the original Handle values in the preview before any correction | Source/target Handle exports, resolver tests, diagnosed cause, separately approved correction or deferral | High; do not delete/change Handle values based on this observation alone |
| `PSR-005` | P1 | Manifest | Establish a public history page that records the unavailable `aro-audit.org` source and the absence of a canonical schema | Citable page, hash, source-history note, non-normative lifecycle | High if a new schema is retroactively declared to be the old contract |
| `PSR-006` | P1 | Demo object | Bind a sanitized example description/fixture to an immutable revision and label all literal demo values | Fixture hash, demo label, non-production disclaimer | Medium; demo values must not become normative defaults |
| `PSR-007` | P1 | All five | Add record-level citation instructions that identify PID, registry class, lifecycle, source version, authors/contributors, and access date | `CITATION.cff`/BibTeX or landing-page citation per record; DOI only if actually minted | Low; avoid claiming external adoption or endorsement |
| `PSR-008` | P1 | All five | Define lifecycle labels and a maintenance/supersession policy | Machine-readable status plus human-readable policy | Medium; migration phase is not authorized to alter records |
| `PSR-009` | P1 | All five | Publish an explicit relationship graph distinguishing typed registry links, descriptive links, and inferences | Versioned graph with provenance; no unresolved edge presented as fact | Medium/high; relationships may change semantics and need separate approval |
| `PSR-010` | P2 | Public verification slice | Provide sanitized positive/negative fixtures and reproducible validator/result evidence without disclosing private code/data | Clean-room disclosure review; fixture hashes; independent reproduction | Medium; avoid leaking proprietary algorithms, secrets, or customer data |
| `PSR-011` | P2 | All public URLs | Replace mutable `main` references in future metadata with immutable release/commit/archive references, while retaining an audit trail of original URLs | Link manifest, redirect/history policy, immutable revision check | Medium; not part of current byte-preserving migration |

## Minimal verification slice suitable for partial public development

The smallest useful public development unit is not a copy of a private
repository. It is a separately reviewed bundle containing:

```text
public-verification-slice/
  README.md                  # exact scope, lifecycle, claims boundary
  artifact-manifest.json     # PIDs, versions, SHA-256, relationships
  specification/             # approved immutable public contract only
  schema/                    # approved schema bytes, if disclosure is allowed
  fixtures/valid/            # synthetic, non-sensitive examples
  fixtures/invalid/          # one failure per documented rule
  expected-results/          # deterministic validation reports
  verify/                    # minimal reproducible runner or API client
  CITATION.cff
  LICENSE
  SECURITY.md
```

Before implementing it, a human must choose the public repository, approve the
licence, approve each disclosed byte, decide whether validator logic is open or
only an implementation-neutral API/client is public, and authorize any schema
work. The current decision explicitly does not authorize those actions.

## Verification and close criteria

A remediation item closes only when its exact public artifact is anonymously
retrievable, immutable or version-bound, hashed, citable, lifecycle-labelled,
and linked from an owner-approved canonical page. HTTP `200` alone is
insufficient. Conversely, an anonymous `404` to an intentional private source
is not itself a demand to expose the private repository.

```text
PUBLIC_REMEDIATION_INVENTORY_READY=true
PRIVATE_REPOSITORY_DISCLOSURE_REQUIRED=false
PUBLIC_VERIFICATION_SURFACE_REQUIRED_FOR_PUBLIC_CLAIMS=true
REMEDIATION_IMPLEMENTED=false
SCHEMA_CHANGED=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
