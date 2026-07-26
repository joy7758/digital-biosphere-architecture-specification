---
document_id: DBA-TITMAS-CS-D02-PRE-15-OFFLINE-QIANFAN-WRAPPER-DIAGNOSTIC-RESULT-0.1
title: TITMAS CS-D02 PRE-15 Offline Qianfan Wrapper Diagnostic Result v0.1
title_zh: TITMAS CS-D02 PRE-15 Qianfan Wrapper 离线诊断结果 v0.1
version: 0.1.0
status: offline-diagnostic-pass-extraction-gap-confirmed-exact-pre14-cause-unknown
maturity: Development
decision_reference: CS-D02-PRE-15
offline_diagnostic_pass: true
provider_success_proven: false
valid_problem_records: 0
cs_g0_pass: false
---

# TITMAS CS-D02 PRE-15 Offline Qianfan Wrapper Diagnostic Result v0.1

## Result

PRE-15 已完成零请求离线诊断：

```text
LIVE_MODEL_REQUESTS_EXECUTED=0
PROVIDER_NETWORK_REQUESTS_EXECUTED=0
PRE14_RAW_PROVIDER_BODY_ACCESSED=false
SYNTHETIC_CASES_MATCHED=8/8
CALLER_EXTRACTION_COVERAGE_GAP_CONFIRMED=true
OFFLINE_DIAGNOSTIC_PASS=true
```

## Main Finding

当前 installed tool metadata 声明语义结果包含：

```text
answer: string
model: "kimi-k2.6"
provider: "baidu-qianfan"
untrusted_external_content: true
usage: object
```

PRE-14 caller 只检查了：

- `structuredContent.answer`；
- `content[0].text` 可解析为 JSON wrapper 后的 `answer`。

没有检查：

- direct `answer`；
- 对该 tool 明确限定的 plain `content[0].text` answer。

因此 PRE-14 的 `PROVIDER_RESPONSE_NOT_EXTRACTABLE` 可能包含 caller extraction gap，而不应
被升级为“provider/model 没有回答”。

## What Remains Unknown

```text
PRE14_EXACT_QIANFAN_FAILURE_CAUSE=UNKNOWN_RAW_ENVELOPE_NOT_PERSISTED
PRE14_PROVIDER_ANSWER_PROVEN=false
PRE14_PROVIDER_NO_ANSWER_PROVEN=false
```

PRE-14 raw envelope 按数据最小化规则没有保存。本离线诊断不能恢复它，也不能反向证明
实际使用了哪一种 wrapper shape。

## Future Extraction Contract Candidate

未来若获得单独请求授权，应按顺序检查：

1. `structuredContent.answer`；
2. direct `answer`；
3. `content[0].text` 解析为 wrapper 后的 `answer`；
4. 仅对该声明工具，将 plain `content[0].text` 作为 answer。

若多个路径提供不一致 answer，必须失败关闭。提取后仍必须 direct JSON parse，并使用冻结
response Schema 验证；不得 JSON repair。

## Synthetic Validation

以下八类 synthetic fixture 全部匹配预期：

- structured-content answer；
- direct answer；
- JSON-wrapped content text；
- plain content text；
- missing answer；
- non-string answer；
- invalid JSON answer；
- Schema-mismatch answer。

Synthetic PASS 只验证 extraction contract，不是 Qianfan provider evidence。

## Next Permitted Action

```text
PREPARE_SEPARATE_ONE_REQUEST_QIANFAN_CONFIRMATION_RECOMMENDATION_ONLY
```

如继续，必须建立新的 recommendation、Decision、冻结 request/extraction contract 和远端
授权基线。PRE-14 不能重开，DeepSeek 的既有合格结果也不能在没有明确组合规则的情况下
自动关闭 provider confirmation gate。

## Non-effects

```text
QIANFAN_PROVIDER_SCHEMA_CONFIRMATION_PASS=false
PROVIDER_SCHEMA_CONFIRMATION_PASS=false
CANDIDATE_REVIEW_COMPLETED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## References

- [declared tool contract](declared-tool-contract.v0.1.json)
- [synthetic fixtures](synthetic-wrapper-fixtures.v0.1.json)
- [machine result](offline-diagnostic-result.v0.1.json)
- [execution receipt](execution-receipt.v0.1.json)
