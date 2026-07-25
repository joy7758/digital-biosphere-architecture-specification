---
document_id: DBA-TITMAS-RFC-NUMBERING-DOCUMENT-MODEL-0.1
title: TITMAS RFC Numbering and Document Model v0.1
title_zh: TITMAS RFC 编号与文档模型 v0.1
version: 0.1.0
status: numbering-model-candidate-no-rfc-assigned
maturity: Development
maturity_scope: entire-document
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-document-identity-model-candidate
architecture_domain: TITMAS
document_maturity: Development
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
rfc_ids_assigned: 0
existing_documents_promoted: 0
authority_effect: none
---

# TITMAS RFC Numbering and Document Model v0.1

## 1. Boundary of the Term RFC（RFC 术语边界）

`TITMAS RFC` 在本模型中表示 TITMAS 内部的 Request for Comments candidate（征求意见文档
候选）。它不是 IETF RFC，不得使用 `RFC NNNN`、`Internet Standard`、`IETF Standard` 或
其他足以造成外部标准认可误解的名称。

IETF 的新工作通常从 Internet-Draft 开始，进入 RFC 需要其正式流程；参见
[IETF Introduction](https://www.ietf.org/about/introduction/) 与
[RFC 2026](https://www.rfc-editor.org/info/rfc2026/)。TITMAS 只借鉴“先草案、再审查、
再积累实现经验”的方法，不复制 IETF 编号、流程权力或标准地位。

## 2. Canonical Identifier（规范标识）

未来获准进入编号流程的文档使用：

```text
TITMAS-0001
TITMAS-0002
...
```

规则：

- 四位十进制数，单调递增；
- 编号一旦发布不得复用；
- 编号只标识文档 lineage，不表示成熟度、采纳、实现或标准地位；
- Rejected、Withdrawn、Superseded、Deprecated 文档保留编号和历史；
- 当前 `NEXT_NUMBER=NOT_RESERVED`，本文件不分配任何正式编号。

## 3. Category Model（分类模型）

可使用 category-qualified display identifier：

```text
TITMAS-E-0001
TITMAS-A-0001
TITMAS-V-0001
TITMAS-I-0001
TITMAS-R-0001
TITMAS-S-0001
```

| Code | Category | Scope |
|---|---|---|
| `E` | Evidence and Execution Boundary | Evidence/Execution 的结构、lineage、failure 与 non-truth 边界 |
| `A` | Adapter Contract | passive capture、handoff、translation 与 no-writeback 契约 |
| `V` | Verification and Conformance | verification reference、case、result 与 semantic non-elevation |
| `I` | Interoperability Profile | framework/protocol mapping、version binding 与 compatibility |
| `R` | Recommendation and Evaluation Interface | 有界 Evaluation 输入、结果引用、Recommendation 交接与 advisory-only 语义 |
| `S` | Core Specification | TITMAS 自身术语、对象、生命周期与规范性规则 |

`TITMAS-NNNN` 是 lineage identifier；category 是 metadata/display view。一个编号不能通过
更改 category 产生第二文档。涉及多类时选择主 category，并在 metadata 中列
`secondary_categories`。

Research Contribution 默认使用非规范 Research Note，不占用 `R` 类编号；只有研究结果
进入 Evaluation/Recommendation interface proposal 时，才可提出 `R` 类候选。该调整避免
把研究结论误写成 SAEE Evaluation Authority。

## 4. Document Status（文档状态）

| Status | Meaning | What it does not mean |
|---|---|---|
| `Draft` | 工作草稿，可大幅变化 | consensus、decision、public standard |
| `Experimental` | 获准在有界范围积累实现/使用反馈 | Stable、production、ecosystem adoption |
| `Candidate` | 范围趋于完整，等待最终 review/decision | approved standard、implementation authorization |
| `Stable` | 对 exact scope/version 作出明确稳定决定 | certification、universal adoption、DBOS/SAEE authority |
| `Deprecated` | 不建议新采用，保留迁移与历史 | deleted、invalid history |

`document_status` 与既有
[Document Maturity Policy](titmas-document-maturity-policy-v0.1.md) 的
`document_maturity` 分开记录。建议 crosswalk 仅用于审查，不自动转换：

| document_status | usual maturity range |
|---|---|
| `Draft` | `Development` / `Alpha` |
| `Experimental` | `Alpha` / `Beta` |
| `Candidate` | `Release Candidate` |
| `Stable` | `Stable` |
| `Deprecated` | `Deprecated` |

## 5. Required Metadata（必需元数据）

```yaml
titmas_id:
category:
secondary_categories: []
title:
version:
document_status: Draft|Experimental|Candidate|Stable|Deprecated
document_maturity: Development
normative: false
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
proposal_reference:
supersedes:
superseded_by:
canonical_source_ref:
compatibility_statement:
implementation_refs: []
conformance_refs: []
known_limitations: []
```

`normative: true` 只有在 Specification Authority scope、Owner 和 Architecture Decision
全部可追溯时才允许。

## 6. Number Assignment Gate（编号分配闸门）

未来分配编号至少需要：

1. Proposal 通过 intake 和 duplicate review；
2. category、title、scope、non-goals、human accountability 完整；
3. canonical registry path、issuer 和 conflict policy 已决定；
4. public/private status 与 license/IPR policy 明确；
5. 编号分配外部动作已另行授权（若涉及公共仓库）。

本模型没有建立 registry、issuer、仓库或自动编号器。

## 7. Existing Document Non-promotion（既有文档不升级）

现有 `architecture/` 文档、ADR、mapping、schema、review 和 report 均不因本模型自动获得
TITMAS 编号，也不成为 formal standard。

```text
EXISTING_DOCUMENTS_PROMOTED_TO_TITMAS_RFC=0
TITMAS_RFC_IDS_ASSIGNED=0
TITMAS_STABLE_STANDARDS_CREATED=0
TITMAS_RFC_REGISTRY_CREATED=false
TITMAS_NUMBER_ISSUER_ASSIGNED=false
```

## 8. Non-elevation Rules（非抬升规则）

```text
NUMBER_NE_MATURITY=true
NUMBER_NE_ADOPTION=true
DRAFT_NE_CONSENSUS=true
EXPERIMENTAL_NE_STANDARD=true
MAPPING_NE_ADOPTION=true
IMPLEMENTATION_NE_SPECIFICATION=true
DEPRECATED_NE_DELETED=true
TITMAS_RFC_NE_IETF_RFC=true
```
