---
document_id: DBA-PROGRAM-STATUS-2026-07-21
title: Digital Biosphere Program Status Snapshot
title_zh: 数字生物圈项目群状态快照
status: observed-governance-snapshot-owner-decisions-recorded
observed_at: 2026-07-21
freshness: point-in-time
release_status: website-candidate-published-developer-preview-not-released
developer_preview_status: website-live-clean-clone-remediation-required
source_policy: direct-read-only-observation
---

# Digital Biosphere Program Status Snapshot（数字生物圈项目群状态快照）

## 1. Executive Status（总览状态）

```text
PROGRAM_ID=DIGITAL_BIOSPHERE
PROGRAM_PHASE=TRUSTED_MULTI_AGENT_INFRASTRUCTURE_WEBSITE_CANDIDATE_AND_RELEASE_GATING
PROGRAM_HEALTH=ATTENTION_REQUIRED
CURRENT_MILESTONE=DP-CCV
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
EXTERNAL_DEVELOPER_TRIAL_PLAN_DEFINED=true
EXTERNAL_DEVELOPER_TRIAL_CONDITIONALLY_AUTHORIZED=true
EXTERNAL_DEVELOPER_TRIAL_EXECUTION_AUTHORIZED=false
EXTERNAL_CONTACT_AUTHORIZED=false
PARTICIPANT_SOURCE_CONFIRMED=false
EXTERNAL_DEVELOPER_VALIDATION_COMPLETE=false
EXTERNAL_DEVELOPER_PARTICIPANTS=0
DBA_REMOTE_BASELINE_CREATED=true
DBOS_REMOTE_BASELINE_CREATED=true
DBA_CLEAN_CLONE_PASS=true
DBOS_CLEAN_CLONE_PASS=true
SAEE_PUBLIC_CLEAN_CLONE_PASS=true
SAEE_DBOS_ADAPTER_CLEAN_CLONE_PASS=false
CROSS_PROJECT_CLEAN_CLONE_PASS=false
PUBLIC_WEBSITE_DEPLOYED=true
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
| `DBA` | `main` | `366a312f91a3efe173732e18d3f8d9436e5c102d` | source commit 已推送；`ADR-020` 当前在隔离 release-preparation branch 中 | `origin/main` 包含双语网站、部署报告和网站候选 prerelease | Owner 决策已记录但尚未形成新远端基线；Developer Preview 未发布 |
| `DBOS` | `main` | `b4e3cbe2af442be861dbab3f7b2ffd2567443077` | source commit 已推送 | `origin/main` 可干净检出；仓库当前为 private | fresh install、331/331 tests、34/34 validators、两个 Demo 通过；不是 Agent Runtime |
| `SAEE` | public `main` | `e503c22109bdb7c83dc465d66e2a22760a3c8d90` | public source 可干净检出；内部工作树另有未发布变化 | `origin/main` 是裁剪公共产品层 | public smoke/demo 通过；DBOS Developer Preview Adapter 不在公共 source，跨项目 gate 失败 |
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
| External Developer Trial Preparation | `PLAN_DEFINED_TRIAL_NOT_AUTHORIZED` | Trial Plan、Guide、Feedback Template、Conformance Report 与 ADR-018 已形成；参与者 0、无外部试用 |
| Clean Clone Validation | `FAIL_REQUIRED_SAEE_ADAPTER_MISSING` | DBA 与 DBOS 全通过；SAEE public source 缺少必需 Adapter；见 `CLEAN-CLONE-VALIDATION-REPORT.md` |

## 4. Active Decisions and Blockers（当前决策与阻塞）

- `DQ-002`：决定 DBA 独立仓库根目录与当前父级 Git 根目录之间的拓扑；
- `DQ-003`：确认 DBOS、SAEE、Research Agent Pilot 的 canonical status source；
- `DQ-004`：选择第一个跨项目 conformance（符合性）里程碑；
- `DQ-008`：决定当前驾驶舱与既有 DBA public meaning layer 的规范关系和单一前门；
- `DQ-009`：最终 Developer Preview Release（开发者预览版发布）仍需 Trial Result 和 `released_by_ref`；
- `DQ-001`、`DQ-011`、`DQ-012`、`DQ-014` 已由 `ADR-020` 关闭；
- `DQ-010` 已形成条件决定：Clean Clone、试用包、真实参与者来源、隐私和停止规则全部满足后才生效；
- `DQ-013` 已由 `ADR-019` 标记为 `SUPERSEDED`；
- `B-001` 已由 `ADR-020` 解除；Program Owner 是 `zhangbin`，不产生运行、演化或发布权；
- `B-002`：DBA Git 根目录不是 DBA 目录本身，影响仓库边界和远端展示；
- `B-003`：核心项目状态入口尚未统一，阻止可靠自动汇总。
- `B-005`：两个 DBA 语义表面尚未完成 canonical reconciliation（规范对齐），阻止对外声明唯一入口。
- `B-006` 已在当前本地工作树中通过 version-aware historical binding（版本感知历史绑定）处理，34/34 validators 通过；历史 Evidence 未改写。该缓解尚未形成发布版本。
- `B-007`：DBA 与 DBOS source commits 已形成；SAEE Adapter 仍仅存在于内部工程历史，public `main` 无该入口，因此跨项目 source freeze 尚未完成。

详细信息见 [`DECISION-QUEUE.md`](DECISION-QUEUE.md) 和 [`RISK-AND-BLOCKER-REGISTER.md`](RISK-AND-BLOCKER-REGISTER.md)。

## 5. Next Program Actions（下一步项目群行动）

1. 在三个仓库采用 `Apache-2.0`，保留第三方许可边界；
2. 按冻结 blob ID 在隔离分支实现 SAEE 精确 19 文件 public-safe extraction；
3. 保持 DBOS private，并冻结 private collaborator trial 的远端 source commit；
4. 使用三个最终远端 commit 重跑完整 Clean Clone；
5. 整体通过后冻结 `trial_package_id`、隐私说明和停止规则；
6. 等待真实 `participant_source`，再使 `DQ-010` 条件授权生效并联系 3–5 名开发者；
7. Trial Result 完成后再处理 `DQ-009`；Pilot 自身 gate 通过前保持 Research Agent Prototype 为 `NOT_READY`。

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
