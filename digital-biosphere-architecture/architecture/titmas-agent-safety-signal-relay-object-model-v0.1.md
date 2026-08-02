---
spec_id: TITMAS-AGENT-SAFETY-SIGNAL-RELAY-OBJECT-MODEL-0.1
title: TITMAS Agent Safety Signal Relay Minimum Object Model v0.1
title_zh: TITMAS 智能体安全信号中继最小对象模型 v0.1
status: ACCEPTED_ARCHITECTURE_SPECIFICATION_P2
normative: true
schema_status: SPECIFICATION_ONLY_SCHEMA_NOT_CREATED
implementation_status: NOT_IMPLEMENTED
primary_repository: digital-biosphere-architecture
decision_ref: ADR-040
---

# TITMAS 智能体安全信号中继最小对象模型 v0.1

## 1. Scope and invariants（范围与不变量）

本规范冻结六类对象的语义、字段、认识状态、披露 ceiling 和不等同关系。它不创建 JSON
Schema、数据库、API、matcher、CLI、服务或信号实例。

```text
OBJECT_COUNT=6
GLOBAL_PUBLISHER_TRUST_SCORE_ALLOWED=false
APPLICABILITY_AND_LOCAL_TEST_RESULT_SEPARATED=true
RAW_PRIVATE_TRAJECTORY_REQUIRED=false
LOCAL_MATCHING_PREFERRED=true
```

所有 assertion 必须标注：

```text
OBSERVED
INFERRED
REPRODUCED
VALIDATED
```

较高状态不得由 LLM、票数或发布者自报自动产生；必须带对应 evidence/verification refs 和
limitations。缺失时保持实际较低状态或 unknown。

## 2. Common types（公共类型）

### 2.1 Cause status（原因状态）

```text
ACCIDENTAL
ADVERSARIAL
ENVIRONMENTAL_DRIFT
SYSTEMIC_DESIGN_FAULT
UNKNOWN_CAUSE
```

`UNKNOWN_CAUSE` 是证据不足时的默认值。观察到攻击路径、相似名称或可被利用的弱点，不等于
已证明 `ADVERSARIAL`。原因改变必须形成新 assertion/revision，保留旧判断。

### 2.2 Applicability outcome（适用性结果）

`ApplicabilityAssessment.outcome` 只允许：

```text
POSSIBLY_AFFECTED
NOT_AFFECTED
UNKNOWN
```

它只回答结构化受影响条件是否与给定 profile/context 相容，不回答本地风险是否已发生。

### 2.3 Local validation result（本地验证结果）

本地测试结果只允许：

```text
CONFIRMED_AFFECTED
TESTED_NOT_REPRODUCED
TEST_INCONCLUSIVE
NOT_TESTED
```

本地结果属于 `ValidationFeedback`；不得写入或替代 `ApplicabilityAssessment.outcome`。
`TESTED_NOT_REPRODUCED` 只对 exact profile/test/context 有效，不自动产生全局 `NOT_AFFECTED`。

### 2.4 Beneficial capability（正向能力）

`beneficial_capability.category` 只允许：

```text
DETECTION_CAPABILITY
RECOVERY_CAPABILITY
DEFENSIVE_CONTROL
ISOLATION_MEASURE
SAFETY_CANDIDATE_DISCOVERY
```

每项必须记录 `direct_causal_link_to_incident`。不得扩展为通用技能、工具推荐、商业机会、
人才/项目发现、能力市场或与异常无直接因果关系的功能。

### 2.5 Disclosure levels（披露等级）

```text
PUBLIC_DEFENSIVE
RESTRICTED_VALIDATION
PRIVATE_EVIDENCE
LOCAL_ONLY
```

字段表中的 `maximum_permitted_disclosure` 是默认最宽允许范围：

- `PUBLIC_DEFENSIVE`：脱敏后可进入公开防御信号；
- `RESTRICTED_VALIDATION`：只给经策略接受的验证者/接收者；
- `PRIVATE_EVIDENCE`：只在证据 Owner 的受控域内保存或按引用访问；
- `LOCAL_ONLY`：不得离开接收方/提交方本地环境。

实例策略可以收紧，绝不能放宽。字段值一旦包含更敏感内容，必须提升为更严格等级或删除/摘要。

### 2.6 Publisher assurance and local trust（发布者保证与本地信任）

`publisher_assurance` 是结构化记录，不是分数：

| field | semantics | maximum_permitted_disclosure |
|---|---|---|
| `publisher_ref` | stable publisher reference | `PUBLIC_DEFENSIVE` |
| `identity_binding_method` | DBOS/external verified binding method ref | `PUBLIC_DEFENSIVE` |
| `proof_refs` | proofs or verification receipts, not raw keys | `RESTRICTED_VALIDATION` |
| `assurance_level` | declared bounded level/policy enum | `PUBLIC_DEFENSIVE` |
| `policy_ref` | exact assurance policy/version | `PUBLIC_DEFENSIVE` |
| `verified_at` | verification time and source | `PUBLIC_DEFENSIVE` |
| `limitations` | unknown/conflict/expiry limitations | `PUBLIC_DEFENSIVE` |

禁止字段：`global_trust_score`、`reputation_score`、`trusted_publisher_rank`。

`recipient_local_trust_decision` 由接收方本地策略生成并默认 `LOCAL_ONLY`：

```text
TRUST_FOR_LOCAL_VALIDATION
DO_NOT_TRUST
REQUIRES_LOCAL_REVIEW
NOT_DECIDED
```

Relay 和 Publisher 不得设置、覆盖或推断该值。

## 3. Object 1 — IncidentCaseSubmission

用途：提交异常案例和最小证据引用；提交不等于 admission、复现或发布。

| field | required | semantics | maximum_permitted_disclosure |
|---|---:|---|---|
| `object_type` | yes | constant `IncidentCaseSubmission` | `PUBLIC_DEFENSIVE` |
| `schema_version` | yes | exact contract version | `PUBLIC_DEFENSIVE` |
| `case_id` | yes | stable submission ID, not Evidence ID | `PUBLIC_DEFENSIVE` |
| `submitted_at` | yes | time + source | `PUBLIC_DEFENSIVE` |
| `submitter_ref` | yes | stable actor ref | `RESTRICTED_VALIDATION` |
| `submitter_proof_refs` | yes | assurance refs, no secrets | `RESTRICTED_VALIDATION` |
| `incident_time_range` | yes | bounded known/estimated range | `RESTRICTED_VALIDATION` |
| `observations` | yes | assertion list, initially `OBSERVED` | `RESTRICTED_VALIDATION` |
| `cause_status` | yes | five-value enum; default unknown | `PUBLIC_DEFENSIVE` |
| `cause_assertion_status` | yes | epistemic status of cause | `PUBLIC_DEFENSIVE` |
| `environment_summary` | yes | minimized runtime/tool/permission classes | `RESTRICTED_VALIDATION` |
| `evidence_refs` | yes | external evidence/material refs | `PRIVATE_EVIDENCE` |
| `evidence_digests` | yes | exact digest and scope | `RESTRICTED_VALIDATION` |
| `verification_receipt_refs` | no | `agent-evidence`/DBOS/other bounded refs | `RESTRICTED_VALIDATION` |
| `raw_local_paths` | no | local evidence locations | `LOCAL_ONLY` |
| `secrets_or_credentials` | prohibited | must never be submitted | `LOCAL_ONLY` |
| `redaction_record` | yes | removed/generalized fields and reason | `RESTRICTED_VALIDATION` |
| `consent_or_authorization_refs` | when required | collection/use authority refs | `PRIVATE_EVIDENCE` |
| `limitations` | yes | sampling, clock, missing context, conflicts | `RESTRICTED_VALIDATION` |
| `requested_disposition` | yes | `REVIEW_ONLY|REPRODUCTION_REQUESTED` | `RESTRICTED_VALIDATION` |

## 4. Object 2 — AgentSafetySignal

用途：表达有界、版本化、可纠正/过期/撤回的安全声明。

| field | required | semantics | maximum_permitted_disclosure |
|---|---:|---|---|
| `object_type` | yes | constant `AgentSafetySignal` | `PUBLIC_DEFENSIVE` |
| `schema_version` | yes | exact schema version | `PUBLIC_DEFENSIVE` |
| `signal_id` | yes | stable ID independent from title/alias | `PUBLIC_DEFENSIVE` |
| `signal_version` | yes | immutable version | `PUBLIC_DEFENSIVE` |
| `status` | yes | `DRAFT|CANDIDATE|VALIDATED_BOUNDED|ACTIVE|UPDATED|CORRECTED|EXPIRED|REVOKED` | `PUBLIC_DEFENSIVE` |
| `title` | yes | concise defensive title | `PUBLIC_DEFENSIVE` |
| `summary` | yes | non-executable public-safe summary | `PUBLIC_DEFENSIVE` |
| `publisher_assurance` | yes | structured assurance, never score | `PUBLIC_DEFENSIVE` |
| `case_refs` | yes | source case refs; public IDs may be pseudonymous | `RESTRICTED_VALIDATION` |
| `evidence_refs` | yes | redacted/public or restricted refs only | `RESTRICTED_VALIDATION` |
| `evidence_assurance` | yes | admission/verification state + limitations | `PUBLIC_DEFENSIVE` |
| `assertions` | yes | each carries epistemic status | `PUBLIC_DEFENSIVE` |
| `cause_status` | yes | five-value enum | `PUBLIC_DEFENSIVE` |
| `cause_assertion_status` | yes | evidence state of cause classification | `PUBLIC_DEFENSIVE` |
| `broken_assumptions` | yes | exact system assumptions and scope | `PUBLIC_DEFENSIVE` |
| `beneficial_capabilities` | yes | restricted five-category list + causal link | `PUBLIC_DEFENSIVE` |
| `attack_paths` | yes | defensive abstraction; exploit details may be restricted | `RESTRICTED_VALIDATION` |
| `affected_conditions` | yes | typed required/any predicates | `PUBLIC_DEFENSIVE` |
| `exclusion_conditions` | yes | conditions supporting `NOT_AFFECTED` | `PUBLIC_DEFENSIVE` |
| `unknown_conditions` | yes | unresolved predicates and impact | `PUBLIC_DEFENSIVE` |
| `detection_advice` | yes | non-executable test descriptions | `PUBLIC_DEFENSIVE` |
| `disposition_advice` | yes | non-executable local policy options | `PUBLIC_DEFENSIVE` |
| `prohibited_action_types` | yes | command/tool-call/auto-fix forbidden | `PUBLIC_DEFENSIVE` |
| `issued_at` | when published | publisher time + source | `PUBLIC_DEFENSIVE` |
| `not_before` | when published | validity start | `PUBLIC_DEFENSIVE` |
| `expires_at` | when published | mandatory finite validity | `PUBLIC_DEFENSIVE` |
| `supersedes` | no | predecessor version refs | `PUBLIC_DEFENSIVE` |
| `correction_or_revocation_refs` | no | lifecycle refs | `PUBLIC_DEFENSIVE` |
| `content_digest` | yes | exact object digest scope | `PUBLIC_DEFENSIVE` |
| `signature_envelope_ref` | when published | DSSE/in-toto or future approved envelope | `PUBLIC_DEFENSIVE` |
| `disclosure_manifest` | yes | per-field actual disclosure classifications | `PUBLIC_DEFENSIVE` |
| `limitations` | yes | coverage, independence, trust and context limits | `PUBLIC_DEFENSIVE` |

`AgentSafetySignal` 不得内嵌 `PRIVATE_EVIDENCE` 或 `LOCAL_ONLY` 字段值。若必须引用，使用受控
reference + digest + access policy，不复制原始内容。

## 5. Object 3 — AgentExposureProfile

用途：描述接收智能体是否具有受影响条件。完整画像默认本地保存；Relay 只接收最小化谓词。

| field | required | semantics | maximum_permitted_disclosure |
|---|---:|---|---|
| `object_type` | yes | constant `AgentExposureProfile` | `RESTRICTED_VALIDATION` |
| `schema_version` | yes | exact version | `RESTRICTED_VALIDATION` |
| `profile_id` | yes | local or pseudonymous stable ID | `RESTRICTED_VALIDATION` |
| `profile_digest` | yes | exact minimized profile digest | `RESTRICTED_VALIDATION` |
| `subject_stable_ref` | local yes | DBOS/external stable identity ref | `LOCAL_ONLY` |
| `subject_proof_refs` | local yes | identity binding proof refs | `LOCAL_ONLY` |
| `identity_binding_method` | yes | method class/version, not secrets | `RESTRICTED_VALIDATION` |
| `capability_classes` | yes | minimized capability predicates | `RESTRICTED_VALIDATION` |
| `runtime_name_version` | yes | exact or bounded runtime version | `RESTRICTED_VALIDATION` |
| `tool_classes` | yes | classes by side-effect, not secrets | `RESTRICTED_VALIDATION` |
| `tool_inventory` | no | exact local tool names/endpoints | `LOCAL_ONLY` |
| `permission_classes` | yes | summarized read/write/execute/network classes | `RESTRICTED_VALIDATION` |
| `permission_details` | no | exact scopes/accounts/resources | `LOCAL_ONLY` |
| `resolver_behavior` | yes | candidate/binding/ambiguity behavior predicates | `RESTRICTED_VALIDATION` |
| `context_manifest_digest` | yes | exact assessment context | `RESTRICTED_VALIDATION` |
| `context_valid_until` | yes | invalidation boundary | `RESTRICTED_VALIDATION` |
| `local_policy_ref` | local yes | recipient trust/action policy | `LOCAL_ONLY` |
| `recipient_local_trust_decision` | local yes | local four-value decision | `LOCAL_ONLY` |
| `disclosed_predicates` | when remote match | only predicates released to Relay | `RESTRICTED_VALIDATION` |
| `unknown_fields` | yes | missing/withheld/unresolvable fields | `RESTRICTED_VALIDATION` |
| `limitations` | yes | self-attested/proof-backed distinctions | `RESTRICTED_VALIDATION` |

## 6. Object 4 — ApplicabilityAssessment

用途：对 exact signal/profile/matcher/context 做确定性三值条件评估。它不是本地测试结果。

| field | required | semantics | maximum_permitted_disclosure |
|---|---:|---|---|
| `object_type` | yes | constant `ApplicabilityAssessment` | `RESTRICTED_VALIDATION` |
| `schema_version` | yes | exact version | `RESTRICTED_VALIDATION` |
| `assessment_id` | yes | stable result ID | `RESTRICTED_VALIDATION` |
| `signal_id_version_digest` | yes | immutable signal input | `RESTRICTED_VALIDATION` |
| `profile_id_digest` | yes | minimized profile input | `RESTRICTED_VALIDATION` |
| `matcher_spec_version` | yes | normative matcher specification only in P2 | `PUBLIC_DEFENSIVE` |
| `context_manifest_digest` | yes | execution/assessment context | `RESTRICTED_VALIDATION` |
| `outcome` | yes | only three applicability values | `RESTRICTED_VALIDATION` |
| `matched_predicates` | yes | satisfied affected conditions | `RESTRICTED_VALIDATION` |
| `unmatched_predicates` | yes | explicit non-matches | `RESTRICTED_VALIDATION` |
| `unknown_predicates` | yes | absent/withheld/conflicted inputs | `RESTRICTED_VALIDATION` |
| `exclusion_predicates` | yes | exclusions considered | `RESTRICTED_VALIDATION` |
| `reason_codes` | yes | deterministic bounded reasons | `RESTRICTED_VALIDATION` |
| `recommended_test_refs` | yes | non-executable test specification refs | `PUBLIC_DEFENSIVE` |
| `recipient_local_trust_decision` | local only | recipient-owned; Relay must not set | `LOCAL_ONLY` |
| `local_validation_result` | prohibited | belongs only to ValidationFeedback | `LOCAL_ONLY` |
| `assessed_at` | yes | time + source | `RESTRICTED_VALIDATION` |
| `valid_until` | yes | context expiry | `RESTRICTED_VALIDATION` |
| `limitations` | yes | matcher/profile/withholding limits | `RESTRICTED_VALIDATION` |

## 7. Object 5 — ValidationFeedback

用途：接收方提交最小本地测试结果和证据回执引用；不是投票、声誉或自动信号更新。

| field | required | semantics | maximum_permitted_disclosure |
|---|---:|---|---|
| `object_type` | yes | constant `ValidationFeedback` | `RESTRICTED_VALIDATION` |
| `schema_version` | yes | exact version | `RESTRICTED_VALIDATION` |
| `feedback_id` | yes | stable feedback ID | `RESTRICTED_VALIDATION` |
| `signal_id_version_digest` | yes | tested signal | `RESTRICTED_VALIDATION` |
| `assessment_ref` | yes | preceding applicability result | `RESTRICTED_VALIDATION` |
| `recipient_pseudonymous_ref` | yes | deduplication ref, not global identity score | `RESTRICTED_VALIDATION` |
| `recipient_assurance` | yes | proof-backed/self-attested + limitations | `RESTRICTED_VALIDATION` |
| `profile_digest` | yes | exact minimized profile | `RESTRICTED_VALIDATION` |
| `context_manifest_digest` | yes | exact test context | `RESTRICTED_VALIDATION` |
| `test_spec_refs` | yes | approved non-executable tests | `PUBLIC_DEFENSIVE` |
| `test_result` | yes | only four local validation values | `RESTRICTED_VALIDATION` |
| `result_reason_codes` | yes | deterministic/local reasons | `RESTRICTED_VALIDATION` |
| `verification_receipt_refs` | when tested | external receipts, not raw evidence | `PRIVATE_EVIDENCE` |
| `raw_test_output` | no | raw logs/traces | `LOCAL_ONLY` |
| `redacted_result_summary` | no | safe bounded summary | `RESTRICTED_VALIDATION` |
| `cause_observation` | no | does not override signal cause | `RESTRICTED_VALIDATION` |
| `submitted_at` | yes | time + source | `RESTRICTED_VALIDATION` |
| `retention_class` | yes | P3 policy class | `RESTRICTED_VALIDATION` |
| `limitations` | yes | environment, coverage, non-reproduction limits | `RESTRICTED_VALIDATION` |

反馈聚合必须按 assurance、独立性和 context 分层；禁止 `N votes => trusted` 或自动更新全局分数。

## 8. Object 6 — SignalLifecycleRecord

用途：append-only 记录发布、更新、纠正、过期、撤回，不删除历史。

| field | required | semantics | maximum_permitted_disclosure |
|---|---:|---|---|
| `object_type` | yes | constant `SignalLifecycleRecord` | `PUBLIC_DEFENSIVE` |
| `schema_version` | yes | exact version | `PUBLIC_DEFENSIVE` |
| `lifecycle_record_id` | yes | append-only record ID | `PUBLIC_DEFENSIVE` |
| `signal_id` | yes | stable signal lifecycle | `PUBLIC_DEFENSIVE` |
| `signal_version` | yes | version affected | `PUBLIC_DEFENSIVE` |
| `sequence` | yes | strictly increasing sequence | `PUBLIC_DEFENSIVE` |
| `previous_record_ref_digest` | except genesis | predecessor continuity | `PUBLIC_DEFENSIVE` |
| `event` | yes | `PUBLISHED|UPDATED|CORRECTED|EXPIRED|REVOKED` | `PUBLIC_DEFENSIVE` |
| `reason_codes` | yes | bounded lifecycle reasons | `PUBLIC_DEFENSIVE` |
| `reason_summary` | yes | non-sensitive public explanation | `PUBLIC_DEFENSIVE` |
| `private_reason_refs` | no | sensitive investigation/evidence refs | `PRIVATE_EVIDENCE` |
| `effective_at` | yes | effective time + source | `PUBLIC_DEFENSIVE` |
| `expires_at` | when applicable | finite expiry | `PUBLIC_DEFENSIVE` |
| `issuer_assurance` | yes | issuer/recovery role assurance | `PUBLIC_DEFENSIVE` |
| `superseding_signal_ref` | update/correction | exact next version | `PUBLIC_DEFENSIVE` |
| `signature_envelope_ref` | published events | signed lifecycle event | `PUBLIC_DEFENSIVE` |
| `delivery_cursor` | yes | monotonic public feed cursor | `PUBLIC_DEFENSIVE` |
| `recipient_delivery_receipts` | no | pseudonymous minimal receipts | `RESTRICTED_VALIDATION` |
| `limitations` | yes | clock, delivery, mirror, key limitations | `PUBLIC_DEFENSIVE` |

## 9. Cross-object constraints（跨对象约束）

1. `IncidentCaseSubmission` 不得直接创建 `ACTIVE` signal；必须经过 P3 gates。
2. `AgentSafetySignal.publisher_assurance` 不得生成或覆盖 recipient local trust。
3. `ApplicabilityAssessment.outcome` 与 `ValidationFeedback.test_result` 永远是两个字段、两个阶段。
4. `NOT_AFFECTED` 必须有满足的 exclusion 或明确的 required-condition non-match；资料缺失只能
   `UNKNOWN`。
5. `CONFIRMED_AFFECTED` 只来自本地测试结果，不改变其他接收方的适用性。
6. cause status 与 attack path 分离；存在 attack path 不得自动标为 `ADVERSARIAL`。
7. beneficial capability 必须通过受限枚举和直接因果链接；否则 schema/policy 拒绝。
8. correction/revocation 追加 `SignalLifecycleRecord`，不得覆盖或删除旧 object bytes。
9. 对象名称/alias 只用于 discovery；binding 必须使用 stable ref + proof result。
10. 任何 context digest/version 变化都使既有 applicability/local result 进入重新评估状态。
11. 在 `ASSR-OI-010` 解决前，任何 ARO audit receipt/reference 必须标记
    `UNVERIFIED_CONTEXT`；它不得提高 evidence/publisher/recipient assurance，不得单独满足
    reproduction 或 publication gate。

## 10. Synthetic example（合成规范示例）

```yaml
object_type: AgentSafetySignal
schema_version: "0.1"
signal_id: "urn:titmas:safety-signal:synthetic:fuzzy-resolution-hijacking"
signal_version: 1
status: CANDIDATE
cause_status: ACCIDENTAL
cause_assertion_status: OBSERVED
broken_assumptions:
  - "name_or_alias_is_unique_and_sufficient_for_binding"
beneficial_capabilities:
  - category: SAFETY_CANDIDATE_DISCOVERY
    direct_causal_link_to_incident: "typo exposed the need for candidate recovery"
affected_conditions:
  - "resolver.alias_used_as_binding_key == true"
  - "stable_identity_proof_verified != true"
exclusion_conditions:
  - "fuzzy_match_only_generates_candidates == true AND exact_id_and_proof_required == true"
prohibited_action_types:
  - REMOTE_COMMAND
  - AUTO_REMEDIATION
limitations:
  - "synthetic specification example; not a published signal"
```

该示例是 `SPECIFICATION_MATERIAL`，不是公共信号、真实事件结论或实现 fixture。

## 11. Negative object examples（负例）

以下任一情况必须被未来 schema/policy 拒绝：

- `outcome=CONFIRMED_AFFECTED` 出现在 `ApplicabilityAssessment`；
- `test_result=POSSIBLY_AFFECTED` 出现在 `ValidationFeedback`；
- `beneficial_capability.category=GENERAL_TOOL_RECOMMENDATION`；
- `cause_status=ADVERSARIAL` 但只有 `OBSERVED` 名称冲突且没有敌对证据；
- `publisher_assurance.global_trust_score=0.98`；
- `detection_advice.command="..."` 或包含 tool call payload；
- `AgentSafetySignal` 内嵌 raw private trace、credential 或 exact private tool inventory；
- `NOT_AFFECTED` 由 withheld/unknown profile 字段推出；
- correction 通过删除旧 signal/version 实现。

## 12. P2 result（P2 结果）

```text
P2_COMPLETE=true
MINIMUM_OBJECT_MODEL_FROZEN=true
OBJECT_COUNT=6
FIELD_DISCLOSURE_CEILINGS_DEFINED=true
PUBLISHER_ASSURANCE_LOCAL_TRUST_SEPARATED=true
APPLICABILITY_LOCAL_TEST_SEPARATED=true
CAUSE_STATUS_UNCERTAINTY_PRESERVED=true
BENEFICIAL_CAPABILITY_SCOPE_RESTRICTED=true
SCHEMA_FILE_CREATED=false
IMPLEMENTATION_CREATED=false
```
