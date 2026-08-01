---
matrix_id: DBA-MCP-2026-07-28-TRUST-IMPACT-0.1
title: MCP 2026-07-28 Trust Impact Matrix v0.1
title_zh: MCP 2026-07-28 可信影响矩阵 v0.1
status: release-candidate-reference-only-final-not-verified
primary_repository: DBA
baseline_version: 2025-11-25
candidate_version: 2026-07-28
release_candidate_locked_at: 2026-05-21
final_release_planned_at: 2026-07-28
final_release_verified: false
source_ref: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
reference_adopted: false
implementation_authorized: false
---

# MCP 2026-07-28 Trust Impact Matrix v0.1

## 1. Scope（范围）

本矩阵比较 MCP `2025-11-25` 与官方锁定的 `2026-07-28` release candidate（发布候选）对 ARO、任务生命周期、状态、追踪、授权和证据映射的潜在影响。

它不是 final specification（最终规范）对账、implementation plan（实现计划）、adapter、conformance result（符合性结果）或 adoption decision（采纳决定）。

```text
MCP_BASELINE_VERSION=2025-11-25
MCP_CANDIDATE_VERSION=2026-07-28
MCP_RELEASE_STATE=LOCKED_RELEASE_CANDIDATE
MCP_FINAL_RELEASE_VERIFIED=false
MCP_REFERENCE_ADOPTED=false
MCP_IMPLEMENTATION_AUTHORIZED=false
```

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

问题：如果潜在用户需要在 MCP breaking change 前识别证据与状态连续性风险，智能体是否推荐本矩阵？

```text
AGENT_RECOMMENDATION=RECOMMENDED_FOR_READ_ONLY_PREPARATION
RECOMMENDED_AS=RELEASE_CANDIDATE_TRUST_IMPACT_INVENTORY
NOT_RECOMMENDED_AS=FINAL_MIGRATION_OR_RUNTIME_COMPATIBILITY_PROOF
```

不推荐当前实施的原因：

- final specification 尚未发布和核验；
- exact SDK、server、client、extension 与 conformance 状态未知；
- Digital Biosphere 当前没有公共生产 MCP Runtime 需要紧急迁移；
- protocol telemetry、consent、authorization 与 Evidence 仍需保持分离。

## 3. Impact Matrix（影响矩阵）

| change_id | RC 变化 | 旧证据风险 | Digital Biosphere 只读影响 | final 后复核 |
|---|---|---|---|---|
| `MCP-I01` | 移除 `initialize`／`initialized` | 依赖一次握手保存 client/version/capability 的证据不再同构 | ARO 每次请求需保留 protocol version 与 client metadata reference | exact field、required/optional 与负例 |
| `MCP-I02` | 移除 `Mcp-Session-Id` 与协议级 session | session ID 不能继续作为长期任务或主体连续性代理 | 明确 `MCP session != DBOS Identity`；应用 state handle 单独记录 | stateless request replay／correlation |
| `MCP-I03` | application state 使用显式 handle | handle 暴露给模型，可错配、泄露、重放或跨主体传递 | handle 只作 untrusted state reference；绑定 tenant／purpose／lifecycle | handle scope、expiry、replay negatives |
| `MCP-I04` | `server/discover` 与 per-request capability | capability 可能按请求、节点或时间变化 | capability observation 必须带 server/version/time；不升级为 DBOS Capability | drift／conflict／cache cases |
| `MCP-I05` | `ttlMs` 与 `cacheScope` | 旧 `tools/list` 证据可能过期或跨用户污染 | 记录 cache age、scope、refresh reason 和 tool metadata digest | stale/shared-cache negatives |
| `MCP-I06` | `Mcp-Method`／`Mcp-Name` headers | header/body 不一致可能产生路由与审计分叉 | 保存拒绝结果和 header/body reconciliation；header 不作 authority | mismatch／gateway rewrite cases |
| `MCP-I07` | W3C Trace Context in `_meta` | trace correlation 容易被写成完整执行证明 | `traceparent` 只作 observation link；不是 Identity、Evidence 或 Truth | missing/forged/sampled trace cases |
| `MCP-I08` | Tasks 迁移为 extension | 旧实验 task lifecycle 与新 handle 不兼容 | 任务状态、cancel、update、result 按 extension version 分开 | task extension exact version and state machine |
| `MCP-I09` | server-to-client 仅限 active request；`InputRequiredResult` | elicitation／consent 的时间与父请求关系变化 | 必须绑定 initiating request、requestState、human response 与 retry | replay、wrong-parent、stale-response cases |
| `MCP-I10` | OAuth/OIDC authorization hardening | 旧 token／issuer 证据可能缺少 `iss` 或 issuer binding | MCP authorization 只证明 access decision，不证明 persona／delegation／execution correctness | issuer mix-up、migration、scope accumulation |
| `MCP-I11` | Roots／Sampling／Logging 标注弃用 | “弃用”等同“已移除”会造成错误迁移；Logging 替代容易把 OTel 当 Evidence | 保留 annotation-only 和至少一年生命周期；OTel 仍是 observation only | final deprecation text and dates |
| `MCP-I12` | 完整 JSON Schema 2020-12 | 外部 `$ref`、深度和验证成本引入资源／供应链风险 | 禁止自动解引用外部 `$ref`；限制 depth／time／size；schema valid 不等于 tool safe | parser limits、SSRF／DoS negatives |
| `MCP-I13` | error `-32002` → `-32602` | literal error matching 会产生 silent compatibility failure | error code 与 semantic class 分开记录 | exact changelog and client behavior |
| `MCP-I14` | Extensions 独立版本与维护 | core version 不再唯一决定整体行为 | extension ID/version/maintainer/source 单独绑定 | extension compatibility and provenance |

## 4. ARO / Evidence Mapping（ARO／证据映射）

| MCP material | 可作为 | 不可自动成为 |
|---|---|---|
| protocol version／client info | request context observation | DBOS Identity |
| tool discovery／metadata | capability candidate input | Capability 或 Permission |
| tool call／result | execution material | 正确执行或 Truth |
| trace context | correlation reference | complete Evidence |
| OAuth/OIDC result | access authorization material | persona continuity 或 delegation validity |
| task handle／state | application lifecycle reference | Entity identity 或 final state truth |
| elicitation response | consent evidence input | DBA／DBOS release authorization |
| monitor／gateway log | evidence producer output | independent verification |

## 5. Release-day Verification Gate（发布日核验闸门）

2026-07-28 或之后只在以下一手证据出现时刷新：

1. official final specification URL；
2. exact version/date 与 changelog；
3. final 与 locked RC delta；
4. official SDK support matrix；
5. conformance scenarios for affected Standards Track SEPs；
6. final Tasks / Apps extension versions；
7. authorization、deprecation 与 JSON Schema final wording。

结果状态：

```text
FINAL_MATCHES_RC=UNKNOWN
FINAL_DELTA_REVIEW_COMPLETE=false
ARO_MAPPING_REVIEW_COMPLETE=false
EVIDENCE_MAPPING_REVIEW_COMPLETE=false
IMPLEMENTATION_CHANGE_REQUIRED=UNKNOWN
IMPLEMENTATION_AUTHORIZED=false
```

## 6. Non-claims（非声明）

```text
MCP_FINAL_SPECIFICATION_PUBLISHED=false
MCP_REFERENCE_ADOPTED=false
MCP_RUNTIME_CONNECTED=false
MCP_COMPATIBILITY_TESTED=false
MCP_CONFORMANCE_PASS=false
DBOS_CAPABILITY_CHANGED=false
SAEE_CAPABILITY_CHANGED=false
EXTERNAL_SUBMISSION_SENT=false
```
