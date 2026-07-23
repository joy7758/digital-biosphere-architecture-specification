# Trusted Multi-Agent Infrastructure

中文：**面向多智能体系统的可信基础设施**。

Digital Biosphere 是总项目；DBA、DBOS、SAEE 和未来 Digital Entities 是同一项目
中的不同责任域。我们不创建另一个 Agent Framework，而是解决智能体长期运行和协作后
的身份连续、执行追踪、证据准入、验证边界与长期评价问题。

> Infrastructure for long-running, collaborative, and verifiable digital entities.

[网站首页](https://redcrag.cn/)提供完整中英文说明和机器可读状态，不要求访问 GitHub
才能理解当前架构与验证阶段。

## 当前阶段：Technical Validation Pilot

第一个垂直切片已经完成设计，目标是验证以下链路是否能在不混淆权力和事实的情况下闭合：

```text
Microsoft AGT observation candidate
  → TITMAS mapping
  → EEOAP statement and profile validation
  → DBOS Evidence Admission
  → Evidence and Verification references
  → SAEE read-only evaluation
  → Validation Report
```

当前只是验证方案，不是已执行 Demo，也不是产品、社区或生态采用：

```text
TITMAS_TECHNICAL_VALIDATION_DESIGN_COMPLETE=true
TITMAS_PILOT_EXECUTION_AUTHORIZED=false
COMPLETE_VERTICAL_SLICE_EXECUTED=false
COMMUNITY_ESTABLISHED=false
PRODUCTION_READY=false
```

必须保持：

- `Observation != Evidence`
- `Evidence != Truth`
- `Evaluation != Authority`
- `Recommendation != Decision`
- `Decision != Execution`
- `DBOS != SAEE`

## 从这里开始

- [完整网站（中国大陆可直接访问）](https://redcrag.cn/)
- [Technical Validation Pilot Framework](digital-biosphere-architecture/architecture/titmas-technical-validation-pilot-framework-v0.1.md)
- [Adoption Validation Framework](digital-biosphere-architecture/architecture/titmas-adoption-validation-framework-v0.1.md)
- [Telemetry-to-Evidence Admission Contract](digital-biosphere-architecture/architecture/telemetry-to-evidence-admission-contract.md)
- [项目公开总览](digital-biosphere-architecture/PUBLIC-PROJECT-OVERVIEW.md)
- [DBA 驾驶舱与架构规范](digital-biosphere-architecture/README.md)
- [Developer Preview v0.1 发布说明](digital-biosphere-architecture/DEVELOPER-PREVIEW-v0.1-RELEASE-NOTES.md)
- [机器可读状态](https://redcrag.cn/status.json)
- [智能体入口](https://redcrag.cn/llms.txt)

## 当前发布事实

`Trusted Multi-Agent Infrastructure Developer Preview v0.1` 已发布。它仍是受限开发者
预览，不构成生产可用性、自动权限、客户采用、社区成立或 Pilot 执行证明。

```text
DEVELOPER_PREVIEW_RELEASED=true
DBOS_PUBLIC_SAFE_WHEEL_PUBLISHED=true
AGENT_CUSTOMER_VALIDATION_RERUN_RESULT=PASS
OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY
PRODUCTION_READY=false
```
