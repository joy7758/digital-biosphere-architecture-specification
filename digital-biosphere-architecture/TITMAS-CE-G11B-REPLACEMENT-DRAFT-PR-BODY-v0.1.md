## Scope

This Draft PR exposes the complete immutable CE-G11B integration candidate for
independent review.

```text
BASE_REF=codex/production-observability-baseline
BASE_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
HEAD_REF=codex/ce-g11b-phase-b-integration-governance
HEAD_SHA=c608fd78d7d50d1733ddd9e19aeb6870c5a08288
VALIDATED_MERGE_TREE=bd67298eb8d869b024eaf9f03a53636c6dc377d4
```

## External validation attestation

Validation Result and Report are kept on a distinct evidence ref so that
post-execution evidence does not mutate the immutable candidate:

```text
EVIDENCE_REF=codex/ce-g11b-atomic-integration-evidence
EVIDENCE_SHA=89baeeeb42904b4ea41652d649f8be9a484f3b48
VALIDATION_STATUS=PASS_SHA_BOUND_EXTERNAL_ATTESTATION
TRACKED_JSON=1165/1165
DEPENDENCIES=23/23
SITE_TESTS=16/16
CE_SCHEMAS=3/3
CE_TESTS=49/49
SOURCE_TREE_REMOTE_DRIFT=0
```

Direct evidence:

- [Machine Result](https://github.com/joy7758/digital-biosphere-architecture-specification/blob/89baeeeb42904b4ea41652d649f8be9a484f3b48/digital-biosphere-architecture/TITMAS-CE-G11B-IMMUTABLE-CANDIDATE-MERGE-TREE-VALIDATION-RESULT-v0.1.json)
- [Validation Report](https://github.com/joy7758/digital-biosphere-architecture-specification/blob/89baeeeb42904b4ea41652d649f8be9a484f3b48/digital-biosphere-architecture/TITMAS-CE-G11B-IMMUTABLE-CANDIDATE-MERGE-TREE-VALIDATION-REPORT-v0.1.md)

## Relationship to PR #22

PR #22 remains open and unchanged as the historical Phase A review surface. This
Draft PR supersedes it only as the review candidate because PR #22 points to
`codex/ce-g11b-phase-a-decision@e032115adbe38cc84bde80cc9b10b96f6da1b428`
and does not contain the later governance and validation chain.

Closing PR #22 requires a separate Decision.

## Review boundaries

- Draft PR creation is not review approval.
- Validation PASS is not merge authorization.
- Evidence is not Truth.
- No auto-merge, reviewer, label or milestone is assigned by this action.
- No run request, workflow dispatch, merge, release, deployment, production
  readiness or commercial offering is authorized.
- Merge requires independent review evidence and a separate Merge Decision.
