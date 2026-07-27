---
document_id: DBA-TITMAS-CE-G6-IMMUTABLE-RELEASE-REVALIDATION-REPORT-0.1
title: TITMAS CE-G6 Immutable Release Revalidation Report v0.1
title_zh: TITMAS CE-G6 不可变发布版本重验证报告 v0.1
version: 0.1.0
status: pass-immutable-release-revalidation-only-not-deployment-authorized
maturity: Development
maturity_scope: proposed-static-release-read-only-revalidation
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G6
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G6 Immutable Release Revalidation Report v0.1

## 1. Outcome

```text
CE_G6_EXECUTED=true
CE_G6_RESULT=PASS_IMMUTABLE_RELEASE_REVALIDATION_ONLY
SERVER_SSH_SESSIONS=1
PUBLIC_HTTP_REQUESTS=0
MODEL_REQUESTS=0
ARCHIVE_EXTRACTION=false
SERVER_FILE_WRITE=false
SYMLINK_SWITCH=false
NGINX_RELOAD=false
DEPLOYMENT=false

REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT_AUTHORIZED=false
TLS_ROOT_CAUSE_PROVEN=false
DEPLOYMENT_SUCCESS_GUARANTEED=false
```

机器证据：

- [CE-G6 result](commercial-evaluation-immutable-release-revalidation/ce-g6-result.v0.1.json)；
- [Result Schema](commercial-evaluation-immutable-release-revalidation/ce-g6-result.schema.v0.1.json)；
- [Revalidation harness](commercial-evaluation-immutable-release-revalidation/ce_g6_release_revalidator.py)；
- [Decision](TITMAS-COMMERCIAL-EVALUATION-CE-G6-DECISION-RECORD.v0.1.json)。

## 2. Server artifact result

| Check | Result |
|---|---|
| Current symlink remains `7da4bcf...` | PASS |
| Proposed release `f810796...` exists | PASS |
| Archive bytes `962612` | PASS |
| Archive SHA-256 `fceb10...` | PASS |
| Archive path/member safety | PASS |
| Archive regular files | `61/61` |
| Manifest source revision | `f810796...` |
| Manifest declared files | `60` |
| Release bytes + SHA-256 | `60/60` |
| Release file set exact | PASS |
| Archive file set exact | PASS |

Archive 没有解压；harness 通过 `tarfile` stream read（流式读取）检查 member path、type、
bytes 和 digest。

## 3. Source and contract result

```text
SITE_SOURCE_DIFF_F810_TO_CE_G6_HEAD=0
AGENT_EVALUATION_ENTRY_SCHEMA_POSITIVE_PASS=true
NEGATIVE_BOUNDARY_CASES_REJECTED=5/5
ENTRY_SOURCE_TO_RELEASE_HASH_MATCH=true
ENTRY_SCHEMA_SOURCE_TO_RELEASE_HASH_MATCH=true
```

5 个负例：

- `evaluation_only=false`；
- `artifact.no_deps_allowed=true`；
- `effects.runtime=true`；
- artifact SHA-256 缺失；
- production recommendation。

全部被 Schema 拒绝。

## 4. Truth boundary

待发布文件继续声明：

```text
ENTRY_MATURITY=Development
ENTRY_STATUS=DEVELOPMENT_CONTRACT_SOURCE_PREPARED_NOT_DEPLOYED
EVALUATION_ONLY=true
PRODUCTION_RECOMMENDATION=DO_NOT_RECOMMEND_FOR_PRODUCTION
AVAILABLE_OFFERING=false
PRODUCTION_READY=false
CUSTOMER_ADOPTION_CLAIMED=false
CUSTOMERS_VERIFIED=0
CONTRACTS_CREATED=0
SLA_DEFINED=false
```

这证明 artifact 未发生 truth elevation，不证明运行行为或结果正确性。

## 5. Next gate

CE-G6 只解除 proposed immutable release integrity（拟发布不可变版本完整性）缺口。下一步
可准备：

```text
NEXT_ACTION=PREPARE_CE_G7_EXACT_REDEPLOYMENT_RECOMMENDATION
NEXT_ACTION_AUTHORIZED=false
```

CE-G7 必须独立定义：

- pre-switch current target；
- atomic symlink switch；
- `nginx -t` 与 reload；
- immediate route/header validation；
- two-vantage post-switch observation；
- 任何失败的 exact rollback；
- failure/archive/release preservation；
- no product/no SLA/no production effects。

## 6. Non-claims

```text
CE_G6_NE_DEPLOYMENT_AUTHORIZATION=true
CE_G6_NE_TLS_ROOT_CAUSE_PROOF=true
CE_G6_NE_DEPLOYMENT_SUCCESS_GUARANTEE=true
CE_G6_NE_PRODUCTION_READINESS=true
CE_G6_NE_SLA=true
CE_G6_NE_COMMERCIAL_OFFERING=true
CE_G6_NE_CERTIFICATION=true
```
