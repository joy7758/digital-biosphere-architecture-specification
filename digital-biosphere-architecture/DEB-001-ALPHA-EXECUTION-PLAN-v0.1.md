---
plan_id: DEB-001-ALPHA-EXECUTION-PLAN-0.1
experiment_id: DEB-001
version: v0.1
title: DEB-001 Alpha Execution Plan v0.1
scope: execution-preparation-only
status: planning
created_at: 2026-07-24
implementation_authorized: false
runtime_authorized: false
api_authorized: false
authority_system: none
---

# DEB-001-ALPHA-EXECUTION-PLAN-v0.1

## 1. Alpha Experiment Objective（Alpha 实验目标）

Plan and prepare the first reproducible execution of `DEB-001` as a constrained alpha trial of the pre-registered design.

This is preparation planning only:

- No code
- No runtime implementation
- No API
- No runtime authority
- No production deployment

## 2. Minimal Population Size（最小种群规模）

- Total population minimum: `90`
- Distribution:
  - Efficiency Strategy: `30`
  - Balance Strategy: `30`
  - Exploration Strategy: `30`

This is the minimum valid comparability baseline.

## 3. Number of Experimental Rounds（实验轮次）

- Planned alpha rounds: `5`
- Round block structure:
  - Round 1: Baseline stability
  - Round 2: Drift adaptation
  - Round 3: Scarcity stress
  - Round 4: Shock response
  - Round 5: Recovery and repeatability check

No post-result strategy profile modification during alpha.

## 4. Replication Plan（复现计划）

- Internal replication target: `2` independent replication sets minimum.
- One replication must be independently prepared by a second reviewer context.
- Seed reuse policy:
  - Fixed seed list defined in execution metadata.
  - Replay required for one full re-run path.
- Divergence classification:
  - reproducible-match
  - acceptable variance
  - unresolved divergence (documented)

## 5. Environment Parameter Set（环境参数配置）

Use a frozen alpha set drawn from DEB-001 pilot plan:

- Phases:
  - Stable
  - Drift
  - Scarcity
  - Shock
  - Recovery

- Core parameter fields:
  - drift slope
  - shock intensity
  - shock timing
  - observation delay
  - competition intensity
  - resource renewal profile

- Parameter state is pinned at start and remains constant within Alpha execution block.

## 6. Resource Configuration（资源配置）

- Resource model follows DEB-001 pilot references.
- Resource totals and regeneration by phase are pre-registered.
- Resource utilization logs must be collected per strategy and per agent.
- Concentration / bottleneck indicator collected as part of resilience and dependency reporting.

## 7. Evidence Output Requirements（证据输出要求）

Mandatory evidence channels:

- `lineage records`
- `action traces`
- `selection records`
- `outcome records`

Output requirements:

- Every record includes run, phase, and step context.
- Evidence references must be immutable and replayable.
- Incomplete channels must be explicitly marked and explained.

## 8. Expected Storage Structure（预期存储结构）

### 8.1 Per-run bundle

- `run_manifest.yml`
- `manifest_run_metadata.json`
- `lineage.jsonl`
- `action_traces.jsonl`
- `selection_records.jsonl`
- `outcome_records.jsonl`
- `metric_timeseries.csv`
- `reproducibility_plan.md`

### 8.2 Package-level index

- `DEB-001-PREREGISTRATION-v0.1` reference
- `DEB-001-PILOT-PACKAGE-v0.1` reference
- `experiment_status_matrix` link
- `readiness_review_notes`

## 9. Success Criteria for Alpha Phase（Alpha 阶段成功标准）

Alpha is considered successful when:

1. Pre-registration fields are fully satisfied before first run.
2. Evidence channels are complete or explicitly flagged with reasons.
3. Reproducibility bundle is structurally complete.
4. At least one full run set produces a valid `DigitalEcologyBoxResult` object.
5. No unplanned post-hoc hypothesis/metric changes are introduced.

## 10. Transition Criteria（转化标准）

### 10.1 Alpha Preparation → Alpha Execution

- All readiness checks pass (or are fully justified as NOT_READY with explicit mitigation).
- Strategy baseline references are immutable and linked.
- Environment and resource parameters are pinned.
- Evidence outputs and storage layout are finalized.

### 10.2 Alpha Execution → Result Package

- Result package is generated for all alpha runs.
- Population comparison fields are populated for all three strategy groups.
- Publication-ready falsification status is assigned (supported / rejected / inconclusive).
- Result artifact is ready for registry linkage.

## 11. Non-goals（非目标）

- no code
- no implementation
- no runtime authority
- no production deployment
- no policy enforcement behavior
- no execution authorization

