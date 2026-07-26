---
document_id: DBA-TITMAS-CS-D02-PRE-36-TITMAS-INTEGRATIONS-RB0-PUBLIC-SAFE-FILESET-DECISION-0.1
title: TITMAS CS-D02 PRE-36 TITMAS Integrations RB0 Public-safe Fileset Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-36 TITMAS Integrations RB0 公开安全文件集决定记录 v0.1
version: 0.1.0
status: authorized-offline-rb0-public-safe-fileset-candidate-only
maturity: Development
decision_id: CS-D02-PRE-36
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
implementation_authorized: false
external_repository_modification_authorized: false
license_adopted: false
---

# TITMAS CS-D02 PRE-36 TITMAS Integrations RB0 Public-safe Fileset Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001`、PRE-35 Development adoption 和 PRE-36 exact
recommendation，授权：

```text
DECISION_RESULT=AUTHORIZE_OFFLINE_TITMAS_INTEGRATIONS_RB0_PUBLIC_SAFE_FILESET_CANDIDATE_ONLY
DECIDED_BY_REF=zhangbin
PRIMARY_REPOSITORY=digital-biosphere-architecture
STAGING_DIRECTORY=commercialization-standards-titmas-integrations-rb0-fileset
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
CANDIDATE_FILES_MAX=9
IMPLEMENTATION_FILES_MAX=0
EXTERNAL_REPOSITORY_MODIFICATIONS_MAX=0
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
```

## Authorized Outputs

只允许在 DBA staging directory 中形成以下保留 `.candidate` 后缀的文件：

1. `LICENSE.candidate`；
2. `AGENTS.md.candidate`；
3. `llms.txt.candidate`；
4. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json.candidate`；
5. `titmas-integrations-entry.schema.v0.1.json.candidate`；
6. `README.md.candidate`；
7. `SECURITY.md.candidate`；
8. `MAINTAINERS.md.candidate`；
9. `IMPLEMENTATION-DECLARATION.template.v0.1.json.candidate`。

`LICENSE.candidate` 可以包含 exact Apache License 2.0 text，但只作为待审候选；本决定不
采纳 license，也不允许把 candidate rename 或复制进 target repository。

## Stop Conditions

出现以下任一条件立即停止：

- target HEAD 或 dirty count 与冻结值不一致；
- 需要修改、写入、commit 或 push `titmas-integrations`；
- 需要创建 source、package metadata、tests、API 或 Runtime；
- 需要采用 license、package name、provider binding 或 release claim；
- 需要 network、model、provider API 或 credential；
- public-safe、human/machine consistency 或 failure preservation 无法验证。

## Non-effects

```text
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
