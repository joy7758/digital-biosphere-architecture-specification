---
report_id: DBA-WEB-DEPLOY-003
title: Trusted Multi-Agent Infrastructure Public Website Deployment Report
title_zh: 可信多智能体基础设施公开网站部署报告
status: pass-technical-validation-homepage-synchronized-not-pilot-executed
observed_at: 2026-07-23T21:35:24+08:00
public_url: https://redcrag.cn/
github_release_url: https://github.com/joy7758/digital-biosphere-architecture-specification/releases/tag/v0.1-developer-preview
github_release_tag: v0.1-developer-preview
host: 180.76.115.193
current_validated_source_revision: e087fa8f2ebc7c6fca0cbc094bf45f03e3d32d46
deployment_state: developer-preview-v0.1-released
developer_preview_released: true
technical_validation_design_complete: true
technical_validation_pilot_execution_authorized: false
complete_vertical_slice_executed: false
production_ready: false
agent_created: false
runtime_created: false
permission_created: false
---

# Trusted Multi-Agent Infrastructure Public Website Deployment Report

## Conclusion（结论）

`https://redcrag.cn/` 已从 immutable Baidu Cloud release directory（百度云不可变
发布目录）提供 TMAI Developer Preview v0.1 的中英文、agent-readable（智能体可读）
正式静态站点。2026-07-23 的首页同步增加了完整 Technical Validation Pilot 说明，
包括目标垂直切片、阶段 Owner、成功标准、阻塞项、公开材料和 Reviewer-first 边界；
理解这些信息不依赖访问 GitHub。

```text
PUBLIC_WEBSITE_DEPLOYED=true
PUBLIC_WEBSITE_HEALTH_PASS=true
PUBLIC_WEBSITE_SECURITY_HEADERS_PASS=true
PUBLIC_WEBSITE_ROLLBACK_TARGET_PRESERVED=true
DEVELOPER_PREVIEW_RELEASED=true
TITMAS_TECHNICAL_VALIDATION_DESIGN_COMPLETE=true
TITMAS_PILOT_EXECUTION_AUTHORIZED=false
COMPLETE_VERTICAL_SLICE_EXECUTED=false
PRODUCTION_READY=false
```

正式发布不等于生产 Runtime、客户采用、Permission、Agent 或 Digital Entity 实例。

## Published routes（公开入口）

以下 14 个入口在正式切换后返回 HTTP `200`：

| Route | Role |
|---|---|
| `/` | 中文首页 |
| `/en/` | English home |
| `/status/` | 中文状态页 |
| `/en/status/` | English status |
| `/llms.txt` | LLM-readable project entry |
| `/agent-index.json` | Agent discovery index |
| `/status.json` | Machine-readable program status |
| `/agent-customer-package.json` | Agent recommendation and boundary package |
| `/dbos-public-package-manifest.json` | Exact DBOS wheel manifest |
| `/release.json` | Active release source and state |
| `/release-manifest.json` | SHA-256 artifact inventory |
| `/robots.txt` | Crawler policy |
| `/sitemap.xml` | Public route index |
| `/og.png` | Social preview asset |

中英文页面包含各自的正式发布标识。`release.json`、`status.json`、Agent Index 和 DBOS
manifest 的 tag、decision reference、release state 与 package URL 一致。

## Artifact integrity（工件完整性）

```text
SOURCE_REVISION=e087fa8f2ebc7c6fca0cbc094bf45f03e3d32d46
ACTIVE_RELEASE_DIRECTORY=/srv/tmai/releases/e087fa8f2ebc7c6fca0cbc094bf45f03e3d32d46
SITE_ARCHIVE_BYTES=1723055
SITE_ARCHIVE_SHA256=bdc7e69bb54e70c094f4e7a8b804d2d021ffb45b5ee3b807cf7793d01a0f959a
MANIFEST_FILES=21
ON_HOST_MANIFEST_PASS=true
```

正式 archive（压缩包）使用 `--no-xattrs` 构建，不包含候选包曾出现的 macOS provenance
扩展属性头。服务器逐一验证 21 个清单文件的 byte size 和 SHA-256，随后才执行原子切换。

## Transport and security（传输与安全）

- HTTP 重定向至 `https://redcrag.cn/`；
- Nginx 配置检查通过且服务为 `active`；
- HSTS、CSP、`nosniff`、frame denial、referrer policy 和 permissions policy 保留；
- 系统、SSH、证书、防火墙和安全配置未修改；
- 公网多路检查观察到多次瞬时 `SSL_ERROR_SYSCALL`，有界重试后全部通过。

## Rollback（回滚）

正式站点通过 atomic symlink switch（原子符号链接切换）激活。前一候选版本仍保留：

```text
PREVIOUS_RELEASE=/srv/tmai/releases/1113130ca4213b70fcebd6247fec794854295e8c
ROLLBACK_MECHANISM=ATOMIC_SYMLINK_SWITCH
PRIOR_ACTUAL_ROLLBACK_VALIDATION=true
```

既有候选部署曾完成实际切回和恢复；本次复用相同机制并保留精确旧目标，没有为了报告
再次制造线上回滚。

## GitHub source and release binding（GitHub 来源与发布绑定）

- Homepage source merge：`e087fa8f2ebc7c6fca0cbc094bf45f03e3d32d46`
- Pull request：<https://github.com/joy7758/digital-biosphere-architecture-specification/pull/14>
- 网站内容同步不创建新产品版本；Developer Preview v0.1 的既有 release identity 保持不变。

- Release：<https://github.com/joy7758/digital-biosphere-architecture-specification/releases/tag/v0.1-developer-preview>
- `draft=false`
- `prerelease=false`
- Tag commit：`1113130ca4213b70fcebd6247fec794854295e8c`
- DBOS wheel SHA-256：`edf92e548860384b1416a612a7e319e0d994bb324f8621847d0d154624ae8f09`
- DBOS repository visibility：`PRIVATE`

候选 tag `v0.1-public-website-candidate.7` 及更早候选版本继续作为历史记录，不被改写成
正式 Developer Preview。

## Truth boundary（事实边界）

- `OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY`；
- `R-015` 为 0 critical、0 high、2 disclosed moderate advisories；
- DBOS 整仓不公开，只公开 exact public-safe wheel；
- 没有公共 Runtime、托管 API、Permission grant 或生产 SLA；
- Technical Validation Pilot 只完成设计，尚未获执行授权，14 项符合性负例执行数仍为 0；
- 第一位外部角色定义为 Reviewer；没有成立社区、招募 Contributor 或声明上游采用；
- 没有创建 Agent、Runtime、Entity、Capability instance、Permission 或科研 Evidence。
