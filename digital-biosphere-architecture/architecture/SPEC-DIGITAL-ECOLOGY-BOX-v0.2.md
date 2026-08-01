---
spec_id: DBA-DIGITAL-ECOLOGY-BOX-0.2
title: SPEC-Digital Ecology Box v0.2
title_zh: 数字生态箱规范 v0.2
status: non-executable-minimum-reproducible-experiment-spec
implementation_authorized: false
experiment_executed: false
pilot_executed: false
admission_required: true
admission_review_completed: false
admission_decision_created: false
registration_authorized: false
runtime_created: false
repository_created: false
---

# SPEC-DIGITAL-ECOLOGY-BOX-v0.2

中文：Digital Ecology Box 最小可复现实验单元（v0.2）。

本规范定义用于 `Digital Biosphere Laboratory` 的最小可复现实验单元，不是实现设计、不是 API 规范、不是运行系统。

## 1. Digital Ecology Box Concept（数字生态箱概念）

Digital Ecology Box（DEB，数字生态箱）是一个最小实验宇宙，包含：
- 一组 Candidate Agent（候选智能体）；
- 一组可参数化环境变量；
- 一个资源池；
- 一个选择/适应交互循环；
- 可复核的证据观察与记录层。

目标不是验证单个模型优劣，而是比较“长周期生存动力学表现”。

## 2. Box Manifest Structure（箱子描述结构）

```yaml
apiVersion: dbox.digital-biosphere.io/v0.2
kind: DigitalEcologyBox
metadata:
  box_id: DEB-<uuid>
  name: <human-readable-name>
  version: v0.2
  created_at: <rfc3339-time>
  owner_reference: <owner_reference_uri>
  authors: [<identity_ref>]
  status:
    phase: Proposed | Deployed | Completed
    conditions:
      - type: Reproducibility
        status: True | False | Unknown
        reason: ...
      - type: EvidenceReady
        status: ...
  revision: <semver-or-git-hash>
  provenance:
    spec_reference: <immutable-adr-or-doc-ref>
    approved_by: <decision-ref>
    reviewed_at: <rfc3339-time>
    notes_hash: <sha256>
spec:
  environment:
    step_count: <int>
    seed: <uint64>
    uncertainty_profile: <profile_ref>
    event_schedule:
      - t: 0
        phase: stable
      - t: n
        phase: resource_shift
  resources:
    total: <float>
    renew_rate: <float>
    scarcity_curve: <piecewise>
  agent_population:
    count: <int>
    strategy_distribution: <distribution-ref>
    adaptation_policy_refs: [<profiles>]
  selection_pressure:
    mode: adaptive | exploration | mixed
    decision_window: <time-window>
    evidence_required: true
  observation:
    metrics_ref: <metric-schema-ref>
    evidence_sink: <uri-or-local-ref>
    retention:
      decision_evidence: true
      execution_evidence: true
      failure_paths: true
```

## 3. Agent Profile Model（Agent 档案模型）

每个 Agent 档案包含最小维度：

- `agent_reference`：稳定身份引用；
- `strategy_profile`：策略族名称；
- `adaptation_profile`：参数化适应参数；
- `capability_set`：能力边界集合；
- `resource_usage_model`：资源消耗参数；
- `behavior_constraints`：行为约束与不可执行边界；
- `experiment_mode`：是否允许竞争、探索、协作。

## 4. Environment Model（环境模型）

环境至少包括：

1. 资源动态（总量、再生速率、分配规则）；
2. 约束事件（干预、规则变更、外部冲击）；
3. 观测噪声（采样率、漏报、延迟）；
4. 竞争压力参数（新 Agent 入场、资源重分配频率）；
5. 可达性边界（Agent 对环境变量可见性）。

环境模型必须显式声明：
- 观察窗口；
- 随机性来源；
- 采样缺失策略；
- 决策边界。

## 5. Resource Model（资源模型）

资源模型用于体现生存压力而非奖励最大化：

- `initial_resource`：初始总量；
- `depletion_rate`：枯竭模型；
- `renewal_rate`：补给模型；
- `scarcity_event`：阶段性稀缺事件；
- `recovery_path`：恢复时间函数；
- `cost_of_adaptation`：适应代价。

资源分配事件必须保留 `unknown/unsupported` 分支，以支持 `PARTIAL/CONFLICTED` 语义。

## 6. Interaction Loop（交互循环）

```text
1. Context build (环境状态 + 资源状态 + 历史状态)
2. Candidate discovery (可行目标/动作集合发现)
3. Selection pressure application (策略依据 + 限制 + evidence requirements)
4. Selection output (可选目标/动作 + rank + rationale)
5. Execution event (如果且仅如果被独立授权)
6. Evidence capture (输入/过程/结果/失败/约束)
7. Evaluation projection (survival metrics 更新)
8. Recovery adaptation (策略更新或状态更新)
9. Governance annotation (decision evidence + evidence integrity flags)
```

交互循环中任何一步的失败必须保持可区分状态，不得自动回退为成功。

## 7. Selection Pressure Configuration（选择压力配置）

包含至少以下参数：

- `pressure_profile`: stable | declining | oscillating | shock
- `competition_intensity`: 低 / 中 / 高
- `adaptation_budget`: 每轮允许变化幅度
- `diversity_guard`: 最低多样性阈值
- `stability_guard`: 平衡约束阈值
- `resilience_trigger`: 扰动恢复阈值

输出结果必须标注：
- 是否满足生存目标；
- 是否触发 `recovery`；
- 是否出现策略集中化；
- 是否发生 `selection lock`。

## 8. Evidence Observation Requirements（证据观察要求）

DEB 不直接执行决策，只产出证据对象和观察记录。

要求：
- 输入证据、过程证据、结果证据三类分离；
- 对每一轮记录 provenance（来源、版本、时间、上下文）；
- 与外部组件交互时必须保留 `boundary_reference`；
- 失败要保留 `UNKNOWN/PARTIAL/HOLD/CONFLICTED/REJECTED`；
- 证据可按实验后重放验证，且不依赖实时计算结果重建。

## 9. Experiment Result Format（实验结果格式）

结果文件采用最小结构：

- `box_id`
- `run_id`
- `seed`
- `step_count`
- `final_metrics`（适应/平衡/多样性/韧性）
- `time_series`（按 step 的指标变化）
- `selection_evidence_log`
- `resource_ledger`
- `failure_log`
- `reproducibility_statement`

结果不作为任何执行授权依据，仅支持 `Observed Law` 提取与版本对比。

## 10. Reproducibility Requirements（可复现性要求）

- 固定 `seed` 与随机源；
- 固定 `spec_version` 与环境版本；
- 固定 `candidate set` 与策略定义；
- 证据链完整可重放（包含失败分支）；
- 清晰记录未满足前提条件；
- 一份结果必须支持至少两名研究者在不同环境下独立复现；
- 发布前需附 `reproducibility_report`（可复现实验者、偏差来源、复现失败原因）。

## 11. First Experiment in v0.2（v0.2 第一个实验）

### DEB-001: Survival Under Selection Pressure（选择压力下的生存实验）

#### 环境与规模
- 资源总量：100
- Agent 数量：10
- 3-5 阶段周期演化

#### 策略族
- **A. 最大效率策略**：优先短期资源收益；
- **B. 平衡策略**：效率+稳定；
- **C. 探索策略**：强调策略多样性和环境覆盖。

#### 环境变化
1. 阶段1：稳定环境；
2. 阶段2：资源减少；
3. 阶段3：规则变化；
4. 阶段4：竞争 Agent 进入。

#### 观察指标
- 长期存活轮次；
- 适应恢复时间；
- 多样性指数；
- 平衡偏离度；
- 资源再分配弹性。

#### 结果预期
- 比较三类策略在 `SurvivalFitness` 与指标稳定性上的差异；
- 识别“短期强者是否带来长期脆弱”的反例；
- 输出 Decision Evidence（建议性）用于后续生态模型更新，不产生命令。

## 12. Non-implementation Statements（非实现声明）

```text
DIGITAL_ECOLOGY_BOX_V0_2_DEFINED=true
IMPLEMENTATION_AUTHORIZED=false
PILOT_EXECUTED=false
DBA_CONTROL_LOOP_IMPLEMENTED=false
DBOS_LIFECYCLE_WRITTEN=false
SAEE_COMMAND_OUTPUT_ENABLED=false
VERIFIABLE_CERTIFICATE_GENERATION_INHERITED=false
```

