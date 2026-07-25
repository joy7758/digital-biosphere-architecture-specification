---
document_id: DBA-TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-0.1
title: TITMAS Commercialization Standing Recommendation Authorization v0.1
title_zh: TITMAS 商业化按推荐执行常设授权 v0.1
version: 0.1.0
status: active-bounded-fail-closed
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_owner_ref: zhangbin
decision_reference: TITMAS-CS-STANDING-001
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Bounded human delegation for exact recommended actions; not automatic gate approval, blanket external action, self-approval, implementation, commercial availability, certification, or production authorization."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: human-standing-recommendation-authorization
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
authorized_at: 2026-07-25T10:50:56+08:00
directive_active: true
automatic_gate_approval: false
agent_self_approval: false
explicit_false_override: false
authority_effect: bounded-standing-delegation
---

# TITMAS Commercialization Standing Recommendation Authorization v0.1

## 1. Human Directive（人工指令）

Human Program Owner `zhangbin` 已明确提供：

> 并给予完全授权，再次遇到按照推荐执行。

本记录把该指令解释为：

> 在 TITMAS 商业化标准推进范围内，当未来推荐已经绑定 exact action、target、scope、
> preconditions、false effects 和 fail-closed stop rules 时，Codex 可按推荐直接形成并执行
> 对应的有界决定，不再重复请求同一形式的泛化确认。

机器记录：

- [standing directive JSON](TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-v0.1.json)；
- [directive Schema](architecture/schemas/titmas-commercialization-standing-recommendation-authorization.schema.v0.1.json)。

## 2. Scope（适用范围）

```text
DIRECTIVE_ID=TITMAS-CS-STANDING-001
SCOPE=TITMAS_COMMERCIALIZATION_STANDARD_TRACK
VALIDITY=UNTIL_REVOKED
```

适用于：

- DBA/TITMAS 商业化标准路线的 architecture/specification governance；
- problem validation、ownership crosswalk、review、conformance 和 readiness contracts；
- decision packet、machine record、Schema 和审计材料；
- authorized internal validation；
- path-scoped commit and push；
- 已有精确推荐所要求的下一有界动作。

不自动扩展到 DBOS、SAEE 或其他项目的代码、Runtime、发布、部署或 operational state。

## 3. Eligibility Contract（可直接执行条件）

所有条件必须同时满足：

1. 有 canonical recommendation record；
2. 推荐只包含一个或清晰分离的 exact option；
3. primary repository、target artifact/action 和 scope 明确；
4. required preconditions 有直接证据；
5. 明确列出 Authority、Ownership、Implementation、External Action、Commercial、
   Certification 和 Release effects；
6. 明确 stop/fail-closed 条件；
7. 不与更晚或更具体的人类决定冲突；
8. 必须生成独立 Decision/Authorization Record，不能只引用模型回答；
9. 结果仍需验证并记录失败、未知和限制；
10. 所有 materially different（实质不同）动作分别留痕。

任一条件缺失：

```text
STANDING_DIRECTIVE_APPLICABLE=false
ACTION_EXECUTED=false
```

## 4. Current Explicit False Boundary（当前明确禁止覆盖）

`CS-D01` 同时明确：

```text
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```

常设指令不能把这些字段直接改为 true。未来如推荐需要其中任一动作，必须先形成一个新的
exact-scope decision packet，明确 target、data/audience、risk、rollback 和 effects，再依据
本常设指令记录新的有界决定。

## 5. Material Action Rules（重大动作规则）

以下动作只有在 future exact recommendation packet 明确列出时，常设指令才可能适用：

- external outreach、participant enrollment 或数据收集；
- DBOS/SAEE/Adapter implementation；
- API、Runtime、network、cloud 或 database resource；
- public release、merge 或 deployment；
- product、price、SLA、contract 或 payment；
- trademark、legal representation、Certification 或 Certificate；
- destructive data/repository action。

“推进商业化”“完全授权”本身不是这些动作的 exact target。

## 6. Permanent Non-elevation Rules（永久非抬升规则）

```text
RECOMMENDATION_NE_UNRECORDED_DECISION=true
DECISION_RECORD_REQUIRED=true
AUTOMATIC_GATE_APPROVAL=false
AGENT_SELF_APPROVAL=false
EXPLICIT_FALSE_OVERRIDE=false

SPECIFICATION_NE_IMPLEMENTATION=true
SCHEMA_VALID_NE_CONFORMANCE_PASS=true
CONFORMANCE_PASS_NE_CERTIFICATION=true
COMMERCIAL_INTEREST_NE_CUSTOMER_ADOPTION=true
PAYMENT_NE_PERMISSION=true
EVIDENCE_NE_TRUTH=true
EVALUATION_NE_AUTHORITY=true
```

常设指令提供 human delegation provenance（人工委托来源），不赋予 Agent 独立 Architecture
Authority、Operational Authority 或 Commercial Authority。

## 7. Decision Record Requirements（决定记录要求）

每次应用必须生成：

```yaml
decision_id:
standing_directive_reference: TITMAS-CS-STANDING-001
recommendation_reference:
exact_action:
primary_repository:
target_refs: []
preconditions:
scope:
false_effects:
stop_conditions:
decided_by_ref: zhangbin
executed_by:
execution_receipt:
result:
known_limitations: []
```

没有该记录，不能声称“已按常设指令授权”。

## 8. Revocation and Conflict（撤销与冲突）

- Human Owner 可随时撤销或缩小常设指令；
- 后续更具体的人类决定优先；
- 两个推荐冲突时停止，不自行选择；
- source/Owner/status 冲突时标记 `CONFLICTED`；
- 无法证明 prerequisites 时保持 `BLOCKED`；
- 已执行历史保留，不因撤销而删除。

## 9. Current Effect（当前效果）

```text
TITMAS_STANDING_RECOMMENDATION_DIRECTIVE_ACTIVE=true
TITMAS_STANDING_DIRECTIVE_SCOPE=COMMERCIALIZATION_STANDARD_TRACK
REPEATED_GENERIC_CONFIRMATION_REQUIRED=false
EXACT_DECISION_RECORD_REQUIRED=true

AUTOMATIC_GATE_APPROVAL=false
AGENT_SELF_APPROVAL=false
EXPLICIT_FALSE_OVERRIDE=false

CURRENT_IMPLEMENTATION_AUTHORIZED=false
CURRENT_EXTERNAL_ACTION_AUTHORIZED=false
CURRENT_COMMERCIAL_OFFER_AUTHORIZED=false
CURRENT_CERTIFICATION_AUTHORIZED=false
CURRENT_RELEASE_AUTHORIZED=false
```
