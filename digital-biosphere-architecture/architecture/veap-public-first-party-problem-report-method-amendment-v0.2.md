---
document_id: DBA-TITMAS-VEAP-PUBLIC-FIRST-PARTY-PROBLEM-REPORT-METHOD-AMENDMENT-0.2
title: VEAP Public First-party Problem Report Method Amendment Candidate v0.2
title_zh: VEAP 公开第一方问题报告方法修订候选 v0.2
version: 0.2.0
status: development-method-revision-candidate-delta-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-07
predecessor: veap-public-first-party-problem-report-method-amendment-v0.1.md
predecessor_review: ../commercialization-standards-public-source-method-review/VEAP-PUBLIC-FIRST-PARTY-METHOD-AGENT-REVIEW-v0.1.md
method_adopted: false
desk_research_execution_authorized: false
public_source_search_authorized: false
public_source_collection_authorized: false
public_source_record_counting_authorized: false
valid_problem_records: 0
cs_g0_pass: false
authority_effect: none
---

# VEAP Public First-party Problem Report Method Amendment Candidate v0.2

## 0. Status and Delta Scope（状态与修订范围）

本文件只修订
[v0.1 method candidate](veap-public-first-party-problem-report-method-amendment-v0.1.md)
在 [PRE-06 two-provider review](../commercialization-standards-public-source-method-review/VEAP-PUBLIC-FIRST-PARTY-METHOD-AGENT-REVIEW-v0.1.md)
中被明确指出的六项问题。v0.1 冻结输入、审查结果和 dissent 保持不变。

```text
METHOD_V0_2_CANDIDATE_DEFINED=true
PRE_06_REQUIRED_CORRECTIONS_ADDRESSED=6
METHOD_DELTA_REVIEW_REQUIRED=true

METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_SEARCH_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

本候选没有检索、下载、复制、登记、评分或计数任何真实 issue、incident、组织、个人或
客户材料。

机器契约：

- [method contract](veap-public-first-party-problem-report-method-contract.v0.2.json)；
- [contract Schema](schemas/veap-public-first-party-problem-report-method-contract.schema.v0.2.json)。

## 1. Unchanged Purpose and Source Classes（不变的目的与来源类别）

方法仍只用于未来审查：承担直接维护、运行、治理或事件调查责任的主体，是否公开报告了
具体 operational problem（运行问题）。以下边界不变：

- eligible candidate：official Maintainer issue、official incident report、official
  project postmortem、accountable organization technical report；
- secondary article、promotional material、search snippet、model-generated content、
  unattributed/private material 不合格；
- 公开 URL、GitHub issue 或署名本身不证明 first-party accountability；
- 公开报告不证明 TITMAS consent、customer、adoption、market fit 或 VEAP fit。

## 2. Required Qualification Fields（资格字段）

未来 `VALID` candidate 必须显式支持：

1. `canonical_public_source_ref`；
2. `source_publisher_ref`；
3. `accountable_source_role`；
4. `accountable_role_verification`；
5. `published_at` 与 `observed_at`；
6. `recent_example`；
7. `problem_area`；
8. `current_workaround`；
9. `workaround_limitations`；
10. `measurable_cost_or_risk`；
11. `priority_basis`；
12. `existing_alternatives`；
13. `source_integrity`；
14. `relationship_classification`；
15. `independence_basis`；
16. `source_context_key`；
17. `report_lineage`；
18. `retention_disposition`；
19. `reviewer_refs`；
20. `known_limitations`。

缺失字段保持 `UNKNOWN`。模型、Reviewer 或 TITMAS 作者不得推断补齐；缺失材料使记录
保持 `PARTIAL` 或 `INVALID`。

## 3. Accountable Source Role Verification（责任来源角色核验）

`accountable_source_role` 必须有记录地核验，不能只依赖 Reviewer 判断。

最低核验记录：

1. `publisher_controlled_role_reference`：发布方控制的 Maintainer、team、incident owner、
   security/platform ownership 或等价角色页面；
2. `source_to_system_responsibility_binding`：把该角色与被描述项目、系统、流程或事件连接；
3. `observed_at`、`reviewer_ref` 和核验结果；
4. 任何 contradictory signal（矛盾信号）和 limitation。

规则：

- 只有署名、社交资料、搜索摘要或第三方介绍：`PARTIAL`；
- 发布方责任绑定无法核验：`PARTIAL`；
- 存在矛盾角色声明：`CONFLICTED`，暂停计数；
- Reviewer judgment alone（仅审查者判断）永远不足；
- 核验只证明来源角色，不证明其对 TITMAS 承担责任。

## 4. Relationship Classification（组织关系分类）

每条候选必须使用以下一个关系状态：

| class | treatment |
|---|---|
| `SAME_CONTROL_OR_ORGANIZATION` | 默认同一 independence context |
| `PARENT_CHILD_CONTROL` | 不自动独立；需要控制与运行责任分析 |
| `CONSORTIUM_OR_SHARED_GOVERNANCE` | 不自动独立；需要成员责任和事件来源分析 |
| `RELATED_BUT_OPERATIONALLY_DISTINCT` | 只有直接证据证明不同运行责任、不同问题实例和不同控制路径时才可提议独立 |
| `INDEPENDENT_ORGANIZATION` | 可进入独立性审查，仍不自动计数 |
| `UNKNOWN_RELATIONSHIP` | `PARTIAL`，不得计数 |

关联组织、母子组织或联盟名称不同，不等于 independence。共同控制、共同 incident owner、
共同 project governance 或同一 source chain 默认合并。

## 5. Context Key and Deduplication（上下文键与去重）

每个候选生成稳定的 `source_context_key`，组成：

```text
controlling_organization_or_governance
+
governed_project_system_or_workflow
+
incident_event_or_problem_root
+
declared_time_window
```

规则：

- 同一 context key 默认只有一个 canonical record；
- mirrors、forks、reposts、quotation chains 和多个模型不增加 independence；
- 同一来源的更新进入 `report_lineage`，通过 `supersedes`／`updates` 连接；
- 同一组织多个报告若描述同一事件或根因，合并为一个 context；
- 同一组织多个报告若可能描述不同事件，先分别保留，但在 Human Decision 前不增加组织
  independence；
- 只有记录了不同 operational responsibility、不同事件根和不同 control path，才可提议
  `RELATED_BUT_OPERATIONALLY_DISTINCT`；
- 作者相关来源披露冲突，默认不计独立记录；
- 关系、控制或事件根无法验证时保持 `PARTIAL`。

## 6. Multiple and Conflicting Reports（多个与冲突报告）

多个有效或冲突报告不得静默覆盖：

- canonical record 保存所有 `report_lineage` references；
- 内容一致的更新保留 lineage，不重复计数；
- 内容冲突时状态变为 `CONFLICTED`；
- `CONFLICTED` 立即暂停当前与历史计数效果；
- 必须记录 conflict summary、source versions、reviewer inputs 和 resolution decision；
- 只有 Human Decision Owner 可以决定 merge、supersede、separate context 或 invalidate；
- resolution 前不得选择对 TITMAS 最有利的版本。

## 7. Retention and Deletion（保留与删除）

未来执行若另行获授权，仍采用 data minimization（数据最小化）：

- 完整页面、完整文章、完整 issue discussion 和原始 provider envelope 不保存；
- 必要临时摘录最多 25 个英文单词或等量短语；
- 临时摘录在 extraction review 完成后最多保留 7 日，然后删除；
- 长期只保留 canonical URL、标题、publisher、accountable role verification、时间、
  content hash、context key、字段级释义、状态、review/decision references 和 limitation；
- 不保留直接标识符、联系方式、credential、private log 或 customer Evidence；
- 删除临时内容后保留最小 tombstone、hash 和 disposition，用于证明删除和历史连续性；
- source-use authorization 到期、撤销或冲突时立即停止新增处理。

上述为候选 retention policy，不创建 Store、Crawler、Database 或数据处理权限。

## 8. Correction, Removal and Withdrawal（更正、移除与撤回）

状态：

```text
ACTIVE
  -> CORRECTION_PENDING
  -> CORRECTED | WITHDRAWN | SOURCE_REMOVED_UNVERIFIABLE
```

规则：

- 发现来源更正、删除、hash drift 或责任角色变化时立即进入 `CORRECTION_PENDING`；
- 一进入 correction/removal 流程即暂停该记录的计数效果；
- 保留原 hash、观察时间、变更原因和最小 tombstone，禁止静默删除历史；
- `CORRECTED` 创建新版本并链接 predecessor；
- `WITHDRAWN` 保留撤回原因与决定来源；
- `SOURCE_REMOVED_UNVERIFIABLE` 不得继续作为 `VALID`；
- 恢复计数需要重新 Method/Claim-Privacy input 和 Human Decision Owner 决定；
- 来源发布者未请求 TITMAS 处理不等于 consent；公开信息处理仍受 source-use policy 限制。

## 9. Candidate Counting Policy（候选计数策略）

```text
COUNTING_POLICY_STATUS=CANDIDATE_NOT_ADOPTED
PUBLIC_SOURCE_VALID_RECORDS_MAX_TOWARD_CS_G0=2
PUBLIC_SOURCE_RECORD_CAN_SATISFY_CONTINUE_REVIEW_INTEREST=false
DIRECT_OR_GOVERNED_RESPONSIBILITY_CONTEXT_STILL_REQUIRED=true
METHOD_ADOPTION_REQUIRED_BEFORE_COUNTING=true
PER_RECORD_HUMAN_COUNTING_DECISION_REQUIRED=true
AUTOMATIC_COUNTING_ALLOWED=false
```

两条上限只防止 desk research 替代直接责任上下文。它不是已采纳规则。即使 v0.2 delta
review 通过，也必须先有独立 method-adoption decision；之后每一条记录还要由 Human
Decision Owner 独立决定是否计入。

## 10. Mapping and Claim Boundaries（映射与声明边界）

| Existing field | Public-source mapping |
|---|---|
| `observer_ref` | 第一方发布者或可归因责任角色引用 |
| `organization_or_context_ref` | 被描述项目、组织或运行上下文 |
| `human_accountability_ref` | 已核验来源责任角色；不表示 TITMAS 责任 |
| `consent_reference` | `NOT_APPLICABLE_PUBLIC_SOURCE_USE_BASIS` |
| `source_record_reference` | canonical URL、version/time、hash 和 context key |
| `contract_review_interest` | `NOT_ASKED` |
| `private_demo_review_interest` | `NOT_ASKED` |
| `commercial_commitment` | `false` |
| `customer_adoption` | `false` |

```text
PUBLICATION_NE_CONSENT_TO_TITMAS=true
PUBLIC_REPORT_NE_CUSTOMER=true
PUBLIC_REPORT_NE_ADOPTION=true
SOURCE_PROBLEM_NE_VEAP_FIT=true
PUBLIC_SOURCE_REVIEW_NE_MARKET_VALIDATION=true
```

## 11. Review and Adoption Gates（审查与采纳闸门）

记录创建者不能 self-validate。方法采纳前至少需要：

1. v0.2 Method 与 Claim/Privacy delta review 完成；
2. 六项 PRE-06 required change 被逐项验证；
3. Human Decision Owner 独立决定 adopt、return 或 reject；
4. 另行定义 source-search/collection exact scope、allowed domains、时间和 record cap；
5. 指定 retention、correction、removal、incident 和 appeal owner；
6. 指定独立 record review 与 counting owner；
7. 保留 `PARTIAL`、`INVALID`、`CONFLICTED`、`WITHDRAWN` 和失败。

Method adoption 仍不等于 execution authorization。没有独立 execution decision，禁止浏览、
检索、收集、登记或计数。

## 12. Current Recommendation and Non-effects（当前推荐与非效果）

```text
AGENT_RECOMMENDATION=DELTA_REVIEW_REQUIRED
RECOMMENDED_AS=FAIL_CLOSED_PUBLIC_FIRST_PARTY_METHOD_REVISION_CANDIDATE
NOT_RECOMMENDED_AS=ADOPTED_METHOD_OR_DESK_RESEARCH_EXECUTION

METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_SEARCH_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION=false

IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
