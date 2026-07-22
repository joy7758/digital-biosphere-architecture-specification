---
document_id: TMAI-DQ-018-DECISION-PACKET-20260722
title: DQ-018 Telemetry Admission Foundation Implementation Decision Packet
title_zh: DQ-018 遥测准入基础实施决策包
status: ready-for-human-decision-agent-review-complete
decision_id: DQ-018
candidate_slice_id: DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION
primary_repository: digital-biosphere-os
implementation_authorized: false
commit_authorized: false
production_ready: false
---

# DQ-018 Telemetry Admission Foundation Implementation Decision Packet

中文：DQ-018 遥测准入基础实施决策包。

## 1. Decision Question（决策问题）

是否批准在 `digital-biosphere-os` 实施 `DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION`，由 DBOS Domain Owner 负责，在不创建网络 listener、Collector、Evidence、Agent、Runtime 或 Permission 的条件下，建立 production-path reference conformance foundation（生产路径参考符合性基础）：Telemetry Observation→Admission material 的唯一失败关闭边界？

## 2. Why This Slice Now（为什么先做该切片）

`PR-G1` 只读映射已经证明：

- DBOS remote `main@cd3f867...` 有安全的有界对象、注册记录、测试和 validator，但无 OTel/OTLP intake、Telemetry admission ledger 或 production durability；
- SAEE public `main@2173c25...` 只有 DBOS preview 的只读评价投影；
- SAEE development observation 的 OTel-style mapper 明确 synthetic、experimental、非 OTLP、非 Evidence authority；
- 直接部署 Collector 或实现 Evidence promotion 会绕过 `Telemetry != Evidence != Truth`。

因此首切片先建立 Observation Plane（观察平面）到 DBOS Existence Plane（存在平面）的唯一 material admission contract（材料准入契约）。

## 3. Normative Inputs（规范输入）

| input | status | role |
|---|---|---|
| [`architecture/trusted-multi-agent-protocol-specification.md`](architecture/trusted-multi-agent-protocol-specification.md) | `DEFINED` | 六对象、四边界、责任平面 |
| [`architecture/opentelemetry-observability-profile.md`](architecture/opentelemetry-observability-profile.md) | `DEFINED` | OTel/OTLP/Resource/Context/Signal 与 Evidence 边界 |
| [`PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md`](PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md) | `PR_G1_PASS` | 当前实现、缺口、重复权威与来源分层 |
| [`architecture/telemetry-admission-foundation-specification.md`](architecture/telemetry-admission-foundation-specification.md) | `PROPOSED` | exact object/state/store/self-observation contract |
| [`architecture/telemetry-admission-threat-model.md`](architecture/telemetry-admission-threat-model.md) | `PROPOSED` | 24 个威胁和停止条件 |
| [`architecture/telemetry-admission-conformance-recovery-plan.md`](architecture/telemetry-admission-conformance-recovery-plan.md) | `PROPOSED` | 预注册测试、恢复、负载表征和回退 |
| [`DQ-018-TELEMETRY-ADMISSION-AGENT-RECOMMENDATION.md`](DQ-018-TELEMETRY-ADMISSION-AGENT-RECOMMENDATION.md) | `COMPLETE_SPLIT_RESULT` | 两路智能体推荐该切片作为 next step，同时拒绝当前 production recommendation；不是授权 |
| immutable DBA baseline commit | `MISSING` | 实施执行前强制条件 |

## 4. Exact Included Scope（精确纳入范围）

1. closed `TelemetryObservationEnvelope v0.1` schema；
2. append-only `TelemetryAdmissionRecord v0.1` state machine；
3. deterministic validator + stable reason codes；
4. Resource/Instrumentation Scope/Context/version/sampling/redaction/delivery limitations；
5. DBOS-issued committed receipt 重放与 external suspected duplicate 分离；
6. closed input + exact persistence allowlist + bounded opaque references；
7. SQLite single-host transactional reference-conformance backend；
8. migration checksum、async/concurrency/crash/corruption、cross-version backup/restore、integrity 和 rollback；
9. bounded custom self-observation metrics；
10. preregistered conformance/negative/fault/recovery/concurrency tests；
11. agent-readable README and source inventory。

## 5. Exact Excluded Scope（精确排除范围）

```text
OTLP_NETWORK_LISTENER=false
OTEL_SDK_INSTRUMENTATION=false
COLLECTOR_DEPLOYMENT=false
PUBLIC_API=false
RAW_TELEMETRY_STORAGE=false
EVIDENCE_OBJECT_CREATION=false
VERIFICATION_OBJECT_CREATION=false
IDENTITY_OR_ENTITY_CREATION=false
CAPABILITY_OR_PERMISSION_GRANT=false
SAEE_INVOCATION=false
AGENT_OR_RUNTIME_CREATION=false
MULTI_TENANT_OR_HA=false
PRODUCTION_DEPLOYMENT=false
DBOS_EXP_0001_MUTATION=false
```

## 6. Implementation Preconditions（实施前置条件）

全部满足后才可修改 DBOS：

1. Agent Recommendation Gate 完成，且分开记录 next-slice recommendation 与 current production non-recommendation；
2. Human Program Owner 对 DQ-018 明确授权；
3. `dbos_domain_owner_ref` 明确；
4. 当前 DBA production architecture + mapping + packet 形成 immutable commit 并推送；
5. DBOS remote `main` exact base commit 重新确认；
6. DBOS 工作树既有未跟踪／用户变化隔离，不覆盖；
7. 建立 `codex/` prefixed DBOS branch；
8. before-state 334 tests、34 validators 重新通过；
9. implementation plan 引用本 packet 的 exact DBA commit；
10. 无新增外部服务、账号、云资源或 secret authority。

## 7. Implementation Stop Conditions（实施停止条件）

- 需要网络 listener、Collector 或 SAEE 调用才能继续；
- 需要修改 frozen Evidence、历史记录或现有 capability truth；
- 需要自动 Permission/Identity/Evidence promotion；
- SQLite reference backend 无法满足事务／恢复合同；
- sensitive content 无法在 persistence 前可靠拒绝；
- 现有 DBOS tests/validators 失败且不能在 exact slice 内修复；
- threat model 的 Critical/High finding 无法关闭；
- 发现已有 canonical DBOS implementation 会造成第二权威；
- scope 需要 multi-tenant、HA 或 production service 才能成立。

停止后记录 `BLOCKED`，不扩大 scope。

## 8. Agent Recommendation Result（智能体推荐结果）

两路独立 provider 在修正 dedupe trust、sensitive metadata、reference bounds 和 recovery 合同后，对三个次序选项得出相同结论：

```text
OPTION_A_CONTROLLED_FOUNDATION=RECOMMENDED_AS_NEXT_STEP
OPTION_B_ALL_AT_ONCE=NOT_RECOMMENDED
OPTION_C_STOP=NOT_RECOMMENDED
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
```

评审中的拒绝记录也已保留；它们证明该切片不能被单独当成最终生产产品。详见 [`DQ-018-TELEMETRY-ADMISSION-AGENT-RECOMMENDATION.md`](DQ-018-TELEMETRY-ADMISSION-AGENT-RECOMMENDATION.md)。

## 9. Decision Options（决策选项）

### Option A — Authorize Exact Slice（批准精确切片）

```text
DQ-018=AUTHORIZE_DBOS_PR_2A_TELEMETRY_ADMISSION_FOUNDATION
dbos_domain_owner_ref=<human-reference>
```

效力：允许在 immutable DBA baseline 形成后修改 DBOS exact slice；不授权 commit/push DBOS、Collector、SAEE、Pilot、Deployment 或 production claim，除非用户同时明确授权相应动作。

### Option B — Defer（暂缓）

```text
DQ-018=DEFER_DBOS_PR_2A_TELEMETRY_ADMISSION_FOUNDATION
reason=<reason>
```

效力：保留规范和映射，不进入 DBOS 实现。

### Option C — Reject（拒绝）

```text
DQ-018=REJECT_DBOS_PR_2A_TELEMETRY_ADMISSION_FOUNDATION
reason=<reason>
```

效力：关闭该候选；必须提出新 ADR/Decision 才能换方案。

## 10. Separate Git Authorization（独立 Git 授权）

DBA 当前 production architecture/mapping 工作树未 commit、未 push。若需要形成前置 immutable baseline，必须单独授权：

```text
AUTHORIZE_DBA_PRODUCTION_BASELINE_COMMIT_AND_PUSH=true
target_branch=codex/production-observability-baseline
```

该 Git 授权不等于 DQ-018 实现授权；DQ-018 也不自动授权 DBOS commit/push。

## 11. Current Decision State（当前决策状态）

```text
DQ_018_PACKET_PREPARED=true
AGENT_RECOMMENDATION_COMPLETE=true
NEXT_SLICE_RECOMMENDED_BY_TWO_AGENTS=true
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
HUMAN_DECISION_RECORDED=false
DBA_IMMUTABLE_BASELINE_CREATED=false
DBOS_IMPLEMENTATION_AUTHORIZED=false
DBOS_IMPLEMENTATION_STARTED=false
PRODUCTION_READY=false
```
