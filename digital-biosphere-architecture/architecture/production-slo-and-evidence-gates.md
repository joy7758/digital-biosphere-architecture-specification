---
spec_id: TMAI-PRODUCTION-SLO-EVIDENCE-GATES-0.1
title: TMAI Production SLO and Evidence Gates v0.1
title_zh: TMAI 生产 SLO 与证据闸门 v0.1
status: accepted-candidate-targets-not-measured
decision_reference: ADR-023-trusted-multi-agent-protocol-and-production-observability.md
measurement_started: false
targets_achieved: false
production_ready: false
---

# TMAI Production SLO and Evidence Gates v0.1

## 1. Measurement Boundary（测量边界）

本文件为 `TMAI-SELF-HOSTED-SINGLE-TENANT-1` 定义 candidate production targets（候选生产目标）。目标被定义不表示已经测量或达到；每项结果必须绑定 exact version、environment、workload、window、query 和 evidence reference。

## 2. Primary KPIs（核心指标）

### KPI-1: Governed Record Continuity（受治理记录连续率）

```text
complete_chains / eligible_governed_executions
```

完整链至少包含 Identity、Authorization、Execution、Evidence 和 Verification 引用。Critical workflow（关键工作流）目标为 `100%`；缺任一关键引用必须 fail closed。

### KPI-2: Observation Delivery Integrity（观察交付完整性）

```text
accepted_observations_with_explicit_delivery_state / emitted_observations
```

目标为 `>=99.9%`；其余必须能归类为 partial、retrying、dropped、duplicate-suspected 或 unknown。该 KPI 不允许用采样后的分母隐藏丢失。

### KPI-3: Safe Change and Recovery Rate（安全变更与恢复率）

```text
authorized_changes_with_verified_rollback_or_recovery / governed_changes
```

目标为 `100%`。自动 Permission 提升、SAEE direct writeback、失败记录静默删除和无法解释的状态跃迁必须为 `0`。

## 3. Service Level Objectives（服务等级目标）

| SLO ID | 指标与范围 | v0.1 候选目标 | 必需证据 |
|---|---|---|---|
| `SLO-001` | DBOS core record service monthly availability | `>=99.9%` | availability query、maintenance exclusions、incident records |
| `SLO-002` | 已确认 canonical DBOS record 恢复完整性 | `100%` | backup/restore checksum、replay result、failure log |
| `SLO-003` | acknowledged canonical record 的 RPO | `0` | controlled disaster drill；未确认写入另行报告 |
| `SLO-004` | core service RTO | `<=30 minutes` | timed recovery drill 和恢复验证 |
| `SLO-005` | Critical governed chain completeness | `100%` | Identity→Authorization→Execution→Evidence→Verification query |
| `SLO-006` | OTLP accepted delivery with explicit outcome | `>=99.9%` | Collector/exporter counters、partial/rejected/dropped totals |
| `SLO-007` | W3C Trace Context continuity for eligible distributed operations | `>=99.0%` | trace continuity query、missing-context inventory |
| `SLO-008` | SAEE direct DBOS writeback | `0` | network/write audit、contract tests |
| `SLO-009` | automatic Permission escalation | `0` | authorization audit、negative tests |
| `SLO-010` | silent deletion of failures/evidence history | `0` | append/history audit、retention verification |
| `SLO-011` | default sensitive GenAI content capture | `0` | configuration audit、redaction tests、sample inspection |
| `SLO-012` | unresolved exploitable Critical/High release blockers | `0` | dependency/container/code/config scans and human triage |
| `SLO-013` | Evidence admission requests with explicit terminal or hold/unknown outcome | `100%` | request/admission lifecycle reconciliation; no silent timeout/loss |
| `SLO-014` | Evidence Object created without valid admission record, subject binding and policy reference | `0` | object-to-admission/identity/policy query and negative tests |
| `SLO-015` | SAEE production-adapter requests with explicit completed/failed/timeout/unsupported/conflict outcome within profile timeout | `>=99.9%` | adapter request/outcome/latency query; timeout value frozen before pilot |
| `SLO-016` | SAEE output without exact input, model, policy and limitation provenance | `0` | Evaluation/Recommendation provenance audit |
| `SLO-017` | successful SAEE direct DBOS writeback or automatic recommendation execution | `0` | network/write audit、DBOS change inventory、negative tests |

如果实现无法达到候选目标，必须提交新 Architecture/Production Decision，说明替代目标、风险、期限和补偿控制；不得在报告中静默降低分母或阈值。

## 4. OpenTelemetry SLIs（OpenTelemetry 服务指标）

至少测量：

- received、accepted、rejected、partial、retried、dropped 和 duplicate-suspected signal counts；
- Collector queue size、queue capacity、export failures、retry delay、CPU、memory 和 throughput；
- signal type、Resource、Instrumentation Scope 和 semantic convention version coverage；
- trace context missing/broken links；
- sampling decision 和 unsampled critical record path；
- redaction/filter counts；
- cardinality limit and dropped attribute counts；
- DBOS intake accepted/rejected/unknown counts；
- Evidence/Verification creation latency，但不得把低延迟替代正确性。

### 4.1 Collector operational evidence binding（Collector 运维证据绑定）

以上指标必须通过
[`opentelemetry-collector-operational-evidence-profile.v0.1.json`](opentelemetry-collector-operational-evidence-profile.v0.1.json)
与其 [strict Schema](schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json) 绑定到
exact Collector version、instrument stability、OTLP↔Prometheus name projection、Resource、configuration、
query、window、threshold、clock 和 observation source。机器画像预定义 12 类 observation 与 6 类
derived SLI formula semantics（派生 SLI 公式语义），但 exact query/threshold/window 当前均为 `null`。

这些 `null` 是失败关闭的未来输入，不得用本节候选 SLO 目标、dashboard default（仪表盘默认值）或
占位摘要代替。没有 exact query bundle、counter-reset/no-data rule、独立 self-observation（自观测）、
blackbox/storage/drift 结果和 delivery reconciliation（交付对账）时，`PR-G3` 必须保持关闭。

## 5. Evidence Package for a Gate（闸门证据包）

每个生产 gate 的 Evidence Package 必须符合 [`production-gate-evidence-manifest-specification.md`](production-gate-evidence-manifest-specification.md)、[`schemas/production-gate-evidence-manifest.schema.v0.1.json`](schemas/production-gate-evidence-manifest.schema.v0.1.json) 和 [`production-gate-evidence-profiles.v0.1.json`](production-gate-evidence-profiles.v0.1.json)。以下旧式文本投影只用于人工阅读，不能代替机器清单、immutable digest（不可变摘要）或 gate profile：

```text
gate_id=
profile_id=
artifact_version=
source_commit=
environment_ref=
workload_ref=
measurement_window=
otel_versions=
collector_version=
collector_release_core_contrib_commits=
collector_component_inventory_digest=
collector_binary_image_sbom_provenance_signature_digests=
collector_normalized_config_and_runtime_binding_digests=
collector_distribution_case_result_ref=
collector_operational_evidence_profile_digest=
collector_metric_stability_naming_resource_and_query_bundle_digests=
collector_alert_route_runbook_bundle_digests=
semantic_convention_versions=
queries_or_test_refs=
positive_results=
negative_results=
failures_and_unknowns=
security_findings=
rollback_or_restore_ref=
reviewed_by_ref=
reviewed_at=
result=PASS|FAIL|BLOCKED|NOT_ASSESSED
```

Schema valid（模式有效）只表示结构正确；artifact/digest verification、exact profile coverage、blocking unknown/security/recovery review 和 Human Decision binding 未通过时，结果必须失败关闭。

## 6. Required Fault and Negative Tests（必需故障与负例）

| 测试 | 必须证明 |
|---|---|
| Collector unavailable | SDK/agent 的 queue、drop 和 retry 可见，不伪造成功 |
| Gateway restart | 重试和 duplicate 被识别；不重复创建 canonical Evidence |
| Observability backend unavailable | 后端故障不直接破坏 DBOS canonical records |
| DBOS intake unavailable | telemetry 可观测但 Evidence admission 保持未完成 |
| Disk full / queue overflow | fail closed、告警、drop counters 和恢复路径成立 |
| Invalid OTLP / incompatible semconv | 不重试永久坏数据；保留 rejected diagnostic |
| Collector source/component/config drift | exact commit/byte/component/build/config/runtime reconciliation 失败关闭；不使用 floating tag 或 current state 覆盖 desired state |
| Transform deterministic data error | 与 transient downstream failure 分离；不 silent partial transform，不进入无界 poison retry |
| Health OK while exporter blocked | health 只证明局部 extension 状态；不得单独形成 readiness、trust 或 gate pass |
| Self-telemetry missing or stale | 标记 `UNKNOWN/NOT_READY`；不得 zero-fill 或用主 exporter 的同路径信号替代 |
| Counter reset or mixed Collector version | 按 instance lifecycle 分窗并保留版本；不得产生负 rate 或无版本聚合 |
| Alert path unavailable / no data | no-data alert 和 delivery test 必须失败可见；dashboard green 不得替代 route/runbook 结果 |
| WAL writable metric absent while disk fails | 使用独立 disk free/write probe；internal metrics 或 health OK 不得覆盖 storage failure |
| Missing Context | 不猜测 parentage；链路标记 partial/unknown |
| Sampled-out span | 不声称完整执行或 Evidence chain |
| Sensitive prompt/tool payload | 默认不采集或在 intake 前删除/哈希 |
| SAEE unavailable | DBOS 继续保留事实；评价状态为 unavailable/unknown |
| Conflicting SAEE recommendations | 保留冲突，禁止自动采纳 |
| Revoked authorization | 后续执行被拒绝并形成失败记录 |
| Backup restore | acknowledged canonical records 逐项恢复并通过连续性检查 |

## 7. Observation Window（观察周期）

进入 `PR-G6` 的有界 pilot 至少应包括：

- 7 天 staging soak（预生产长稳）；
- 30 天 bounded production observation（受控生产观察）；
- 至少一次 Collector failure、DBOS restore 和 rollback drill；
- 正常、失败、拒绝、超时、重复、断链和人工停止记录；
- 预冻结 workload 与流量范围。

该周期是 v0.1 候选门槛，尚未执行。

## 8. Non-claims（非声明）

```text
SLO_TARGETS_DEFINED=true
SLO_MEASUREMENT_STARTED=false
SLO_TARGETS_ACHIEVED=false
FAULT_TESTS_EXECUTED=false
PILOT_STARTED=false
PRODUCTION_READY=false
```
