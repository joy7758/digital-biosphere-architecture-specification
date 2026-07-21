---
review_id: TMAI-WEB-DEPENDENCY-REVIEW-20260722-001
title: Trusted Multi-Agent Infrastructure Website Dependency Review
title_zh: 可信多智能体基础设施网站依赖复核
status: review-complete-bounded-residual-disclosed
reviewed_at: 2026-07-22
formal_release_blocker_cleared: true
risk_acceptance_granted: false
---

# Website Dependency Review（网站依赖复核）

## Outcome（结论）

站点依赖已在不使用 `npm audit fix --force` 的条件下完成同主版本升级和回归验证。
完整依赖树从 12 项漏洞（2 low、2 moderate、8 high）降至 2 项 moderate；当前结果为
0 critical、0 high、2 moderate。正式发布前的 dependency review（依赖复核）已完成，
剩余风险必须继续在 release notes（发布说明）中披露，但不再单独阻塞静态网站发布。

这不是对第三方依赖的安全认证，也不产生 Runtime、Agent、Permission 或发布授权。

## Reviewed Change（已复核变更）

| Package | Before | Reviewed version |
|---|---:|---:|
| `next` / `eslint-config-next` | `16.2.6` | `16.2.11` |
| `react` / `react-dom` / `react-server-dom-webpack` | `19.2.6` | `19.2.8` |
| `@cloudflare/vite-plugin` | `1.37.1` | `1.45.1` |
| `vite` | `8.0.13` | `8.1.5` |
| `wrangler` | `4.92.0` | `4.112.0` |
| `@tailwindcss/postcss` / `tailwindcss` | `4.2.1` | `4.3.3` |
| `@vitejs/plugin-react` | `6.0.2` | `6.0.3` |
| `@vitejs/plugin-rsc` | `0.5.26` | `0.5.28` |

`npm audit fix` without force（不使用强制模式）还更新了可安全修复的间接依赖，消除了
完整依赖树中的 low 和 high 项。lockfile（锁文件）保留完整解析结果。

## Residual Advisory（残余通告）

剩余 2 项 moderate 都源于 `next@16.2.11` 内置的 `postcss@8.4.31`，对应
`GHSA-qx2v-qp2m-jg93`。在本次复核时，npm 仅给出 `next@9.3.3` 的强制降级方案；
该方案是破坏性且不符合当前 Next 16 架构，因此被拒绝。

风险边界如下：

- 百度云服务器只接收 `site/out/` 静态文件；
- 服务器不安装或运行 Node.js、Next.js、Vinext、Vite 或 PostCSS；
- PostCSS 只存在于受控构建阶段，不构成公开 Runtime（运行时）；
- 静态导出仍须通过内容边界、清单 hash（哈希）和线上响应验证；
- 当 Next 发布包含修复的非破坏性版本时，应重新审计并升级。

## Verification（验证）

| Check | Result |
|---|---|
| `npm audit` | `0 critical / 0 high / 2 moderate / 0 low` |
| `npm audit --omit=dev` | `0 critical / 0 high / 2 moderate / 0 low` |
| `npm test` | `5/5 PASS` |
| `npm run lint` | `PASS` |
| `SOURCE_REVISION=DEPENDENCY-AUDIT-PRECOMMIT npm run release:static` | `PASS` |
| Static source revision check | `PASS` |
| 20-file release manifest verification | `PASS` |

最终正式工件仍必须从合并后的 exact `origin/main` commit（精确主分支提交）重新构建；
`DEPENDENCY-AUDIT-PRECOMMIT` 只是一项预提交回归标记，不是发布 source revision。

```text
DEPENDENCY_REVIEW_COMPLETE=true
FORMAL_RELEASE_BLOCKER_CLEARED=true
DEPENDENCY_RISK_ACCEPTED=false
RUNTIME_DEPENDENCIES_DEPLOYED=false
CRITICAL_VULNERABILITIES=0
HIGH_VULNERABILITIES=0
MODERATE_VULNERABILITIES=2
FORCED_AUDIT_FIX_USED=false
```
