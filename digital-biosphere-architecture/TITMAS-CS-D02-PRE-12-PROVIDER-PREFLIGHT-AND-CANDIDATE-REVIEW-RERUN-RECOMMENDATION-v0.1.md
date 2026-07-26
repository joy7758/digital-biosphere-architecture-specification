---
document_id: DBA-TITMAS-CS-D02-PRE-12-PROVIDER-PREFLIGHT-AND-CANDIDATE-REVIEW-RERUN-RECOMMENDATION-0.1
title: TITMAS PRE-12 Provider Preflight and Candidate Review Rerun Recommendation v0.1
title_zh: TITMAS PRE-12 Provider 预检与候选记录审查重跑建议 v0.1
version: 0.1.0
status: EXACT_TWO_STAGE_RERUN_RECOMMENDATION_PREPARED_NOT_DECIDED
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_candidate: CS-D02-PRE-12
primary_repository: digital-biosphere-architecture
recommendation: AUTHORIZE_TWO_PROVIDER_PREFLIGHT_THEN_CONDITIONAL_FOUR_SESSION_CANDIDATE_REVIEW_RERUN_ONLY
live_model_requests_recommended_max: 6
live_model_requests_authorized: false
implementation_effect: none
commercial_effect: none
authority_effect: none
---

# TITMAS PRE-12 Provider Preflight and Candidate Review Rerun Recommendation v0.1

中文：TITMAS PRE-12 Provider 预检与候选记录审查重跑建议 v0.1。

## 1. Agent Recommendation Gate（智能体推荐闸门）

```text
AGENT_RECOMMENDATION=RECOMMENDED_WITH_STRICT_PRECONDITIONS
RECOMMENDED_AS=TWO_STAGE_PROVIDER_PREFLIGHT_AND_BOUNDED_AGENT_RECORD_REVIEW
NOT_RECOMMENDED_AS=BLIND_RETRY_RECORD_VALIDATION_COUNTING_OR_MARKET_PROOF
```

如果潜在 Agent developer 需要复现多 provider 记录审查，我会推荐先执行独立、最小的
provider preflight（Provider 预检），只有两条路径都证明当前 request/response contract
可用后，才执行候选记录审查。这样能把 provider-path failure 与 record-review judgment
分开，避免再次消耗全部审查会话却得不到任何可解释输出。

我不会推荐直接重复 PRE-10：PRE-10 四个请求额度已经消耗，且 PRE-11 只证明了当前公开
契约和一个 DeepSeek model identifier drift（模型标识漂移），没有证明 Qianfan timeout
或 DeepSeek HTTP 400 的确切原因。

## 2. Direct Evidence（直接证据）

- PRE-10 remote failure baseline：
  `04a66365e62a8f9645ca33ece70926f51e8c07eb`；
- PRE-11 offline diagnostic result baseline：
  `5efabf72837d6fa57ab3666584c3816b110e1413`；
- Qianfan 当前官方文档和已安装工具均继续声明 `kimi-k2.6`，但工具内部 envelope、
  timeout 与 transport 行为不可见；
- DeepSeek 当前官方 Chat Completion 文档列出 `deepseek-v4-flash` 和
  `deepseek-v4-pro`，PRE-10 的 `deepseek-chat` 不在当前枚举；
- DeepSeek JSON mode 仍要求 request 使用 `response_format=json_object`，同时 prompt
  明确要求 JSON；
- PRE-09 四条候选仍为 `PARTIAL`；`VALID=0`、counting 未授权、`CS-G0=false`。

## 3. Exact Recommended Action（精确推荐动作）

建议未来建立独立 `CS-D02-PRE-12` Decision，只授权下面一个原子化的两阶段执行：

```text
ACTION=TWO_PROVIDER_PREFLIGHT_THEN_CONDITIONAL_FOUR_SESSION_CANDIDATE_REVIEW_RERUN
PRIMARY_REPOSITORY=digital-biosphere-architecture
STAGE_A_PREFLIGHT_REQUESTS_MAX=2
STAGE_B_REVIEW_REQUESTS_MAX=4
TOTAL_LIVE_MODEL_REQUESTS_MAX=6
RETRY_MAX=0
FALLBACK_MAX=0
JSON_REPAIR_MAX=0
TOOLS_ALLOWED=false
NEW_SOURCE_SEARCH=false
NEW_SOURCE_COLLECTION=false
```

### Stage A: provider-specific preflight

只允许两个最小、无候选内容的 contract preflight：

| Session | Provider path | Model | Request cap | Required result |
|---|---|---|---:|---|
| `QF-KIMI-PREFLIGHT-PRE12-P1` | installed Qianfan/Kimi tool | fixed `kimi-k2.6` | 1 | parseable JSON matching the frozen preflight Schema |
| `DS-V4PRO-PREFLIGHT-PRE12-P2` | reviewed DeepSeek direct path | `deepseek-v4-pro` | 1 | HTTP success plus parseable JSON matching the frozen preflight Schema |

Preflight prompt 只验证当前路径能否返回指定的最小 JSON shape，不包含四条候选、市场问题、
TITMAS 价值判断或审查结论。Preflight 输出不能计入 record-review threshold、模型意见、
候选覆盖或有效问题记录。

进入 Stage B 的必要条件：

```text
PREFLIGHT_REQUESTS_EXECUTED=2
PREFLIGHT_PARSEABLE_RESPONSES=2
PREFLIGHT_PROVIDERS_WITH_SUCCESS=2
PREFLIGHT_SCHEMA_FAILURES=0
PREFLIGHT_BOUNDARY_FAILURES=0
```

任一条件不满足，立即停止，Stage B 请求数必须为 `0`。

### Stage B: bounded candidate record review

只有 Stage A 全部通过后，才执行四个固定角色会话：

| Session | Provider / model | Reviewer role | Request cap |
|---|---|---|---:|
| `QF-KIMI-SOURCE-PFPC-R1` | Qianfan / `kimi-k2.6` | `SOURCE_QUALIFICATION_REVIEWER` | 1 |
| `QF-KIMI-ACCOUNTABILITY-PFPC-R2` | Qianfan / `kimi-k2.6` | `ACCOUNTABILITY_RELEVANCE_REVIEWER` | 1 |
| `DS-V4PRO-CLAIM-PRIVACY-PFPC-R3` | DeepSeek / `deepseek-v4-pro` | `CLAIM_AND_PRIVACY_REVIEWER` | 1 |
| `DS-V4PRO-ADVERSARIAL-PFPC-R4` | DeepSeek / `deepseek-v4-pro` | `ADVERSARIAL_RECORD_REVIEWER` | 1 |

Stage B 必须继续绑定 PRE-09 exact candidate set，以及 PRE-10 的 public-safe source pack、
review prompt semantics 和 response contract。新计划必须重新计算并冻结所有实际字节
digest，不得在执行时使用未约束的 `latest`。

Stage B 保留 PRE-10 原阈值，不降低：

```text
REVIEW_PARSEABLE_SESSIONS_MIN=3
REVIEW_PROVIDERS_WITH_SUCCESS_MIN=2
REVIEW_CANDIDATE_IDS_COVERED_MIN=4
REVIEW_BOUNDARY_FAILURES_MAX=0
```

Stage A 的两个 preflight 不得计入以上四项阈值。

## 4. Preconditions（前置条件）

- PRE-10 与 PRE-11 commits 必须保持 local = remote；
- 建立独立 PRE-12 Decision/Authorization Record；
- 建立新的 machine-readable execution plan 与 Schema；
- 分别冻结 preflight prompt、preflight response Schema、candidate-review prompt、
  candidate-review response Schema、source pack、candidate set、model identifiers、session
  IDs、阈值和请求上限；
- 明确 Qianfan 使用已安装的一字段工具路径；DeepSeek 使用已审查的 current model
  identifier 与 JSON request contract；
- 在任何 live request 前 commit/push 授权基线并验证 local = remote；
- 只允许 public-safe inputs，不读取、显示或写入 API key；
- 结果格式必须预先定义成功、失败、未知、未执行和停止位置。

## 5. Required Outputs（要求输出）

若未来获准执行，只允许形成：

- PRE-12 frozen execution plan、Schema 和 authorization baseline receipt；
- 两条 sanitized preflight observations；
- 在 Stage A 通过时最多四条 sanitized candidate-review observations；
- deterministic threshold result；
- execution receipt，必须保留 consumed、not-executed、failure 和 stop reason；
- human-readable result report；
- path-scoped commit/push receipt。

不得保存 API key、Authorization header、Cookie、raw provider body、直接个人标识符或
客户数据。

## 6. Stop Conditions（停止条件）

任一条件发生即失败关闭：

- PRE-12 authorization baseline 未远端验证；
- 实际 model、endpoint、prompt、Schema、source pack、candidate set、阈值或请求上限与
  冻结计划不一致；
- 任一 provider preflight 未成功、不可解析、Schema 不合格或产生边界违规；
- Stage A 未通过却试图开始 Stage B；
- 任何 session 试图 retry、fallback、调用工具或修复 JSON；
- 需要读取、显示、复制或持久化真实 API key 或 raw provider body；
- 任何模型回答试图直接赋予 `VALID`、执行 counting、关闭 `CS-G0` 或产生商业结论；
- 任何结果试图覆盖 PRE-10 或 PRE-11 历史。

## 7. Post-run Governance Boundary（执行后治理边界）

即使 Stage A 和 Stage B 全部通过，结果也只能成为 independent Agent record review
input（独立智能体记录审查输入）。每条候选是否进入 counting 仍需要既有治理合同要求的
独立决定；模型不能自我批准。

```text
AGENT_REVIEW_RESULT_NE_VALID_RECORD=true
VALID_RECORD_NE_COUNTED_RECORD=true
COUNTED_RECORD_NE_CS_G0_PASS=true
PROBLEM_SIGNAL_NE_CUSTOMER_ADOPTION=true
```

## 8. Standing Directive Eligibility（常设授权适用性）

本建议提供 exact action、primary repository、preconditions、false effects 和 fail-closed
stop rules，但 live provider requests 是 materially different action（实质不同动作）。
因此当前只达到：

```text
RECOMMENDATION_READY_FOR_BOUNDED_DECISION=true
STANDING_DIRECTIVE_ELIGIBILITY=REVIEW_REQUIRED
```

只有在独立 Decision、冻结计划、Schema 和远端授权基线完成后，才能把 live request
authorization 写为 true。

## 9. False Effects（非效果）

```text
PRE_12_DECIDED=false
PRE_12_EXECUTION_AUTHORIZED=false
LIVE_MODEL_REQUESTS_AUTHORIZED=false
PREFLIGHT_EXECUTED=false
CANDIDATE_REVIEW_RERUN_EXECUTED=false
PRE_10_HISTORY_CHANGED=false
PRE_11_HISTORY_CHANGED=false
CANDIDATE_STATUS_CHANGED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
