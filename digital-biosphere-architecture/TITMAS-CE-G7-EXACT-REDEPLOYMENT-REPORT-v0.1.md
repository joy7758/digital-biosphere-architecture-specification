---
document_id: DBA-TITMAS-CE-G7-EXACT-REDEPLOYMENT-REPORT-0.1
title: TITMAS CE-G7 Exact Redeployment Report v0.1
title_zh: TITMAS CE-G7 精确重新部署报告 v0.1
version: 0.1.0
status: fail-closed-rollback-pass-controller-tls-failure
maturity: Development
maturity_scope: public-static-development-site-release-attempt
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G7
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G7 Exact Redeployment Report v0.1

## 1. Outcome

```text
CE_G7_EXECUTED=true
CE_G7_RESULT=FAIL_CLOSED_ROLLBACK_PASS
ATOMIC_SWITCH_PASS=true
SERVER_LOCAL_ROUTES_PASS=11/11
SERVER_LOCAL_SECURITY_HEADERS_PASS=6/6
CONTROLLER_PUBLIC_ROUTES_PASS=10/11
CONTROLLER_FAILURE_ROUTE=/en/
CONTROLLER_CURL_EXIT_CODE=35
RETRY_EXECUTED=false
GITHUB_VANTAGE_WORKFLOW_TRIGGERED=false
ROLLBACK_PASS=true
CURRENT_RELEASE=7da4bcf16eeec7de1c61031fe08fc04081cf8705
```

机器证据：

- [CE-G7 result](commercial-evaluation-exact-redeployment/ce-g7-result.v0.1.json)；
- [server switch receipt](commercial-evaluation-exact-redeployment/ce-g7-server-switch-receipt.v0.1.json)；
- [controller receipt](commercial-evaluation-exact-redeployment/ce-g7-controller-immediate.v0.1.json)；
- [rollback receipt](commercial-evaluation-exact-redeployment/ce-g7-rollback-receipt.v0.1.json)；
- [Decision](TITMAS-COMMERCIAL-EVALUATION-CE-G7-DECISION-RECORD.v0.1.json)。

## 2. What passed

- exact preconditions；
- archive bytes/SHA-256；
- atomic symlink switch；
- post-switch `nginx -t` 与 reload；
- server-local TLS path 的 11/11 HTTP 200、bytes 和 SHA-256；
- 6/6 required security headers；
- controller path 其余 10/11 路由。

这排除了“所有 server-local content 都不可读”，但不证明全局网络可靠或 TLS 根因。

## 3. Stop rule and rollback

controller 使用：

```text
curl 8.7.1
SecureTransport
LibreSSL/3.3.6
proxy_environment_present=false
```

第二个路由 `/en/` 返回 `curl exit 35`、无 HTTP code、0 bytes。没有 retry、fallback 或
TLS bypass。根据 CE-G7 Decision，run-request 未创建、GitHub workflow 未触发，并立即
原子回滚。

Rollback 结果：

```text
ROLLBACK_TARGET=7da4bcf16eeec7de1c61031fe08fc04081cf8705
NGINX_TEST_PASS=true
NGINX_RELOAD_PASS=true
ROOT_HASH_PASS=true
```

## 4. Truth boundary

```text
NEW_CONTRACT_WEBSITE_DEPLOYED=false
REDEPLOYMENT_ADMISSION_PASS=false
TIME_WINDOW_OBSERVATION_COMPLETED=false
TLS_ROOT_CAUSE_PROVEN=false
CONTENT_DEFECT_PROVEN=false
AVAILABLE_OFFERING=false
PRODUCTION_READY=false
SLA_DEFINED=false
CERTIFICATION_CREATED=false
```

CE-G7 证明 failure-close 与 rollback 控制有效，不证明发布成功。

## 5. New architecture issue

同一代 macOS system curl / SecureTransport / LibreSSL：

- GitHub-hosted macOS 在 CE-G5 通过 `12/12`；
- 本地 controller 在 CE-G7 的 `/en/` 出现 `curl exit 35`；
- CE-G3 也曾在本地路径出现一次 `curl exit 35`。

因此当前证据更接近 client/network-path-specific intermittent transport signal（特定客户端
或网络路径的间歇传输信号），但仍不足以证明 exact root cause。不能把 server-local
`11/11` 或 CE-G5 `24/24` 用来覆盖本次失败。

## 6. Next gate

```text
NEXT_ACTION=PREPARE_CE_G8_CONTROLLER_TLS_FAILURE_DIAGNOSIS_RECOMMENDATION
NEXT_ACTION_AUTHORIZED=false
AUTOMATIC_REDEPLOYMENT=false
```

CE-G8 应先区分：

- local system curl / SecureTransport path；
- local Python / OpenSSL path；
- DNS / IPv4 / IPv6 / connection reuse；
- server-side handshake evidence；
- controller 是否应是 admission gate 或只作为 non-independent diagnostic。

任何 live request、redeployment 或 policy change 仍需独立 exact Decision。
