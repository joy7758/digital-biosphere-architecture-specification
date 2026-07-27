# TITMAS CS-D02 PRE-74 Offline Schema Failure Diagnostic and Sanitized Failure Detail Capture Recommendation v0.1

## 1. Recommendation

```text
AGENT_RECOMMENDATION=RECOMMENDED
EXACT_RECOMMENDED_ACTION=AUTHORIZE_PRE74_OFFLINE_RESPONSE_CONTRACT_TRANSMISSION_GAP_DIAGNOSTIC_AND_SANITIZED_FAILURE_DETAIL_CAPTURE_DESIGN
PRE74_RECOMMENDATION_PREPARED=true
PRE74_DECIDED=false
PRE74_OFFLINE_EXECUTION_AUTHORIZED=false
PRE74_OFFLINE_EXECUTED=false
PRE74_LIVE_RETRY_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

建议执行一次零网络、零凭据、零 target/DBOS/SAEE write 的 PRE-74 离线诊断与
failure-detail capture contract 设计。本文件自身不授权 live retry，不改变 PRE-73
response Schema，也不采纳新的 request contract。

## 2. Agent recommendation gate

如果潜在 Agent 开发者问“是否推荐立即重跑 PRE-73”，当前答案应为：

> 不推荐直接重跑。PRE-73 两条响应都到达 HTTP 200、exact model 和 direct JSON，
> 但均在 Schema gate 失败；而 exact rejected path 未被脱敏保存。先修复 contract
> transmission 与 failure observability，才能避免再次消耗请求预算却得到同样的
> 不可诊断结果。

这个方向值得继续，因为问题集中在 review request/capture contract，而不是 target
实现或 Provider transport。

## 3. Direct offline diagnosis

对两条确定性 system + user message 逐字段复核后：

| response contract group | required | exact keys transmitted | missing |
|---|---:|---:|---|
| top level | 10 | 6 | `verdict`, `summary`, `question_assessments`, `cross_cutting_findings` |
| question assessment | 7 | 1 | `assessment`, `severity`, `finding`, `affected_symbols`, `proposed_tests`, `limitations` |
| explicit non-claims | 8 | 6 | `conformance_pass`, `release_authorized` |

此外：

```text
RESPONSE_SCHEMA_FILE_IN_REVIEW_INPUTS=false
RESPONSE_SCHEMA_SERIALIZED_IN_REQUEST=false
SCHEMA_STRUCTURE_MARKERS_PRESENT=0/3
CONTRACT_VERSION_NAME_MENTIONED=true
REQUEST_CONTRACT_TRANSMISSION_GAP_PROVEN=true
GAP_PROVEN_AS_EXACT_SCHEMA_FAILURE_CAUSE=false
MODEL_INTERNAL_CAUSALITY_PROVEN=false
```

也就是说，prompt 要求模型“符合 v0.2”，却没有把该 v0.2 的完整结构告诉模型。这个缺口
与 0/2 Schema failure 一致，但由于 raw response 和脱敏 failure path 都未保存，不能把它
升级为两次失败的精确因果结论。

## 4. Exact offline scope

PRE-74 只允许生成：

1. response-contract transmission map；
2. sanitized failure-detail capture contract；
3. 至少 12 个 synthetic validation-failure fixtures；
4. offline diagnostic result；
5. execution receipt。

禁止：

- network、live model 或 credential read；
-读取或恢复 PRE-73 raw response；
-修改 `titmas-integrations`、DBOS 或 SAEE；
-采纳 request revision 或修改 response Schema；
-再次调用 Qianfan/Qwen；
-产生 Security Review、Provider support、conformance、Standard Ready 或 release claim。

## 5. Sanitized failure detail boundary

未来失败记录只允许白名单字段：

```text
phase
error_class
instance_path
schema_path
validator
offending_value_type
offending_value_length
```

明确禁止：

```text
error_message
offending_value
assistant_content
provider_envelope
request_payload
source_package
credential_value
authorization_header
```

phase flag 必须在进入下一 gate 前先更新，避免再次出现 direct JSON 已通过却被记录为
false 的阶段性失真。

## 6. Success and stop gates

成功要求：

- 6/6 frozen input hashes；
- 3/3 transmission coverage groups；
- 至少 12 个 synthetic cases；
- valid sanitized failure detail 通过 Schema；
- forbidden-field、raw-value 和 authority mutation 全部失败关闭；
- network/model/credential/raw response/target/DBOS/SAEE actions 全为 0。

任一 raw message/value、secret、network、live retry 或 target write 尝试都必须立即停止。

## 7. Authority boundaries

```text
Contract transmission gap != exact Schema failure cause
Synthetic diagnostic != Provider runtime validation
Failure path capture != raw response persistence
Schema failure != Security Review finding
Offline pass != live retry authorization
Agent Review != formal Human Security Review
Evidence != Truth
```

## 8. Machine-readable references

- [PRE-74 scope](commercialization-standards-pre74-schema-failure-diagnostic/pre74-offline-diagnostic-scope.v0.1.json)
- [PRE-74 coverage observation](commercialization-standards-pre74-schema-failure-diagnostic/pre74-contract-transmission-coverage-observation.v0.1.json)
- [PRE-73 receipt](commercialization-standards-p0-exact-agent-security-review/pre73-execution-receipt.v0.1.json)
- [PRE-58 analogous transmission-gap result](commercialization-standards-qwen-response-contract-diagnostic/PRE-58-QWEN-RESPONSE-CONTRACT-OFFLINE-DIAGNOSTIC-RESULT-v0.1.md)
