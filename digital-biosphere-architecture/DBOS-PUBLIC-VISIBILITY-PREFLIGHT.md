---
document_id: DBA-DBOS-PUBLIC-VISIBILITY-PREFLIGHT-2026-07-21
title: DBOS Repository Public Visibility Preflight
title_zh: DBOS 仓库公开可见性预检
status: private-collaborator-trial-selected-public-visibility-not-authorized
source_commit: b4e3cbe2af442be861dbab3f7b2ffd2567443077
repository_visibility: private
repository_visibility_changed: false
decision_reference: architecture/ADR-020-release-preparation-owner-decisions.md
child_repository_modified: false
last_reviewed: 2026-07-21
---

# DBOS Public Visibility Preflight（DBOS 公开可见性预检）

## 1. Scope（范围）

本报告为 `DQ-014` 提供只读预检。它检查当前 DBOS 冻结提交的已跟踪文件、Git 历史
文件名、常见高置信度密钥标记、超大 blob（内容对象）、GitHub 安全功能和许可证状态。
它不改变 GitHub visibility（可见性），不替代专业 secret scan（密钥扫描）、法律审查
或 Domain Owner 的公开决定。

```text
PRIMARY_REPOSITORY=DBA
OBSERVED_CHILD_REPOSITORY=DBOS
DBOS_MODIFIED=false
GITHUB_VISIBILITY_CHANGED=false
```

## 2. Observed Snapshot（观察快照）

| 项目 | 结果 |
|---|---|
| GitHub repository | `joy7758/digital-biosphere-os` |
| Commit | `b4e3cbe2af442be861dbab3f7b2ffd2567443077` |
| Visibility | `PRIVATE` |
| Tracked files | 457 |
| Root `LICENSE` | 缺失 |
| Sensitive filename patterns | 0 个命中 |
| Private-key PEM markers | 0 个命中 |
| High-confidence AWS/GitHub/OpenAI/Google token patterns | 0 个命中 |
| Generic credential assignment patterns | 0 个命中 |
| Sensitive filenames in reachable Git history | 0 个命中 |
| Reachable Git blobs over 5 MiB | 0 个命中 |
| Independent scanner | `gitleaks/gitleaks@v8.30.1`；官方 checksum（校验和）通过 |
| Reachable Git history scanned | 2 commits；约 3.87 MB |
| Gitleaks findings | 0 |
| GitHub Secret Scanning | `DISABLED` |
| GitHub Dependabot Alerts | `DISABLED` |

扫描只报告文件和模式计数，不输出任何可能的 secret value（密钥值）。

## 3. Interpretation（解释）

当前快照与独立 Gitleaks 历史扫描均未发现密钥，是 `DQ-014` 的正向信号，
但不足以证明仓库可以立即公开：

- Gitleaks 覆盖当前可达 Git 历史，但任何规则型 scanner（扫描器）都不能证明不存在
  未知格式、外部存储、运行时 secret 或未纳入 Git 的私有材料；
- GitHub Secret Scanning 当前禁用，没有平台侧 alert evidence（告警证据）；
- Dependabot Alerts 当前禁用，没有平台侧依赖漏洞告警面；
- 根许可证缺失，外部复制、修改和分发权利不明确；
- `PRIVATE` 仓库的 authenticated clean clone（认证检出）不等于匿名开发者可访问；
- 公开前仍需确认文档、fixture、历史 commit message 和个人数据边界。

## 4. Decision and Future Public Gate（决定与未来公开闸门）

`ADR-020` 已选择 `PRIVATE_COLLABORATOR_TRIAL`。本次试用不把 DBOS 切换为 public，
不把认证检出写成匿名可用，也不授权具体协作者。未来如提出 public visibility 变化，
仍必须重新完成下列闸门并形成新决定：

1. `DQ-012` 选择许可证，并由各 Repository Owner 采用；
2. 在未来最终 remote commit 与 tag 上重跑相同 Gitleaks 版本；
3. 明确 GitHub Secret Scanning / Dependabot 的启用策略；
4. 对个人数据、私有域名、内部地址、凭据占位符和第三方资产做人工抽样复核；
5. 决定先进行 private collaborator trial（私有协作者试用）还是直接 public；
6. 公开后从无认证环境执行 anonymous clone、安装、测试、Validator 和 Demo；
7. 保留 visibility rollback（可见性回退）和 incident response（事件响应）责任人。

## 5. Decision State（决策状态）

```text
DQ_014_PRELIMINARY_TECHNICAL_INPUT_COMPLETE=true
HIGH_CONFIDENCE_SECRET_PATTERN_HITS=0
GITLEAKS_FULL_REACHABLE_HISTORY_SCAN_PASS=true
GITLEAKS_FINDINGS=0
FULL_SECRET_HISTORY_AUDIT_COMPLETE=false
LICENSE_SELECTED=true
LICENSE_ID=Apache-2.0
DBOS_PUBLIC=false
DBOS_PUBLICATION_AUTHORIZED=false
PRIVATE_COLLABORATOR_TRIAL_SELECTED=true
COLLABORATORS_ADDED=0
DEVELOPER_PREVIEW_RELEASED=false
```

结论：`PRIVATE_COLLABORATOR_TRIAL` 已被 Human Owner 选择；本预检和该选择不自动批准
添加具体协作者、改变仓库可见性或正式发布。
