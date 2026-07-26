---
document_id: DBA-TITMAS-CS-D02-PRE-48-RB1-BOUNDED-IMPLEMENTATION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-48 RB1 Bounded Implementation Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-48 RB1 有界实现建议 v0.1
version: 0.1.0
status: exact-recommendation-ready-not-decided
maturity: Development
recommendation_id: CS-D02-PRE-48
primary_repository: digital-biosphere-architecture
target_repository: https://github.com/joy7758/titmas-integrations.git
target_write_authorized: false
implementation_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-48 RB1 Bounded Implementation Recommendation v0.1

## Recommendation

```text
RECOMMENDATION=AUTHORIZE_EXACT_RB1_PROVIDER_NEUTRAL_PHASE_CONTRACT_REFERENCE_IMPLEMENTATION_AND_TESTS
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_HEAD=f80629364752c465316b9d1238fe5447a88565ca
NEW_FILES_MAX=8
UPDATED_FILES_MAX=6
SOURCE_FILES_MAX=2
TEST_FILES_MAX=2
PROVIDER_BINDINGS_MAX=0
NETWORK_CALLS_IN_IMPLEMENTATION_MAX=0
RUNTIME_INSTANCES_MAX=0
RELEASES_MAX=0
```

PRE-47 Agent Review 以 `3/4` qualifying、3 个 `CONDITIONALLY_RECOMMENDED`、0
Authority safety failures 通过冻结闸门。三个 qualifying reviewer 一致认为问题相关、
入口清晰、学习成本低，但要求实现前补齐：

1. P0–P9 phase taxonomy 和 attribution rules；
2. trace serialization contract；
3. Schema version；
4. immutable first-failure record 的 retention 边界；
5. conformance-style negative tests。

PRE-48 只建议建立一个纯数据、provider-neutral、可替换的 reference implementation。
它不实现网络请求、不绑定模型 Provider、不生成 Evidence、不调用 DBOS 或 SAEE。

## Constitutional Alignment

本建议遵守 TITMAS Digital Immune Constitution：

- 不建立无限强中心，只提供一个可组合、可替换的小主体契约；
- 明确 Capability、Authority、Permission 和 Execution 边界；
- Observation 只记录发生了什么，不自动成为 Evidence 或 Truth；
- 首个失败不可由 retry、fallback 或 repair 改写；
- 实现可被其他 Agent/Adapter 复用，但不能自动获得权限。

## Exact Target Fileset

只允许新增 8 个文件：

1. `pyproject.toml`；
2. `src/titmas_integrations/__init__.py`；
3. `src/titmas_integrations/instrumentation.py`；
4. `schemas/phase-trace.schema.v0.1.json`；
5. `tests/test_instrumentation_contract.py`；
6. `tests/test_negative_boundaries.py`；
7. `IMPLEMENTATION-DECLARATION.v0.1.json`；
8. `schemas/implementation-declaration.schema.v0.1.json`。

只允许更新 6 个现有文件：

1. `README.md`；
2. `AGENTS.md`；
3. `SECURITY.md`；
4. `llms.txt`；
5. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json`；
6. `schemas/titmas-integrations-entry.schema.v0.1.json`。

禁止修改或删除其他路径。`crewai/`、`langchain/`、`mcp/`、`openai-agents/` 和
`examples/` 保持空占位，不创建 Provider/Framework binding。

## Distribution and Namespace

PRE-48 Decision 如采纳，将只为 Development branch 固定：

```text
DISTRIBUTION_NAME=titmas-integrations
PYTHON_IMPORT_NAMESPACE=titmas_integrations
MINIMUM_PYTHON=3.11
RUNTIME_DEPENDENCIES=0
PROVIDER_DEPENDENCIES=0
```

包可以在隔离本地环境构建和测试，但不能发布到 PyPI、GitHub Release 或任何 registry。
“Package created”只表示 source tree 中存在可构建 Development package，不表示 release
或 commercial availability。

## Public API Candidate Adopted Only by Decision

唯一允许的 public symbols：

- `PhaseId`
- `PhaseStatus`
- `FailureCategory`
- `PhaseEvent`
- `PhaseTrace`
- `validate_phase_trace`

禁止公开：

- HTTP client；
- Provider client；
- retry/fallback executor；
- DBOS Evidence writer；
- SAEE evaluator；
- Runtime、Agent、Permission 或 Authorization API。

## P0–P9 Attribution Contract

`PhaseId` 顺序固定：

```text
P0 DNS_RESOLUTION
P1 TCP_CONNECT
P2 TLS_HANDSHAKE
P3 HTTP_REQUEST_HEADERS_WRITE
P4 HTTP_REQUEST_BODY_WRITE
P5 HTTP_RESPONSE_STATUS_AND_HEADERS
P6 HTTP_RESPONSE_BODY
P7 RESPONSE_CONTENT_EXTRACTION
P8 RESPONSE_SCHEMA_VALIDATION
P9 SANITIZED_RESULT_HANDOFF_COMMIT
```

每个 `PhaseTrace` 必须包含完整、无重复的 P0–P9：

- P0 predecessor 为 `null`；
- 后续 predecessor 必须是前一个 phase；
- 成功路径全部为 `PASS`；
- 失败路径必须且只能有一个首个 `FAIL`；
- 首个失败前全部为 `PASS`；
- 首个失败后全部为 `NOT_EXECUTED_PREREQUISITE_FAILED`；
- `PASS` / `FAIL` 的 `executed=true`；
- `NOT_EXECUTED_PREREQUISITE_FAILED` 的 `executed=false`；
- `PASS` 和未执行 phase 的 `failure_category=NONE`；
- `FAIL` 的 `failure_category` 不能为 `NONE`；
- elapsed、timeout 和 byte count 必须为非负数；
- `started_at_monotonic_ref` 是非空 opaque reference，不得包含系统时间、地址或秘密。

实现不得自动重试、fallback、repair 或覆盖 `PhaseTrace`。

## Serialization and Retention Boundary

`PhaseTrace.to_dict()` 输出：

- `schema_version="0.1.0"`；
- ordered `events`；
- 只包含 Development contract 允许的字段。

JSON Schema 必须拒绝 additional properties、缺 phase、phase 乱序、重复 phase、负数计数、
非法 predecessor、多个 FAIL、FAIL 后继续执行、secret/raw-body/prompt/review-content
字段。

实现不写磁盘、不提供 store、不提供 TTL scheduler。Retention 由调用方治理，并在
README/AGENTS/Implementation Declaration 中固定：

```text
RETENTION_POLICY_IMPLEMENTED=false
CALLER_MUST_DECLARE_RETENTION=true
IMMUTABLE_RECORD_DOES_NOT_MEAN_PERMANENT_STORAGE=true
```

## Exact Tests

`tests/test_instrumentation_contract.py` 至少覆盖：

1. 完整成功 trace；
2. P0–P9 每个 phase 作为首个失败的 10 个参数化用例；
3. deterministic serialization；
4. `schema_version`；
5. predecessor 和 phase order；
6. frozen/immutable behavior；
7. `validate_phase_trace` 正负路径。

`tests/test_negative_boundaries.py` 必须执行 PRE-43 的 10 个负例：

1. network access 不存在；
2. credential/Authorization 字段不可表达；
3. provider-neutral core 不依赖 Provider SDK；
4. 不导入 DBOS Runtime 或 SAEE；
5. Observation 不声明 Evidence/Truth；
6. Schema pass 不声明 provider correctness/conformance；
7. retry/fallback/repair 不能改写首个失败；
8. raw payload/prompt/review content/hidden reasoning 不可持久化；
9. 不声明 provider support/production readiness；
10. contract type 不授予 Permission/Authorization/Execution。

测试只能使用 Python standard library `unittest`。冻结命令：

```text
TEST_COMMAND=PYTHONPATH=src python3 -m unittest discover -s tests -v
BUILD_COMMAND=python3 -m build --no-isolation
NETWORK_DURING_TESTS=0
```

若环境没有已经可用的 `build` 模块，build 记录为 `NOT_EXECUTED_DEPENDENCY_UNAVAILABLE`，
不得联网安装依赖；测试仍必须执行。

## Truth-surface Updates

若实现与测试实际通过，六个 truth surface 只能更新为：

```text
MATURITY=Development
PACKAGE_CREATED=true
SOURCE_FILES=2
TEST_FILES=2
IMPLEMENTATION_CREATED=true
PROVIDER_BINDINGS=0
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
RUNTIME_CREATED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_AVAILABILITY=NOT_CLAIMED
```

`IMPLEMENTATION-DECLARATION.v0.1.json` 必须引用 exact source/test digests、Development
specification hash 和 Decision commit，并明确 unsupported/unknown 状态。

## Validation and Result

实现后必须：

1. 验证 target HEAD 与所有 precondition digest；
2. 执行 exact tests；
3. 扫描 source/test 是否出现网络、Provider、DBOS/SAEE Runtime、secret/raw content API；
4. 验证 `TITMAS-INTEGRATIONS-ENTRY.v0.1.json` 及 Implementation Declaration；
5. 执行 build 或记录 fail-closed not-executed；
6. 比对 exact 14-path fileset；
7. 提交到 `codex/rb0-governance-baseline`，不触碰 `main`；
8. 从远端做 clean-clone test；
9. 在 DBA 保存 result、receipt 和 target commit。

任何 test、Schema、inventory、truth surface 或 clean-clone failure 都保留目标分支和失败
记录，并停止，不形成 conformance、release 或 provider claim。

## Rollback

Rollback anchor：

```text
TARGET_PARENT=f80629364752c465316b9d1238fe5447a88565ca
ROLLBACK_MEANING=RESTORE_EXACT_RB0_DEVELOPMENT_BASELINE
FORCE_PUSH_ALLOWED=false
MAIN_BRANCH_WRITE_ALLOWED=false
```

回滚只能通过后继提交删除 8 个新增文件并恢复 6 个更新文件，不能重写历史。

## Non-effects

```text
RECOMMENDATION_IS_IMPLEMENTATION=false
TARGET_WRITE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
PROVIDER_BINDING_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
DBOS_CHANGED=false
SAEE_CHANGED=false
AGENT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_TRUTH_CHANGED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```

## Stop Conditions

目标 commit、14-path fileset、public API、P0–P9 rules、test/Schema/retention boundary、
rollback 或 truth-surface update 漂移；需要网络、外部依赖安装、Provider binding、
DBOS/SAEE change、Agent/Runtime、Permission、main merge、PR、tag、release、deployment、
certification 或 commercial claim 时立即 fail closed。

## Standing Directive Assessment

该建议只有一个 exact option，固定 repository/branch/commit、14 paths、6 public symbols、
0 runtime dependencies、P0–P9 invariants、两类 tests、rollback、truth surface、non-effects
和 stop rules，满足 `TITMAS-CS-STANDING-001` 候选条件。

本文件只是 Recommendation。目标写入和实现开始前仍须独立 PRE-48 Decision Record。
