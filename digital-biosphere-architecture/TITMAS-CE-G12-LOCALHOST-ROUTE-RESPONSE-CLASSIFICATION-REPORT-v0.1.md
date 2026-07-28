---
document_id: DBA-TITMAS-CE-G12-LOCALHOST-ROUTE-RESPONSE-CLASSIFICATION-REPORT-0.1
title: TITMAS CE-G12 Localhost Route Response Classification Report v0.1
title_zh: TITMAS CE-G12 本机路由响应分类报告 v0.1
version: 0.1.0
status: pass-canonical-directory-redirect-classified-no-redeployment-authorized
maturity: Development
maturity_scope: read-only-failed-deployment-route-contract-diagnostic-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-LOCALHOST-ROUTE-RESPONSE-CLASSIFICATION
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Localhost Route Response Classification Report v0.1

## 1. Outcome

```text
RESULT=PASS_LOCALHOST_ROUTE_RESPONSE_CLASSIFIED_NO_REDEPLOYMENT_AUTHORIZED
CLASSIFICATION=CANONICAL_DIRECTORY_REDIRECT
ROUTE_PAIRS_PASS=3/3
ROOT_ROUTE_PASS=true
LOCALHOST_REQUESTS=14
SERVER_WRITES=0
CURRENT_SWITCHES=0
REDEPLOYMENT_AUTHORIZED=false
```

机器结果：

- [Classification Result](commercial-evaluation-fresh-candidate/ce-g12-localhost-route-response-classification-result.v0.1.json)。

## 2. Root cause

上一次部署的 `/en` 178-byte mismatch 已经分类：

```text
PRIOR_FAILURE_CAUSE=VALIDATION_CONTRACT_DID_NOT_CAPTURE_OR_FOLLOW_CANONICAL_DIRECTORY_REDIRECT
CANDIDATE_CONTENT_FAILURE_PROVEN=false
NGINX_ROOT_FAILURE_PROVEN=false
```

不是直接证明“178 bytes 等于 redirect”，而是通过 fresh status、Location、followed body
和 canonical path 的完整 evidence chain 证明。

## 3. Observed route contract

| non-canonical | initial | Location | followed final | body hash | canonical direct |
|---|---:|---|---:|---|---:|
| `/en` | 301 | `https://redcrag.cn/en/` | 200 | expected file exact | `/en/` = 200 |
| `/status` | 301 | `https://redcrag.cn/status/` | 200 | expected file exact | `/status/` = 200 |
| `/en/status` | 301 | `https://redcrag.cn/en/status/` | 200 | expected file exact | `/en/status/` = 200 |

`/` 直接返回 200，body hash 与 current `index.html` 完全一致。

## 4. Nginx boundary

只读观察：

```text
CONFIG=/etc/nginx/conf.d/redcrag.cn.conf
CONFIG_SHA256=ddbd14b27abcce59330d86156fc0d42ea2ebaf933f3bc1447eba0fc9c13b29b5
STATIC_ROOT=/srv/tmai/current
INDEX=index.html
TRY_FILES_INCLUDES=$uri $uri/ $uri/index.html
CONFIG_CHANGED=false
CERTIFICATE_OR_PRIVATE_KEY_PATH_RECORDED=false
```

Nginx 对 directory path 的 canonical slash redirect 是当前有效契约，不是本轮新增或修改的
配置。

## 5. Correct future validation contract

future activation 必须同时验证：

```text
NON_CANONICAL_INITIAL_STATUS=301
NON_CANONICAL_LOCATION=exact trailing-slash URL
FOLLOWED_FINAL_STATUS=200
FOLLOWED_FINAL_BODY_HASH=expected static file hash
CANONICAL_DIRECT_STATUS=200
CANONICAL_DIRECT_BODY_HASH=expected static file hash
```

或者在只验证内容时直接请求 `/en/`、`/status/`、`/en/status/`。不得再把 no-follow 301 body
与 HTML file hash 直接比较。

## 6. State and boundaries

```text
CURRENT_TARGET=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
SERVER_STATE_CHANGED=false
ARTIFACT_REUSE_AUTHORIZED=false
CURRENT_SWITCH_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

## 7. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_PRESERVED_ARTIFACT_ATOMIC_ACTIVATION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
ARTIFACT_REUSE_AUTHORIZED=false
CURRENT_SWITCH_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
```

下一份 Recommendation 可评估：只读重验 preserved artifact/final tree 后，是否允许一次
CAS-guarded atomic activation，并使用本报告固定的 canonical route contract；不得重新传输或
解包，也不得把 activation 升级为新产品 release。
