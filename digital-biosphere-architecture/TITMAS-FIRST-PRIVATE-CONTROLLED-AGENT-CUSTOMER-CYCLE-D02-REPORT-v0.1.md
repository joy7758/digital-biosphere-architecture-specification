---
document_id: TITMAS-FIRST-PRIVATE-CONTROLLED-AGENT-CUSTOMER-CYCLE-D02-REPORT-v0.1
title: TITMAS First Private Controlled Agent Customer Cycle D02 Report v0.1
title_zh: TITMAS 首个私有受控智能体客户闭环 D02 报告 v0.1
status: stopped-failed-closed-human-disposition-required
decision_id: TITMAS-FIRST-PRIVATE-CONTROLLED-AGENT-CUSTOMER-CYCLE-D02
decision: ACCEPT_ONCE
decided_by_ref: zhangbin
source_main: 601eb69d33cf71f448e704aa2c11ee77f3e58fe2
gateway_revision: 05f9b3f26c9bd970d0e2c615bb7117e7b9dd4b6f
---

# TITMAS First Private Controlled Agent Customer Cycle D02 Report v0.1

## Outcome

The one-time private controlled cycle was dispatched exactly three times and
then stopped fail closed. The Qwen planning call, the single local black-box
operation and the Qwen customer-assessment call completed. The independent
Kimi review did not complete: its request was dispatched, but no response
headers or body were captured before the client timeout.

```text
PRIVATE_AGENT_CUSTOMER_PLANNING_COMPLETE=true
PRIVATE_BLACK_BOX_OPERATION_COMPLETE=true
PRIVATE_AGENT_CUSTOMER_ASSESSMENT_COMPLETE=true
INDEPENDENT_AGENT_REVIEW_COMPLETE=false

FIRST_PRIVATE_AGENT_CUSTOMER_CYCLE_COMPLETE=false
HUMAN_DISPOSITION_REQUIRED=true

STOP_REASON=POST_DISPATCH_OUTCOME_UNKNOWN
AUTOMATIC_RETRY_CREATED=false
PROVIDER_SUBSTITUTION_USED=false
```

The Kimi outcome is `UNKNOWN`, not `REJECT`, `ABSTAIN` or a negative customer
judgment. A new call would require a new explicit Human Decision.

## Source and authorization

```text
REPOSITORY=joy7758/digital-biosphere-architecture-specification
REPOSITORY_VISIBILITY=PRIVATE
SOURCE_MAIN=601eb69d33cf71f448e704aa2c11ee77f3e58fe2
SOURCE_MAIN_DRIFT=false
POST_EXECUTION_ORIGIN_MAIN=73431b7dd26f971c053f0d7136ed6edc63608236
POST_EXECUTION_REMOTE_MAIN_ADVANCED=true
D02_SENSITIVE_PATH_OVERLAP_AFTER_EXECUTION=0

PR_NUMBER=49
PR_HEAD=05f9b3f26c9bd970d0e2c615bb7117e7b9dd4b6f
PR_MERGE_COMMIT=601eb69d33cf71f448e704aa2c11ee77f3e58fe2

DECISION_ID=TITMAS-FIRST-PRIVATE-CONTROLLED-AGENT-CUSTOMER-CYCLE-D02
DECISION=ACCEPT_ONCE
DECIDED_BY_REF=zhangbin
DECISION_SCOPE=ONE_PRIVATE_CONTROLLED_AGENT_CUSTOMER_CYCLE
```

The historical readiness packet remains a pre-execution record. This report
records the later Human Decision and actual bounded attempt; it does not
rewrite the readiness artifact as if it had already authorized execution.

`origin/main` advanced by PR #50 only after all three D02 dispatches. The two
new commits add a governance-intelligence intake and update the repository
README; they do not touch the D02 gateway, Response Capture, private boundary,
customer bundle or execution authorization paths. This audit branch therefore
preserves the exact executed source instead of rebasing the completed attempt
onto an unexecuted revision.

## Provider terms and data scope

Provider terms were observed on `2026-07-29T08:41:14Z` from official sources:

- Alibaba Cloud Token Plan endpoint and account guidance:
  <https://help.aliyun.com/zh/model-studio/other-tools-token-plan>
- Alibaba Cloud Token Plan Team quick start and data-use statement:
  <https://help.aliyun.com/zh/model-studio/token-plan-team-quickstart>
  and
  <https://help.aliyun.com/zh/model-studio/token-plan-team-faq>
- Alibaba Cloud Qwen model and pricing references:
  <https://help.aliyun.com/zh/model-studio/qwen3-7-max>
  and
  <https://help.aliyun.com/zh/model-studio/model-pricing>
- Baidu Qianfan model list, pricing and service terms:
  <https://cloud.baidu.com/doc/qianfan/s/rmh4stp0j>,
  <https://cloud.baidu.com/doc/qianfan/s/wmh4sv6ya>,
  <https://cloud.baidu.com/doc/qianfan/s/emh4stmvj> and
  <https://cloud.baidu.com/doc/qianfan/s/Mmk5a8wjk>.

The configured Alibaba endpoint and dedicated key were used. Account edition,
contract status and server-side retention were not inferred beyond the
official material. Baidu's general agreement cautions against submitting
confidential material and permits service-related processing; therefore the
review input was restricted to nonconfidential synthetic content. No claim is
made that Provider-side storage is zero or that deletion was independently
verified.

```text
PROVIDER_TERMS_REVIEW_COMPLETED=true
DATA_CLASSIFICATION=NONCONFIDENTIAL_SYNTHETIC_EVALUATION_ONLY

PERSONAL_DATA_INCLUDED=false
CUSTOMER_DATA_INCLUDED=false
CONFIDENTIAL_CORE_INCLUDED=false
SECRET_INCLUDED=false
REAL_PRODUCTION_EVIDENCE_INCLUDED=false

CONTRIBUTOR_CORE_ACCESS=false
REVIEWER_CORE_ACCESS=false
CONTRIBUTOR_PRIVATE_REPOSITORY_ACCESS=false
REVIEWER_PRIVATE_REPOSITORY_ACCESS=false
PRIVATE_CONTEXT_EXPOSURE_COUNT=0
```

Only the nine-file customer bundle, synthetic request contract, sanitized
customer-visible gateway projection and explicit evaluation tasks were
eligible for Provider transmission. No repository history, private source,
gateway implementation, internal tests, credentials, absolute local paths,
current ChatGPT conversation or hidden expected answer was transmitted.

## Preflight and budget

```text
REQUEST_SHAPE_PREFLIGHT=PASS
CAPTURE_DESTINATION_PREFLIGHT=PASS
SCHEMA_VALIDATION=PASS
DATA_SCOPE_GATE=PASS

PRIVATE_EVALUATION_GATEWAY_TESTS=16/16_PASS
RESPONSE_CAPTURE_TESTS=16/16_PASS
PRIVATE_BOUNDARY_TESTS=18/18_PASS

CORE_SOURCE_DISCLOSURE_FINDINGS=0
SECRET_FINDINGS=0
PRIVATE_PATH_FINDINGS=0
```

The pre-call conservative public-rate-equivalent estimate, including a safety
margin and the maximum three calls, was `CNY 1.3432`, below the authorized
`CNY 10` hard ceiling. The two captured Qwen calls used 5,313 input tokens and
4,278 output tokens; their public pay-as-you-go-equivalent estimate is
approximately `CNY 0.3400`. Kimi usage and any resulting charge are unknown
because no response was captured. Alibaba Token Plan may account in plan
credits rather than direct per-call RMB. No claim of exact invoice cost is
made.

```text
MAX_PROVIDER_SPEND_CNY=10
PRECALL_ESTIMATED_COST_CNY_UPPER=1.3432
KNOWN_QWEN_PUBLIC_RATE_EQUIVALENT_CNY=0.3400
ACTUAL_PROVIDER_INVOICE_COST=UNKNOWN
BUDGET_LIMIT_BREACH_OBSERVED=false
```

## Controlled customer flow

### Contributor planning

```text
ATTEMPT_ID=D02-CONTRIBUTOR-PLAN
PROVIDER=ALIBABA_DASHSCOPE
REQUESTED_MODEL=qwen3.7-max
RETURNED_MODEL=qwen3.7-max
MODEL_IDENTITY_STATUS=MATCH
HTTP_STATUS=200
FINAL_STATE=FINALIZED_SUCCESS
REQUEST_PAYLOAD_SHA256=df30d8636527ab1c0b5bfc65c2e8c2194bdca8aadaf1fc72268d542b1c928565
RESPONSE_BODY_SHA256=49b3edc6e1685d65391f1055395848bc6849fc67f2436a8b698cf3368ce3031b
USAGE_INPUT_TOKENS=2202
USAGE_OUTPUT_TOKENS=2868
USAGE_TOTAL_TOKENS=5070
```

The structured planning object was parsed and contract-validated in memory.
It selected a non-abstaining operation, because the local gateway and second
Contributor call were reached. The temporary orchestrator did not durably
persist the sanitized structured object before the later Reviewer timeout
terminated the process. The raw Provider response was deliberately deleted
after capture and cannot be reconstructed from its hash.

```text
PLANNING_RESULT=VALIDATED_IN_MEMORY_CONTENT_NOT_RETAINED
PLANNING_CONTENT_RECOVERY_WITHOUT_NEW_PROVIDER_CALL=false
```

### Local black-box operation

Exactly one loopback gateway operation completed using the Contributor's
unmodified request body. Reaching the second Contributor call establishes
that the gateway response was customer-visible, JSON-parseable and had a
`FINALIZED_SUCCESS` local capture.

The operation name, HTTP status, reason code and request/response body hashes
were held only in the terminated process and were not durably retained. They
must not be guessed or silently reconstructed.

```text
GATEWAY_OPERATION=NOT_RETAINED
GATEWAY_HTTP_STATUS=NOT_RETAINED
PUBLIC_REASON_CODE=NOT_RETAINED
REQUEST_BODY_SHA256=NOT_RETAINED
RESPONSE_BODY_SHA256=NOT_RETAINED
RESPONSE_CAPTURE_FINAL_STATE=FINALIZED_SUCCESS
GATEWAY_PUBLIC_EXPOSURE=false
```

This is an audit-instrumentation defect in the one-off orchestrator, not
evidence that the local gateway failed or that its result was correct.

### Contributor assessment

```text
ATTEMPT_ID=D02-CONTRIBUTOR-ASSESSMENT
PROVIDER=ALIBABA_DASHSCOPE
REQUESTED_MODEL=qwen3.7-max
RETURNED_MODEL=qwen3.7-max
MODEL_IDENTITY_STATUS=MATCH
HTTP_STATUS=200
FINAL_STATE=FINALIZED_SUCCESS
REQUEST_PAYLOAD_SHA256=306c8cd58db0c75fe4b55ca1025728228a3b1185d0ee4ed11a5dfd61f4d038f5
RESPONSE_BODY_SHA256=e0d261f36010c851d02533b782367876b20127c1e4b410742253bb80ef858a53
USAGE_INPUT_TOKENS=3111
USAGE_OUTPUT_TOKENS=1410
USAGE_TOTAL_TOKENS=4521
```

The structured assessment was parsed and contract-validated in memory. Its
recommendation content was not durably persisted before the Reviewer timeout.
No recommendation category is inferred from the response hash or token count.

```text
CUSTOMER_ASSESSMENT=VALIDATED_IN_MEMORY_CONTENT_NOT_RETAINED
CUSTOMER_RECOMMENDATION=UNKNOWN
```

### Independent review

```text
ATTEMPT_ID=D02-INDEPENDENT-REVIEW
PROVIDER=BAIDU_QIANFAN
REQUESTED_MODEL=kimi-k2.6
RETURNED_MODEL=
MODEL_IDENTITY_STATUS=NOT_ASSESSED
HTTP_STATUS=0
FINAL_STATE=FAILED_AFTER_DISPATCH_OUTCOME_UNKNOWN
FAILURE_PHASE=DISPATCH
OUTCOME_CLASSIFICATION=POST_DISPATCH_OUTCOME_UNKNOWN
RETRY_ELIGIBILITY=PROHIBITED_WITHOUT_NEW_HUMAN_DECISION
REQUEST_PAYLOAD_SHA256=a49d68aaa02e91edc98f7a2d32d49f7983215f0fadcb170c8e8aea8c8f9b3e84
RESPONSE_BODY_SHA256=
TOKEN_USAGE=UNKNOWN
```

```text
REVIEW_VERDICT=UNKNOWN
CUSTOMER_RESULT_SUPPORTED=NOT_ASSESSED
AUTOMATIC_RETRY_AUTHORIZED=false
```

## Response Capture

```text
MODEL_CALL_COUNT=3
PROVIDER_CALL_COUNT=3

FINALIZED_SUCCESS_COUNT=2
POST_DISPATCH_OUTCOME_UNKNOWN_COUNT=1
REQUESTED_MODEL_EQUALS_RETURNED_MODEL_COUNT=2
RAW_RESPONSE_SPOOL_COUNT=0
RAW_PROMPT_RETAINED=false
RAW_RESPONSE_RETAINED=false
HIDDEN_REASONING_RETAINED=false
CREDENTIAL_MATERIAL_RETAINED=false
```

The count records dispatched calls. It does not claim that the third model
completed inference or returned a review.

## Deterministic post-validation

| Validation | Result |
|---|---|
| Private Evaluation Gateway | `16/16 PASS` |
| Response Capture | `16/16 PASS` |
| Private boundary and source classification | `18/18 PASS` |
| TITMAS conformance unit tests | `40/40 PASS` |
| Agent-native tests | `25/25 PASS` |
| Reference tests | `5/5 PASS` |
| Site tests | `22/22 PASS` |
| Site lint | `PASS` |
| Production dependency audit | `0 vulnerabilities` |
| Core source disclosure scan | `0 findings` |
| Strong-pattern secret scan | `0 findings` |
| Private-path disclosure scan | `0 findings` |
| Unauthorized export | `0` |

The complete site development dependency tree continues to report nine
high-severity advisories. This D02 cycle did not change dependencies or apply
a breaking forced upgrade.

## Limitations and final cycle state

1. The independent review is unresolved after dispatch; it cannot be treated
   as pass, rejection or abstention.
2. The sanitized Qwen plan, gateway projection and Qwen assessment were
   validated in memory but not durably retained by the temporary orchestrator.
3. Hashes prove byte continuity only; they do not reveal meaning, establish
   truth, authorize action or prove customer value.
4. The synthetic loopback result does not establish production readiness,
   commercial adoption, a service-level commitment or an external customer.
5. Any further Provider call requires a new Human Decision; D02 itself cannot
   be retried under `ACCEPT_ONCE`.

```text
PRIVATE_AGENT_CUSTOMER_PLANNING_COMPLETE=true
PRIVATE_BLACK_BOX_OPERATION_COMPLETE=true
PRIVATE_AGENT_CUSTOMER_ASSESSMENT_COMPLETE=true
INDEPENDENT_AGENT_REVIEW_COMPLETE=false

FIRST_PRIVATE_AGENT_CUSTOMER_CYCLE_COMPLETE=false
HUMAN_DISPOSITION_REQUIRED=true

CORE_REPOSITORIES_PRIVATE=true
PUBLIC_EXPORT_AUTHORIZED=false
COMMERCIAL_ACCESS_GRANTED=false
COMMERCIAL_AGREEMENTS_ACTIVE=false
TITMAS_COMMUNITY_ESTABLISHED=false
```

## TITMAS drift check

```text
TITMAS_DRIFT_CHECK

AI_AGENT_IS_OPERATIONAL_CUSTOMER=true
HUMAN_OR_ORGANIZATION_IS_ACCOUNTABLE_PRINCIPAL=true

CUSTOMER_RECEIVED_CONTRACT_NOT_IMPLEMENTATION=true
CORE_SOURCE_DISCLOSED=false
PRIVATE_REPOSITORY_ACCESS_GRANTED=false

MODEL_CALL_COUNT_LE_3=true
AUTOMATIC_RETRY_CREATED=false
PROVIDER_SUBSTITUTION_USED=false

NEW_CONTROL_AUTHORITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
RUNTIME_OR_EXECUTOR_CREATED=false

COMMERCIAL_PILOT_AUTOMATICALLY_AUTHORIZED=false
COMMUNITY_ESTABLISHED_OVERCLAIMED=false

TITMAS_DRIFT_CHECK_RESULT=PASS_WITH_RECORDED_LIMITATIONS
```
