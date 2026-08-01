---
spec_id: DBA-DEB-001-SPEC-v0.1
spec_name: SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1
title: Digital Ecology Box Experiment DEB-001 v0.1
title_zh: 数字生态箱实验 DEB-001 v0.1
status: theory-driven-empirical-spec
implementation_authorized: false
runtime_authorized: false
schema_authorized: false
api_authorized: false
pilot_executed: false
experiment_name: DEB-001 Efficiency vs Survival
created_at: 2026-07-24
---

# SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1

## 1. Scope and Intent（范围与目标）

This document defines the first empirical validation experiment for Digital Survival Theory.

- This is an experiment specification, not a product design.
- No code, no runtime implementation, and no API is defined.
- The experiment is conducted inside the Digital Ecology Box conceptual framework.

Experiment name: `DEB-001 Efficiency vs Survival`

## 2. Research Hypothesis（研究假设）

### 2.1 Primary Hypothesis

In dynamic environments with uncertainty, competition, environmental drift, and adaptation pressure:

- The **maximum-efficiency strategy** achieves higher short-term gains but lower long-term survival outcomes.
- A **balanced strategy** achieves higher long-horizon survival probability by preserving resource slack and adaptive capacity.
- A **high-exploration strategy** preserves diversity and resilience, and recovers faster under shocks, though sometimes with lower early efficiency.

### 2.2 Formalized Statement

Let survival-related state at step `t` be `S_t` and step-level performance be `P_t`.


a) `corr(P_t, SurvivalFitness_t) < corr(S_t, SurvivalFitness_t)` for long horizon windows.

b) `adaptation` and `diversity` mediate survival when environment volatility exceeds threshold `V*`.

c) If diversity collapses and resource concentration rises, long-horizon failure risk increases independent of immediate efficiency.

### 2.3 Null Hypothesis（可证伪假设）

- H0-1: Efficiency strategy has equal or better `Survival Fitness` than balance/exploration under all tested volatility regimes.
- H0-2: `Diversity Index` has no measurable effect on `Resilience Score` under shock.
- H0-3: Repeated shocks do not change relative ranking between the three strategies.

Rejecting these null hypotheses supports Digital Survival Theory expectations.

## 3. Agent Populations（智能体群体）

Three fixed strategy populations are defined.

### 3.1 Population A: Efficiency Strategy（效率策略）

- Objective: maximize immediate resource yield per step.
- Behavior profile:
  - Greedy action selection
  - Minimal exploration
  - Low policy switching cost tolerance
  - Preference for short-horizon gains
- Risk expectation: high concentration and overfit risk.

### 3.2 Population B: Balance Strategy（平衡策略）

- Objective: jointly optimize efficiency and continuity.
- Behavior profile:
  - Controlled exploration ratio
  - Adaptive thresholds for risk/recovery trade-off
  - Explicit stability reserve policy
  - Periodic diversity-preserving action sampling
- Risk expectation: moderate efficiency, higher survival under medium volatility.

### 3.3 Population C: Exploration Strategy（探索策略）

- Objective: maximize information gain and adaptive capacity.
- Behavior profile:
  - Higher action branching
  - Frequent policy perturbation
  - Low exploit lock-in tolerance
  - Slower exploitation consolidation
- Risk expectation: lower short-term performance, higher shock recovery and long-tail robustness.

### 3.4 Population Configuration

- `population_size_total = 90`
- `size_per_type = 30`
- Equal-size initialization to avoid sampling bias.

## 4. Environment Model（环境模型）

### 4.1 Core Components

- `env_phase` in `{stable, drift, constrained, shock_recovery}`
- `task_complexity`: 3-level scalar in `[0.2, 0.8]`
- `state_observability`: visible / partial / delayed
- `noise_profile`: Gaussian + missing-observation events

### 4.2 Dynamics

- Discrete step simulation.
- State transition function changes per phase:
  - **Phase α (stable)**: slowly varying baseline
  - **Phase β (drift)**: directionally changing task and reward mapping
  - **Phase γ (scarcity)**: resource throughput decline
  - **Phase δ (shock)**: abrupt and multi-variable disruption

### 4.3 Control Variables

- Random seed `seed`
- Drift slope `μ_drift`
- Scarcity onset time `t_scarcity`
- Shock frequency `f_shock`
- Shock intensity `I_shock`
- Observation delay `d_obs`

## 5. Resource Model（资源模型）

- `resource_total = 1000` normalized units per run.
- `regeneration_rate` per phase:
  - stable: `+8%`
  - drift: `+4%`
  - scarcity: `+1%`
  - shock_recovery: `+5%`
- `access_cost` by action: base cost + strategy adjustment.
- `adaptation_cost`: penalty for policy switch and exploration branching.
- `concentration_risk`: nonlinear penalty when top 20% actors hold >60% effective resources.

Resource ledger must record per-agent and per-phase consumption, reserves, recovery, and denied requests.

## 6. Selection Pressure Variables（选择压力变量）

1. `resource_pressure` (0~1): scarcity force level.
2. `competition_pressure` (0~1): arrival rate of alternative options.
3. `volatility` (0~1): magnitude/frequency of parameter perturbation.
4. `coherence_window` (steps): how long recent rewards dominate selection.
5. `diversity_guard` (0~1): minimum allowed diversity floor.
6. `stability_guard` (0~1): tolerance threshold for fluctuation amplitude.

Selection pressure is applied uniformly across all agents; strategy behavior differentiates response.

## 7. Environmental Shock Scenarios（环境冲击情景）

### Scenario S1: Abrupt Scarcity Spike（突发稀缺）
- At `t = 0.35T`, resource regeneration drops by 70% for `0.1T`.

### Scenario S2: Rule Inversion（规则逆转）
- A formerly high-yield action becomes high-cost from `t = 0.5T`.

### Scenario S3: Observation Blackout（观测中断）
- Observation delay increases; missing evidence probability rises from 10% to 60% in a window.

### Scenario S4: Single-Point Failure（单点失败）
- One high-capacity resource node is removed for `0.15T`.

### Scenario S5: Entry Competition Burst（竞争突增）
- New actors with initially high capability but unknown stability enter; increases replacement pressure and selection volatility.

Each scenario must be tested independently and in combined sequence.

## 8. Evidence Requirements（证据要求）

All evidence artifacts are mandatory for this experiment.

### 8.1 Lineage（系谱）
- `experiment_id`, `spec_version`, `seed`, `phase_config`
- Agent ancestry metadata:
  - `agent_type`
  - `strategy_id`
  - `initial_capability_profile`
  - `revision_chain` for any adaptation events

### 8.2 Action Traces（行为轨迹）
- Per-step action chosen and rationale category
- Resource usage per action
- Rejected or deferred actions with reason codes

### 8.3 Selection Records（选择记录）
- Candidate set used
- Selection outcome
- Selection rationale summary
- Confidence/uncertainty state
- Conflict, HOLD, UNKNOWN, PARTIAL states where applicable

### 8.4 Outcome Records（结果记录）
- Survival state transitions
- Recovery events
- Diversity and concentration trajectory
- Shock response outcome (recovered / not recovered / collapsed)

## 9. Metrics（指标）

All metrics must be computed per population and per run.

- **Survival Fitness**
  - Primary composite indicator
  - Includes persistence horizon, survivability under shocks, and recovery completeness

- **Adaptation Velocity**
  - Change in effective strategy quality immediately after environmental phase shift
  - Time to re-attain baseline performance band

- **Diversity Index**
  - Diversity across strategy behavior, selected action classes, and resource channels
  - Must decline gracefully; cliff-like collapse is a risk flag

- **Resilience Score**
  - Area-under-recovery-loss curve and time-to-recover after shock
  - Includes post-shock minimum-functionality threshold crossing delay

- **Stability Index**
  - Frequency and amplitude of systemic oscillation around critical metrics
  - Penalizes repeated lock-in reversals and concentration spikes

## 10. Reproducibility Requirements（可复现性要求）

### 10.1 Deterministic Controls

- Fixed seed and seeded randomness catalog per run.
- Immutable spec snapshot hash (`spec_version` + full text digest).
- Fixed population initialization profiles and size.

### 10.2 Replication Protocol

- Minimum 2 independent re-runs by different operators.
- Independent re-run must include:
  - same `seed` and environment schedule;
  - explicit hardware/runtime metadata;
  - full evidence bundle.

### 10.3 Evidence Integrity

- All logs are immutable append-only per run.
- Unknown/failed/conflicted cases preserved, never omitted.
- Output package must include a reproducibility manifest.

### 10.4 Minimum Acceptance for Claim

A claim of preliminary regularity requires:
- at least 5 full runs per strategy class,
- one full rerun with same seed,
- one independent rerun with equivalent but separate execution context.

## 11. Expected Observations and Falsification Criteria（预期观察与可证伪标准）

### 11.1 Expected Observations

1. Efficiency population leads in early steps but decays faster under high-volatility phases.
2. Balance population keeps higher `Survival Fitness` in multi-shock regimes.
3. Exploration population shows stronger `Resilience Score` and `Adaptation Velocity` after shocks.
4. Diversity collapse predicts earlier systemic instability than resource depletion alone.

### 11.2 Falsification Criteria

`DEB-001` is falsified if all conditions hold:

- Efficiency strategy achieves consistently higher `Survival Fitness` across all shock/scenario configurations.
- Diversity Index shows no correlation with `Resilience Score` and Stability under shock.
- Selection evidence cannot distinguish outcome differences between strategies when exposure histories differ.
- Re-runs fail reproducibility with full configuration parity.

### 11.3 Triage Rule

If criteria conflict with current DST assumption, label result as `INCONCLUSIVE-NEED-REFINE` and feed back into Theory Layer refinement with no governance escalation.

## 12. Experimental Outputs（实验输出）

Minimum deliverables:

- `DEB-001-spec.yaml`-equivalent manifest
- `run_summary.csv` (per run)
- `lineage.jsonl`
- `action_traces.jsonl`
- `selection_records.jsonl`
- `outcome_records.jsonl`
- `reproducibility_report.md`

All outputs are for theory validation only.

## 13. Non-goals（非目标，强调）

- 不定义接口。
- 不定义 API。
- 不定义实现调度。
- 不定义运行部署。
- 不定义任何执行授权机制。
- 不定义治理裁决逻辑。

