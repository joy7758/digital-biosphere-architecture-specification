---
document_id: DBA-DEVELOPER-PREVIEW-RELEASE-PLAN-0.1
title: Trusted Multi-Agent Infrastructure Developer Preview Release Plan v0.1
title_zh: 可信多智能体基础设施开发者预览发布计划 v0.1
status: release-plan-not-release
target_release: trusted-multi-agent-infrastructure-developer-preview-v0.1
release_authorized: false
deployment_authorized: false
last_reviewed: 2026-07-21
---

# Trusted Multi-Agent Infrastructure Developer Preview Release Plan v0.1（可信多智能体基础设施开发者预览发布计划 v0.1）

## 1. Release Semantics（发布语义）

本文件定义如何判断和形成 Developer Preview release（开发者预览发布），本身不是 Release、Deployment（部署）或 Adoption（采用）。

```text
PLAN_NE_RELEASE=true
RELEASE_NE_DEPLOYMENT=true
RELEASE_NE_ADOPTION=true
DEVELOPER_PREVIEW_NE_PRODUCTION_READY=true
VERSION_NE_IMPLEMENTATION=true
```

## 2. Release Candidate Contents（候选发布内容）

| deliverable | Owner | 必须存在 | 不得暗示 |
|---|---|---|---|
| Public Project Overview | DBA | 定位、架构、事实边界、导航 | 三仓库合并或 DBA 是产品 Runtime |
| DBOS Local Package Path | DBOS | 可复制安装、锁定依赖或明确版本、单一测试入口 | 已发布 PyPI package（Python 包） |
| Multi-Agent Trust Demo | Demo + DBOS | 三角色、记录链、负向边界、确定性运行 | 生产 Agent 或真实外部执行 |
| SAEE Evaluation Layer | SAEE | 四类输出、数据来源、局限、只读接口 | 自动决策或 DBOS 控制权 |
| Agent Customer Validation Protocol | DBA | 多 Provider／model 画像、公开与冻结上下文、正负场景、预冻结阈值 | 模型推荐等于采用或发布授权 |
| Agent Customer Package and Result | DBA | 机器发现、精确公开验证命令、组合流、适用／不适用规则、原始回答与评分 | 给定 URL 等于开放网络自然发现，或规范等于 Runtime |
| Conformance Report | DBA aggregation（聚合） | 命令、版本、测试、validator、已知限制 | 子项目 capability truth 被 DBA 改写 |
| Test-to-Feature Ledger | DBA aggregation；功能归责任仓库 | 失败测试、归属、重复审查、最小功能和回归结果 | 测试失败自动授权功能或 Demo 成为 canonical implementation |

## 3. Release Lifecycle（发布生命周期）

```text
DRAFT
  -> INTERNAL_REVIEW
  -> RELEASE_CANDIDATE
  -> VALIDATED
  -> AGENT_CUSTOMER_VALIDATION
  -> AGENT_VALIDATION_REVIEW
  -> RELEASE_DECISION
  -> RELEASED
  -> DEPRECATED
  -> ARCHIVED
```

状态变化必须保留 `decision_reference`、`source commits`、`validation evidence`、`known limitations` 和 `released_by_ref`。`VALIDATED` 不自动进入 `RELEASED`。

## 4. Release Gate Checklist（发布闸门清单）

- [x] DBA 公开入口无孤立子项目叙事，且所有链接有效；
- [x] DBOS 从临时隔离 Python 环境按本地 editable install（可编辑安装）命令安装并运行；
- [x] DBOS 全部适用 validator 和测试通过；
- [x] 所有测试触发的功能都有 Owner、duplicate review（重复审查）和回归结果；
- [x] `DBOS-EXP-0001` 历史 Evidence 未修改；
- [x] 三角色 Demo 可确定性重放并保留失败路径；
- [x] DBOS 记录链不推导 Permission、Truth 或 Capability Grant；
- [x] SAEE 输入只来自声明的 DBOS 输出契约；
- [x] SAEE 输出只含 Evaluation / Recommendation，不含 Command；
- [x] DBOS output / SAEE input 跨项目 conformance tests 通过；
- [x] 无 Agent、Runtime、Entity、Permission、Digital Organism 生产实例；
- [x] Agent Customer Validation Protocol、预先冻结成功标准和 ADR-021 已准备；
- [x] 首轮 12/12 Agent API sessions 已完成并保留原始回答；
- [x] DBA、DBOS、SAEE source commits 已冻结并分配 `trial_package_id`；
- [x] clean-clone validation 已对同一冻结版本通过；
- [x] 四项 agent-readable 失败阈值已修复并用 `TMAI-ACV-20260722-002` 复测；
- [x] Agent Customer Validation Result 达到 `PASS`；12/12 overall verdict 保持边界正确的 `CONDITIONAL`；
- [x] 使用真实公开搜索与 GitHub repository search 单独观察自然发现，结果保留为 `NOT_OBSERVED`；
- [ ] 元数据修复后观察到外部索引刷新，或 Human Owner 显式接受 Developer Preview 的发现限制；
- [ ] DBOS agent access／distribution 路线已有明确 Human Decision；
- [ ] Human Release Decision（人工发布决策）包含明确 `released_by_ref`；
- [ ] release notes（发布说明）区分本地预览、发布、部署和采用。

以上勾选仅表示当前本地工作树的 release candidate（候选发布）材料满足对应检查，不表示 source commits、干净 clone、外部试用或发布已经完成。

## 5. Current Release Assessment（当前发布判断）

```text
RELEASE_STATUS=NOT_READY
PUBLIC_ENTRY_DRAFTED=true
DBOS_EXAMPLES_LOCALLY_RUN=true
DBOS_TESTS=331_PASS
DBOS_FULL_VALIDATOR_SUITE=34_PASS
MULTI_AGENT_TRUST_DEMO_LOCAL=true
SAEE_EVALUATION_LAYER_LOCAL=true
CROSS_PROJECT_CONFORMANCE_LOCAL=PASS
EXTERNAL_TRIAL_GUIDE_READY=true
EXTERNAL_TRIAL_PLAN_READY=true
DBA_SOURCE_COMMIT_READY=true
DBOS_SOURCE_COMMIT_READY=true
SAEE_PUBLIC_ADAPTER_SOURCE_READY=true
CLEAN_CLONE_VALIDATED=true
CLEAN_CLONE_RESULT=PASS_FROZEN_REMOTE_SOURCES
AGENT_CUSTOMER_VALIDATION_ID=TMAI-ACV-20260721-001
AGENT_CUSTOMER_API_SESSIONS=12
AGENT_CUSTOMER_VALIDATION_BASELINE_RESULT=CONDITIONAL
AGENT_CUSTOMER_RERUN_ID=TMAI-ACV-20260722-002
AGENT_CUSTOMER_VALIDATION_RESULT=PASS
AGENT_CUSTOMER_REMEDIATION_REQUIRED=false
AGENT_CUSTOMER_RERUN_COMPLETE=true
OPEN_WEB_DISCOVERY_OBSERVATION_ID=TMAI-OWD-20260722-001
OPEN_WEB_DISCOVERY_RESULT=NOT_OBSERVED
GITHUB_DISCOVERY_METADATA_REMEDIATED=true
OPEN_WEB_REINDEX_OBSERVED=false
HUMAN_DEVELOPER_TRIAL_REQUIRED=false
DBOS_AGENT_ACCESS_DECIDED=false
RELEASE_AUTHORIZED=false
```

阻塞原因：

1. DBOS 仍为 private，AI agent 没有公开 package、API 或自主获取路径；
2. `OPEN_WEB_DISCOVERY=NOT_OBSERVED`；GitHub 元数据已修复，但尚未观察到重新索引或显式限制接受；
3. `R-015` 仍需正式发布风险复核；
4. `DQ-009` 尚无 Human Release Decision 与 `released_by_ref`。

## 6. Rollback and Preservation（回退与保留）

Developer Preview 发布失败或撤销时：

- 保留 release candidate、失败日志和版本引用；
- 不删除旧 Evidence、Evaluation 或 negative result（负向结果）；
- 发布入口退回 `NOT_READY` 或 `DEPRECATED`，不改写历史；
- DBOS、SAEE 和 DBA 各自保留自己领域的事实；
- Demo 数据可清理，但清理动作必须只针对明确生成的临时目录，不触及规范台账。
