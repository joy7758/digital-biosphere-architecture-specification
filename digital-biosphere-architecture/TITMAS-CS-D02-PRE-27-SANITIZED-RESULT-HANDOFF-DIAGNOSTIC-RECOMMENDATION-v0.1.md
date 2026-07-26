---
document_id: DBA-TITMAS-CS-D02-PRE-27-SANITIZED-RESULT-HANDOFF-DIAGNOSTIC-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-27 Sanitized Result Handoff Diagnostic Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-27 消毒后结果交接诊断建议 v0.1
version: 0.1.0
status: exact-offline-diagnostic-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-27
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
network_request_authorized: false
live_model_request_authorized: false
contract_adoption_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-27 Sanitized Result Handoff Diagnostic Recommendation v0.1

## 1. Why PRE-27 Exists

PRE-26 在远端验证的 Decision 与 authorization receipt 之后启动唯一授权执行进程，但执行
通道没有返回任何 sanitized stdout：

```text
PRE26_EXECUTION_PROCESS_COMPLETION_OBSERVED=true
PRE26_SANITIZED_STDOUT_BYTES_OBSERVED=0
PRE26_SANITIZED_SESSION_RESULTS_RECOVERED=0
PRE26_QUALIFYING_REVIEWS=0
PRE26_FORMAL_ADOPTION_DECISION_REVIEW_READY=false
PRE26_RESULT=INCOMPLETE_FAIL_CLOSED
```

PRE-26 的请求预算已经按最保守边界耗尽，不能重试。当前缺口不是可以归因给 Kimi、GLM
或 Qianfan 的 provider failure，而是 caller 与 orchestration channel 之间没有一个可验证、
独立于 stdout 的 sanitized-result handoff。

## 2. Pre-development Agent Recommendation Gate

如果潜在 Agent 客户现在询问“是否应采用 TITMAS v0.2 provider review contract 或依赖这条
审查链路”，当前回答是：

```text
RECOMMEND_TITMAS_V0_2_CONTRACT_FOR_IMPLEMENTATION_OR_PRODUCTION_USE=NO
REASON=NO_QUALIFYING_REVIEW_AND_SANITIZED_RESULT_HANDOFF_IS_NOT_OBSERVABLE
RECOMMEND_OFFLINE_HANDOFF_DIAGNOSTIC=YES
RECOMMEND_NEW_PROVIDER_REQUEST=NO
```

不推荐的具体原因：

1. PRE-26 没有产生可验证 session result；
2. stdout completion 不能证明 sanitized result 已交付；
3. raw envelope 禁止持久化，不能事后恢复；
4. 没有独立 sink 时，caller output loss 会让整个 evidence chain 断裂；
5. `VALID_PROBLEM_RECORDS=0` 且 `CS_G0_PASS=false`。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_PRE26_SANITIZED_RESULT_HANDOFF_DIAGNOSTIC_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
PROVIDER_NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
MODEL_SUBSTITUTIONS_MAX=0
SECRET_READS_MAX=0
RAW_PROVIDER_ENVELOPES_CREATED=0
IMPLEMENTATION_AUTHORIZED=false
CONTRACT_ADOPTION_AUTHORIZED=false
```

只建议用 synthetic fixtures 验证一个临时、进程外可观察的 sanitized-result sink
contract。该动作不重新执行 Kimi/GLM，不访问 Qianfan，不读取 API key，不创建 reusable
Adapter 或 Runtime。

## 4. Proposed Handoff Contract

future offline diagnostic 应冻结：

1. sanitized result 必须先通过 frozen session-result Schema；
2. sink 只允许包含 schema-valid sanitized result，不允许 raw envelope、usage、credential、
   hidden reasoning 或 provider error body；
3. sink 使用新建的受限临时目录和单一 exact file target；
4. 写入使用 `write -> fsync -> atomic rename` 的 committed-state protocol；
5. receipt 必须绑定 content SHA-256、byte count、Schema id 和 lifecycle state；
6. stdout 可选；sink 是唯一可恢复 handoff，stdout 不是 canonical evidence；
7. sink 缺失、空文件、partial write、invalid JSON、Schema failure、digest mismatch、
   duplicate commit 或 cleanup failure 均失败关闭；
8. 失败 fixture 必须保留，不能自动 repair；
9. diagnostic 完成后删除临时 sink；只把 synthetic validation result 和 digest 写入 Git。

该 contract 只是 review-governance handoff candidate，不是 Evidence Truth、DBOS Evidence
Object、Runtime storage、database、queue、product API 或 production durability guarantee。

## 5. Required Synthetic Fixtures

至少包括：

| fixture | expected |
|---|---|
| Schema-valid sanitized result + stdout present | PASS |
| Schema-valid sanitized result + stdout suppressed | PASS |
| sink missing | FAIL_CLOSED |
| sink empty | FAIL_CLOSED |
| partial JSON | FAIL_CLOSED |
| response Schema invalid | FAIL_CLOSED |
| raw envelope field present | FAIL_CLOSED |
| credential-like field present | FAIL_CLOSED |
| digest mismatch | FAIL_CLOSED |
| duplicate committed sink | FAIL_CLOSED |
| cleanup failure | FAIL_CLOSED |

fixture 内容必须是 synthetic；不得包含真实 provider response、secret 或 PRE-26 丢失内容的
推定版本。

## 6. Required Outputs

若未来独立 Decision 采用本建议，只可创建：

- sanitized-result handoff contract 与 Schema；
- synthetic positive/negative fixtures 与 Schema；
- offline diagnostic plan、input manifest 与 Schema；
- deterministic validation result 与 Schema；
- authorization receipt、execution receipt 和 result report；
- cockpit synchronization。

禁止创建：

- provider caller、Adapter、SDK、Runtime 或 service；
- production persistence；
-真实 Agent、Entity、Permission、Evidence Truth；
- 新 provider request、model review 或 recovered PRE-26 result。

## 7. Preconditions

1. PRE-26 authorization receipt、failure result、execution receipt 和 report 在目标远端；
2. 四个 source hash 全部匹配；
3. standing directive active；
4. 独立 PRE-27 Decision、plan、Schema 和 fixtures 在 execution 前远端验证；
5. offline diagnostic network access 明确为 0；
6. 使用全新临时目录，不覆盖任何用户文件；
7. PRE-26 request budget 保持关闭。

Frozen sources:

| artifact | SHA-256 |
|---|---|
| `contract-v0-2-candidate-review-authorization-receipt.v0.1.json` | `62c1bcf7199dea1038bb64715d1f3fcb3afd22a0c8fac9e2fe7b0ece39530a39` |
| `contract-v0-2-candidate-review-execution-failure-result.v0.1.json` | `0fd25dc98d5e5fe1c48b3c51ac0ab11d450bed8d043c933b11331e70d383e861` |
| `contract-v0-2-candidate-review-execution-receipt.v0.1.json` | `5cf13eebbd81741486e7851589e5ad95bc84d98c8c5c711c9c6d8e6b3be35f3a` |
| `PRE-26-V0-2-CONTRACT-CANDIDATE-REVIEW-RESULT-v0.1.md` | `624fdda71acf96d8c76d390295bfaf73f786faba86b7304ee94790e0e4373852` |

## 8. Stop Conditions

- 任一 source/hash 漂移；
- 任何 network、provider、model 或 credential access；
- 临时 target 不唯一或可能覆盖既有文件；
- raw envelope、usage、secret、hidden reasoning 或 error body 进入 sink；
- synthetic failure 被自动修复或删除；
- sink PASS 被抬升为 provider correctness、review completion、contract Adoption、
  implementation、production durability、conformance、Certification、Release 或 customer
  proof；
- PRE-26 request budget 被重新打开。

## 9. Success Conditions

```text
SOURCE_HASHES_MATCH=4/4
SCHEMAS_META_VALID=ALL
SYNTHETIC_FIXTURE_EXPECTATIONS_MATCH=11/11
STDOUT_SUPPRESSED_VALID_SINK_RECOVERED=true
RAW_PROVIDER_FIELDS_PERSISTED=0
CREDENTIAL_FIELDS_PERSISTED=0
NETWORK_REQUESTS_EXECUTED=0
LIVE_MODEL_REQUESTS_EXECUTED=0
PRE26_REQUEST_BUDGET_REOPENED=false
HANDOFF_CONTRACT_CANDIDATE_READY=true
PROVIDER_REVIEW_RERUN_READY=false
CONTRACT_ADOPTED=false
IMPLEMENTATION_CREATED=false
```

## 10. False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE26_RESULT_CHANGED=false
PRE26_REQUEST_BUDGET_REOPENED=false
PRE26_SESSION_RESULTS_RECOVERED=false
HANDOFF_CONTRACT_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
RUNTIME_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 11. Standing Directive Eligibility

本建议只有一个 exact offline action，输入、临时 target、fixture 数、network/secret cap、输出、
stop conditions 和 false effects 均已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE27_DECIDED=false
AT_RECOMMENDATION_TIME_DIAGNOSTIC_EXECUTION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_NETWORK_REQUESTS_EXECUTED=0
AT_RECOMMENDATION_TIME_IMPLEMENTATION_CREATED=false
```
