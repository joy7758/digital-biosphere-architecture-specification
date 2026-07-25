---
document_id: DBA-TITMAS-GOOD-FIRST-CONTRIBUTION-CATALOG-0.1
title: TITMAS Good First Contribution Catalog v0.1
title_zh: TITMAS 首次贡献候选清单 v0.1
status: local-preparation-candidates-not-public-issues
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
document_type: non-executable-contribution-catalog
architecture_domain: TITMAS
public_issues_created: false
tasks_assigned: false
contributors_recruited: false
external_action_authorized: false
implementation_authorized: false
---

# TITMAS Good First Contribution Catalog v0.1

## 1. Boundary（边界）

本清单帮助第一次接触的开发者或受治理智能体理解“可以贡献什么”。每项只是
`LOCAL_PREPARATION_CANDIDATE`：

```text
CATALOG_ENTRY_NE_GITHUB_ISSUE=true
CATALOG_ENTRY_NE_ASSIGNMENT=true
CATALOG_ENTRY_NE_IMPLEMENTATION_AUTHORIZATION=true
CATALOG_ENTRY_NE_COMMUNITY_ESTABLISHMENT=true
```

## 2. Candidate Contributions（候选贡献）

| id | candidate | 预期产物 | 验证 | 风险 | 当前状态 |
|---|---|---|---|---|---|
| `GFC-001` | 首次接触五分钟理解测试 | 记录首次接触者对 TITMAS/DBOS/SAEE/Agent Framework 的解释和误解 | 与 README、AGENTS 和 Strategy 对照 | 不得写成客户采用 | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-002` | 中英文术语一致性检查 | 术语差异清单和 bounded fix proposal | 精确文件/行、canonical term | 不改对象含义 | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-003` | 本地链接与 source version 审查 | broken/stale link report | 只读链接检查、exact ref | 上游当前状态可能变化 | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-004` | 文档 maturity metadata inventory | 每个 TITMAS 文档的 maturity/Owner/Decision 缺口表 | 依据成熟度政策；missing 保留 | 不自动升级状态 | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-005` | Authority non-elevation 负例 | Proposal 中新增一个可复现负例 | 证明 PASS 不产生 Authority/Permission/Truth | 不运行真实权限动作 | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-006` | OpenTelemetry reference delta note | 钉住版本与当前 upstream 的差异候选 | primary source、commit、observed_at | reference 不等于 adoption | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-007` | Agent-readable entry schema review | JSON/Schema 字段缺口和兼容建议 | JSON parse、required field、false effects | Schema 不等于 API | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-008` | Known limitations inventory | 已知限制去重和来源绑定 | limitation → source → affected surface | 不把计划写成修复事实 | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-009` | Contribution Proposal dry run | 使用模板描述一个文档改进，不实施 | scope、source、negative、decision path 完整 | Proposal 不等于 Decision | `AVAILABLE_FOR_LOCAL_PREPARATION` |
| `GFC-010` | Workstream activation negative review | 找出一个“不应成立 SIG”的候选并说明缺口 | 对照八项 activation gate | 不创建 Workstream | `AVAILABLE_FOR_LOCAL_PREPARATION` |

## 3. Selection Rules（选择规则）

首次贡献候选必须：

- 不要求生产凭据、私有数据或外部账号；
- 不需要修改 DBOS/SAEE canonical truth；
- 不创建 Agent、Runtime、Entity、Permission 或真实 Evidence；
- 结果可由另一个人或智能体在本地重复检查；
- 有明确 done criteria（完成条件）和 non-claim；
- 大于文档修正的变化先填写 Proposal。

## 4. Completion Record（完成记录）

未来每项完成记录使用：

```yaml
catalog_id:
contribution_ref:
contributor_type:
human_accountability_ref:
source_refs: []
checks: []
review_result:
decision_reference:
merged_or_adopted: false
effects:
  authority: none
  permission: none
  runtime: none
  release: none
```

本文件不记录当前完成者，因为尚未开放公共贡献表面，也没有任务分配。

## 5. Current Status（当前状态）

```text
TITMAS_GOOD_FIRST_CONTRIBUTION_CATALOG_CREATED=true
TITMAS_GOOD_FIRST_CONTRIBUTION_CANDIDATES=10
TITMAS_GOOD_FIRST_ISSUES_CREATED=false
TITMAS_CONTRIBUTIONS_RECEIVED=0
TITMAS_CONTRIBUTORS_RECRUITED=0
```
