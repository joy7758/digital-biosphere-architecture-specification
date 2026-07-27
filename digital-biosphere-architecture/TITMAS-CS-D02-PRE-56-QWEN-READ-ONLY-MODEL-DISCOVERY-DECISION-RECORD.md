# PRE-56 Qwen Read-Only Model Discovery Decision Record

```text
DECISION_ID=CS-D02-PRE-56
STATUS=ONE_REQUEST_READ_ONLY_MODEL_DISCOVERY_AUTHORIZED_NOT_EXECUTED
DECISION_RESULT=AUTHORIZE_ONE_EXACT_READ_ONLY_QWEN_MODEL_DISCOVERY_REQUEST
DECIDED_BY_REF=zhangbin
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
PROVIDER_REQUESTS_MAX=1
MODEL_INFERENCE_REQUESTS_MAX=0
RETRY_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

## Decision

依据 canonical PRE-56 Recommendation、PRE-55 retained failure 和
`TITMAS-CS-STANDING-001`，授权对 Human Owner 指定 Base URL 的 exact `/models` URL
执行一次 authenticated read-only GET。

授权只覆盖 model identifier discovery 和 exact seven-file sanitized packet。不得执行
Chat Completions、自动选择模型或把 listing 提升为 entitlement、support 或 inference pass。

## Boundaries

- 一次请求，不重试、不 fallback、不换 endpoint；
- 不发送 request body 或模型 prompt；
- 只保留白名单字段、排序去重的 model ids 和 raw-response hash；
- credential value 不输出、不落盘、不进入 Git；
- 不修改 Provider configuration、DBOS、SAEE 或 `titmas-integrations`；
- 不授权 Provider integration、Security Review、implementation、release 或 commercial
  offer。

## Next Gate

创建并验证 exact seven-file PRE-56 packet。发现通过后只能形成 exact model candidate
selection Recommendation；新的 inference 需要新的独立 Decision。
