---
document_id: DBA-TITMAS-WORKSTREAM-CHARTER-TEMPLATE-0.1
title: TITMAS Workstream Charter Template v0.1
title_zh: TITMAS 工作流章程模板 v0.1
status: template-only-no-workstream-created
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-workstream-charter-template
architecture_domain: TITMAS
workstream_created: false
sig_created: false
maintainer_assigned: false
external_action_authorized: false
authority_effect: none
---

# TITMAS Workstream Charter Template v0.1

本模板用于未来真实工作成熟后提议 Workstream，不创建 Workstream、SIG、会议、Maintainer、
仓库或社区 Authority。

## 1. Workstream Identity（工作流标识）

```yaml
workstream_id:
display_name:
status: PROPOSED
charter_version: 0.1
proposal_reference:
activation_decision_reference:
created_at:
review_at:
```

## 2. Mission and Scope（使命与范围）

```text
mission=
problem=
in_scope=
out_of_scope=
non_goals=
expected_artifacts=
```

工作流必须解决一项已经出现的真实、持续工作，不能只因组织图完整而成立。

## 3. Canonical Sources and Authority（规范来源与权力）

```yaml
canonical_source_refs: []
external_reference_versions: []
affected_authority_domains: []
domain_owner_refs: []
architecture_decision_path:
```

必须保持：

```text
WORKSTREAM_NE_ARCHITECTURE_AUTHORITY=true
WORKSTREAM_NE_DBOS_OPERATIONAL_AUTHORITY=true
WORKSTREAM_NE_SAEE_EVOLUTION_AUTHORITY=true
MAINTAINER_REVIEW_NE_RELEASE_AUTHORIZATION=true
```

## 4. Roles（角色）

```yaml
maintainer_candidates: []
reviewer_candidates: []
triager_candidates: []
participant_entry:
term:
replacement_path:
removal_path:
conflict_of_interest_disclosure:
```

候选人不能因出现在模板中获得角色。指派必须引用独立 Decision、明确接受记录和 scope。

## 5. Working Model（工作方式）

```text
primary_async_record=
proposal_path=
review_path=
decision_record_path=
meeting_required=false
meeting_notes_path=
record_retention=
```

优先采用可搜索、可链接、可异步参与的记录。只有真实协作需要时才建立会议；会议结论必须
回写到规范 Proposal/Decision，口头共识不能替代架构记录。

## 6. Deliverables and Maturity（交付与成熟度）

| artifact | Owner | version | maturity | acceptance evidence |
|---|---|---|---|---|
| `TBD` | `NOT_ASSIGNED` | `TBD` | `Development` | `NOT_ASSESSED` |

每个 artifact 独立遵循
[TITMAS Document Maturity Policy](titmas-document-maturity-policy-v0.1.md)。

## 7. Security, Privacy and Conduct（安全、隐私与行为）

```text
code_of_conduct_reference=
security_disclosure_path=
data_handling_rules=
credential_handling_rules=
supply_chain_rules=
```

三项路径未明确时，Workstream 不得激活。

## 8. Success, Review and Closure（成功、复核与关闭）

成功证据应以可复用 artifact、外部实现反馈、版本声明和符合性结果为主，不以会议数、
成员数、Star 或 PR 数代替。

```yaml
success_measures: []
review_cadence:
inactivity_threshold:
closure_conditions: []
archive_path:
successor_workstream:
```

关闭或撤回 Workstream 必须保留历史、失败和 Decision。

## 9. Activation Gate（激活闸门）

全部为真才可提交激活决定：

- [ ] 真实持续工作及至少一项有界 artifact 已存在；
- [ ] Charter、scope、non-goals 和 canonical sources 完整；
- [ ] Maintainer/Reviewer 候选有贡献证据并明确接受；
- [ ] DBA、DBOS、SAEE Authority 边界通过审查；
- [ ] Contributor Guide 与正式 Code of Conduct 已采纳；
- [ ] Security Disclosure 与 Conflict of Interest 路径明确；
- [ ] 公共贡献表面和相应外部动作已获授权；
- [ ] DBA Architecture Decision 明确激活范围。

```text
TITMAS_WORKSTREAM_TEMPLATE_CREATED=true
TITMAS_WORKSTREAM_CREATED=false
TITMAS_SIG_CREATED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_WORKSTREAM_ACTIVATION_AUTHORIZED=false
```
