---
document_id: DBA-TITMAS-CS-D02-PRE-56-QWEN-READ-ONLY-MODEL-DISCOVERY-RECOMMENDATION-0.1
version: 0.1.0
status: canonical-recommendation-ready-for-standing-directive-eligibility-review
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
provider_requests_max: 1
model_requests_max: 0
credential_identifiers_max: 1
implementation_authorized: false
---

# PRE-56 Qwen Read-Only Model Discovery Recommendation

## Recommendation

```text
RECOMMENDATION_ID=CS-D02-PRE-56
RECOMMENDED_ACTION=AUTHORIZE_ONE_EXACT_READ_ONLY_QWEN_MODEL_DISCOVERY_REQUEST
RECOMMENDATION=RECOMMENDED
HTTP_METHOD=GET
PATH=/models
PROVIDER_REQUESTS_MAX=1
MODEL_INFERENCE_REQUESTS_MAX=0
RETRY_MAX=0
FALLBACK_MAX=0
MODEL_SUBSTITUTION_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

PRE-55 已证明 `qwen3.7-plus-2026-05-26` 在 Human Owner 指定 endpoint 上返回
`model_not_found`。建议只对同一 Base URL 的 OpenAI-compatible `/models` surface 执行一次
只读发现，以确认当前 endpoint 暴露的 exact model identifiers。

该请求不执行推理、不选择模型、不重跑 PRE-55，也不证明每个 listed model 都有实际
entitlement、余额、稳定性或 inference success。

## Exact Request

```text
BASE_URL_SOURCE=HUMAN_OWNER_PROVIDED
METHOD=GET
URL=https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/models
AUTHORIZATION=Bearer ${DASHSCOPE_API_KEY}
TIMEOUT_SECONDS=30
```

Credential value 只能进入 Authorization header，不得输出、写入 packet 或提交 Git。

## Sanitization Contract

只允许从成功 response 中保留：

- HTTP status；
- outer object parse result；
- `data` 是否为 array；
- 排序、去重后的 string `id` 列表，最多 500 项；
- 总数、截断标志；
- raw response SHA-256；
- elapsed time；
- non-secret error code／error class。

不得保留 response 中的 credential、request headers、account、billing、quota、owner、
created timestamp 或其他 metadata。

## Pass Rule

```text
HTTP_2XX=true
OUTER_JSON_OBJECT=true
DATA_ARRAY=true
MODEL_ID_COUNT_MIN=1
SECRET_SCAN_PASS=true
```

不满足任一项即 `FAIL_CLOSED`。禁止 retry、fallback、第二 endpoint、HTML scraping、
model guessing 或手工补值。

## Exact Seven-File Packet

```text
commercialization-standards-qwen-model-discovery/
  PRE-56-QWEN-MODEL-DISCOVERY-RESULT-v0.1.md
  discovery-plan.v0.1.json
  discovery-plan.schema.v0.1.json
  sanitized-model-inventory.v0.1.json
  sanitized-model-inventory.schema.v0.1.json
  execution-receipt.v0.1.json
  execution-receipt.schema.v0.1.json
```

Separate Decision Markdown、JSON 和 Schema 可在 execution 前创建。

## Preconditions

- DBA remote HEAD 是 `f3d9aeacc5761c017ed8d0b27ae51bd529f3c2b8`；
- PRE-55 packet、cockpit sync 和 clean-clone verification 已通过；
- PRE-55 失败保持不可重试；
- local Git-excluded secret file 中 credential identifier 非空、Base URL 精确匹配；
- secret file mode 是 `600`；
- 没有更晚、更具体 Human Decision 冲突。

## Stop Conditions

- credential identifier 或 Base URL 缺失／变化；
- request 需要推理 body、第二个 endpoint 或模型 alias；
- HTTP／network／TLS／parse／shape／secret scan 失败；
- response 无 non-empty model id；
- 输出将包含 credential、account 或非白名单 metadata。

## Non-Effects

```text
MODEL_DISCOVERY_NE_MODEL_ENTITLEMENT=true
MODEL_LISTING_NE_INFERENCE_SUCCESS=true
MODEL_LISTING_NE_PROVIDER_SUPPORT=true
MODEL_LISTING_NE_SECURITY_REVIEW=true
PROVIDER_INTEGRATION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## Next Gate

若发现通过，只允许形成一个 exact model candidate selection Recommendation；任何新模型
推理都需要新的 Recommendation 和 Decision。
