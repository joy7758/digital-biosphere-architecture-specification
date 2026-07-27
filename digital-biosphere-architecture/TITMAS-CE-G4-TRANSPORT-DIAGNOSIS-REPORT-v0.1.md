---
document_id: DBA-TITMAS-CE-G4-TRANSPORT-DIAGNOSIS-REPORT-0.1
title: TITMAS CE-G4 Transport Failure Diagnosis Report v0.1
title_zh: TITMAS CE-G4 传输故障诊断报告 v0.1
version: 0.1.0
status: pass-bounded-diagnostic-root-cause-unresolved
maturity: Development
maturity_scope: exact-ce-g4-read-only-diagnosis
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G4
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G4 Transport Failure Diagnosis Report v0.1

## 1. Verdict（结论）

```text
CE_G4_DIAGNOSTIC_EXECUTION=PASS
REQUESTS_EXECUTED=12/12
DEFAULT_PATH=6/6_PASS
DIRECT_RESOLVE_PATH=5/6_PASS
TRANSPORT_FAILURES=1
HTTP_200_HASH_CONSISTENCY=PASS
EXACT_ROOT_CAUSE_PROVEN=false
REDEPLOYMENT_AUTHORIZED=false
```

诊断执行符合授权，但没有证明 exact root cause。机器结果：

- [result](commercial-evaluation-agent-entry-transport-diagnosis/ce-g4-transport-diagnosis-result.v0.1.json)
- [Schema](commercial-evaluation-agent-entry-transport-diagnosis/ce-g4-transport-diagnosis-result.schema.v0.1.json)

## 2. Diagnostic Matrix（诊断矩阵）

固定两个资源：

- `/llms.txt`
- `/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json`

固定两条路径：

- `DEFAULT_PATH` → remote IP `198.18.0.90`；
- `DIRECT_RESOLVE_PATH` → remote IP `180.76.115.193`。

三轮顺序执行；无 retry、fallback、parallel request 或 TLS bypass。

| Path class | Result | Failure |
|---|---:|---|
| Default | `6/6 PASS` | 0 |
| Direct resolve | `5/6 PASS` | 1 × `LibreSSL SSL_ERROR_SYSCALL` |

失败：

```text
ROUND=3
PATH_CLASS=DIRECT_RESOLVE_PATH
TARGET=/llms.txt
CURL_EXIT_CODE=35
HTTP_CODE=null
SSL_VERIFY_RESULT=1
LATENCY_SECONDS=0.052739
```

## 3. Server Correlation（服务器关联）

同期聚合日志：

```text
NGINX_ERROR_LINES=0
NGINX_SSL_OR_HANDSHAKE_ERRORS=0
ACCESS_5XX=0
JOURNAL_WARNINGS=0
RAW_LOGS_PERSISTED=false
```

这些记录没有证明服务器故障，也不能排除未被当前日志配置捕获的 handshake-level failure。

## 4. Hypothesis Assessment（假设评估）

| Hypothesis | Result | Basis |
|---|---|---|
| Asset-specific content failure | `NOT_SUPPORTED` | 不同资源出现同类错误；所有 HTTP 200 body hash 一致 |
| Default proxy path uniquely fails | `REFUTED` | 唯一 CE-G4 failure 发生在 direct-resolve path |
| New release content causes failure | `NOT_SUPPORTED` | CE-G4 在已回滚旧版本上仍复现 |
| Transient client/network TLS path | `SUPPORTED_NOT_PROVEN` | 短暂 handshake error，后继请求成功 |
| Server TLS failure | `OPEN_NOT_PROVEN` | 服务器无 error/5xx，但日志不足以完全排除 |
| Exact root cause | `UNRESOLVED` | 当前只有一个客户端机器和一个服务器 |

## 5. Commercialization Effect（商业化效果）

该结果证明：

- TITMAS 可以保留失败并按策略回滚；
- 机器入口内容在所有成功请求间字节一致；
- 当前单机的 default/direct 对照不足以证明可用性。

该结果不证明：

- production reliability；
- SLA；
- root cause closure；
- public entry availability；
- customer adoption 或 commercial offering。

## 6. Next Gate（下一闸门）

必须先满足
[Public Entry Redeployment Admission Policy v0.1](architecture/titmas-public-entry-redeployment-admission-policy-v0.1.md)：

```text
INDEPENDENT_NETWORK_VANTAGES>=2
DISTINCT_EGRESS_PATHS>=2
DISTINCT_TLS_CLIENT_STACKS>=2
HTTP_200_BODY_HASH_CONSISTENCY=true
TLS_VERIFICATION_BYPASS=false
FAILURES_PRESERVED=true
```

当前默认路径与 direct-resolve 路径来自同一台 Mac，不算两个 independent vantage。
下一步只能准备独立视角观察和重新部署决定；执行尚未授权。
