---
document_id: TMAI-PRODUCTION-ARCHITECTURE-HUMAN-DECISION-READINESS-REGISTRY-0.1
title: TMAI Production Architecture Human Decision Readiness Registry v0.1
title_zh: TMAI 生产架构人工决策就绪注册表 v0.1
status: immutable-dba-content-baseline-created-dq-018-fresh-before-state-pending
freshness: historical-decision-time-snapshot-superseded-for-current-status
observed_at: 2026-07-22
primary_repository: digital-biosphere-architecture
architecture_frozen: true
human_decision_recorded: true
implementation_authorized: true
production_ready: false
---

# TMAI Production Architecture Human Decision Readiness Registry v0.1

中文：TMAI 生产架构人工决策就绪注册表 v0.1。

## 1. Outcome（结果）

> Historical snapshot：本注册表及 strict JSON 保留 `DQ-018` 执行前的 decision-time truth，
> 不静默改写已绑定输入。当前执行事实以 [`PROGRAM-STATUS.md`](PROGRAM-STATUS.md)、
> [`DECISION-QUEUE.md`](DECISION-QUEUE.md) 和
> [`DBOS-PR-2A-GIT-AUTHORIZATION-RECORD.md`](DBOS-PR-2A-GIT-AUTHORIZATION-RECORD.md)
> 为准：DQ-018 已实施并达到 PR-G2A review ready，但尚未获 gate approval。

六项精确人工决定已经记录，DBA content baseline 的 exact commit/tree 已形成。当前只等待从远端复验
freeze attestation，并执行 fresh DBOS before-state。本注册表将四项 reference adoption、`ADR-024` 架构
序列、`DQ-018` 有界实现授权和三个仍缺输入的 DQ 汇入一个 truth surface（事实表面），防止版本采纳、
实现授权、Git 冻结和部署授权互相替代。

机器真值：

- [registry JSON](PRODUCTION-ARCHITECTURE-HUMAN-DECISION-READINESS-REGISTRY.v0.1.json)
- [strict JSON Schema](architecture/schemas/production-architecture-human-decision-readiness-registry.schema.v0.1.json)
- [split-result Agent review](PRODUCTION-DECISION-READINESS-AGENT-RECOMMENDATION.md)

```text
Decision packet ready != Decision recorded
Decision recorded != Implementation started
Reference adoption != Runtime selection
Architecture registry != Immutable Git baseline
OpenTelemetry backend != DBOS canonical store
```

## 2. Recorded Decisions and Remaining Queue（已记录决定与剩余队列）

| DQ | Decision Queue status | packet readiness | next human action | recommended option is only advisory | immediate effect now |
|---|---|---|---|---|---|
| `DQ-022` | `DECIDED_REFERENCE_ADOPTED` | exact token recorded | none | `v1.11.0` exact reference | reference only; implementation false |
| `DQ-023` | `DECIDED_REFERENCE_ADOPTED` | exact token recorded | none | core Stable + pinned GenAI Development mapping | reference only; implementation false |
| `DQ-024` | `DECIDED_REFERENCE_ADOPTED` | exact token recorded | none | Stable Schema/Resource + Entity quarantine | reference and quarantine policy only |
| `DQ-025` | `DECIDED_REFERENCE_ADOPTED` | exact token recorded | none | exact custom-minimal 8+2 inventory | architecture inventory only; no build/config/deploy |
| `ADR-024` | `ACCEPTED_ARCHITECTURE_SEQUENCE` | exact token recorded | none | accept S0–S9 staged path | sequence only; every stage remains gated |
| `DQ-018` | `DECIDED_IMPLEMENTATION_AUTHORIZED_PRECONDITIONS_PENDING` | exact token and DBOS Owner recorded | form immutable DBA baseline, then fresh DBOS before-state | bounded Telemetry Admission Foundation | authorization true; start false until both prerequisites pass |
| `DQ-019` | `BLOCKED_INPUT` | no decision packet | provide backend/Owner/RPO/RTO/direct evidence | none | none |
| `DQ-020` | `BLOCKED_INPUT` | no decision packet | provide decisions plus exact deployment and operational bindings | none | none |
| `DQ-021` | `BLOCKED_INPUT` | no decision packet | provide Identity/Data Governance/provenance/Evidence-policy inputs | none | none |

六个 exact token 均由 `decided_by_ref=zhangbin` 在 `2026-07-22T12:05:04+08:00` 独立给出并记录。
用户对未来类似事项的概括性“按推荐授权”不替代新版本、部署、外部资源、Permission、生产流量或不可逆
发布所需的独立决策记录。

## 3. Dependency-safe Path（依赖安全路径）

```text
DQ-022 OTLP reference ─┐
DQ-023 semantic ref ───┼─> DQ-024 Schema/Resource/Entity boundary
DQ-025 Collector ref ──┘

ADR-024 staged production sequence decision
  ↓ required before post-foundation production stages

explicit DQ-018 decision + immutable DBA baseline + fresh DBOS before-state
  ↓
bounded DBOS PR-2A implementation and direct evidence
  ↓
DQ-019 production persistence selection
  ↓
DQ-020 authenticated listener / Collector synthetic staging
  ↓
PR-G2I + Data Governance + provenance policy
  ↓
DQ-021 separate Evidence Admission
```

图中连线是 prerequisite（前置）或 reference precedence（参考优先顺序），不是自动状态机。任一步
仍需要各自的人类决定和 direct evidence（直接证据）。

## 4. Exact Decision Inputs（精确决策输入）

每个 decision packet 的 Markdown 与 JSON 已在机器注册表中用 SHA-256 绑定。该摘要只证明“当前审查
输入是哪一份”，不证明整个未提交 worktree 已冻结。当前事实：

```text
BRANCH=codex/production-observability-baseline
BASE_HEAD=769b5589d07eb9bc9efbaf0930039c3d49632372
WORKTREE_ENTRY_COUNT_AT_REGISTRY_CAPTURE=98
STAGED_ENTRY_COUNT=0
CANDIDATE_COMMIT=264f3171c3dfa8a9f614c7d0c835e4be26870d01
CANDIDATE_TREE=b83f25d9f5e6b47f7d6717320026cc242c817b03
IMMUTABLE_BASELINE_CREATED=true
COMMIT_AUTHORIZED=true
PUSH_AUTHORIZED=true
```

后续若任何已绑定 packet 发生变化，必须重新计算摘要并重新审查，不得继续沿用本注册表的绑定。

## 5. OpenTelemetry Production Boundary（OpenTelemetry 生产边界）

OpenTelemetry 官方说明自身是 vendor- and tool-agnostic（供应商／工具中立）的 telemetry framework，
不是 observability backend；backend 的 storage 与 visualization 由其他工具承担。Collector 可以向一个
或多个 backend 导出，但成功导出只证明某一 transport hop（传输跳）结果。

- [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
- [Components](https://opentelemetry.io/docs/concepts/components/)
- [Collector internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)
- [Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/)

因此以下问题保留为 deferred production questions（延期生产问题），而不是现在制造答案：

1. observability backend 的 Owner、vendor/open-source candidate、HA、retention 和 migration；
2. exact query/rule/alert route/runbook digest；
3. telemetry retention/access/deletion 与 DBOS Evidence retention 的隔离；
4. backend failure、data loss、query staleness 和 tenant isolation 的直接证据。

这些问题必须在 `DQ-019`–`DQ-021` 的真实输入出现后处理。提前写一个“已选 backend”或占位 query
摘要会制造虚假事实。

## 6. Collision Prevention（冲突防护）

1. 每个 DQ／ADR decision reference 只能记录一个 human decision token；
2. `decided_by_ref` 和 `decided_at` 缺失时，Decision 恒为未记录；
3. `DQ-022`–`DQ-025` 只可能采纳架构 reference，不授权实现；
4. `DQ-018` 不授权 DBA commit/push，Git 授权必须分开；
5. `DQ-025` 不构建 binary/image/config，也不选择 deployment；
6. `DQ-020` 不能用 health `200 OK`、dashboard green 或模型推荐绕过直接证据；
7. Collector/export/backend records 不得自动成为 DBOS Evidence、Truth、Permission 或 canonical fact；
8. immutable content identity 只由 [`PRODUCTION-ARCHITECTURE-BASELINE-FREEZE-RECORD.md`](PRODUCTION-ARCHITECTURE-BASELINE-FREEZE-RECORD.md) 中的 exact commit/tree 定义；attestation 不扩张技术权限。

## 7. Stop Rule（停止规则）

下列 stop-rule block 是本注册表冻结时的历史状态。当前合法路径已经推进到 `PR-G2A Human
Review`；`DQ-019`–`DQ-021` 仍等待各自真实输入和独立决定：

```text
REFERENCE_ADOPTED=true
ARCHITECTURE_FROZEN=true
IMPLEMENTATION_AUTHORIZED=true
IMPLEMENTATION_MAY_START=false
COMMIT_AUTHORIZED=true
PUSH_AUTHORIZED=true
COLLECTOR_SELECTED=false
BACKEND_SELECTED=false
CONFIGURATION_CREATED=false
ENDPOINT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
EVIDENCE_CREATED=false
PERMISSION_GRANTED=false
TESTS_EXECUTED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
