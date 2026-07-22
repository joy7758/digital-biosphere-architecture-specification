---
document_id: TMAI-PRODUCTION-PATH-AGENT-RECOMMENDATION-20260722
title: TMAI Staged Production Path Agent Recommendation
title_zh: TMAI 分阶段生产路径智能体推荐记录
status: complete-sequence-recommended-production-not-ready
observed_at: 2026-07-22
sequence_recommended_by_two_agents: true
post_catalog_sequence_delta_recommended_by_two_agents: true
production_customer_recommendable_now: false
implementation_authorized: false
production_ready: false
---

# TMAI Staged Production Path Agent Recommendation

中文：TMAI 分阶段生产路径智能体推荐记录。

## 1. Scope（范围）

两路真实 provider 评审的是 DQ-018 之后的完整 production implementation sequence（生产实施序列），不是当前产品就绪度，也不是对任何 implementation/deployment 的授权。

评审输入：

- [`architecture/production-persistence-adapter-specification.md`](architecture/production-persistence-adapter-specification.md)；
- [`architecture/otlp-collector-production-profile.md`](architecture/otlp-collector-production-profile.md)；
- [`architecture/telemetry-to-evidence-admission-contract.md`](architecture/telemetry-to-evidence-admission-contract.md)；
- [`architecture/production-implementation-sequence.md`](architecture/production-implementation-sequence.md)；
- [`architecture/production-slo-and-evidence-gates.md`](architecture/production-slo-and-evidence-gates.md)。

## 2. Sessions（会话）

| session ID | provider/model | result |
|---|---|---|
| `TMAI-PRODUCTION-PATH-20260722-QIANFAN-01` | Baidu Qianfan / `ernie-4.5-turbo-128k` | `CONDITIONALLY_APPROVE_WITH_REVISIONS`；顺序 S1→S9 被认可；指出存储隔离验证、Collector HA、签名来源、阶段集成和 Pilot 演练缺口 |
| `TMAI-PRODUCTION-PATH-20260722-ARK-01` | Volcengine Ark / `deepseek-v4-flash-260425` | `NOT_RECOMMENDED`；指出 Collector HA/DR、Identity prerequisite、安全/数据治理、Owner/runbook、逐阶段 rollback 和试点覆盖缺口 |
| `TMAI-PRODUCTION-PATH-20260722-ARK-02` | Volcengine Ark / `deepseek-v4-flash-260425` | `RECOMMENDED_AS_CORRECT_PATH`；`recommend_sequence=true`；当前 production recommendation=false；confidence `moderate` |
| `TMAI-PRODUCTION-PATH-20260722-QIANFAN-02` | Baidu Qianfan / `ernie-4.5-turbo-128k` | `CONDITIONAL`；`recommend_sequence=yes`；当前 production recommendation=false；confidence `medium` |

调用使用现有 provider credentials，未将 key 写入 DBA。模型输出是 recommendation material（推荐材料），不是 Authority、customer adoption 或 production proof。

## 3. Objection Closure（异议关闭）

| objection | disposition | architecture change |
|---|---|---|
| Collector/DBOS storage 可能混用 | accepted | 加入 DSN、identity、network、volume、key、backup 隔离与 cross-wiring negative test |
| Collector 无 HA/failover | accepted | >=2 gateway replicas、anti-affinity、LB readiness/drain、per-replica WAL、failure drills、capacity envelope |
| 来源签名不足 | accepted with bounded semantics | Evidence provenance `P0`–`P3`；high-impact 至少 `P2` 或 Human Risk Decision；签名仍不是 Truth |
| S2/S3 之间无集成 gate | accepted | `S2.5`、`S3A`、`S3B` 和 `G3A`–`G3F` |
| Evidence 依赖未证明 Identity | accepted | `PR-G2I` Identity Continuity prerequisite；OTel Resource 禁止创建 Identity |
| 安全只在后期 | clarified and strengthened | `S1`–`S5` 每阶段先做 scoped security review，`S6` 再做综合 gate |
| 数据治理/合规缺失 | accepted | Data Steward、inventory、purpose、classification、retention、residency、incident 和 policy tests |
| 运维 Owner/runbook 不清 | accepted | 九类 role matrix、on-call/escalation、backup owner 和逐阶段 rollback/re-entry |
| 7/30 天 Pilot 可能不足 | clarified and strengthened | 7 + 30 = 至少 37 连续日；必须覆盖 full failure-domain inventory、backup/PITR、HA、OTLP、capacity、on-call；未覆盖则延长 |
| stateful trace routing 与 Collector 冲突 | rejected as factual mismatch, clarified | OTel 官方 gateway 模式支持 load-balancing exporter 按 trace ID 路由；该 affinity 不是 DBOS Authority |
| 需要跨 replica 同步 Collector WAL | rejected as wrong durability model, clarified | per-replica WAL 不是 consensus log；丢失必须计量；跨区持久需 `Q2_MESSAGE_QUEUE`；canonical RPO 属于 DBOS store |
| Evidence/SAEE SLO 不足 | accepted | 增加 `SLO-013`–`SLO-017` 及请求/准入/来源/zero-writeback 查询 |

## 4. Final Result（最终结论）

```text
PRODUCTION_PATH_AGENT_REVIEW_COMPLETE=true
PRODUCTION_IMPLEMENTATION_SEQUENCE_RECOMMENDED_BY_TWO_AGENTS=true
UNRESOLVED_SEQUENCE_DESIGN_BLOCKERS=0
DQ_018_HUMAN_DECISION_REQUIRED=true
IMMUTABLE_DBA_BASELINE_REQUIRED=true
ALL_IMPLEMENTATION_AND_CONFORMANCE_EVIDENCE_PENDING=true
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
PRODUCTION_READY=false
```

两路智能体认可“先建准入、再建生产持久化、再打开 OTLP/Collector、再独立 Evidence admission、最后 SAEE/Pilot/Production Decision”的生产路径。

他们也一致不推荐当前系统作为 production customer solution（生产客户解决方案）。剩余 blocker 是需要人类决策和直接实施证据的真实前置，不能用本记录关闭。

## 5. Immediate Gate（当前闸门）

原 production path review 使用的 OTLP 草案版本之后在未冻结工作树内刷新为 `1.11.0`，并新增 OpenTelemetry alignment matrix 与 Production Gate Evidence Contract。该 delta 已单独经过两路复审；最终两路均推荐 S0 Architecture Contract Freeze、均报告 design blockers `0`、均保持 production customer recommendation=false。详见 [`PRODUCTION-EVIDENCE-CONTRACT-AGENT-RECOMMENDATION.md`](PRODUCTION-EVIDENCE-CONTRACT-AGENT-RECOMMENDATION.md)。这不会反向改写本文件保留的初始拒绝历史。

### 5.1 Post-catalog Sequence Delta Review（目录形成后的序列差异复评）

56-case catalog 暴露旧 `S3A=offline decoder` 与 `S1` reference-conformance 的重复风险后，序列被修正为：

```text
S1 / DQ-018 = one pinned offline decoder + Telemetry Admission; no listener
S3A / DQ-020 = reuse S1 decoder contract + authenticated loopback listener
S3B / PR-G3 = multi-replica Collector + delivery reconciliation
```

两路 provider 对该精确差异再次评审：

| session ID | provider/model | result |
|---|---|---|
| `TMAI-PRODUCTION-PATH-SEQUENCE-DELTA-20260722-QIANFAN-01` | Baidu Qianfan / `ernie-4.5-turbo-128k` | `RECOMMENDED`；mapping correct=true；duplicate risk closed=true；DQ-018/DQ-020 boundary preserved=true；corrections=[]；production=false |
| `TMAI-PRODUCTION-PATH-SEQUENCE-DELTA-20260722-ARK-01` | Volcengine Ark / `deepseek-v4-flash-260425` | `RECOMMENDED`；mapping correct=true；duplicate risk closed=true；DQ-018/DQ-020 boundary preserved=true；corrections=[]；production=false |

这证明架构映射获得智能体推荐，不证明 decoder/listener/Collector 已实施。

```text
CURRENT_GATE=DQ_018_HUMAN_DECISION
DBA_BASELINE_COMMIT_PUSH_AUTHORIZED=false
DBOS_IMPLEMENTATION_AUTHORIZED=false
COLLECTOR_DEPLOYMENT_AUTHORIZED=false
EVIDENCE_ADMISSION_AUTHORIZED=false
PRODUCTION_PILOT_AUTHORIZED=false
```
