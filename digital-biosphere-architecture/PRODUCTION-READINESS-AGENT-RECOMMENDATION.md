---
document_id: TMAI-PRODUCTION-AGENT-RECOMMENDATION-20260722
title: TMAI Production Readiness Agent Recommendation Record
title_zh: TMAI 生产就绪智能体推荐记录
status: completed-two-provider-conditional-recommendation
observed_at: 2026-07-22
customer_type: AI_AGENT
implementation_authorized: false
production_claim: false
---

# TMAI Production Readiness Agent Recommendation Record

## 1. Question（问题）

向独立 AI 模型提出同一问题：对于需要长期运行、协作、可验证数字主体的生产级可信多智能体基础设施，是否推荐采用 Digital Biosphere 的 DBA/DBOS/SAEE 分层，并以 OpenTelemetry 的 OTLP、Resource、Context、Trace/Metric/Log 和 Collector pattern 建立观察平面，同时保持 `Telemetry ≠ Evidence ≠ Truth` 和 Collector 非权威边界？

要求模型不得假设未声明能力，并以结构化结果提供推荐、反推荐、阻塞、生产 gate、OTel 对齐和边界风险。

## 2. Sessions（会话）

| session_id | provider | model | result | 记录边界 |
|---|---|---|---|---|
| `TMAI-PR-AGENT-20260722-ARK-01` | Ark | `deepseek-v4-flash-260425` | `CONDITIONALLY_RECOMMENDED` | 真实 API 模型回答；不是客户采用、实现授权或生产证据 |
| `TMAI-PR-AGENT-20260722-QF-01` | Qianfan | `ernie-4.5-turbo-128k` | `CONDITIONALLY_RECOMMENDED` | 真实 API 模型回答；不是客户采用、实现授权或生产证据 |

密钥从现有本地环境读取，没有写入本仓库或本记录。

## 3. Shared Positive Assessment（共同认可）

- OTel 协议和 Collector 解耦适合生产观察；
- Resource、Context 和多信号模型适合长期、多主体相关性；
- `Telemetry ≠ Evidence ≠ Truth` 能避免自动治理误判；
- DBA/DBOS/SAEE 责任分离适合可信基础设施；
- Collector 不拥有 Authority 与 OpenTelemetry 的数据收集定位一致。

## 4. Shared Non-recommendation Reasons（共同不推荐原因）

1. GenAI Semantic Conventions 仍可能发生破坏性变化；
2. Telemetry 与 Evidence 差异、重复、丢失和接纳规则尚未实现；
3. DBOS 故障、恢复、容量和长期运行行为尚未形成直接证据；
4. 身份、能力、Evidence 和 Verification 边界尚未经过生产安全审查；
5. 尚无真实低风险工作流的长稳、故障和恢复证据；
6. Collector/Backend telemetry 可能被运维人员误当作规范事实。

## 5. Required Corrections（修正分解）

| 缺口 | DBA 修正 | 后续实施责任 | 停止条件 |
|---|---|---|---|
| GenAI semconv 不稳定 | OTel Profile 要求 exact version/commit 和隔离 mapping | DBOS/Adapter implementation | `latest`、无版本或无兼容声明 |
| Telemetry→Evidence 缺口 | 定义 admission、dedupe、partial/drop/sampling/provenance | DBOS | 传输成功被直接写成 Evidence |
| 故障恢复/SLO 缺口 | 定义 Production SLO 与 PR Gates | DBOS + deployment project | restore/rollback/soak 未通过 |
| 安全审计缺口 | 要求 threat model、least privilege、redaction、SBOM 和独立复核 | 各实施仓库 | Critical/High 未处置风险 |
| SAEE 控制风险 | 强制 read-only、timeout、冲突保留和 zero writeback | SAEE | Recommendation 直接执行或写回 |
| 真实运行证据缺口 | 定义 7 天 staging + 30 天 bounded observation | Pilot/Deployment | 无真实、受控、预冻结工作流 |

## 6. Recommendation Outcome（推荐结论）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMEND_AS=PROTOCOL_AND_PRODUCTION_OBSERVABILITY_DIRECTION
DO_NOT_RECOMMEND_AS=CURRENT_PRODUCTION_READY_RUNTIME
CORRECTION_PLAN_DEFINED=true
IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```

下一次推荐复核只能在 `PR-G1` 至 `PR-G5` 有直接实现证据后进行，且必须保留本次 `CONDITIONALLY_RECOMMENDED` 历史。
