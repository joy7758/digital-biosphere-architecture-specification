---
document_id: DBA-TITMAS-CE-G5-INDEPENDENT-VANTAGE-VALIDATION-REPORT-0.1
title: TITMAS CE-G5 Independent Vantage Validation Report v0.1
title_zh: TITMAS CE-G5 独立视角验证报告 v0.1
version: 0.1.0
status: pass-transport-observation-redeployment-decision-required
maturity: Development
maturity_scope: public-entry-transport-observation
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G5
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G5 Independent Vantage Validation Report v0.1

## 1. Outcome

```text
CE_G5_EXECUTED=true
GITHUB_ACTIONS_RUN=30263067801
COUNTED_VANTAGES=2
INDEPENDENT_EXECUTION_ENVIRONMENTS=2
DISTINCT_NETWORK_EGRESS=2
DISTINCT_CLIENT_TLS_STACKS=2
PUBLIC_ORIGIN_REQUESTS=24
REQUESTS_PASS=24/24
CONTENT_HASH_MATCH=24/24
RETRY_USED=false
FALLBACK_USED=false
TLS_VERIFICATION_BYPASS_USED=false

TRANSPORT_OBSERVATION_PASS=true
REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT_AUTHORIZED=false
ROOT_CAUSE_PROVEN=false
```

CE-G5 证明两个独立临时 runner 在本次有界窗口内均能稳定读取当前公开版本，并得到与
固定部署文件一致的内容。它没有重新部署网站，也没有证明此前 TLS 故障的根因。

机器证据：

- [Composite result](commercial-evaluation-independent-vantage/ce-g5-composite-result.v0.1.json)；
- [Composite Schema](commercial-evaluation-independent-vantage/ce-g5-composite-result.schema.v0.1.json)；
- [Ubuntu receipt](commercial-evaluation-independent-vantage/ce-g5-GITHUB_HOSTED_UBUNTU.v0.1.json)；
- [macOS receipt](commercial-evaluation-independent-vantage/ce-g5-GITHUB_HOSTED_MACOS.v0.1.json)；
- [Receipt Schema](commercial-evaluation-independent-vantage/ce-g5-vantage-receipt.schema.v0.1.json)；
- [Fixed hash baseline](commercial-evaluation-independent-vantage/ce-g5-current-release-hash-baseline.v0.1.json)；
- [Exact run request](commercial-evaluation-independent-vantage/ce-g5-run-request.v0.1.json)。

GitHub Actions：

`https://github.com/joy7758/digital-biosphere-architecture-specification/actions/runs/30263067801`

## 2. Execution evidence

| Vantage | Environment | Client / TLS | Requests | Result |
|---|---|---|---:|---|
| `GITHUB_HOSTED_UBUNTU` | Linux x86_64 ephemeral runner | Python `http.client` / OpenSSL 3.0.13 | 12 | PASS |
| `GITHUB_HOSTED_MACOS` | Darwin arm64 ephemeral runner | system curl / SecureTransport + LibreSSL 3.3.6 | 12 | PASS |

每个 vantage：

- 3 rounds；
- 每轮 4 个固定路由；
- 顺序请求；
- 0 retry；
- 0 fallback；
- 0 TLS bypass；
- 12/12 HTTP 200；
- 12/12 body hash 与当前 immutable release 文件一致；
- proxy environment absent。

## 3. Network-egress correlation

源站按 exact run-scoped User-Agent 只读过滤 Nginx access log：

| Vantage | Matching records | Distinct source count | Persisted source evidence |
|---|---:|---:|---|
| Ubuntu | 12 | 1 | salted SHA-256 only |
| macOS | 12 | 1 | salted SHA-256 only |

两个 salted hashes 不同，因此在本次执行中证明了两个不同 network egress。Salt 原值、
原始 source IP 和原始 Nginx log 均未持久化。

该结论不等于 multi-cloud（多云）证明：两个 runner 都由 GitHub-hosted infrastructure
提供。

## 4. Preserved schema failure

第一次独立回执校验失败：

```text
INITIAL_SCHEMA_VALIDATION=FAIL
FAILURE=CURL_EXIT_CODE_PROPERTY_MISSING_FROM_SCHEMA
```

原因是 harness 正确输出了 `curl_exit_code`，但 v0.1 Schema 初稿未声明该属性。处置：

1. 不重跑 workflow；
2. 不修改两份原始回执；
3. 补充 Schema 的 `curl_exit_code` 定义；
4. 用修正后的 Schema 重新验证原始回执；
5. 2/2 Schema 与 semantic validation PASS。

这次修正是 data-contract defect remediation（数据契约缺陷修正），不是把失败结果改写为
成功。

## 5. Gate assessment

CE-G5 已通过：

- independent execution environment gate；
- distinct egress gate；
- distinct client/TLS stack gate；
- current-live content hash gate；
- no-retry/no-bypass gate。

但仍保持：

```text
PROPOSED_RELEASE_REVALIDATED_IN_CE_G5=false
REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT_AUTHORIZED=false
```

原因是 CE-G5 只验证当前回滚版本
`/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705`。准备重新发布的 immutable
release 和 archive 必须在未来 exact decision 中重新核对 manifest、source revision、
rollback target 与 post-switch failure handling。

## 6. Toolchain warning

GitHub 对固定的 `actions/checkout` 与 `actions/upload-artifact` 给出 Node.js 20
deprecation warning，并在平台侧强制用 Node.js 24 运行。这不是本次观察失败，但属于
workflow maintenance risk（工作流维护风险），后续只能在官方 Action 提供相应 runtime
版本后更新固定 SHA，不能为消除警告改用未固定 action。

## 7. Non-claims

本报告不证明：

- 全球可用性；
- uptime、SLO 或 SLA；
- production readiness；
- customer adoption；
- commercial offering；
- certification；
- Agent 业务逻辑、安全性或结果正确性；
- 早期 TLS 故障的精确根因。

```text
RUNTIME_CREATED=false
API_CREATED=false
AGENT_CREATED=false
ENTITY_CREATED=false
CAPABILITY_CREATED=false
PERMISSION_CREATED=false
WEBSITE_REDEPLOYED=false
DBOS_OR_SAEE_CHANGED=false
```
