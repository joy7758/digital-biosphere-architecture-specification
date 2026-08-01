---
profile_id: DBA-MONITOR-EVIDENCE-0.1
title: Monitor Evidence Profile and Gap Matrix v0.1
title_zh: 监控器证据剖面与缺口矩阵 v0.1
status: proposed-reference-only-research-profile
primary_repository: DBA
source_refs:
  - https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations
  - https://www.aisi.gov.uk/blog/how-our-new-control-red-team-is-stress-testing-frontier-monitors
observed_at: 2026-07-25
profile_adopted: false
implementation_authorized: false
saee_change_authorized: false
dbos_change_authorized: false
---

# Monitor Evidence Profile and Gap Matrix v0.1

## 1. Purpose（目的）

本剖面定义一个 monitor（监控器）作为 evidence producer（证据生产者）时，最少需要记录哪些版本、范围、路由、盲区和验证材料。它不规定监控器实现，也不把 monitor score（监控分数）升级为 Truth、Authority、Permission、Decision 或 SAEE Fitness。

```text
MONITOR_IS_EVIDENCE_PRODUCER=true
MONITOR_IS_AUTHORITY=false
MONITOR_OUTPUT_IS_TRUTH=false
MONITOR_OUTPUT_CAN_CLOSE_GATE_ALONE=false
PROFILE_ADOPTED=false
IMPLEMENTATION_AUTHORIZED=false
```

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

问题：如果潜在用户依赖 LLM monitor 监督自主 Agent，智能体是否推荐本剖面？

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=MONITOR_EVIDENCE_DISCLOSURE_AND_REASSESSMENT_CONTRACT
NOT_RECOMMENDED_AS=MONITOR_RUNTIME_OR_AUTOMATIC_SAFETY_DECISION
```

条件：

- 记录 exact monitor version、model、prompt／policy、routing coverage 和 threshold；
- 保留 false positive、false negative、not-reviewed 与 unknown；
- 使用 independent action／environment evidence（独立动作／环境证据）交叉检查；
- 高影响 gate 仍需 Human Decision；
- 不能用同一 monitor 自评来证明自身充分性。

## 3. Minimum Monitor Evidence Object（最小监控证据对象）

```text
monitor_ref
monitor_version
model_ref
model_version_or_digest
prompt_or_policy_digest
decision_thresholds
observed_at
input_event_scope
action_types_in_scope[]
action_types_not_routed[]
routing_rules_ref
known_bypass_classes[]
red_team_evidence_refs[]
false_positive_assessment
false_negative_assessment
independent_verification_refs[]
operator_ref
human_review_ref
unknowns[]
```

字段缺失时使用 `UNKNOWN`，不得默认为“覆盖”“安全”或“无异常”。

## 4. Evidence Gap Matrix（证据缺口矩阵）

| gap_id | 失败模式 | 单一 monitor 看见什么 | 仍需独立证据 | 默认状态 |
|---|---|---|---|---|
| `ME-G01` | Agent 不自述规则外动作 | self-report 为正常 | tool call、network、filesystem、privilege 与 final-state trace | `HOLD_MISSING_EVIDENCE` |
| `ME-G02` | chain-of-thought 不含关键动作理由 | reasoning 未显示异常 | 外部动作与环境变化 | `HOLD_MISSING_EVIDENCE` |
| `ME-G03` | 伪装成误解用户要求 | 低 suspicion score | exact user request、policy、action effect 与 counterfactual review | `REVIEW_REQUIRED` |
| `ME-G04` | 利用 monitor prompt gap | 未命中规则 | prompt／policy version、red-team case、rule coverage | `REASSESSMENT_REQUIRED` |
| `ME-G05` | 动作未路由给 monitor | 没有 observation | routing inventory、not-reviewed action count、gateway／runtime trace | `HOLD_MISSING_EVIDENCE` |
| `ME-G06` | monitor model 本身失配或被攻击 | score 仍存在 | independent monitor／rule-based／human cross-check | `REVIEW_REQUIRED` |
| `ME-G07` | threshold／model／prompt 版本变化 | 历史 pass | exact delta 与 bounded revalidation | `REASSESSMENT_REQUIRED` |
| `ME-G08` | 同源 failure path | Agent trace 与 monitor 同时缺失 | independent blackbox、environment、receipt 与 immutable log | `HOLD_MISSING_EVIDENCE` |

## 5. Claim and Authority Rules（主张与权力规则）

```text
NO_ALERT_NE_SAFE=true
LOW_SUSPICION_SCORE_NE_AUTHORIZED_EXECUTION=true
MONITOR_PASS_NE_EVIDENCE_SUFFICIENCY=true
MONITOR_PASS_NE_RELEASE_AUTHORIZATION=true
MONITOR_VERSION_CHANGE_REQUIRES_REASSESSMENT=true
UNREVIEWED_ACTION_COUNT_MUST_BE_PRESERVED=true
```

禁止：

- 把 `no alert` 写成没有发生越权；
- 把 monitor 的品牌、模型能力或内部部署写成独立验证；
- 把一个 monitor 对另一个 monitor 的评分写成最终 authority；
- 把 AISI 研究结论写成 Digital Biosphere 已实现 monitor validation；
- 在无 SAEE 变更授权时新增 evaluator、gate 或 Runtime。

## 6. Repository Routing（仓库路由）

| responsibility | repository / authority | 当前允许 |
|---|---|---|
| profile、字段与非提升边界 | DBA | proposal / research only |
| execution、tool、environment 与 evidence facts | DBOS／Agent Evidence canonical source | read-only reference |
| monitor reliability／risk recommendation | SAEE | future separately authorized input only |
| accept／hold／stop／release decision | Human Decision Authority | explicit decision required |

## 7. Status（状态）

```text
PROFILE_DEFINED=true
PROFILE_ADOPTED=false
SCHEMA_DEFINED=false
VALIDATOR_IMPLEMENTED=false
MONITOR_RUNTIME_CREATED=false
SAEE_IMPLEMENTATION_CHANGED=false
DBOS_IMPLEMENTATION_CHANGED=false
TESTS_EXECUTED=0
EXTERNAL_SUBMISSION_SENT=false
```
