# DEB-TITMAS-001 Blind Review Protocol

## Candidate preparation

Each task pair produces origin-neutral candidates labelled only:

```text
Candidate A
Candidate B
Candidate C
```

The label is randomized before review. The reviewer must not receive:

- `HUMAN_FIRST` or `AGENT_NATIVE`;
- participant, Provider, model, session or lineage identity;
- hidden answer, allocation key or execution transcript;
- private path, credential or reasoning content.

The origin mapping remains sealed by the Human experiment custodian until all
rubrics and dispositions are frozen.

## Review dimensions

Each candidate is assessed separately for:

1. `quality`;
2. `maintainability`;
3. `conformance`;
4. `long_term_value`.

The rubric must record factual defect counts and explanation. No dimension can
be replaced by a single overall score.

## Independence

- producer cannot review its own candidate;
- several sessions of the same model remain one lineage unless lineage
  independence is directly evidenced;
- a reviewer role does not create Authority;
- reviewer disagreement is preserved and routed to Human adjudication.

## Unblinding

Origin is revealed only after the reviewer signs the frozen result set.
Unblinding does not permit score changes. Any correction after unblinding is a
separate, versioned erratum with rationale.

## Failure handling

Premature unblinding, leaked identity, changed rubric, missing candidate,
deleted failure or outcome-aware reassignment invalidates the affected task
pair. It remains recorded as `STOPPED` or `NOT_ASSESSED`, never silently
excluded.

```text
BLIND_REVIEW_PROTOCOL_PREPARED=true
BLIND_REVIEW_EXECUTED=false
ORIGIN_MAPPING_CREATED=false
```
