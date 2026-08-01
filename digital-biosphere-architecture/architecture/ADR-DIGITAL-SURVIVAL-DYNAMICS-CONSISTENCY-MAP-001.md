---
document_id: ADR-DIGITAL-SURVIVAL-DYNAMICS-CONSISTENCY-MAP-001
title: Digital Survival Dynamics v0.2 Consistency Mapping
title_zh: 数字生存动力学 v0.2 一致性映射
status: framework-only-mapping
primary_repository: digital-biosphere-architecture
document_type: cross-adr-mapping
implementation_authorized: false
schema_authorized: false
runtime_authorized: false
external_action_authorized: false
release_authorized: false
---

# ADR-DIGITAL-SURVIVAL-DYNAMICS-CONSISTENCY-MAP-001

## 1. Purpose（目的）

本文件给出当前 Selection Dynamics / Digital Ecology 体系从 v0.1 到 v0.2 的一致性映射（consistency mapping），用于后续文档联动和术语统一。  
文件仅用于架构一致性对齐，不定义实现、不新增功能，不变更代码。

## 2. Core Thesis Alignment（核心命题对齐）

| v0.1 命题 | v0.2 对齐命题 | 映射结论 |
|---|---|---|
| `How does an agent select actions/targets?` | `How do autonomous digital ecosystems survive, adapt, and evolve under changing environments?` | 从“单代理决策正确性”升级为“系统长期生存研究”。Selection 仅是子机制。 |
| 选择正确性与决策质量优先 | 生存稳定性与长期韧性优先（性能是其中一个子指标） | 目标层次上调，选择指标不再为唯一目标。 |
| 经验性推荐导向 | 观察驱动与证据先于结论 | 实验输出默认是 advisory evidence，不是治理命令。 |
| 候选排序即权威 | 排序为解释证据的一部分（非 trust/非权限） | 保持禁区：`score != trust`, `selection != authorization`。 |

## 3. Document Layer Mapping（文档层映射）

| 现有文档 | 作用 | v0.2 语义位置 | 一致性说明 |
|---|---|---|---|
| `ADR-DIGITAL-BIOSPHERE-LABORATORY-CHARTER-002` | DBA/DBL 顶层理论重定位 | v0.2 总入口 | 明确将研究焦点从“Agent选择”转为“数字生存动力学”。 |
| `ADR-DIGITAL-SURVIVAL-DYNAMICS-THEORY-001` | 理论最高层 | 研究根框架 | 建立父理论、指标、实验原则、边界禁区。 |
| `ADR-DIGITAL-SURVIVAL-DYNAMICS-001` | DSD 架构 ADR | v0.2 方法化分解 | 定义 Selection、Adaptation、Balance、Diversity、Resilience。 |
| `ADR-TITMAS-SELECTION-DYNAMICS-FREEZE-001` | Selection Dynamics 冻结 | v0.2 子系统定位 | 确认 SD 为子系统并锁定非目标（非授权、非政策权威）。 |
| `SPEC-DIGITAL-ECOLOGY-BOX-v0.2` | 最小实验单元规范 | v0.2 实验执行边界（非实现） | 将 DEB-001 试验设计固定为可复现实验结构。 |

## 4. Concept Mapping（核心概念映射）

| v0.1 概念 | v0.2 对应概念 | 迁移规则 | 保留约束 |
|---|---|---|---|
| Selection Pressure Engine | 选择压力机制（Selection 分支） | 作为 SD 子机制保留 | 输出仍为建议性解释，不授权。 |
| AgentRank | 解释性候选排序机制 | 留作 SD 排名机制 | `AgentRank != trust`。 |
| 决策证据链（Decision Evidence） | 选择建议证据（Decision Evidence） | 归入 Evidence Layer，强调 provenance 和 failure semantics | 不等于 Execution/Permission。 |
| Conformance | Selection Dynamics Conformance | 保持 Level 0/1/2/3 验证语义的技术职责 | 不与执行治理混淆。 |
| Certification | 合规声明（建议性） | 保留只对实现/规范兼容性作声明 | 不表示安全保证。 |
| Registry | 规范与实现目录索引 | 保持 metadata index 角色 | Registry 无授权能力。 |
| DBL（旧） | DBL 理论实验层 | 对齐至生态生存研究载体 | 不生产 runtime。 |
| 目标选择正确性 | 生存相关选择机制 | 从“最终目标”转为“指标子组件” | 需联合 Adaptation/Balance/Diversity/Resilience 评估。 |

## 5. Boundary Invariants（边界不变量）

下列不变量为 v0.2 冻结一致性前提，所有文档应保持全文一致：

```text
selection != authorization
score != trust
evidence != permission
recommendation != command
selection_dynamics != survival_theory
selection_output != policy_decision
```

## 6. Responsibility Decomposition（职责分解一致性）

### 6.1 v0.1 传统定位

- 主体关注：解释和提升选择过程；
- 扩展路径：Selection Engine / Evidence / Conformance / Certification。

### 6.2 v0.2 映射后定位

- **Digital Survival Dynamics（父理论）**：确定研究问题、指标和实验路线；
- **Selection Dynamics（子系统）**：提供可复核的选择机制与候选排序证据；
- **Evidence/TITMAS/SAEE/Registry**：在各自边界内消费/映射/验证，不接管执行。

## 7. Migration Rules（迁移规则）

1. 每个新文档在 `Purpose`/`Scope` 中必须明确：是 `DSD` 还是 `SD` 责任。  
2. 每个与 SD 相关的文档在 `Terminology` 中必须声明 `score != trust`。  
3. 所有 Decision/Recommendation 表达必须补充 `advisory only` 与 `no execution effect`。  
4. Registry、VEC、EEOAP、SAEE、TITMAS 引用必须以交接边界语义出现，不得混淆为授权链。  
5. 若遇冲突，优先读取：
   - `ADR-DIGITAL-SURVIVAL-DYNAMICS-THEORY-001`
   - `ADR-TITMAS-SELECTION-DYNAMICS-FREEZE-001`
   - `ADR-DIGITAL-SURVIVAL-DYNAMICS-001`

## 8. Consistency Check Template（对照清单）

- [ ] 术语是否从“选择正确性”转为“生存稳定性”？
- [ ] 是否明确 SD 不是生存理论总目标？
- [ ] 是否声明了 selection/evidence 的 advisory-only 边界？
- [ ] 是否有 failure semantics（unknown/partial/conflicted/hold/rejected）？
- [ ] 是否避免把 evidence、score、recommendation 与 authorization/permission/command 混用？
- [ ] 是否给 Registry、TITMAS、SAEE 的交接添加边界字段（scope/provenance/state）？
- [ ] 是否说明可复现与可重放条件？

## 9. Frozen Outcome（冻结结论）

映射后的体系采用如下固定关系：

```text
Digital Survival Dynamics
  -> Selection Dynamics (subsystem, frozen as advisory mechanism)
  -> Evidence Architecture / Conformance / Registry / Certification (downstream interoperability & verification)
```

因此，所有后续 Selection Dynamics 相关变更都应先通过上述映射关系与不变量进行一致性检查。
