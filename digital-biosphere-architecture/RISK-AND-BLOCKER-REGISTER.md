---
document_id: DBA-RISK-BLOCKER-REGISTER-0.1
title: Digital Biosphere Program Risk and Blocker Register v0.1
title_zh: 数字生物圈项目群风险与阻塞台账 v0.1
status: active-risk-register
as_of_date: 2026-07-22
risk_acceptance_authority_assigned: true
---

# Digital Biosphere Program Risk and Blocker Register v0.1（数字生物圈项目群风险与阻塞台账 v0.1）

## 1. Risk Scale（风险等级）

- `CRITICAL`：可能导致越权、历史破坏、错误发布或不可恢复状态；
- `HIGH`：阻塞核心项目群推进或使驾驶舱失真；
- `MEDIUM`：增加重复建设、漂移或维护成本；
- `LOW`：局部可恢复问题。

风险等级不自动产生停止、授权或风险接受决定。

## 2. Active Risks（当前风险）

| risk_id | level | 风险 | 当前证据 | 缓解措施 | Owner 状态 |
|---|---|---|---|---|---|
| `R-002` | `HIGH` | DBA 本地 Git root 是 `/Users/zhangbin/Documents/New project`，不是 DBA 目录；远端树保留额外目录层 | 2026-07-21 `git rev-parse --show-toplevel` 与已发布远端结构 | 处理 `DQ-002`；在决定前禁止历史重写、删除或 force push | `DECISION_REQUIRED` |
| `R-003` | `HIGH` | 核心项目没有经 DBA 确认的统一 canonical status source | DBOS、SAEE 有多个 README、status、manifest 和证据表面；Pilot 有独立 readiness 状态 | 处理 `DQ-003`，为每项目记录一个规范入口及冲突规则 | `DOMAIN_CONFIRMATION_REQUIRED` |
| `R-004` | `MEDIUM` | 核心项目工作树存在大量当前变化，静态快照容易过期或误读 | 2026-07-21 只读 Git observation | 驾驶舱只记录 commit、branch、时间和状态来源；dirty count 不作为成熟度 | `MITIGATED_BY_POLICY` |
| `R-005` | `HIGH` | DBOS ↔ SAEE 接口曾只有 Specification，容易被误写成已集成 | 2026-07-21 已完成同一 synthetic envelope 的 scoped local conformance；没有生产 Runtime、写回或真实 Evidence | 保留 `SCOPED_LOCAL` 限定；clean clone 与 source release 后再评审更高状态 | `LOCAL_MITIGATION_VALIDATED_NOT_RELEASED` |
| `R-006` | `MEDIUM` | Research Agent Pilot 没有发现 `origin`，且当前 `NOT_READY` | Pilot README、Git observation | 先完成 Human Review 和 source approval；远端决策独立处理 | `PILOT_OWNER_INPUT_REQUIRED` |
| `R-007` | `MEDIUM` | POP、ARO、Agent Evidence、Token Governor 与 DBOS/SAEE 存在潜在重复责任 | DBA project mapping 与本地候选发现 | 逐项目执行 Portfolio Admission 和 duplicate capability review | `REVIEW_REQUIRED` |
| `R-008` | `MEDIUM` | 静态驾驶舱可能把旧观察继续展示为当前事实 | 当前没有 refresh cadence 或只读 adapter | 每个快照必须带 `observed_at`；过期标记 `STALE`；处理 `DQ-007` | `POLICY_DEFINED_IMPLEMENTATION_PENDING` |
| `R-009` | `HIGH` | Program Governance 被误读为 DBOS/SAEE 执行或代码控制权 | 用户原始管理意图与现有 authority model 的语义张力 | 在 Charter、Program Governance Spec 和 AGENTS 中固定权力分离 | `MITIGATED_BY_SPECIFICATION` |
| `R-010` | `HIGH` | 当前 Program Governance Cockpit 与既有 DBA public meaning layer 可能形成双重 DBA 入口和规范漂移 | README canonicality、project mapping 与既有独立公开仓库 | 处理 `DQ-008`；决定单一前门、交叉引用、迁移或长期分工，决定前不得声称已完成 canonical reconciliation | `DECISION_REQUIRED` |
| `R-011` | `HIGH` | DBOS 当前文档演化与 `DBOS-EXP-0001` 冻结 identity evidence 的校验语义冲突 | Version-aware historical binding 已实现；旧 digest 未改写；34/34 validators 通过并对当前漂移发 warning | source 隔离与 clean-clone 回归后再决定是否正式关闭 | `LOCAL_MITIGATION_VALIDATED_NOT_RELEASED` |
| `R-012` | `MEDIUM` | DBOS 默认顶层测试曾发现 0 tests，开发者可能误读结果 | `tools/run_tests.py` 现在逐目录运行且零测试失败；`main@cd3f867` 为 334/334 tests；wheel 不再安装误导性的仓库测试命令 | 发布时区分源码测试入口与已安装 wheel 的 validation smoke，并保留分发负例 | `MITIGATED_REMOTE_MAIN_VALIDATED_NOT_RELEASED` |
| `R-014` | `HIGH` | 3–5 人小样本、个别正面反馈或试用 PASS 可能被过度解释为客户验证、市场采用或发布授权 | External Developer Trial Plan 明确样本仅验证 onboarding、理解、使用和问题相关性信号 | 预冻结成功阈值；保留失败；Trial Result、Customer Validation、Release、Adoption 分开；发布仍需 `DQ-009` | `MITIGATED_BY_PLAN_NOT_YET_TESTED` |
| `R-015` | `MEDIUM` | 站点构建依赖 advisory 会随数据库刷新；2026-07-22 clean clone 一度报告 1 moderate + 6 high，自动修复建议会错误降级 Next/Cloudflare/Wrangler | exact overrides 固定 `fast-uri 3.1.4`、`postcss 8.5.22`、`sharp 0.35.3`；clean `npm ci` 后 audit 0，build、11/11 tests、lint PASS；服务器仍不部署 Node.js | 保持 overrides 与 lock 对账；每次 clean clone 重跑 audit；禁止 `npm audit fix --force`；上游兼容版本出现后以独立 review 移除 overrides | `MITIGATED_EXACT_OVERRIDES_VALIDATED_RECHECK_EACH_BUILD` |
| `R-016` | `HIGH` | Agent API 模型的推荐或 `PASS` 被误写成真实客户采用、market fit（市场匹配）或发布授权 | `TMAI-ACV-20260721-001` 是 12 个受控、给定材料的模型会话，不含真实生产调用 | 固定 `Agent Recommendation ≠ Customer Adoption ≠ Release`；保留 Human `released_by_ref` | `MITIGATED_BY_PROTOCOL` |
| `R-017` | `MEDIUM` | 给定 URL 后的机器理解或元数据 description 命中被误写成 open-web discovery（开放网络自然发现） | `TMAI-OWD-20260722-001` 首轮 6 查询无命中；修复后 GitHub 完整新 description 已命中，但规范英文名、中文名和 4 个公开搜索仍无精确命中 | 保留 `OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY`；`ADR-022` 仅为 v0.1 接受该限制，后续继续复查 | `ACCEPTED_LIMITATION_FOR_V0_1_RECHECK_OPEN` |
| `R-018` | `HIGH` | DBOS 保持 private，使 AI agent 能理解 TMAI 但不能自主获取、运行或复用核心存在基础设施 | exact public-safe wheel 已作为 GitHub Release asset 公开并通过匿名 hash 和隔离安装复验 | 整仓继续 private；只使用有界包并保持 Runtime/Permission 非声明 | `MITIGATED_BY_PUBLIC_SAFE_WHEEL_RELEASE_DBOS_PRIVATE` |
| `R-019` | `HIGH` | 直接公开 DBOS 整仓会披露本机路径和未纳入发布的项目资产清单 | `main@cd3f867` 有 48 个跟踪文件包含 `/Users/...`；0 Gitleaks findings 不能消除该 metadata exposure（元数据暴露） | 禁止整仓公开；使用不含 registry/evidence/reports/paths 的 39-file public-safe wheel | `WHOLE_REPOSITORY_PUBLIC_FAIL_CLOSED` |
| `R-020` | `CRITICAL` | OpenTelemetry Trace/Metric/Log 或 Collector receipt 被直接升级为 DBOS Evidence、Verification 或 Truth | OTLP 明确允许 partial success、drop、retry 和 duplicate；sampling 也可能造成不完整 | 强制 Telemetry→Evidence admission、dedupe、provenance、delivery state 和独立 Verification Object | `MITIGATED_BY_SPECIFICATION_IMPLEMENTATION_PENDING` |
| `R-021` | `HIGH` | GenAI/MCP Semantic Conventions 仍为 Development 或缺少稳定 Schema URL，自动跟随上游会破坏长期合同 | 2026-07-22 `semantic-conventions-genai@2e994c6...` README 为 `Schema URL: TODO` | DQ-023 pinned mapping 已采纳；DQ-018 authorized offline subset 已 fail-closed 验证；升级与部署仍须独立审查 | `MITIGATED_IN_OFFLINE_SLICE_DEPLOYMENT_REVALIDATION_REQUIRED` |
| `R-022` | `HIGH` | Sampling、高基数、敏感 prompt/tool payload、queue overflow 或 Collector 故障导致证据链缺失、泄密或成本失控 | OTel 官方明确要求数据最小化、敏感属性处理、最小权限和资源保护 | evidence-critical 事件走非概率 DBOS 路径；默认关闭内容采集；限流、redaction、自观测和故障测试 | `PRODUCTION_CONTROLS_DEFINED_NOT_IMPLEMENTED` |
| `R-023` | `HIGH` | Production architecture、SLO targets 或模型推荐被误写成生产实现或 `PRODUCTION_READY` | 当前只有 DBA 规范；Collector、endpoint、真实 Pilot 和生产授权均不存在 | 固定 `PR-G0` 至 `PR-G7`、deployment-specific claim 和 `PRODUCTION_READY=false` | `MITIGATED_BY_GATE_BASELINE` |
| `R-024` | `HIGH` | DBOS/SAEE 本地 remote-tracking refs、远程 `main`、开发分支和发布制品来源被合并成一个“当前实现” | `PR-G1` 观察到 DBOS 本地 `main@0caa2c4` vs remote `main@cd3f867`；SAEE development `697ae208`、滞后本地 `origin/main@e503c221` 和另行检出的 remote public `main@2173c25` 是不同观察面 | 每次映射记录 exact remote commit、development observation、artifact source 和用途；禁止跨表面外推 | `MITIGATED_BY_EXPLICIT_SOURCE_LAYERS_REFRESH_REQUIRED` |
| `R-025` | `CRITICAL` | 单机 JSON、`fcntl`、atomic replace 或 SQLite reference pass 被误写成 production durability，导致跨 store 崩溃不一致或无法恢复 | DQ-018 SQLite reference 已通过 synthetic crash/backup/restore/rollback；仍无 canonical multi-node transaction、HA、PITR 或生产 RPO/RTO 证据 | `PR-G2A` 只审查 reference slice；DQ-019/PR-G2B 必须另选 backend/profile 并产生 HA/fencing/PITR/direct drill | `REFERENCE_HARDENED_PRODUCTION_DURABILITY_OPEN` |
| `R-026` | `HIGH` | 智能体、评审者或文档将“参考符合性首切片”误当成“最终生产产品”，然后要求提前合并 Collector、Evidence、SAEE、HA 或反向声称已生产就绪 | DQ-018 多轮 Agent Review 已实际出现该误读 | 强制分开 `NEXT_SLICE_RECOMMENDED` 与 `PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW`；保留拒绝历史；SQLite 标记 reference only；后续每个 gate 独立授权 | `MITIGATED_BY_SPLIT_RECOMMENDATION_RECHECK_REQUIRED_AT_PRODUCTION_GATE` |
| `R-027` | `CRITICAL` | Collector queue/WAL/broker 与 DBOS canonical store 混用，导致 transport loss 被写成 canonical durability 或一个失败域同时摧毁两层 | 尚无 Collector deployment，但常见“用一个存储简化”误用路径 | 强制 DSN/identity/network/volume/key/backup 隔离和 cross-wiring negative test；Collector 不继承 DBOS RPO | `CONTROL_DEFINED_NOT_IMPLEMENTED` |
| `R-028` | `HIGH` | 将 per-replica Collector WAL 误当跨 replica consensus log 或 `RPO=0`，隐藏 PVC/replica 永久丢失 | OpenTelemetry file storage 可恢复重启队列，但 disk/queue/retry 仍可丢数据 | 每 replica exclusive WAL；丢失 reconciliation；跨 failure-domain 持久需 `Q2_MESSAGE_QUEUE`；canonical RPO 由 DBOS store 单独证明 | `CONTROL_DEFINED_NOT_IMPLEMENTED` |
| `R-029` | `CRITICAL` | 加密签名、hardware attestation 或 Human Review 被误写成 event Truth、Permission 或 scientific validity | Evidence provenance 需更高保证，但保证范围容易外推 | `P0`–`P3` 只证明 source/material binding；Evidence/Verification/Truth/Authority 持续分离；签名负例与撤销测试 | `CONTROL_DEFINED_NOT_IMPLEMENTED` |
| `R-030` | `HIGH` | 已采纳 staged production sequence 被误写成后续阶段已授权、已实施或当前 production recommendation | `ADR-024` 只采纳顺序；production=false | DQ-018 只授权 exact foundation；`DQ-019`–`DQ-021=BLOCKED_INPUT`；每阶段独立决定，生产前重做 Agent/customer review | `MITIGATED_BY_STAGE_GATES` |
| `R-031` | `CRITICAL` | JSON Schema valid、CI green 或 manifest 自报 `PASS` 被误写成生产 gate 已关闭，且范围、digest、Owner、失败和未知项无法追溯 | 旧 Evidence Package 只有自由文本字段，不能机器强制 exact scope 和 fail-closed semantics | Production Gate Evidence Manifest schema + profile + immutable binding + blocking unknown/security/recovery + Human Decision 组合验证；manifest 自身 effects 恒为 false | `CONTROL_DEFINED_VALIDATOR_NOT_IMPLEMENTED` |
| `R-032` | `HIGH` | OTel/OTLP/SemConv/Collector 自动跟随 `latest`，未审查 wire/schema/behavior/security delta 就改变长期协议 | `DQ-022`–`DQ-025` 已采纳 exact versions/commits；未授权自动升级 | 每次上游更新重新执行 delta inventory、compatibility/security review 和独立 Human Version Decision；Runtime compatibility 另行直接测试 | `MITIGATED_BY_PINNED_REFERENCES_REVALIDATE_ON_CHANGE` |
| `R-033` | `CRITICAL` | `service.instance.id`、`gen_ai.agent.id`、trace/span/conversation ID、tool 或 evaluation telemetry 被提升为 DBOS Identity/Execution/Capability/Permission 或 SAEE/Governance Authority | OTel/GenAI 字段为资源、相关性、操作或评价材料；来源可能由 instrumentation/Collector 提供或伪造 | strict schema、independent context/digest 与 DQ-018 authority negatives 已实现；32/32 semantic authorized cases PASS，14 deployment cases blocked | `MITIGATED_IN_OFFLINE_SLICE_DEPLOYMENT_REVALIDATION_REQUIRED` |
| `R-034` | `CRITICAL` | synthetic、缺 case、错 digest、未授权 Decision 或自评 reviewer 的 semantic conformance result 被伪造成 `PASS`，再被 production manifest 或 gate 聚合器采信 | mapping/observation Schema 不能验证 46-case closure、47/47 coverage、implementation/environment binding 或独立审查；测试数量本身也不能关闭 gate | strict result-set Schema 要求 FROZEN、non-synthetic、46/46 PASS、47/47 coverage、exact digests、DQ-023/022/018（deployment gate 另需 DQ-020）、implemented validator 和 independent APPROVED review；23/23 结果负例拒绝；未来 validator 必须做 cross-document reconciliation；所有 result effects 恒 false | `CONTROL_DEFINED_VALIDATOR_NOT_IMPLEMENTED` |
| `R-035` | `CRITICAL` | 按输入动态获取 Schema、未验证 redirect/DNS/final host、poisoned cache、digest drift 或无 lineage transform 可形成 SSRF、供应链替换、不可重放字段变化或敏感数据泄漏 | OTel 允许 Schema URL fetch/redirect；TMAI 尚无 schema acquisition/cache/transform implementation；`DQ-024` 45-case contract 中 source/transform/data-governance cases 仍全为 `NOT_EXECUTED` | Runtime fetch 默认关闭；build/release exact allowlist、per-hop/DNS/private-range check、bounded parser、immutable URL/version/digest/format cache key、append-only transform lineage、tenant/purpose/retention binding；结果不能关闭 gate | `CONTROL_DEFINED_DQ_024_PENDING_VALIDATOR_NOT_IMPLEMENTED` |
| `R-036` | `CRITICAL` | Resource detector precedence、`OTEL_RESOURCE_ATTRIBUTES`、OTel Entity/`OTEL_ENTITIES` 或普通 digest 被提升为 DBOS Identity/Entity/Permission/Truth，或跨租户引用泄露数据存在性 | Resource Data Model 与 OTel Entity/Propagation 为 Development；environment、detector 和 Entity input 可伪造；普通 SHA-256 对低熵 payload 可被字典推断 | Resource precedence != trust authority；conflicting non-empty URL fail closed；Development Entity quarantine 无 direct promotion；现有 Candidate/Admission/Authorization/Registration path 必须重走；tenant-scoped opaque reference/HMAC policy、45-case Entity/data-governance/result negatives | `CONTROL_DEFINED_DQ_024_PENDING_VALIDATOR_NOT_IMPLEMENTED` |
| `R-037` | `CRITICAL` | Collector floating tag、可变 release tag、预构建发行版或未固定依赖被误当 immutable production source，导致组件、依赖或构建结果在未决策时漂移 | 官方 releases 仓库明确警告 release tags 可能因发布修复而变化；当前只有 exact commit/byte inventory 和拟议 OCB 版本，尚无 binary、image、SBOM、provenance、signature 或 reproducible-build 证据 | build 必须从 exact release/core/contrib commits 与已登记 byte digests解析；只编译 8 个组件和 2 个本地 providers；锁定 module graph，产出 SBOM/license/provenance/signature/vulnerability/reproducibility/component reconciliation；任何差异 fail closed | `CONTROL_DEFINED_DQ_025_PENDING_BUILD_AND_VALIDATOR_NOT_IMPLEMENTED` |
| `R-038` | `HIGH` | Alpha/Beta Collector component、Transform OTTL 错误或 health endpoint 被提升为成熟、正确处理、系统健康或生产信任 | candidate 中 health check 为 Alpha，多个 processors/extensions 为 Beta；Transform 官方说明可能产生 unsound transformation、identity conflict 和 orphaned telemetry；`error_mode=propagate` 也不能单独证明永久/瞬时错误分类正确 | Profiles 不编译；Alpha health 只作有界信号且不能单独驱动 readiness；Transform 需 malformed/config/runtime/poison-retry、authority mutation 和 lineage 负例；无法证明时从 untrusted ingress 移除并保持 `PR-G3` 关闭 | `CONTROL_DEFINED_DQ_025_PENDING_RUNTIME_CONFORMANCE` |
| `R-039` | `CRITICAL` | Collector internal metric/log 缺失、改名、stale、counter reset、mixed version 或共享失败路径被解释成“零失败／健康”，dashboard、health 或 hop-local `sent` 进而被用来关闭生产闸门 | Collector internal telemetry 的配置 schema、metric projection 和 log 格式存在稳定性边界；WAL、listener、config drift 与端到端交付还需要独立来源；当前没有 query/threshold/alert/route/runbook 或直接测量 | strict operational-evidence profile 强制 12 observation/6 SLI、OTLP↔Prometheus naming/stability、UNKNOWN/no-zero-fill、counter lifecycle split、独立 self-observation/blackbox/storage/drift、composite readiness、no-data alert 与 delivery reconciliation；45/45 negatives 通过但实现和测量仍阻塞 | `CONTROL_DEFINED_DQ_020_BLOCKED_NO_MEASUREMENT` |
| `R-040` | `CRITICAL` | 已记录 reference adoption、Git freeze、bounded implementation authorization 和未来 blanket wording 互相替代 | 六项 exact token、Authority 和效果已独立记录；DBA/DBOS remote receipts 已验证；未来版本、部署和外部资源仍没有 decision | registry 与 gate records 分开 recommendation、review、approval、execution；PR-G2A 保持未批准 | `MITIGATED_CURRENT_GATES_REMAIN_EXPLICIT` |
| `R-041` | `HIGH` | 公共 validation result / DTO 被未来 persistence adapter 当作 authority token，绕过 canonical revalidation | DQ-018 独立审查曾复现 forged accepted decision；SQLite store 已改为重新验证 normalized envelope，并增加负例 | PR-G2B 适配器合同必须规定 validation object 不是 capability/permission/authority token，并复用同一负例 | `MITIGATED_CURRENT_SLICE_RECHECK_REQUIRED_AT_PR_G2B` |
| `R-042` | `HIGH` | 周期 integrity scan 一次性 materialize 全部 admission records，使长期运行内存随记录量增长并形成可用性风险 | predecessor `fdda745c…` 一小时 run 峰值 RSS 192,724,992；`3a63161…` 改为 cursor streaming 并新增禁止 record-cursor `fetchall()` 的回归测试；同环境一小时峰值降至 38,223,872，59 次周期检查与最终检查均 PASS | 保留精确新旧 artifact；只关闭当前 macOS arm64 SQLite reference 路径；生产 backend 和其他平台必须重跑相同 failure/memory controls，不能外推为 SLO | `MITIGATED_REFERENCE_SLICE_CROSS_PLATFORM_REVALIDATION_REQUIRED` |
| `R-043` | `CRITICAL` | 外部 identity discovery、enterprise access authorization、telemetry、receipt、signature、attestation 或 audit log 被提升为 DBOS Identity／Capability／Permission、POP persona continuity、正确 Execution、Evidence、Verification 或 Truth | FINOS #346/#341、MCP EMA、ANS 与 Microsoft Toolkit 提供不同层次的参考信号；它们都没有授予 DBA 内部 authority 或证明 evidence sufficiency | 注册表固定 6 项 route 与 forbidden promotion；所有来源保持 `REFERENCE_ONLY_NOT_ADOPTED`；未来分别走 `DQ-006`、`DQ-021` 与既有 admission／human-decision gate | `CONTROL_DEFINED_REFERENCE_ONLY_NO_ADOPTION` |
| `R-044` | `HIGH` | 只检查异常、退出码、schema shape 或字段存在，会漏掉 final state、invariant、contract 与 authority effect 已错误但流程“成功”的 silent semantic failure | LogicHunter `arXiv:2607.06195v1` 报告其研究范围内的静默语义失败；该来源是预印本，当前项目也没有由此产生的直接缺陷证据 | 作为未来 `PR-G2`／`PR-G4` review input；要求 exact implementation 下的 final-state、invariant、contract、authority-effect assertions 和直接证据；当前不创建 validator 或 gate PASS | `REVIEW_INPUT_DEFINED_IMPLEMENTATION_AND_DIRECT_EVIDENCE_OPEN` |
| `R-045` | `CRITICAL` | 外部治理趋势把 SAEE 从 `EVOLUTION_INTELLIGENCE_LAYER` 推成 audit／compliance engine，Evidence 副线覆盖受控 SAEE／Agent Evidence 合并主线，并把 local digest、MCP、demo 或 marketplace review 提升为 proof、service 或商业验证 | 2026-07-23 简报提出 Evidence Governance 定义权、`SAEE Agent Compliance Engine`、Persona identity ownership、三个直接 PR 与 workshop 路线；现有规范事实仍为 Phase 0.5、Phase 1 未授权、OTLP／trusted conversion／identity／delegation 缺失、public MCP／marketplace／customer／production false | 固定 `MAINLINE_DRIFT_DETECTED`；保留三客户版本；Evidence 走既有 crosswalk／reuse／migration gate；OTLP 与 identity 只保留 conditional proposal；workshop 与 compliance claim 禁止；外部动作保持 Human gate | `CONTROL_DEFINED_MAINLINE_CORRECTION_REQUIRED_NO_IMPLEMENTATION` |

## 3. Active Blockers（当前阻塞）

| blocker_id | 阻塞事项 | 阻塞范围 | 解除条件 | 不阻塞 |
|---|---|---|---|---|
| `B-002` | DBA Git topology（Git 拓扑）未决定 | 独立仓库根、干净发布结构和后续自动化 | `DQ-002` 选择并执行单独授权的迁移方案 | 当前工作树内的非破坏性文档更新 |
| `B-003` | canonical status source 未确认 | 自动或周期性可信状态汇总 | DBOS、SAEE、Pilot 各自提供 source + freshness + conflict policy | 当前时间点只读 snapshot |
| `B-004` | Research Agent Human Review 与 approved source 不完整 | Prototype Authorization Review 和实验 | Pilot 自己的 readiness gate 达到可审查状态并获得人工决定 | Pilot 规范改进和 DBA 项目群规划 |
| `B-005` | 两个 DBA 语义表面未完成 canonical reconciliation | 对外唯一入口、规范优先级和自动检索路由 | `DQ-008` 形成决定并完成引用/迁移验证 | 当前仓库作为 Program Governance Cockpit 的工作树基线 |
| `B-013` | DBOS 已有离线 Telemetry admission reference ledger，但没有 OTLP intake、canonical production durability、部署 integration 与 SLO 自观测 | `PR-G2B/G2T/G2I/G2C`、`PR-G3`、`PR-G5` 和 bounded pilot | PR-G2A Human Review 后按 DQ-019/020/021 分阶段产生耐久性、部署、恢复和 SLO 直接证据 | 当前离线 slice 的维护与审查 |
| `B-014` | SAEE public main 只有 preview adapter；development OTel-style mapper 是 synthetic/experimental，缺 production version/timeout/conflict isolation | `PR-G4` 和端到端 production evaluation | 单独映射并验证 read-only transport、unsupported version、timeout、conflict、resource exhaustion 和 zero writeback | DBOS 首个 admission foundation slice |
| `B-015` | production persistence backend/distribution/topology/Owner 尚未选定，HA/PITR/RPO/RTO 无直接证据 | `DQ-019`、`PR-G2B`、`PR-G5A` 和真实长期数据 | DQ-018 实施证据 + 候选对比 + Human DQ-019 + 故障/恢复演练 | DQ-018 reference-conformance 审查 |
| `B-016` | Collector exact distribution reference 已由 `DQ-025` 采纳，但 `DQ-020` 仍 `BLOCKED_INPUT`；binary/image/SBOM/config/runtime、deployment repository/Owner、exact failure domains/LB/security/capacity、metric stability/naming/Resource/query/threshold/alert/route/runbook bindings 和直接测量均不存在 | `DQ-020`、`PR-G3`、OTLP listener/Collector staging | DQ-018/019/022–025 prerequisites/direct evidence + exact build/config/runtime/topology/operational bindings + 56/46/45/48 四套独立 case-level result + self-observation/blackbox/storage/drift/no-data/alert-delivery/delivery-reconciliation results + independent technical/security review + Owner/repository + `G3A`–`G3F` | offline architecture/profile/Schema/matrix/decision review；不授权 build、configuration、query、alert、listener、measurement、deployment 或 real traffic |
| `B-017` | Evidence admission 尚未授权，Identity Continuity、Data Governance、provenance assurance 和 Verification 无实施证据 | `DQ-021`、`PR-G2C/G2I`、`PR-G5B`、SAEE production input | DQ-018/020 证据 + exact Evidence policy/schema + Human DQ-021 + security/data-governance tests | Telemetry material 和 reference conformance |
| `B-018` | Schema/Resource/Entity 的 36 个 DQ-018 authorized offline cases 已通过，但 acquisition/cache/transform、真实 detector provenance 和 9 个 DQ-020 deployment cases 仍未执行 | `PR-G2T`、`PR-G3`、`PR-G5`、`PR-G6` | DQ-020 authorization + exact deployment source/policy/environment + 剩余 9 cases + 独立 review | 当前 36-case offline subset 与 DBA reference review |

## 4. Resolved Risk and Cleared Blockers（已解决风险与已解除阻塞）

| item_id | 原问题 | 解除证据 | 保留边界 |
|---|---|---|---|
| `R-001` | Program Authority 未指派 | `ADR-020` 指派 `zhangbin` 并记录复核、替代和权力边界 | 不产生运行、演化、账号或发布权；重大 release 时复核 |
| `R-013` | 三仓库没有冻结、可引用、可复验的最终远端 source commits | DBA `91928e3`、DBOS `0caa2c4`、SAEE `2173c25`；完整 Clean Clone、331 tests、34 validators、8 Adapter tests 和 19/19 blobs 通过 | 只关闭 source/clean-clone 风险；不产生外部验证或发布授权 |
| `B-001` | 没有已记录的 Program Owner / decision source | `DQ-001` / `ADR-020`，`decided_by_ref=zhangbin` | 每个执行、外部联系和发布动作仍遵循各自 gate |
| `B-007` | 三仓库 source commits 未冻结且跨仓库 Clean Clone 未通过 | `CLEAN-CLONE-VALIDATION-REPORT.md` 后继结果 `PASS` | DBOS 是 authenticated private clone；外部试用仍受 `B-008` 阻塞 |
| `B-008` | 缺少 3–5 名人类开发者或招募渠道 | `ADR-021` 采用 AI agent 为首要客户并完成 12/12 受控模型基线 | 人类试用没有执行、没有被改写成通过；未来仍可作为次级可用性研究 |
| `B-009` | Agent Customer Validation 基线的 exact invocation、composition、positive fit 和 simple-task negative control 未达阈值 | `TMAI-ACV-20260722-002` 用相同阈值复测：12/12 sessions、全部阈值通过；原 `001=CONDITIONAL` 保留 | 只解除 agent-readable packaging blocker；不产生 DBOS 公开、客户采用或发布授权 |
| `B-010` | DBOS 没有已发布的公开 package、API 或面向 AI agent 的受控可调用路径 | `ADR-022`、exact GitHub Release asset、匿名 SHA-256 和隔离安装复验 | 只解除有界 package 获取阻塞；没有公共 Runtime、托管 API、Permission 或整仓公开 |
| `B-011` | 规范名称与公开网络仍未命中 TMAI | `ADR-022` 为 Developer Preview v0.1 显式接受并继续披露 `PARTIAL_METADATA_ONLY` | 只解除 v0.1 发布阻塞；发现事实没有升级，索引刷新后仍需复查 |
| `B-012` | TMAP、OTel Profile 和 Production SLO 未映射到 DBOS/SAEE 当前实现 | `PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md`：remote source、development observation、supported/partial/missing、duplicate authority 和 exact slice 候选已记录；`PR-G1=PASS_READ_ONLY_MAPPING` | 只解除 mapping blocker；`B-013`、`B-014` 继续阻止实现符合性、Pilot 和生产声明 |
| `B-019` | production architecture baseline 和 DQ-018 起点尚未远端复验 | DBA predecessor 与 hardened successor packet 均有非循环 remote attestation；DBOS predecessor `5c52c1c…` / `aa6440e…` 及 hardened source `3a63161…` / receipt `bf1b3b6…` 均完成 remote clean clone | 只关闭 remote provenance blocker；不产生 PR-G2A approval 或 production authorization |

| blocker_id | 原阻塞 | 解除证据 | 保留边界 |
|---|---|---|---|
| `B-006` | 冻结 `README.md` digest 与当前文档漂移导致 validator 失败 | Version-aware historical binding；34/34 validators `PASS`；旧 digest 未改写 | 仅当前本地工作树解除；未发布、未做 clean clone |

## 5. Risk Handling Rules（风险处理规则）

1. 风险只能由显式人工决定接受、缓解、转移或关闭；
2. `MITIGATED_BY_SPECIFICATION` 不表示运行风险已消失；
3. 失败、冲突和未知必须保留历史；
4. 子项目风险事实由子项目维护，DBA 只引用与项目群相关的摘要；
5. `CRITICAL` 或 `HIGH` 风险涉及 destructive action（破坏性操作）、权限、发布或外部影响时必须停止并请求新授权；
6. blocker 解除必须引用直接证据，不能只因计划存在而关闭。

```text
TRACKED_RISKS=45
ACTIVE_RISKS=43
RESOLVED_RISKS=2
ACTIVE_BLOCKERS=10
BLOCKERS_CLEARED=8
LOCAL_BLOCKERS_CLEARED_NOT_RELEASED=1
RISKS_ACCEPTED=1
RISK_REGISTER_GRANTS_AUTHORITY=false
```
