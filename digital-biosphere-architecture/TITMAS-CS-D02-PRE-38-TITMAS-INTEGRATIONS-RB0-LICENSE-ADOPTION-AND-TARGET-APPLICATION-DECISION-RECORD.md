---
document_id: DBA-TITMAS-CS-D02-PRE-38-TITMAS-INTEGRATIONS-RB0-LICENSE-ADOPTION-AND-TARGET-APPLICATION-DECISION-0.1
title: TITMAS CS-D02 PRE-38 TITMAS Integrations RB0 License Adoption and Target Application Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-38 TITMAS Integrations RB0 许可证采纳与目标应用决定记录 v0.1
version: 0.1.0
status: authorized-exact-license-and-ten-path-rb0-application-pending-validation
maturity: Development
decision_id: CS-D02-PRE-38
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
license_adoption_decided: true
target_repository_modification_authorized: true
implementation_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-38 TITMAS Integrations RB0 License Adoption and Target Application Decision Record v0.1

## Standing Directive Eligibility

PRE-38 recommendation 已绑定一个 exact option、governance/execution repositories、target
baseline、branch、ten paths、bytes/digests、license、validation、rollback、commit/push、
false effects 和 stop conditions。它没有与更晚人类决定冲突。

因此依据 `TITMAS-CS-STANDING-001`：

```text
STANDING_DIRECTIVE_APPLICABLE=true
AUTOMATIC_GATE_APPROVAL=false
AGENT_SELF_APPROVAL=false
DECIDED_BY_REF=zhangbin
DECISION_RECORD_REQUIRED=true
```

## Decision

```text
DECISION_RESULT=ADOPT_EXACT_APACHE_2_0_AND_AUTHORIZE_EXACT_TEN_PATH_TITMAS_INTEGRATIONS_RB0_APPLICATION_COMMIT_AND_PUSH_ONLY
EXECUTION_PRIMARY_REPOSITORY=titmas-integrations
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BASELINE_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
TARGET_BRANCH=codex/rb0-governance-baseline
COMMIT_MESSAGE=chore: establish TITMAS integrations RB0 governance baseline
LICENSE_SPDX=Apache-2.0
LICENSE_SHA256=2191d05c6ee7c145480916b745bd020484adb61653be943c43cff10bc22927a1
TARGET_PATHS_EXACT=10
TARGET_FILES_CREATED=9
TARGET_FILES_UPDATED=1
```

授权只覆盖：

- 从 exact baseline 创建隔离 worktree 和 exact target branch；
- 应用 revised manifest 中的十个 exact path/digest；
- 零 provider/model/credential 的本地验证和 rollback simulation；
- path-scoped commit；
- 非 force push exact branch；
- 把 execution result 和 target commit 写回 DBA。

## Stop Conditions

出现 baseline/branch/digest/README/path/Schema/public-safe/rollback 漂移，或需要 source、
package、tests、Runtime、provider/model/credential、force push、merge、PR、tag、release、
deployment、provider support、conformance、certification、production 或 commercial claim
时必须 fail closed。

## Decision Effects Before Execution

```text
LICENSE_ADOPTION_DECIDED=true
LICENSE_FILE_APPLIED=false
EXTERNAL_REPOSITORY_MODIFICATION_AUTHORIZED=true
TARGET_REPOSITORY_MODIFIED=false
TARGET_BRANCH_PUSH_AUTHORIZED=true

ARCHITECTURE_AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```
