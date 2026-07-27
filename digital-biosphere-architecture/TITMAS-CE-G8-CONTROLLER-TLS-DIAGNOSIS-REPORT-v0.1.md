---
document_id: DBA-TITMAS-CE-G8-CONTROLLER-TLS-DIAGNOSIS-REPORT-0.1
title: TITMAS CE-G8 Controller TLS Failure Diagnosis Report v0.1
title_zh: TITMAS CE-G8 控制端 TLS 失败诊断报告 v0.1
version: 0.1.0
status: inconclusive-log-correlation-fail-closed
maturity: Development
maturity_scope: controller-transport-diagnosis-on-rollback-release
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G8
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G8 Controller TLS Failure Diagnosis Report v0.1

## 1. Outcome

```text
CE_G8_EXECUTED=true
CONTROLLER_REQUESTS_EXECUTED=4/4
CONTROLLER_REQUESTS_PASS=4/4
CONTROLLER_FAILURE_REPRODUCED=false
CONTENT_HASH_CONSISTENCY_PASS=true
SERVER_CORRELATION=FAIL_CLOSED
SERVER_CORRELATION_ERROR_CLASS=error
COMPOSITE_CLASSIFICATION=INCONCLUSIVE
ROOT_CAUSE_PROVEN=false
REDEPLOYMENT=false
```

机器证据：

- [controller receipt](commercial-evaluation-controller-tls-diagnosis/ce-g8-controller.v0.1.json)；
- [server correlation receipt](commercial-evaluation-controller-tls-diagnosis/ce-g8-server-correlation.v0.1.json)；
- [composite](commercial-evaluation-controller-tls-diagnosis/ce-g8-composite.v0.1.json)；
- [result](commercial-evaluation-controller-tls-diagnosis/ce-g8-result.v0.1.json)。

## 2. Controller observations

四个 request matrix entries 都只执行一次并通过：

| ID | Stack/path | Result |
|---|---|---|
| A | system curl，normal | PASS |
| B | system curl，direct IPv4 + HTTP/1.1 | PASS |
| C | Python/OpenSSL，normal DNS | PASS |
| D | Python/OpenSSL，direct IPv4 + SNI | PASS |

四个响应都是 48045 bytes，SHA-256：

```text
8169a448f400b7b88184d4902a3d44edf58c6ac364b923ec0c1130585c91d69a
```

环境分类：

```text
SYSTEM_HTTP_PROXY=LOOPBACK_ENABLED
SYSTEM_HTTPS_PROXY=LOOPBACK_ENABLED
ROUTE_INTERFACE_CLASS=TUNNEL
NORMAL_IPV4_CLASS=SYNTHETIC_198_18_0_0_15
DIRECT_IPV4_CLASS=PUBLIC_IPV4
```

这些事实支持“本地路径包含 proxy/TUN interception（代理/TUN 拦截）”，但本次没有失败，
所以不能证明它造成 CE-G7 的 `curl exit 35`。

## 3. Correlation failure

server correlator 遵守 exact `12:31:56Z–12:31:57Z` window、0 padding、no raw-log
persistence，但工具返回：

```text
status=FAIL_CLOSED
error_class=error
```

根据 CE-G8 Decision，没有增加 SSH session 或扩大窗口，也没有重跑请求。由于服务器
handshake/access signal 未被有效评估，综合分类必须保持 `INCONCLUSIVE`。

## 4. Non-claims

```text
NO_FAILURE_OBSERVED_NE_ROOT_CAUSE_RESOLVED=true
PASSING_CLIENT_NE_FIX=true
PROXY_TUN_OBSERVED_NE_CAUSE_PROVEN=true
CORRELATOR_FAILURE_NE_SERVER_FAILURE=true
POLICY_CHANGED=false
REDEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
SLA_DEFINED=false
```

## 5. Next gate

```text
NEXT_ACTION=PREPARE_CE_G9_OFFLINE_LOG_CORRELATOR_REMEDIATION_RECOMMENDATION
NEXT_ACTION_AUTHORIZED=false
NEW_PUBLIC_REQUESTS_AUTHORIZED=false
NEW_SSH_SESSIONS_AUTHORIZED=false
```

CE-G9 应只做 offline fixture、stage-specific sanitized errors、跨 Python 版本测试和 exact
window parser 修正；不能重跑 CE-G8 或重新部署。
