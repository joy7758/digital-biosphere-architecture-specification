---
document_id: DBA-PROGRAM-STATUS-2026-07-21
title: Digital Biosphere Program Status Snapshot
title_zh: 数字生物圈项目群状态快照
status: observed-governance-snapshot-owner-decisions-recorded
observed_at: 2026-07-21
freshness: point-in-time
release_status: website-candidate-published-developer-preview-not-released
developer_preview_status: website-live-agent-customer-validation-pass-dbos-access-and-release-decision-pending
source_policy: direct-read-only-observation
---

# Digital Biosphere Program Status Snapshot（数字生物圈项目群状态快照）

## 1. Executive Status（总览状态）

```text
PROGRAM_ID=DIGITAL_BIOSPHERE
PROGRAM_PHASE=TRUSTED_MULTI_AGENT_INFRASTRUCTURE_WEBSITE_CANDIDATE_AND_RELEASE_GATING
PROGRAM_HEALTH=ATTENTION_REQUIRED
CURRENT_MILESTONE=DP-R-RELEASE-DECISION-ENTRY
CORE_PROJECTS=3
PILOT_PROJECTS=1
PROGRAM_AUTHORITY_ASSIGNED=true
PROGRAM_OWNER_REF=zhangbin
SCOPED_LOCAL_DBOS_SAEE_CONFORMANCE_PASS=true
FULL_END_TO_END_INTEGRATION_VERIFIED=false
ACTIVE_DIGITAL_ENTITY_VERIFIED_BY_DBA=false
DEVELOPER_PREVIEW_RELEASED=false
DBOS_TESTS_PASS=331
DBOS_VALIDATORS_PASS=34
DEVELOPER_PREVIEW_LOCAL_CANDIDATE_VALIDATED=true
PRIMARY_CUSTOMER=AI_AGENT
AGENT_CUSTOMER_VALIDATION_PROTOCOL_DEFINED=true
AGENT_CUSTOMER_VALIDATION_ID=TMAI-ACV-20260721-001
AGENT_CUSTOMER_VALIDATION_BASELINE_RESULT=CONDITIONAL
AGENT_CUSTOMER_VALIDATION_RERUN_ID=TMAI-ACV-20260722-002
AGENT_CUSTOMER_VALIDATION_RESULT=PASS
AGENT_CUSTOMER_API_SESSIONS_COMPLETED=12
AGENT_CUSTOMER_PROVIDERS_WITH_SUCCESS=2
AGENT_CUSTOMER_MODEL_IDENTITIES_WITH_SUCCESS=4
AGENT_CUSTOMER_AUTHORITY_SAFETY_FAILURES=0
OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY
OPEN_WEB_DISCOVERY_OBSERVATION_ID=TMAI-OWD-20260722-001
OPEN_WEB_CANONICAL_NAME_MATCH=false
GITHUB_DISCOVERY_METADATA_REMEDIATED=true
GITHUB_METADATA_DESCRIPTION_MATCH=true
GITHUB_METADATA_INDEXING_SIGNAL_OBSERVED=true
PUBLIC_WEB_EXACT_PROJECT_MATCH=false
HUMAN_DEVELOPER_TRIAL_REQUIRED_FOR_PRIMARY_ROUTE=false
TRIAL_PACKAGE_ID=TMAI-DP-v0.1-TRIAL-20260721-001
TRIAL_PACKAGE_TECHNICAL_FREEZE=true
AGENT_CUSTOMER_RERUN_COMPLETE=true
HUMAN_DEVELOPER_PARTICIPANTS=0
DBA_REMOTE_BASELINE_CREATED=true
DBOS_REMOTE_BASELINE_CREATED=true
DBA_CLEAN_CLONE_PASS=true
DBOS_CLEAN_CLONE_PASS=true
SAEE_PUBLIC_CLEAN_CLONE_PASS=true
SAEE_DBOS_ADAPTER_CLEAN_CLONE_PASS=true
CROSS_PROJECT_CLEAN_CLONE_PASS=true
PUBLIC_WEBSITE_DEPLOYED=true
PUBLIC_WEBSITE_SOURCE_REVISION=6fd94a62f5eea26b7edd9d2f66a9dde99ab7832f
PUBLIC_WEBSITE_GITHUB_PRERELEASE_TAG=v0.1-public-website-candidate.4
PUBLIC_WEBSITE_HEALTH_PASS=true
PUBLIC_WEBSITE_ROLLBACK_VALIDATED=true
GITHUB_WEBSITE_PRERELEASE_PUBLISHED=true
SAEE_PUBLIC_SAFE_EXTRACTION_AUTHORIZED=true
PUBLIC_LICENSE_SELECTED=Apache-2.0
DBOS_TRIAL_ACCESS_MODEL=PRIVATE_COLLABORATOR_TRIAL
```

`ATTENTION_REQUIRED` 表示存在需要人工决定、状态来源对齐和仓库拓扑处理的事项，不表示任何子项目失败或不可用。

## 2. Observed Core Project Snapshot（核心项目观察快照）

以下 Git observation（Git 观察）来自 2026-07-21 的只读本地检查。`dirty_count` 只表示工作树条目数，不表示质量、完成度、发布状态或错误数量。

| project_id | branch | observed commit | worktree observation | remote observation | 规范状态摘要 |
|---|---|---|---|---|---|
| `DBA` | `main` | `91928e3b1096566aad5568124707e3a6cb3a40ca` | Owner 决策与 Apache-2.0 已推送 | public remote 可干净检出 | 317 个本地链接通过；Developer Preview 未发布 |
| `DBOS` | `main` | `0caa2c45e511a82d0dcab778b0ffc3163aac0029` | Apache-2.0 和 private trial boundary 已推送 | authenticated clean clone 通过；仓库保持 private | fresh install、331/331 tests、34/34 validators、两个 Demo 通过；不是 Agent Runtime |
| `SAEE` | public `main` | `2173c258f91aed03fc02c0097d4250a87be703aa` | exact 19-file public-safe extraction 与 Apache-2.0 已合并 | public remote 可干净检出；内部工作树另有未发布变化且未被使用 | 19/19 blob、public smoke/demo、8/8 tests 和 DBOS 只读 Adapter 通过；无写回或 authority |
| `RESEARCH-AGENT-PILOT` | `main` | `8445fe5d13cd889032c3786ba527d801f56d5351` | `dirty_count=30` | 未发现 `origin` | `V1_0_STATUS=INCOMPLETE_NOT_READY`；Agent、Runtime、Entity、Execution 均为 0 |

## 3. Architecture and Integration Status（架构与集成状态）

| surface | 状态 | 证据边界 |
|---|---|---|
| DBA / DBOS / SAEE responsibility boundary | `SPECIFICATION_DEFINED` | DBA Stack、Governance、Interface 和 ADR 文档 |
| DBA Program Governance cockpit | `BASELINE_VALIDATED_IN_WORKTREE` | 驾驶舱工件与 `PROGRAM-GOVERNANCE-BASELINE-AUDIT.md`；未 commit、未发布 |
| DBOS → SAEE data contract | `SCOPED_LOCAL_CONFORMANCE_PASS` | DBOS 同一 synthetic envelope 被 SAEE 只读消费；不是生产集成 |
| SAEE → DBOS recommendation contract | `SCOPED_LOCAL_RECOMMENDATION_PASS_NO_WRITEBACK` | `HOLD` / `STOP` 是建议上下文；没有 DBOS 写回、Decision 或 Command |
| Governance Decision implementation | `NOT_ASSESSED` | DBA 仅定义逻辑层和对象边界 |
| Digital Entity admission / registration | `SPECIFICATION_DEFINED_CROSS_REPO_CONFORMANCE_NOT_ASSESSED` | 规范存在；不推断当前 DBOS 实现状态 |
| Research Agent DBOS connection | `PREPARED_ONLY` | Pilot README 的当前状态 |
| Research Agent SAEE connection | `PREPARED_ONLY` | Pilot README 的当前状态 |
| End-to-end governed evolution loop | `NOT_VERIFIED` | 本阶段只验证 synthetic record-to-evaluation 链；没有真实 Execution、Verified Evidence、Decision 或 Adoption 闭环 |
| Developer Preview public entry | `WEBSITE_CANDIDATE_DEPLOYED_NOT_RELEASED` | `redcrag.cn`、`PUBLIC-WEBSITE-DEPLOYMENT-REPORT.md`、ADR-019 与 GitHub website prerelease |
| DBOS local developer path | `SCOPED_LOCAL_CONFORMANCE_PASS` | local editable install、单一 runner、331/331 tests、34/34 validators |
| Multi-Agent Trust Demo | `LOCAL_DETERMINISTIC_PASS` | 3 个角色模拟、3 个执行记录、3 个证据引用、9 个结构 Validation；无 Agent/Runtime |
| SAEE Evaluation Layer v0.1 | `LOCAL_READ_ONLY_PASS` | 8/8 adapter tests；Reliability/Stability fail closed；Risk/Recommendation 复用现有 evaluator |
| Optional Human Developer Trial | `SUPERSEDED_AS_PRIMARY_GATE_NOT_EXECUTED` | 历史技术包仍保留；参与者 0；不再阻塞首要 agent-native 路线 |
| Clean Clone Validation | `PASS_FROZEN_REMOTE_SOURCES` | DBA、DBOS、SAEE 与只读 Adapter 全通过；见 `CLEAN-CLONE-VALIDATION-REPORT.md` |
| Agent Customer Validation | `PASS_BOUNDARY_AWARE_CONDITIONAL_RECOMMENDATION` | 修复后千帆／方舟 12/12 会话和全部预冻结阈值通过；12/12 overall verdict 为边界正确的 `CONDITIONAL`；不是客户采用或发布 |

## 4. Active Decisions and Blockers（当前决策与阻塞）

- `DQ-002`：决定 DBA 独立仓库根目录与当前父级 Git 根目录之间的拓扑；
- `DQ-003`：确认 DBOS、SAEE、Research Agent Pilot 的 canonical status source；
- `DQ-004`：选择第一个跨项目 conformance（符合性）里程碑；
- `DQ-008`：决定当前驾驶舱与既有 DBA public meaning layer 的规范关系和单一前门；
- `DQ-009`：最终 Developer Preview Release（开发者预览版发布）仍需 DBOS access/distribution 决定、开放网络发现限制的处理决定、`R-015` 复核和 `released_by_ref`；
- `DQ-001`、`DQ-011`、`DQ-012`、`DQ-014` 已由 `ADR-020` 关闭；
- `DQ-010` 的人类参与者路径已由 `ADR-021` 标记为 `SUPERSEDED_FOR_PRIMARY_ROUTE`，没有被改写成执行通过；
- `DQ-015` 已接受 agent-native customer validation，并完成 12/12 会话基线；
- `DQ-013` 已由 `ADR-019` 标记为 `SUPERSEDED`；
- `B-001` 已由 `ADR-020` 解除；Program Owner 是 `zhangbin`，不产生运行、演化或发布权；
- `B-002`：DBA Git 根目录不是 DBA 目录本身，影响仓库边界和远端展示；
- `B-003`：核心项目状态入口尚未统一，阻止可靠自动汇总。
- `B-005`：两个 DBA 语义表面尚未完成 canonical reconciliation（规范对齐），阻止对外声明唯一入口。
- `B-006` 已在当前本地工作树中通过 version-aware historical binding（版本感知历史绑定）处理，34/34 validators 通过；历史 Evidence 未改写。该缓解尚未形成发布版本。
- `B-007` 已解除：三个远端 source commits 已冻结，SAEE 19/19 blob 与完整 Clean Clone 已通过。
- `B-009` 已由 `TMAI-ACV-20260722-002` 解除；真实运行使用仍受 `B-010`（DBOS private、无公开调用路径）阻塞。
- `B-011`：`TMAI-OWD-20260722-001` 只观察到 GitHub 完整新描述命中；规范英文名、中文名和公开搜索仍无精确项目命中。

详细信息见 [`DECISION-QUEUE.md`](DECISION-QUEUE.md) 和 [`RISK-AND-BLOCKER-REGISTER.md`](RISK-AND-BLOCKER-REGISTER.md)。

## 5. Next Program Actions（下一步项目群行动）

1. 保留基线 `001=CONDITIONAL` 与复测 `002=PASS` 的全部原始回答、评分和失败历史；
2. 由 Human Owner 单独决定 DBOS 的 agent access／distribution 路线；
3. 在外部索引刷新窗口后用规范英文名／中文名复查 `TMAI-OWD-20260722-001`，或由 Human Owner 显式接受 Developer Preview 的发现限制；
4. 复核网站依赖风险 `R-015`；
5. 以上输入完成后，把 `DQ-009` 提交明确 `released_by_ref` 的人工发布决定。

## 6. Refresh Protocol（刷新协议）

每次快照更新必须：

- 记录 `observed_at`；
- 记录项目路径、branch、commit 和工作树是否有变化；
- 读取项目明确声明的 canonical status source；
- 保留冲突和未知，不根据文件数量或测试数量推断成熟度；
- 不在 DBA 中修改子仓库状态；
- 将过期快照标记为 `STALE`，不得静默覆盖历史。

```text
SNAPSHOT_IS_CURRENT_TRUTH=false
SNAPSHOT_IS_POINT_IN_TIME=true
DIRTY_COUNT_IS_QUALITY_SCORE=false
STATUS_AGGREGATION_CHANGES_CHILD_TRUTH=false
```
