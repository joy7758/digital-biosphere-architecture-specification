# PRE-55 Qwen Onboarding Benchmark Decision Record

```text
DECISION_ID=CS-D02-PRE-55
STATUS=QWEN_ONBOARDING_BENCHMARK_AUTHORIZED_NOT_EXECUTED
DECISION_RESULT=AUTHORIZE_QWEN_ONBOARDING_BENCHMARK_EXACT_THREE_PUBLIC_SAFE_REQUESTS
DECIDED_BY_REF=zhangbin
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
PROVIDER_REQUESTS_MAX=3
MODEL_REQUESTS_MAX=3
CONCURRENCY_MAX=1
RETRY_MAX=0
FALLBACK_MAX=0
MODEL_SUBSTITUTION_MAX=0
JSON_REPAIR_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

## Decision

依据 canonical PRE-55 Recommendation、Human Owner 明确提供的本地 credential 和 endpoint
配置，以及 `TITMAS-CS-STANDING-001`，授权对 exact Qwen route 执行最多三次
public-safe、顺序、fail-closed onboarding benchmark。

授权只覆盖 Recommendation 冻结的 exact endpoint、exact model、三阶段执行条件、JSON
contract、sanitized packet 和验证。不得读取或记录 credential value 之外的 secret state。

## Boundaries

- `QWEN-ONBOARD-01` 失败则 `02/03` 不执行；
- `QWEN-ONBOARD-02` 失败则 `03` 不执行；
- 失败请求消耗预算且原样保留；
- 禁止 retry、fallback、模型替换、alias inference、内容提取和 JSON repair；
- 不发送私有代码、客户材料、PII 或未公开证据；
- raw response 只在临时执行上下文中用于解析和 SHA-256，不进入 Git；
- 不修改 `titmas-integrations`、DBOS、SAEE 或 Provider configuration；
- 不授权 Provider integration、Security Review、implementation、release、commercial offer
  或 certification。

## Next Gate

创建并验证 exact nine-file PRE-55 packet。只有 `PASS_3_OF_3` 才允许形成独立
multi-Provider review preflight Recommendation；它仍不等于 Provider support 或 Security
Review complete。
