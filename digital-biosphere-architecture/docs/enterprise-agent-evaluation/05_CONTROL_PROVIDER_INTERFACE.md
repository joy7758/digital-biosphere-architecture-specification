# ControlProvider 控制提供器接口 v0.1

状态：`INTERFACE_ONLY`。本文件不创建服务器、数据库、运行时、权限或执行器。

## 1. 目的

`ControlProvider` 为评测过程描述前置检查、后置检查、人工批准请求和决定记录的可拔插边界。当前默认候选是 TITMAS 现有 Action Gate；Agent Control 仅为未来可选适配器。

同一次行动只能存在一条权威执行决定链。外部控制组件的结果可以成为输入，但不得创建第二套权威事实、证据或授权源。

## 2. 最小操作

```text
evaluate_pre_action(action_context) -> control_decision
evaluate_post_action(action_context, execution_reference) -> control_decision
request_human_approval(action_context, decision_reference) -> approval_request_reference
record_decision(control_decision) -> decision_record_reference
```

这些是语义操作，不是已实现的 API 或 endpoint。

## 3. 最小输入

`action_context` 至少绑定：

- `action_id`、`action_type` 和目标引用；
- 发起主体身份和版本；
- EEP/ESP、政策和任务引用及摘要；
- 请求参数摘要；
- 允许工具、禁止动作和审批规则；
- 证据要求与已有证据引用；
- 时间有效期、幂等键和关联标识；
- 当前评测模式：`NATIVE` 或 `STABILIZED`。

缺少关键绑定时必须失败关闭，不得由自由文本补齐事实。

## 4. 决定枚举

| 决定 | 语义 | 是否自动授权执行 |
|---|---|---|
| `ALLOW` | 当前控制链在绑定范围内允许继续 | 否；仍需独立执行层消费有效决定 |
| `DENY` | 明确拒绝 | 否 |
| `WARN` | 允许继续评估但保留警告 | 否 |
| `ESCALATE` | 要求人工决定 | 否 |
| `TRANSFORM` | 只建议使用明确记录的安全转换后重新评估 | 否 |
| `ERROR` | 控制提供器无法可靠决定 | 否，必须失败关闭 |

每个决定必须包含稳定 `reason_codes`、输入摘要、提供器/规则版本、有效期和证据引用。解释文本不能替代 reason code。

## 5. TITMAS Native Gate 映射

| Action Gate 决定 | ControlProvider 决定 | 备注 |
|---|---|---|
| `ALLOW` | `ALLOW` | 保留原决定引用、范围、有效期和一次性消费约束 |
| `BLOCK` | `DENY` | 不得被人工说明文字改写为允许 |
| `REQUIRE_APPROVAL` | `ESCALATE` | 只有绑定同一请求元组的有效人类批准可重新触发评估 |

Action Gate 当前没有 `WARN` 或 `TRANSFORM` 的规范等价物，适配器不得虚构。`ERROR` 用于运输、解析、版本或证据验证失败，并保持失败关闭。

## 6. Agent Control 可选适配器边界

未来只有在真实公开评测证明 TITMAS Native Gate 无法表达已观察控制需求，并经独立 Human Gate 后，才可实验 Agent Control Adapter。适配器必须：

1. 实现同一 `ControlProvider` 语义而不改变 EEP/ESP；
2. 把 Agent Control 结果映射为候选控制输入，不成为新的治理权威；
3. 不复制身份、政策、决定、证据或评测事实数据库；
4. 可完全移除，移除后历史决定引用仍可解释；
5. 显式记录服务器、SDK、规则和 evaluator 版本；
6. 接受 TITMAS Human Authority 的最终决定，不自我批准。

R0 不安装、不启动或配置 Agent Control、PostgreSQL、UI 或遥测。

## 7. 人工批准

`request_human_approval` 只创建请求，不产生批准。有效批准必须：

- 来自已认证且有对应角色的人类主体；
- 绑定动作、目标、参数摘要、政策版本和有效期；
- 可拒绝、撤销和过期；
- 不得覆盖篡改、缺失或无效证据；
- 不得把评价建议变成权限事实。

## 8. 记录、幂等和回放

`record_decision` 记录决定及其输入绑定，不执行动作。相同规范输入应得到可比较结果；政策、目标、版本、有效期或参数变化必须产生新决定。决定消费、执行回执和后置评估分别记录，禁止将一次决定重放到不同目标或不同版本。

## 9. 权力不等式

```text
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Verification != Authorization
ControlProvider discovery != Permission
External control output != TITMAS fact authority
```
