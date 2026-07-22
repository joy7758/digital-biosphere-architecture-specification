---
document_id: TMAI-OTEL-COLLECTOR-DEPLOYMENT-PROFILE-AGENT-REVIEW-20260722-001
title: TMAI OpenTelemetry Collector Deployment Profile Agent Recommendation
title_zh: TMAI OpenTelemetry Collector 部署画像智能体建议
status: two-provider-post-hardening-review-complete
reviewed_at: 2026-07-22
authority: advisory-only
human_decision_created: false
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# TMAI OpenTelemetry Collector Deployment Profile Agent Recommendation

中文：TMAI OpenTelemetry Collector（开放遥测采集器）部署画像智能体建议。

## 1. Review Boundary（评审边界）

本记录执行 AGENTS 的 Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）。
问题被拆成两个互不替代的判断：

1. 是否推荐 proposed non-executable profile（拟议非执行画像）进入 bounded Human Architecture
   Review（有界人工架构审查）；
2. 是否推荐当前 Runtime、deployment 或 production use（生产使用）。

模型回答是 Recommendation，不是 Architecture Decision、`DQ-020` Authorization、客户采用或
OpenTelemetry 认证。本轮没有创建 Agent 实例；只执行了两个既有模型 API 的受控 advisory session。

| provider | model | authority |
|---|---|---|
| Baidu Qianfan（百度千帆） | `ernie-4.5-turbo-128k` | Recommendation only |
| Volcengine Ark（火山方舟） | `deepseek-v4-flash-260425` | Recommendation only |

API key 只从 `/Users/zhangbin/GitHub/SAEE/.env.local` 读取，没有写入本仓库、prompt、输出或工件。

## 2. Initial Challenge Review（首轮挑战审查）

首轮只给出 profile scope、边界、未决输入和 existing catalog reuse（现有目录复用）。

| provider | initial recommendation | human review | current runtime/deployment | useful challenge |
|---|---|---|---|---|
| Qianfan | `CONDITIONALLY_RECOMMENDED` | `true` | `false` | 要求把 synthetic-only、composite readiness、transform activation 和 config update 机制写得更可执行 |
| Ark | `NOT_RECOMMENDED` | `true` | `false` | 正确拒绝把未决 Owner/topology/budget/artifacts 写成部署就绪；同时暴露 queue/WAL state、mTLS/auth extension 和 internal telemetry 的易误读点 |

首轮 `NOT_RECOMMENDED` 是对“当前可部署/可生产”的正确否定，不推翻
`recommended_for_human_review=true`。模型把 intentional blockers（故意保留的阻塞输入）混入
document corrections（文档修正）后，本轮按来源事实做了分类，未把模型措辞直接升级为规范事实。

## 3. Corrections Applied（已完成修正）

| challenge | architecture correction | direct evidence |
|---|---|---|
| staging-only 只有叙述、无 fail-closed contract | 只允许带 immutable reference/digest、source identity、`CONFORMANCE` purpose 和 retention 的 approved synthetic fixture；其他输入拒绝 | deployment profile `scope` + readiness matrix `Staging input gate` |
| remote config 被误读为缺少更新机制 | 明确 v0.1 只用 immutable versioned config，经 static/security/synthetic gates、canary、滚动重启和 exact rollback | deployment profile `configuration_contract.update_mechanism` |
| Alpha health 之外没有最小 readiness 定义 | 规定 8 项 external composite readiness floor；threshold 为空时 fail closed | deployment profile `topology.load_balancer.minimum_readiness_predicates` |
| `stateful_processors=false` 与 WAL 看似冲突 | 明确跨请求 processor state 禁止，per-exporter queue/per-replica WAL 是唯一 local transport-state exception | deployment profile `topology.gateway_tier.only_local_state_exception` |
| 无 auth extension 被误读为无认证 | 明确首阶段只候选 native receiver TLS/mTLS + external network/source policy；OIDC/bearer 需先修改 `DQ-025` inventory | readiness matrix boundary 2 |
| transform enable trigger 不清晰 | 绑定 Human-approved versioned config + static/security/synthetic gates + `CFG-004/005/006` | deployment profile `pipeline_contract.transform` |
| 可能通过修改 profile effects 表示实施 | effects 永远 false；未来 implementation/deployment result 为独立工件 | readiness matrix Stage Freeze Contract |

## 4. Post-hardening Delta Review（加固后增量复评）

复评明确定义：`recommendation` 只问“是否适合作为有界人工审查输入”；Runtime/deployment 单独回答。

| provider | bounded human-review recommendation | current runtime/deployment | boundary/authority errors | required document corrections | duplicate construction | production ready |
|---|---|---:|---:|---:|---:|---:|
| Qianfan | `CONDITIONALLY_RECOMMENDED` | `false` | 0 | 0 | 0 | `false` |
| Ark | `RECOMMENDED` | `false` | 0 | 0 | 0 | `false` |

两路共同结论：

- `recommended_for_human_review=true`；
- `recommended_for_current_runtime_or_deployment=false`；
- 没有开放的 boundary/authority error；
- 没有必须在人工审查前修复的文档错误；
- 没有必要的新 conformance catalog；
- Owner、repo、artifact、topology、budget、threshold、runbook、review 和 direct results 仍是未来输入；
- `PRODUCTION_READY=false`。

两模型把 dynamic control plane 或 OIDC/bearer extension 列为“future input”。本规范明确二者均不是
v0.1 必需输入，而是被排除的替代方案：native TLS/mTLS 和 immutable rollout 足以定义首个候选；
未来若选择二者才触发 `DQ-025` inventory amendment。该措辞记为 residual model misclassification
（模型残余误分类），不构成开放文档错误。

## 5. Final Recommendation Record（最终建议记录）

```text
AGENT_RECOMMENDATION=RECOMMENDED_FOR_BOUNDED_HUMAN_ARCHITECTURE_REVIEW
QIANFAN_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
ARK_RECOMMENDATION=RECOMMENDED
RECOMMENDED_FOR_CURRENT_RUNTIME_OR_DEPLOYMENT=false
BOUNDARY_OR_AUTHORITY_ERRORS=0
REQUIRED_DOCUMENT_CORRECTIONS_BEFORE_HUMAN_REVIEW=0
UNNECESSARY_DUPLICATE_CONSTRUCTION=0
HUMAN_DECISION_CREATED=false
DQ_020_STATUS=BLOCKED_INPUT
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```

这份建议只允许把 deployment profile 作为 `DQ-020` 的一个 architecture input（架构输入）继续
维护。它不允许创建配置、build、listener、Collector、Runtime、Telemetry、Evidence 或 Permission。
