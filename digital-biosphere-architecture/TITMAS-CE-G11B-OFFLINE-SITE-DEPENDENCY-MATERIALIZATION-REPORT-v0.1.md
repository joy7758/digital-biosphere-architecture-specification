# TITMAS CE-G11B Offline Site Dependency Materialization Report v0.1

```text
RESULT=FAIL_CLOSED_NPM_CI_LOCKFILE_SYNC_REPORTED_MISSING_SITE_0_1_0
COMMAND=npm ci --offline --ignore-scripts --no-audit --no-fund
ATTEMPTS=1
EXIT_CODE=1
NPM_ERROR_CODE=EUSAGE
RETRIES=0
NETWORK_FALLBACKS=0
INSTALL_SCRIPTS=0
EXISTING_NODE_MODULES_REUSE=0
SITE_TESTS=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
```

npm 11.12.1 报告 package/lock 不同步，并报告 lockfile 缺少 `site@0.1.0`。静态观察显示
root name/version 与 package.json 一致，也没有发现显式 `site` dependency；因此 exact
root cause、npm bug 和 lockfile defect 均未证明。

一次性安装授权已消耗。不得重试、切换安装方式、联网或复用现成 `node_modules`。
下一步只允许准备 zero-install npm CLI / lockfile behavior diagnostic Recommendation。
