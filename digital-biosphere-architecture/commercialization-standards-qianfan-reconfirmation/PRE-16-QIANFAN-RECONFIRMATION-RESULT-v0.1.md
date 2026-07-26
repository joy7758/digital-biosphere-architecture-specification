---
document_id: DBA-TITMAS-CS-D02-PRE-16-QIANFAN-RECONFIRMATION-RESULT-0.1
title: TITMAS CS-D02 PRE-16 Qianfan Reconfirmation Result v0.1
title_zh: TITMAS CS-D02 PRE-16 千帆复确认结果 v0.1
version: 0.1.0
status: executed-fail-closed-qianfan-schema-reconfirmation-failed
maturity: Development
decision_reference: CS-D02-PRE-16
composite_provider_gate_pass: false
candidate_review_completed: false
valid_problem_records: 0
cs_g0_pass: false
---

# TITMAS CS-D02 PRE-16 Qianfan Reconfirmation Result v0.1

## Result

PRE-16 已在远端授权基线核验后严格执行唯一一次千帆/Kimi 请求，并失败关闭：

```text
NEW_LIVE_MODEL_REQUESTS_AUTHORIZED_MAX=1
NEW_LIVE_MODEL_REQUESTS_EXECUTED=1
QIANFAN_REQUESTS_EXECUTED=1
DEEPSEEK_NEW_REQUESTS_EXECUTED=0
REQUESTS_REMAINING=0

RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
JSON_REPAIR_ATTEMPTS=0
FENCE_STRIPPING_ATTEMPTS=0
SUBSTRING_EXTRACTION_ATTEMPTS=0

QIANFAN_DIRECT_JSON_PARSE_PASS=true
QIANFAN_FULL_FROZEN_SCHEMA_PASS=false
QIANFAN_CANDIDATE_IDS_COVERED=0
QIANFAN_BOUNDARY_EVALUATION_COMPLETE=false

FROZEN_DEEPSEEK_FULL_SCHEMA_PASS=true
DEEPSEEK_CANDIDATE_IDS_COVERED=4
FROZEN_INPUT_DIGESTS_MATCH=true

COMPOSITE_PROVIDER_GATE_PASS=false
CANDIDATE_REVIEW_COMPLETED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

## Qianfan Session Outcome

| Session | Outcome | Counting effect |
|---|---|---|
| `QF-KIMI-SCHEMA-RECONFIRM-PRE16-P1` | 冻结 request hash 匹配；命中 tool-specific `content[0].text`；该字符串可直接解析为 JSON，但根对象不符合完整 frozen response Schema | none |

该事实只证明：按 PRE-16 冻结 extraction contract 得到的 JSON 对象未通过规范响应
Schema。由于 raw provider body、非符合响应和 wrapper 未被保存，不能进一步声称：

- provider 已经或没有生成 reviewer answer；
- 模型能力失败；
- exact raw wrapper shape 已被识别；
- 候选记录已经被复核。

## Composite Gate

PRE-16 组合闸门要求新的 Qianfan response 与冻结的 PRE-14 DeepSeek response 分别通过
完整 Schema，并分别覆盖 4 个 candidate，且两者的边界评价均完成。实际结果为：

```text
QIANFAN_SCHEMA_CONFORMANT=false
FROZEN_DEEPSEEK_SCHEMA_CONFORMANT=true
PROVIDERS_WITH_SCHEMA_CONFORMANT_RESPONSE=1
QIANFAN_CANDIDATE_COVERAGE_MET=false
DEEPSEEK_CANDIDATE_COVERAGE_MET=true
BOUNDARY_EVALUATION_COMPLETE=false
ALL_CONDITIONS_MET=false
FAIL_CLOSED=true
```

冻结的 DeepSeek 合格响应不能替代第二个 provider，也不能补足 Qianfan 的 candidate
coverage 或 boundary evaluation。

## Data and Authority Boundaries

- 未保存 raw provider body、token usage、隐藏推理或非符合响应；
- 未显示或持久化 API key；
- 未发送客户数据、个人数据、私有源码或直接个人标识符；
- Schema conformance 不等于 candidate validity、Evidence Truth、Market Validation、
  Customer Adoption 或 CS-G0；
- 没有改变 DBOS、SAEE、Agent、Runtime、Authority、Permission、Offering、
  Certification 或 Release 状态。

## Next Permitted Action

```text
PREPARE_SEPARATE_ZERO_LIVE_REQUEST_QIANFAN_EXTRACTION_CONTRACT_REVIEW_RECOMMENDATION_ONLY
```

PRE-16 的唯一请求额度已经用尽。后续只能先形成独立、零 live request 的 recommendation
和 Decision，对 installed tool 的声明输出契约与 caller extraction contract 进行静态审查；
不得直接重试或把失败归因于模型。

## References

- [sanitized Qianfan observation](sanitized-qianfan-observation.v0.1.json)
- [composite gate result](composite-gate-result.v0.1.json)
- [execution receipt](execution-receipt.v0.1.json)
- [authorization receipt](authorization-baseline-receipt.v0.1.json)
