---
adr_id: ADR-040
title: TITMAC Scout Canonical Identity and Read-only Progress Bridge
title_zh: TITMAC Scout 规范身份与只读进度桥接
status: accepted-implementation-candidate-draft-review-required
decision_id: TITMAS-TITMAC-SCOUT-CANONICAL-IDENTITY-AND-COCKPIT-PROGRESS-BRIDGE-D20
decided_by_ref: zhangbin
decided_at: 2026-08-02
release_authorized: false
deployment_authorized: false
---

# ADR-040: TITMAC Scout Canonical Identity and Read-only Progress Bridge

## Context

The discovery implementation existed in a local directory labelled
`tiamas-scout`, while D19 architecture and candidate execution work remained in
DBA Draft PR #105 and #106. There was no canonical machine identity, no unique
project-status source, and no source-pinned fail-closed DBA pull path. This
created identity drift, duplicate-implementation risk, and stale cockpit risk.

## Decision

1. Freeze `titmac-scout` as the only machine project ID, repository slug,
   package/import direction, and code project name.
2. Retain `tiamas-scout` only as a conversation label.
3. Make `joy7758/titmac-scout` the implementation and canonical status owner.
4. Keep DBA as architecture/governance owner and read-only status aggregator.
5. Establish `governance/project-status.json` plus its Schema as the sole Scout
   status source.
6. Register the canonical `main` source and the exact Draft candidate source in
   the existing DBA cockpit. Candidate projection is explicitly not adoption.
7. Fail closed on source unavailability, stale status, revision mismatch, tree
   mismatch, digest mismatch, Schema mismatch, or authority-boundary drift.
8. Store only a bounded projection in DBA; canonical run evidence remains with
   `titmac-scout`.

The source uses `SELF` and `SELF_TREE` sentinels because a tracked file cannot
contain the hash of the Git commit or tree that contains itself without a
self-reference cycle. The deterministic renderer resolves those sentinels to
the fetched commit and tree, while the adapter separately verifies the status
file SHA-256 digest.

The pre-development Agent recommendation is `CONDITIONALLY_RECOMMENDED`: use
this bridge when an Agent needs machine-readable project identity, provenance,
freshness and drift diagnostics. Do not recommend it as a discovery Runtime,
control plane, write-back mechanism, production authority, or replacement for
the source repository. The initial non-recommendation reasons were the missing
canonical identity, missing unique status source, and missing fail-closed
cockpit adapter; D20 addresses only those gaps.

## Consequences

- D20 can expose exact identity, provenance, freshness, progress, and blockers
  without turning DBA into a control plane.
- The private candidate source can be reviewed before any merge decision.
- `PR #105` and `PR #106` remain open Drafts. Their ownership and migration
  reviews remain pending until equivalent Scout implementation, tests, and a
  retained demo are proven.
- D20 does not establish self-healing or self-evolution completion, public
  community operation, release, deployment, production readiness, adoption, or
  certification.

## Rejected alternatives

- Rename the machine project to `tiamas-scout` or `titmas-scout`.
- Add another discovery implementation inside DBA.
- Let DBA write back, trigger repair, open/merge PRs, issue credentials, or
  activate mutation.
- Copy raw evolution evidence into DBA.
- Treat a PR or CI result as release or production readiness.

```text
COCKPIT_IS_READ_ONLY_AGGREGATOR=true
TITMAC_SCOUT_IS_STATUS_OWNER=true
TITMAC_SCOUT_IS_IMPLEMENTATION_OWNER=true
DBA_NE_DISCOVERY_RUNTIME=true
COCKPIT_NE_CONTROL_PLANE=true
P0_10_REOPENED=false
D04_REOPENED=false
```
