---
document_id: DBA-TITMAS-CS-D02-PRE-49-RB1-CONFORMANCE-HARNESS-AND-LOCAL-VERIFICATION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-49 RB1 Conformance Harness and Local Verification Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-49 RB1 符合性工具与本地验证建议 v0.1
version: 0.1.0
status: exact-recommendation-ready-not-decided
maturity: Development
recommendation_id: CS-D02-PRE-49
primary_repository: digital-biosphere-architecture
target_repository: https://github.com/joy7758/titmas-integrations.git
target_write_authorized: false
conformance_execution_authorized: false
provider_binding_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-49 RB1 Conformance Harness and Local Verification Recommendation v0.1

## Recommendation

```text
RECOMMENDATION=AUTHORIZE_EXACT_RB1_INDEPENDENT_PATH_CONFORMANCE_HARNESS_AND_LOCAL_CONTRACT_REHEARSAL
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_HEAD=001da006aa32a1eeeb058daa31dcab39197fa4de
TARGET_MAIN=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
NEW_FILES_MAX=16
UPDATED_FILES_MAX=8
CONFORMANCE_FIXTURES=7
CONFORMANCE_SOURCE_FILES=1
TEST_FILES_ADDED=1
PROVIDER_BINDINGS_MAX=0
NETWORK_REQUESTS_MAX=0
RUNTIME_INSTANCES_MAX=0
RELEASES_MAX=0
```

PRE-48 已在 exact target commit 建立 Development reference implementation，
14/14 paths、20/20 tests、2/2 machine Schema、6/6 declared artifact digests 和远端
clean clone 均通过。当前仍缺少一个不导入实现模块、只消费 serialized phase trace 的
independent-path conformance harness。

本建议只建立本地 Development contract rehearsal。这里的
`independent-path` 表示 validator 实现路径与 `titmas_integrations.instrumentation`
分离，不表示第三方机构、独立实验室、认证、Provider conformance 或标准组织认可。

## Agent Recommendation Basis

PRE-47 三个 qualifying Agent reviewer 均为 `CONDITIONALLY_RECOMMENDED`，共同要求：

1. 固定 P0–P9 taxonomy 与 attribution rules；
2. 定义 serialization contract；
3. 提供 schema version；
4. 明确 retention boundary；
5. 建立 conformance-style negative tests。

PRE-48 已完成前四项并执行代码级负边界测试。PRE-49 只处理第五项及 serialized
artifact 的独立验证路径。该 Agent review 不是 conformance authorization，也不是
Human Customer Evidence。

## Constitutional Alignment

- 验证器是职责单一、边界受限、可替换的小组件，不建立中心控制器；
- Observation 仍不等于 Evidence 或 Truth；
- validator result 不是 Authority、Permission、Authorization 或 Command；
- first failure 不得被 retry、fallback、repair 或 fixture normalization 改写；
- validator 不导入 DBOS、SAEE、Provider SDK 或 target implementation module；
- local rehearsal 不自动升级为 Provider、Runtime、production 或 commercial claim。

## Exact Target Fileset

只允许新增 16 个文件：

1. `CONFORMANCE.md`
2. `CONFORMANCE-DECLARATION.v0.1.json`
3. `schemas/conformance-declaration.schema.v0.1.json`
4. `conformance/phase-trace-conformance-profile.v0.1.json`
5. `conformance/phase-trace-conformance-profile.schema.v0.1.json`
6. `conformance/case-manifest.v0.1.json`
7. `conformance/case-manifest.schema.v0.1.json`
8. `conformance/validate.py`
9. `conformance/fixtures/pass-success.v0.1.json`
10. `conformance/fixtures/pass-failure-p0.v0.1.json`
11. `conformance/fixtures/pass-failure-p9.v0.1.json`
12. `conformance/fixtures/fail-multiple-fail.v0.1.json`
13. `conformance/fixtures/fail-post-failure-execution.v0.1.json`
14. `conformance/fixtures/fail-sensitive-additional-field.v0.1.json`
15. `conformance/fixtures/fail-phase-order.v0.1.json`
16. `tests/test_conformance_harness.py`

只允许更新 8 个文件：

1. `README.md`
2. `AGENTS.md`
3. `SECURITY.md`
4. `llms.txt`
5. `IMPLEMENTATION-DECLARATION.v0.1.json`
6. `schemas/implementation-declaration.schema.v0.1.json`
7. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json`
8. `schemas/titmas-integrations-entry.schema.v0.1.json`

禁止修改或删除其他路径。现有 package public API 和 P0–P9 实现不能改变。

## Conformance Profile

`phase-trace-conformance-profile.v0.1.json` 必须固定：

```text
PROFILE_VERSION=0.1.0
IMPLEMENTED_CONTRACT_SHA256=f72eb33bdb5042514deed499fdabddbc74121bc9c22c16f79316eae2aeca9913
TARGET_IMPLEMENTATION_COMMIT=001da006aa32a1eeeb058daa31dcab39197fa4de
VALIDATOR_IMPORTS_TARGET_IMPLEMENTATION=false
VALIDATOR_RUNTIME_DEPENDENCIES=0
PROVIDER_CONFORMANCE=false
THIRD_PARTY_INDEPENDENCE=false
CERTIFICATION=false
```

Profile 只验证：

- serialized top-level shape、`schema_version=0.1.0` 和 additional properties；
- exact P0–P9 order、predecessor、status、executed 与 failure category；
- 非负 timing/byte count、HTTP status、safe opaque reference 和 digest shape；
- 成功 trace 全 PASS；
- 失败 trace 只有一个首个 FAIL，后续全部未执行；
- sensitive/raw/prompt/review/hidden-reasoning 字段不可表达；
- fixture manifest 的 path、SHA-256、expected result 与 case ID。

不验证网络、Provider 请求、模型行为、DBOS Evidence admission、SAEE evaluation、
operational security、production reliability 或 customer value。

## Fixture Corpus

冻结 7 个 serialized fixture：

| case | expected | purpose |
|---|---|---|
| `CONF-PASS-001` | `PASS` | 完整成功 P0–P9 |
| `CONF-PASS-002` | `PASS` | P0 为首个失败，P1–P9 未执行 |
| `CONF-PASS-003` | `PASS` | P9 为首个失败 |
| `CONF-FAIL-001` | `FAIL` | 多个 FAIL |
| `CONF-FAIL-002` | `FAIL` | 首个失败后继续执行 |
| `CONF-FAIL-003` | `FAIL` | 增加 `prompt` 等敏感 additional field |
| `CONF-FAIL-004` | `FAIL` | phase 顺序错误 |

Manifest 必须保存每个 fixture 的 one-way SHA-256。Validator 不允许修改、归一化、
修复或覆盖 fixture。

## Validator Independence and Authority Boundary

`conformance/validate.py`：

- 只使用 Python standard library；
- 不 import `titmas_integrations`；
- 不 import DBOS、SAEE、Provider SDK 或网络模块；
- 不写入 fixture 或结果历史；
- 输出 deterministic summary；
- 对 manifest hash drift、path escape、duplicate case ID、unknown expected result 和
  validator exception fail closed；
- exit code 只表示本次 local rehearsal 是否符合冻结预期。

Validator PASS 不产生 Evidence、Truth、Permission、Authorization、Certification、
Provider support 或 release status。

## Commands and Environment

冻结命令：

```text
TEST_COMMAND=PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v
CONFORMANCE_COMMAND=PYTHONDONTWRITEBYTECODE=1 python3 conformance/validate.py --manifest conformance/case-manifest.v0.1.json
BUILD_COMMAND=uv build --offline --out-dir <fresh-temporary-directory>
NETWORK_ALLOWED=false
```

当前机器已直接观察到：

```text
PYTHON_3_14_AVAILABLE=true
UV_0_11_16_AVAILABLE=true
PYTHON_BUILD_MODULE_AVAILABLE=false
SETUPTOOLS_IN_ACTIVE_PYTHON_AVAILABLE=false
```

Build 必须只用 `uv build --offline`。若 cache 或 backend 不可用，记录
`NOT_EXECUTED_OR_FAILED_OFFLINE_DEPENDENCY_UNAVAILABLE` 并停止 build claim；不得联网
安装。Build artifact 只进入新建临时目录，记录 hash 后不发布、不复制进仓库。

## Truth-surface Result Classes

只有全部 tests、fixture manifest、validator、Schema、hash、source boundary 和远端
clean-clone 通过时，目标 truth surface 才可写：

```text
LOCAL_REFERENCE_CONTRACT_REHEARSAL=PASS
INDEPENDENT_PATH_VALIDATOR=true
THIRD_PARTY_INDEPENDENT_CONFORMANCE=false
PROVIDER_CONFORMANCE_EXECUTED=false
PROVIDER_SUPPORTED=false
SECURITY_REVIEW_EXECUTED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_AVAILABILITY=NOT_CLAIMED
```

结果分级：

- `PASS_LOCAL_REFERENCE_CONTRACT_REHEARSAL`
- `FAIL_LOCAL_REFERENCE_CONTRACT_REHEARSAL`
- `BLOCKED_INPUT_OR_ENVIRONMENT`

任何失败和 unknown 必须保留，不得降阈值、修复 fixture 或改成 PASS。

## Validation and Result

执行后必须：

1. 验证 target HEAD、`main`、contract hash 和 PRE-48 artifact digests；
2. 比对 exact 24-path fileset；
3. 运行全部 unit tests；
4. 运行独立路径 conformance command；
5. 验证 profile、manifest、declaration 和 target entry Schema；
6. 验证 7/7 fixture hashes；
7. 扫描 validator 不导入 target implementation、网络、Provider、DBOS 或 SAEE；
8. 执行 offline build 或保留精确失败；
9. 路径限定提交、推送非默认分支；
10. 从远端 clean clone 重跑 tests、conformance、Schema 和 hash；
11. 在 DBA 保存 result、receipt、target commit 与失败。

## Rollback

```text
TARGET_PARENT=001da006aa32a1eeeb058daa31dcab39197fa4de
FORCE_PUSH_ALLOWED=false
MAIN_BRANCH_WRITE_ALLOWED=false
```

Rollback 只能通过后继提交删除 16 个新增文件并恢复 8 个更新文件，不能重写历史。

## Non-effects

```text
RECOMMENDATION_IS_DECISION=false
TARGET_WRITE_AUTHORIZED=false
CONFORMANCE_EXECUTION_AUTHORIZED=false
PROVIDER_BINDING_CREATED=false
PROVIDER_SUPPORTED=false
PROVIDER_CORRECTNESS_PROVEN=false
THIRD_PARTY_INDEPENDENT_CONFORMANCE=false
DBOS_CHANGED=false
SAEE_CHANGED=false
AGENT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_TRUTH_CHANGED=false
MAIN_CHANGED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```

## Stop Conditions

target commit、24-path fileset、public API、contract hash、fixture corpus、validator
independence、build offline boundary、result classification、rollback 或 truth surface
发生漂移；需要网络、Provider binding、DBOS/SAEE change、Agent/Runtime、Permission、
main、merge、PR、tag、release、deployment、certification 或 commercial claim 时立即
fail closed。

## Standing Directive Assessment

该建议只有一个 exact option，固定 repository/branch/commit、24 paths、7 fixtures、
independent-path validator、offline build、commands、result classes、rollback、
non-effects 和 stop rules，满足 `TITMAS-CS-STANDING-001` 候选条件。

本文件只是 Recommendation。目标写入和 conformance rehearsal 开始前仍须独立
PRE-49 Decision Record。
