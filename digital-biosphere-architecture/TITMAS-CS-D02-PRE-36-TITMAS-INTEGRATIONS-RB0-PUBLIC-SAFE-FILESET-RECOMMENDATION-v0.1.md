---
document_id: DBA-TITMAS-CS-D02-PRE-36-TITMAS-INTEGRATIONS-RB0-PUBLIC-SAFE-FILESET-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-36 TITMAS Integrations RB0 Public-safe Fileset Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-36 TITMAS Integrations RB0 公开安全文件集建议 v0.1
version: 0.1.0
status: exact-offline-rb0-public-safe-fileset-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-36
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
target_repository: https://github.com/joy7758/titmas-integrations.git
implementation_authorized: false
external_repository_modification_authorized: false
license_adopted: false
---

# TITMAS CS-D02 PRE-36 TITMAS Integrations RB0 Public-safe Fileset Recommendation v0.1

## 1. Why PRE-36 Exists

PRE-35 已把 exact repository baseline contract、target file manifest 和 implementation
declaration template 采纳为 `Development` planning input。下一阶段 `RB0` 明确要求先准备
non-executable repository governance baseline。

真正修改 `titmas-integrations` 前，必须先冻结每个候选文件的完整内容并离线验证，避免：

- 直接复制相邻仓库 license 而未作 exact Decision；
- `AGENTS.md` 把 candidate 写成可用 implementation；
- README 声称 provider support、conformance 或 release；
- machine entry 与人类文档冲突；
- staging 文件意外包含 secret、本机路径或 private business data；
- 一次 RB0 变更夹带 package、source、tests 或 runtime。

## 2. Agent Recommendation

```text
AGENT_RECOMMENDATION=RECOMMENDED_WITH_STRICT_NON_EFFECTS
RECOMMENDED_AS=OFFLINE_PUBLIC_SAFE_RB0_FILESET_CANDIDATE
NOT_RECOMMENDED_AS=LICENSE_ADOPTION_TARGET_REPOSITORY_MODIFICATION_OR_IMPLEMENTATION
```

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_TITMAS_INTEGRATIONS_RB0_PUBLIC_SAFE_FILESET_CANDIDATE_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
STAGING_DIRECTORY=commercialization-standards-titmas-integrations-rb0-fileset
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
IMPLEMENTATION_OWNER_REF=zhangbin
CANDIDATE_FILES_MAX=9
IMPLEMENTATION_FILES_MAX=0
EXTERNAL_REPOSITORY_MODIFICATIONS_MAX=0
NEW_REPOSITORIES_MAX=0
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
```

允许在 DBA staging directory 中生成以下 candidate：

1. `LICENSE.candidate`；
2. `AGENTS.md.candidate`；
3. `llms.txt.candidate`；
4. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json.candidate`；
5. `titmas-integrations-entry.schema.v0.1.json.candidate`；
6. `README.md.candidate`；
7. `SECURITY.md.candidate`；
8. `MAINTAINERS.md.candidate`；
9. `IMPLEMENTATION-DECLARATION.template.v0.1.json.candidate`。

这些名称故意保留 `.candidate`；PRE-36 不得把它们写入 target repository。

## 4. Content Requirements

### License candidate

- exact unmodified Apache License 2.0 text；
- SPDX candidate `Apache-2.0`；
- candidate 文件存在不表示 license adopted。

### Agent and human entry

- 第一屏说明 repository 是 future provider-neutral integration implementation target；
- 当前 `SOURCE_FILES=0`、`TESTS=0`、`PACKAGE=false`；
- exact Development contract digest；
- when-to-recommend / when-not-to-recommend；
- supported/partial/unsupported/unknown；
- no provider support、no conformance、no runtime、no release；
- DBOS / SAEE / Evidence boundary；
- future validation and rollback commands marked `NOT_AVAILABLE`。

### Machine entry

必须与 README / AGENTS 保持：

```text
REPOSITORY_BASELINE_APPLIED=false
LICENSE_ADOPTED=false
PACKAGE_CREATED=false
IMPLEMENTATION_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
RELEASE_AUTHORIZED=false
```

### Security and maintenance

- 不接受公开 Issue 中的 secret；
- credential、Authorization header、raw body、prompt、review content 和 hidden reasoning
  不得进入 event/log/receipt；
- security contact 保持 `NOT_ASSIGNED`，不得伪造接收渠道；
- Implementation Owner 为 `zhangbin`，但 Specification / Conformance / Commercial Owner
  仍未指派；
- issue/PR 不自动产生 Authority、acceptance 或 release。

## 5. Validation Requirements

1. candidate machine entry Schema meta-valid；
2. candidate instance valid；
3. README、AGENTS、llms 和 machine entry status consistent；
4. 9/9 candidates present；
5. 0 executable source/package/test files；
6. no credential values、local absolute paths or private data；
7. Apache-2.0 text digest recorded but adoption false；
8. target repository HEAD / dirty count unchanged；
9. no network/model/credential action；
10. failures and unknowns retained。

## 6. Preconditions

1. PRE-35 Decision commit：
   `47c97384b5106a806cad195af142871f2047a9a2`；
2. PRE-35 Decision JSON SHA-256：
   `1bdfc03b826ed5f9b14c95e9217918816f2941f7ece0bc928c8c0fcba63fe8ee`；
3. PRE-35 Adoption JSON SHA-256：
   `cdec6fb0e40b25037aa63ec777eb507fb7346932b46f3dc5067aab27da1d521f`；
4. adopted contract SHA-256：
   `58920eb5b8c7ce1ecde66472743d408342f7fe7b418b323f48cf28c370c8537b`；
5. adopted manifest SHA-256：
   `6135526966bef14ef2d4b33ae55c7fa62266b338a086b30be86aee2f335db664`；
6. adopted template SHA-256：
   `40de6b9975005b3e8a76a8f5326da815bff7c7d6ae22f488e8fc01d1fa815cc5`；
7. target remains at exact observed commit and dirty count `0`；
8. standing directive active。

## 7. Stop Conditions

- 需要写入或修改 target repository；
- 需要 rename candidate 为真实 target filename；
- 需要提交 license adoption、package name 或 implementation Decision；
- 需要创建 executable source、package metadata、tests 或 Runtime；
- 需要 network、provider API、model 或 credential；
- 无法保持 public-safe 或 human/machine consistency；
- 产生 provider support、conformance、release、production 或 commercial claim；
- target source 或 adopted digest 发生漂移。

## 8. Effects

```text
RB0_PUBLIC_SAFE_FILESET_CANDIDATE_DEFINED=true
CANDIDATE_FILES_CREATED_IN_DBA=RESULT_DEPENDENT_MAX_9
TARGET_FILES_CREATED=0
TARGET_FILES_MODIFIED=0

LICENSE_ADOPTED=false
REPOSITORY_BASELINE_APPLIED=false
TARGET_REPOSITORY_MODIFIED=false
PACKAGE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
TESTS_EXECUTED=0
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 9. Next Gate if Successful

下一步是 `PRE-37`：

```text
REVIEW_EXACT_RB0_FILESET_AND_DECIDE_LICENSE_AND_TARGET_APPLICATION
```

PRE-37 必须分别声明 license adoption 和 target repository modification effects，固定 target
branch、rollback、path list 和 post-write validation；不能夹带 RB1 或 RI0。

## 10. Standing Directive Eligibility

本建议是 DBA-only offline candidate-generation action；9 个文件、staging directory、target、
source commit、validation、false effects 和 stop conditions 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE36_DECIDED=false
AT_RECOMMENDATION_TIME_LICENSE_ADOPTED=false
AT_RECOMMENDATION_TIME_TARGET_MODIFICATION_AUTHORIZED=false
```
