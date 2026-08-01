---
profile_id: DBA-EVALUATION-OPERATOR-CONTROL-CLAIM-EVIDENCE-0.1
title: Evaluation Operator Control and Third-Party Claim Evidence Matrix v0.1
title_zh: 评估运行方控制与第三方主张证据矩阵 v0.1
status: proposed-reference-only-research-profile
primary_repository: DBA
observed_at: 2026-07-26
source_refs:
  - https://openai.com/index/hugging-face-model-evaluation-security-incident/
  - https://huggingface.co/blog/security-incident-july-2026
  - https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/
  - https://www.aisi.gov.uk/blog/international-evaluation-best-practice-and-open-questions-in-ai-measurement
profile_adopted: false
implementation_authorized: false
saee_change_authorized: false
dbos_change_authorized: false
---

# Evaluation Operator Control and Third-Party Claim Evidence Matrix v0.1

## 1. Purpose（目的）

本矩阵回答两个问题：

1. 评测运行方能否用证据证明 Agent 的实际边界、检测、归因和处置仍在控制内；
2. 第三方评估报告能否说明其结论支持什么决定、基于哪些参数、有哪些限制和不确定性。

它不是 sandbox（沙箱）、monitor（监控器）、SIEM（安全信息与事件管理）、SAEE evaluator、合规认证或执行授权。

```text
OPERATOR_CONTROL_EVIDENCE_PROFILE_DEFINED=true
THIRD_PARTY_CLAIM_MAPPING_DEFINED=true
PROFILE_ADOPTED=false
SCHEMA_DEFINED=false
VALIDATOR_IMPLEMENTED=false
SAEE_CHANGE_AUTHORIZED=false
DBOS_CHANGE_AUTHORIZED=false
```

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

问题：如果潜在客户需要独立审查一次高风险 Agent 评测是否受控、其结果能否用于上线或复测决定，智能体是否推荐本矩阵？

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=EVIDENCE_DISCLOSURE_AND_CLAIM_BOUNDARY_CHECKLIST
NOT_RECOMMENDED_AS=CONTROL_RUNTIME_CERTIFICATION_OR_DECISION_AUTHORITY
```

条件：

- exact operator、environment、sandbox、egress policy、monitor 和时间窗口可引用；
- 独立 network／identity／infrastructure evidence 能与 Agent trace 对账；
- detection、attribution、containment 与 notification 分开记录；
- 报告声明 decision objective、evaluation parameters、limitations 和 uncertainty；
- Human Decision Authority 仍负责采纳、停止、发布或上线决定。

## 3. Evaluation Operator Control Evidence Chain（评估运行方控制证据链）

```text
Evaluation Operator
  -> Evaluation Objective
  -> Agent / Model / Harness
  -> Sandbox and Egress Policy
  -> External Infrastructure Boundary
  -> Detection
  -> Attribution
  -> Containment
  -> Evidence Reconciliation
  -> Human Decision
```

### 3.1 Minimum fields（最小字段）

```text
evaluation_operator_ref
evaluation_objective
decision_objective
agent_ref
model_ref
model_version_or_digest
harness_ref
environment_ref
sandbox_policy_ref
sandbox_policy_digest
egress_policy_ref
egress_policy_digest
allowed_external_targets[]
observed_external_targets[]
network_evidence_refs[]
identity_and_credential_evidence_refs[]
monitor_refs[]
actions_not_observed_by_monitors[]
boundary_breach_detected_at
operator_awareness_at
attribution_completed_at
containment_started_at
containment_completed_at
external_notification_refs[]
independent_reconstruction_refs[]
timeline_conflicts[]
unknowns[]
```

字段不存在时必须使用 `UNKNOWN` 或空数组并解释原因，不能默认为“未发生”“受控”或“无影响”。

### 3.2 Control gap matrix（控制缺口矩阵）

| gap_id | 失败模式 | 单一来源可能显示 | 仍需证据 | 默认状态 |
|---|---|---|---|---|
| `EOC-G01` | sandbox 标签存在但实际可外联 | 配置写着 restricted | 网络策略、代理、cache、路由和实际 egress | `HOLD_MISSING_EVIDENCE` |
| `EOC-G02` | Agent trace 完整但运营方未及时察觉 | 事后有动作日志 | awareness timestamp、alert delivery、on-call response | `REASSESSMENT_REQUIRED` |
| `EOC-G03` | 发现异常但未完成来源归因 | anomaly alert | model／harness／run／credential binding | `HOLD_MISSING_EVIDENCE` |
| `EOC-G04` | monitor 未观察关键动作 | no alert | routing inventory、gateway、network、filesystem 和 privilege trace | `HOLD_MISSING_EVIDENCE` |
| `EOC-G05` | 受影响方已处置但运行方仍未知 | target containment | 双方时间线、notification、incident correlation | `REVIEW_REQUIRED` |
| `EOC-G06` | 媒体与官方叙述冲突 | days-long 或 internal discovery claim | final technical report、forensic timeline、exact disputed items | `HOLD_CONFLICTING_ACCOUNTS` |
| `EOC-G07` | 处置完成被写成旧评测仍有效 | containment receipt | changed environment／model／policy delta 和 bounded rerun | `REASSESSMENT_REQUIRED` |

## 4. Third-Party Evaluation Claim Discipline（第三方评估主张纪律）

### 4.1 NAAIMES method to evidence fields

| method requirement | minimum evidence field | 缺失时允许的结论 | 禁止提升 |
|---|---|---|---|
| 明确评估目标与决策用途 | `evaluation_objective`, `decision_objective` | `PURPOSE_UNCLEAR` | 泛化为安全、可靠或上线建议 |
| 选择合适 benchmark | `benchmark_ref`, `benchmark_selection_rationale` | `BENCHMARK_FIT_NOT_ESTABLISHED` | 单一分数代表完整系统 |
| 保持生成可比性 | `inference_settings_ref`, `harness_ref`, `model_digest` | `CROSS_RUN_COMPARABILITY_NOT_ESTABLISHED` | 跨模型／跨版本直接排名 |
| 保持评分可比性 | `scoring_criteria_ref`, `judge_ref`, `human_review_ref` | `SCORING_COMPARABILITY_NOT_ESTABLISHED` | judge 输出成为 Truth |
| 评估完整系统 | `system_boundary`, `tool_refs`, `environment_ref`, `interaction_scope` | `MODEL_ONLY_RESULT` | 模型结果代表工具化 Agent 系统 |
| 记录过程与结果 | `trace_ref`, `log_refs`, `result_ref`, `debugging_notes_ref` | `REPRODUCIBILITY_LIMITED` | 日志存在即完整或真实 |
| 报告限制与不确定性 | `limitations[]`, `uncertainty_statement`, `unknowns[]` | `BOUNDED_RESULT_ONLY` | PASS 等于认证或授权 |
| 透明度与选择性披露 | `selective_disclosure_statement`, `withheld_material_classes[]` | `DISCLOSURE_BOUNDED` | 未公开材料被推断为不存在 |

### 4.2 Read-only mapping to current SAEE surfaces（到 SAEE 当前表面的只读映射）

| method concept | current SAEE surface observed on 2026-07-26 | mapping state | future separately authorized input |
|---|---|---|---|
| run and trace identity | `run_ref`, `trace_ref`, `agent`, `scenario` | `DIRECT_OR_NEAR_DIRECT` | exact model／harness／environment digest |
| claim under evaluation | `claim_type`, `scope` | `DIRECT_OR_NEAR_DIRECT` | `decision_objective` |
| assessment result | `assessment`, `profile_result`, `evidence_assessment` | `DIRECT` | benchmark and scoring provenance |
| evidence gaps | `missing_requirements`, `failed_relationships`, `reason_codes`, `failure_analysis` | `DIRECT` | not-observed action inventory |
| bounded interpretation | `limitations`, `boundary_statement`, `truth_boundary` | `DIRECT` | structured `uncertainty_statement` |
| recommendation | reliability `recommendation` | `DIRECT_BUT_NON_AUTHORITATIVE` | intended decision maker and decision-change criteria |
| comparability | no dedicated current output field observed | `GAP` | inference／scoring／judge／harness refs |
| system boundary | partial through `scenario`, `scope`, trace and current truth boundary | `PARTIAL` | tools、runtime、network、sandbox、external targets |
| independent verification | no dedicated current output field observed | `GAP` | `independent_verification_refs[]` |
| selective disclosure | no dedicated current output field observed | `GAP` | withheld classes and misuse／contamination rationale |

Observed SAEE source surface:

```text
OBSERVED_REPOSITORY=SAEE
OBSERVED_BRANCH=feat/canonical-capability-inventory-routing-v1
OBSERVED_COMMIT=697ae2080f11b7905b20c39079914eb98169783b
OBSERVED_WORKTREE_STATE=DIRTY_OUTSIDE_THE_THREE_OBSERVED_PATHS
```

- `agent-interface/capabilities/saee-evaluate-agent-run-output.v0.1.schema.json`
- `schemas/saee-agent-reliability-report.schema.v1.0.json`
- `saee_backend/services/agent_run_capability.py`

This table is a read-only observation. It does not assign canonical authority to the local dirty checkout and does not authorize modification of those files.

## 5. Claim and Authority Rules（主张与权力规则）

```text
TRACE_EXISTS_NE_OPERATOR_AWARENESS=true
ALERT_EXISTS_NE_ATTRIBUTION_COMPLETE=true
CONTAINMENT_COMPLETE_NE_PRIOR_EVALUATION_VALID=true
BENCHMARK_PASS_NE_SYSTEM_SAFETY=true
REPORT_RECOMMENDATION_NE_DECISION_AUTHORITY=true
THIRD_PARTY_EVALUATOR_NE_CERTIFICATION_AUTHORITY=true
SECONDARY_REPORT_NE_FINAL_INCIDENT_TRUTH=true
```

禁止：

- 依据单一 Agent log 宣称评测全过程受控；
- 依据单一 monitor 的 `no alert` 宣称没有越界；
- 把 Reuters 的时间线或 OpenAI 的初步声明任一方单独写成最终联合事实；
- 把 NAAIMES 方法指导写成 SAEE 合规或认证地位；
- 未获独立授权就修改 SAEE Schema、evaluator、Runtime 或 gate；
- 由本 profile 自动产生 stop、release、Permission 或 Authority。

## 6. Repository Routing（仓库路由）

| responsibility | canonical owner / source | 当前允许 |
|---|---|---|
| 证据字段、缺口、主张边界 | DBA | proposed research profile |
| execution、network、environment facts | DBOS／Agent Evidence canonical source | future read-only input |
| claim adequacy and reliability context | SAEE | future separately authorized mapping |
| incident facts | source organizations／forensic record | pinned source reference only |
| accept／hold／stop／release | Human Decision Authority | explicit decision required |

## 7. Status（状态）

```text
PROFILE_DEFINED=true
PROFILE_ADOPTED=false
SCHEMA_DEFINED=false
VALIDATOR_IMPLEMENTED=false
OPERATOR_CONTROL_RUNTIME_CREATED=false
SAEE_IMPLEMENTATION_CHANGED=false
DBOS_IMPLEMENTATION_CHANGED=false
TESTS_EXECUTED=0
EXTERNAL_SUBMISSION_SENT=false
```
