---
document_id: DBA-TITMAS-CE-G12-READ-ONLY-PREFLIGHT-REPORT-0.1
title: TITMAS CE-G12 Read-only Preflight Report v0.1
title_zh: TITMAS CE-G12 只读预检报告 v0.1
version: 0.1.0
status: fail-closed-current-target-mismatch-redeployment-decision-not-authorized
maturity: Development
maturity_scope: ce-g12-read-only-server-preflight
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-P
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Read-only Preflight Report v0.1

## Result

```text
CE_G12_PREFLIGHT_EXECUTED=true
CE_G12_PREFLIGHT_RESULT=FAIL_CLOSED
FAILURE_STAGE=P02_CURRENT_TARGET
SSH_SESSIONS=1/1
SERVER_WRITES=0
PUBLIC_REQUESTS=0
RETRIES=0
REDEPLOYMENT_DECISION_ALLOWED=false
```

Machine result：

[`ce-g12-read-only-preflight-result.v0.1.json`](commercial-evaluation-exact-redeployment/ce-g12-read-only-preflight-result.v0.1.json)

## Exact observation

Decision-bound expected current target：

```text
/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
```

唯一 SSH session 成功读取 `/srv/tmai/current`，但值不等于上述 expected target，因此在
`P02_CURRENT_TARGET` 立即失败关闭。

failure handler 没有输出或持久化实际 target。当前 canonical truth 只能记录：

```text
CURRENT_TARGET_MATCH=false
ACTUAL_CURRENT_TARGET=UNKNOWN_NOT_PERSISTED
```

不能从 mismatch 推断当前是 proposed release、其他 release、broken symlink 或恶意状态。

## Checks executed

| Check | Result |
|---|---|
| P01 local SSH binding | PASS：`hongyan-4cj → root@180.76.115.193:22`，`identitiesonly=yes` |
| P02 current symlink | FAIL_CLOSED：target mismatch |
| P03 release directory shape | NOT_EXECUTED |
| P04 archive bytes/hash | NOT_EXECUTED |
| P05 manifest file count | NOT_EXECUTED |
| P06 11 route file hashes | NOT_EXECUTED |
| P07 `nginx -t` | NOT_EXECUTED |
| P08 log readability | NOT_EXECUTED |
| P09 `journalctl` availability | NOT_EXECUTED |
| P10 local correlation hashes | PASS before SSH |

P10 verified：

```text
BINDING_SCHEMA_SHA256=2263c3c224097f6d7ed233bd5ff261a6dd225e11f10e290d0d1dc4aa382be684
BINDING_FIXTURE_SHA256=cee58ceb4088ba99f4c0c5631a309898bf9c7df8a6d6ad64fc85ac920ad80f06
CORRELATOR_SHA256=b72ad6e707a95f65e20f235963306e04c4f3e81342f4c762514cffcbf7e2d0e3
```

## Boundary preservation

```text
RAW_LOG_READS=0
JOURNAL_CONTENT_READS=0
SOURCE_IP_READS=0
SERVER_ENVIRONMENT_DUMPS=0
CREDENTIAL_VALUES_PERSISTED=0
NGINX_RELOADS=0
SYMLINK_SWITCHES=0
SERVER_WRITES=0
PUBLIC_REQUESTS=0
DEPLOYMENTS=0
RELEASES=0
```

没有 retry、fallback、TLS bypass 或第二次 SSH。失败没有被覆盖或解释为 PASS。

## Consequence

CE-G12 Recommendation 的 fresh-current-target precondition 不成立：

```text
PREFLIGHT_PASS=false
PREFLIGHT_FRESHNESS_AVAILABLE=false
CE_G12_X_REDEPLOYMENT_DECISION_ALLOWED=false
REDEPLOYMENT_AUTHORIZED=false
```

PR #27 merge、post-merge repository validation、CE-G11 correlation adapter 和历史 CE-G7
rollback PASS 都不能覆盖当前 server target mismatch。

## New architecture issue

存在一个 current-target continuity gap（当前目标连续性缺口）：

> DBA historical baseline 记录 stable target，但 fresh read-only observation 表明 current
> symlink 已不同；实际 target 未在本次 failure receipt 中持久化。

这不是 deployment failure 证据，也不是 unauthorized change 证据。需要一个新的、exact、
read-only diagnostic Recommendation 决定是否值得执行一次 target-classification read，
并明确是否允许持久化 actual target 的 sanitized release identifier。

## Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_CURRENT_TARGET_MISMATCH_DIAGNOSTIC_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
SSH_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```

本报告不授权第二次 SSH、服务器读取/写入、symlink 修复、rollback、deployment 或
CE-G12-X Decision。
