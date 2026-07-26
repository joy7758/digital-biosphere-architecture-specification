---
document_id: DBA-PROVIDER-REQUEST-INSTRUMENTATION-OWNER-TARGET-ASSIGNMENT-0.1
title: Provider Request Instrumentation Owner and Target Assignment v0.1
title_zh: Provider 请求可观测实现 Owner 与目标指派 v0.1
version: 0.1.0
status: bounded-owner-assigned-development-candidate-target-accepted
maturity: Development
decision_reference: CS-D02-PRE-33
implementation_authorized: false
external_repository_modified: false
---

# Provider Request Instrumentation Owner and Target Assignment v0.1

## Assignment

| field | value |
|---|---|
| bounded Implementation Owner | `zhangbin` |
| responsibility | future exact source maintenance and repository-baseline Proposal responsibility |
| Development candidate target | `https://github.com/joy7758/titmas-integrations.git` |
| observed target commit | `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8` |
| acceptance scope | repository baseline planning only |
| implementation authorization | `false` |

该指派解决的是“谁对未来实现 source 负责”和“下一份 baseline Proposal 指向哪个现有
候选仓库”。它不证明账号权限，不修改候选仓库，也不建立实现、provider support、
conformance 或 release。

## Required Separation

```text
SPECIFICATION_OWNER=NOT_ASSIGNED
IMPLEMENTATION_OWNER=zhangbin
CONFORMANCE_REVIEWER=NOT_ASSIGNED
COMMERCIAL_OFFERING_OWNER=NOT_ASSIGNED

DBA=SPECIFICATION_ONLY
DBOS=EXISTENCE_AND_EVIDENCE_BOUNDARY
SAEE=READ_ONLY_EVALUATION
TITMAS_INTEGRATIONS=DEVELOPMENT_CANDIDATE_TARGET_ONLY
```

## Next Gate

候选仓库在任何修改前，必须完成独立 repository baseline remediation contract，至少覆盖：

- exact license Decision；
- `AGENTS.md` 与 agent-readable discovery；
- package/API boundary；
- provider-neutral core 与 provider binding layout；
- deterministic tests 和 negative cases；
- security / secret handling；
- maintenance、version、deprecation、rollback；
- conformance 与 release non-claims。

```text
REPOSITORY_BASELINE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_REPOSITORY_MODIFICATION_AUTHORIZED=false
```
