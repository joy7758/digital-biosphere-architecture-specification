---
document_id: DBA-TITMAS-CE-G12-SSH-TARGET-MAPPING-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 SSH Target Mapping Remediation Recommendation v0.1
title_zh: TITMAS CE-G12 SSH 目标映射修复建议 v0.1
version: 0.1.0
status: ssh-target-mapping-remediation-recommended-agent-review-required
maturity: Development
maturity_scope: read-only-deployment-admission-preflight-transport-remediation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 SSH Target Mapping Remediation Recommendation v0.1

## 1. Recommendation

采用 **Option A：保留旧 session 的失败事实，建立新的 transport-specific Decision，
把 SSH identity 固定为本机配置 alias `hongyan-4cj`，再最多执行一个 fresh、只读、
零重试 preflight session**。

```text
RECOMMENDED_OPTION=A
FAILED_SESSION_PRESERVED=true
FAILED_SESSION_RETRY=false
FRESH_DECISION_REQUIRED=true
FRESH_SESSION_RECOMMENDED=true
FRESH_SESSION_AUTHORIZED=false
SSH_TARGET_ALIAS=hongyan-4cj
EXPECTED_HOSTNAME=180.76.115.193
EXPECTED_REMOTE_USER=root
IDENTITY_FILE_PATH_RECORDED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

本建议不建立 SSH session，不调用网络，不读取或修改 server，不创建 release directory，
不传输 archive，不切换 symlink，不 reload nginx，不部署、不发布。

## 2. Preserved failure evidence

远端固定的失败 evidence：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-deployment-admission-preflight-result.v0.1.json` | `64a0b0017e8bba2b7499f0eacbf0d53b2a2d1cf3cd0e66d7f13d73159224e05e` |
| `TITMAS-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-ADMISSION-PREFLIGHT-REPORT-v0.1.md` | `9bb75893ae9037e75867bea34815224c6b121633bee6a5d201617aa1c5d4e91b` |

evidence commit：

```text
68a44cb5e2712164bc177f098ac0454407250c15
```

唯一旧 session：

```text
ATTEMPTED_TARGET=zhangbin@180.76.115.193
SSH_SESSIONS=1
SSH_EXIT=255
FAILURE=PERMISSION_DENIED_PUBLICKEY
SERVER_SCRIPT_STARTED=false
SERVER_READS_COMPLETED=0
SERVER_WRITES=0
RETRIES=0
```

该结果只证明尝试的 transport identity 未通过 public-key authentication。它不证明 server
不可用、目标路径不存在、current/rollback 状态异常或 deployment 不可行。

## 3. Local-only target mapping diagnosis

失败后没有再次调用网络或 SSH，只读取了本机 SSH config。已观察到：

```text
HOST_ALIAS=hongyan-4cj
HOSTNAME=180.76.115.193
USER=root
IDENTITIES_ONLY=yes
STRICT_HOST_KEY_CHECKING=accept-new
IDENTITY_FILE_CONFIGURED=true
IDENTITY_FILE_PATH_PERSISTED=false
```

因此根因分类为：

```text
ROOT_CAUSE=DECISION_TARGET_BYPASSED_CONFIGURED_ALIAS_USER_AND_IDENTITY_MAPPING
```

本地 config 是 transport configuration evidence，不是 server observation、credential
disclosure、deployment authority 或成功保证。

## 4. Exact remediation boundary

新的 Decision 必须：

1. 明确旧 session 已完成且不可 retry；
2. 仅把未来 transport identity 固定为 exact alias `hongyan-4cj`；
3. 在任何 network call 前使用本地 `ssh -G hongyan-4cj` 检查：
   - hostname 是 `180.76.115.193`；
   - user 是 `root`；
   - identitiesonly 是 `yes`；
   - 至少解析出一个 identityfile；
4. 不记录、提交或输出 identity file 的绝对路径、private-key 内容或 credential；
5. 仅在 mapping assertions 全部通过时，允许一个新的 non-interactive SSH session；
6. 该 session 复用上一 Decision 的 exact read-only server script 和最多 12 个 read；
7. session 内 server write、public request、transfer、extract、repair、rollback、deployment、
   release 均保持为零；
8. auth、host-key、mapping 或任一 observation 失败即关闭，不 retry、不 fallback；
9. 生成新的 v0.2 Preflight Result 和 Report，不覆盖 v0.1 failure；
10. 只提交新的结果材料。

建议的 network transport 必须通过 alias：

```text
ssh hongyan-4cj
```

不得重新使用：

```text
ssh zhangbin@180.76.115.193
ssh root@180.76.115.193
```

后者都会绕开“Decision 固定 alias/config mapping”这一审计边界，即使技术上可能连接成功。

## 5. Candidate remains immutable

后续 fresh preflight 仍绑定同一 candidate：

```text
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound-portable.tar.gz
ARCHIVE_BYTES=979463
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
RELEASE_ID=c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
CANDIDATE_CHANGED=false
```

任何 bytes/hash drift 都必须在连接前停止。

## 6. Options

### Option A — New alias-bound read-only Decision and fresh session（推荐）

保留失败，修正被审计的 transport identity；在独立 Decision 和 qualifying review 后才允许
一个 fresh session。

### Option B — Retry the failed session（拒绝）

旧 Decision 的一个 session 和零 retry cap 已用尽；retry 会改写既有执行事实。

### Option C — Use `root@IP` without a new Decision（拒绝）

即使 user 可能正确，也绕过已观察到的 alias、identityfile 和 identitiesonly 映射，且没有
新的授权。

### Option D — Treat local SSH config as a successful preflight（拒绝）

本地配置不能证明 current target、rollback、filesystem 或 server 状态。

### Option E — Deploy because the candidate is exact（拒绝）

candidate exactness 不等于 deployment admission；服务器只读前置条件仍未观察。

## 7. Caps and stop conditions

未来新的 preflight caps：

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
LOCAL_SSH_CONFIG_RESOLUTIONS_MAX=1
SSH_SESSIONS_MAX=1
SERVER_READ_COMMANDS_MAX=12
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
FILE_CREATIONS=0
ARCHIVE_TRANSFERS=0
ARCHIVE_EXTRACTIONS=0
CHMOD_CHOWN_OPERATIONS=0
SYMLINK_SWITCHES=0
NGINX_TESTS=0
NGINX_RELOADS=0
REPAIRS=0
ROLLBACKS=0
DEPLOYMENTS=0
RELEASES=0
RETRIES=0
NETWORK_FALLBACKS=0
```

停止于：

- Recommendation/Review/Decision/Decision review 未远端固定；
- returned model 不是 exact `qwen3.7-max`；
- local config 解析结果与 expected hostname/user/identitiesonly 不符；
- identityfile 缺失，或需要公开其路径或内容；
- candidate/evidence hash drift；
- SSH/auth/host-key failure；
- read-only script 需要 write、retry、fallback 或第二个 session；
- 任何把 preflight 升级为 deployment、release、Standard Ready、Production 或 commercial
  offering 的要求。

## 8. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
failure_preservation_sound
root_cause_classification_sound
alias_bound_transport_sound
local_mapping_check_scope_sufficient
credential_non_disclosure_sound
fresh_session_not_retry_sound
candidate_immutability_preserved
read_only_preflight_scope_preserved
caps_and_stop_rules_sufficient
no_deployment_or_release_inference
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers 和
corrections、returned model exact `qwen3.7-max`。

## 9. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
LOCAL_CONFIG_NE_SERVER_OBSERVATION=true
FAILED_SESSION_NE_RETRY_AUTHORITY=true
FRESH_SESSION_NE_FAILED_SESSION_RETRY=true
SSH_MAPPING_NE_CREDENTIAL_DISCLOSURE=true
READ_ONLY_PREFLIGHT_NE_DEPLOYMENT=true
CANDIDATE_PASS_NE_DEPLOYMENT_ADMISSION=true
SSH_SESSION_CREATED=false
SERVER_READ_EXECUTED=false
SERVER_WRITE_EXECUTED=false
PUBLIC_SITE_CHANGED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
