---
document_id: DBA-TITMAS-CS-D02-PRE-38-TITMAS-INTEGRATIONS-RB0-LICENSE-ADOPTION-AND-TARGET-APPLICATION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-38 TITMAS Integrations RB0 License Adoption and Target Application Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-38 TITMAS Integrations RB0 许可证采纳与目标应用建议 v0.1
version: 0.1.0
status: exact-license-adoption-and-target-application-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-38
standing_directive_reference: TITMAS-CS-STANDING-001
governance_repository: digital-biosphere-architecture
execution_primary_repository: titmas-integrations
target_repository: https://github.com/joy7758/titmas-integrations.git
license_adopted: false
target_repository_modification_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-38 TITMAS Integrations RB0 License Adoption and Target Application Recommendation v0.1

## 1. Why PRE-38 Exists

PRE-36 已生成九个 public-safe RB0 candidates；PRE-37 已完成 exact target mapping、
relative Schema gap resolution、revised ten-path manifest、application plan 和 rollback
plan。离线结果达到：

```text
PRE37_VALIDATION_PASS=true
PRE38_HUMAN_DECISION_REVIEW_READY=true
TARGET_PATHS_MAPPED=10
LOCAL_SCHEMA_REFERENCES_RESOLVED=2
TARGET_REPOSITORY_MODIFIED=false
LICENSE_ADOPTED=false
```

PRE-38 是第一个会改变 `titmas-integrations` 仓库状态的 gate。必须把 license adoption、
external repository modification、branch、exact paths、bytes、commit/push、validation 和
rollback 全部写清，不能从“准备就绪”推导执行权。

## 2. Agent Recommendation

```text
AGENT_RECOMMENDATION=RECOMMENDED_WITH_EXACT_TEN_PATH_AND_FAIL_CLOSED_REMOTE_BOUNDARY
RECOMMENDED_AS=NON_EXECUTABLE_RB0_REPOSITORY_GOVERNANCE_BASELINE_ONLY
NOT_RECOMMENDED_AS=RB1_PACKAGE_RI0_IMPLEMENTATION_PROVIDER_SUPPORT_CONFORMANCE_OR_RELEASE
```

推荐理由：

- target 当前只是目录占位和宽泛 README，智能体无法区分计划、实现、支持和符合性；
- exact RB0 文件集能提供人类／智能体／机器一致的零实现 truth surface；
- Apache-2.0 与开放、可替换基础设施方向一致；
- PRE-37 已纠正 template Schema 相对路径并验证 rollback；
- 变更不创建 package、source、tests、Runtime 或 provider binding。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=ADOPT_EXACT_APACHE_2_0_AND_AUTHORIZE_EXACT_TEN_PATH_TITMAS_INTEGRATIONS_RB0_APPLICATION_COMMIT_AND_PUSH_ONLY
GOVERNANCE_REPOSITORY=digital-biosphere-architecture
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
SOURCE_FILES_CREATED=0
PACKAGE_METADATA_FILES_CREATED=0
TEST_FILES_CREATED=0
NETWORK_REQUESTS_FOR_VALIDATION_MAX=0
MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
FORCE_PUSH_ALLOWED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 4. Exact Target Operations

### Create

1. `LICENSE`；
2. `AGENTS.md`；
3. `llms.txt`；
4. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json`；
5. `schemas/titmas-integrations-entry.schema.v0.1.json`；
6. `SECURITY.md`；
7. `MAINTAINERS.md`；
8. `IMPLEMENTATION-DECLARATION.template.v0.1.json`；
9. `implementation-declaration-template.schema.v0.1.json`。

### Update

10. `README.md`，prior SHA-256 必须为
    `7c05c774f54535b52947168c76cd766ed0ede73d98c7ccf09d07727b488eb685`。

Exact source bytes 和 digest 以
[revised manifest](commercialization-standards-titmas-integrations-rb0-target-mapping/revised-target-file-manifest.v0.2.json)
为准。

## 5. Execution Method

1. 从 exact baseline commit 建立隔离 worktree；
2. 创建 `codex/rb0-governance-baseline`；
3. 再次验证 remote/local baseline、dirty count 和 README digest；
4. 只把 revised manifest 的 ten exact source bytes 应用到 ten target paths；
5. 执行零网络 content/schema/path/security/non-claim validation；
6. 执行 rollback simulation，不修改真实 baseline history；
7. 只 stage ten target paths；
8. 使用 exact commit message；
9. 禁止 force，push exact branch；
10. 写回 DBA execution receipt 与 target commit。

## 6. Required Post-write Validation

- target paths exactly `10`；
- all ten target digests match revised manifest；
- all local `$schema` references resolve；
- both Schemas meta-valid；
- machine entry and implementation template instance-valid；
- README / AGENTS / llms / machine zero-state consistent；
- public-safe pattern matches `0`；
- executable source/package metadata/test files added `0`；
- target existing `.gitkeep` paths unchanged；
- rollback simulation restores prior README and removes only nine new paths；
- branch push confirmed without merge, PR, tag or release.

## 7. Preconditions

1. PRE-37 Decision commit:
   `1d34ae8c73bc0edf761264af9d9cfa20e8a90ef9`；
2. PRE-37 planning commit:
   `b29213e29f3a62749d35f65c243ae3abd21b9ddd`；
3. PRE-37 result commit:
   `4ff97084b1902e84552f8480e03f079c6d514378`；
4. PRE-37 result SHA-256:
   `06dc2d2a374ec94ca50b51810a7c2f7134eac076d95d538a39406080600f4631`；
5. PRE-37 validation result SHA-256:
   `684321375ec08a8f591544beb669d3345d050a4ca4298d0f07b314fa89eb2599`；
6. PRE-37 receipt SHA-256:
   `06e0ec68451d3ae0baeefe37507288ac6867a5e19ccdac4855d3a6f9c73477aa`；
7. revised manifest SHA-256:
   `aa6828203d33f2a73e04cdb71b1807e9a022c4bf95541b2dd366fa207f1ce508`；
8. target remains at exact baseline and dirty count `0`；
9. target branch does not already contain conflicting history；
10. standing directive remains active.

## 8. Stop Conditions

- local or remote target baseline drifts；
- target worktree is not clean；
- target branch exists with non-matching history；
- any exact source digest or prior README digest mismatches；
- any target path escapes the repository or collides；
- any local Schema reference is unresolved；
- source, package metadata, tests, API or Runtime would be created；
- credential, raw payload, private data or local path is detected；
- validation would require provider/model/credential action；
- push would require force；
- action would merge, open PR, tag, release, deploy or claim provider support,
  conformance, certification, production or commercial availability.

## 9. Explicit Effects

If PRE-38 is decided and validation succeeds:

```text
LICENSE_ADOPTED=true
TARGET_REPOSITORY_MODIFIED=true
REPOSITORY_BASELINE_APPLIED=true
TARGET_BRANCH_PUSHED=true

PACKAGE_CREATED=false
SOURCE_IMPLEMENTATION_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
TESTS_EXECUTED=0
RUNTIME_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
PRODUCTION_READY=false
```

## 10. Standing Directive Eligibility

这是 material external repository action，但 exact target、license、branch、paths、bytes、
validation、rollback、commit/push 和 false effects 已完整列出，符合常设授权第 5 节对
future exact recommendation packet 的要求。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
EXACT_DECISION_RECORD_REQUIRED=true
AT_RECOMMENDATION_TIME_LICENSE_ADOPTED=false
AT_RECOMMENDATION_TIME_TARGET_MODIFICATION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_ACTION_EXECUTED=false
```

## 11. Next Gate if Successful

下一步不是 RB1 或 RI0。先建立 `PRE-39`：

```text
VERIFY_REMOTE_CLEAN_CLONE_RB0_AND_DECIDE_RB0_ADOPTION_STATUS_ONLY
```

只有 clean clone、agent-readable entry、Schema/instance、rollback 和 remote branch
验证通过后，才能决定 RB0 是否作为 target repository Development baseline 被确认。
