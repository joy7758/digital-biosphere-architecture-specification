---
document_id: DBA-TITMAS-PUBLIC-ENTRY-REDEPLOYMENT-ADMISSION-POLICY-0.1
title: TITMAS Public Entry Redeployment Admission Policy v0.1
title_zh: TITMAS 公开入口重新部署准入策略 v0.1
version: 0.1.0
status: development-policy-defined-not-executed
maturity: Development
maturity_scope: public-static-entry-redeployment
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G4
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Fail-closed redeployment admission policy; no Runtime, availability guarantee, SLA, certification, commercial offering, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs:
  - commercial-evaluation-agent-entry-transport-diagnosis/ce-g4-transport-diagnosis-result.v0.1.json
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-redeployment-admission-policy
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS Public Entry Redeployment Admission Policy v0.1

## 1. Purpose（目的）

本策略定义 CE-G3 回滚后，公开机器入口再次部署前必须具备的证据。它解决：

> 如何区分 release content defect（发布内容缺陷）与 observation transport instability
> （观察传输路径不稳定），同时保持失败关闭。

本策略不是部署授权。

## 2. Independence Definition（独立性定义）

一个 independent network vantage（独立网络视角）必须同时满足：

- 独立执行环境；
- 独立 network egress；
- 独立 DNS/connection path；
- 可记录的 TLS client stack；
- 与另一 vantage 不共享同一 local proxy/TUN；
- 不从另一 vantage 代理请求。

同一台机器上的：

- default DNS；
- `--resolve`；
- IPv4/IPv6 切换；
- 不同 curl 参数；

不构成两个 independent vantage。

## 3. Minimum Evidence（最低证据）

重新部署决定前至少需要：

```text
VANTAGES>=2
DISTINCT_NETWORK_EGRESS>=2
DISTINCT_TLS_CLIENT_STACKS>=2
ROUNDS_PER_VANTAGE>=3
CRITICAL_ROUTES_PER_ROUND>=4
RETRY_WITHIN_ROUND=false
TLS_VERIFICATION_BYPASS=false
```

Critical routes：

```text
/
/llms.txt
/agent-index.json
/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
```

每条记录必须包含 timestamp、vantage reference、TLS stack、resolved/remote IP、HTTP code、
latency、bytes、SHA-256 和 failure class。

## 4. Content Gate（内容闸门）

以下必须全部通过：

- local static export；
- release manifest；
- remote manifest；
- contract/schema positive validation；
- negative boundary validation；
- all HTTP 200 body hashes match the expected release manifest；
- no machine truth elevation；
- previous rollback target remains available。

任何 body hash mismatch 都是 hard stop，不得解释为 transient transport。

## 5. Transport Gate（传输闸门）

结果分类：

| Result | Gate effect |
|---|---|
| 所有独立视角全部通过 | `TRANSPORT_OBSERVATION_PASS`，仍需 exact redeployment decision |
| 任一视角出现 TLS/transport failure | `TRANSPORT_OBSERVATION_UNSTABLE`，禁止重新部署 |
| HTTP 4xx/5xx | `PUBLIC_ROUTE_FAIL`，禁止重新部署 |
| 只有同一机器多路径通过 | `INSUFFICIENT_INDEPENDENCE` |
| 使用 retry 或 TLS bypass | `INVALID_OBSERVATION` |

该 gate 不定义 uptime、SLO 或 SLA。

## 6. Redeployment Decision Requirements（重新部署决定要求）

即使所有准入证据通过，仍必须有独立 exact decision，包含：

- source revision；
- immutable target directory；
- current and rollback symlink targets；
- archive SHA-256；
- manifest count；
- health routes；
- independent observation receipts；
- switch、rollback 和 failure preservation rules；
- no-product/no-SLA/no-production effects。

Observation pass 不自动产生 Deployment Authorization。

## 7. Failure Preservation（失败保留）

- 不允许删除 CE-G3 failed release；
- 不允许删除 CE-G3 archive；
- 不允许把 11/12 改写为 12/12；
- 不允许用后续成功覆盖 LibreSSL failures；
- 根因未知必须保持 `UNRESOLVED`；
- 新证据只能追加或显式 supersede，不能静默改写。

## 8. Current State（当前状态）

```text
POLICY_DEFINED=true
POLICY_MATURITY=Development
INDEPENDENT_VANTAGES_VALIDATED=0
REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT_AUTHORIZED=false

RUNTIME_CREATED=false
API_CREATED=false
AGENT_CREATED=false
PERMISSION_CREATED=false
CERTIFICATION_CREATED=false
SLA_DEFINED=false
COMMERCIAL_OFFER_CREATED=false
PRODUCTION_READY=false
```
