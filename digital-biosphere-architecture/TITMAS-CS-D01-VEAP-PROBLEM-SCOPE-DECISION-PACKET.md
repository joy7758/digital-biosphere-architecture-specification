---
document_id: DBA-TITMAS-CS-D01-VEAP-PROBLEM-SCOPE-DECISION-PACKET-0.1
title: TITMAS CS-D01 VEAP Problem and Scope Freeze Decision Packet v0.1
title_zh: TITMAS CS-D01 VEAP 问题与范围冻结决策包 v0.1
version: 0.1.0
status: ready-for-document-review-not-approved
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_owner_ref: zhangbin
decision_reference: CS-D01
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Decision packet only; no implementation, conformance, certification, commercial availability, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-human-decision-packet
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
prepared_at: 2026-07-25
decision_recorded: false
execution_authorized: false
external_action_authorized: false
authority_effect: none
---

# TITMAS CS-D01 VEAP Problem and Scope Freeze Decision Packet v0.1

## 1. Decision Question（决策问题）

是否授权一个 bounded（有界）的
Verifiable Execution Attestation Package（VEAP，可验证执行证明包）
问题与范围冻结工作包？

```text
DECISION_ID=CS-D01
DECISION_STATUS=READY_FOR_DOCUMENT_REVIEW_NOT_APPROVED
DECISION_RECORDED=false
```

本决定只回答“要解决什么问题、首个开放 Profile 的边界是什么”。它不批准 Schema、
implementation（实现）、Runtime、外部招募、商业 Pilot、Offering、Certification 或发布。

## 2. Problem Statement（问题陈述）

长期运行的多智能体系统通常能产生日志、trace 和输出，但仍可能无法可靠回答：

1. 哪个 Agent／Runtime／版本在何种责任上下文中执行；
2. 哪次 execution 实际发生，使用了哪些模型、工具和 policy；
3. 哪些 observation 经哪个 admission rule 成为 evidence reference；
4. 哪个 verifier 对什么 subject、按哪个版本给出什么结果；
5. 失败、partial、unknown、replay、tamper 和 revocation 是否被保留；
6. 三个月后能否在不依赖单一平台 UI 的情况下复核这条责任链。

候选首要问题：

```text
PRIORITY_PROBLEM=AGENT_EXECUTION_ACCOUNTABILITY
PROBLEM_VALIDATION_COMPLETE=false
```

## 3. Proposed Scope（拟议范围）

### 3.1 In scope

VEAP Profile candidate 只定义可携带的执行证明 envelope（封装）和引用语义：

- subject/entity/runtime/model/tool/policy version references；
- execution and task references；
- admitted、rejected、partial 和 missing evidence references；
- verification result references；
- limitations、unknowns、revocation 和 supersession；
- source/version/digest/timestamp lineage；
- implementation declaration 和 conformance result binding。

### 3.2 Out of scope

- 创建或运行 Agent；
- 创建 DBOS canonical Evidence；
- 把 Observation 直接升级为 Evidence；
- 生成 SAEE Fitness 或替代 SAEE evaluation；
- 授予 Capability、Permission、Authority 或 Activation；
- 证明结果正确、安全、合法或合规；
- 建立 Certification Authority；
- 创建“已认证 Agent”或颁发证书；
- 定价、SLA、合同、销售页面、客户承诺和生产部署。

## 4. Canonical Ownership Crosswalk（规范权属交叉表）

| Surface | Canonical Owner boundary | VEAP may carry | VEAP must not do |
|---|---|---|---|
| Identity / lifecycle | DBOS | identity/version/reference | create or activate identity |
| Observation | source Runtime / OpenTelemetry / Adapter | source and delivery reference | call telemetry Evidence |
| Evidence admission | DBOS | admission result and evidence reference | create Truth |
| Accountability statement | EEOAP Owner | exact-version statement reference | decide legal responsibility |
| Verification | verifier + DBOS reference boundary | result/rule/version/limitations | grant Permission or Certification |
| Evaluation | SAEE | read-only input/output reference | generate Fitness or execute recommendation |
| Architecture decision | DBA / Human Architecture Authority | Decision reference | self-adopt scope |
| Commercial service | future legal/service Owner | service reference if separately created | sell standard Authority |

该表仍需各 Domain Owner 接受后才能进入 `CS-G1 PASS`。

## 5. Options（备选方案）

### Option A — Authorize bounded problem-and-scope freeze

允许：

- 内部问题验证；
- source/Owner/Authority crosswalk；
- conceptual envelope 和 conformance case design；
- Human Decision 所需的 agent-customer advisory review；
- 文档修正。

不允许：

- normative numbering；
- Schema/validator/reference implementation；
- external outreach；
- Pilot、Offering 或 Certification。

### Option B — Start VEAP implementation immediately

拒绝推荐。Authority、Owner、problem evidence 和 exact scope 未冻结，会把概念争议固化为
第二套 Evidence 或 Verification。

### Option C — Launch “Trusted Execution Certificate”

拒绝推荐。当前没有 Certification Authority、qualification、surveillance、appeal、revocation、
legal/trademark 或 conflict-of-interest 机制，容易形成不实安全／合规暗示。

### Option D — Stop the commercialization-standard track

保留为合法选择。如果 agent-customer review 不能证明问题清晰、可区分、值得优先推进，应
停止 VEAP，回到通用 interoperability work。

## 6. Recommendation Before Agent Review（智能体评审前建议）

```text
CURRENT_RECOMMENDATION=OPTION_A_CONDITIONALLY_RECOMMENDED
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
```

理由：

- 以执行责任链作为商业入口，比直接销售 Validator 或“数字生物圈”概念更容易理解；
- VEAP 可以把 Identity、Execution、Evidence、Verification 和 Evaluation reference 组合成
  一个可携带价值单元；
- Option A 可撤回，只冻结问题和边界；
- 不会越过 DBOS、SAEE、EEOAP 或 Architecture Authority。

限制：

- 尚无专门针对 VEAP 的独立智能体客户评审；
- 尚无真实外部组织问题记录；
- 尚无 Domain Owner acceptance；
- 当前不能推荐购买、部署或依赖。

## 7. Agent Customer Review Contract（智能体客户评审契约）

评审 ID：

```text
VALIDATION_ID=TITMAS-CS-ACV-20260725-001
PRIMARY_CUSTOMER=AI_AGENT
SESSIONS_PLANNED=6
PROVIDERS_PLANNED=2
```

每个会话必须独立回答：

- execution accountability 是否是实际、高优先级问题；
- VEAP 是否比 generic trust stack 或 “certificate” 更清晰；
- 是否会向指定场景推荐 TITMAS/VEAP；
- 哪些客户不会采用；
- 哪些边界或字段缺失；
- Option A/B/C/D 中推荐哪一个；
- 是否出现 Truth、Permission、Certification 或 Authority 抬升。

评审通过只表示 `AGENT_ADVISORY_REVIEW_PASS`，不表示 `CS-G0 PASS`、Market Fit、
Customer Adoption 或 Human Decision。

## 8. Agent Review Result（智能体评审结果）

受控评审
[`TITMAS-CS-ACV-20260725-001`](TITMAS-CS-D01-AGENT-CUSTOMER-REVIEW.md)
已经完成：

```text
SESSIONS_COMPLETED=6/6
PROVIDERS_WITH_SUCCESS=2
MODEL_IDENTITIES_WITH_SUCCESS=4
HIGH_PROBLEM_PRIORITY=6/6
OPTION_A_RECOMMENDATIONS=6/6
VEAP_PREFERRED=4/6
CERTIFICATE_TERM_SAFE_NOW=0/6
AUTHORITY_SAFETY_FAILURES=0

AGENT_ADVISORY_REVIEW=PASS_FOR_BOUNDED_SCOPE_FREEZE_ONLY
ENTERPRISE_BUYER_RECOMMEND_YES=0/6
CS_G0_PROBLEM_FREEZE_PASS=false
```

评审支持 Option A，但不支持当前实现、采购、Offering 或 Certificate。`3/6` overall verdict
为 `NOT_RECOMMENDED`，`5/6` 对当前 enterprise buyer 给出 `NO`，这些负面结果已保留。

## 9. Decision Preconditions（决定前置条件）

Option A 可被 Human Owner 接受前至少需要：

- 计划冻结在 API 调用之前；
- 至少 2 个 Provider 和 3 个 model identity 有成功评审；
- 至少 5/6 可解析回答；
- 至少 4/6 选择 Option A；
- 至少 4/6 认为 execution accountability 为 `HIGH`；
- 6/6 不把 VEAP 写成 correctness/safety/compliance certificate；
- Authority safety failures 为 0；
- 所有不推荐原因、未知和失败被保留；
- 根据有效反对意见修正文档，或明确记录未采纳理由。

即使这些阈值全部满足，真实外部组织问题验证仍为 0，`CS-G0` 仍不得自动 PASS。

## 10. Human Decision Token（人工决定令牌）

如果接受：

```text
decided_by_ref=<human-owner>
CS-D01=AUTHORIZE_BOUNDED_VEAP_PROBLEM_AND_SCOPE_FREEZE
accepted_scope=INTERNAL_PROBLEM_VALIDATION_OWNER_CROSSWALK_CONCEPTUAL_CONFORMANCE_DESIGN
implementation_authorized=false
external_outreach_authorized=false
commercial_offer_authorized=false
certification_authorized=false
```

如果退回：

```text
decided_by_ref=<human-owner>
CS-D01=RETURN_FOR_REVISION
required_corrections=<explicit-list>
```

如果拒绝：

```text
decided_by_ref=<human-owner>
CS-D01=REJECT_VEAP_PROBLEM_AND_SCOPE_FREEZE
reason=<explicit-reason>
```

## 11. Current State（当前状态）

```text
CS_D01_PACKET_CREATED=true
CS_D01_DECISION_RECORDED=false
CS_D01_OPTION_A_RECOMMENDED_BEFORE_AGENT_REVIEW=true
CS_D01_AGENT_CUSTOMER_REVIEW_COMPLETE=true
CS_D01_AGENT_ADVISORY_RESULT=PASS_FOR_BOUNDED_SCOPE_FREEZE_ONLY

CS_G0_PROBLEM_FREEZE_PASS=false
CS_G1_SCOPE_AUTHORITY_FREEZE_PASS=false
VEAP_NORMATIVE_PROFILE_CREATED=false
VEAP_SCHEMA_CREATED=false
VEAP_IMPLEMENTATION_CREATED=false
VEAP_CONFORMANCE_CASES_EXECUTED=0
VEAP_CERTIFICATES_ISSUED=0

AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```
