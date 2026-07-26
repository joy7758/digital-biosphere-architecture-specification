---
document_id: DBA-TITMAS-PROVIDER-ADAPTER-CONFORMANCE-PROFILE-0.1
title: TITMAS Provider Adapter Conformance Profile Candidate v0.1
title_zh: TITMAS Provider Adapter 符合性画像候选 v0.1
version: 0.1.0
status: profile-candidate-created-not-adopted
maturity: Development
decision_reference: CS-D02-PRE-18
primary_repository: digital-biosphere-architecture
provider_neutral: true
implementation_authorized: false
conformance_execution_authorized: false
profile_adopted: false
authority_effect: none
---

# TITMAS Provider Adapter Conformance Profile Candidate v0.1

中文：TITMAS Provider Adapter 符合性画像候选 v0.1。

## 1. Purpose and Status

本画像定义 Agent Review provider Adapter 的供应商中立契约边界，使 transport、
semantic extraction、direct JSON parse、full reviewer Schema validation 和后续治理判断
保持为五个不同状态。

```text
PROFILE_CANDIDATE_CREATED=true
PROFILE_ADOPTED=false
ADAPTER_IMPLEMENTED=false
CONFORMANCE_EXECUTED=false
PROVIDER_SUPPORTED=false
```

机器契约：

- [Profile JSON](provider-adapter-conformance-profile.v0.1.json)；
- [Profile Schema](schemas/provider-adapter-conformance-profile.schema.v0.1.json)；
- [Request Descriptor Schema](schemas/provider-adapter-request-descriptor.schema.v0.1.json)；
- [Result Descriptor Schema](schemas/provider-adapter-result-descriptor.schema.v0.1.json)；
- [Failure Taxonomy](provider-adapter-failure-taxonomy.v0.1.json)；
- [Conformance Case Catalog](provider-adapter-conformance-cases.v0.1.json)。

## 2. Normalized Boundary

```text
Frozen review request
  → provider-neutral Request Descriptor
  → exact provider transport boundary
  → privacy-preserving shape observation
  → declared extraction path
  → direct JSON parse
  → full frozen reviewer Schema validation
  → provider-neutral Result Descriptor
  → separate candidate/governance review
```

Request Descriptor 只记录 request identity、provider/model reference、prompt/Schema digest、
reviewer role、时间、policy 和数据分类。它不保存 secret，也不证明请求已经发出。

Result Descriptor 记录 transport、semantic answer、extraction path、shape、parse、Schema、
failure 和 request accounting。它不得保存 raw provider body、secret 或 usage payload。

## 3. Extraction Rules

1. 只接受 active contract 明确声明的 extraction path；
2. wrapper 最多解包一次；
3. arbitrary plain text、未知 JSON envelope 或深层搜索不能自动成为 semantic answer；
4. 两个 byte-identical candidate 可以确定性去重；
5. 两个 non-identical candidate 必须以
   `AMBIGUOUS_NON_IDENTICAL_ANSWERS` 失败关闭；
6. JSON 必须直接解析，禁止修复、code-fence stripping 或语义重写；
7. 只有完整冻结 reviewer Schema PASS 后，才允许引用 sanitized conformant response；
8. Schema PASS 仍不产生 candidate validity、record counting、`CS-G0` 或市场结论。

## 4. Failure Contract

最小 failure class：

```text
TRANSPORT_ERROR
PROVIDER_ERROR
NO_EXTRACTABLE_ANSWER
UNKNOWN_RUNTIME_ENVELOPE
UNDECLARED_NESTING
AMBIGUOUS_NON_IDENTICAL_ANSWERS
DIRECT_JSON_PARSE_FAILED
FULL_SCHEMA_VALIDATION_FAILED
POLICY_VIOLATION
```

失败、unknown、ambiguous 和 policy violation 必须保留。不得用自动 retry、provider
fallback、JSON repair 或 later success 静默覆盖。

## 5. Conformance Case Boundary

[Case catalog](provider-adapter-conformance-cases.v0.1.json) 定义 20 个 provider-neutral
case，覆盖 direct object、declared semantic text、single wrapper、unknown envelope、
missing/wrong type、parse/Schema failure、deduplication、ambiguity、nesting、transport/provider
error、retry/fallback/repair、raw/secret/usage persistence 和 semantic non-elevation。

所有 case 当前均为：

```text
status=NOT_EXECUTED
execution_authorized=false
```

Catalog 的存在不是 Adapter conformance evidence。

## 6. Reference Provider Boundary

Qianfan/Kimi 与 DeepSeek 只作为历史、经过清理的 evidence reference，帮助识别
transport/semantic wrapper gap 和 direct-schema example。两者均保持：

```text
REFERENCE_STATE=REFERENCE_ONLY_NOT_ADOPTED
SUPPORTED=false
ADOPTED=false
CERTIFIED=false
```

Profile 不含任何 provider-specific normative required field。未来每个 provider/model 组合
需要 exact implementation、exact profile version、完整 case execution、独立 receipt 和单独
Human Adoption Decision。

## 7. Claim Non-elevation

| Observation | Allowed meaning | Must not become |
|---|---|---|
| Request descriptor Schema valid | 元数据结构符合 | request sent、authorization、provider support |
| Transport succeeded | transport 边界返回成功 | semantic answer、Schema PASS、candidate validity |
| Full reviewer Schema PASS | sanitized reviewer object 结构符合 | valid problem record、counting、`CS-G0`、market proof |
| Offline Profile Schema rehearsal PASS | 本地候选文件和 fixture 结构一致 | Adapter implementation、conformance、adoption、certification |

## 8. Future Conformance Entry

未来真正执行符合性测试前至少需要：

- exact Adapter implementation reference；
- exact Profile version；
- exact provider/model reference；
- 全部 required cases 的执行授权；
- failure、unknown 和 partial result retention；
- independent execution receipt；
- Profile adoption 的独立 Human Decision。

PRE-18 不满足也不关闭这些后继 Gate。

## 9. Non-effects

```text
ADAPTER_IMPLEMENTATION_AUTHORIZED=false
CONFORMANCE_EXECUTION_AUTHORIZED=false
CONFORMANCE_CASES_EXECUTED=0
PROFILE_ADOPTED=false
PROVIDER_ADOPTION=false
CANDIDATE_REVIEW_COMPLETED=false
RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
