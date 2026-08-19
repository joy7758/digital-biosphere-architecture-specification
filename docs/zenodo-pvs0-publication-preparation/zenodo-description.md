# TITMAS 21.T11966 Five-Record Public Verification Slice PVS-0 Candidate

## Publication description

TITMAS FDO PVS-0 is a bounded public-verification package for five
heterogeneous records registered under prefix `21.T11966`. The proposed Zenodo
deposit would archive the exact public Git commit
`fe7c1c2e0787fc753953209dfbc53b105406fad5` from
`joy7758/titmas-fdo-public-verification`. It preserves record identity,
observed registry classification, lifecycle labels, provenance, explicit
relationships, exact historical experimental v0.1 snapshots, synthetic test
fixtures, expected results, and a deterministic offline verification runner.

The five records have distinct registry roles:

| Identifier | Preserved classification | PVS-0 role |
|---|---|---|
| `21.T11966/aro-audit-profile-v1` | `FdoProfile` | Draft/experimental future candidate; non-normative and not semantically frozen. |
| `21.T11966/fdo-operation-evidence-profile-v0-1` | `FdoProfile` | Immutable historical experimental v0.1; predecessor only to a separately governed possible v1 lineage. |
| `21.T11966/aro-audit-manifest-v1` | `BasicInfoType` | Legacy/demo/history preservation only. |
| `21.T11966/aro-audit-demo-obj-v1` | `BasicInfoType` | Demo/non-normative preservation only. |
| `21.T11966/aro-audit-demo-do-1` | `FdoService` | Demo service/instance; it is not and must never be reclassified as a Data Type. |

A shared prefix does not make these records one normative suite. The package
records only evidence-limited observed and descriptive relationships; it does
not add relationships to a Data Type Registry or infer compatibility,
inheritance, adoption, or normative dependency.

## Offline verification scope

The included Python runner operates on local files and does not contact a
registry, Handle resolver, package index, telemetry service, private
repository, or production system. For a supplied JSON object, it checks the
bundled historical JSON Schema and recomputes the three historical integrity
digests using a fixed runner-local serialization rule. The package contains
one positive and two negative synthetic fixtures with machine-readable
expected results. The exact source commit records ten passing bounded runner
tests. Normal Git-clone execution and a fresh 43-file Git export of that
commit both passed all disclosure, hash, release-control, and ten runner checks
during this preparation review.

A runner `PASS` means only that the supplied bytes satisfy the bundled schema
and the three implemented digest comparisons within the documented PVS-0
limits. It does not establish evidence truth, identity, permission,
authorization, legal non-repudiation, policy compliance, complete semantic
conformance, interoperability, or fitness for use.

The verification inventory is environment-aware without weakening the fixed
allowlist. At an exact Git top-level it verifies tracked candidate files and
allows repository metadata to remain outside the candidate inventory. In an
exported publication tree it recursively inspects the filesystem and rejects
unapproved files. This behavior was implemented, reviewed, committed, pushed,
and reverified at the exact commit cited above.

## Historical v0.1 boundary

The operation-evidence profile is preserved as an immutable historical
experimental snapshot, not rewritten as v1:

- specification SHA-256:
  `ba8fb0ae317d1474c60d7f77b8e8da1fab0eccb447213e2b669fe9e30413cd0e`;
- schema SHA-256:
  `cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8`.

The runner's serialization rule and safety limits are reproducibility rules
for this bounded package, not new v0.1 semantics and not a v1 specification.
Any future TITMAS v1 candidate requires a separate identity, specification,
versioning process, implementation evidence, conformance corpus, and human
decision.

## Status and non-claims

PVS-0 is a historical experimental public-verification candidate. Publication
of an archive would make the cited bytes persistently discoverable; it would
not make any record an official FDO standard and would not demonstrate FDO
endorsement, certification, production readiness, adoption, complete
conformance, community governance, registry migration completion, or service
availability.

The exact public source commit still contains pre-publication candidate state
markers created before the repository was pushed. They are retained as part of
the exact source history and must be reviewed before a Zenodo upload; this
description does not silently rewrite them or treat them as current DOI or
Release evidence.

The package uses a differentiated file-level license policy: Apache-2.0 for
code and schemas, CC-BY-4.0 for documentation and specifications, and CC0-1.0
for synthetic fixtures and generated results. Copyright-holder and disclosure-
authority confirmation remain human publication gates.
