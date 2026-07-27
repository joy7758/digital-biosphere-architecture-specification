# Trusted Multi-Agent Infrastructure Developer Preview v0.1

本仓库是 Digital Biosphere Architecture（数字生物圈架构，DBA）的 GitHub
入口。DBA 负责 `Trusted Multi-Agent Infrastructure`（可信多智能体基础设施）的
Program Governance（项目群治理）、Architecture Specification（架构规范）和
Release Governance（发布治理）；它不是 Runtime（运行时），不替代 DBOS 或 SAEE。

当前版本尚未正式发布。请从以下入口开始：

- [项目公开总览](digital-biosphere-architecture/PUBLIC-PROJECT-OVERVIEW.md)
- [DBA 驾驶舱与架构规范](digital-biosphere-architecture/README.md)
- [Developer Preview 计划](digital-biosphere-architecture/DEVELOPER-PREVIEW-PLAN.md)
- [Clean Clone 验证报告](digital-biosphere-architecture/CLEAN-CLONE-VALIDATION-REPORT.md)

当前 Commercial Evaluation（商业评估）集成闸门已完成不可变候选 merge-tree 验证：

- exact `qwen3.7-max` 对 v0.2 授权决策：`APPROVE`，0 blocker，0 correction；
- candidate `c608fd78…` + canonical `ccf473f3…` 的 merge tree `bd67298e…` 完成完整验证；
- 1165/1165 tracked JSON、23/23 dependencies、16/16 site tests、3/3 CE Schemas、49/49 CE tests 均通过；
- replacement Draft PR Recommendation 已由 exact `qwen3.7-max` 推荐 Option A；PR Creation Decision 仍待建立；
- 未授权创建或修改 PR、merge、release、deployment 或服务器操作。

[查看 CE-G11B 验证报告](digital-biosphere-architecture/TITMAS-CE-G11B-IMMUTABLE-CANDIDATE-MERGE-TREE-VALIDATION-REPORT-v0.1.md)

```text
DEVELOPER_PREVIEW_RELEASED=false
EXTERNAL_DEVELOPER_VALIDATION_COMPLETE=false
CE_G11B_VALIDATION_AUTHORIZATION_APPROVED=true
CE_G11B_VALIDATION_EXECUTED=true
CE_G11B_VALIDATION_PASS=true
PRODUCTION_READY=false
```
