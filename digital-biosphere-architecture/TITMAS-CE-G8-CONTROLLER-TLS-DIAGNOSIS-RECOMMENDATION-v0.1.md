---
document_id: DBA-TITMAS-CE-G8-CONTROLLER-TLS-DIAGNOSIS-RECOMMENDATION-0.1
title: TITMAS CE-G8 Controller TLS Failure Diagnosis Recommendation v0.1
title_zh: TITMAS CE-G8 控制端 TLS 失败诊断建议 v0.1
version: 0.1.0
status: exact-bounded-recommendation-qwen-correction-incorporated
maturity: Development
maturity_scope: controller-transport-diagnosis-on-rollback-release
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G8 Controller TLS Failure Diagnosis Recommendation v0.1

## 1. Recommendation

建议只在当前 rollback release（回滚版本）上执行一次有界 controller TLS diagnosis
（控制端 TLS 诊断），区分：

- macOS system curl / SecureTransport；
- Python / OpenSSL；
- normal route；
- direct IPv4 + SNI route；
- server-side handshake/access signal。

该动作不部署、不重试 CE-G7、不修改策略、不证明根因。

## 2. Evidence baseline

```text
CE_G7_RESULT=FAIL_CLOSED_ROLLBACK_PASS
CURRENT_RELEASE=7da4bcf16eeec7de1c61031fe08fc04081cf8705
SERVER_LOCAL_ROUTES_PASS=11/11
CONTROLLER_PUBLIC_ROUTES_PASS=10/11
CONTROLLER_FAILURE_ROUTE=/en/
CONTROLLER_CURL_EXIT_CODE=35
RETRY_EXECUTED=false
```

CE-G3 与 CE-G4 也在同一本地路径观察过 `curl exit 35`；CE-G5 的 GitHub-hosted macOS
相同代 SecureTransport/LibreSSL 则通过 `12/12`。因此存在重复信号，但 exact root cause
仍为 `UNRESOLVED`。

## 3. Agent-customer recommendation

```text
provider=Alibaba Cloud Model Studio compatible endpoint
model=qwen3.7-plus
verdict=RECOMMENDED
would_recommend_to_agent_customer=true
confidence=0.92
```

唯一 blocking correction：

> server read-only log correlation 必须严格绑定四次 observation 的 exact start/end
> timestamps，不能扩大窗口或持久化窗口外 raw logs。

本建议已纳入。模型输出是 advisory input，不是 Authority、Decision 或 root-cause proof。

## 4. Exact request matrix

稳定 rollback release 的 `/en/`：

| ID | Client | Resolution | HTTP | Attempts |
|---|---|---|---|---:|
| A | macOS system curl / SecureTransport | normal route | default | 1 |
| B | macOS system curl / SecureTransport | `--resolve 180.76.115.193` | HTTP/1.1 | 1 |
| C | Python `http.client` / OpenSSL | normal DNS | HTTP/1.1 | 1 |
| D | Python socket + SSL / OpenSSL | direct `180.76.115.193` + SNI `redcrag.cn` | HTTP/1.1 | 1 |

总 public GET cap 为 4；sequential、retry=false、fallback=false、TLS bypass=false。

## 5. Offline controller facts

只保存：

- system proxy enable booleans 与 target class（loopback/non-loopback/none）；
- route interface class（physical/tunnel/loopback/other）；
- curl 与 Python TLS stack version；
- address-family counts/classes。

不保存：

- interface identifier；
- proxy address/port；
- credentials；
- full route/DNS/network configuration；
- raw request/response bodies；
- raw error text。

## 6. Exact server correlation

执行前允许一个只返回 exact current symlink 的 preflight SSH session。四次 observation
完成后，只允许另一个 SSH session 做 log correlation：

- `since` 精确等于 first observation start；
- `until` 精确等于 last observation end；
- 不加前后 padding；
- 只输出 access count、HTTP classes、SSL/handshake error count/classes；
- source IP 只输出 ephemeral salt 后的 SHA-256；
- 不输出或持久化 raw access/error/journal lines；
- 不修改 server。

## 7. Classification boundary

允许分类：

```text
CLIENT_STACK_OR_LOCAL_PATH_SIGNAL
ADDRESS_PATH_SIGNAL
SERVER_HANDSHAKE_SIGNAL
INCONCLUSIVE
NO_FAILURE_OBSERVED
```

所有分类都是 `SUPPORTED_NOT_PROVEN` 或 `OBSERVED_ONLY`。即使四次全部通过，也只能是
`NO_FAILURE_OBSERVED`，不能写为 root cause resolved。

## 8. Caps and false effects

```text
MODEL_REQUESTS_ALREADY_USED_FOR_RECOMMENDATION=1
NEW_PUBLIC_GETS_MAX=4
SSH_SESSIONS_MAX=2
RETRY=false
FALLBACK=false
TLS_BYPASS=false
WEBSITE_REDEPLOYMENT=false
SYMLINK_SWITCH=false
NGINX_RELOAD=false
SERVER_WRITE=false
RAW_LOG_PERSISTENCE=false

POLICY_CHANGE=false
CONTROLLER_GATE_CLASSIFICATION_CHANGE=false
RUNTIME=false
API=false
AGENT=false
ENTITY=false
PERMISSION=false
CAPABILITY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
PRODUCTION_READY=false
```

## 9. Stop rules

以下任一情况停止并保留 `INCONCLUSIVE`：

- current release 不等于 exact rollback target；
- offline privacy filter 无法执行；
- request matrix、attempt count、client/route binding 不精确；
- raw logs、raw error、proxy address 或 interface identifier 将被持久化；
- log window 超出 exact observation start/end；
- SSH session、public GET 或 model cap 超限；
- retry、fallback 或 TLS bypass 被启用。

## 10. Standing-directive eligibility

本建议固定 exact diagnostic、request matrix、time window、privacy rules、caps、classifications、
stop rules 和 false effects，满足 `TITMAS-CS-STANDING-001`。执行仍需独立 Decision。
