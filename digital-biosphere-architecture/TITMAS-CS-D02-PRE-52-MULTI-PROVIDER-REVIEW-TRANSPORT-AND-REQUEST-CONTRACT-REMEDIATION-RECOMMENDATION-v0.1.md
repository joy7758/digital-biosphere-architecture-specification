---
document_id: DBA-TITMAS-CS-D02-PRE-52-MULTI-PROVIDER-REVIEW-REMEDIATION-RECOMMENDATION-0.1
version: 0.1.0
status: canonical-recommendation-ready-for-standing-directive-eligibility-review
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
network_requests_max: 0
credential_reads_max: 0
model_requests_max: 0
implementation_authorized: false
---

# PRE-52 Multi-Provider Review Transport and Request Contract Remediation Recommendation

## Recommendation

```text
RECOMMENDATION_ID=CS-D02-PRE-52
RECOMMENDED_ACTION=AUTHORIZE_DBA_ONLY_OFFLINE_MULTI_PROVIDER_REVIEW_FAILURE_DIAGNOSIS_AND_PREALLOCATED_SESSION_CONTRACT_PACKET
RECOMMENDATION=RECOMMENDED
NETWORK_REQUESTS=0
MODEL_REQUESTS=0
CREDENTIAL_READS=0
TARGET_WRITES=0
IMPLEMENTATION_AUTHORIZED=false
```

建议仅在 DBA 对 PRE-51 保留结果与既有多 Provider 历史证据做离线交叉分析，形成新的
preallocated-session contract（预分配会话契约）。不重跑 PRE-51，不调用模型，不读取
`.env`，不把历史成功当成当前 Provider 可用性。

## Direct Findings To Preserve

1. PRE-51 exact Qianfan `kimi-k2.6`：1/4 直接 JSON 成功，3/4 timeout/network error；
2. 较早 v0.4 review：Qianfan Kimi HTTP 200 但 content 为空；Qianfan ERNIE、Ark Doubao、
   Ark GLM 和 direct DeepSeek 当次直接 JSON 成功；
3. PRE-29 只证明当次 Qianfan DNS/TCP/TLS 可达，未证明 model/request path；
4. 因此 `KIMI_QIANFAN_CURRENT_ROUTE=INTERMITTENT_NOT_SELECTED_FOR_NEXT_LIVE_REVIEW`；
5. 不能从相同 host 的 lower-layer PASS 推断 inference success；
6. 不能把 Ark／DeepSeek 历史成功升级为当前 account entitlement、model availability
   或 future request success。

## Candidate Allocation Contract

未来独立 Decision 才能选择的候选会话：

| 固定角色 | Provider candidate | Model candidate | 当前状态 |
|---|---|---|---|
| Agent Developer | DeepSeek direct | `deepseek-v4-pro` | `OFFICIAL_AND_HISTORICAL_REFERENCE_ONLY` |
| Machine Customer | Qianfan direct/tool | exact model pending | `MODEL_BINDING_UNRESOLVED` |
| Integration Maintainer | Ark | `doubao-seed-2-0-lite-260215` | `OFFICIAL_AND_HISTORICAL_REFERENCE_ONLY` |
| Security Reviewer | Ark or DeepSeek | separately fixed | `NOT_SELECTED` |

每个角色必须在 Decision 前绑定唯一 Provider、endpoint、model、credential identifier 和
request hash。Provider failure 只产生该 session failure，不得由其他 Provider 补位。

## Required Remediation Rules

- `allocation != fallback`；
- no retry、fallback、model substitution、alias inference or JSON repair；
- direct JSON only；
- one public-safe prompt per session；
- raw Provider envelope、credential、Authorization、prompt history 和 hidden reasoning 不落盘；
- Qianfan credential 继续由 installed tool 管理，除非新的 direct-client Decision 明确
  credential identifier 和 secret-safe destination；
- Ark 只允许官方 `https://ark.cn-beijing.volces.com/api/v3/chat/completions` candidate；
- DeepSeek 只允许官方 `https://api.deepseek.com/chat/completions` candidate；
- model ID 必须在执行 gate 重新核验，历史 ID 不自动沿用；
- P0 Provider-binding gap 继续为 false，不属于本次 review transport remediation 的关闭范围。

## Exact Outputs

```text
commercialization-standards-titmas-integrations-rb1-multi-provider-review-remediation/
  PRE-52-MULTI-PROVIDER-REVIEW-REMEDIATION-RESULT-v0.1.md
  failure-evidence-matrix.v0.1.json
  failure-evidence-matrix.schema.v0.1.json
  preallocated-session-contract.v0.1.json
  preallocated-session-contract.schema.v0.1.json
  remediation-negative-cases.v0.1.json
  remediation-negative-cases.schema.v0.1.json
  execution-receipt.v0.1.json
  execution-receipt.schema.v0.1.json
```

Separate Decision Markdown, JSON and Schema may be created before execution.

## Preconditions

- DBA remote remains `86658d4ccd282bcf347a5bb70a968cd3154619cc`；
- PRE-51 result remains fail closed；
- target remains `5ac891c5af88b1e9aeacdb3666217c6f832a57a6`；
- exact historical observations remain reference-only；
- official references are observed on `2026-07-27`；
- no later specific Human Decision conflicts。

## Stop Conditions

Stop if any output:

- retries or replaces PRE-51；
- claims a proven root cause from timeout metadata；
- claims Provider/model/account availability from documentation or history；
- reads a credential or emits a request；
- authorizes direct clients, implementation, Provider binding or security approval；
- converts a candidate allocation into fallback；
- changes P0 to PASS；
- omits failures, unknowns or semantic non-effects。

## Next Gate

Successful PRE-52 may only enable an exact multi-provider preflight/review Recommendation. That
future Recommendation must separately bind each session and must not reopen PRE-51.

## Official References

- Qianfan text generation:
  `https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb`；
- Qianfan model/API reference:
  `https://cloud.baidu.com/doc/qianfan/s/Smoghsq3g`；
- Ark ChatCompletions:
  `https://api.volcengine.com/api-docs/view?action=ChatCompletions&serviceCode=ark&version=2024-01-01`；
- DeepSeek Chat Completions:
  `https://api-docs.deepseek.com/api/create-chat-completion`。

References are planning inputs, not adoption or current account/model proof.
