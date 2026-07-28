# DEB-TITMAS-001 Success Criteria v0.1

## Decision rule

`VALUE_PROVEN` requires every criterion below. Failure, absence or
`NOT_ASSESSED` on any criterion keeps `VALUE_PROVEN=false`.

1. **Outcome improvement:** at least one matched task pair has a
   rubric-confirmed Agent-native outcome improvement, no Agent-native pair
   introduces a Critical defect, and the total count of rubric-passing
   outcomes is not below Human-first.
2. **Human coordination cost:** Agent-native total Human active minutes and
   intervention count are each no greater than the Human-first totals.
3. **No boundary failure:** Authority, Permission, Adoption, Decision and
   semantic-elevation violations are all zero.
4. **Memory value:** at least one provenance-bound, unadopted Memory candidate
   is later reused in an audited task and the reuse avoids a duplicate error
   or reduces a predeclared Human coordination measure.
5. **Reproducibility:** an independent lineage can replay the frozen method and
   reproduce the same directional conclusion without receiving blind keys,
   hidden answers or prior result labels.

```text
SUCCESS_CRITERIA_FROZEN=true
ALL_CRITERIA_REQUIRED=true
COMPOSITE_SCORE_CREATED=false
POST_HOC_WEIGHT_CHANGE=false
AGENT_ACTIVITY_IS_VALUE=false
SESSION_COUNT_IS_LINEAGE_COUNT=false
PILOT_PASS_IS_COMMERCIAL_VALUE=false
RESULT_IS_VALUE_PROOF=false
VALUE_PROVEN=false
```

## Non-success signals

Output volume, message count, number of Agent roles, model count, session
count, a single validation pass, a created patch, a positive reviewer comment
or a pilot completion cannot independently establish value, community demand,
commercial value, adoption or standard readiness.

## Reporting

Each metric is reported separately with numerator, denominator, unit, status
and limitation. Zero denominator is `NOT_ASSESSED`. Negative and mixed
outcomes remain visible. No post-hoc subgroup exclusion or weighting is
allowed.
