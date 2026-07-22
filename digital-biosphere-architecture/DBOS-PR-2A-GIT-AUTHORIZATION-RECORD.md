---
document_id: TMAI-DBOS-PR-2A-GIT-AUTHORIZATION-20260722
title: DBOS PR-2A Git Authorization Record
title_zh: DBOS PR-2A Git 操作授权记录
status: authorized-and-executed
decision_reference: DQ-018
authorization_token: DBOS_PR_2A_GIT=AUTHORIZE_COMMIT_AND_PUSH
decided_by_ref: zhangbin
authorized_at: 2026-07-22T19:14:31+08:00
executed_at: 2026-07-22T19:35:08+08:00
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
2. DBOS branch 必须继续基于 `cd3f867c4379ec555c45e7d554088ad12ce08a24`，且 corrected exact source
   manifest 在源码提交前仍为 `sha256:9a8c3546a925812f0da86dad6cd09aa4680b2b29b734cd07dcfa9bc51f8dfe95`；
3. 只暂存 DQ-018 exact source/test/report scope，不包含主工作树 `reports/reference-runs/`；
4. push 前重取远端并拒绝非 fast-forward；禁止 force push；
5. clean clone 任一必需验证失败则停止在当前阶段，不更新为 PR-G2 ready；
6. implementation source commit 与后续 receipt-only commit 分开绑定，避免循环自引用。

## 5. Manifest Scope Correction（清单范围修正）

授权记录首次推送后、DBOS 源码提交前的 staged-vs-manifest reconciliation（暂存与清单对账）发现：

```text
previous_manifest=sha256:f09e99b95a3332d40abc933eaee35ea8a646b11d330ffaa5213ee0bb28f339b4
previous_files=53
missing_source_class=3 SQL migration files
corrected_manifest=sha256:9a8c3546a925812f0da86dad6cd09aa4680b2b29b734cd07dcfa9bc51f8dfe95
corrected_files=56
corrected_bytes=704010
```

原因是旧 `source_manifest()` 的 glob 覆盖 Python/JSON/YAML/Markdown，但遗漏
`dbos/telemetry_admission/**/*.sql`。SQL migrations 是 DQ-018 实现源码，不能排除。提交前已：

1. 增加 SQL source pattern；
2. 重新计算 manifest；
3. 确认 expected files `56` 与 staged files `56` 完全相同；
4. 将旧 `f09e99…` 及其回执保留为 historical incomplete-scope receipts（历史不完整范围回执）；
5. 要求从 corrected source commit 重跑所有验证。

该修正不扩大 DQ-018 功能，只修复 source provenance completeness（源码来源完整性）。Human Owner 的
commit/push 授权继续适用于同一 exact slice；不产生新的运行或生产权限。

## 6. Execution Receipt（执行回执）

```text
DBA_AUTHORIZATION_COMMIT=7f2d3a0e39f65a92b7a96ea899ca12e3c050a0db
DBOS_SOURCE_COMMIT=a3e491c954e911d84baa09fd6d9466fb80280941
DBOS_RECEIPT_COMMIT=5f437b0719936470535211b796af3e9722e8f11b
REMOTE_BRANCH=codex/telemetry-admission-foundation
CLEAN_CLONE_RESULT=PASS
PR_G2_READY_FOR_HUMAN_REVIEW=true
PR_G2_APPROVED=false
```

源码 commit 与 receipt-only commit 已分别以非强制 push 推送到远端同名分支。远端精确源码
干净检出结果包括：523/523 tests、189/189 telemetry tests、35/35 validators、25/25
telemetry validator checks、OTel authorized subset 32/32 + 36/36、rollback PASS，以及两个
独立远端检出的 byte-identical wheel。

对应 DBOS review packet 位于
`reports/telemetry-admission-foundation/DBOS-PR-2A-PR-G2-REVIEW-PACKET-2026-07-22.json`
并明确保持 `production_ready=false`。

## 7. Current Effect（当前效果）

```text
DBOS_COMMIT_AUTHORIZED=true
DBOS_PUSH_AUTHORIZED=true
DBOS_COMMIT_EXECUTED=true
DBOS_PUSH_EXECUTED=true
PR_G2_READY_FOR_HUMAN_REVIEW=true
PR_G2_APPROVED=false
PRODUCTION_READY=false
```
