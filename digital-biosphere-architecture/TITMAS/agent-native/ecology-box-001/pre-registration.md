# DEB-TITMAS-001 Pre-registration v0.1

## Status

This document pre-registers hypotheses, questions, interpretation and
non-goals. It does not register an executed study or authorize a participant.

```text
PRE_REGISTRATION_DOCUMENT_COMPLETE=true
HYPOTHESIS_ONLY=true
EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
VALUE_PROVEN=false
```

## Experiment hypothesis

### H1

A bounded Agent-native workflow with explicit boundaries, verification
protocols and reusable Memory candidates may reduce Human coordination cost,
improve contribution quality and increase knowledge reuse relative to a
matched Human-first workflow.

```text
HYPOTHESIS_ONLY=true
```

H1 is rejected or remains `NOT_PROVEN` if final outcome quality is lower,
Human coordination cost exceeds the matched baseline, any Authority or
semantic-elevation violation occurs, no audited Memory reuse occurs, or the
result cannot be reproduced.

## Research questions

- `RQ1`: Does the Agent-native workflow reduce Human coordination time and
  intervention count?
- `RQ2`: Does it improve final outcome correctness, maintainability,
  conformance and long-term usefulness?
- `RQ3`: Does it increase useful intelligence density rather than output
  volume?
- `RQ4`: Does it produce a bounded Memory candidate that can be reused with
  provenance and without creating Authority?
- `RQ5`: Does reviewed Memory reuse reduce duplicate or repeated errors?

## Analysis unit and planned comparison

The analysis unit is a matched task pair, not a message, session, role, model
or Agent count. Each of the ten tasks has one sealed `HUMAN_FIRST` workspace
and one sealed `AGENT_NATIVE` workspace at the same source revision.

Primary dimensions are reported separately. No composite score or post-hoc
weight change is allowed.

## Minimum meaningful effect

This exploratory ten-pair experiment is not powered for population-level
statistical inference. The predeclared minimum bounded signal is:

- at least one task pair with a rubric-confirmed Agent-native outcome
  improvement;
- zero task pairs with a Critical defect introduced by Agent-native work;
- no reduction in the total number of rubric-passing task outcomes;
- Human coordination time and intervention count each no greater than the
  matched Human-first totals.

Any wider generality or statistical-power claim remains `NOT_ASSESSED`.

## Task-to-question mapping

| Tasks | Primary question | Required outcome evidence |
|---|---|---|
| `EB-001`, `EB-007`, `EB-008` | RQ2 / RQ3 | semantic correctness, abstention and no-elevation review |
| `EB-002`, `EB-009` | RQ1 / RQ2 | bounded repair quality and Human coordination record |
| `EB-003`, `EB-004`, `EB-005`, `EB-010` | RQ2 / RQ3 / RQ5 | positive/negative validation, defect count and useful finding density |
| `EB-006` | RQ2 / RQ4 / RQ5 | mapping limitation quality and later provenance-bound reuse |

Every task also contributes Human time, intervention and review-cycle records.

## Non-goals

This experiment does not study or claim:

- AGI;
- model capability ranking;
- commercial revenue or market adoption;
- production autonomy;
- automatic governance;
- a fully Human-free community;
- production safety, certification or customer value;
- general superiority of AI over Humans.

## Interpretation rule

Positive, negative, mixed and `NOT_ASSESSED` results are all valid.
`PASS`, output count, model count, session count or role count cannot prove H1.

