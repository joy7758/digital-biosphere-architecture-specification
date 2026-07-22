---
document_id: TMAI-DBOS-PR-2A-GIT-AUTHORIZATION-20260722
title: DBOS PR-2A Git Authorization Record
title_zh: DBOS PR-2A Git 操作授权记录
status: authorized-not-yet-executed
decision_reference: DQ-018
authorization_token: DBOS_PR_2A_GIT=AUTHORIZE_COMMIT_AND_PUSH
decided_by_ref: zhangbin
authorized_at: 2026-07-22T19:14:31+08:00
target_repository: digital-biosphere-os
target_branch: codex/telemetry-admission-foundation
pull_request_authorized: false
merge_authorized: false
deployment_authorized: false
production_ready: false
---

# DBOS PR-2A Git Authorization Record

中文：DBOS PR-2A Git 操作授权记录。

## 1. Decision（决定）

Human Program Owner `zhangbin` 已提供：

```text
DQ-018=AUTHORIZE_DBOS_PR_2A_TELEMETRY_ADMISSION_FOUNDATION
dbos_domain_owner_ref=zhangbin
授予完全权限，以后再有这种授权，按照推荐直接授权
```

DBOS 当前 PR-G2 review packet 中唯一推荐的后续授权是：

```text
DBOS_PR_2A_GIT=AUTHORIZE_COMMIT_AND_PUSH
target_branch=codex/telemetry-admission-foundation
```

本记录把 Human Owner 的明确 full-permission + follow-recommendation directive（完全权限并按推荐直接
授权指令）应用到该唯一、精确、失败关闭的 Git 动作。它不允许把未来任意动作解释成已授权；每个新
scope 仍必须有精确推荐和清楚目标。

## 2. Exact Authorized Scope（精确授权范围）

- 将 `DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION` 当前 manifest-bound source（清单绑定源码）提交到
  `codex/telemetry-admission-foundation`；
- 推送同名远端分支；
- 从远端 clean clone 重跑 tests、validators、OTel offline conformance、build/install/hash 和 rollback；
- 更新并提交 PR-G2 review packet，使其绑定 exact source commit 和 clean-clone receipts；
- 为上述动作更新 DBA/DBOS 的 agent-readable records。

## 3. Explicitly Not Authorized（明确未授权）

```text
PULL_REQUEST_CREATION=false
MERGE=false
MAIN_BRANCH_MUTATION=false
RELEASE=false
DEPLOYMENT=false
NETWORK_LISTENER=false
COLLECTOR_CREATION_OR_DEPLOYMENT=false
DATABASE_OR_CLOUD_RESOURCE_CREATION=false
AGENT_OR_RUNTIME_CREATION=false
ENTITY_CAPABILITY_PERMISSION_EXECUTION_CREATION=false
EVIDENCE_OR_VERIFICATION_CREATION=false
SAEE_INVOCATION=false
PRODUCTION_READY_CLAIM=false
```

Commit/push 只使源码远端可追溯，不产生 PR-G2 Human Approval、DQ-019、DQ-020、DQ-021、部署或生产状态。

## 4. Preconditions and Stop Rules（前置条件和停止规则）

1. DBA 当前 production branch 必须先提交并推送本授权记录；
2. DBOS branch 必须继续基于 `cd3f867c4379ec555c45e7d554088ad12ce08a24`，且当前实现 manifest
   在源码提交前仍为 `sha256:f09e99b95a3332d40abc933eaee35ea8a646b11d330ffaa5213ee0bb28f339b4`；
3. 只暂存 DQ-018 exact source/test/report scope，不包含主工作树 `reports/reference-runs/`；
4. push 前重取远端并拒绝非 fast-forward；禁止 force push；
5. clean clone 任一必需验证失败则停止在当前阶段，不更新为 PR-G2 ready；
6. implementation source commit 与后续 receipt-only commit 分开绑定，避免循环自引用。

## 5. Current Effect（当前效果）

```text
DBOS_COMMIT_AUTHORIZED=true
DBOS_PUSH_AUTHORIZED=true
DBOS_COMMIT_EXECUTED=false
DBOS_PUSH_EXECUTED=false
PR_G2_APPROVED=false
PRODUCTION_READY=false
```
