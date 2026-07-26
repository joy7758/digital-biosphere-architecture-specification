# PRE-38 TITMAS Integrations RB0 Target Application Result v0.1

## Result

```text
PRE38_RESULT=REMOTE_BRANCH_PUSHED_SEMANTIC_TRUTH_CONFLICT_FAIL_CLOSED_REMEDIATION_REQUIRED
PRE38_DECISION_COMMIT=16a5282ab5dd551787529116fd02bb83921b5cf9
TARGET_BASELINE_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_COMMIT=d54bf17ea94ee614b83253cd6abd8cb51bfdd45b
TARGET_PATHS_APPLIED=10
TARGET_PATH_DIGESTS_MATCH=10
REMOTE_BRANCH_PUSHED=true
REMOTE_MAIN_UNCHANGED=true
LICENSE_ADOPTION_DECIDED=true
LICENSE_FILE_APPLIED_TO_TARGET_BRANCH=true
SEMANTIC_TRUTH_CONSISTENT=false
REPOSITORY_BASELINE_VALIDATED=false
REMEDIATION_REQUIRED=true
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## Execution history

PRE-38 的目标写入和远端分支推送已经发生，不能被后续失败抹去：

1. 第一次 pre-commit path enumeration 使用 `git status --porcelain`，Git 把未跟踪的
   `schemas/` 折叠为目录项，导致 exact-path 比较失败。该失败保留为
   `GIT_STATUS_UNTRACKED_DIRECTORY_COLLAPSE`；
2. 第二次改用 `git ls-files --others --exclude-standard` 后，十个 path、十个 digest、
   两个 Schema、两个 instance、两个本地 Schema 引用、public-safe 检查和 rollback
   dry-run 均通过；
3. exact path-scoped commit 被非 force push 到
   `codex/rb0-governance-baseline`；
4. post-push semantic truth audit 发现 README、Agent entry、LLM entry、machine entry、
   Security 和 Maintainers 仍声明“candidate not applied”或
   `LICENSE_ADOPTED=false`。这些声明与 PRE-38 Decision 和远端分支事实冲突，因此最终结果
   fail closed。

## What is true

- Apache-2.0 adoption 已由 PRE-38 Decision 明确决定；
- exact `LICENSE` bytes 已进入目标分支；
- 目标分支已经创建、commit 并 push；
- `origin/main` 仍保持原 commit，未 merge；
- package、source、tests、Runtime、provider support、conformance、Certification、
  Release 和 Commercial Offering 均未产生。

## What is not true

- 不能把该分支称为 truth-consistent RB0 baseline；
- 不能声称 RB0 已完成 validation 或 adoption；
- 不能 merge、开 PR、tag、release 或进入 RB1；
- 不能删除、force-push、amend 或重写已经推送的失败历史。

## Required remediation

后继 Recommendation 必须只处理七个 truth-surface path：

1. `README.md`；
2. `AGENTS.md`；
3. `llms.txt`；
4. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json`；
5. `schemas/titmas-integrations-entry.schema.v0.1.json`；
6. `SECURITY.md`；
7. `MAINTAINERS.md`。

修正只能陈述“RB0 applied to this branch, not merged”，不得增加实现、Provider、
Conformance、Runtime、Release、Permission、Authority 或商业状态。
