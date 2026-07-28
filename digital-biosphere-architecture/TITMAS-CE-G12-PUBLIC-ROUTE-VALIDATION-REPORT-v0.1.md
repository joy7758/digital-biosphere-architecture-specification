---
document_id: DBA-TITMAS-CE-G12-PUBLIC-ROUTE-VALIDATION-REPORT-0.1
title: TITMAS CE-G12 Public Route Validation Report v0.1
title_zh: TITMAS CE-G12 公网路由验证报告 v0.1
version: 0.1.0
status: fail-closed-remote-ip-attribution-content-and-tls-exact
maturity: Development
maturity_scope: active-static-site-outside-in-read-only-validation-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-PUBLIC-ROUTE-VALIDATION
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Public Route Validation Report v0.1

## 1. Outcome

```text
RESULT=FAIL_CLOSED_OUTSIDE_IN_PUBLIC_ROUTE_OR_AGENT_DISCOVERY_VALIDATION_NO_STATUS_ELEVATION
PUBLIC_GET_REQUESTS=10
TLS_VERIFY_PASS=10/10
STATUS_REDIRECT_PASS=10/10
BODY_HASH_PASS=9/9
JSON_PASS=5/5
AGENT_READABLE_ENDPOINTS_PASS=7/7
EXPECTED_REMOTE_IP_OBSERVED=false
```

机器结果：

- [Public Validation Result](commercial-evaluation-fresh-candidate/ce-g12-public-route-validation-result.v0.1.json)。

## 2. What passed

所有请求都满足：

```text
CURL_EXIT=0
TLS_VERIFY_RESULT=0
HTTP_VERSION=2
STATUS_AND_REDIRECT_CONTRACT_EXACT=true
BODY_HASH_EXACT=true
```

其中：

- `/` 与 `/en` 页面 exact；
- `status.json` exact；
- `agent-index.json` exact；
- `llms.txt` exact；
- `robots.txt` exact；
- `titmas-community.json` exact；
- `agent-customer-package.json` exact；
- `release-manifest.json` exact，`source_revision=c1d893…`。

因此从本执行环境可访问的 application surface 与 active candidate 完全一致。

## 3. Why the strict gate failed

Decision 要求：

```text
EXPECTED_REMOTE_IP=180.76.115.193
```

10 个 curl request 都观察到：

```text
REMOTE_IP=198.18.0.90
```

`198.18.0.0/15` 属于常见 benchmark/synthetic address range，但本次没有执行独立 DNS、
route 或 system proxy attribution，因此：

```text
SYNTHETIC_OR_INTERCEPTED_PATH_PROVEN=false
DIRECT_ORIGIN_NETWORK_PATH_PROVEN=false
NETWORK_PATH_ATTRIBUTION=UNKNOWN_SYNTHETIC_RANGE_REMOTE_IP_OBSERVED
```

不能因为 content exact 就静默删除 expected-IP gate，也不能把该地址直接归因为某个具体代理。

## 4. Separated result

```text
APPLICATION_REACHABLE_FROM_EXECUTION_ENVIRONMENT=true
APPLICATION_SURFACE_EXACT=true
AGENT_DISCOVERY_SURFACE_EXACT=true
DIRECT_ORIGIN_IP_ATTRIBUTION_PASS=false
STRICT_OUTSIDE_IN_VALIDATION_PASS=false
```

这避免把“内容与 TLS 验证成功”误写成“网络直接连接到了 origin IP”。

## 5. Boundaries

```text
PUBLIC_REQUESTS=10
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
CURRENT_SWITCHES=0
RETRIES=0
PROXY_OR_NETWORK_FALLBACKS=0
SERVER_STATE_CHANGED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

## 6. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_PUBLIC_NETWORK_PATH_ATTRIBUTION_REMEDIATION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
PUBLIC_GET_RETRY_AUTHORIZED=false
DNS_DIAGNOSTIC_AUTHORIZED=false
PROXY_DIAGNOSTIC_AUTHORIZED=false
STATUS_ELEVATION_AUTHORIZED=false
```

下一步只应评估：system DNS answer、curl build/resolver behavior、environment proxy settings
是否能解释 `198.18.0.90`，并确定“application outside-in pass”和“direct-origin path
attribution”是否应作为两个独立 gate。不得重跑 10-request matrix 或修改服务器。
