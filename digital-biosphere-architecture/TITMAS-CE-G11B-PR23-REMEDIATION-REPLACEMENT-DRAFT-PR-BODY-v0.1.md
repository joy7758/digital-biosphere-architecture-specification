## Scope

This Draft PR exposes the remediated immutable CE-G11B integration candidate for
independent review.

```text
BASE_REF=codex/production-observability-baseline
BASE_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
HEAD_REF=codex/ce-g11b-pr23-remediation-candidate
HEAD_SHA=e6a193f4bf0d48d65649077122f0ab262460daac
VALIDATED_MERGE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
```

## Distinct evidence

R1 preserves the fail-closed selector-scope result. R2 performs the complete
validation with the historically frozen exact three-schema selector.

```text
R1_EVIDENCE_SHA=d054b5cf3880904aba84816501b07358fcfb4c06
R1_STATUS=FAIL_CLOSED_CE_SCHEMA_SELECTOR_SCOPE_MISMATCH
R2_EVIDENCE_SHA=27bc3b6e586a2259d17152a2022a85d2dd69107b
R2_STATUS=PASS_SHA_BOUND_EXACT_THREE_SCHEMA_R2_VALIDATION
TRACKED_JSON=1165/1165
SITE_TESTS=16/16
CE_SCHEMA_HASH_AND_META=3/3
CE_TESTS=49/49
SOURCE_AND_REMOTE_DRIFT=0
```

- [R1 failure result](https://github.com/joy7758/digital-biosphere-architecture-specification/blob/d054b5cf3880904aba84816501b07358fcfb4c06/digital-biosphere-architecture/TITMAS-CE-G11B-PR23-REMEDIATION-CANDIDATE-DISTINCT-EVIDENCE-VALIDATION-RESULT-v0.1.json)
- [R2 pass result](https://github.com/joy7758/digital-biosphere-architecture-specification/blob/27bc3b6e586a2259d17152a2022a85d2dd69107b/digital-biosphere-architecture/TITMAS-CE-G11B-PR23-EXACT-THREE-SCHEMA-R2-VALIDATION-RESULT-v0.1.json)
- [R2 validation report](https://github.com/joy7758/digital-biosphere-architecture-specification/blob/27bc3b6e586a2259d17152a2022a85d2dd69107b/digital-biosphere-architecture/TITMAS-CE-G11B-PR23-EXACT-THREE-SCHEMA-R2-VALIDATION-REPORT-v0.1.md)

## Historical PRs

PR #22, PR #23 and closed PR #24 remain unchanged historical review surfaces.
This Draft PR supersedes them only as the current review candidate. Closing or
editing any historical PR requires a separate Decision.

## Review boundaries

- Draft PR creation is not review approval.
- Validation PASS is not merge authorization.
- Evidence is not Truth.
- No reviewer, label, milestone or auto-merge is assigned by this action.
- No workflow dispatch, run request, merge, release, deployment, production
  readiness or commercial offering is authorized.
- Merge requires independent review evidence and a separate Merge Decision.
