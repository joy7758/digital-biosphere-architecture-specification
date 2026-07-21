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
| External Developer Trial Plan | DBA | 3–5 人画像、流程、理解／使用／价值指标、成功标准、试用到发布的 gate | 计划等于试用执行或客户验证 |
| Trial Guide and Session Record | DBA / Developer Experience | 操作步骤、自由回答、评分 rubric、隐私和清理说明 | 参与者反馈等于采用、认证或 SLA（服务等级协议） |
| Conformance Report | DBA aggregation（聚合） | 命令、版本、测试、validator、已知限制 | 子项目 capability truth 被 DBA 改写 |
| Test-to-Feature Ledger | DBA aggregation；功能归责任仓库 | 失败测试、归属、重复审查、最小功能和回归结果 | 测试失败自动授权功能或 Demo 成为 canonical implementation |

## 3. Release Lifecycle（发布生命周期）

```text
DRAFT
  -> INTERNAL_REVIEW
  -> RELEASE_CANDIDATE
  -> VALIDATED
  -> EXTERNAL_TRIAL
  -> TRIAL_REVIEW
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
- [x] 外部试用指南和反馈入口已准备；
- [x] External Developer Trial Plan、预先冻结成功标准和 ADR-018 已准备；
- [ ] DBA、DBOS、SAEE source commits 已冻结并分配 `trial_package_id`；
- [ ] clean-clone validation 通过且参与者可获得同一版本；
- [ ] `DQ-010` 已授权试用执行和外部联系；
- [ ] 3–5 名合格外部 Agent Developer 已完成试用并保留失败记录；
- [ ] Trial Result Report 已按 `PASS|CONDITIONAL|FAIL|INCOMPLETE` 完成复核；
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
SAEE_PUBLIC_ADAPTER_SOURCE_READY=false
CLEAN_CLONE_VALIDATED=false
CLEAN_CLONE_RESULT=FAIL_REQUIRED_SAEE_ADAPTER_MISSING
TRIAL_PACKAGE_READY=false
TRIAL_EXECUTION_AUTHORIZED=false
EXTERNAL_CONTACT_AUTHORIZED=false
EXTERNAL_TRIAL_PARTICIPANTS=0
EXTERNAL_TRIAL_EXECUTED=false
EXTERNAL_TRIAL_RESULT=NOT_ASSESSED
RELEASE_AUTHORIZED=false
```

阻塞原因：

1. DBA 与 DBOS source commits 已形成，但 SAEE public `main` 不含必需 DBOS Adapter；
2. Clean Clone 中 DBA、DBOS 通过，SAEE Adapter 失败；
3. `DQ-011` 尚未决定安全的 SAEE Adapter 公开／分发边界；
4. `DQ-010` 尚未授权试用执行、参与者联系或反馈收集；
5. 3–5 名外部开发者试用和 Trial Result Report 尚未发生；
6. `DQ-009` 尚无 Human Release Decision 与 `released_by_ref`。

## 6. Rollback and Preservation（回退与保留）

Developer Preview 发布失败或撤销时：

- 保留 release candidate、失败日志和版本引用；
- 不删除旧 Evidence、Evaluation 或 negative result（负向结果）；
- 发布入口退回 `NOT_READY` 或 `DEPRECATED`，不改写历史；
- DBOS、SAEE 和 DBA 各自保留自己领域的事实；
- Demo 数据可清理，但清理动作必须只针对明确生成的临时目录，不触及规范台账。
