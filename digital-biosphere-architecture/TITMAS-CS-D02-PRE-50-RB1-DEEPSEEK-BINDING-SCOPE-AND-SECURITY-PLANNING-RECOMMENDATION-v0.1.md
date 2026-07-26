---
document_id: DBA-TITMAS-CS-D02-PRE-50-RB1-DEEPSEEK-BINDING-PLANNING-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-50 RB1 DeepSeek Binding Scope and Security Planning Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-50 RB1 DeepSeek 绑定范围与安全规划推荐 v0.1
version: 0.1.0
status: canonical-recommendation-ready-for-standing-directive-eligibility-review
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
target_repository_observation: https://github.com/joy7758/titmas-integrations.git
target_branch_observation: codex/rb0-governance-baseline
target_commit_observation: 5ac891c5af88b1e9aeacdb3666217c6f832a57a6
target_write_paths_authorized: 0
credential_read_authorized: false
network_request_authorized: false
provider_binding_implementation_authorized: false
release_authorized: false
---

# PRE-50 RB1 DeepSeek Binding Scope and Security Planning Recommendation

## 1. Recommendation

```text
RECOMMENDATION_ID=CS-D02-PRE-50
RECOMMENDED_ACTION=AUTHORIZE_DBA_ONLY_RB1_DEEPSEEK_BINDING_SCOPE_SECURITY_AND_AGENT_REVIEW_PLANNING_PACKET
RECOMMENDATION=RECOMMENDED
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY_WRITE_PATHS=0
PROVIDER_REQUESTS=0
CREDENTIAL_READS=0
IMPLEMENTATION_AUTHORIZED=false
```

建议只在 DBA 创建一个 machine-readable（机器可读）的 Provider binding planning packet，
固定单一 Provider candidate、transport candidate、安全边界、失败分类、负例和下一轮
Agent Review 输入。该行动不修改 `titmas-integrations`，不读取任何 credential，不发起
Provider 请求，不安装依赖，不形成 Provider support 或 conformance 声明。

## 2. Why This Action Is Next

PRE-49 已证明：

- target `5ac891c…` 的 provider-neutral Development reference implementation 可本地验证；
- 独立代码路径 validator 与 7 个冻结 fixture 的 rehearsal 为 `PASS`；
- 两次 offline build 均成功但产物 hash 不同；
- Provider binding、Provider conformance、第三方审查、安全审查和 release 仍为 false。

`B-025` 要求下一步先固定一个 Provider candidate 及其 credential、network、timeout、
error、sanitization、review、retention、rollback 和 stop rules。直接进入代码会跳过该
边界。

## 3. Exact Provider Candidate

```text
PROVIDER_CANDIDATE_ID=DEEPSEEK_OPENAI_COMPATIBLE_CHAT_COMPLETIONS
BASE_URL_CANDIDATE=https://api.deepseek.com
ENDPOINT_CANDIDATE=POST /chat/completions
MODEL_CANDIDATE=deepseek-v4-pro
STREAM_CANDIDATE=false
THINKING_TYPE_CANDIDATE=disabled
RESPONSE_FORMAT_CANDIDATE=json_object
CREDENTIAL_IDENTIFIER_ONLY=DEEPSEEK_API_KEY
PROVIDER_SUPPORT_STATUS=UNKNOWN_NOT_ADOPTED
```

选择理由：

- DeepSeek 官方文档当前明确 OpenAI-compatible base URL、Chat Completions endpoint、
  Bearer credential 方式和 `deepseek-v4-pro` 模型标识；
- 当前 DBA 历史中 DeepSeek direct-JSON 路径既有成功也有失败，只足以支持“规划候选”，
  不能证明 Provider correctness 或稳定支持；
- 只选一个 Provider，避免 fallback、model substitution 和多供应商失败被隐藏。

官方事实只是 planning reference。Provider 文档、model availability、SDK/API behavior
或价格变化都必须在未来执行 gate 重新核验。

## 4. Exact Transport Candidate

```text
TRANSPORT_CANDIDATE=httpcore==1.0.9
TRANSPORT_MODE_CANDIDATE=synchronous_http_1_1_direct
HTTP_2_CANDIDATE=false
PROXY_CANDIDATE=false
REDIRECT_CANDIDATE=false
AUTOMATIC_RETRY_CANDIDATE=false
TLS_VERIFICATION_CANDIDATE=true
SNI_HOSTNAME_CANDIDATE=api.deepseek.com
```

HTTPCore 官方 trace extension 当前暴露：

- TCP connect；
- TLS start；
- request headers/body；
- response headers/body；
- started、complete 和 failed events；
- connect/read/write/pool timeout extension。

官方文档同时说明 trace event set 可能跨版本变化，因此只能把 exact pin
`httpcore==1.0.9` 作为待审 candidate。PyPI 当前列出 1.0.9、Python `>=3.8`、
BSD-3-Clause；target 当前要求 Python `>=3.11`，但 dependency、license、hash、漏洞、
transitive dependency 和供应链接受仍需独立审查。

### 4.1 P0 Gap

HTTPCore trace 没有单独 DNS event。`connection.connect_tcp` 不能把 DNS 与 TCP 时间或
失败原因可靠拆分为 P0/P1。

```text
P0_DIRECT_OBSERVABILITY_WITH_CANDIDATE_TRANSPORT=false
P0_GAP=NOT_DIRECTLY_OBSERVABLE_IN_HTTPCORE_TRACE_REQUIRES_AGENT_REVIEW
P0_MUST_NOT_BE_SYNTHETIC_PASS=true
```

PRE-50 不选择自定义 resolver 或第二套 network path。未来 Agent/Security Review 必须在
以下选项中形成独立推荐：

1. 明确的 bounded resolver observation；
2. 可审计的 custom HTTPCore network backend；
3. 更换能够直接分离 P0/P1 的 transport；
4. 修订 Provider-binding profile，明确 P0 为 unsupported gap，但不得声称 P0–P9 完整
   conformance。

P0 未解决前，Provider-binding implementation recommendation 必须保持 blocked。

## 5. Planning Boundaries

### 5.1 Network and Endpoint

- only `https`；
- exact host `api.deepseek.com`；
- exact port `443`；
- exact path `/chat/completions`；
- no redirects、proxy、alternate host、beta base URL、Anthropic route 或 IP literal；
- certificate verification and hostname verification required；
- direct HTTP/1.1 candidate；HTTP/2 disabled for the first bounded profile；
- total request count in PRE-50 remains zero。

### 5.2 Credential and Sensitive Data

- only identifier `DEEPSEEK_API_KEY` may appear；
- credential value must never be read in PRE-50；
- future implementation must read the value only at request construction time；
- Authorization header value, request/response body, prompt, tool content, review content,
  hidden reasoning and environment dump must never enter phase events, logs, exceptions,
  fixtures, receipts or Git；
- allowed retained values are bounded byte counts, approved enum values, SHA-256 digests and
  sanitized timestamps/references；
- raw Provider error body retention is forbidden。

### 5.3 Candidate Limits

These are review candidates, not implemented limits:

```text
POOL_TIMEOUT_SECONDS=5
CONNECT_TIMEOUT_SECONDS=10
WRITE_TIMEOUT_SECONDS=30
READ_TIMEOUT_SECONDS=60
TOTAL_REQUEST_DEADLINE_SECONDS=90
MAX_SERIALIZED_REQUEST_BYTES=131072
MAX_RESPONSE_BODY_BYTES=1048576
MAX_OUTPUT_TOKENS=4096
MAX_CHOICES=1
```

No timeout may be `None` or infinite. Response reads must enforce a cumulative byte limit before
full buffering. Limit values require Agent/Security Review before implementation.

## 6. Failure Taxonomy Candidate

The planning packet must map first failure to one of:

```text
DNS_RESOLUTION_OR_P0_OBSERVABILITY_GAP
TCP_CONNECT_FAILURE
TLS_HANDSHAKE_FAILURE
REQUEST_HEADERS_WRITE_FAILURE
REQUEST_BODY_WRITE_FAILURE
HTTP_STATUS_FAILURE
RESPONSE_HEADERS_INVALID
RESPONSE_BODY_TIMEOUT
RESPONSE_BODY_SIZE_EXCEEDED
RESPONSE_BODY_READ_FAILURE
PROVIDER_EMPTY_OR_NULL_CONTENT
PROVIDER_FINISH_REASON_LENGTH
PROVIDER_CONTENT_FILTERED
PROVIDER_INSUFFICIENT_SYSTEM_RESOURCE
DIRECT_JSON_PARSE_FAILURE
RESPONSE_SCHEMA_FAILURE
SANITIZATION_FAILURE
HANDOFF_COMMIT_FAILURE
UNKNOWN_FAIL_CLOSED
```

HTTP `400/401/402/422/429/500/503` and other non-2xx responses must be preserved as first failure
metadata without raw body retention. Even when Provider documentation suggests retry or alternate
providers, the candidate profile performs no retry, fallback, alias inference, model substitution
or JSON repair.

## 7. Exact Planning Outputs

If authorized, PRE-50 may create exactly this directory and 12 files:

```text
commercialization-standards-titmas-integrations-rb1-provider-binding-planning/
  PRE-50-RB1-DEEPSEEK-BINDING-SCOPE-AND-SECURITY-PLANNING-RESULT-v0.1.md
  deepseek-binding-scope-and-security-plan-v0.1.md
  deepseek-binding-scope-and-security-plan.v0.1.json
  deepseek-binding-scope-and-security-plan.schema.v0.1.json
  deepseek-binding-negative-case-catalog.v0.1.json
  deepseek-binding-negative-case-catalog.schema.v0.1.json
  deepseek-binding-agent-review-input.v0.1.json
  deepseek-binding-agent-review-input.schema.v0.1.json
  pre50-provider-binding-planning-validation-result.v0.1.json
  pre50-provider-binding-planning-validation-result.schema.v0.1.json
  pre50-provider-binding-planning-execution-receipt.v0.1.json
  pre50-provider-binding-planning-execution-receipt.schema.v0.1.json
```

Separate governance records may be created:

```text
TITMAS-CS-D02-PRE-50-RB1-DEEPSEEK-BINDING-SCOPE-AND-SECURITY-PLANNING-DECISION-RECORD.md
TITMAS-CS-D02-PRE-50-RB1-DEEPSEEK-BINDING-SCOPE-AND-SECURITY-PLANNING-DECISION-RECORD.v0.1.json
architecture/schemas/titmas-cs-d02-pre50-deepseek-binding-planning-decision-record.schema.v0.1.json
```

## 8. Required Preconditions

1. DBA remote branch remains exactly `5a0a684928056a6f516d250e25855764e0b0e4dd`;
2. target branch remains exactly `5ac891c5af88b1e9aeacdb3666217c6f832a57a6`;
3. target `main` remains `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8`;
4. PRE-49 result and `B-025` remain canonical current inputs；
5. standing directive `TITMAS-CS-STANDING-001` remains active；
6. no later specific Human Decision conflicts；
7. official references are recorded with `observed_at=2026-07-27`；
8. exact planning fileset and zero target write scope are retained。

## 9. Validation

PRE-50 planning execution must:

- validate every JSON instance against its paired Draft 2020-12 Schema；
- reject additional properties in machine records；
- validate exact enum/status/effect values；
- bind the other 11 planning artifacts by SHA-256 in the execution receipt；
- report the receipt file's own SHA-256 only in the post-write validation output or later cockpit
  sync, because a canonical file cannot contain its own stable digest；
- verify Markdown relative links；
- verify 12/12 files and no target change；
- search for credential values, Authorization header values, raw bodies, prompts and hidden
  reasoning；
- retain every `UNKNOWN`, P0 gap and failed validation；
- produce no `PASS_PROVIDER_CONFORMANCE` or equivalent class。

## 10. Stop Conditions

Stop without partial semantic elevation if:

- DBA/target commit differs；
- official Provider/model/endpoint evidence conflicts or disappears；
- P0 is silently marked PASS；
- any credential value or sensitive body is read or retained；
- planning requires dependency installation, target write or network request；
- an artifact claims Provider support, conformance, security approval, release or commercial
  availability；
- exact fileset or Schema validation fails；
- standing directive is revoked or contradicted。

## 11. Next Gate

Successful PRE-50 planning may only enable a separate recommendation for four bounded sequential
Agent Review sessions:

1. Agent developer；
2. Agent recommender / machine customer；
3. integration maintainer；
4. security reviewer。

That future review must assess Provider/model/transport choice, P0 gap, credential handling,
network restrictions, failure taxonomy, sanitization, limits, dependency supply chain and stop
conditions. It does not authorize implementation.

## 12. False Effects

```text
TARGET_REPOSITORY_CHANGED=false
PROVIDER_BINDING_IMPLEMENTED=false
PROVIDER_REQUEST_EXECUTED=false
CREDENTIAL_READ=false
DEPENDENCY_INSTALLED=false
PROVIDER_SUPPORTED=false
PROVIDER_CONFORMANCE_EXECUTED=false
THIRD_PARTY_CONFORMANCE=false
SECURITY_REVIEW_EXECUTED=false
REPRODUCIBLE_BUILD_PROVEN=false
DBOS_CHANGED=false
SAEE_CHANGED=false
AGENT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_TRUTH_CHANGED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```

## 13. Official Reference Pins

Observed on `2026-07-27`:

- DeepSeek first API call:
  `https://api-docs.deepseek.com/quick_start/pricing-details-usd/`；
- DeepSeek Chat Completions:
  `https://api-docs.deepseek.com/api/create-chat-completion/`；
- DeepSeek JSON Output:
  `https://api-docs.deepseek.com/guides/json_mode/`；
- DeepSeek error codes:
  `https://api-docs.deepseek.com/quick_start/error_codes/`；
- HTTPCore extensions:
  `https://www.encode.io/httpcore/extensions/`；
- HTTPCore PyPI:
  `https://pypi.org/project/httpcore/`。

Official reference observation is not adoption, implementation or conformance.
