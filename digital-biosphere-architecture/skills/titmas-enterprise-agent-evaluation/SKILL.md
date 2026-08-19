---
name: titmas-enterprise-agent-evaluation
description: Use the frozen TITMAS enterprise evaluation contracts to compare bounded agent deployment options, preserve evidence limits, and produce a scenario-scoped recommendation.
assign_when: A task creates an enterprise agent evaluation, compares two deployment options, builds a scenario pack, produces a recommendation card, reviews a failure, compares native and stabilized results, or decides whether a version change requires retesting.
---

# TITMAS enterprise agent evaluation

## Canonical references

Read these files before acting; do not create a second definition:

1. `../../docs/enterprise-agent-evaluation/00_R0_DECISION_AND_ASSET_MAP.md`
2. `../../docs/enterprise-agent-evaluation/02_ENTERPRISE_EVALUATION_PROFILE.schema.json`
3. `../../docs/enterprise-agent-evaluation/03_ENTERPRISE_SCENARIO_PACK.schema.json`
4. `../../docs/enterprise-agent-evaluation/04_EVALUATION_RECOMMENDATION_AND_PRESENTATION.md`
5. `../../docs/enterprise-agent-evaluation/05_CONTROL_PROVIDER_INTERFACE.md`
6. `../../docs/enterprise-agent-evaluation/06_FIRST_PROFILE_AND_PHASE_GATES.md`

## Procedure

1. Read and validate the EEP and ESP.
2. Check versions, digests, permissions and frozen-case state.
3. Mark the run as `NATIVE` or `STABILIZED`.
4. Run or read results only when the current Human Gate permits it.
5. Map existing TITMAS evidence without creating a new fact source.
6. Separate observed execution facts, advisory model judgments and final human adjudication.
7. Calculate the frozen recommendation index, then apply red lines independently.
8. Produce deployment level, evidence level, recommendation card and evidence references.
9. Check that every claim remains inside the scenario, version, data and authority boundary.

## Required output

Include: scenario, tested configuration, test version, recommendation index, red-line result, deployment level, evidence level, major cost, human intervention, largest residual risk, suitable users, unsuitable users and validity boundary.

## Stop conditions

Stop on missing version/digest, unfrozen cases, ambiguous authority, secrets or prohibited data, absent required evidence, invalid human approval, or an attempt to treat evaluation as permission.

Never treat evidence completeness as business truth, a model judge as final authority, an unobserved field as PASS, or stabilized performance as native vendor performance. Do not create a universal leaderboard, capture chain of thought, execute irreversible enterprise actions, claim certification/absolute safety/permanent stability, or build stability features without an observed failure.
