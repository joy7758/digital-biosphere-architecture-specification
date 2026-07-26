# TITMAS CS-D02 PRE-49 RB1 Conformance Harness and Local Verification Decision Record

```text
DECISION_ID=CS-D02-PRE-49
DECISION_RESULT=AUTHORIZE_EXACT_RB1_INDEPENDENT_PATH_CONFORMANCE_HARNESS_AND_LOCAL_CONTRACT_REHEARSAL
DECIDED_BY_REF=zhangbin
DECIDED_AT=2026-07-27T05:58:16+08:00
STANDING_DIRECTIVE=TITMAS-CS-STANDING-001
RECOMMENDATION_COMMIT=6542d6b6c896edb9d1306cd3877a1c6b8920875b
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_PARENT=001da006aa32a1eeeb058daa31dcab39197fa4de
NEW_FILES_MAX=16
UPDATED_FILES_MAX=8
FIXTURES=7
NETWORK_REQUESTS_MAX=0
PROVIDER_BINDINGS_MAX=0
MAIN_BRANCH_WRITE=false
```

本决定采纳
[`TITMAS-CS-D02-PRE-49-RB1-CONFORMANCE-HARNESS-AND-LOCAL-VERIFICATION-RECOMMENDATION-v0.1.md`](TITMAS-CS-D02-PRE-49-RB1-CONFORMANCE-HARNESS-AND-LOCAL-VERIFICATION-RECOMMENDATION-v0.1.md)
中的唯一精确选项。

授权仅包括：

1. 在目标 Development 分支新增 16 个、更新 8 个冻结路径；
2. 建立不导入 target implementation 的 standard-library serialized-trace validator；
3. 建立 3 个 PASS 和 4 个 FAIL 的版本绑定 fixture corpus；
4. 运行本地 unit tests、manifest rehearsal、Schema、hash 和 source-boundary checks；
5. 只允许用 `uv build --offline` 在新临时目录进行 build smoke；
6. 路径限定提交、推送非默认分支并执行远端 clean-clone 验证；
7. 在 DBA 记录结果、失败、target commit 和后续 gate。

本决定中的 `independent-path` 只表示验证器代码路径与 target implementation 分离，
不表示第三方独立机构、认证、Provider conformance 或标准组织认可。

不授权联网安装、Provider binding、DBOS/SAEE 变更、Agent、Runtime、Evidence、
Permission、`main` 写入、merge、PR、tag、release、deployment、Certification 或
Commercial Offering。

任何 target commit、24-path fileset、fixture、public API、validator independence、
offline build、result class、truth surface 或 rollback 漂移均 fail closed。失败必须保留，
不能用 fixture repair、阈值降低或权限扩大方式修正。
