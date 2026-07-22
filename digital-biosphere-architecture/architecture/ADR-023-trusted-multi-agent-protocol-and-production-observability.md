---
adr_id: ADR-023
title: Adopt Trusted Multi-Agent Protocol Direction and OpenTelemetry-aligned Production Observability
title_zh: 采纳可信多智能体协议方向与 OpenTelemetry 对齐的生产观测架构
status: accepted-architecture-baseline
decided_at: 2026-07-22
decided_by_ref: zhangbin
implementation_authorized: false
deployment_authorized: false
production_claim_authorized: false
---

# ADR-023: Trusted Multi-Agent Protocol and Production Observability

## Context（背景）

`Trusted Multi-Agent Infrastructure Developer Preview v0.1` 已发布，但仍是 package、规范、Demo 和受限只读评价链路，不是生产 Runtime 或生产采用。

Human Program Owner 明确更新长期战略：Digital Biosphere 是一个总项目，DBA、DBOS、SAEE 和 Digital Entities 是责任层；项目不得发展成普通 Agent Platform、Agent Framework、Workflow Tool 或 AI Cloud Platform，而应通过 Protocolization（协议化）成为长期运行、协作和可验证数字主体的可信基础设施。

同时要求后续生产化重度参考 OpenTelemetry。OpenTelemetry 提供开放的 Signal、Resource、Context、OTLP、Semantic Convention、SDK 和 Collector 解耦模式，但其 telemetry 不自动满足 DBOS Evidence、Verification、Authorization 或 SAEE Evaluation 语义。

## Decision（决定）

采纳以下架构基线：

1. 对外主定位为 `Trusted Multi-Agent Infrastructure`；Digital Biosphere 保持总项目和长期愿景；
2. 采用 `Trusted Multi-Agent Protocol v0.1` 作为协议化方向；
3. 核心协议对象为 Identity、Capability、Execution、Evidence、Verification 和 Evolution Interface；
4. 公开表达使用 Identity、Capability、Execution、Evidence 四个可信边界；
5. DBOS 定位为 `Trusted Multi-Agent Existence Infrastructure`，继续保持 `DBOS governs existence`；
6. SAEE 定位为 `Evolution Intelligence Layer`，继续保持 `SAEE governs evolution`；
7. 生产观察平面重度采用 OpenTelemetry 的 OTLP、Resource、Context、Trace/Metric/Log 和 Collector patterns；
8. OTel GenAI/MCP Semantic Conventions 只允许 exact-version/commit mapping，不冻结 Development 字段为 TMAP canonical contract；
9. 建立独立 Telemetry→Evidence admission，保持 `Telemetry ≠ Evidence ≠ Truth`；
10. 首个生产目标采用 self-hosted、single-tenant、human-governed profile；
11. 任何生产实现、部署或生产声明必须另行通过 Production Gates 和 Human Production Decision。

## Alternatives（替代方案）

### A. 继续扩展 Agent 功能

拒绝。该路线与 Foundation Model 和 Agent Framework 生态重复，并弱化项目在可信边界、生命周期和可验证性上的差异。

### B. 直接把 OpenTelemetry telemetry 当作 DBOS Evidence

拒绝。OTLP 允许 partial success、drop、retry 和 duplicate；sampling、敏感数据与不稳定 GenAI 字段也会破坏 Evidence 完整性声明。

### C. 自建完整 telemetry protocol

拒绝。除 TMAP 特有的身份、授权、Evidence、Verification 和 Evaluation 边界外，应优先复用开放且已有生态的 OTel/W3C 规范。

### D. 直接进入多租户云平台

拒绝作为首个生产目标。租户隔离、跨区域、计费和托管密钥会扩大当前验证面。

## Agent Recommendation Review（智能体推荐审查）

Ark `deepseek-v4-flash-260425` 与 Qianfan `ernie-4.5-turbo-128k` 对相同方案均给出 `CONDITIONALLY_RECOMMENDED`。两者共同要求版本钉住 GenAI 语义、正式 Telemetry→Evidence 接纳、故障恢复/SLO、安全审查和有界真实试点。

决定接受这些不推荐原因，并将其作为 `PR-G1` 至 `PR-G6` 的强制阻塞项。模型推荐不授权实现或生产声明。

## Consequences（影响）

- DBA 获得新的协议、生产就绪和 OTel mapping 规范入口；
- Verification Object 在核心数据契约中成为独立 DBOS 对象；
- DBOS 的下一实施方向应是可持久化、可恢复、可观测、版本化的存在治理基础，而不是 Agent 功能；
- SAEE 的下一实施方向应是受版本约束的只读评价 Adapter、失败隔离和长期评价，不是 Controller；
- Collector、SDK、Backend 和 Adapter 保持可替换；
- production-ready 只能由 exact deployment evidence 和显式 Human Decision 形成。

## Excluded Scope（排除范围）

本决定不：

- 修改 DBOS 或 SAEE 仓库；
- 创建 Collector 配置、endpoint、API、SDK 或 Runtime；
- 创建 Agent、Entity、Capability、Evidence 或 Permission 实例；
- 授权生产实施、服务器部署或真实工作流；
- 声称 OpenTelemetry alignment 等于安全认证或生产就绪；
- 改写 Developer Preview v0.1 的历史状态。

## Status（状态）

```text
ARCHITECTURE_DIRECTION_ACCEPTED=true
TMAP_SPECIFICATION_DEFINED=true
OTEL_OBSERVABILITY_PROFILE_DEFINED=true
PRODUCTION_READINESS_BASELINE_DEFINED=true
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
