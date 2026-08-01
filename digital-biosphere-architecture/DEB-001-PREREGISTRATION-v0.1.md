---
preregistration_id: DEB-001-PREREGISTRATION-0.1
experiment_id: DEB-001
version: v0.1
title: DEB-001 Preregistration v0.1
scope: scientific-preregistration-for-comparison
status: frozen-before-execution
created_at: 2026-07-24
reference_set:
  - Digital Survival Theory Foundation v0.1
  - ADR-DIGITAL-SURVIVAL-THEORY-FREEZE-001
  - DEB-001-PILOT-PACKAGE-v0.1
  - DEB-001-STRATEGY-BASELINE-v0.1
  - DEB-001-EXPERIMENTAL-ALIGNMENT-CHECKLIST-v0.1
  - DEB-READINESS-STATUS-MATRIX-v0.1
execution_authorized: false
runtime_authorized: false
api_authorized: false
authority_system: none
---

# DEB-001-PREREGISTRATION-v0.1

## 1. Experiment Identity（实验身份）

- `experiment_id`: `DEB-001`
- `version`: `v0.1`
- `name`: `DEB-001 Efficiency vs Survival`
- `type`: `Digital Ecology Box experiment preregistration`
- `pre-registered_at`: `2026-07-24`

## 2. Research Question（研究问题）

In dynamic and uncertain environments with selection pressure and shocks, which strategy population (`Efficiency`, `Balance`, `Exploration`) demonstrates higher long-horizon survival characteristics?

## 3. Primary Hypothesis（主假设）

`Balance` and `Exploration` strategy populations will show higher long-horizon survival outcomes than `Efficiency` under repeated shock and volatility conditions.

## 4. Null Hypothesis（零假设）

`Efficiency` strategy is not worse and is equal or better than `Balance` and `Exploration` across all required DEB-001 comparison dimensions (`Survival Fitness`, adaptation under shocks, and post-disturbance stability).

## 5. Falsification Criteria（证伪标准）

The primary hypothesis is falsified if all of the following hold under pre-specified DEB-001 run conditions:

- `Efficiency` has equal/higher `Survival Fitness` in all registered shock scenarios.
- `Efficiency` has equal/higher `Adaptation Velocity` under equivalent change points.
- `Efficiency` has equal/higher `Resilience Score` and `Stability Index` under shock and recovery windows.
- No reproducible advantage for `Balance`/`Exploration` remains after independent replay.

## 6. Frozen Strategy References（冻结策略引用）

All strategy definitions are frozen to:

- `DEB-001-STRATEGY-BASELINE-v0.1.md`
- strategy profiles: `Efficiency`, `Balance`, `Exploration`
- no post-registration strategy parameter changes are allowed for this pre-registered analysis scope.

## 7. Frozen Metrics（冻结指标）

The following metrics and definitions are fixed before execution.

### 7.1 Survival Fitness
- Purpose: long-horizon persistence measure.
- Interpretation: higher values indicate stronger survival outcomes.

### 7.2 Adaptation Velocity
- Purpose: responsiveness time after environment changes.
- Interpretation: lower values indicate faster beneficial adaptation.

### 7.3 Diversity Index
- Purpose: heterogeneity and anti-concentration measure.
- Interpretation: higher values indicate broader strategy/action diversity.

### 7.4 Resilience Score
- Purpose: disruption handling and recovery quality.
- Interpretation: higher values indicate faster, stronger recovery.

### 7.5 Stability Index
- Purpose: variance and collapse-risk control of key state variables.
- Interpretation: higher values indicate fewer harmful oscillations.

### 7.6 Dependency Index
- Purpose: concentration and single-point fragility indicator.
- Interpretation: lower dependency concentration is preferred.

Metric versioning and formula references are inherited from:

- `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1.md`

## 8. Environment Assumptions（环境假设）

- Environment phases and shocks follow `SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1`.
- Resources, observation noise, and competition pressure are applied as scenario inputs, not agent-tuned constants.
- Environment version and configuration hash are fixed in the execution plan.
- No unplanned environment overrides are allowed during pre-registered run blocks.

## 9. Planned Comparisons（计划比较）

Comparisons are pre-specified as:

1. Efficiency vs Balance
2. Efficiency vs Exploration
3. Balance vs Exploration

Across each pair:

- `Survival Fitness`
- `Adaptation Velocity`
- `Diversity Index`
- `Resilience Score`
- `Stability Index`
- `Dependency Index`

Comparison outcome is reported with strategy-order and uncertainty context.

## 10. Statistical Interpretation Principles（统计解释原则）

- Report effect direction, magnitude, and uncertainty.
- Apply pre-specified comparison criteria only (no unplanned subgroup reinterpretation).
- Distinguish support, no effect, and null-compatible null.
- Acknowledge incomplete or conflicting runs as reproducibility constraints.
- Use `SUPPORTED`, `REJECTED`, `INCONCLUSIVE` at hypothesis level.

## 11. Handling of Unexpected Results（异常结果处理）

- `supported`: results match pre-registered directional expectations with reproducible evidence.
- `rejected`: primary hypothesis false under falsification criteria; publish evidence and interpretation.
- `inconclusive`: missing/inconsistent replications or unresolved evidence states (`UNKNOWN` / `CONFLICTED` / `PARTIAL`) prevent conclusion.

No post-hoc strengthening of supporting claims is permitted.

## 12. Post-Registration Change Policy（注册后变更规则）

- Core hypotheses, metrics, and strategy baselines are immutable after registration.
- Any substantive change requires a new preregistration version and explicit rationale.
- If changed, link new version to old version and mark as “superseded with comparison.”
- Cross-version comparability requires explicit deltas for metric formula and strategy definition.

## 13. Non-goals（非目标）

- no runtime control
- no execution authority
- no changing hypotheses after observing results
- no API
- no code/runtime implementation

