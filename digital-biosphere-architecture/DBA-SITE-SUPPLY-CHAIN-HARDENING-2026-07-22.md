# DBA Site Supply-Chain Hardening Receipt

```text
receipt_id=TMAI-DBA-SITE-SUPPLY-CHAIN-HARDENING-20260722-001
trigger=PR_G2A_PACKET_CLEAN_CLONE_AT_CDDD0C7
initial_audit=1_MODERATE_6_HIGH_0_CRITICAL
post_hardening_audit=0_TOTAL
deployment_performed=false
production_ready=false
```

## Outcome（结果）

从远端 `codex/production-observability-baseline@cddd0c7600bf3615cef4f9be381e16c98a701c2b`
执行 clean `npm ci` 时，当前 advisory database 报告 7 项依赖漏洞：1 moderate、6 high。
这是旧 `R-015` 的事实漂移，不能继续沿用“2 moderate”快照。

本次只加固 DBA 静态站点的 build dependency graph（构建依赖图），没有部署网站，也没有
修改 DBOS、SAEE、Runtime、Agent、Entity、Permission 或 Evidence。

## Exact Resolution（精确处置）

| package | old resolved version | override | reason |
|---|---:|---:|---|
| `fast-uri` | `3.1.2` | `3.1.4` | 关闭 IDN/backslash host-confusion advisories，同时保持 AJV 的 `^3` 范围 |
| `postcss` | Next 内嵌 `8.4.31` | `8.5.22` | 关闭 CSS stringify advisory；统一到当前已验证 8.x |
| `sharp` | `0.34.5` | `0.35.3` | 关闭继承的 libvips advisories；Node 要求 `>=20.9.0` |

没有执行 `npm audit fix --force`，因为 advisory 自动建议会把 Next、Wrangler 或 Cloudflare
Vite plugin 降级到不相容旧版本，不能作为安全修复。

## Exact Files（精确文件）

```text
site/package.json.sha256=e78a322a1580090e4dab22458d4e1df9572d5ae66557793a4cd0d04efd0ae136
site/package-lock.json.sha256=4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd
node=v26.0.0
npm=11.12.1
platform=Darwin-arm64
```

## Validation（验证）

```text
npm_ci=PASS
npm_audit_total=0
npm_audit_critical=0
npm_audit_high=0
npm_audit_moderate=0
site_build=PASS
site_tests=11/11_PASS
site_lint=PASS
```

Audit 是时间点供应链观察，不是永久安全证明。未来 upstream compatible release（上游兼容
版本）可替代 overrides 时，必须单独审查并重跑 clean clone、build、tests、lint 和 audit。
