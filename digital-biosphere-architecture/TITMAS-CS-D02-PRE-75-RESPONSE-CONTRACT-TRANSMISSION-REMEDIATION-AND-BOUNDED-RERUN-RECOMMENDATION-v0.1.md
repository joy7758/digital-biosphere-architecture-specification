---
document_id: DBA-TITMAS-CS-D02-PRE-75-RESPONSE-CONTRACT-TRANSMISSION-REMEDIATION-AND-BOUNDED-RERUN-RECOMMENDATION-0.1
version: 0.1.0
status: canonical-recommendation-ready-for-decision
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
network_requests_max: 0
live_model_requests_max: 0
credential_value_reads_max: 0
implementation_authorized: false
---

# TITMAS CS-D02 PRE-75 Response-Contract Transmission Remediation and Bounded Rerun Recommendation v0.1

## 1. Recommendation

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
EXACT_RECOMMENDED_ACTION=AUTHORIZE_PRE75_OFFLINE_FULL_RESPONSE_SCHEMA_TRANSMISSION_REMEDIATION_AND_PRE76_TWO_REQUEST_RERUN_SCOPE_DESIGN
PRE75_RECOMMENDATION_PREPARED=true
PRE75_DECIDED=false
PRE75_OFFLINE_EXECUTION_AUTHORIZED=false
PRE75_OFFLINE_EXECUTED=false
PRE76_LIVE_RERUN_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

建议授权一次严格离线的 PRE-75 request-contract transmission remediation。它只生成
完整 response Schema 传输候选、两条 deterministic request fixture、覆盖验证、脱敏
failure-capture integration 和未来 PRE-76 两请求复测范围。

本 Recommendation 不授权调用 Qianfan 或 Qwen，不采纳新的 request contract，也不改变
frozen PRE-73 response Schema。

## 2. Pre-development Agent recommendation gate

如果潜在 Agent 开发者问“你会推荐继续这条修复路线吗？”，答案是：

> 有条件推荐。PRE-74 已证明两条请求都没有携带完整响应契约；因此应先让每条请求自行
> 携带 hash-bound、machine-checkable 的完整 Schema，并离线证明传输完整性。只有这个
> 候选通过后，才值得申请最多两次、顺序执行、失败关闭的 Provider 复测。

当前不推荐直接在线重跑，原因是：

1. request contract 尚未形成可复验的完整 Schema 传输候选；
2. PRE-74 capture contract 仍是 `DEVELOPMENT_CANDIDATE_NOT_ADOPTED`；
3. 直接重跑会再次消耗请求预算，却不能证明修复输入已经稳定；
4. Agent Review 仍不能替代 formal Human Security Review。

## 3. Root-cause boundary

PRE-74 已证明：

```text
RESPONSE_SCHEMA_SERIALIZED_IN_PRE73_REQUESTS=false
TOP_LEVEL_EXACT_KEYS_TRANSMITTED=6/10
QUESTION_ASSESSMENT_EXACT_KEYS_TRANSMITTED=1/7
EXPLICIT_NON_CLAIM_EXACT_KEYS_TRANSMITTED=6/8
SCHEMA_STRUCTURE_MARKERS_TRANSMITTED=0/3
TRANSMISSION_GAP_PROVEN=true
EXACT_PRE73_FAILURE_CAUSE_PROVEN=false
```

PRE-75 只修复已证明的 transmission gap。它不得声称已恢复 PRE-73 的 exact rejected
path，也不得把合成测试升级为 Provider runtime causality。

## 4. Stage separation

### Stage A — PRE-75 offline remediation

只允许生成：

1. `pre75-review-request-contract-candidate.v0.2.json`；
2. Qianfan 与 Qwen 两条 deterministic rendered-request fixture；
3. 完整 response Schema canonical transmission payload；
4. contract-transmission coverage validation；
5. PRE-74 sanitized failure-detail capture integration；
6. PRE-76 exact two-request rerun scope candidate；
7. offline result 和 execution receipt。

Stage A 的 Decision 不得授权 Stage B。

### Stage B — future PRE-76 bounded live rerun

只有 Stage A 远端基线验证通过后，才能形成独立 PRE-76 Recommendation 与 Decision。未来
范围上限：

```text
PROVIDERS=BAIDU_QIANFAN,ALIBABA_CLOUD_MODEL_STUDIO
REQUESTS_MAX=2
REQUESTS_PER_PROVIDER_MAX=1
CONCURRENCY_MAX=1
RETRY_MAX=0
FALLBACK_MAX=0
MODEL_SUBSTITUTION_MAX=0
RESPONSE_EXTRACTION_MAX=0
JSON_REPAIR_MAX=0
RAW_REQUEST_OR_RESPONSE_PERSISTENCE_MAX=0
```

上述边界只是设计输入，不是当前授权。

## 5. Full-contract transmission rule

每条 future request 必须自行携带：

1. frozen response Schema 经
   `UTF8_JSON_SORT_KEYS_TRUE_SEPARATORS_COMMA_COLON_ENSURE_ASCII_FALSE`
   生成的完整 canonical JSON；
2. source Schema file SHA-256 与 canonical payload SHA-256；
3. exact session id 与 review role binding；
4. exact target commit 与 source-package SHA-256；
5. direct single JSON object、no fence/prefix/suffix/extraction/repair；
6. 10/10 top-level required keys；
7. 7/7 question-assessment required keys；
8. 8/8 explicit non-claim keys；
9. ordered `SR-001` through `SR-016` binding；
10. Agent Review advisory-only boundary。

不得依赖只存在于本地 Schema 文件、plan、README 或 validator 中的 out-of-band
requirement。

## 6. Exact offline validation

PRE-75 成功至少需要：

- 7/7 frozen input hashes；
- 2/2 rendered requests each contain the exact canonical response Schema bytes；
- 2/2 response Schema hashes match；
- top-level `10/10`、question assessment `7/7`、explicit non-claims `8/8`；
- Schema structure markers `3/3`；
- exact session/role bindings `2/2`；
- at least 16 mutation negatives fail closed；
- sanitized failure details pass their Schema；
- phase accounting preserves direct-JSON pass before later Schema failure；
- rendered request stays within a locally declared 131072-byte design budget；
- network/model/credential/raw response/target/DBOS/SAEE actions all equal 0。

## 7. Stop conditions

任一情况必须停止：

- input hash、target commit 或 frozen response Schema 漂移；
- live Provider request、credential value read 或 network action；
- raw PRE-73 response recovery；
- raw error message、offending value、source package 或 request persistence；
- response Schema semantic change；
- request candidate adoption；
- target、DBOS 或 SAEE write；
- 把 offline pass 写成 Provider support、formal Human Security Review、conformance、
  Standard Ready、release 或 production。

## 8. Authority boundaries

```text
Recommendation != Decision
Offline request candidate != adopted request contract
Rerun scope design != live rerun authorization
Full Schema transmission != Provider conformance
Schema pass != Security Review correctness
Agent Review != formal Human Security Review
Evidence != Truth
DBA != DBOS != SAEE
```

## 9. Machine-readable references

- [PRE-75 scope](commercialization-standards-pre75-response-contract-transmission-remediation/pre75-remediation-and-rerun-scope.v0.1.json)
- [PRE-74 result](commercialization-standards-pre74-schema-failure-diagnostic/pre74-offline-diagnostic-result.v0.1.json)
- [PRE-74 receipt](commercialization-standards-pre74-schema-failure-diagnostic/pre74-execution-receipt.v0.1.json)
- [PRE-74 transmission map](commercialization-standards-pre74-schema-failure-diagnostic/pre74-response-contract-transmission-map.v0.1.json)
- [PRE-73 request contract](commercialization-standards-p0-exact-agent-security-review/pre73-review-request-contract.v0.1.json)
- [Frozen response Schema](commercialization-standards-p0-exact-agent-security-review/pre73-agent-review-response.schema.v0.2.json)

## 10. Required next gate

记录独立 PRE-75 Decision 后，才可执行 Stage A。即使 Stage A 通过，Stage B 仍必须等待
PRE-76 Recommendation、Decision、authorization baseline 和 remote clean-clone validation。
