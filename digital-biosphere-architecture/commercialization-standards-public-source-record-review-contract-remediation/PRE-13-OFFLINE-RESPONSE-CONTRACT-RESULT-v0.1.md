# PRE-13 Offline Response Contract Result v0.1

## 1. Result

`CS-D02-PRE-13` 的零请求离线修订已通过：

```text
OFFLINE_RESPONSE_CONTRACT_REMEDIATION_PASS=true
FULL_RESPONSE_SCHEMA_EMBEDDED=true
SOURCE_PACK_EMBEDDED=true
ROLE_SOURCE_PACK_SCHEMA_BINDING_DETERMINISTIC=true
QIANFAN_SINGLE_FIELD_BINDING_DEFINED=true
DEEPSEEK_JSON_OBJECT_BINDING_DEFINED=true
COMPLIANT_SYNTHETIC_FIXTURE_ACCEPTED=true
NONCOMPLIANT_SYNTHETIC_FIXTURES_REJECTED=3/3
LIVE_MODEL_REQUESTS_EXECUTED=0
```

这证明新 request contract 在离线状态下是自包含、确定性且可验证的。它不证明任何
provider 已按该契约成功返回结果。

## 2. Contract Change

PRE-12 request 只要求匹配一个文件名所指向的 Schema。PRE-13 rendered contract 改为：

```text
Frozen review prompt
  + reviewer role placeholder
  + complete frozen source pack
  + normative full response Schema bytes
  + deterministic UTF-8/LF/SHA-256 binding
```

Canonical artifact：

- [rendered request contract](rendered-request-contract.v0.1.txt)
- [provider binding fixtures](provider-binding-fixtures.v0.1.json)
- [validator fixtures](response-contract-validator-fixtures.v0.1.json)
- [machine validation result](offline-validation-result.v0.1.json)

## 3. Provider Bindings

Qianfan binding：

```text
request_field=query
schema_binding=FULL_SCHEMA_EMBEDDED_IN_QUERY
live_request=false
```

DeepSeek binding：

```text
request_field=messages[0].content
response_format=json_object
schema_binding=FULL_SCHEMA_EMBEDDED_IN_MESSAGE_CONTENT
live_request=false
```

四个 reviewer role 均有独立的 rendered request SHA-256；两种 provider binding 复用相同
自包含内容，但没有执行网络请求。

## 4. Synthetic Validation

| Fixture | Expected | Observed | Result |
|---|---:|---:|---|
| `COMPLIANT_ACCEPTED` | valid | valid | `PASS` |
| `MISSING_BOUNDARY_FIELD_REJECTED` | invalid | invalid | `PASS` |
| `COUNTING_EFFECT_TRUE_REJECTED` | invalid | invalid | `PASS` |
| `UNKNOWN_EXTRA_FIELD_REJECTED` | invalid | invalid | `PASS` |

第一次本地 validator 命令因 Python 删除语法错误在验证前退出；没有修改结果或执行外部
动作。修正后完成一次离线验证，记录为：

```text
LOCAL_PRE_VALIDATION_FAILURES=1
OFFLINE_VALIDATION_RUNS_COMPLETED=1
```

## 5. Boundary

```text
PROVIDER_EXECUTION_VALIDATED=false
SYNTHETIC_FIXTURE_COUNTS_AS_PROVIDER_EVIDENCE=false
CANDIDATE_REVIEW_COMPLETED=false
RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

Schema conformance 仍不等于 Evidence Truth，offline fixture 仍不等于 provider evidence。

## 6. Next Route

PRE-13 授权已消耗。下一步只能另行准备：

```text
PREPARE_SEPARATE_BOUNDED_PROVIDER_CONFIRMATION_RECOMMENDATION_ONLY
```

如果未来建议 provider confirmation，必须重新冻结最小请求数、provider/model、完整
rendered bytes、阈值、失败关闭规则和远端授权基线。当前不授权任何 live request。
