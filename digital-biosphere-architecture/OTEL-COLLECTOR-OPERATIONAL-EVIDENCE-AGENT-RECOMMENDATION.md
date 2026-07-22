---
document_id: TMAI-OTEL-COLLECTOR-OPERATIONAL-EVIDENCE-AGENT-RECOMMENDATION-0.1
title: OpenTelemetry Collector Operational Evidence Agent Recommendation
title_zh: OpenTelemetry Collector 运维证据智能体建议
status: completed-advisory-review-not-implementation-authorization
observed_at: 2026-07-22
primary_repository: digital-biosphere-architecture
decision_reference: DQ-020
---

# OpenTelemetry Collector Operational Evidence Agent Recommendation

中文：OpenTelemetry Collector（开放遥测采集器）运维证据智能体建议。

## 1. Scope（范围）

根据仓库 `AGENTS.md`，在把 Collector operational evidence contract（运维证据契约）纳入生产架构
候选输入前，使用两个真实、相互独立的模型 API 进行边界审查。审查只评价架构文档是否值得进入
bounded human architecture review（有限人工架构审查）；它不创建 Agent instance（智能体实例）、
Runtime（运行时）、Collector configuration、query、alert、runbook、Evidence 或 Permission。

```text
Agent recommendation != Human decision
Architecture review != Implementation authorization
Model API response != Customer adoption
Recommended contract != Recommended current production deployment
```

API key 仅从 `/Users/zhangbin/GitHub/SAEE/.env.local` 读取到进程环境；未复制到 DBA、未写入报告、
未输出到终端。模型请求和回答均未改变 SAEE 或 DBOS。

## 2. Reviewers（审查模型）

| provider / model | role | authority |
|---|---|---|
| Baidu Qianfan（百度千帆）/ `ernie-4.5-turbo-128k` | independent advisory reviewer（独立建议审查者） | Recommendation only（仅建议） |
| Volcengine Ark（火山方舟）/ `deepseek-v4-flash-260425` | independent advisory reviewer（独立建议审查者） | Recommendation only（仅建议） |

两次最终复核使用同一边界摘要：精确部署 digest（摘要）、query/rule/route/runbook reference（引用）
当前故意为 `null`；不存在的实现对象不得被虚构；空值阻断实现、测量、部署和生产闸门，但不阻断对
规范本身的有限人工架构审查。

## 3. Review History（审查历史）

| review | result | retained finding |
|---|---|---|
| Qianfan initial review | `CONDITIONALLY_RECOMMENDED` | 正确拒绝当前 Runtime/production；但把有意留空的 resource、alert 和 runbook 摘要误判为审查前文档错误 |
| Ark initial review | `RECOMMENDED` | 允许有限人工架构审查；当前 Runtime/production=false；无边界错误或重复目录建议 |
| Contract hardening | machine contract changed | 增加 `INTENTIONALLY_UNRESOLVED_FAIL_CLOSED`、禁止伪造值、分离“允许架构审查”和“禁止运行授权” |
| Qianfan final delta review | `RECOMMENDED` | bounded human review=true；runtime/deployment=false；production=false；document corrections=[]；boundary errors=[] |
| Ark final delta review | `RECOMMENDED` | bounded human review=true；runtime/deployment=false；production=false；document corrections=[]；boundary errors=[] |

## 4. Final Recommendation（最终建议）

两个模型最终都认可：该契约可以作为 `DQ-020` 的 architecture review input（架构审查输入），原因是
未解析值已机器可检验地失败关闭，而不是被伪装成已有运行制品。

共同保留的 future implementation inputs（未来实现输入）包括：

- exact deployment/config/resource digests（精确部署／配置／资源摘要）；
- exact query/rule/route/runbook bindings（精确查询／规则／路由／运行手册绑定）；
- direct failure/capacity/durability/rollback results（直接故障／容量／持久性／回滚结果）；
- independent technical and security review outputs（独立技术与安全审查结果）。

它们是未来输入，不是当前架构文档错误；缺任一输入都不能批准 implementation、measurement、
deployment 或 `PR-G3` closure。

## 5. Decision Boundary（决策边界）

```text
TWO_MODEL_ARCHITECTURE_REVIEW_RECOMMENDED=true
BOUNDED_HUMAN_ARCHITECTURE_REVIEW_ALLOWED=true
REMAINING_ARCHITECTURE_DOCUMENT_CORRECTIONS=0
BOUNDARY_OR_AUTHORITY_ERRORS=0
CURRENT_RUNTIME_OR_DEPLOYMENT_RECOMMENDED=false
PRODUCTION_READY=false
DQ_020_STATUS=BLOCKED_INPUT
```

本建议不能替代 `DQ-020` 人类决定，也不能由模型回答反向生成 platform owner、部署仓库、配置、
证据、权限或生产状态。
