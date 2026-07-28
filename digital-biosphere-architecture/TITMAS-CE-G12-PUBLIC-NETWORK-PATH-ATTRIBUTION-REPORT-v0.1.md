---
document_id: DBA-TITMAS-CE-G12-PUBLIC-NETWORK-PATH-ATTRIBUTION-REPORT-0.1
title: TITMAS CE-G12 Public Network Path Attribution Report v0.1
title_zh: TITMAS CE-G12 公网网络路径归因报告 v0.1
version: 0.1.0
status: local-synthetic-dns-mapping-observed-no-direct-origin-or-status-elevation
maturity: Development
maturity_scope: local-read-only-network-path-attribution
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Public Network Path Attribution Report v0.1

## 1. Outcome

```text
PATH_CLASSIFICATION=LOCAL_SYNTHETIC_DNS_MAPPING_OBSERVED
APPLICATION_SURFACE_EXACT=true
APPLICATION_REACHABLE_THROUGH_OBSERVED_SYSTEM_PATH=true
DIRECT_ORIGIN_IP_ATTRIBUTION_AVAILABLE=false
DIRECT_ORIGIN_PATH_PASS=false
PUBLIC_HTTP_MATRIX_RERUN=false
SERVER_STATE_CHANGED=false
NETWORK_STATE_CHANGED=false
PRODUCTION_READY=false
```

本机 system resolver 与独立 `dig A` 查询均把 `redcrag.cn` 解析为
`198.18.0.90`。该地址与上一轮十项公网请求中 `curl` 观察到的 remote IP 完全一致，
并属于 `198.18.0.0/15` 保留测试地址范围。因此，上一轮失败的 expected-origin-IP
闸门可归因为当前本机网络路径中的 synthetic DNS mapping（合成 DNS 映射）。

这不改变上一轮已经直接证明的内容事实：10/10 状态和重定向契约、9/9 body hash、5/5
JSON 以及 7/7 agent-readable endpoints 均精确通过。

## 2. Bound governance

| Item | Bound value |
|---|---|
| Decision | `TITMAS-COMMERCIAL-EVALUATION-CE-G12-PUBLIC-NETWORK-PATH-ATTRIBUTION-DECISION-RECORD.v0.1.json` |
| Decision SHA-256 | `3bac1d0a71a2bce189f35685230280ee587d38b8d6b3c159c5ed03a1c2900543` |
| Qwen Decision Review | `TITMAS-COMMERCIAL-EVALUATION-CE-G12-PUBLIC-NETWORK-PATH-ATTRIBUTION-QWEN-DECISION-REVIEW-v0.1.json` |
| Review SHA-256 | `7d4b1ae2c180cae41ee3e7c91be97fb8d85bd538de1f269721be0ba54dc3723c` |
| Governance commit | `9f68e85d309881f654092b0ee486679b1115d80b` |
| Local / remote head | exact match |
| Review result | exact `qwen3.7-max`, `APPROVE`, confidence `0.95`, zero blockers/corrections |

## 3. Read-only observations

### 3.1 Resolver

```text
FILTERED_RESOLVER_COUNT=10
FILTERED_NAMESERVER_COUNT=5
SYNTHETIC_NAMESERVER_COUNT=3
SYSTEM_RESOLVER_A=198.18.0.90
INDEPENDENT_DIG_A=198.18.0.90
DNS_LOOKUPS=2
```

### 3.2 Proxy

过滤后的 macOS proxy metadata 显示：

```text
HTTP_PROXY_CONFIG=127.0.0.1:1080 enabled
HTTPS_PROXY_CONFIG=127.0.0.1:1080 enabled
SOCKS_PROXY_CONFIG=disabled
PROXY_AUTO_CONFIG=disabled
PROXY_AUTO_DISCOVERY=disabled
PROXY_ENVIRONMENT_VARIABLES_PRESENT=0/8
```

没有记录 credential、PAC 内容或 proxy environment value。上述配置只证明存在本机
intermediation（中介）路径，不能证明具体代理、VPN、安全产品或上游运营方。

## 4. Classification proof

`LOCAL_SYNTHETIC_DNS_MAPPING_OBSERVED` 的三个必要条件全部成立：

1. system resolver 与 independent lookup 都返回 `198.18.0.90`；
2. `198.18.0.90` 属于 `198.18.0.0/15`；
3. 上一轮 `curl` remote IP 也为 `198.18.0.90`。

因此无需、也不得重跑十项 HTTP matrix。当前环境不能直接证明请求与
`180.76.115.193` 建立了端到端连接，所以严格 direct-origin path gate 保持 false。

## 5. Execution accounting

```text
ACTUAL_DIAGNOSTIC_EXECUTIONS=1
LOCAL_CONFIG_READS=4
DNS_LOOKUPS=2
HTTP_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
NETWORK_CONFIG_CHANGES=0
DNS_FLUSHES=0
PROXY_CHANGES=0
RETRIES=0
FALLBACKS=0
CREDENTIAL_VALUES_RECORDED=0
```

一次工具包装命令因模板插值在 shell 启动前被拒绝；它没有产生配置读取、DNS lookup
或其他网络活动，因此不计入实际诊断执行。

## 6. Commercialization boundary

本报告消除了“为什么 observed remote IP 不是预期源站 IP”的本地环境解释缺口，但不把
应用层内容验证升级为 direct-origin 验证，也不产生发布或商业状态：

```text
LOCAL_PATH_CLASSIFICATION_NE_DIRECT_ORIGIN_VALIDATION=true
SYNTHETIC_DNS_MAPPING_NE_SPECIFIC_PRODUCT_ATTRIBUTION=true
APPLICATION_VALIDATION_NE_PRODUCTION_READINESS=true
EVIDENCE_NE_TRUTH=true
NEW_PRODUCT_RELEASE=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
```

## 7. Result artifact

机器可读结果：

`commercial-evaluation-fresh-candidate/ce-g12-public-network-path-attribution-result.v0.1.json`
