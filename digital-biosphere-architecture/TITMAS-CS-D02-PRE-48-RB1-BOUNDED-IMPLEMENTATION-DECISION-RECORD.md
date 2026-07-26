# TITMAS CS-D02 PRE-48 RB1 Bounded Implementation Decision Record

```text
DECISION_ID=CS-D02-PRE-48
DECISION_RESULT=AUTHORIZE_EXACT_RB1_PROVIDER_NEUTRAL_PHASE_CONTRACT_REFERENCE_IMPLEMENTATION_AND_TESTS
DECIDED_BY_REF=zhangbin
DECIDED_AT=2026-07-27T05:33:21+08:00
STANDING_DIRECTIVE=TITMAS-CS-STANDING-001
RECOMMENDATION_COMMIT=323a95926107911e13501877bf3db07a3961efaf
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_PARENT=f80629364752c465316b9d1238fe5447a88565ca
NEW_FILES_MAX=8
UPDATED_FILES_MAX=6
SOURCE_FILES_MAX=2
TEST_FILES_MAX=2
NETWORK_CALLS_IN_IMPLEMENTATION_MAX=0
PROVIDER_BINDINGS_MAX=0
MAIN_BRANCH_WRITE=false
```

本决定采纳
[`TITMAS-CS-D02-PRE-48-RB1-BOUNDED-IMPLEMENTATION-RECOMMENDATION-v0.1.md`](TITMAS-CS-D02-PRE-48-RB1-BOUNDED-IMPLEMENTATION-RECOMMENDATION-v0.1.md)
中的唯一精确选项。

授权仅包括：

1. 在目标 Development 分支新增 8 个、更新 6 个冻结路径；
2. 实现无网络、无 Provider SDK、无 DBOS/SAEE Runtime 依赖的 P0–P9 数据契约；
3. 建立 standard-library 单元测试与 JSON Schema；
4. 更新目标仓库 Development truth surfaces；
5. 路径限定提交、推送该非默认分支并执行 clean-clone 验证；
6. 在 DBA 中记录结果、失败和 target commit。

不授权 Provider binding、外部依赖联网安装、Agent、Runtime、Evidence、Permission、
DBOS/SAEE 变更、`main` 写入、merge、PR、tag、release、deployment、Certification 或
Commercial Offering。

任何 fileset、API、P0–P9 invariant、测试、Schema、truth surface 或 rollback 漂移均
fail closed。测试或构建失败必须保留，不能用降低断言或扩大权限方式修复。
