---
document_id: DBA-TITMAS-CE-G12-PUBLIC-NETWORK-PATH-ATTRIBUTION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Public Network Path Attribution Recommendation v0.1
title_zh: TITMAS CE-G12 公网网络路径归因建议 v0.1
version: 0.1.0
status: local-network-path-attribution-recommended-agent-review-required
maturity: Development
maturity_scope: failed-expected-remote-ip-gate-local-diagnostic-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Public Network Path Attribution Recommendation v0.1

## 1. Recommendation

采用 **Option A：不重跑 HTTP matrix，只读取本机 resolver/proxy/curl 配置并执行最多两个
DNS lookup，分类 `198.18.0.90` 的本地路径来源**。

```text
RECOMMENDED_OPTION=A
HTTP_RETRY_RECOMMENDED=false
LOCAL_PATH_DIAGNOSTIC_RECOMMENDED=true
LOCAL_PATH_DIAGNOSTIC_AUTHORIZED=false
SERVER_MUTATION_AUTHORIZED=false
```

## 2. Fixed failure evidence

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-public-route-validation-result.v0.1.json` | `f20e12db44dd5206a2cc0bc798fe2f76ac8c7243acb5aa28e89b40366a0b62d4` |
| `TITMAS-CE-G12-PUBLIC-ROUTE-VALIDATION-REPORT-v0.1.md` | `65f529afce1d642dffffc89e91282ab0a0009538ce3eb558a4864603cf3b59a8` |

evidence commit `45e48cf42697d3509303d4c2f3a574842e21d785`。

```text
CONTENT_TLS_STATUS_HASH_CONTRACTS_PASS=10/10
EXPECTED_REMOTE_IP=180.76.115.193
OBSERVED_REMOTE_IP=198.18.0.90
STRICT_OUTSIDE_IN_PASS=false
```

## 3. Exact diagnostic

未来独立 Decision 最多允许：

1. 读取 `curl --version`；
2. 读取 `scutil --dns` 的 resolver nameserver/search/supplemental metadata，不记录私密内容；
3. 读取 `scutil --proxy`，只记录 enable flags、proxy type 和非 credential host/port；
4. 读取 proxy environment variable 的 present/absent，绝不记录 value；
5. 一次 system resolver lookup；
6. 一次 independent DNS A lookup；
7. 判断 answers 是否都为 `198.18.0.90` 且属于 `198.18.0.0/15`；
8. 生成 Result/Report。

不得执行 HTTP GET、`--resolve`、SSH、server read/write、network change、proxy disable、
DNS flush、retry 或 fallback。

## 4. Classification

`LOCAL_SYNTHETIC_DNS_MAPPING_OBSERVED`：

- system 与 independent lookup 都返回相同 RFC2544-range address；
- curl remote IP 与该 mapping 一致；
- 只证明本地 network path 使用 synthetic mapping，不归因到具体产品。

`CURL_PATH_INTERMEDIATION_OBSERVED`：

- DNS answer 与 curl remote IP 不同，且 proxy/config evidence 足以解释。

`UNKNOWN`：

- lookup/config evidence 不一致或不足。

无论分类如何：

```text
APPLICATION_SURFACE_EXACT=true
DIRECT_ORIGIN_PATH_PASS=false
PRODUCTION_READY=false
```

## 5. Caps

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
DNS_LOOKUPS_MAX=2
LOCAL_CONFIG_READS_MAX=4
HTTP_REQUESTS=0
SSH_SESSIONS=0
SERVER_WRITES=0
NETWORK_CONFIG_CHANGES=0
RETRIES=0
FALLBACKS=0
```

## 6. Review contract

exact `qwen3.7-max` 一次 direct JSON，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
failure_evidence_sufficient
no_http_retry_sound
local_diagnostic_scope_sufficient
credential_non_disclosure_sound
classification_rules_sound
application_vs_path_gate_separation_sound
caps_and_stop_rules_sufficient
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers/
corrections、exact `qwen3.7-max`。

## 7. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
PATH_ATTRIBUTION_NE_PUBLIC_REVALIDATION=true
SYNTHETIC_ADDRESS_NE_SPECIFIC_PROXY_ATTRIBUTION=true
HTTP_REQUESTS_EXECUTED=0
SERVER_STATE_CHANGED=false
STATUS_ELEVATION_AUTHORIZED=false
```
