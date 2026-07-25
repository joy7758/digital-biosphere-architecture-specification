---
document_id: DBA-TITMAS-CS-D02-PREREQUISITE-SELECTION-DECISION-PACKET-0.1
title: TITMAS CS-D02 Prerequisite Selection Decision Packet v0.1
title_zh: TITMAS CS-D02 前置条件选择决策包 v0.1
version: 0.1.0
status: packet-prepared-blocked-human-input-no-selection-no-outreach
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-01
parent_decision_reference: CS-D02
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Human prerequisite-selection packet only; no role acceptance, reviewer appointment or outreach, store selection or implementation, problem-validation execution, data collection, gate pass, commercialization, certification, or release claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-human-decision-packet
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
prepared_at: 2026-07-25
---

# TITMAS CS-D02 Prerequisite Selection Decision Packet v0.1

## 0. Decision Status（决定状态）

本包准备一个独立、较小的前置决定：

> 是否接受有界 Owner/Data Steward 角色，并授权准备招募两名独立 human Reviewer、选择本地
> 加密非 Git 存储方案？

```text
DECISION_CANDIDATE_ID=CS-D02-PRE-01
PARENT_DECISION_ID=CS-D02
PACKET_PREPARED=true
DECISION_READY=false
DECISION_RECORDED=false

ROLE_ACCEPTANCE_RECORDED=false
REVIEWER_RECRUITMENT_AUTHORIZED=false
REVIEWER_OUTREACH_EXECUTED=false
STORE_SELECTED=false
STORE_IMPLEMENTED=false
```

机器入口：

- [machine packet](TITMAS-CS-D02-PREREQUISITE-SELECTION-DECISION-PACKET.v0.1.json)；
- [packet Schema](architecture/schemas/titmas-cs-d02-prerequisite-selection-decision-packet.schema.v0.1.json)。

## 1. Scope（范围）

本决定候选只处理：

1. Problem Validation Owner / Privacy Data Steward 的角色接受；
2. Reviewer 来源路线和有界招募准备；
3. 私有验证 Store 类别和选择准备。

本决定即使未来批准，也不自动授权：

- 参与者联络或招募；
- 公开网页材料审查；
- Agent API 调用；
- 验证数据收集；
- Store 创建、部署或测试；
- 问题验证执行；
- `CS-G0`、`CS-G1` 或下游 Gate PASS。

## 2. Owner Acceptance Option（Owner 接受选项）

### O1 — Accept bounded dual role（推荐）

```text
problem_validation_owner_ref=zhangbin
privacy_data_steward_ref=zhangbin
role_overlap_disclosed=true
role_scope=CS_D02_PREPARATION_ONLY
operational_authority_created=false
```

推荐原因：当前项目只有一个已知 Program Decision Owner；让同一人承担有界准备职责可以减少
协调成本，但必须保留独立 Method/Claim Review，且不能自我验证记录。

当前：

```text
O1_RECOMMENDED=true
O1_ACCEPTED=false
```

### O2 — Nominate different humans

有效但当前没有 identities、acceptance 或 conflict records。

### O3 — Defer

安全但 CS-D02 保持阻塞。

## 3. Reviewer Sourcing Options（Reviewer 来源选项）

### R1 — Bounded external human reviewer recruitment（条件推荐）

目标：

- 1 名独立 Method Reviewer；
- 1 名独立 Security + Claim Reviewer；
- 两人都不是问题记录创建者；
- Agent 只提供辅助，不计入 human minimum。

在招募前必须决定：

- exact recruitment channel；
- budget cap；
- message/terms；
- identity、competence、independence 和 conflict evidence；
- confidential contact route；
- no participant/customer outreach boundary；
- expiry、stop 和 revocation。

```text
R1_RECOMMENDED=CONDITIONALLY
R1_DECISION_READY=false
R1_OUTREACH_AUTHORIZED=false
```

### R2 — Known trusted human nomination

如果用户已有合适人选，优先于公开招募；当前 identities 为 0，因此不可执行。

### R3 — Agent-only review

```text
R3_ALLOWED=false
```

模型可以做 advisory review，不能成为正式 human Reviewer。

### R4 — Defer

合法停止选项。

## 4. Store Selection Options（Store 选择选项）

### S1 — Local encrypted non-Git store（条件推荐）

推荐类别：

```text
LOCAL_ENCRYPTED_PRIVATE_NON_GIT_VALIDATION_STORE
```

优势：

- 最小网络暴露；
- 适合最多 20 条、14 天的有界准备；
- 与公开 Git、DBOS canonical Evidence 和 Runtime 隔离；
- 成本和运维复杂度最低。

决定前仍缺：

- exact path/container reference；
- FileVault/encrypted container applicability evidence；
- independent access identity strategy；
- backup/no-backup choice；
- deletion/tombstone procedure；
- incident route。

```text
S1_RECOMMENDED=CONDITIONALLY
S1_SELECTED=false
S1_IMPLEMENTATION_AUTHORIZED=false
```

### S2 — Isolated Baidu server private store

当前不推荐首轮使用：需要网络、server account、host hardening、backup、tenant/access、incident
和跨设备数据传输控制。已有服务器不等于本用途已批准。

### S3 — Managed private cloud store

当前不推荐：引入 provider、费用、residency、contract 和 access complexity。

### S4 — Defer

合法停止选项。

## 5. Combined Recommendation（组合推荐）

```text
RECOMMENDED_OWNER_OPTION=O1
RECOMMENDED_REVIEWER_OPTION=R1_CONDITIONAL
RECOMMENDED_STORE_OPTION=S1_CONDITIONAL

OVERALL_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
DECISION_READY=false
```

阻塞输入：

- reviewer recruitment channel；
- reviewer budget cap；
- reviewer outreach expiry；
- exact local encrypted store reference；
- encryption/access applicability reference；
- confidential incident route。

## 6. Exact Future Decision Token（未来精确决定 token）

以下模板当前未填写完整，因此不是决定：

```text
decided_by_ref=zhangbin
CS-D02-PRE-01=AUTHORIZE_BOUNDED_REVIEWER_RECRUITMENT_AND_LOCAL_STORE_SELECTION_PREPARATION

owner_option=O1
problem_validation_owner_acceptance=ACCEPT_ZHANGBIN_BOUNDED_PREPARATION_ROLE
privacy_data_steward_acceptance=ACCEPT_ZHANGBIN_WITH_ROLE_OVERLAP_DISCLOSURE
role_overlap_conflict_disclosure_ref=<exact-reference>

reviewer_option=R1
reviewer_pattern=ONE_METHOD_PLUS_ONE_SECURITY_CLAIM_HUMAN
reviewer_recruitment_channel=<exact-channel>
reviewer_budget_currency=CNY
reviewer_budget_cap=<non-negative-number>
reviewer_outreach_expires_at=<RFC3339>
reviewer_outreach_authorized=<true-or-false>

store_option=S1
store_class=LOCAL_ENCRYPTED_PRIVATE_NON_GIT_VALIDATION_STORE
exact_store_reference=<exact-path-or-container-reference>
encryption_applicability_reference=<exact-reference>
access_control_candidate_reference=<exact-reference>
store_selection_authorized=<true-or-false>
store_implementation_authorized=false

participant_outreach_authorized=false
public_web_review_authorized=false
agent_api_call_authorized=false
data_collection_authorized=false
problem_validation_execution_authorized=false
commercial_offer_authorized=false
certification_authorized=false
release_authorized=false
```

任一 `<...>` 未填或任何 boolean 冲突时，保持 `BLOCKED_INPUT`。

## 7. Standing Directive Assessment（常设指令判断）

```text
STANDING_DIRECTIVE_ACTIVE=true
STANDING_DIRECTIVE_APPLICABLE_NOW=false
```

虽然 O1/R1/S1 是当前推荐组合，但 R1 和 S1 缺 exact channel、budget、expiry、store 和
incident references，并且此前明确 `external_outreach_authorized=false`。常设指令不能覆盖
该 false，也不能替人填写预算或同意角色。

## 8. Current State（当前状态）

```text
CS_D02_PRE_01_PACKET_PREPARED=true
CS_D02_PRE_01_DECISION_READY=false
CS_D02_PRE_01_DECISION_RECORDED=false

PROBLEM_VALIDATION_OWNER_ACCEPTED=false
PRIVACY_DATA_STEWARD_ACCEPTED=false
INDEPENDENT_HUMAN_REVIEWERS_SELECTED=0
REVIEWER_RECRUITMENT_AUTHORIZED=false
REVIEWER_OUTREACH_EXECUTED=false
STORE_OPTION_SELECTED=false
STORE_IMPLEMENTED=false

PARTICIPANT_OUTREACH_AUTHORIZED=false
PUBLIC_WEB_REVIEW_AUTHORIZED=false
AGENT_API_CALL_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
