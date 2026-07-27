---
document_id: DBA-TITMAS-CE-G4-TRANSPORT-FAILURE-DIAGNOSIS-RECOMMENDATION-0.1
title: TITMAS CE-G4 Transport Failure Diagnosis Recommendation v0.1
title_zh: TITMAS CE-G4 传输故障诊断建议 v0.1
version: 0.1.0
status: recommended-exact-bounded-read-only-diagnosis
maturity: Development
maturity_scope: exact-ce-g3-transport-failure
owner_ref: zhangbin
decision_reference: TITMAS-CS-STANDING-001
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Read-only transport diagnosis only; no website redeployment, Runtime, API, SLA, certification, production, or commercial compatibility claim."
implementation_feedback_refs: []
conformance_refs:
  - commercial-evaluation-agent-entry-publication/ce-g3-publication-receipt.v0.1.json
known_limitations: [SEE_DOCUMENT_BODY]
document_type: bounded-diagnostic-recommendation
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G4 Transport Failure Diagnosis Recommendation v0.1

## 1. Current Evidence（当前证据）

CE-G3 留下两个相互独立、未重试的相同 TLS failure：

| Attempt | Path | Error |
|---|---|---|
| uncounted stdout-missing attempt | `/llms.txt` | `curl (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL` |
| auditable round 2 | `/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json` | `curl (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL` |

两个不同资源出现相同 handshake-level error，降低 asset-specific content failure 的可能性。

只读环境证据：

```text
LOCAL_CURL=8.7.1
LOCAL_TLS_STACK=SecureTransport_LibreSSL_3_3_6
SYSTEM_HTTP_PROXY=LOOPBACK_ENABLED_PORT_1080
SYSTEM_HTTPS_PROXY=LOOPBACK_ENABLED_PORT_1080
LOCAL_DNS_REDCRAG_CN=198.18.0.90
DNS_CLASS=SYNTHETIC_BENCHMARK_RANGE
ACTUAL_SERVER=180.76.115.193

SERVER_NGINX_ERROR_LINES_WINDOW=0
SERVER_NGINX_JOURNAL_WARNING_LINES=0
SERVER_ACCESS_5XX_WINDOW=0
```

当前最合理但尚未证明的假设：

```text
PRIMARY_HYPOTHESIS=LOCAL_PROXY_OR_TUN_TRANSPORT_PATH
EXACT_ROOT_CAUSE_PROVEN=false
```

## 2. Recommendation（建议）

推荐一个 exact action：

```text
RUN_BOUNDED_PROXY_PATH_VS_DIRECT_RESOLVE_TLS_DIAGNOSTIC
```

不是重新部署。

## 3. Diagnostic Matrix（诊断矩阵）

固定两个公开只读资源：

```text
/llms.txt
/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
```

固定两条客户端路径：

1. `DEFAULT_PATH`：当前默认网络/TUN/DNS 路径；
2. `DIRECT_RESOLVE_PATH`：
   `curl --noproxy '*' --resolve redcrag.cn:443:180.76.115.193`。

执行：

```text
ROUNDS=3
REQUESTS_PER_ROUND=4
TOTAL_REQUEST_CAP=12
SEQUENTIAL=true
RETRY=false
FALLBACK=false
MAX_TIME_SECONDS=20
```

每条记录：

- observed_at；
- path class；
- target path；
- curl exit code；
- HTTP code；
- remote IP；
- TLS verification result；
- latency；
- bytes；
- body SHA-256；
- stderr failure class。

## 4. Interpretation Rules（解释规则）

| Observation | Bounded interpretation |
|---|---|
| Default fails, direct passes | local proxy/TUN path implicated；不自动证明具体 proxy product defect |
| Default and direct both fail | server/network/TLS path remains open；需要服务器与外部 vantage diagnosis |
| Both pass all rounds | transient failure not reproduced；不能宣称根因关闭 |
| Hash differs on HTTP 200 | content-path inconsistency；停止，不重新部署 |
| TLS verification disabled or bypassed | invalid diagnostic；停止 |

`--resolve` 只固定目标 IP，不允许 `-k`、`--insecure` 或证书绕过。

## 5. Server-side Read-only Correlation（服务器只读关联）

诊断后只允许读取聚合计数：

- Nginx error lines；
- Nginx journal warning lines；
- access 5xx count。

不得把原始 IP、User-Agent、cookie、authorization header 或完整日志写入仓库。

## 6. Stop Rules（停止规则）

- 请求总数超过 12；
- 出现私密数据、凭据或个人标识；
- 需要改变系统 proxy、DNS、Nginx、证书或防火墙；
- 需要重新部署；
- 使用 retry、fallback、parallel request 或 TLS bypass；
- HTTP 200 响应 hash 在同一版本/路径间不一致；
- 当前线上 symlink 偏离已回滚目标。

## 7. Effects（效果）

```text
READ_ONLY_NETWORK_DIAGNOSIS_RECOMMENDED=true
REDEPLOYMENT_RECOMMENDED=false
ROOT_CAUSE_PROVEN=false

CONFIG_CHANGE=false
RUNTIME=false
API=false
AGENT=false
ENTITY=false
PERMISSION=false
CAPABILITY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFER=false
PRODUCTION_READY=false
```
