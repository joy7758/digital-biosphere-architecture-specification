---
package_id: DEB-001-PILOT-PACKAGE-v0.1
experiment_id: DEB-001
version: v0.1
title: DEB-001 Pilot Package v0.1
status: preparation-ready
scope: experiment-preparation-only
created_at: 2026-07-24
digital_survival_theory_ref: Digital-Survival-Theory-Foundation-v0.1.md
adr_ref: ADR-DIGITAL-SURVIVAL-THEORY-FREEZE-001.md
experiment_spec_ref: SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1.md
result_spec_ref: SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1.md
governance_spec_ref: SPEC-DIGITAL-ECOLOGY-BOX-GOVERNANCE-v0.1.md
workflow_ref: DEB-EXPERIMENT-SUBMISSION-WORKFLOW-v0.1.md
execution_authorized: false
runtime_authorized: false
api_authorized: false
authority_effect: none
---

# DEB-001-PILOT-PACKAGE-v0.1

## 1. Experiment Identity（实验标识）

- `experiment_id`: `DEB-001`
- `version`: `v0.1`
- `research_question`: `In dynamic and uncertain environments, which strategy profile (Efficiency, Balance, Exploration) shows higher long-horizon survival performance in digital ecology settings?`

## 2. Hypothesis（假设）

### 2.1 Primary Hypothesis（主假设）

`In environments with uncertainty, competition, and shocks, balanced and exploratory strategy populations will show higher long-horizon survival quality than a pure efficiency strategy.`

### 2.2 Null Hypothesis（零假设）

`Efficiency strategy has equal or higher Survival Fitness than balance and exploration strategies across the same DEB-001 shock conditions and reproducibility envelope.`

### 2.3 Falsification Criteria（证伪标准）

- Falsify 主假设 if:
  - Efficiency strategy has statistically stable dominance in `Survival Fitness` across all required runs;
  - No significant positive difference in `Resilience Score` and `Adaptation Velocity` between balance/exploration and efficiency under repeated shock scenarios;
  - Reproducibility status is accepted while above effects remain stable.

- If evidence is mixed or incomplete, status is `inconclusive` per result specification.

## 3. Agent Populations（代理群体）

Three strategy populations are used, aligned with `DEB-001` in `SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1`:

- Efficiency Strategy
  - Objective: short-horizon efficiency.
  - Expected profile: high early yield, low adaptation willingness.

- Balance Strategy
  - Objective: short performance + stability/continuity trade-off.
  - Expected profile: controlled diversification and resilience behavior.

- Exploration Strategy
  - Objective: long-horizon adaptability through broader behavior exploration.
  - Expected profile: slower early gains, stronger adaptation under novel conditions.

## 4. Environment Configuration Summary（环境配置摘要）

- Environment phases: stable, drift, scarcity, shock, recovery.
- Volatility controls and shock schedule follow DEB-001 definition in `SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1`.
- Observation model includes delay/noise configurations used in experiment design.

## 5. Resource and Selection Pressure Summary（资源与选择压力摘要）

- Resource baseline and renewal schedules configured by phase.
- Selection pressure dimensions include resource pressure, competition pressure, volatility, coherence window, and guard thresholds.
- No implementation of control policy is specified here; pressure is scenario-driven for evidence generation.

## 6. Evidence Collection Plan（证据采集计划）

Required evidence channels (mandatory):

- `lineage_records`
- `action_traces`
- `selection_records`
- `outcome_records`

All channels must provide immutable references and integrity state (`AVAILABLE`, `PARTIAL`, `CONFLICTED`, `UNKNOWN`, `FAIL`) in final result package.

## 7. Expected Result Object（预期结果对象）

Result output must follow `DigitalEcologyBoxResult` in `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1.md`, including:

- Experiment metadata:
  - `experiment_id`, `experiment_version`, `box_spec_reference`, `execution_seed`, `environment_version`, `agent_population_version`.
- `population_results` for Efficiency, Balance, Exploration with fields:
  - population survival outcome
  - resource utilization
  - adaptation events
  - strategy changes
  - lineage transitions
- Metric block for:
  - Survival Fitness
  - Adaptation Velocity
  - Diversity Index
  - Resilience Score
  - Stability Index
  - Dependency Index
- `reproducibility` section
- `falsification_record` section
- `theory_feedback` section

## 8. Reproducibility Checklist（复现清单）

- Fixed seed policy declared before execution.
- Environment version pinned.
- Strategy version pinned.
- Experiment specification version pinned.
- Result schema version pinned.
- Independent replay plan defined.
- Evidence bundle replayability verified.

## 9. Publication Checklist（发布清单）

Before publication, verify:

1. Submission package completeness.
2. Review checklist items satisfied (`SPEC-DIGITAL-ECOLOGY-BOX-GOVERNANCE-v0.1`).
3. Result schema compliance (`SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1`).
4. Falsification status recorded as:
   - supported / rejected / inconclusive
5. Replication status attached.
6. Publication note includes limitations and non-goal reminder.

## 10. Archive Metadata（归档元数据）

- Immutable package reference:
  - package_id
  - experiment_id
  - version
  - registry reference
- Version linkage:
  - ADR, experiment spec, result spec, governance spec, workflow reference.
- Lineage linkage:
  - parent context
  - DEB-001 run IDs
  - future replications and follow-ups.

## 11. Known Limitations（已知限制）

- This is an experiment preparation package only; it does not execute any run.
- No runtime assumptions are included.
- No API definitions are included.
- No authority/approval claims are made.
- Any future conclusions must follow falsification categories and review results.

