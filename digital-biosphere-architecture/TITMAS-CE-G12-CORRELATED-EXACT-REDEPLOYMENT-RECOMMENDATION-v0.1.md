---
document_id: DBA-TITMAS-CE-G12-CORRELATED-EXACT-REDEPLOYMENT-RECOMMENDATION-0.1
title: TITMAS CE-G12 Correlated Exact Redeployment Recommendation v0.1
title_zh: TITMAS CE-G12 关联式精确重新部署建议 v0.1
version: 0.1.0
status: exact-preflight-first-recommendation-agent-review-required-decision-pending
maturity: Development
maturity_scope: correlated-exact-static-redeployment-recommendation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Correlated Exact Redeployment Recommendation v0.1

## 1. Recommendation outcome

采用 **Option A：准备 preflight-first（先预检）、fail-closed（失败关闭）的关联式精确
重新部署治理包，但不授权当前执行**。

```text
CE_G12_RECOMMENDATION_PREPARED=true
AGENT_CUSTOMER_VERDICT=CONDITIONALLY_RECOMMENDED
RECOMMENDED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
FRESH_SERVER_PREFLIGHT_COMPLETE=false
CURRENT_EVIDENCE_SUFFICIENT_FOR_RECOMMENDATION=true
CURRENT_EVIDENCE_SUFFICIENT_FOR_EXECUTION=false
CE_G12_DECISION_RECORDED=false
REDEPLOYMENT_AUTHORIZED=false
REDEPLOYMENT_EXECUTED=false
```

这一步不是再次证明静态站点“可以构建”，而是把已有 immutable release（不可变发布物）、
current target（当前目标）、CE-G11 correlation（相关性证据）、atomic switch（原子切换）、
two-vantage observation（双观察点）和 rollback（回滚）绑定成一个未来可审查的精确执行
合同。

## 2. Pre-development agent-customer gate

exact `qwen3.7-max` 已以 independent AI-agent infrastructure customer and release-safety
reviewer（独立智能体基础设施客户与发布安全审查者）身份返回：

```text
VERDICT=CONDITIONALLY_RECOMMENDED
SELECTED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
PREPARE_RECOMMENDATION_NOW=true
REDEPLOYMENT_EXECUTION_NOW=false
CURRENT_EVIDENCE_SUFFICIENT_FOR_RECOMMENDATION=true
CURRENT_EVIDENCE_SUFFICIENT_FOR_EXECUTION=false
OFFLINE_BINDING_CAN_REMAIN_NON_AUTHORITY=true
```

直接记录：

[`TITMAS-CE-G12-PREDEVELOPMENT-AGENT-CUSTOMER-RECOMMENDATION-GATE-v0.1.json`](TITMAS-CE-G12-PREDEVELOPMENT-AGENT-CUSTOMER-RECOMMENDATION-GATE-v0.1.json)

该模型把 PR #27 post-merge validation 描述为 proposed release 的 validation；本建议不传播
这一表述。canonical release bytes 仍只以 CE-G7 proposed release baseline 为准，PR #27
只证明治理仓库和 repository integration（仓库集成）状态，不证明 live deployment。

## 3. Exact immutable topology

### 3.1 Current and rollback target

```text
PUBLIC_ORIGIN=https://redcrag.cn
LAST_VERIFIED_CURRENT_RELEASE=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
ROLLBACK_RELEASE=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
CURRENT_RELEASE_BASELINE_SHA256=c08c9c4991fea0f385fdd0720e0fbef99ee5676e0ced108012f37ef3b12d6b8c
FRESH_CURRENT_RELEASE_VERIFICATION_REQUIRED=true
```

`LAST_VERIFIED_CURRENT_RELEASE` 是 2026-07-27 的 historical evidence，不是 2026-07-28
live truth。任何 server mutation 之前必须由独立 read-only preflight Decision 重新验证。

### 3.2 Proposed immutable release

```text
PROPOSED_RELEASE=/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
SOURCE_REVISION=f8107969aa1f43be8ecf43f557297a630309fe41
ARCHIVE_BYTES=962612
ARCHIVE_SHA256=fceb10bba908fee4c36bed5fcccc88c3f6ff44d1326c3e1565be17cd12ac167e
MANIFEST_FILES=60
ROUTE_HASH_BASELINE_COUNT=11
PROPOSED_RELEASE_BASELINE_SHA256=173fa2a0972bbbf3f61d4a649a1331249334c0fa003a668da200318a7858f7fc
```

不得用 PR #27 merge commit、working-tree label 或新 static export 暗中替换该 release。
需要新 release 时必须退出 CE-G12，另建 recommendation。

### 3.3 Correlation evidence producer

```text
BINDING_SCHEMA_SHA256=2263c3c224097f6d7ed233bd5ff261a6dd225e11f10e290d0d1dc4aa382be684
BINDING_FIXTURE_SHA256=cee58ceb4088ba99f4c0c5631a309898bf9c7df8a6d6ad64fc85ac920ad80f06
CORRELATOR_SHA256=b72ad6e707a95f65e20f235963306e04c4f3e81342f4c762514cffcbf7e2d0e3
BINDING_EXPECTED_CURRENT_RELEASE=/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
BINDING_AUTHORIZATION_STATUS=NOT_AUTHORIZED
BINDING_AUTHORITY_EFFECT=false
BINDING_IS_PERMISSION=false
```

binding 必须继续非授权。未来 Human Decision 授权的是 exact preflight 或 execution，
不是把 binding metadata 变成 Permission。

## 4. Evidence lineage and limits

| Evidence | What it proves | What it does not prove |
|---|---|---|
| CE-G5 current baseline | 2026-07-27 stable target 与 bounded public observation | 当前实时 target |
| CE-G7 result `08fbeae…` | proposed release server gate `11/11`、headers `6/6`、rollback PASS；controller `/en/` exit 35 | TLS root cause、redeployment admission |
| CE-G8 | 四次 diagnosis observation 完成 | failure reproduction 或 exact root cause |
| CE-G11A | hash-bound correlation adapter、local `26/26`、negative `9/9` | live server authorization 或 deployment |
| CE-G11B / PR #27 | integration merged at `c1d8931…`；post-merge JSON/site/CE validation PASS | live release bytes、server state、Production |
| CE-G12 agent gate | Recommendation preparation is useful | Decision、Authority 或 execution safety |

```text
TLS_ROOT_CAUSE_PROVEN=false
CURRENT_SERVER_STATE_FRESH=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
EVIDENCE_NE_TRUTH=true
EVALUATION_NE_AUTHORITY=true
```

## 5. Two-decision gate structure

### Gate CE-G12-P — Read-only preflight Decision

必须先形成独立 Decision，只授权一次 SSH session 和 read-only server preflight：

1. 读取 `/srv/tmai/current`，必须精确等于 stable target；
2. 验证 stable 与 proposed release directories 均存在；
3. proposed release 的 11 个 route files、manifest count 和 hashes 必须匹配 baseline；
4. archive bytes/hash 必须匹配；
5. binding Schema、fixture、correlator bytes/hash 必须匹配；
6. `nginx -t` 必须通过，但不得 reload；
7. 确认 access/error log 与 journal 的最小读取路径可用，不读取或持久化 raw content；
8. 生成 sanitized preflight receipt；
9. preflight freshness 在未来 execution Decision 记录时不得超过 1,800 秒。

任何 mismatch：

```text
CE_G12_PREFLIGHT=FAIL_CLOSED
SERVER_WRITES=0
REDEPLOYMENT_DECISION_ALLOWED=false
```

### Gate CE-G12-X — Separate redeployment Decision

只有 CE-G12-P PASS、Recommendation review 合格且 exact preflight receipt/hash 已远端固定，
才可建立新的 execution Decision。它必须再次固定：

- operator reference 与 credential reference，但不持久化 secret；
- exact current/proposed/rollback targets；
- exact archive、manifest、route 和 correlation hashes；
- UTC execution window；
- commands、caps、stop rules、rollback 和 post-action receipt；
- public request audience、retention 和 sanitized evidence boundary。

CE-G12-P PASS 不自动产生 CE-G12-X。

## 6. Proposed execution state machine

未来 CE-G12-X 若被独立授权，必须按顺序执行：

```text
PREFLIGHT_RECEIPT_VERIFIED
        ↓
ATOMIC_SWITCH
        ↓
NGINX_CONFIG_TEST
        ↓
NGINX_RELOAD
        ↓
SERVER_LOCAL_GATE
        ↓
CONTROLLER_IMMEDIATE_GATE
        ↓
CORRELATION_GATE
        ↓
TWO_VANTAGE_GATE
        ↓
POST_ACTION_VERIFICATION
        ↓
SUCCESS_OR_EXACT_ROLLBACK
```

### Stage 1 — Atomic switch

- 切换前再次读取 current target；
- 只允许从 stable target 切至 proposed target；
- atomic symlink switch 最多一次；
- `nginx -t` 与 reload 各最多一次；
- 不允许 inplace overwrite。

### Stage 2 — Server-local gate

- 对 baseline 的 11 个 routes 各执行一次；
- route content hash `11/11`；
- required security headers `6/6`；
- target、manifest 和 archive identity 必须保持不变。

### Stage 3 — Controller immediate gate

- 对相同 11 个 routes 各执行一次；
- TLS verification 不得 bypass；
- proxy environment 必须记录为 sanitized boolean；
- 任一路径非 PASS 时不重试，并进入 Stage 4 后立即 rollback。

### Stage 4 — Correlation gate

- 在 proposed target 仍 active 时执行一次；
- window 最大 60 秒，覆盖 controller request；
- binding fixture/hash 必须精确；
- source hash salt 只在内存使用，raw salt、raw IP 和 raw logs 不持久化；
- receipt 只证明 observation 与 server evidence correlation；
- correlation PASS 不得把 controller FAIL、TLS root cause 或 content correctness 改写为 PASS。

如果 controller gate PASS，correlation 仍必须证明 expected request records；如果 controller
gate FAIL，correlation 只用于区分“server observed / not observed / unknown”，随后必须回滚。

### Stage 5 — Two-vantage gate

仅在 Stages 1–4 全部 PASS 后触发：

```text
VANTAGES=GITHUB_HOSTED_UBUNTU,GITHUB_HOSTED_MACOS
ROUTES=/,/llms.txt,/agent-index.json,/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
ROUNDS=3
ROUND_GAP_SECONDS=10
REQUESTS_PER_VANTAGE=12
TOTAL_PUBLIC_REQUEST_CAP=24
RETRY=false
FALLBACK=false
TLS_BYPASS=false
```

两个 vantage 都必须 content/hash/transport PASS。它们仍只证明 bounded observation，不
证明全球可用性、SLO 或 SLA。

### Stage 6 — Post-action verification

所有 gate PASS 才可保留 proposed target，并生成 deployment receipt。否则必须：

1. atomic switch 回 stable target；
2. `nginx -t` 和 reload；
3. stable root/hash verification；
4. 保存 failed release、archive、failure receipt 和 correlation receipt；
5. 不删除失败材料，不重试。

## 7. Exact caps

```text
PREFLIGHT_SSH_SESSIONS_MAX=1
EXECUTION_SSH_SESSIONS_MAX=1
ATOMIC_FORWARD_SWITCHES_MAX=1
ATOMIC_ROLLBACK_SWITCHES_MAX=1
SERVER_LOCAL_PUBLIC_REQUESTS_MAX=11
CONTROLLER_PUBLIC_REQUESTS_MAX=11
CORRELATION_EXECUTIONS_MAX=1
INDEPENDENT_VANTAGE_JOBS_MAX=2
INDEPENDENT_VANTAGE_PUBLIC_REQUESTS_MAX=24
TOTAL_PUBLIC_REQUESTS_MAX=46
NGINX_CONFIG_TESTS_MAX=3
NGINX_RELOADS_MAX=2
RETRIES=0
FALLBACKS=0
TLS_BYPASS=0
SOURCE_CHANGES=0
DBOS_CHANGES=0
SAEE_CHANGES=0
AGENTS_CREATED=0
RUNTIMES_CREATED=0
PERMISSIONS_CREATED=0
```

`TOTAL_PUBLIC_REQUESTS_MAX` 只在未来 CE-G12-X Decision 中生效，不是本 Recommendation
授权。

## 8. Stop and rollback conditions

以下任一情况停止；若 forward switch 已发生则 exact rollback：

- preflight receipt 缺失、过期或 hash 不匹配；
- current target 不是 stable target；
- proposed/rollback directory 或 baseline bytes 不匹配；
- binding/correlator hash 或 non-authority fields 不匹配；
- `nginx -t`、reload、server route/hash/header 任一失败；
- controller 任一路径失败或产生 unknown；
- correlation current-target、binding、window、log 或 journal stage 失败；
- correlation 无法解释为 bounded evidence；
- 任一 vantage、hash、TLS 或 artifact validation 失败；
- request/SSH/switch/reload/model cap 超限；
- retry、fallback、TLS bypass、raw secret/log/IP persistence 被要求；
- Authority、Permission、Standard Ready、Production、SLA、Certification 或 commercial
  offering 被暗中抬升。

## 9. Options

### Option A — Preflight-first exact correlated redeployment governance（推荐）

先形成 CE-G12-P；PASS 后再形成 CE-G12-X。Recommendation、preflight 和 execution
三者分别留痕。

### Option B — Deploy now（拒绝）

没有 fresh preflight，且 redeployment admission 仍为 false。

### Option C — Build a new release first（当前拒绝）

会改变被诊断 release bytes，破坏 CE-G7 failure 与 CE-G12 correlation 的可比性。若确需
新 release，必须退出本 gate 并另建基线。

### Option D — Abandon correlated path（拒绝）

CE-G11A/11B 已消除原 hard-coded correlation blocker；直接放弃会浪费可验证路径。

## 10. Recommendation review contract

只允许一次 exact `qwen3.7-max` review。direct JSON 必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
preflight_before_execution_decision_sound
immutable_topology_binding_sound
binding_non_authority_preserved
correlation_before_rollback_sound
two_vantage_gate_sound
rollback_and_no_retry_sound
caps_and_stop_rules_sufficient
evidence_claims_bounded
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

不合格时保留原结果，不抽取、不修复、不重试、不换模型。

## 11. Non-authorizations and next gate

```text
RECOMMENDATION_NE_DECISION=true
PREFLIGHT_AUTHORIZED=false
SSH_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
NETWORK_EXECUTION_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
PUBLICATION_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
SLA=false
CERTIFICATION=false
COMMERCIAL_OFFERING=false
AUTHORITY_ELEVATION=false
OWNERSHIP_CHANGE=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

若 Recommendation review 合格，下一步只允许：

```text
NEXT_ACTION=PREPARE_CE_G12_READ_ONLY_PREFLIGHT_DECISION
NEXT_ACTION_AUTHORIZED=false
```

Recommendation review PASS 不是 CE-G12-P Decision，更不是 CE-G12-X execution
authorization。
