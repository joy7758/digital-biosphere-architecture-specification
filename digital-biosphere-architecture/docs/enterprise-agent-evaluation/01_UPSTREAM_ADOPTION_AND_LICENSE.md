# 上游采用与许可证矩阵

核验日期：`2026-08-19`。GitHub 项目通过 Codex GitHub 插件只读核验；商业平台只核验官方网页和官方文档。公开可见不等于允许复制，本文件也不是法律意见。

## 冻结矩阵

| 对象 | 官方来源与固定点 | 许可证 | 解决的问题 | 与 TITMAS 重叠 | 独特能力 | 引入/维护成本与数据影响 | 退出方式 | 决策 |
|---|---|---|---|---|---|---|---|---|
| AgentFit | [RecruitBase/agentfit](https://github.com/RecruitBase/agentfit)，`main@83df008272e4d2a29bb2b36ff5a1356e60c86609`，README 标示 v0.3.0 | BUSL-1.1；变更日 2030-07-30，之后 Apache-2.0。当前不是开源许可证 | 以 Business Need Profile、权重、阈值、硬门、重复试验和解释性报告判断业务适配度 | 企业要求、权重、通过/失败、推荐解释 | BNP 形式和治理式二元决定 | 若安装会引入 Python/模型/适配器和 BUSL 传播/分发审查；可能处理评测数据；版本与许可证维护成本高 | 不安装、不复制代码；只保留独立 EEP 方法表达 | `REFERENCE_ONLY` |
| τ³-bench | [sierra-research/tau2-bench](https://github.com/sierra-research/tau2-bench)，`main@a2c024725189473d2d7cea3a5cfdbcc67478e41f`；README 标示 v1.0.1 评分更新 | MIT | 用政策、工具、任务、用户模拟和最终业务状态评价工具型客服智能体 | 场景、工具、任务、禁止动作、结果裁决 | 双控制交互、领域任务与状态式评价方法 | 整体安装会引入 Python 3.12、uv、模型密钥及可选语音/RAG 栈；数据量和维护面大 | 只用独立 ESP；未来适配器必须可移除且不改变 TITMAS 内部格式 | `PRIMARY_METHOD_REFERENCE / SELECTIVE_METHOD_ADOPTION` |
| Agent Control | [agentcontrol/agent-control](https://github.com/agentcontrol/agent-control)，`main@541f872e79b109524ed029db038118d3beb8b033`，release v8.5.0 | Apache-2.0 | 集中配置运行时控制，对输入输出执行可插拔安全检查 | 前后置门控、人工升级、决定记录 | 完整服务器、SDK、UI、PostgreSQL 与多框架控制包装 | 引入会产生第二服务、数据库、运行认证、策略和遥测维护面；会接触智能体输入输出 | 保留 `ControlProvider` 抽象，默认使用现有 TITMAS Gate；适配器可完全卸载 | `DEFERRED_OPTIONAL_COMPONENT` |
| Galileo | [官方产品页](https://galileo.ai/products)、[官方实验文档](https://docs.galileo.ai/sdk-api/experiments/experiments)，检索于 2026-08-19 | 商业专有服务；未作为开源依赖核验 | 离线/线上评测、可观察性、失败分析与实时防护 | 评测、监控、失败分析 | 成熟的端到端商业可观察与评价工作流 | 接入会产生供应商账户、SDK/服务依赖和数据外发审查 | 不接入核心；未来仅允许客户自选 OpenTelemetry Export | `COMPETITOR_AND_CAPABILITY_REFERENCE` |
| Wayfound | [官方网站](https://www.wayfound.ai/)、[官方 Supervisor 文档](https://docs.wayfound.ai/supervisor/overview)，检索于 2026-08-19 | 商业专有服务；未作为开源依赖核验 | 用业务目标、规则、评分卡、会话下钻和监督建议管理智能体 | 业务评分卡、问题摘要、持续监督 | 面向非技术业务负责人的监督表达和网络视图 | 接入会同步交互/会话并形成商业服务锁定；业务和隐私审查成本高 | 只借鉴信息架构和业务语言，不接服务、不复制界面 | `BUSINESS_UI_REFERENCE_ONLY` |
| Benchboard | [官方网站](https://www.benchboard.ai/)，检索于 2026-08-19 | 商业专有服务；未作为开源依赖核验 | 快速生成多轴综合分、审计页面、私有/公开结果和可选榜单 | 结果卡、红线、分享页面、重复评测 | 低门槛传播展示与公开/私有切换 | 接入会上传任务、答案和工件，并引入商业计费/排行榜语义 | 仅借鉴展示结构；不接接口、不采用固定权重和徽章 | `PRESENTATION_REFERENCE_ONLY` |

## 许可证与采用结论

1. AgentFit 的 BUSL-1.1 是代码复用阻断，不是方法参照阻断；TITMAS 必须独立设计 EEP，不复制其七维实现、提示词或代码。
2. τ³-bench 的 MIT 允许依法复用，但 R0 只吸收公开方法，不复制完整内部格式或数据；因此当前无新增许可证文件义务。
3. Agent Control 的 Apache-2.0 不是主要阻断，架构重复和运维成本才是延后原因。
4. Galileo、Wayfound、Benchboard 均按商业专有平台处理；“官网可读”不构成代码、界面或评分数据复制许可。
5. R0 新增运行依赖、数据库、外部服务和供应商适配器均为 `0`。

## 供应链冻结

上游提交只用于形成可审计研究快照。后续版本变化不会自动修改 TITMAS 决策；任何代码引入、服务接入或许可证状态变更都必须重新进行来源、许可证、数据和退出审查，并经过 Human Gate。
