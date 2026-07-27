---
document_id: DBA-TITMAS-AGENT-EVALUATION-ENTRY-PUBLICATION-RECOMMENDATION-0.1
title: TITMAS Agent Evaluation Entry Publication Recommendation v0.1
title_zh: TITMAS 智能体评估入口发布建议 v0.1
version: 0.1.0
status: recommended-exact-static-publication-and-bounded-observation
maturity: Development
maturity_scope: exact-static-site-update
owner_ref: zhangbin
decision_reference: TITMAS-CS-STANDING-001
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Exact static documentation and machine-entry update within the existing Developer Preview; no Runtime, API, product, SLA, certification, customer, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs:
  - TITMAS-AGENT-EVALUATION-ENTRY-VALIDATION-REPORT-v0.1.md
known_limitations: [SEE_DOCUMENT_BODY]
document_type: bounded-publication-recommendation
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS Agent Evaluation Entry Publication Recommendation v0.1

## 1. Recommendation（建议）

推荐一个 exact-scope action：

```text
PUBLISH_AGENT_EVALUATION_ENTRY_CONTRACT_V0_1_TO_EXISTING_STATIC_SITE
AND_RUN_BOUNDED_TIME_WINDOW_AVAILABILITY_OBSERVATION
```

理由：

- CE-G2 Schema 与 instance 已通过；
- 5/5 越权负例被拒绝；
- 网站 15/15 测试、正式静态导出、双语一致性和真值边界通过；
- production dependency audit 为 0 vulnerabilities；
- 当前生产站点、Nginx 和精确回滚目标已只读核验；
- 新内容只增加机器入口、规范和验证报告，不改变 DBOS/SAEE 语义。

## 2. Exact Publication Scope（精确发布范围）

只允许把当前 DBA clean commit 生成的 `site/out/` 上传到一个新的 immutable release
directory：

```text
HOST=hongyan-4cj
RELEASE_ROOT=/srv/tmai/releases
CURRENT_SYMLINK=/srv/tmai/current
PRE_DEPLOY_CURRENT=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
```

允许：

- `SOURCE_REVISION=<clean committed HEAD> npm run release:formal`；
- 建立 `/srv/tmai/releases/<SOURCE_REVISION>/`；
- 上传静态 archive；
- 验证 `release-manifest.json` 的 bytes 和 SHA-256；
- `nginx -t`；
- 原子切换 `/srv/tmai/current`；
- reload Nginx；
- 对 exact public routes 做无静默重试健康检查；
- 若失败，原子切回精确旧目标。

禁止：

- 修改 Nginx 配置；
- 修改系统、SSH、证书、防火墙或安全配置；
- 删除任何历史 release；
- 创建 Git tag、GitHub Release 或 PR；
- 修改 DBOS 或 SAEE；
- 创建 Runtime、API、Agent、Entity、Permission、Capability、Certificate、SLA 或
  Commercial Offering。

## 3. Required Public Routes（必检公开路径）

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

所有路径必须 HTTP `200`。机器契约还必须满足：

```text
evaluation_only=true
artifact.no_deps_allowed=false
discovery.contract_site_deployed=false  # source truth before deployment receipt
recommendation_policy.production_result=DO_NOT_RECOMMEND_FOR_PRODUCTION
effects.runtime=false
effects.permission=false
effects.commercial_offer=false
```

部署完成后，该 historical source field 保留 CE-G2 生成时事实；当前部署状态由 CE-G3
receipt、Program Status 和网站 Agent Index 的后续同步表达，不能重写历史实例。

## 4. Bounded Availability Observation（有界可用性观察）

授权一次短窗口可用性观察：

```text
ROUNDS=3
MINIMUM_ELAPSED_SECONDS=120
TARGETS=11
RETRY_WITHIN_ROUND=false
FAILURES_PRESERVED=true
CLASSIFICATION=OBSERVATION_NOT_SLA
```

每轮记录：

- UTC observed_at；
- target URL；
- HTTP code；
- latency；
- downloaded byte count；
- SHA-256（响应体适用时）；
- result。

该短窗口只验证发布后入口的一致性，不能推导 uptime、reliability、support commitment
或 SLA。

## 5. Rollback and Stop Conditions（回滚和停止条件）

出现任一情况必须停止或回滚：

- source worktree 不干净；
- remote branch 未包含 source revision；
- archive 或 manifest 校验失败；
- target release directory 已存在但不完全匹配；
- `nginx -t` 失败；
- 任一 required route 非 `200`；
- contract/schema/hash 与本地 source 不一致；
- security headers 丢失；
- machine truth 被抬升为 production、SLA、certification 或 commercial offering；
- current symlink 不是精确预期目标。

回滚：

```text
ln -sfn /srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705 /srv/tmai/current
nginx -t
systemctl reload nginx
```

失败记录必须保留；不得删除失败 release directory 以伪造成功历史。

## 6. Effects（效果）

```text
STATIC_PUBLICATION_RECOMMENDED=true
BOUNDED_AVAILABILITY_OBSERVATION_RECOMMENDED=true

NEW_PRODUCT_RELEASE=false
GITHUB_RELEASE=false
TAG=false
PR=false
RUNTIME=false
API=false
AGENT=false
ENTITY=false
PERMISSION=false
CAPABILITY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFER=false
PRODUCTION_READY=false
```
