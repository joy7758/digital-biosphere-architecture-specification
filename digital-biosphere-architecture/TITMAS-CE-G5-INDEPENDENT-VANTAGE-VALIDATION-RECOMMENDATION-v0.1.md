---
document_id: DBA-TITMAS-CE-G5-INDEPENDENT-VANTAGE-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G5 Independent Vantage Validation Recommendation v0.1
title_zh: TITMAS CE-G5 独立视角验证建议 v0.1
version: 0.1.0
status: exact-bounded-recommendation
maturity: Development
maturity_scope: public-entry-transport-observation
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G5 Independent Vantage Validation Recommendation v0.1

## 1. Recommendation

建议执行一个失败关闭、无重试、只读的 independent-vantage observation（独立视角观察）：

```text
GitHub-hosted Ubuntu runner
  Python http.client + OpenSSL

GitHub-hosted macOS runner
  system curl + reported TLS backend

each: 3 rounds x 4 fixed public routes
total public-origin GETs: 24
```

两者必须是独立 ephemeral job（临时任务），记录精确客户端与 TLS stack。源站只执行
read-only correlation（只读相关性核对），不作为第三个客户端视角。

## 2. Why this option

CE-G4 已证明同一 Mac 上的 default path 与 direct-resolve path 不能构成两个独立视角，
且出现过 `LibreSSL SSL_ERROR_SYSCALL`。以下候选被拒绝：

| Candidate | Disposition | Reason |
|---|---|---|
| 百度云源站 + GitHub Actions | Rejected | 源站请求自身不能可靠证明独立外部网络路径 |
| 本地 Mac 代理/TUN + GitHub Actions | Rejected | 本地代理/TUN 使纯净网络与 TLS 路径独立性无法充分证明 |
| Ubuntu + macOS GitHub-hosted runners | Recommended | 独立 job、可验证不同出口、可记录不同客户端/TLS stack；不改源站 |

## 3. Agent-customer recommendation gate

咨询模型：

```text
provider=Alibaba Cloud Model Studio compatible endpoint
model=qwen3.7-plus
role=independent AI-agent infrastructure customer reviewer
advisory_only=true
```

修订后 exact plan 的返回：

```text
verdict=RECOMMENDED
would_recommend_to_agent_customer=true
blocking_corrections=0
confidence=0.95
```

采用的直接理由：

- 两个独立执行环境；
- 通过源站日志中来源 IP 的 salted SHA-256（加盐摘要）确认不同 network egress；
- Ubuntu 与 macOS 使用不同客户端/TLS stack；
- 24 个固定公开 GET，无 retry、fallback 或 TLS bypass；
- 内容与固定当前公开版本 SHA-256 基线逐项比较；
- 只保留摘要和计数，不持久化原始客户端 IP 或原始日志。

模型输出是 advisory evidence（建议证据），不是 Decision、Authorization、Customer
Adoption、Conformance 或 Truth。模型关于“底层 IP 池物理隔离”的表述没有独立证据，
因此不采用；出口独立性只由本次源站相关性结果决定。

## 4. Exact minimum scope

固定路由：

```text
/
/llms.txt
/agent-index.json
/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
```

固定执行：

```text
COUNTED_VANTAGES=2
ROUNDS_PER_VANTAGE=3
ROUTES_PER_ROUND=4
PUBLIC_ORIGIN_GET_CAP=24
RETRY=false
FALLBACK=false
TLS_VERIFICATION_BYPASS=false
PARALLEL_REQUESTS_WITHIN_VANTAGE=false
```

每个请求记录：

- timestamp；
- run/vantage reference；
- client 与 TLS stack；
- resolved remote IP；
- HTTP status；
- latency；
- bytes；
- SHA-256；
- failure class。

源站相关性只允许：

- 按 exact run-scoped User-Agent 过滤；
- 每个 vantage 精确计数 12 条；
- 使用同一个 run-scoped salt 对来源 IP 计算 SHA-256；
- 只持久化两个摘要、计数和 `same_source=false/true`；
- 不持久化原始 IP 或原始日志。

## 5. Pass and stop rules

只有以下全部成立才可记录 `TRANSPORT_OBSERVATION_PASS`：

- 24/24 请求成功；
- 全部 HTTP 200；
- 每个响应 hash 匹配固定 current-release baseline；
- 两个执行环境证据完整；
- 两个 client/TLS stack 不同；
- 两个来源 IP salted hash 不同；
- 源站每个 User-Agent 精确匹配 12 条；
- 未使用 retry、fallback、TLS bypass 或配置变更。

任一缺失均失败关闭，且：

```text
REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT_AUTHORIZED=false
```

即使 observation pass，也只能进入独立 redeployment decision，不能自动部署。

## 6. False effects and non-claims

```text
WEBSITE_REDEPLOYMENT_AUTHORIZED=false
SERVER_CONFIGURATION_CHANGE_AUTHORIZED=false
PRODUCTION_READY=false
SLA_DEFINED=false
COMMERCIAL_OFFER_CREATED=false
CUSTOMER_ADOPTION_PROVEN=false
CERTIFICATION_CREATED=false
DBOS_OR_SAEE_CHANGE_AUTHORIZED=false
RUNTIME_CREATED=false
API_CREATED=false
AGENT_CREATED=false
ENTITY_CREATED=false
PERMISSION_CREATED=false
```

本观察不证明全球可用性、生产高可用、业务逻辑正确性、Agent 安全性或未知攻击免疫。

## 7. Standing-directive eligibility

本建议绑定一个 exact option、固定 target、24 请求上限、隐私边界、失败关闭规则、
rollback effect（无部署所以无需切换）和所有 false effects，满足
`TITMAS-CS-STANDING-001` 的候选适用条件。执行仍必须先有独立 Decision Record。
