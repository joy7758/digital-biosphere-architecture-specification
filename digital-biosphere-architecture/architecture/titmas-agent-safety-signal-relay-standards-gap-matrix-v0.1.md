---
spec_id: TITMAS-AGENT-SAFETY-SIGNAL-RELAY-STANDARDS-GAP-0.1
title: TITMAS Agent Safety Signal Relay Standards and Existing Components Gap Matrix v0.1
title_zh: TITMAS 智能体安全信号中继标准与现有组件差距矩阵 v0.1
status: ACCEPTED_ARCHITECTURE_SPECIFICATION_P1
normative_for_relay_architecture: true
implementation_status: NOT_IMPLEMENTED
conformance_status: NOT_ASSESSED
primary_repository: digital-biosphere-architecture
decision_ref: ADR-040
---

# TITMAS 智能体安全信号中继标准与现有组件差距矩阵 v0.1

## 1. Purpose and decision method（目的与决策方法）

本文件完成 P1：逐项说明既有标准/组件已经解决什么、没有解决什么、Relay 的采用方式、
新增语义的必要性和重复建设风险。

采用方式枚举：

```text
DIRECT_REUSE=规范直接复用，不复制其机制
COMPATIBILITY_PROFILE=建立有界映射或 profile，不宣称原生符合
REFERENCE_ONLY=只作为设计/威胁参考
DEFERRED_NOT_ADOPTED=当前不采用，需后续独立决定
```

“复用”在 P1 只表示架构选择，不表示库依赖、代码、部署、符合性、认证或 adoption 已存在。

## 2. Normative and non-normative layers（规范性与非规范性层）

| Layer | Normative for future Relay | Non-normative/reference only |
|---|---|---|
| Safety Signal domain semantics | 本项目 P2/P3；CSAF compatibility profile | 人类报告、LLM 摘要、新闻正文 |
| JSON object validation | JSON Schema 2020-12 | README 示例或未验证 JSON |
| Future HTTP interface description | OpenAPI 3.1.x | 网页表单、临时 endpoint 文案 |
| Signed envelope/attestation | DSSE + in-toto profile candidate | 自定义签名串、仅有 hash 的“签名”声明 |
| Update/rollback/freeze defense | TUF compatibility profile candidate | 自定义 `latest` 指针或仅靠 wall clock |
| Event stream/discovery | OpenID SSF profile candidate | 自建 webhook/通用消息队列 |
| CTI ecosystem exchange | STIX/TAXII adapter candidate | 把所有 Agent signal 强行建模为 STIX |
| Transparency receipts | SCITT compatibility option | 自建 transparency ledger |
| Object references | AOP compatibility mapping | AOP non-normative registry 当身份权威 |
| Identity/context/evidence authority | DBOS + existing identity/evidence dependencies | Relay 自报 name/alias 或 POP identity |
| Evidence receipt/reference | `agent-evidence` | 第二套原始证据存储 |
| Post-execution audit reference | ARO optional reference | ARO 当 Relay/publisher/trust owner |

## 3. Standards and component gap matrix（标准与组件差距矩阵）

### 3.1 CSAF（Common Security Advisory Framework）

Official source: [OASIS CSAF 2.0](https://www.oasis-open.org/standard/common-security-advisory-framework-version-2-0-3/)

1. **已经解决**：机器可读安全公告的 document tracking、版本、引用、产品树、漏洞/问题、
   product status、notes、remediation 和 publisher/distribution 基础语义；支持 informational
   advisory 与 security incident response profiles。
2. **没有解决**：Agent capability/runtime/tool/permission/identity-binding 条件；
   `publisher_assurance` 与 `recipient_local_trust_decision` 分离；三值 Agent applicability；
   本地复现反馈；异常直接产生的 beneficial capability。
3. **采用决定**：`COMPATIBILITY_PROFILE`。优先映射 document tracking、revision history、
   references、impact/remediation；不复制第二套通用 advisory vocabulary。
4. **必要新增语义**：Agent exposure predicates、broken assumptions、cause status、
   beneficial capability 受限枚举、epistemic status、本地测试结果和披露等级。
5. **重复建设风险**：`HIGH`。若重新设计通用公告、产品状态或 remediation vocabulary 即重复。

### 3.2 DSSE / in-toto

Official sources: [DSSE](https://github.com/secure-systems-lab/dsse)、
[in-toto Attestation envelope](https://github.com/in-toto/attestation/blob/main/spec/v1/envelope.md)

1. **已经解决**：对任意 payload 的 authenticated envelope、payload type 绑定、一个或多个
   signature、key hint，以及 attestation statement/envelope 分层。
2. **没有解决**：PKI、key ownership、publisher trust policy、key revocation、信号语义、
   准确性、撤回传播或接收方行动授权。有效签名不证明内容为真。
3. **采用决定**：`DIRECT_REUSE` 的签名 envelope 候选 + `COMPATIBILITY_PROFILE` 的
   Agent Safety Signal predicate；最终 envelope 选择仍须在 P5 单独授权。
4. **必要新增语义**：`publisher_assurance`、exact signal/schema/context digest、
   policy/ref verification result、limitations。
5. **重复建设风险**：`CRITICAL`。禁止自建签名格式、密码算法或把 digest 冒充 signature。

### 3.3 TUF（The Update Framework）

Official source: [TUF security properties](https://theupdateframework.io/docs/security/)

1. **已经解决**：更新 metadata 的角色分离、threshold/key rotation 思路，以及 rollback、
   freeze、fast-forward 和 key compromise 等攻击的防护模型。
2. **没有解决**：Safety Signal 内容、Agent applicability、证据语义、发布者准确性和本地信任。
3. **采用决定**：`COMPATIBILITY_PROFILE`，用于未来 signal index、版本、expiry、key role、
   correction/revocation metadata；P3 只定义规则，不部署 repository。
4. **必要新增语义**：signal target/version/supersession/revocation reason 与 TUF target metadata
   的映射。
5. **重复建设风险**：`CRITICAL`。禁止自建“latest + timestamp”更新安全方案。

### 3.4 JSON Schema

Official source: [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)

1. **已经解决**：JSON 实例结构、类型、枚举、条件、引用和机器验证词汇。
2. **没有解决**：领域含义、密码学信任、跨对象因果、隐私 policy 或运行时行为。
3. **采用决定**：`DIRECT_REUSE`；未来 schema 必须固定 dialect/version 和 `$id`。
4. **必要新增语义**：六类对象的 TITMAS 字段、枚举、跨引用不变量和披露 ceiling。
5. **重复建设风险**：`HIGH`。不得设计第二套 schema language 或仅靠 prompt 校验。

### 3.5 OpenAPI

Official source: [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0.html)

1. **已经解决**：语言无关 HTTP API discovery、operations、request/response、security scheme
   和 JSON Schema 兼容描述。
2. **没有解决**：服务正确性、信号 trust、identity authority、撤回可达性或本地策略。
3. **采用决定**：`DIRECT_REUSE` 作为未来 API contract；P0–P3 不创建 API server。
4. **必要新增语义**：Agent-first operation IDs、三值/unknown 错误语义、digest/version headers、
   non-execution response constraints。
5. **重复建设风险**：`MEDIUM`。禁止自建 IDL 或把网页文档当机器接口。

### 3.6 STIX / TAXII

Official sources: [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html)、
[TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html)

1. **已经解决**：STIX 的 CTI domain/relationship/observable/pattern 对象；TAXII 的 HTTPS
   API root、collection、manifest、object/version、分页和状态资源。
2. **没有解决**：Agent exposure profile、publisher assurance/local trust 分离、证据 admission、
   本地复现结果和非执行建议；TAXII 不是信号 truth 或 action authorization。
3. **采用决定**：`COMPATIBILITY_PROFILE` 但 `DEFERRED_NOT_ADOPTED` 于 P0–P3。
   仅在需要进入既有 CTI 生态时定义 STIX extension/TAXII collection adapter。
4. **必要新增语义**：Agent subject/condition、Safety Signal lifecycle 与 CTI object/version 映射。
5. **重复建设风险**：`HIGH`。不得自建通用 CTI protocol/message bus；也不得为追求兼容把
   非 CTI 语义强行压入 STIX indicator。

### 3.7 OpenID SSF（Shared Signals Framework）

Official source: [OpenID Shared Signals Framework 1.0 Final](https://openid.net/specs/openid-sharedsignals-framework-1_0-final.html)

1. **已经解决**：cooperating Transmitter/Receiver、Security Event Token profile、subject
   principals/claims、stream management、push/poll delivery、verification event 和
   `/.well-known/ssf-configuration` discovery。1.0 Final Specification 发布于 2025-08-29。
2. **没有解决**：TITMAS Safety Signal 内容、证据保证、异常假设、Agent runtime conditions、
   correction semantics、全局准确性或本地行动授权。
3. **采用决定**：`COMPATIBILITY_PROFILE`，是未来定向 event stream/discovery 的优先候选；
   P0–P3 不创建 transmitter、receiver、stream 或 webhook。
4. **必要新增语义**：Agent Safety Signal event type、subject identifier 与 DBOS stable ID
   mapping、full-object retrieval/reference、correction/revocation event semantics。
5. **重复建设风险**：`CRITICAL`。不得自建通用 secure webhook、stream management 或
   transmitter discovery。

### 3.8 SCITT（Supply Chain Integrity, Transparency, and Trust）

Official sources: [RFC 9943](https://datatracker.ietf.org/doc/rfc9943/)；
[SCITT Reference APIs draft-11](https://datatracker.ietf.org/doc/draft-ietf-scitt-scrapi/)

1. **已经解决**：RFC 9943 定义 single-issuer signed statement、Transparency Service、
   registration policy、transparent statement 和 receipt，以可验证数据结构增强可审计性、
   可问责性和抗 equivocation；不要求单一中心。SCRAPI 仍在 RFC Editor queue，是 work in progress。
2. **没有解决**：statement 内容准确性、参与方发现/变更通知、Safety Signal 语义、
   Agent applicability、本地 trust 和 correction policy。RFC 9943 明确变更通知不在范围内。
3. **采用决定**：RFC 9943 为 `COMPATIBILITY_PROFILE` 选项；SCRAPI 为 `REFERENCE_ONLY`
   直至正式发布并重新 pin。P0–P3 不建立 transparency service 或 ledger。
4. **必要新增语义**：Safety Signal signed-statement media/profile、signal lifecycle 与 receipt
   的引用关系；correction 保留旧 statement 而非删除历史。
5. **重复建设风险**：`CRITICAL`。不得自建透明账本或把普通 append-only 文件冒充 SCITT。

### 3.9 AOP（Agent Object Protocol）

Current audited source: `agent-object-protocol@c0619f50eba4d8aac3589f41a80a874cceb2707e`

1. **已经解决**：portable object manifest、稳定 object reference、version、digest、schema、
   fixtures/conformance 模式和 optional `signature_ref`。
2. **没有解决**：canonical machine identity、fuzzy binding、publisher trust、signal lifecycle、
   evidence truth 或生产 registry；registry/resolve artifacts 是 non-normative。
3. **采用决定**：`COMPATIBILITY_PROFILE`，映射 Safety Signal/subject refs；不修改 AOP core。
4. **必要新增语义**：Safety Signal object kind/profile、DBOS identity resolution status 和
   proof assurance。
5. **重复建设风险**：`MEDIUM`。不得复制 object ID/version/digest 机制，也不得把 AOP alias
   resolution 当身份认证。

### 3.10 DBOS

Architecture source: [`project-mapping.md`](project-mapping.md)、
[`telemetry-to-evidence-admission-contract.md`](telemetry-to-evidence-admission-contract.md)

1. **已经解决/拥有**：架构上拥有 stable Identity、Lifecycle、Execution、Canonical Evidence、
   Verification 和 execution-context authority；已有 evidence admission/provenance levels 提案。
2. **没有解决**：当前没有经本决定确认的 Safety Signal domain object、relay/distribution、
   recipient applicability 或反馈生命周期实现。
3. **采用决定**：`DIRECT_REUSE` 的规范依赖；任何 mapping/implementation 属 P4+ 独立 gate。
4. **必要新增语义**：只新增 DBOS ref/resolution/assurance/context digest 字段，不复制对象。
5. **重复建设风险**：`CRITICAL`。Relay 不得创建 Identity、Execution、Evidence 或 Verification。

### 3.11 `agent-evidence`

Current audited source: `agent-evidence@911db6650547617c71331ddd9506811f04191656`

1. **已经解决**：执行证据记录、append-only storage、digests、manifest、optional signed metadata、
   offline bundle、verification receipt 和 verify-first/read-only surface。
2. **没有解决**：Safety Signal 语义、受影响条件、发布者 trust、适用性、分发、撤回和反馈聚合。
3. **采用决定**：`DIRECT_REUSE` 的 EvidenceReference/VerificationReceipt reference 能力；
   不复制 raw evidence，不把 Relay 变成第二 Evidence store。
4. **必要新增语义**：receipt ref 的 role、admission/assurance/limitations 和 disclosure ceiling。
5. **重复建设风险**：`CRITICAL`。Relay 只能引用；不得再实现 bundle/store/verifier。

### 3.12 ARO / ARO-Audit

Current audited source: `aro-audit@74a7f584b8cb18ca2655a0dac30e77e41e582c43`

1. **已经解决**：公开参考中的 receipt validation、tamper/replay/lifecycle conformance 和
   post-execution audit/review 模式。
2. **没有解决**：生产 audit control plane、Signal publisher、适用性、信任决定、分发或执行授权；
   当前 README 与边界文档仍有 control-plane 表述冲突。
3. **采用决定**：`REFERENCE_ONLY` 的 optional audit ref；冲突解决前不形成 runtime dependency。
4. **必要新增语义**：仅 `audit_receipt_refs` 和明确 `verification_effect=none`；不复制审计格式。
5. **重复建设风险**：`HIGH`。若 Relay 自建 post-execution audit 或让 ARO 拥有信号状态即重复/越权。

## 4. Adopt-before-build stack decision（先采用再建设）

```text
DOMAIN_CONTENT_BASE=CSAF_COMPATIBILITY_PROFILE
OBJECT_VALIDATION=JSON_SCHEMA_2020_12
FUTURE_API_DESCRIPTION=OPENAPI_3_1
SIGNED_ENVELOPE_CANDIDATE=DSSE_IN_TOTO
UPDATE_SECURITY_CANDIDATE=TUF_PROFILE
EVENT_STREAM_CANDIDATE=OPENID_SSF_PROFILE
CTI_ADAPTER_CANDIDATE=STIX_TAXII_DEFERRED
TRANSPARENCY_CANDIDATE=SCITT_RFC_9943_OPTIONAL
OBJECT_REFERENCE_CANDIDATE=AOP_PROFILE
IDENTITY_CONTEXT_EVIDENCE_AUTHORITY=DBOS_AND_EXISTING_DEPENDENCIES
EVIDENCE_REFERENCE_RECEIPT=AGENT_EVIDENCE
POST_EXECUTION_AUDIT=ARO_REFERENCE_ONLY
```

## 5. Prohibited duplication（禁止重复建设）

本项目不得自建：

- 密码算法、签名 envelope、PKI 或 key discovery infrastructure；
- 通用安全公告语言、通用 CTI language、secure webhook、消息队列或 pub/sub；
- transparency ledger、通用 update framework 或防 rollback 协议；
- 第二套 Identity、Execution、Evidence、Verification、Audit 或全局 reputation system；
- 仅靠 LLM 的 schema、admission、trust、publication 或 applicability decision。

## 6. P1 result（P1 结果）

```text
P1_COMPLETE=true
STANDARDS_COMPARED=12
DIRECT_REUSE_OR_COMPATIBILITY_DECISIONS_RECORDED=true
DUPLICATE_BUILD_PROHIBITIONS_RECORDED=true
IMPLEMENTATION_CREATED=false
CONFORMANCE_CLAIMED=false
```
