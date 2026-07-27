---
document_id: DBA-TITMAS-CE-G10A-BRANCH-SCOPED-TRIGGER-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G10A Branch-Scoped Trigger Remediation Recommendation v0.1
title_zh: TITMAS CE-G10A 分支限定触发修正建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-recommended-decision-pending
maturity: Development
maturity_scope: ce-g10-github-actions-trigger-mechanism-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G10A Branch-Scoped Trigger Remediation Recommendation v0.1

## 1. Problem

CE-G10 workflow 已在 commit
`3f243b265294fc3c41659adbcff44ffc9508dbb7` 远端存在，但只位于
`codex/production-observability-baseline`。仓库 default branch 是 `main`，GitHub 不提供
该 workflow 的 manual dispatch endpoint。

Preflight 已失败关闭，dispatch 和 workflow run 均为 0。

## 2. Recommendation

只修正 trigger mechanism（触发机制）：

1. 移除无效的 `workflow_dispatch`；
2. 增加只匹配 validation branch 与一个 exact run-request path 的 `push` trigger；
3. 增加 strict run-request Schema 和 runner validation；
4. 先提交 trigger implementation，不创建 run-request，因此不触发；
5. 独立验证远端 workflow 后，再单独提交一次 immutable run-request；
6. 保存单次 run、五个 artifacts 和 aggregate result；失败不重试。

Exact trigger：

```text
event=push
branch=codex/production-observability-baseline
path=digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g10-run-request.v0.1.json
trigger_events_cap=1
workflow_runs_cap=1
matrix_jobs=5
retry=false
```

## 3. Agent-customer review

Alibaba Cloud Model Studio `qwen3.7-plus`：

```text
VERDICT=RECOMMENDED
RECOMMENDED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
CONFIDENCE=0.95
```

Blocking corrections 均纳入：

- branch-scoped exact path；
- run-request 只提交一次并包含 frozen hashes；
- exact five-version matrix、read-only permissions、pinned actions、no secrets；
- 不产生 TITMAS public-site request、SSH、server access、deployment 或 retry；
- 保留 run 和 artifacts。

## 4. Proposed exact paths

后续独立 Decision 才可授权：

```text
.github/workflows/titmas-ce-g10-correlator-cross-version.yml
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce_g10_cross_version_runner.py
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/test_ce_g10_cross_version_runner.py
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g10-run-request.schema.v0.1.json
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g10-run-request.v0.1.json
```

Correlator、CE-G9 test、fixtures、Python matrix 和 action SHA 不变。Result Schema
只允许把原 `dispatches` accounting 精确改为 `trigger_event=push`、
`trigger_events=1`、`manual_dispatches=0`；不得改变评价范围或 non-claims。

## 5. Two-commit execution

### Commit A — trigger implementation

- 修改 workflow trigger；
- runner 增加 strict request validation；
- 新增 request Schema；
- tests 验证 branch/path、exact matrix、no retry 和 frozen hashes；
- 不包含 request instance，所以 workflow runs 必须保持 0。

### Commit B — one run request

Request 固定：

- CE-G10 与 CE-G10A decision references；
- Commit A full hash；
- five exact Python patch versions；
- five CE-G9 frozen input hashes；
- `trigger_events_cap=1`；
- `retry=false`；
- all external/server/deployment caps = 0。

Commit B 的 push 是唯一获准 trigger event。

## 6. Stop rules

- Commit A push 意外触发 workflow；
- workflow trigger 超出 exact branch/path；
- request 在 Commit A 之前出现；
- request Schema 或 runner validation 不通过；
- frozen input、matrix、action、permission 或 timeout 漂移；
- credential 被传入 test process；
- public-site request、SSH、server access、deployment、DBOS/SAEE change；
- 任一 run、job、artifact 或 aggregate failure；
- 任何 retry、fallback 或 result repair；
- 任何 TLS、production、certification、SLA 或 commercial claim。

## 7. Effects

```text
MAIN_MERGE=false
DEFAULT_BRANCH_CHANGE=false
CE_G10_SCOPE_CHANGE=false
TRIGGER_MECHANISM_CHANGE=true
WORKFLOW_RUN_AUTHORIZED=false
RUN_REQUEST_AUTHORIZED=false
CE_G10_EXECUTION_COMPLETED=false
```

本建议不是 Decision。下一步只允许 independent review 与 Decision。
