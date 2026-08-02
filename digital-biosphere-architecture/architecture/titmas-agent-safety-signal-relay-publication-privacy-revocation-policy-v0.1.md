---
policy_id: TITMAS-AGENT-SAFETY-SIGNAL-RELAY-PUBLICATION-PRIVACY-REVOCATION-0.1
title: TITMAS Agent Safety Signal Relay Publication, Privacy, and Revocation Policy v0.1
title_zh: TITMAS 智能体安全信号中继发布门、隐私与撤回策略 v0.1
status: ACCEPTED_ARCHITECTURE_SPECIFICATION_P3
normative: true
implementation_status: NOT_IMPLEMENTED
public_signal_status: NOT_AUTHORIZED
primary_repository: digital-biosphere-architecture
decision_ref: ADR-040
---

# TITMAS 智能体安全信号中继发布门、隐私与撤回策略 v0.1

## 1. Purpose and authority boundary（目的与权力边界）

本策略定义但不实现提交、复现、发布、隐私、更新和撤回规则。它不授权任何公共信号、
服务、密钥、接收方动作或自动修复。

```text
SIGNAL_RECEIVED_NE_ACTION_AUTHORIZED=true
APPLICABILITY_NE_CONFIRMED_IMPACT=true
PUBLISHER_ASSURANCE_NE_GLOBAL_TRUST=true
EVIDENCE_REFERENCE_NE_TRUTH=true
CORRECTION_NE_HISTORY_DELETION=true
```

## 2. Gate state model（发布门状态模型）

```text
SUBMITTED
  -> REJECTED_INTAKE | HOLD_INTAKE | ADMITTED_AS_CASE
ADMITTED_AS_CASE
  -> REPRODUCTION_NOT_REQUESTED | REPRODUCTION_PENDING
REPRODUCTION_PENDING
  -> REPRODUCTION_FAILED | REPRODUCED_WITH_LIMITATIONS | INCONCLUSIVE
REPRODUCED_WITH_LIMITATIONS
  -> CANDIDATE_SIGNAL
CANDIDATE_SIGNAL
  -> PUBLICATION_REJECTED | HOLD_REVIEW | VALIDATED_BOUNDED
VALIDATED_BOUNDED
  -> ACTIVE only with separate publication authorization
```

在本轮授权下，最高允许的文档状态是规范定义；任何 signal instance 的最高状态仍为
`NOT_CREATED`。

## 3. Submission gate（提交门）

### 3.1 Required inputs

提交至少必须具有：

1. stable `case_id`、submitter ref 和 proof/assurance limitation；
2. 发生时间范围、观察列表和 `cause_status`；
3. 证据 material/reference + digest scope；
4. runtime/tool/permission/identity-binding 的最小环境摘要；
5. field-level disclosure classification、redaction record 和 collection/use authority；
6. known unknowns、conflicts、clock/sampling/partial limitations；
7. 明确不含 credential、secret、完整私有轨迹或未获准 raw payload。

### 3.2 Outcomes

| Outcome | Condition | Effect |
|---|---|---|
| `REJECTED_INTAKE` | secret/raw private trajectory、无授权、digest/refs 不可解释、恶意 executable payload | 不进入案例；保留最小拒绝 receipt |
| `HOLD_INTAKE` | identity/evidence/disclosure/conflict 未解决 | 不复现、不发布；等待有界输入 |
| `ADMITTED_AS_CASE` | 结构、最小化、引用和边界通过 | 仅成为 review case，不成为信号或 Truth |

提交者的名称、alias、模型声明或 LLM 叙述不能授予 binding、evidence admission 或发布权。

## 4. Independent reproduction gate（独立复现门）

### 4.1 Independence requirements

独立复现者必须与原 submitter/publisher 在 identity、执行上下文和 review role 上可区分；
共享模型输出、共享未审计脚本或同一未经隔离的数据副本不自动算独立。

必须记录：

- exact reproduction specification/version；
- isolated/synthetic environment manifest digest；
- positive、negative 和 unknown cases；
- expected vs observed outcome；
- evidence/verification receipt refs；
- conflicts、non-reproduction 和 limitations。

### 4.2 Outcomes

```text
REPRODUCED_WITH_LIMITATIONS
REPRODUCTION_FAILED
INCONCLUSIVE
```

`REPRODUCTION_FAILED` 和 `INCONCLUSIVE` 必须保留，不能删除或改写为 PASS。单一 LLM 模拟、
文本解释、schema validation 或原提交者重复运行，不满足独立复现门。

## 5. High-impact publication gate（高影响信号发布门）

高影响包括可能导致身份错绑、有副作用工具执行、权限扩大、数据泄露、财务/医疗/法律影响、
大范围供应链影响或跨租户传播的信号。

进入 `VALIDATED_BOUNDED` 前必须全部满足：

1. exact schema、content digest、version 和 signed envelope 可验证；
2. evidence admission/assurance 明示，Evidence Reference 不被写成 Truth；
3. 至少一项符合第 4 节的独立复现；
4. broken assumption、cause status/epistemic status、attack path、直接 beneficial capability 完整；
5. affected、exclusion 和 unknown conditions 均有类型化表达；
6. applicability 与 local validation 结果分离；
7. positive、negative、unknown 和 adversarial fixtures 计划通过独立 review；
8. `publisher_assurance`、key policy、expiry、correction/revocation route 完整；
9. privacy/redaction/data-retention review 通过；
10. 至少两个相互独立角色完成 domain review 与 security review；
11. human risk decision 存在，或达到 DBOS Evidence Admission 规定的高影响来源保证门；
12. 建议字段满足 non-executable constraint。

任何一项缺失：`HOLD_REVIEW` 或 `PUBLICATION_REJECTED`。仅凭 LLM 判断、模型 quorum、
popular vote、publisher reputation 或营销紧迫性不得绕过 gate。

在 `ASSR-OI-010` 关闭前，ARO audit receipt/reference 一律按 `UNVERIFIED_CONTEXT` 处理，
不得提高 assurance、替代 independent reproduction 或满足 high-impact publication gate。

即便达到 `VALIDATED_BOUNDED`，进入 `ACTIVE` 仍需独立 `PUBLIC_SIGNAL_AUTHORIZED=true`；
当前该授权为 false。

## 6. Publisher identity and assurance（发布者身份与保证）

发布者必须使用 stable identity ref、exact proof、approved policy/version 和 finite validity。
保证记录只描述：

- identity binding 是否可验证；
- exact bytes/signature 是否验证；
- key/policy/algorithm/version/time/revocation 结果；
- publisher role 和 allowed signal scope；
- unknowns、conflicts 和 limitations。

禁止：全局可信发布者分数、跨域 reputation 排名、publisher 自报即可信、将有效签名解释为
事件真实或建议获授权。

Publisher、independent reproducer、high-impact reviewer 和 emergency revocation role 应职责分离；
同一主体兼任时必须显式降级 assurance，不能伪装独立。

## 7. Recipient local trust boundary（接收方本地信任边界）

接收方必须独立检查：schema/version、content digest、publisher proof、expiry、lifecycle high-water
mark、local policy 和 context validity，并生成自己的 `recipient_local_trust_decision`。

```text
TRUST_FOR_LOCAL_VALIDATION
DO_NOT_TRUST
REQUIRES_LOCAL_REVIEW
NOT_DECIDED
```

Relay、Publisher、SAEE、网页和其他接收者反馈均不得写入该字段。收到、匹配或本地确认均不
自动授予 action permission；行动仍需接收方本地策略和必要的人类/资源 Owner 授权。

## 8. Field-level disclosure and redaction（字段级披露与脱敏）

### 8.1 Disclosure enforcement

以 P2 字段表的 `maximum_permitted_disclosure` 为上限：

| Level | Relay handling rule |
|---|---|
| `PUBLIC_DEFENSIVE` | 仍须去标识、移除 exploit-enabling 细节并通过 public-safe review |
| `RESTRICTED_VALIDATION` | 仅提供给经策略接受的 receiver/verifier；禁止 public index 内容复制 |
| `PRIVATE_EVIDENCE` | Relay 只保存受控 reference/digest/assurance；原始材料留在 Evidence Owner |
| `LOCAL_ONLY` | Relay 不得接收、存储、记录摘要或在日志中回显 |

### 8.2 Mandatory redaction

必须删除或本地化：credential/token/private key、exact private endpoint、完整 permission scopes、
原始 prompt/trajectory、未获准 PII、客户数据、可直接武器化 exploit steps、内部资产拓扑和
不必要的精确 tool inventory。

Redaction 必须形成记录：字段、原分类、处理方式、reason、actor、time、policy version 和
是否影响结论。脱敏不能静默改变 evidence digest scope。

## 9. Local-first private profile matching（私有画像本地优先）

默认流程：把 public/restricted condition predicates 送到接收方，在本地对完整
`AgentExposureProfile` 匹配；只回传 assessment digest、三值 outcome、unknown predicates 和
最小 feedback。

只有本地能力不足且接收方明确同意时，才可向未来 Relay 披露最小 predicate subset。禁止上传：

- full tool/permission/asset inventory；
- local policy、credential、raw logs/trajectory；
- subject stable identity，除非 exact matching 必需且有授权；
- 与当前 signal 条件无关的 capability/runtime 字段。

Withheld 字段必须作为 `UNKNOWN`，不能推断为 false 或安全。

## 10. Data minimization and retention（数据最小化与保留期限）

以下数值是 `ARCHITECTURE_DEFAULT_PENDING_LEGAL_PRIVACY_REVIEW`，不是已获法律验证的全球
保留规则。更严格或相冲突的法律、合同、司法辖区和 Evidence Owner policy 优先；在
Legal/Privacy Owner 明确决定前，它们只能用于 P4–P6 设计审查，不能授权真实数据保留。
P0–P3 不创建存储。

```text
RETENTION_VALUES_STATUS=ARCHITECTURE_DEFAULT_PENDING_LEGAL_PRIVACY_REVIEW
LEGAL_VALIDATION_COMPLETED=false
REAL_DATA_RETENTION_AUTHORIZED=false
```

| Data class | Storage boundary | Default maximum retention |
|---|---|---|
| Public-safe signal bytes + lifecycle | public/mirrored history | indefinite append-only defensive history；不得含 private data |
| Public publisher assurance metadata | public signal history | 与 signal lifecycle 同期；撤回/过期后仍保留历史状态 |
| Restricted case summary | controlled review store | terminal disposition 后 180 天 |
| Restricted reproduction package | controlled validator store | signal terminal state后 180 天；更长需独立 justification |
| Private evidence | Evidence Owner only; Relay stores refs | Relay raw retention `0`；ref 最长按 Owner policy |
| Full exposure profile | recipient local only | Relay retention `0` |
| Disclosed minimized predicates | ephemeral assessment store | assessment 完成后最多 24 小时 |
| Applicability result | recipient or controlled Relay receipt | 90 天；不含完整 profile |
| Restricted validation feedback | controlled feedback store | 180 天后删除或不可逆去标识 |
| Raw local test output | recipient local only | Relay retention `0` |
| Pseudonymous delivery/ack receipt | subscription state | active subscription + 30 天 |
| Security rejection receipt | minimal abuse/audit record | 90 天，禁止保留 rejected secret payload |

Legal hold、安全事件调查或争议保全可暂停删除，但必须记录 authority、scope、review date 和
access limits；不能以“未来可能有用”为由无限保留。

## 11. Update, correction, expiry, and revocation（更新、纠正、过期与撤回）

| Event | Required use | Forbidden use |
|---|---|---|
| `UPDATED` | 新证据/覆盖范围增加且原核心结论仍有效 | 静默改变旧版本 bytes |
| `CORRECTED` | 原结论、条件、建议或原因状态存在实质错误 | 删除错误历史或复用旧 digest |
| `EXPIRED` | 到达有限有效期且未重新验证 | 继续以 `ACTIVE`/latest 分发 |
| `REVOKED` | 签名/key/publisher/policy/内容严重失信，或建议可能造成危险 | 仅从网页隐藏、保持 feed 为 active |

每个事件必须追加 `SignalLifecycleRecord`，包含 monotonic sequence、predecessor digest、reason、
effective time、issuer/recovery assurance、superseding version 和 signed envelope ref。

Correction 不抹去旧版本；旧版本的查询响应必须显著返回 current lifecycle status 和
superseding ref。

## 12. How old recipients discover withdrawal（旧版本接收者发现撤回）

未来机制必须同时提供：

1. signed monotonic change feed，支持 `after_cursor` 增量获取；
2. signal-specific lifecycle query，不依赖可变网页；
3. finite `expires_at`，离线超过 refresh window 后不能继续视为 active；
4. client high-water mark 和 predecessor continuity，拒绝 rollback；
5. optional OpenID SSF correction/revocation event profile；
6. TUF-style signed metadata/mirror consistency；
7. 可选 pseudonymous delivery/ack receipt，用于测量而非监控；
8. 多镜像/透明度兼容，避免唯一中心选择性隐藏。

客户端无法确认当前 lifecycle、时钟或 feed continuity 时，必须把信号状态视为
`UNKNOWN_OR_STALE`，而不是继续自动信任旧版本。

## 13. Key compromise policy（密钥泄露策略）

1. Publisher signing role 与 emergency recovery/revocation role 分离；
2. 采用 TUF-style root/threshold/rotation 思路，不自建 PKI；
3. 泄露窗口内签发的对象标记 `ASSURANCE_UNKNOWN_PENDING_REVIEW`；
4. 由独立 recovery role 发布 key revocation 与受影响 signal range；
5. 新 key 不得用泄露 key 自证继承；
6. 接收方必须重新验证 current metadata、high-water mark 和 affected versions；
7. 历史有效记录保留，但签名有效性和内容可依赖性分开记录。

当前没有 key、PKI、root 或 recovery service 被创建。

## 14. Malicious publisher policy（恶意发布者策略）

- 暂停该 publisher scope 的新信号进入 publication gate；
- 对受影响 signals 追加 `REVOKED` 或 `HOLD_REVIEW` lifecycle 事件；
- 保留恶意/错误历史和证据引用，禁止静默删除；
- 独立复核其它 publisher/feedback 的关联性，不能按关联数量自动连坐；
- 不生成全局 reputation score；使用 exact policy violations、assurance state 和 scope；
- 接收方本地信任决定不被中心强制覆盖。

## 15. Selective distribution and equivocation（选择性分发与双重陈述）

缓解要求：

- content-addressed immutable versions 和 signed lifecycle；
- 多镜像可核对相同 sequence/digest；
- receiver consistency probe 和 missing-cursor detection；
- 可选 SCITT transparent statement/receipt compatibility；
- 发布者不得向不同接收方用同一 `signal_id/version` 分发不同 bytes；
- 检出 equivocation 时 fail closed、保留两份证据并触发 emergency review。

SCITT compatibility 不等于已经存在 Transparency Service。

## 16. Downgrade, replay, and freeze attacks（降级、重放与冻结攻击）

- version/sequence 必须单调，客户端保存 high-water mark；
- old-but-valid signature 不能覆盖已见的新版本/撤回；
- expiry 和 metadata refresh window 必须有限；
- predecessor gap、fast-forward 异常或 timestamp source unknown 均 fail closed；
- mirror/feed 不一致返回 `UNKNOWN_OR_CONFLICTED`；
- 复用 TUF 的安全模型，不创建自定义 `latest` 信任方案。

## 17. Non-executable advice policy（非可执行建议策略）

所有 `detection_advice`/`disposition_advice` 只允许：

| Allowed field | Meaning |
|---|---|
| `advice_id` | stable specification reference |
| `goal` | defensive objective |
| `preconditions` | local conditions requiring review |
| `expected_observation` | what a local test may observe |
| `risk_if_attempted` | bounded test risk |
| `required_isolation` | sandbox/isolation class |
| `local_approval_required` | always explicit |
| `rollback_or_stop_condition` | human-readable safety stop |

禁止字段/载荷：shell command、code snippet intended for execution、tool call、function arguments、
remote endpoint invocation、credential、auto-apply patch、auto-disable/kill、permission change 或
任何可被接收智能体直接执行的 payload。

```text
ADVICE_IS_EXECUTABLE=false
ADVICE_AUTO_APPLY=false
ADVICE_GRANTS_PERMISSION=false
LOCAL_POLICY_DECIDES_ACTION=true
```

## 18. P3 result（P3 结果）

```text
P3_COMPLETE=true
SUBMISSION_GATE_DEFINED=true
INDEPENDENT_REPRODUCTION_GATE_DEFINED=true
HIGH_IMPACT_PUBLICATION_GATE_DEFINED=true
PUBLISHER_ASSURANCE_POLICY_DEFINED=true
RECIPIENT_LOCAL_TRUST_BOUNDARY_DEFINED=true
FIELD_DISCLOSURE_POLICY_DEFINED=true
LOCAL_FIRST_MATCHING_DEFINED=true
RETENTION_LIMITS_DEFINED=true
CORRECTION_EXPIRY_REVOCATION_DEFINED=true
OLD_RECIPIENT_REVOCATION_DISCOVERY_DEFINED=true
KEY_COMPROMISE_AND_EQUIVOCATION_RULES_DEFINED=true
EXECUTABLE_ADVICE_ALLOWED=false
PUBLIC_SIGNAL_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
```
