---
document_id: DBA-TITMAS-CE-G12-CURRENT-TARGET-MISMATCH-DIAGNOSTIC-RECOMMENDATION-0.1
title: TITMAS CE-G12 Current-target Mismatch Diagnostic Recommendation v0.1
title_zh: TITMAS CE-G12 当前目标不匹配诊断建议 v0.1
version: 0.1.0
status: exact-read-only-recommendation-agent-review-required-decision-pending
maturity: Development
maturity_scope: current-symlink-target-classification-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Current-target Mismatch Diagnostic Recommendation v0.1

## 1. Recommendation

采用 **Option A：建立一次新的、独立授权的 current-target classification（当前目标分类）
只读诊断**。

```text
RECOMMENDED_OPTION=A
SECOND_FULL_PREFLIGHT_RECOMMENDED=false
SERVER_REPAIR_RECOMMENDED=false
ROLLBACK_RECOMMENDED=false
DIAGNOSTIC_DECISION_RECORDED=false
DIAGNOSTIC_EXECUTION_AUTHORIZED=false
```

目标只是回答：

> `/srv/tmai/current` 当前指向 stable、proposed、其他 canonical release，还是非 canonical
> target？

它不再次验证 archive/routes，不读取日志，不 reload，不修复或切换 symlink。

## 2. Direct failure evidence

CE-G12-P 唯一 preflight：

```text
RESULT=FAIL_CLOSED_READ_ONLY_PREFLIGHT_REDEPLOYMENT_DECISION_NOT_AUTHORIZED
FAILURE_STAGE=P02_CURRENT_TARGET
SSH_SESSIONS=1/1
SERVER_WRITES=0
PUBLIC_REQUESTS=0
RETRIES=0
```

直接材料：

- [Result](commercial-evaluation-exact-redeployment/ce-g12-read-only-preflight-result.v0.1.json)
  SHA-256 `d812f7a0ae8874da2520bcbd3d3b2f8d3434abd2245ea5cd324e64900b89280e`；
- [Report](TITMAS-CE-G12-READ-ONLY-PREFLIGHT-REPORT-v0.1.md)
  SHA-256 `f45d3477ee99f8d432c5e55673be25332e37f124bb5baea4732d53234d5882b9`；
- execution evidence commit `d91cb9928e042d1ead0326554ae414f8c4a1c9a4`。

failure handler 没有持久化 actual target，因此当前不能判断：

```text
ACTUAL_CURRENT_TARGET=UNKNOWN_NOT_PERSISTED
CURRENT_TARGET_IS_PROPOSED=UNKNOWN
CURRENT_TARGET_IS_OTHER_RELEASE=UNKNOWN
CURRENT_TARGET_IS_BROKEN=UNKNOWN
```

## 3. Why this diagnostic is necessary

直接继续 CE-G12-X 会违反 fresh-current-target precondition。直接重跑完整 preflight 会：

- 重复已消费的 P01–P10 contract；
- 在不知道 current target 的情况下继续读取大量 release bytes；
- 把诊断问题和 redeployment admission 混在一起。

最小诊断只读取 symlink target 和 target directory shape，可把未知状态收敛为一个受控分类，
同时保持 server writes 和 public requests 为 0。

## 4. Exact target and one-read scope

```text
HOST_ALIAS=hongyan-4cj
HOSTNAME=180.76.115.193
USER=root
PORT=22
IDENTITIES_ONLY=true
CURRENT_SYMLINK=/srv/tmai/current
EXPECTED_STABLE=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
EXPECTED_PROPOSED=/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
```

未来独立 Decision 最多授权：

1. 本地重新核对 `ssh -G hongyan-4cj`；
2. 一个 SSH session；
3. `lstat` 确认 `/srv/tmai/current` 是 symlink；
4. `readlink` 一次；
5. `test -d` 且 `test ! -L` 一次，只检查 target directory shape；
6. 输出一个 sanitized classification receipt；
7. 不执行其他服务器命令。

## 5. Allowed classifications

按顺序分类：

```text
STABLE_EXPECTED
PROPOSED_EXPECTED
OTHER_CANONICAL_RELEASE
NONCANONICAL_TARGET
BROKEN_OR_UNREADABLE
```

规则：

- exact stable path → `STABLE_EXPECTED`；
- exact proposed path → `PROPOSED_EXPECTED`；
- `/srv/tmai/releases/[0-9a-f]{40}` 且目标是 non-symlink directory →
  `OTHER_CANONICAL_RELEASE`；
- readlink 成功但不满足 canonical release pattern → `NONCANONICAL_TARGET`；
- symlink/readlink/target directory shape 失败 → `BROKEN_OR_UNREADABLE`。

## 6. Output privacy contract

允许持久化：

- stable/proposed exact known path；
- 对 `OTHER_CANONICAL_RELEASE`，允许持久化 40-hex release identifier 和完整 canonical
  path，因为它是 deployment lineage identifier，不是 credential；
- 对 `NONCANONICAL_TARGET`，禁止持久化 raw target，只允许：
  - classification；
  - `sha256(raw_target)`；
  - raw target byte length；
- 对 `BROKEN_OR_UNREADABLE`，只允许 stable error stage。

禁止读取或持久化：

```text
PRIVATE_KEY=false
CREDENTIAL_VALUE=false
SERVER_ENVIRONMENT=false
RAW_LOGS=false
JOURNAL=false
SOURCE_IP=false
FILE_CONTENT=false
DIRECTORY_LISTING=false
NGINX_CONFIG=false
```

## 7. Exact caps

```text
DECISION_REVIEW_MODEL_REQUESTS_MAX=1
SSH_SESSIONS_MAX=1
LSTAT_CALLS_MAX=1
READLINK_CALLS_MAX=1
TARGET_DIRECTORY_SHAPE_CHECKS_MAX=1
SERVER_FILE_CONTENT_READS=0
RAW_LOG_READS=0
JOURNAL_READS=0
PUBLIC_REQUESTS=0
NGINX_TESTS=0
NGINX_RELOADS=0
SYMLINK_SWITCHES=0
SERVER_WRITES=0
RETRIES=0
FALLBACKS=0
DEPLOYMENTS=0
```

## 8. Options

### Option A — One target-classification diagnostic（推荐）

最小化未知状态并保持零写入。

### Option B — Retry the full CE-G12-P preflight（拒绝）

会重复消费已失败合同，且在 target 未分类前扩大服务器读取。

### Option C — Repair or rollback immediately（拒绝）

实际 target、变更来源和 server ownership context 都未知；直接写入可能覆盖合法状态。

### Option D — Assume proposed release is current（拒绝）

failure stage 只能证明 mismatch，不能证明 actual value。

## 9. Stop conditions

- host binding 与 Decision 不同；
- Decision/Review 尚未远端固定；
- current path 不是 symlink；
- 需要第二次 readlink；
- target shape check 之外需要 file content 或 directory listing；
- noncanonical raw target 会被持久化；
- 需要任何 log、journal、environment、network、write、reload、switch、retry 或 deployment；
- classification 会被升级为 unauthorized change、deployment success、root cause、Production
  或 commercial truth。

## 10. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
diagnostic_need_supported
one_read_scope_minimal
classification_contract_sound
canonical_identifier_persistence_sound
noncanonical_privacy_boundary_sound
caps_and_stop_rules_sufficient
no_repair_or_redeployment_authority
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

合格阈值：

```text
verdict=RECOMMENDED
confidence>=0.90
selected_option=A
would_recommend_to_agent_customer=true
all_boolean_checks=true
blockers=[]
corrections=[]
```

## 11. Non-authorizations and next gate

```text
RECOMMENDATION_NE_DECISION=true
SECOND_SSH_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
SYMLINK_CHANGE_AUTHORIZED=false
ROLLBACK_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
SLA=false
CERTIFICATION=false
COMMERCIAL_OFFERING=false
AUTHORITY_ELEVATION=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

若 review 合格，下一步只允许：

```text
NEXT_ACTION=PREPARE_CE_G12_CURRENT_TARGET_CLASSIFICATION_DECISION
NEXT_ACTION_AUTHORIZED=false
```
