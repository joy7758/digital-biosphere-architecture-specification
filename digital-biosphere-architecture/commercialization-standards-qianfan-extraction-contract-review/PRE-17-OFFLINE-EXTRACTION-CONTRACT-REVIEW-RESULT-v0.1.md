---
document_id: DBA-TITMAS-CS-D02-PRE-17-OFFLINE-EXTRACTION-CONTRACT-REVIEW-RESULT-0.1
title: TITMAS CS-D02 PRE-17 Offline Extraction Contract Review Result v0.1
title_zh: TITMAS CS-D02 PRE-17 提取契约离线审查结果 v0.1
version: 0.1.0
status: offline-static-review-pass-provider-runtime-unvalidated
maturity: Development
decision_reference: CS-D02-PRE-17
offline_static_review_pass: true
provider_runtime_validation_pass: false
candidate_review_completed: false
valid_problem_records: 0
cs_g0_pass: false
---

# TITMAS CS-D02 PRE-17 Offline Extraction Contract Review Result v0.1

## Result

PRE-17 已在远端授权基线核验后完成零请求静态审查：

```text
LIVE_MODEL_REQUESTS_EXECUTED=0
PROVIDER_NETWORK_REQUESTS_EXECUTED=0
RAW_PRE16_PROVIDER_BODY_ACCESSED=false

TRANSPORT_AND_SEMANTIC_LAYERS_DISTINGUISHED=true
PLAIN_CONTENT_TEXT_ACCEPTANCE_RULE_NARROWED=true
BOUNDED_UNWRAP_PATHS_EXPLICIT=true
MAX_JSON_WRAPPER_UNWRAP_DEPTH=1
ARBITRARY_RECURSIVE_UNWRAP_ALLOWED=false
PRIVACY_PRESERVING_SHAPE_DESCRIPTOR_DEFINED=true

SYNTHETIC_CASES_MATCHED=13/13
OFFLINE_STATIC_REVIEW_PASS=true
PROVIDER_RUNTIME_VALIDATION_PASS=false
QIANFAN_PROVIDER_SCHEMA_CONFIRMATION_PASS=false
COMPOSITE_PROVIDER_GATE_PASS=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

## Main Finding

PRE-15 的最后一条路径“将任意 plain `content[0].text` 当作 answer”过宽。PRE-16 已证明：
该文本可以是可解析 JSON，但并非 reviewer response。v0.2 candidate 改为：

1. 先区分 transport envelope、tool result payload 与 reviewer semantic object；
2. 只允许五个显式 path；
3. wrapper 最多展开一层；
4. plain content text 只有在其直接 JSON 对象通过完整 frozen reviewer Schema 时才接受；
5. 非 reviewer JSON 且不含显式一层 wrapper path 时分类为
   `UNKNOWN_RUNTIME_ENVELOPE`；
6. 多个非相同合格值立即失败关闭。

该新分类不改写 PRE-16 历史结果。PRE-16 继续保持
`FULL_FROZEN_SCHEMA_VALIDATION_FAILED`；静态 crosswalk 只说明同一 sanitized observation
在 v0.2 contract 下应路由到 `UNKNOWN_RUNTIME_ENVELOPE`。

## Privacy-preserving Shape Descriptor

若未来另行授权 provider request，只允许记录：

- 预声明 path 是否存在；
- value type、byte length 和 SHA-256；
- direct JSON parse / parsed shape / full Schema 状态；
- distinct candidate count 和 ambiguity 状态。

禁止保存 raw wrapper、raw answer、raw content text、usage、hidden reasoning、secret 或
个人／客户数据。Descriptor 不是 provider evidence，也不证明 value 的含义。

## Synthetic Validation

13 个 case 覆盖：

- top-level structured/direct answer；
- content text 的 direct/structured wrapper；
- direct reviewer object；
- 非 reviewer JSON、非 JSON、missing 和 wrong type；
- 相同值去重、非相同值歧义失败；
- 二层未声明 nesting；
- reviewer Schema mismatch。

全部 case 与冻结预期一致。该 PASS 只验证离线 extraction candidate，不验证当前 Qianfan
runtime envelope 或模型响应。

## Next Permitted Action

```text
PREPARE_SEPARATE_PROVIDER_ADAPTER_CONFORMANCE_PROFILE_RECOMMENDATION_ONLY
```

商业化标准不应继续依赖 provider-specific wrapper 猜测。下一步应把稳定 semantic answer、
transport metadata、shape descriptor、failure classification 和 full Schema handoff 收敛为
provider-neutral Adapter Conformance Profile；当前不授权实现、再次请求或候选审查。

## References

- [transport / semantic crosswalk](transport-semantic-crosswalk.v0.1.json)
- [extraction contract candidate](extraction-contract-candidate.v0.2.json)
- [shape descriptor contract](shape-descriptor-contract.v0.1.json)
- [synthetic fixtures](synthetic-extraction-fixtures.v0.2.json)
- [offline validation result](offline-validation-result.v0.1.json)
- [execution receipt](execution-receipt.v0.1.json)
- [authorization receipt](authorization-baseline-receipt.v0.1.json)
