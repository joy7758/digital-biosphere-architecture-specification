---
spec_id: DEB-001-STRATEGY-BASELINE-0.1
title: DEB-001 Strategy Baseline v0.1
title_zh: DEB-001 策略基线 v0.1
status: frozen-baseline-for-comparison
scope: scientific-baseline-specification
experiment_id: DEB-001
version: v0.1
implementation_authorized: false
runtime_authorized: false
api_authorized: false
created_at: 2026-07-24
---

# DEB-001-STRATEGY-BASELINE-v0.1

This document defines the frozen baseline strategy profiles used by `DEB-001` and is designed to prevent strategy ambiguity across runs.

It is a scientific baseline specification only:

- No code
- No runtime
- No API

## 1. Baseline Objective

The three strategy populations below are fixed for `DEB-001` and must remain behaviorally stable within a run and documented by version.

Strategy populations:

- `Efficiency Strategy`
- `Balance Strategy`
- `Exploration Strategy`

## 2. Efficiency Strategy

### 2.1 Objective

Maximize short-horizon expected utility per step, with priority on immediate resource gain and direct reward realization.

### 2.2 Allowed Behaviors

- Select actions with highest current expected local payoff.
- Rapidly exploit stable high-yield patterns.
- Minimize deliberate diversification unless payoff drops below immediate threshold.
- Perform low-frequency strategy switches.

### 2.3 Prohibited Behaviors

- Forced exploration beyond defined minimal fallback quota.
- Unbounded speculative branching under clear short-horizon dominance conditions.
- Artificially reducing performance to increase measured diversity.
- Deferred decisions that are solely for long-horizon calibration without short-term basis.

### 2.4 Resource Policy

- Prioritize high-yield actions with minimum cost-to-yield ratio.
- Maintain minimal resource reserve buffer (default low).
- Resource hoarding disallowed unless directly tied to sustained short-horizon yield.

### 2.5 Exploration Policy

- Strictly bounded exploration budget.
- Exploration triggered only under predefined degradation threshold.
- Preference for exploitation-first behavior.

### 2.6 Adaptation Policy

- Trigger adaptation only when repeated short-term losses cross a degradation threshold.
- Use conservative adaptation steps.
- Favor return to previously known efficient actions after transient shocks.

### 2.7 Expected Advantages

- Strong early-step resource conversion efficiency.
- Fast convergence under stable environments.
- Low immediate variance in local objective performance.

### 2.8 Expected Weaknesses

- Higher fragility under regime change.
- Concentration risk and low long-horizon robustness.
- Slower recovery after major shock.

### 2.9 Parameters

- `objective_focus = short_horizon` (primary)
- `explore_ratio = low`
- `reserve_ratio = low`
- `adaptation_step_size = conservative`
- `switch_latency_threshold = high`

### 2.10 Assumptions

- Environment has enough short-term stationarity in early phases.
- Immediate reward remains informative for at least one adaptation cycle.
- Resource continuity is mostly local, not structural.

### 2.11 Expected Failure Modes

- Overfitting to transient states.
- Sudden collapse when exploration depth is required.
- Resource dependency on a few pathways.

### 2.12 Falsification Implications

- If Efficiency Strategy keeps highest `Survival Fitness` under all shock regimes, the hypothesis that balance/exploration improves long-horizon survival is weakened.
- If dependency concentration remains low despite prolonged shocks, claimed efficiency fragility is not supported.

## 3. Balance Strategy

### 3.1 Objective

Optimize a weighted combination of efficiency and continuity using bounded stability constraints.

### 3.2 Stability Mechanisms

- Stability guardrails on action variance.
- Periodic recalibration windows.
- Anti-concentration checks in resource usage.
- Optional recovery-mode pause under high volatility.

### 3.3 Reserve Policy

- Maintain moderate reserve ratio.
- Automatic reserve reinforcement when shock probability rises.
- Reserve release rules are bounded and reversible.

### 3.4 Exploration Limits

- Exploration quota is non-zero but bounded.
- Exploration quality is evaluated by marginal coverage gain, not raw novelty.
- Exploration caps are designed to prevent destabilizing drift.

### 3.5 Adaptation Policy

- Detect regime shifts and apply medium-frequency policy updates.
- Adaptation includes both exploration and consolidation loops.
- Recovery decisions prioritize continuity before short-term gain regain.

### 3.6 Parameters

- `objective_weights = [efficiency, continuity, resilience]`
- `explore_ratio = moderate`
- `reserve_ratio = moderate`
- `stability_threshold = medium`
- `adaptation_step_size = medium`

### 3.7 Assumptions

- Environment changes are detectable within bounded windows.
- Moderate reserve is sufficient to avoid emergency collapse.
- Controlled diversity is beneficial across most volatility levels.

### 3.8 Expected Failure Modes

- Under very high volatility, adaptation speed may lag and lose local efficiency.
- Overconstrained stability settings can cause delayed exploitation recovery.
- Medium diversity may still degrade under prolonged severe shocks.

### 3.9 Falsification Implications

- If Balance Strategy is consistently inferior in both adaptation and long-horizon survival despite moderate shocks, its baseline stability assumptions are falsified.
- If it underperforms both Efficiency and Exploration in all measured regimes, assumptions require version update.

## 4. Exploration Strategy

### 4.1 Exploration Mechanism

- Multi-branch action evaluation.
- Frequent policy perturbations within safety bounds.
- Search for alternative trajectories when uncertainty increases.

### 4.2 Diversity Preservation

- Enforce minimum diversity in action classes and resource channels.
- Prevent collapse to top performers via minimum exploration quotas.
- Maintain fallback portfolio of non-dominant strategies.

### 4.3 Exploitation Tradeoff

- Exploitation occurs conditionally after candidate confidence accumulation.
- Temporary exploitation reduction during uncertainty windows.
- Reward discounting of repeated exploitation to avoid lock-in.

### 4.4 Adaptation Behavior

- High responsiveness to new environmental signals.
- Fast switching when phase transitions are detected.
- Reweight strategies after repeated failures.

### 4.5 Parameters

- `explore_ratio = high`
- `reserve_ratio = moderate-to-high`
- `adaptation_step_size = aggressive`
- `switch_latency_threshold = low`
- `diversity_minimum = high`

### 4.6 Assumptions

- Broader sampling yields useful counterfactual knowledge.
- System can tolerate temporary efficiency drop.
- Diversity has value in uncertain and shocked regimes.

### 4.7 Expected Failure Modes

- Sustained underperformance in stable phases.
- Excessive exploration overhead reducing total short-run gain.
- Noisy signals may cause over-switching.

### 4.8 Falsification Implications

- If Exploration never improves recovery time or resilience under multiple shocks, its assumed long-horizon benefit is falsified.
- If dependency risk increases despite diversification rules, the baseline diversity mechanism is invalid.

## 5. Strategy Versioning Rules（策略版本规则）

1. Baseline parameters are version-locked per strategy population:
   - `efficiency_profile_version`
   - `balance_profile_version`
   - `exploration_profile_version`

2. Any parameter change creates a new strategy version and requires full run-package regeneration.

3. Cross-run comparison is valid only when all strategy version fields are equal.

4. Ambiguity, informal tuning, or untracked local edits invalidate reproducibility.

## 6. Immutable Baseline Requirements（不可变基线要求）

- Baseline definitions are immutable within a registered run set.
- Baseline artifact references must be recorded in package metadata.
- Parameter tables are part of immutable submission package references.

## 7. No Post-Result Strategy Modification Rule（结果后禁止修改规则）

After result publication for a given `DEB-001` run, baseline strategy profiles for that experiment version may not be modified to reinterpret outcomes.

Any adjustment requires:

- a new strategy version declaration,
- a new experiment package,
- and explicit comparability statement in publication metadata.

This rule preserves interpretability and prevents retrospective optimization.

