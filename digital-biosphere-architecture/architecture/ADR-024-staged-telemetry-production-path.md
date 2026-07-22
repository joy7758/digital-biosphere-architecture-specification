---
adr_id: ADR-024
title: Stage the Telemetry Production Path After the Admission Foundation
title_zh: 在遥测准入基础之后分阶段建立生产路径
status: accepted
date: 2026-07-22
decision_effect: architecture-sequence-adopted-stage-gates-remain
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# ADR-024: Stage the Telemetry Production Path After the Admission Foundation

## Context（背景）

`PR-G1` 已证明 DBOS 尚无 production OTel/OTLP intake、canonical durability 和 Evidence admission；`DQ-018` 已就绪但未获人工授权。OpenTelemetry 官方又明确：

- OTLP acknowledgement 只是单个 client/server hop；
- partial success、retry、disconnect 和 duplicate 都有独立语义；
- Collector memory queue、file WAL 和 message queue 的耐久保证不同；
- gateway scaling 需要 stateful routing 和 metric single-writer 约束；
- Collector 会成为新的网络、秘密、资源和敏感数据攻击面。

因此，“部署 Collector”、“换成生产数据库”和“创建 Evidence”不能合并成一个无边界任务。

## Decision（决定）

采纳 [`production-implementation-sequence.md`](production-implementation-sequence.md) 的 staged path（分阶段路径）：

1. Telemetry Admission reference conformance；
2. production persistence selection and proof；
3. authenticated OTLP/Collector staging；
4. separate Telemetry-to-Evidence admission；
5. SAEE read-only production isolation；
6. security/recovery/capacity；
7. bounded pilot；
8. Human Production Decision；
9. separate deployment authorization。

## Alternatives（替代方案）

### A. Build all layers together

Rejected in the proposal（拟议拒绝）：无法将 transport、persistence、Evidence、SAEE 和 deployment 失败分开审计，也会绕过现有权力边界。

### B. Use OpenTelemetry backend as DBOS canonical store

Rejected in the proposal：observability backend 不管理 Identity、Authorization、Evidence Admission 或 DBOS append-only lifecycle semantics。

### C. Remain at SQLite reference-only indefinitely

Allowed as a non-production stop state：可用于符合性和研究，但不能进入 production profile。

## Consequences（影响）

- 每一阶段有独立 Owner、决策、证据和 rollback；
- 生产路径更慢，但失败域和 authority 可审计；
- DBA 继续只管规则，不收容运行秘密、Collector 或数据库；
- DQ-019、DQ-020、DQ-021 只是 future decision inputs，不是预批准；
- 任何时候都可以停在上一个已验证等级，但不得伪造下一等级声明。

## Review Evidence（审查证据）

[`PRODUCTION-PATH-AGENT-RECOMMENDATION.md`](../PRODUCTION-PATH-AGENT-RECOMMENDATION.md) 保留两路模型的初始反对、修订闭环和复审结果。两路模型最终都推荐该 staged sequence（分阶段序列）作为下一条正确路径，同时都明确当前系统仍不适合被推荐为 production customer use（生产客户使用）。Agent recommendation（智能体建议）只构成架构审查输入，不采纳本 ADR，也不授予任何实施或部署权。

OTLP `1.11.0` pre-freeze refresh、20-control OTel alignment 和 Production Gate Evidence Contract 的两路 delta review 见 [`PRODUCTION-EVIDENCE-CONTRACT-AGENT-RECOMMENDATION.md`](../PRODUCTION-EVIDENCE-CONTRACT-AGENT-RECOMMENDATION.md)。最终两路均推荐 S0 Architecture Contract Freeze、均无剩余 design blocker，仍共同判定 production customer recommendation=false。其后 exact `v1.10.0`→`v1.11.0` source/delta、compatibility、size-limit behavior 和独立两路 version review 已形成 [`DQ-022`](../OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.md)，但尚未被 Human Version Decision 采纳。

机器可读投影见 [`PRODUCTION-IMPLEMENTATION-SEQUENCE-v0.1.json`](../PRODUCTION-IMPLEMENTATION-SEQUENCE-v0.1.json)。Markdown 与 JSON 任一发生不一致时，必须停止并由 Architecture Maintainer 修复；不得选择更宽松的一份继续执行。

## Recorded Human Decision（已记录人工决定）

```text
ADR-024=ACCEPT_STAGED_TELEMETRY_PRODUCTION_PATH
decided_by_ref=zhangbin
decided_at=2026-07-22T12:05:04+08:00
```

该决定只采纳架构顺序。DBA baseline 的 commit/push 另由
`AUTHORIZE_DBA_PRODUCTION_BASELINE_COMMIT_AND_PUSH=true` 授权；`DQ-018` 另行授权，且仍需不可变
DBA 基线和 fresh DBOS before-state。它不预授权 `DQ-019`–`DQ-021`、Collector build、配置、
listener、部署、生产流量或生产使用。

```text
ADR_024_STATUS=ACCEPTED
HUMAN_ARCHITECTURE_DECISION_RECORDED=true
PRODUCTION_SEQUENCE_ADOPTED=true
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
