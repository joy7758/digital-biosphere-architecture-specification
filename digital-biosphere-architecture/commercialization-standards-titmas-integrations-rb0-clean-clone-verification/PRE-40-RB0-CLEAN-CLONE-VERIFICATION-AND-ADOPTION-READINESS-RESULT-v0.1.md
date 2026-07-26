# PRE-40 RB0 Clean-clone Verification and Adoption Readiness Result v0.1

## Result

```text
PRE40_RESULT=DEVELOPMENT_RB0_CLEAN_CLONE_VERIFICATION_PASS_ADOPTION_REVIEW_READY_NOT_ADOPTED
PRE40_DECISION_COMMIT=20c3bc70733c05bf1ed6988423a395b55a0118a3
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_COMMIT=9610748d4a72d81278df2bc296518a469ce2fd30
REMOTE_MAIN=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
FRESH_CLEAN_CLONE_EXECUTED=1
EXPECTED_FILES_MATCH=16
EXPECTED_DIGESTS_MATCH=16
EXPECTED_SIZES_MATCH=16
REGULAR_NON_EXECUTABLE_MODES_MATCH=16
SCHEMAS_META_VALID=2
INSTANCES_VALID=2
LOCAL_SCHEMA_REFERENCES_RESOLVED=2
PUBLIC_SAFE_FINDINGS=0
SOURCE_FILES=0
PACKAGE_METADATA_FILES=0
TEST_FILES=0
REPOSITORY_BASELINE_ADOPTED=false
TARGET_REPOSITORY_MODIFIED=false
```

## Verified boundary

Fresh clone 独立证明 exact branch commit 的 Development RB0 governance surface 可重复获取，
并且：

- exact Apache-2.0 bytes 匹配；
- human、agent、LLM、machine、security 和 ownership surface 一致；
- RB0 files 已应用到 branch，但没有 merge；
- baseline validated/adopted 在 gate 执行期间仍为 false；
- implementation、provider support、conformance、Runtime、Release 和 Commercial
  Availability 均未产生；
- `origin/main` 和原始本地 checkout 未改变。

## Known limitation

机器入口的 `repository.target_commit` 当前等于 PRE-38 application anchor
`d54bf17…`，而 clean-clone HEAD 是 `9610748…`。同一 commit 内无法安全嵌入自身尚未生成的
commit hash，因此这不是字节冲突；但字段名存在语义歧义。后继 adoption packet 必须明确：

1. 将该字段定义为 application anchor；或
2. 通过非自引用外部 attestation 表达 verified commit；或
3. 建立明确的新字段/Schema revision。

在该问题被后继 Decision 处理前，不把机器入口称为自包含 current-commit attestation。

## Next gate

PRE-40 只使 RB0 adoption review ready。下一步可以形成 PRE-41 exact Development RB0
adoption and synchronized truth-surface recommendation；不能直接进入 RB1、merge 或发布。
