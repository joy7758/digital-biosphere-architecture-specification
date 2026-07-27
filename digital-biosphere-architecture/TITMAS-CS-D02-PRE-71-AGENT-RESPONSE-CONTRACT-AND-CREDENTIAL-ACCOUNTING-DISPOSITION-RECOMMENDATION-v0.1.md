---
document_id: DBA-TITMAS-CS-D02-PRE-71-AGENT-RESPONSE-CONTRACT-AND-CREDENTIAL-ACCOUNTING-DISPOSITION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-71 Agent Response Contract and Credential Accounting Disposition Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-71 智能体响应契约与凭据计数处置建议 v0.1
version: 0.1.0
status: recommendation-only-decision-required
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_owner_ref: zhangbin
decision_candidate: CS-D02-PRE-71
implementation_authorized: false
live_model_request_authorized: false
release_authorized: false
standard_ready: false
---

# TITMAS CS-D02 PRE-71 Agent Response Contract and Credential Accounting Disposition Recommendation v0.1

## 1. Recommendation

推荐唯一有界动作：

```text
AUTHORIZE_OFFLINE_ONLY_PRE71_STRICT_RESPONSE_CONTRACT_AND_CREDENTIAL_ACCOUNTING_DESIGN
```

该动作只允许在 DBA 内形成：

1. strict direct-JSON response contract v0.2 candidate；
2. provider-native structured-output capability evidence checklist；
3. credential-use accounting profile；
4. offline fixtures、Schema、validator result 和 execution receipt。

它不授权 live model request、response extraction、JSON repair、Provider
substitution、target implementation、formal Human Security Review、Standard
adoption、merge、release 或 deployment。

机器范围：

- [scope](commercialization-standards-p0-security-and-platform-response-contract-remediation/pre71-response-contract-and-credential-accounting-scope.v0.1.json)；
- [scope Schema](commercialization-standards-p0-security-and-platform-response-contract-remediation/pre71-response-contract-and-credential-accounting-scope.schema.v0.1.json)。

## 2. Direct Evidence

PRE-70 已直接观察：

- explicit `DOCKER_HOST` 和 global-config metadata guard 通过；
- 两个 pinned Linux/amd64 lane 均完成 92 tests run、1 skip、suite `OK`
  与 7/7 rehearsal；
- Qianfan response outer envelope 可解析且有 assistant content；
- assistant content 含 Markdown code fence，不满足 direct JSON；
- frozen contract 禁止 extraction、repair 和 retry，因此 Qwen 未执行；
- raw envelope、assistant content、credential value 和 authorization header 均未持久化。

直接证据：

- [PRE-70 result](commercialization-standards-p0-security-and-platform-context-remediation/PRE-70-EXPLICIT-DOCKER-HOST-AND-PLATFORM-VALIDATION-RESULT-v0.1.md)；
- [PRE-70 receipt](commercialization-standards-p0-security-and-platform-context-remediation/pre70-execution-receipt.v0.1.json)。

## 3. Options Considered

### Option A — quietly strip Markdown fences

不推荐。该方案会把明确失败转换成隐式 parser policy，并扩大 ambiguous
envelope、prompt injection 和 partial extraction 的攻击面。

### Option B — weaken the contract to “extractable JSON”

不推荐作为当前默认。若未来确有必要，必须形成独立 extraction grammar、
single-object proof、size/depth limits、adversarial fixtures 和新的 Decision。

### Option C — preserve strict direct JSON and require proven structured output

推荐。保持：

```text
MODEL_OUTPUT_MUST_BE_ONE_DIRECT_JSON_OBJECT
CODE_FENCE_ALLOWED=false
PREFIX_OR_SUFFIX_ALLOWED=false
EXTRACTION_ALLOWED=false
REPAIR_ALLOWED=false
```

Provider lane 在执行前必须提供当前官方能力证据或有界 preflight 证据，证明所请求
model/endpoint/request shape 能被配置为 strict JSON output。没有证据就保持
`PROVIDER_RESPONSE_CONTRACT_UNPROVEN`，不能用 prompt 文本代替能力证明。

## 4. Credential Accounting Correction

PRE-70 frozen plan 同时写入 authenticated provider request 和
`credential_value_reads=0`，两者在运行语义上不相容。推荐以以下字段替代模糊计数：

```text
CREDENTIAL_IDENTIFIERS_CONFIGURED
CREDENTIAL_VALUES_ACCESSED_IN_PROCESS_MEMORY
AUTHORIZATION_HEADER_VALUES_EMITTED_TO_TLS_CLIENT
CREDENTIAL_VALUES_PRINTED
CREDENTIAL_VALUES_PERSISTED
CREDENTIAL_VALUES_EXPOSED_OUTSIDE_AUTHORIZED_TRANSPORT
```

`ACCESSED_IN_PROCESS_MEMORY=1` 不等于 secret exposure。只有明确证据才能把
printed、persisted 或 exposed 置为非零。

## 5. Offline Design Scope

允许：

- 复用 PRE-70 已净化事实；
- 形成 response-contract v0.2 candidate；
- 形成 provider capability evidence checklist；
- 形成 credential accounting profile；
- 创建 synthetic positive/negative fixtures；
- 本地 Schema 与 fail-closed validator；
- DBA path-scoped commit/push。

禁止：

- 读取或记录任何 credential value；
- 调用 Qianfan、Qwen 或其他模型；
- 从 PRE-70 raw response 提取内容；
- 修改 `titmas-integrations`；
- 创建或修改 DBOS、SAEE、Runtime、Agent、Entity、Permission 或 Evidence Truth；
- 宣称 formal review、Provider support、Standard Ready 或 release。

## 6. Required Offline Checks

最少必须拒绝：

1. code-fenced JSON 被当作 direct JSON；
2. prefix/suffix prose 被忽略；
3. extraction 或 repair 被启用；
4. 没有 capability evidence 却声明 response contract proven；
5. authenticated request 同时记录 zero in-memory credential access；
6. in-memory credential access 自动等于 secret exposure；
7. platform PASS 自动等于 formal Security Review；
8. contract candidate 自动等于 adopted Standard。

## 7. Decision Eligibility

本推荐满足 `TITMAS-CS-STANDING-001` 的候选条件，但推荐本身仍不是 Decision。

```text
RECOMMENDATION_RECORDED=true
DECISION_RECORDED=false
OFFLINE_EXECUTION_AUTHORIZED=false
LIVE_MODEL_REQUEST_AUTHORIZED=false
```

只有独立 `CS-D02-PRE-71` Decision 和 frozen execution plan 均记录后，才可开始
离线设计。

## 8. Stop Conditions

任一情况发生即停止：

- PRE-70 receipt 或 target commit 漂移；
- 提案需要 live request、secret value 或 raw provider response；
- 需要修改 target、DBOS 或 SAEE；
- response contract 允许未冻结的 extraction/repair；
- credential accounting 把 access 自动解释为 exposure；
- 产生 Authority、Implementation、Provider support、Standard 或 Release 抬升。

## 9. Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
LIVE_MODEL_REQUEST_AUTHORIZED=false
PROVIDER_SUPPORTED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
CONTRACT_ADOPTED_AS_STANDARD=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## 10. Truth Boundaries

```text
PROMPT_REQUESTING_JSON_NE_STRUCTURED_OUTPUT_CAPABILITY
OUTER_JSON_NE_DIRECT_ASSISTANT_JSON
EXTRACTABLE_JSON_NE_DIRECT_JSON
IN_MEMORY_SECRET_ACCESS_NE_SECRET_EXPOSURE
PLATFORM_PASS_NE_FORMAL_SECURITY_REVIEW
OFFLINE_CONTRACT_DESIGN_NE_PROVIDER_CONFORMANCE
RECOMMENDATION_NE_DECISION
REFERENCE_IMPLEMENTATION_NE_STANDARD
```
