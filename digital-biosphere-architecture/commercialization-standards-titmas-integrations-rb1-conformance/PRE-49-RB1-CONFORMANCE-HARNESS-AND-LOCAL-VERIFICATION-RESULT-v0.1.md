# PRE-49 RB1 Conformance Harness and Local Verification Result v0.1

## Result

```text
PRE49_RESULT=PASS_LOCAL_REFERENCE_CONTRACT_REHEARSAL_REMOTE_CLEAN_CLONE_VERIFIED
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_PARENT=001da006aa32a1eeeb058daa31dcab39197fa4de
TARGET_COMMIT=5ac891c5af88b1e9aeacdb3666217c6f832a57a6
TARGET_MAIN_UNCHANGED=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
AUTHORIZED_PATHS=24/24
UNIT_TESTS=30/30
FROZEN_CASES=7/7
MACHINE_SCHEMA_PAIRS=5/5
FIXTURE_DIGESTS=7/7
DECLARED_ARTIFACT_DIGESTS=11/11
OFFLINE_BUILD_LOCAL=PASS_NOT_PUBLISHED
OFFLINE_BUILD_CLEAN_CLONE=PASS_NOT_PUBLISHED
REPRODUCIBLE_BUILD_PROVEN=false
PROVIDER_CONFORMANCE_EXECUTED=false
THIRD_PARTY_INDEPENDENT_CONFORMANCE=false
RELEASE_AUTHORIZED=false
```

PRE-49 在 `CS-D02-PRE-49` 的精确 Decision 下执行。目标非默认分支新增 16 个文件、
更新 8 个文件；没有修改授权文件集外的路径。目标 `main` 保持不变，没有创建 PR、
merge、tag、release、deployment、Provider binding 或网络请求。

## Conformance Boundary

目标仓库现在包含一个独立代码路径的本地 contract rehearsal：

- validator 只消费 serialized P0–P9 phase trace；
- validator 不导入 target implementation、DBOS、SAEE、Provider SDK 或网络模块；
- 3 个正向 fixture 和 4 个负向 fixture 由 manifest SHA-256 冻结；
- manifest path escape、digest drift、duplicate case、未知 expected result 和 validator
  exception 均 fail closed；
- PASS 只表示本地 Development reference contract rehearsal 符合冻结预期。

这里的 `independent-path` 不是第三方独立审查、认证、Provider conformance、production
readiness 或 customer proof。

## Validation

| check | result |
|---|---|
| exact fileset | `24/24 PASS` |
| final local unit and boundary tests | `30/30 PASS` |
| frozen fixture rehearsal | `7/7 expected results matched` |
| machine instances and Schema | `5/5 PASS` |
| fixture digests | `7/7 PASS` |
| declaration artifact digests | `11/11 PASS` |
| validator runtime dependencies | `0` |
| validator target/provider/network imports | `0` |
| remote branch equality | local and remote both `5ac891c…` |
| remote clean clone | tests, rehearsal, Schema and digests `PASS` |
| target default branch | unchanged at `e8eeccbf…` |

## Retained Failure

第一次完整测试为 `29/30 PASS`。失败项
`test_manifest_digest_drift_fails_closed` 使用指向仓库 fixture 的 symlink 作为临时测试
输入，触发了 validator 的 path-escape guard。该 guard 行为正确；修正仅把测试隔离方式
改为复制到临时目录，没有修改 validator 阈值、fixture 或 expected result。最终测试为
`30/30 PASS`。

## Build Observation

两次 build 均严格使用：

```text
uv build --offline --out-dir <fresh-temporary-directory>
```

本地工作树 build：

```text
sdist_sha256=4cf69c13015b44e21a7021225f54a200cd93e5092dfc18e78fe7f8f978edf696
wheel_sha256=9bfc8525001956135e54124c7e642c29081701108267c24ece6e0db66653a6c2
```

远端 clean-clone build：

```text
sdist_sha256=4fb8ecab03b187c480c04532be34c9e5da98dddcd19301138cdc7245f4ba4a2b
wheel_sha256=57246315b9b2afc3903a5cf5f526ad122f8a18275597e81f86593e3a6110b862
```

两次均成功但产物 hash 不同，因此只能证明 offline build smoke 通过，不能证明
reproducible build（可复现构建）。构建生成的
`src/titmas_integrations.egg-info/` 已从两个验证工作树移除；产物只保留在临时目录，
未复制到仓库、未发布。Setuptools 的 license metadata deprecation warning 已保留为
后续 packaging gate 输入；PRE-49 未授权修改 `pyproject.toml`。

## Non-effects

```text
LOCAL_REFERENCE_CONTRACT_REHEARSAL=PASS
INDEPENDENT_PATH_VALIDATOR=true
THIRD_PARTY_INDEPENDENT_CONFORMANCE=false
PROVIDER_CONFORMANCE_EXECUTED=false
PROVIDER_SUPPORTED=false
PROVIDER_CORRECTNESS_PROVEN=false
REPRODUCIBLE_BUILD_PROVEN=false
SECURITY_REVIEW_EXECUTED=false
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

## Next Gate

```text
NEXT_ACTION=FORM_SEPARATE_RB1_PROVIDER_BINDING_SCOPE_AND_SECURITY_REVIEW_RECOMMENDATION
NEXT_ACTION_IS_PROVIDER_BINDING_IMPLEMENTATION=false
NEXT_ACTION_IS_PROVIDER_CONFORMANCE=false
NEXT_ACTION_IS_RELEASE=false
```

PRE-49 PASS 只解除本地 contract rehearsal 缺口。下一步应先定义单一 Provider
候选、credential boundary、network boundary、timeout/error taxonomy、sanitization、
security review、Provider-specific negative cases 和停止条件，再形成独立 Decision。
