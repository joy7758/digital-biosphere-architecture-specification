---
document_id: DBA-TITMAS-CS-D02-PRE-62-EXACT-LIVE-MULTI-PROVIDER-SECURITY-REVIEW-RECOMMENDATION-0.1
title: TITMAS Exact Live Multi-Provider Security Review Recommendation v0.1
title_zh: TITMAS 精确实时多提供商安全审查建议 v0.1
version: 0.1.0
status: exact-two-request-agent-review-recommended-not-decided
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
decision_candidate: CS-D02-PRE-62
standing_directive_reference: TITMAS-CS-STANDING-001
recommended_by: Codex
recommended_at: 2026-07-27T10:00:00+08:00
implementation_authorized: false
external_execution_authorized: false
formal_security_review_authorized: false
formal_security_review_completed: false
provider_integration_authorized: false
release_authorized: false
standard_ready: false
---

# TITMAS Exact Live Multi-Provider Security Review Recommendation v0.1

## Agent Recommendation

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=BOUNDED_AI_ASSISTED_INTEGRATION_AND_SECURITY_REVIEW_INPUT
NOT_RECOMMENDED_AS=FORMAL_HUMAN_SECURITY_REVIEW_OR_PROVIDER_APPROVAL
EXACT_OPTION=EXECUTE_TWO_SEQUENTIAL_PUBLIC_SAFE_AGENT_REVIEW_REQUESTS
```

如果潜在 Agent developer 需要判断 DeepSeek Provider binding candidate 的工程和安全缺口，
我会推荐执行两个相互分离、严格受限的 agent-review session：

1. Qianfan ERNIE：Integration Maintainer Candidate input；
2. Alibaba Qwen：Independent Security Reviewer Candidate input。

该建议只生成 AI-assisted review input（智能体辅助审查输入）。由于当前没有正式指派的
Human Security Reviewer，输出不能成为正式 Security Review、Provider support、
implementation approval、Certification、SLA 或 production safety 结论。

## Frozen Request Contract

- [request contract candidate](commercialization-standards-multi-provider-live-security-review/request-contract-candidate.v0.1.json)
  SHA-256:
  `9802e2e36d920c53e40f7926ab50420b18f684fe01f7335e8b003fbad14258cc`;
- [request contract Schema](commercialization-standards-multi-provider-live-security-review/request-contract-candidate.schema.v0.1.json)
  SHA-256:
  `68091db94bb127a3ae4f1e0b5109138510d96fd6fad4f3baf5b2d814bef5a03b`;
- Qianfan prompt SHA-256:
  `5c627334ece80374782f8ae3f6c6a71cbbc2e368cbf06f83b8a0bbd6601da482`;
- Qwen prompt SHA-256:
  `1608662d638409c1ce7a3d1ac8ac701482688ca4e55136b597fe8e9643e573d1`.

两个 prompt 都明确要求：

- exact direct JSON，禁止 Markdown；
- `verdict` 只能是 `READY_FOR_AUTHORIZATION`、`REVISE` 或 `BLOCKED`；
- `P0_DNS_OBSERVABILITY_UNRESOLVED=true`；
- Provider support、Security Review completion、Implementation Authorization 和 Authority
  claim 全部为 false；
- findings 和 controls 必须保留，不能静默省略。

## Preconditions

```text
PRE61_RESULT=PASS_20_OF_20_OFFLINE_PREFLIGHT_DESIGN
PRE61_RESULT_SHA256=458595dbe5fc87d80a8e8238cc5248a4a73d1842a00c8efd3159f54c971ecd3e
PRE61_RESULT_COMMIT=2313c05d976e1c11b33cf63c296bb8911befd7bc
PRE61_COCKPIT_COMMIT=230ff20f9276b11a7d779cd158a62d47666ba408
QIANFAN_DIRECT_TEST_RESULT=PASS_3_OF_3_BOUNDED
QWEN_DIRECT_TEST_RESULT=PASS_3_OF_3_V0_2
QIANFAN_API_KEY_IDENTIFIER_CONFIGURED_LOCAL=true
DASHSCOPE_API_KEY_IDENTIFIER_CONFIGURED_LOCAL=true
DASHSCOPE_BASE_URL_IDENTIFIER_CONFIGURED_LOCAL=true
CREDENTIAL_VALUE_RECORDED=false
```

只有 credential identifier 的存在性被核对；Key 值不进入推荐、计划、日志、结果或 Git。

## Exact Execution Scope

```text
PRIMARY_REPOSITORY=digital-biosphere-architecture
PROVIDER_REQUESTS_MAX=2
LIVE_MODEL_REQUESTS_MAX=2
CONCURRENCY_MAX=1
TIMEOUT_SECONDS_PER_REQUEST=60
RETRY_MAX=0
FALLBACK_MAX=0
MODEL_SUBSTITUTION_MAX=0
CONTENT_EXTRACTION_MAX=0
JSON_REPAIR_MAX=0
EXTERNAL_REPOSITORY_WRITES_MAX=0
IMPLEMENTATION_WRITES_MAX=0
```

执行顺序固定：

```text
PRE62-QF-INTEGRATION-01
  -> only if PASS
PRE62-QWEN-SECURITY-01
```

第一条请求如果发生 HTTP failure、empty content、non-direct JSON、Schema mismatch、
request/model/role mismatch 或 boundary mismatch，必须保留失败并停止，不能用第二
Provider 填补。

Raw response 只可在本地临时、`0600` 文件中保留；Git 只保存 sanitized response、hash、
bounded latency、token count、Provider error code 和失败状态。不得保存 credential、
Authorization header、prompt/response transport body 或 hidden reasoning。

## Output Contract

Decision 通过后，必须先远端冻结 execution plan，再执行请求，并生成恰好十个新增结果文件：

1. execution plan Schema；
2. execution plan；
3. response Schema；
4. sanitized result Schema；
5. sanitized result；
6. negative-case Schema；
7. negative cases；
8. result report；
9. receipt Schema；
10. receipt。

所有结果必须保留：

```text
AI_ASSISTED_REVIEW_INPUT_ONLY=true
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
PROVIDER_SUPPORTED=false
PROVIDER_INTEGRATED=false
IMPLEMENTATION_AUTHORIZED=false
STANDARD_READY=false
```

## Stop Conditions

- frozen contract、prompt hash、endpoint、model 或 credential identifier 不匹配；
- required local credential identifier 缺失；
- 需要重试、fallback、model substitution、content extraction 或 JSON repair；
- response 要求提升 Evidence、Evaluation、Recommendation 或 agent verdict 的 Authority；
- P0 DNS finding 被返回为已关闭；
- sanitized output 含 Key、Authorization header、本地密钥路径、raw body 或私密数据；
- 需要 DBOS、SAEE、`titmas-integrations`、Runtime 或 Provider adapter 写入。

## Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
PROVIDER_INTEGRATION_AUTHORIZED=false
FORMAL_SECURITY_REVIEW_AUTHORIZED=false
FORMAL_SECURITY_REVIEW_COMPLETED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

本建议满足 `TITMAS-CS-STANDING-001` 的 exact option、direct preconditions、bounded external
action、false effects 和 fail-closed stop rules。应用常设授权仍必须生成独立 Decision
Record；Recommendation 本身不授权请求。
