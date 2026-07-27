---
document_id: DBA-TITMAS-CE-G7-EXACT-REDEPLOYMENT-RECOMMENDATION-0.1
title: TITMAS CE-G7 Exact Redeployment Recommendation v0.1
title_zh: TITMAS CE-G7 精确重新部署建议 v0.1
version: 0.1.0
status: exact-bounded-conditional-recommendation
maturity: Development
maturity_scope: public-static-development-site-release
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G7 Exact Redeployment Recommendation v0.1

## 1. Recommendation

建议把已经通过 CE-G6 只读重验证的 immutable release（不可变发布版本）：

```text
/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
```

原子切换为 `https://redcrag.cn/` 当前静态入口。该动作只发布 Development 级网站资料，
不创建 Runtime、API、Agent、Entity、Permission、Capability、Certification、SLA、
Commercial Offering（商业服务）或 Production（生产就绪）声明。

## 2. Direct prerequisites

| Evidence | Verified result |
|---|---|
| CE-G5 independent vantages | Ubuntu + macOS，`24/24`，无 retry/fallback/TLS bypass |
| CE-G6 immutable revalidation | archive/release/manifest/source/truth/schema 全部通过 |
| Proposed release | `f8107969aa1f43be8ecf43f557297a630309fe41` |
| Archive | `962612` bytes；SHA-256 `fceb10bba908fee4c36bed5fcccc88c3f6ff44d1326c3e1565be17cd12ac167e` |
| Release manifest | `60/60` |
| Current rollback target | `7da4bcf16eeec7de1c61031fe08fc04081cf8705` |
| Server preflight | both targets exist；current symlink exact；`nginx -t=PASS` |

早期 CE-G3 的一次 TLS transport failure（传输失败）根因仍为 `UNRESOLVED`。CE-G5
证明的是两个独立视角的有界稳定窗口，不是长期可用性、SLO 或 SLA。

## 3. Agent-customer recommendation

```text
provider=Alibaba Cloud Model Studio compatible endpoint
model=qwen3.7-plus
role=independent AI-agent infrastructure customer and release-safety reviewer
verdict=CONDITIONALLY_RECOMMENDED
would_recommend_to_agent_customer=true
confidence=0.85
blocking_corrections=0
```

模型识别两个 non-blocking risks（非阻塞风险）：

1. 未解决的历史 TLS 异常可能复现；任一复现必须触发回滚；
2. 原子切换到双视角完成之间存在短暂公开窗口。

模型输出只作为 advisory input（建议输入），不是 Decision、Authority、Truth 或部署证据。

## 4. Exact action sequence

1. 先提交并推送本 Recommendation、独立 Decision、固定 baseline、observer、Schema、
   tests 和 dormant workflow；此时不创建 run request，不触发 observation；
2. 再核对 current symlink、proposed/rollback release、archive SHA-256 和 `nginx -t`；
3. 用同目录 temporary symlink + atomic rename 把 `/srv/tmai/current` 切到 proposed release；
4. 再次执行 `nginx -t` 和 reload；
5. 在 server-local TLS path 对 11 个路由执行一次无 retry、无 TLS bypass 的 bytes/SHA-256
   校验，并检查 6 个安全响应头；
6. 在 controller public path 对同一 11 个路由执行一次同样的无重试校验；
7. 只有即时校验全部通过，才提交并推送 exact CE-G7 run-request marker；
8. GitHub-hosted Ubuntu 与 macOS 各执行 3 rounds × 4 critical routes，总计 24 GET；
9. 验证 workflow、两份 receipt、Schema、hash、独立环境、network egress 与 TLS stack；
10. 全部通过才保留 proposed release；任一失败按 exact rollback 恢复旧版本。

## 5. Exact routes

Immediate 11-route gate：

```text
/
/en/
/llms.txt
/agent-index.json
/status.json
/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
/TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json
/TITMAS-AGENT-EVALUATION-ENTRY-VALIDATION-REPORT-v0.1.md
/architecture/titmas-agent-evaluation-entry-contract-v0.1.md
/architecture/schemas/titmas-agent-evaluation-entry.schema.v0.1.json
/release-manifest.json
```

Independent-vantage 4-route gate：

```text
/
/llms.txt
/agent-index.json
/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json
```

## 6. Exact rollback

以下任一情况触发 fail-closed rollback：

- precondition mismatch；
- atomic switch、`nginx -t` 或 reload 失败；
- server-local 或 controller immediate check 任一路由非 200、bytes/hash mismatch；
- 任一安全响应头缺失；
- run-request commit/push 失败；
- workflow 未在有界窗口内启动或完成；
- 任一 job、receipt、Schema、hash、request count 或 independence check 失败；
- retry、fallback、proxy 或 TLS bypass 被观察到；
- current symlink 与预期不一致。

Rollback 必须把 `/srv/tmai/current` 原子恢复到：

```text
/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
```

随后执行 `nginx -t`、reload、current-target 和 root route 验证。失败 release、archive、
CE-G3 `11/12`、CE-G5/CE-G6 记录和 TLS root-cause `UNRESOLVED` 历史全部保留。

## 7. Caps and effects

```text
REBUILD=false
UPLOAD=false
DELETE=false
DBOS_CHANGE=false
SAEE_CHANGE=false
RETRY=false
FALLBACK=false
TLS_BYPASS=false

SERVER_LOCAL_GETS_MAX=13
CONTROLLER_PUBLIC_GETS_MAX=12
INDEPENDENT_VANTAGE_GETS_MAX=24
GITHUB_VANTAGES=2
ROUNDS_PER_VANTAGE=3
CRITICAL_ROUTES_PER_ROUND=4

STATIC_DEVELOPMENT_SITE_RELEASE=true
RUNTIME=false
API=false
AGENT=false
ENTITY=false
PERMISSION=false
CAPABILITY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
PRODUCTION_READY=false
```

上限包含 failure path 的 rollback root verification，但不允许 retry。

## 8. Standing-directive eligibility

本建议固定 exact action、source、target、rollback、preconditions、request caps、风险、
failure preservation、stop rules 和 false effects，满足 `TITMAS-CS-STANDING-001` 对
public deployment material action（公开部署重大动作）的适用条件。执行前仍必须形成并
推送独立 Decision Record；Recommendation 本身不是部署授权。
