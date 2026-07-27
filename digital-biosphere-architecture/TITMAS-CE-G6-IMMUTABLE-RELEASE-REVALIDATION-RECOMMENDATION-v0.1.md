---
document_id: DBA-TITMAS-CE-G6-IMMUTABLE-RELEASE-REVALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G6 Immutable Release Revalidation Recommendation v0.1
title_zh: TITMAS CE-G6 不可变发布版本重验证建议 v0.1
version: 0.1.0
status: exact-bounded-conditional-recommendation-correction-incorporated
maturity: Development
maturity_scope: proposed-static-release-read-only-revalidation
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G6 Immutable Release Revalidation Recommendation v0.1

## 1. Recommendation

建议只读重验证 CE-G3 保留的 proposed immutable release（拟发布不可变版本）：

```text
source revision:
f8107969aa1f43be8ecf43f557297a630309fe41

release directory:
/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41

archive:
/tmp/titmas-site-f8107969aa1f43be8ecf43f557297a630309fe41.tar.gz
```

CE-G6 不部署、不切换 symlink、不 reload Nginx、不发送 public HTTP GET。

## 2. Evidence baseline

- CE-G3 保留 release、archive 和失败事实；
- CE-G3 记录 archive `962612` bytes、SHA-256
  `fceb10bba908fee4c36bed5fcccc88c3f6ff44d1326c3e1565be17cd12ac167e`；
- CE-G3 记录 manifest `60/60`；
- CE-G5 在 current-live rollback release 上完成两个独立视角 `24/24`；
- Git 直接比较证明 `f810796...` 到 current `df195a3...` 的 `site/` 源码为零差异；
- 当前线上 symlink 仍指向 `7da4bcf...`。

这些事实允许准备只读 artifact revalidation，不自动允许 deployment。

## 3. Agent-customer recommendation

```text
provider=Alibaba Cloud Model Studio compatible endpoint
model=qwen3.7-plus
role=independent AI-agent infrastructure customer reviewer
verdict=CONDITIONALLY_RECOMMENDED
would_recommend_to_agent_customer=true
confidence=0.82
```

唯一 blocking correction：

> 必须明确 CE-G6 通过不构成部署授权，不证明 TLS 根因已解决，也不保证后续部署成功。

本建议已纳入该修正。模型输出使用了 Markdown code fence，未完全遵守“只输出 JSON”
要求；因此只作为 advisory input，不作为 Schema conformance、Decision 或 Truth。

## 4. Exact read-only scope

必须验证：

1. current symlink 精确为 `7da4bcf...`；
2. proposed release 目录存在，验证期间不写入；
3. archive 大小和 SHA-256 精确匹配；
4. archive member 无绝对路径、`..`、symlink、hardlink 或特殊文件；
5. `release-manifest.json` 可解析，`source_revision=f810796...`；
6. manifest 精确包含 60 个唯一文件；
7. release 目录除 manifest 本身外，无 manifest 未声明或遗漏文件；
8. 60 个文件的 bytes 与 SHA-256 全部匹配；
9. archive 与 release 目录的 61 个 regular files（含 manifest）逐一匹配；
10. Agent Evaluation Entry 保持 Development、evaluation-only 与 false effects；
11. public status 继续声明 available offering、production、customer adoption 和 SLA 为 false；
12. 本地 exact source 的 Schema 正例和 5 个 negative boundary cases 继续失败关闭。

## 5. Exact caps and prohibitions

```text
SERVER_SSH_SESSIONS_MAX=1
PUBLIC_HTTP_REQUESTS_MAX=0
MODEL_REQUESTS_MAX=0
ARCHIVE_EXTRACTION=false
RETRY=false
FALLBACK=false
TLS_BYPASS=false
SERVER_FILE_WRITE=false
SYMLINK_SWITCH=false
NGINX_RELOAD=false
DEPLOYMENT=false
```

允许保存 sanitized hashes、counts、booleans 和 error class；不保存凭据、原始日志、文件
body 或 source IP。

## 6. Pass and stop rules

任一 exact value、path safety、file set、hash、truth boundary、source diff 或 negative case
失败：

```text
CE_G6_RESULT=FAIL_CLOSED
REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT_AUTHORIZED=false
```

全部通过只允许：

```text
CE_G6_IMMUTABLE_RELEASE_REVALIDATION_PASS=true
NEXT_ACTION=PREPARE_CE_G7_EXACT_REDEPLOYMENT_RECOMMENDATION
```

仍不产生 deployment authorization。

## 7. Required non-claims

```text
CE_G6_NE_DEPLOYMENT_AUTHORIZATION=true
CE_G6_NE_TLS_ROOT_CAUSE_PROOF=true
CE_G6_NE_DEPLOYMENT_SUCCESS_GUARANTEE=true
CE_G6_NE_RUNTIME_FUNCTIONAL_VALIDATION=true
CE_G6_NE_PRODUCTION_READINESS=true
CE_G6_NE_SLA=true
CE_G6_NE_COMMERCIAL_OFFERING=true
CE_G6_NE_CERTIFICATION=true
```

## 8. Standing-directive eligibility

本建议固定一个 read-only exact option、目标、预期值、外部动作上限、隐私边界、失败关闭
规则和 false effects，满足 `TITMAS-CS-STANDING-001` 的候选条件。执行仍需独立 Decision。
