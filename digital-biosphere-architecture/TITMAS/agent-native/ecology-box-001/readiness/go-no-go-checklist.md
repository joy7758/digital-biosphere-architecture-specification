# Ecology Box 001 Go / No-Go Checklist v0.1

The machine source is
[`execution-prerequisites-matrix.yaml`](execution-prerequisites-matrix.yaml).

## Deterministic rule

`GO` is valid only when every blocking prerequisite is `SATISFIED`, the
fairness protocol remains `PASS`, all operational roles and exact Provider
profiles are accepted, the frozen ten-task source is unchanged, and
`HD-EB-06=ACCEPT`.

Any `PARTIALLY_SATISFIED`, `NOT_SATISFIED`, `NOT_ASSIGNED`, `NOT_ADOPTED`,
`NOT_ASSESSED`, `CONFLICT` or `EXPIRED` blocking item returns `NO_GO`.

## Current checklist

- [x] frozen source, ten-task set, metrics, roles and criteria;
- [x] fairness protocol design `PASS`;
- [ ] Human baseline operator assigned;
- [ ] Agent participants and independent lineages instantiated;
- [ ] independent blind Reviewer assigned;
- [ ] separate blind custodian assigned;
- [ ] real blind key and origin map created under custody;
- [ ] exact Provider/privacy profiles adopted;
- [ ] budgets and randomization accepted;
- [ ] prospective matched Human baseline accepted;
- [ ] all execution Decisions accepted;
- [ ] final Human execution authorization recorded.

```text
GO_NO_GO_STATUS=NO_GO
GO_NO_GO_REASON=NO_GO_PENDING_OPERATIONAL_ASSIGNMENTS_AND_HUMAN_AUTHORIZATION
NO_GO_NE_EXPERIMENT_FAILURE=true
```

The checklist may only be updated from direct evidence. A document, template,
model recommendation or passing test cannot stand in for an instance,
assignment, adoption or Human Decision.
