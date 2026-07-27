---
document_id: DBA-TITMAS-AGENT-EVALUATION-ENTRY-PUBLICATION-REPORT-0.1
title: TITMAS Agent Evaluation Entry Publication Report v0.1
title_zh: TITMAS 智能体评估入口发布报告 v0.1
version: 0.1.0
status: fail-closed-rollback-pass
maturity: Development
maturity_scope: exact-ce-g3-deployment-attempt
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G3
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS Agent Evaluation Entry Publication Report v0.1

## 1. Verdict（结论）

CE-G3 静态发布执行了部署，但在短窗口第二个可审计轮次出现 1 个 TLS/transport error。
系统按既定 stop rule 原子回滚，旧站点恢复。

```text
CE_G3_EXECUTION_RESULT=FAIL_CLOSED_ROLLBACK_PASS
NEW_CONTRACT_WEBSITE_DEPLOYED=false
TIME_WINDOW_OBSERVATION_COMPLETED=false
AVAILABILITY_SLA_DEFINED=false
```

机器回执：

- [receipt](commercial-evaluation-agent-entry-publication/ce-g3-publication-receipt.v0.1.json)
- [receipt Schema](commercial-evaluation-agent-entry-publication/ce-g3-publication-receipt.schema.v0.1.json)

## 2. Source and Artifact（源码与工件）

```text
SOURCE_REVISION=f8107969aa1f43be8ecf43f557297a630309fe41
REMOTE_REVISION_MATCH=true
SOURCE_WORKTREE_CLEAN=true
ARCHIVE_BYTES=962612
ARCHIVE_SHA256=fceb10bba908fee4c36bed5fcccc88c3f6ff44d1326c3e1565be17cd12ac167e
ARCHIVE_PATH_SAFETY_PASS=true
REMOTE_MANIFEST_FILES_VERIFIED=60
REMOTE_MANIFEST_PASS=true
REMOTE_TRUTH_BOUNDARY_PASS=true
```

正式导出本身通过。导出后附加检查曾错误假设 `release.json` 包含 `production_ready`，
导致一次本地检查失败；核对实际 truth surfaces 后确认：

- `status.json`：`production_ready=false`；
- Agent Index：`production_ready=false`；
- Agent Evaluation Entry：`effects.production_readiness=false`。

该 harness assumption failure（测试假设错误）不计为站点失败，但在报告中保留。

## 3. Deployment Attempt（部署尝试）

```text
PREVIOUS_RELEASE=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
ATTEMPTED_RELEASE=/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
ATOMIC_SWITCH_PASS=true
NGINX_TEST_PASS=true
NGINX_RELOAD_PASS=true
INITIAL_ROUTES=11/11_PASS
SECURITY_HEADERS=6/6_PASS
```

保留的 security headers：

- Strict-Transport-Security；
- Content-Security-Policy；
- X-Content-Type-Options；
- X-Frame-Options；
- Referrer-Policy；
- Permissions-Policy。

## 4. Availability Observation（可用性观察）

授权协议要求：

```text
ROUNDS_REQUIRED=3
MINIMUM_ELAPSED_SECONDS=120
TARGETS_PER_ROUND=11
RETRY_WITHIN_ROUND=false
```

实际：

```text
AUDITABLE_ROUNDS=2
ELAPSED_SECONDS=82
AUDITABLE_RECORDS=22
SUCCESSFUL_RECORDS=21
FAILED_RECORDS=1
MISSING_RECEIPT_ATTEMPTS=1
OBSERVATION_COMPLETED=false
```

第一轮 11/11 为 HTTP `200`。一个原计划的第二轮命令没有返回 stdout，因此没有计为
PASS；事后只读检查本地临时目录发现 10 个响应体和 1 个非空 error receipt：

```text
PATH=/llms.txt
ERROR=LibreSSL SSL_connect: SSL_ERROR_SYSCALL
CURL_EXIT_CODE=35
RETROACTIVELY_COUNTED_AS_ROUND=false
```

重新编号的第二个可审计轮次中：

```text
PATH=/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
RESULT=TRANSPORT_ERROR
CURL_EXIT_CODE=35
EXACT_ROOT_CAUSE_PROVEN=false
RETRY_EXECUTED=false
```

同轮其余 10 个路径为 HTTP `200`。错误可能是瞬时 TLS/transport failure，但没有直接
证据证明根因属于客户端、网络或服务器，因此保持 `UNKNOWN`。

CE-G4 准备阶段的只读诊断又确认：

```text
LOCAL_CURL_TLS_STACK=SecureTransport_LibreSSL_3_3_6
LOCAL_SYSTEM_HTTP_PROXY=LOOPBACK_ENABLED
LOCAL_SYSTEM_HTTPS_PROXY=LOOPBACK_ENABLED
LOCAL_DNS_RESULT=198.18.0.90_SYNTHETIC_RANGE
ACTUAL_SERVER=180.76.115.193
SERVER_NGINX_ERROR_LINES_WINDOW=0
SERVER_NGINX_JOURNAL_WARNING_LINES=0
SERVER_ACCESS_5XX_WINDOW=0
```

这些证据降低 asset-specific failure（资源内容特定故障）的可能性，并把本地 proxy/TUN
传输路径列为首要诊断候选；它们仍不足以证明最终根因。

## 5. Rollback（回滚）

```text
ROLLBACK_TRIGGERED=true
ROLLBACK_STATUS=PASS
CURRENT_AFTER=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
POST_ROLLBACK_NGINX_TEST=PASS
POST_ROLLBACK_NGINX_RELOAD=PASS
POST_ROLLBACK_ROOT_HTTP=200
FAILED_RELEASE_PRESERVED=true
UPLOADED_ARCHIVE_PRESERVED=true
```

没有修改 Nginx 配置、系统、SSH、证书、防火墙或安全配置；没有删除任何 release。

## 6. Boundary Result（边界结果）

```text
RUNTIME_CREATED=false
API_CREATED=false
AGENT_CREATED=false
ENTITY_CREATED=false
PERMISSION_CREATED=false
CAPABILITY_CREATED=false
CERTIFICATION_CREATED=false
SLA_CREATED=false
COMMERCIAL_OFFER_CREATED=false
PRODUCTION_READY=false
```

## 7. Next Gate（下一闸门）

下一步只能准备：

```text
PUBLIC_ENTRY_TRANSPORT_FAILURE_DIAGNOSIS_AND_REDEPLOYMENT_RECOMMENDATION
```

诊断必须区分：

- client/TLS path；
- network transport；
- Nginx/server；
- asset-specific behavior；
- observation harness。

新的网络观察或重新部署尚未授权。不得用一次后来成功的请求覆盖本次失败。
