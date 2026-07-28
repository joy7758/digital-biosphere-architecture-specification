---
document_id: DBA-TITMAS-CE-G12-PUBLIC-ROUTE-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Public Route Validation Recommendation v0.1
title_zh: TITMAS CE-G12 公网路由验证建议 v0.1
version: 0.1.0
status: outside-in-public-route-validation-recommended-agent-review-required
maturity: Development
maturity_scope: active-static-site-outside-in-read-only-validation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Public Route Validation Recommendation v0.1

## 1. Recommendation

采用 **Option A：从本机经真实 DNS/TLS 对 active static site 执行一次 bounded outside-in
validation，核对页面、canonical redirect 和 agent-readable endpoints 的 exact body hash**。

```text
RECOMMENDED_OPTION=A
OUTSIDE_IN_VALIDATION_RECOMMENDED=true
OUTSIDE_IN_VALIDATION_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
CURRENT_SWITCH_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
```

本建议不发起 HTTP request、不建立 SSH、不写 server、不切换 current、不修改 DNS/证书/
Nginx、不发布。

## 2. Activation evidence

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-preserved-artifact-atomic-activation-result.v0.1.json` | `244c50e1f4f1e823d72f44f40b07a94855f35cca716253681d13f4e5ee6223de` |
| `TITMAS-CE-G12-PRESERVED-ARTIFACT-ATOMIC-ACTIVATION-REPORT-v0.1.md` | `5103e69e1b53c8f706aa58648f14f6fb94acd5a2297ff45d621b681966f59857` |

evidence commit：

```text
efca9cbcd9e708448215249796ba422ea5439b05
```

active identity：

```text
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
CURRENT=/srv/tmai/releases/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
LOCALHOST_ROUTE_CONTRACTS=10/10
```

## 3. Exact public validation matrix

真实 origin：

```text
https://redcrag.cn
```

最多 10 个 GET：

| Request | Contract |
|---|---|
| `/` | TLS verified, 200, body hash = candidate `index.html` |
| `/en` no-follow | 301, exact Location `/en/` |
| `/en` follow | final 200, body hash = `en/index.html` |
| `/status.json` | 200, exact body hash and valid JSON |
| `/agent-index.json` | 200, exact body hash and valid JSON |
| `/llms.txt` | 200, exact body hash, non-empty |
| `/robots.txt` | 200, exact body hash |
| `/titmas-community.json` | 200, exact body hash and valid JSON |
| `/agent-customer-package.json` | 200, exact body hash and valid JSON |
| `/release-manifest.json` | 200, exact body hash, source revision exact |

每个 request 使用正常 DNS 和系统 CA，不允许 `--resolve`、insecure TLS、proxy fallback 或
alternate domain。记录 resolved IP、TLS verify result、HTTP version、status、redirect/final
URL、bytes/hash。

## 4. Success conditions

```text
DNS_RESOLVED=true
REMOTE_IP_OBSERVED=true
TLS_VERIFY_RESULT=0
ROOT_BODY_HASH_EXACT=true
CANONICAL_REDIRECT_EXACT=true
EN_BODY_HASH_EXACT=true
AGENT_READABLE_ENDPOINTS_EXACT=7/7
JSON_ENDPOINTS_PARSE=true
PUBLIC_REQUESTS=10
SERVER_MUTATION=0
```

body hash 必须与本地 fixed candidate archive/extractor dry-run files 比较，而不是只检查
HTTP 200。

## 5. Options

### Option A — Ten exact outside-in requests（推荐）

验证真实 DNS/TLS/CDN-free public path 与 agent-readable discovery surface。

### Option B — Treat localhost validation as public reachability（拒绝）

localhost 不经过真实 DNS、外部网络与 public TLS path。

### Option C — Browser screenshot only（拒绝）

截图不能证明 body hash、JSON validity 或 agent-readable endpoint exactness。

### Option D — Declare Production after public pass（拒绝）

public reachability pass 仍不是 Production、new release 或 commercial offering。

## 6. Caps and stop conditions

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
PUBLIC_GET_REQUESTS_MAX=10
SSH_SESSIONS=0
SERVER_READ_COMMANDS=0
SERVER_WRITES=0
CURRENT_SWITCHES=0
DNS_CHANGES=0
CERTIFICATE_CHANGES=0
NGINX_CHANGES=0
RETRIES=0
PROXY_OR_NETWORK_FALLBACKS=0
NEW_PRODUCT_RELEASES=0
```

停止于 governance/candidate hash drift、exact model/review failure、DNS/TLS failure、unexpected
remote IP、redirect/status/body hash/JSON failure、需要 retry/proxy/alternate domain、任何 server
mutation 或 status elevation。

## 7. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
activation_evidence_sufficient
outside_in_scope_well_formed
public_route_matrix_sufficient
agent_readable_endpoint_matrix_sufficient
tls_dns_observation_contract_sufficient
body_hash_and_json_contract_sound
caps_and_stop_rules_sufficient
release_gate_separation_sound
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers 和
corrections、returned model exact `qwen3.7-max`。

## 8. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
PUBLIC_VALIDATION_NE_PRODUCTION=true
REACHABILITY_NE_NEW_PRODUCT_RELEASE=true
HTTP_SUCCESS_NE_AGENT_ADOPTION=true
PUBLIC_REQUESTS_EXECUTED=false
SSH_SESSION_CREATED=false
SERVER_WRITE_EXECUTED=false
CURRENT_CHANGED=false
PUBLIC_VALIDATION_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
