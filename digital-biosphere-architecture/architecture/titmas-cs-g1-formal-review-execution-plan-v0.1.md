---
document_id: DBA-TITMAS-CS-G1-FORMAL-REVIEW-EXECUTION-PLAN-0.1
title: TITMAS CS-G1 Formal Review Execution Plan v0.1
title_zh: TITMAS CS-G1 正式审查执行计划 v0.1
status: PLAN_PREPARED_EXECUTION_BLOCKED_PENDING_HUMAN_DECISION
maturity: Development
maturity_scope: entire-document
created_at: 2026-07-28T16:36:29+08:00
primary_repository: digital-biosphere-architecture
owner_ref: NOT_ACCEPTED
decision_reference: CS-G1-ROLE-REVIEW-D01-NOT_DECIDED
implementation_effect: none
execution_effect: none
authority_effect: none
---

# TITMAS CS-G1 Formal Review Execution Plan v0.1

中文：TITMAS CS-G1 正式审查执行计划 v0.1。

## 1. Current state（当前状态）

```text
PLAN_PREPARED=true
PLAN_EXECUTION_AUTHORIZED=false
ROLE_ACCEPTED=false
REVIEWER_ASSIGNED=false
REVIEW_SESSION_EXECUTED=0
FORMAL_REVIEW_COMPLETE=false
CROSSWALK_ACCEPTED=false
CS_G1_PASS=false
```

本计划把三个未来 advisory review sessions 的输入、输出、失败和聚合规则冻结为一个
agent-readable（智能体可读）协议。它不能绕过待决定的
`CS-G1-ROLE-REVIEW-D01`，不能自行运行模型，也不能把 review result 转换为 Human
Decision。

## 2. Execution prerequisite（执行前置条件）

执行前必须有精确 Human Decision：

```text
CS-G1-ROLE-REVIEW-D01=ACCEPT_OPTION_A_BOUNDED_OWNER_ACCOUNTABILITY_AND_ROLE_SCOPED_QWEN_REVIEW
ROLE_ACCEPTED=true
CS_G1_ROLE_SCOPED_AGENT_REVIEW_AUTHORIZED=true
```

若 token 缺失、不同、过期或被撤销：

```text
EXECUTION_RESULT=NOT_EXECUTED
REQUESTS_SENT=0
```

Option B/C/D 不授权本计划的三个 `qwen3.7-max` sessions。

## 3. Immutable input set（不可变输入集合）

| Input | SHA-256 | Purpose |
|---|---|---|
| Owner/review decision candidate MD | `eedf8dccd903b0a3301d09ae1cd2df4a8877821c3120c97c4585b23aaf6f6f73` | 角色、期限、例外和 false effects |
| Owner/review decision candidate JSON | `4bf68d8dca71e436e25edc00b9c992fe608c676e7607a07a866c41341e0b0218` | 机器可读职责与三会话范围 |
| Candidate Qwen review | `1797e425127bc58e3479b52a1c50aa8fcc11b1795e39bfe10479f2cef76ddaa6` | Option A recommendation，不是决定 |
| CS-G1 readiness audit | `f296cb8e7eda80febbeca9b4157f92d5422a6ae75602a0e79e6e375c8b5460b5` | Gate 缺口与停止条件 |
| VEAP risk register | `ef1a38a4af01efe36cabb3e13c8e4815d05ba71c7703521c4fea05cd8a471492` | 16 个 OPEN risk |
| VEAP ownership crosswalk | `53a50508dcae8d490c79b7c4d9a3eee1b1ddc002d9808d2ea19b287a92dd7edf` | 14 个 candidate ownership surfaces |

任一 digest 改变时，必须停止并发布新的 plan revision。不得对变化后的文件沿用本计划
review result。

## 4. Review sessions（审查会话）

### 4.1 `CS-G1-REV-SEC-01`

Scope:

- `VEAP-SEC-001` 至 `VEAP-SEC-005`。

必须逐项判断：

- required control 是否足够明确、可实现、可验证；
- stop condition 是否失败关闭；
- 是否遗漏 source binding、replay、tenant/subject、revocation 或 sensitive-content 风险；
- disposition、required correction 和 residual risk。

### 4.2 `CS-G1-REV-PRIV-01`

Scope:

- `VEAP-PRIV-001` 至 `VEAP-PRIV-004`。

必须逐项判断：

- purpose/recipient limitation；
- reference-first minimization；
- retention、withdrawal、deletion、legal hold；
- linkability、namespace 和 public-safe extraction；
- disposition、required correction 和 residual risk。

### 4.3 `CS-G1-REV-CLAIM-AUTH-01`

Scope:

- `VEAP-CLAIM-001` 至 `VEAP-CLAIM-005`；
- `VEAP-AUTH-001` 至 `VEAP-AUTH-002`；
- canonical crosswalk 台账中从 `PROGRAM_ARCHITECTURE_RULE` 至
  `CERTIFICATION` 的全部 14 条 `surface_id`；必须使用台账原值，不得以概念别名替代。

必须逐项判断：

- Evidence/Truth、Verification/Permission、Evaluation/Authority 是否分离；
- certificate、certified Agent、production proof、complete-history 等禁止声明；
- VEAP 是否成为 DBOS、EEOAP、SAEE 或 verifier 的第二 canonical owner；
- SAEE advisory result 是否可能被转换为 Decision、writeback 或 Execution；
- 每条 crosswalk 的 `candidate_owner`、`authority_status`、allowed/prohibited effects 和
  blocking decisions 是否一致；
- disposition、required correction 和 residual risk。

## 5. Request contract（请求合同）

每个 session：

```text
PROVIDER=ALIBABA_CLOUD_MODEL_STUDIO
REQUESTED_MODEL=qwen3.7-max
REQUESTS=1
RETRY=0
FALLBACK=0
SUBSTITUTION=0
EXTRACTION=0
REPAIR=0
TEMPERATURE=0
TOOLS_ALLOWED=false
EXTERNAL_RETRIEVAL_ALLOWED=false
MEMORY_RETRIEVAL_ALLOWED=false
DIRECT_JSON_REQUIRED=true
PUBLIC_SAFE_FROZEN_BYTES_ONLY=true
```

请求必须包含：

1. review ID；
2. exact item IDs；
3. input paths、SHA-256 和 bytes；
4. role-specific question；
5. result Schema；
6. non-elevation invariants；
7. provider/model/request-count constraints。

不得把一个 session 的结果复制到另一个 scope。

## 6. Result contract（结果合同）

每个输出必须符合：

`schemas/titmas-cs-g1-formal-review-result.schema.v0.1.json`。

允许的逐项 disposition：

```text
ACCEPTED
ACCEPTED_WITH_RESIDUAL_RISK
RETURN_FOR_REVISION
REJECTED
NOT_ASSESSED
```

允许的 overall verdict：

```text
ACCEPT_FOR_HUMAN_FREEZE_REVIEW
RETURN_FOR_REVISION
REJECT
NOT_AVAILABLE
```

`ACCEPT_FOR_HUMAN_FREEZE_REVIEW` 只表示可提交人工 freeze review，不表示 risk accepted、
crosswalk accepted 或 `CS-G1 PASS`。

## 7. Fail-closed rules（失败关闭规则）

任何一项成立时，对应 session 必须失败：

- request 未被精确 Human Decision 授权；
- source digest/bytes 不匹配；
- HTTP/transport/provider failure；
- returned model 不是 `qwen3.7-max`；
- direct content 不是单一 JSON object；
- result 不符合 Schema；
- item 丢失、重复或 scope 外 item 出现；
- retry、fallback、substitution、extraction、repair 或 tool use 出现；
- failure、dissent、unknown 或 limitation 未保留。

失败 session：

```text
OVERALL_VERDICT=NOT_AVAILABLE
FORMAL_REVIEW_COMPLETE=false
CS_G1_PASS=false
```

不得用另一会话、历史输出或人工摘要填补。

## 8. Deterministic aggregation（确定性聚合）

只有全部条件满足时，三会话 bundle 才能标记
`READY_FOR_HUMAN_FREEZE_REVIEW`：

1. 3/3 session 均 `COMPLETED`；
2. 3/3 returned model identity 精确匹配；
3. 3/3 direct JSON 和 Schema validation 通过；
4. 16/16 risks 均有唯一 disposition；
5. 14/14 crosswalk surfaces 均有唯一 disposition；
6. `REJECTED`、`RETURN_FOR_REVISION`、`NOT_ASSESSED` 项为 0；
7. blocker 和 required correction 为 0；
8. 所有 residual risks 单独列出；
9. 所有 unresolved authority decisions 单独列出；
10. no-effect fields 全部为 false。

即使 bundle ready：

```text
RESIDUAL_RISK_ACCEPTED=false
CROSSWALK_ACCEPTED=false
SPECIFICATION_AUTHORITY_DELEGATED=false
CS_G1_PASS=false
```

后继 Human Decision 必须逐项接受、退回或拒绝。

## 9. Output inventory（未来输出清单）

只有执行获授权后，才可产生：

```text
architecture/reviews/cs-g1/security-review-result.v0.1.json
architecture/reviews/cs-g1/privacy-review-result.v0.1.json
architecture/reviews/cs-g1/claim-authority-review-result.v0.1.json
architecture/reviews/cs-g1/formal-review-bundle-result.v0.1.json
```

本计划不创建这些 result placeholders，防止“文件存在”被误读为 review 已执行。

## 10. Current effects（当前效力）

```text
ROLE_ACCEPTED=false
REVIEWER_ASSIGNED=false
REVIEW_EXECUTION_AUTHORIZED=false
REVIEW_REQUEST_SENT=false
REVIEW_RESULT_CREATED=false
FORMAL_REVIEW_COMPLETE=false
RESIDUAL_RISK_ACCEPTED=false
CROSSWALK_ACCEPTED=false
AUTHORITY_DELEGATED=false
CS_G1_PASS=false
IMPLEMENTATION_AUTHORIZED=false
STANDARD_READY=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
```

## 11. Agent-readable answer（智能体可读答案）

```text
WHAT_IS_READY=Frozen three-session review protocol and result Schema
WHAT_IS_NOT_READY=Role acceptance, review execution, results, risk acceptance, crosswalk acceptance, CS-G1
CAN_SEND_MODEL_REQUESTS_NOW=false
WHY=CS-G1-ROLE-REVIEW-D01 has no explicit Human Option
WHAT_HAPPENS_AFTER_OPTION_A=Execute exactly three scoped qwen3.7-max reviews, preserve failures, then stop for Human freeze Decision
```
