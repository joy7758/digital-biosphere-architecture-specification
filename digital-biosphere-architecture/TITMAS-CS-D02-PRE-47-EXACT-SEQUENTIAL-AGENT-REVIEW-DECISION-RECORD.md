# TITMAS CS-D02 PRE-47 Exact Sequential Agent Review Decision Record

```text
DECISION_ID=CS-D02-PRE-47
DECISION_RESULT=AUTHORIZE_EXACT_FOUR_SESSION_SEQUENTIAL_QIANFAN_AGENT_REVIEW_WITH_FROZEN_PRE46_CONTRACT
DECIDED_BY_REF=zhangbin
DECIDED_AT=2026-07-27T05:16:39+08:00
STANDING_DIRECTIVE=TITMAS-CS-STANDING-001
RECOMMENDATION_COMMIT=09a8f4f88730bf3a9348ed99814690c17a44e907
REQUEST_MANIFEST_SHA256=c6af3cf2f6b7e4d57950271cc1ed028bad16b38db5016737035aa43ceef5c984
PLAN_SHA256=0c14371dbc0484b0a96b4ecd585d3568f58ca9d2b42b27144c3188fb3a16e6be
NETWORK_REQUESTS_MAX=4
CREDENTIAL_READS_MAX=1
PARALLEL_REQUESTS_MAX=1
RETRY_FALLBACK_SUBSTITUTION_ALIAS_REPAIR_MAX=0
TARGET_REPOSITORY_FILES_MODIFIED_MAX=0
```

该决定采纳
[`TITMAS-CS-D02-PRE-47-EXACT-SEQUENTIAL-AGENT-REVIEW-RECOMMENDATION-v0.1.md`](TITMAS-CS-D02-PRE-47-EXACT-SEQUENTIAL-AGENT-REVIEW-RECOMMENDATION-v0.1.md)
中的唯一精确选项。

授权范围仅包括：

1. 从本地环境读取一次 `QIANFAN_API_KEY`，不输出、不持久化；
2. 按冻结顺序向 exact Qianfan endpoint 发出最多四个请求；
3. 每次请求后先持久化并验证 sanitized success/failure result；
4. 使用冻结阈值计算 `PASS`、`FAIL` 或 `BLOCKED`；
5. 在 DBA 中保存四个 session results、一个 validation result、一个 execution
   receipt 和一个人类可读报告。

本决定不修改 PRE-44 历史，不授权 retry、fallback、model substitution、alias
inference、JSON repair、response-format 推断、目标仓库写入、RB1 implementation、
package、source、tests、provider support、conformance、Runtime、release、commercial
offering、certification、Authority、Permission 或 Evidence Truth。

即使审查通过，也只能形成独立 RB1 implementation recommendation；不能直接实现。
