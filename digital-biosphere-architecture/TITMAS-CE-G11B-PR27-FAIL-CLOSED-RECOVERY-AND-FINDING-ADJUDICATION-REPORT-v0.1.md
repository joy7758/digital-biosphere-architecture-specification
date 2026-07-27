# TITMAS CE-G11B PR #27 Fail-Closed Recovery and Finding Adjudication Report v0.1

## Outcome

```text
RECOVERY_STATUS=PASS
EXACT_MODEL=qwen3.7-max
RECOVERY_REQUESTS=4/4
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_EXTRACTIONS=0
JSON_REPAIRS=0
LANE_B_ADJUDICATION=QUALIFYING_5_OF_5
LANE_C_REPLACEMENT=CLEAR
LANE_D=CLEAR
SYNTHESIS=CLEAR
SYNTHESIS_CONFIDENCE=0.95
BLOCKING_FINDINGS=0
CANDIDATE_CHANGES_REQUIRED=0
MERGE_ADMISSION_RECOMMENDATION_ALLOWED=true
MERGE_AUTHORIZED=false
```

The prior Lane C failure remains immutable. The recovery used a new request identity and a
new Decision, not a retry or repair of the failed response.

## Lane B adjudication

All five original findings were preserved with their source severity:

| Finding | Source severity | Disposition | Blocking | Candidate change |
|---|---:|---|---|---|
| B-001 | HIGH | REJECTED | false | false |
| B-002 | MEDIUM | REJECTED | false | false |
| B-003 | MEDIUM | REJECTED | false | false |
| B-004 | LOW | PARTIALLY_CONFIRMED | false | false |
| B-005 | LOW | REJECTED | false | false |

B-004 remains a non-blocking documentation opportunity: the `error_class` Schema can
describe or bound its intentionally extensible string format without removing support for
`UNEXPECTED_<exception>`. This review does not authorize that source change.

## Lane C replacement

The replacement request returned `CLEAR` at confidence `0.95`:

- exact `qwen3.7-max`;
- 6/6 unique assigned files and complete reviewed-file coverage;
- all nine binding subchecks passed;
- 0 findings.

The old non-qualifying response was not reconstructed, extracted, repaired or overwritten.

## Lane D

Lane D returned `CLEAR` at confidence `0.95` with 83/83 files reviewed. Two Low findings
confirm correct historical preservation and require no correction:

- D-001: invalid timestamp is retained with an explicit erratum;
- D-002: non-qualifying v0.1 Decision review is retained while v0.2 corrects the layering.

Post-capture audit found that the direct rationale said “88 assigned files” even though both
structured arrays and the frozen contract prove 83. The direct content remains unchanged;
`D-CAP-001` records this discrepancy and synthesis uses 83 as structural truth.

## Synthesis

The exact synthesis covered all five Lane B findings and all three Lane D/capture
observations. It preserved source severity, returned `CLEAR` at confidence `0.95`, and found
no blocking issue requiring candidate changes.

This is semantic review evidence only. It is not Human Review, GitHub approval, merge
admission, merge execution, release, deployment, Standard Ready, production readiness or a
commercial offering.

## PR and authority effects

No source or candidate branch was modified. No GitHub review/comment was submitted. PR #27
was not mutated, marked ready, closed or merged. No release, deployment or website action
occurred.

## Next gate

R2 static validation plus the complete semantic review now permit preparation of a separate
PR #27 merge-admission Recommendation. That next gate must:

1. reverify the exact PR/base/head/merge-tree and all review hashes;
2. retain B-004 as a non-blocking documentation opportunity;
3. retain `D-CAP-001` and the structural 83-file truth;
4. separate merge admission from merge execution;
5. require a new independent Decision before any PR or merge action.

The next gate is not authorized by this report.
