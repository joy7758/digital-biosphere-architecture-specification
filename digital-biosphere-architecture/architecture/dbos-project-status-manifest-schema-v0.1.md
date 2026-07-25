---
document_id: DBA-DBOS-PROJECT-STATUS-MANIFEST-SCHEMA-0.1
title: DBOS Project Status Manifest Schema v0.1 Design Review
title_zh: DBOS 项目状态清单 Schema v0.1 设计审查
status: SCHEMA_AND_ADR_PROPOSAL_READY_FOR_HUMAN_REVIEW
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: ARCHITECTURE_SCHEMA_PROPOSAL_AND_ADR
primary_repository: DBA
future_implementation_repository: DBOS
decision_queue_reference: DQ-003
source_resolution_reference: architecture/dbos-canonical-source-resolution-v0.1.md
observed_at: 2026-07-23
implementation_effect: NONE
actual_manifest_created: false
actual_schema_created: false
embedded_schema_json_validated: true
embedded_schema_metaschema_validated: true
dbos_repository_modified: false
revision_modified: false
repository_migration_authorized: false
---

# DBOS Project Status Manifest Schema v0.1 Design Review

中文：DBOS 项目状态清单 Schema v0.1 设计审查。

## 0. Design Verdict（设计结论）

本次设计审查填补 [DBOS Canonical Source Resolution Review v0.1](dbos-canonical-source-resolution-v0.1.md)
发现的 project-local canonical status manifest（项目本地规范状态清单）缺口，但不创建实际
manifest 或 Schema 文件。

```text
DESIGN_RESULT=SCHEMA_AND_ADR_PROPOSAL_READY_FOR_HUMAN_REVIEW
PROPOSED_MANIFEST_PATH=PROJECT-STATUS.json
PROPOSED_SCHEMA_PATH=schemas/project-status.schema.json
MANIFEST_AUTHORITY=DBOS_PROJECT_LOCAL
DBA_ROLE=REFERENCE_ONLY_AGGREGATOR
TITMAS_ROLE=READ_ONLY_VERSIONED_CONSUMER
MANIFEST_SELF_AUTHORIZATION=false
ACTUAL_MANIFEST_CREATED=false
ACTUAL_SCHEMA_CREATED=false
DBOS_DQ_003_SLICE_DECIDED=false
DBOS_DQ_003_SLICE_IMPLEMENTED=false
IMPLEMENTATION_RECOMMENDED_NOW=false
```

推荐采用 project-local manifest + separate Schema（项目本地清单 + 独立 Schema）方案：

```text
DBOS repository
  ├─ PROJECT-STATUS.json
  └─ schemas/project-status.schema.json

DBA
  └─ read-only reference + observed_at + freshness + conflict state

TITMAS
  └─ read-only source coordinate consumption; no status write authority
```

`PROJECT-STATUS.json` 的角色是 canonical project status index（规范项目状态索引），不是
Runtime truth database（运行事实数据库）、Release Decision、Gate Service、Permission、
Evidence、Verification 或 Production Authorization。Schema validation（结构验证）只证明
字段形状符合提案，不能证明引用的 commit、tag、decision、release、artifact 或状态是真的。

## 1. Scope and Design Constraints（范围与设计约束）

### 1.1 本次任务

本文件完成：

1. 定义 `PROJECT-STATUS.json` 的最小对象模型；
2. 给出 JSON Schema 2020-12 proposal（提案）；
3. 定义 source、branch、commit、release/tag、authority、owner、status、divergence 与 review
   timestamp 的失败关闭规则；
4. 给出 ADR decision recommendation（架构决策建议）；
5. 定义未来实施、验证、采纳和 DBA 引用顺序。

### 1.2 明确禁止

```text
AUTO_SELECT_SOURCE=false
AUTO_UPDATE_REVISION=false
AUTO_FETCH_OR_PULL=false
AUTO_MIGRATE_REPOSITORY=false
AUTO_CLOSE_DQ_003=false
AUTO_PROMOTE_STATUS=false
AUTO_AUTHORIZE_RELEASE=false
AUTO_AUTHORIZE_PRODUCTION=false
```

本提案不得根据本地 checkout、文件修改时间、最新 branch tip、tag 名称、GitHub Release、
package version、测试数量或 validator `PASS` 自动选择 canonical source。

### 1.3 Primary repository（主责任仓库）

| 工作 | primary repository | 本次状态 |
|---|---|---|
| Schema/ADR architecture proposal | DBA | 本文件 |
| 未来实际 `PROJECT-STATUS.json` 和 Schema | DBOS | `NOT_AUTHORIZED_NOT_CREATED` |
| DBA status projection | DBA | 后继只读引用；本次不修改 |
| TITMAS source consumption | TITMAS architecture domain | 后继接口输入；无写权 |

## 2. Existing Surface Review（现有表面审查）

### 2.1 不能复用的现有表面

| 现有表面 | 当前角色 | 为什么不能成为 DBOS project status authority |
|---|---|---|
| DBOS `README.md` | 人类/智能体叙事入口 | 包含历史状态和已过期自述；不能稳定表达多来源、freshness 与 conflict |
| DBOS `pyproject.toml` | package metadata | `0.1.0.dev0` 只描述分发包版本，不描述项目、gate、release 或 Runtime 状态 |
| DBOS `constitution/constitution.yaml` | 领域宪法与 registry pointer | 定义对象与边界，不是项目 branch/release/status 清单 |
| DBOS `registry/project-manifests.yaml` | federation central pending placeholders | 自述不是 project-local adopted manifest；复用会混淆 federation 与项目状态 |
| DBA `PROGRAM-STATUS.md` | timestamped program observation（带时间项目群观察） | DBA 只能引用聚合，不能成为 DBOS child-project truth |
| DBA `site/public/status.json` | public program projection（公共项目群投影） | 包含跨项目/网站/发布状态，不能反向写入 DBOS 权威 |
| SAEE `PROJECT_STATUS.md` 模式 | SAEE 自身的长篇状态叙事 | 不是 DBOS Schema，且 prose status（叙事状态）不适合作为确定性机器契约 |

### 2.2 不重复的边界

新 manifest 不复制：

- DBOS Identity、Lifecycle、Capability、Execution、Evidence 或 Verification registry；
- DQ-018/PR-G2A 的 source/receipt/test packet；
- DBA Decision Queue、Risk Register、Gate Record 或 Program Status；
- Git commit graph、tag object、GitHub Release API 或 artifact bytes；
- SAEE Evaluation、Fitness、Risk 或 Evolution Recommendation；
- TITMAS interoperability mapping。

它只保存稳定引用、有限状态枚举、观察时间、Owner binding（Owner 绑定）、unknowns 和
conflict classification（冲突分类）。

## 3. Required Field Model（必需字段模型）

| 用户要求 | Schema 字段 | 语义 |
|---|---|---|
| project identity | `project_identity` | 固定 DBOS ID、名称、架构角色；repository 不等于 Runtime |
| canonical repository | `canonical_source.repository_url` | 被 Human Decision 接受的仓库 URL；不自动发现 |
| canonical branch | `canonical_source.default_branch_ref` | 完整 Git ref；不允许模糊 `latest` |
| reviewed commit | `canonical_source.reviewed_commit` | 40 位 exact SHA；必须与观察时间绑定 |
| release/tag | `release_state.source_release` + `distribution_releases` | 源码 tag 与分发 release 分开 |
| authority type | `authority.authority_type` | DBOS 是规范存在与记录边界；manifest 不是 Authority generator |
| owner | `owners` | Program、Domain、manifest、release Owner 分角色与 scope 绑定 |
| status | `status` | source/implementation/release/production 多轴状态，不用一个模糊字符串 |
| divergence handling | `divergence` | classification、compared refs、blocking state 与 resolution rule |
| review timestamp | `review` | observed/reviewed/freshness/next-review 与 reviewer/decision 引用 |

## 4. Proposed JSON Schema（建议 JSON Schema）

下列代码块是设计提案，不是已创建的 `schemas/project-status.schema.json`。

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "dbio://schema/dbos-project-status/v0.1",
  "title": "DBOS Project Status Manifest v0.1",
  "description": "Agent-readable DBOS project status index. Validation never grants authority, permission, release, runtime, evidence truth, or production readiness.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "$schema",
    "schema_version",
    "manifest_id",
    "project_identity",
    "canonical_source",
    "release_state",
    "authority",
    "owners",
    "status",
    "divergence",
    "review",
    "effects",
    "limitations"
  ],
  "properties": {
    "$schema": {
      "type": "string",
      "const": "schemas/project-status.schema.json"
    },
    "schema_version": {
      "type": "string",
      "const": "0.1"
    },
    "manifest_id": {
      "type": "string",
      "const": "dbio://project-status/dbos/v0.1"
    },
    "project_identity": {
      "$ref": "#/$defs/projectIdentity"
    },
    "canonical_source": {
      "$ref": "#/$defs/canonicalSource"
    },
    "release_state": {
      "$ref": "#/$defs/releaseState"
    },
    "authority": {
      "$ref": "#/$defs/authority"
    },
    "owners": {
      "$ref": "#/$defs/owners"
    },
    "status": {
      "$ref": "#/$defs/statusAxes"
    },
    "divergence": {
      "$ref": "#/$defs/divergence"
    },
    "review": {
      "$ref": "#/$defs/review"
    },
    "effects": {
      "$ref": "#/$defs/zeroEffects"
    },
    "limitations": {
      "type": "array",
      "minItems": 1,
      "items": {"$ref": "#/$defs/nonEmptyString"},
      "uniqueItems": true
    }
  },
  "$defs": {
    "nonEmptyString": {
      "type": "string",
      "minLength": 1
    },
    "nullableString": {
      "type": ["string", "null"]
    },
    "gitObjectId": {
      "type": "string",
      "pattern": "^[0-9a-f]{40}$"
    },
    "gitCommit": {
      "$ref": "#/$defs/gitObjectId"
    },
    "gitRef": {
      "type": "string",
      "pattern": "^refs/(heads|tags)/[A-Za-z0-9._/-]+$"
    },
    "sha256": {
      "type": "string",
      "pattern": "^sha256:[0-9a-f]{64}$"
    },
    "projectIdentity": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "project_id",
        "canonical_name",
        "architecture_role",
        "repository_is_runtime",
        "repository_is_digital_entity"
      ],
      "properties": {
        "project_id": {"type": "string", "const": "DBOS"},
        "canonical_name": {"type": "string", "const": "Digital Biosphere Operating System"},
        "architecture_role": {"type": "string", "const": "CANONICAL_EXISTENCE_AND_RECORD_BOUNDARY"},
        "repository_is_runtime": {"type": "boolean", "const": false},
        "repository_is_digital_entity": {"type": "boolean", "const": false}
      }
    },
    "gatedSource": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "gate_or_decision_ref",
        "branch_ref",
        "source_commit",
        "receipt_commit",
        "adoption_status",
        "auto_promotes_to_main"
      ],
      "properties": {
        "gate_or_decision_ref": {"$ref": "#/$defs/nonEmptyString"},
        "branch_ref": {"$ref": "#/$defs/gitRef"},
        "source_commit": {"$ref": "#/$defs/gitCommit"},
        "receipt_commit": {
          "oneOf": [
            {"$ref": "#/$defs/gitCommit"},
            {"type": "null"}
          ]
        },
        "adoption_status": {
          "type": "string",
          "enum": [
            "PROPOSED",
            "AUTHORIZED",
            "IMPLEMENTED_RECEIPT_BOUND",
            "READY_FOR_HUMAN_REVIEW",
            "APPROVED",
            "REJECTED",
            "SUPERSEDED",
            "CONFLICTED"
          ]
        },
        "auto_promotes_to_main": {"type": "boolean", "const": false}
      }
    },
    "canonicalSource": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "repository_url",
        "repository_visibility",
        "default_branch_ref",
        "status_manifest_path",
        "status_authority",
        "reviewed_commit",
        "observed_at",
        "live_remote_verified",
        "gated_sources"
      ],
      "properties": {
        "repository_url": {
          "type": "string",
          "const": "https://github.com/joy7758/digital-biosphere-os.git"
        },
        "repository_visibility": {
          "type": "string",
          "enum": ["PRIVATE", "PUBLIC", "INTERNAL", "UNKNOWN"]
        },
        "default_branch_ref": {
          "type": "string",
          "const": "refs/heads/main"
        },
        "status_manifest_path": {
          "type": "string",
          "const": "PROJECT-STATUS.json"
        },
        "status_authority": {
          "type": "string",
          "const": "DBOS_PROJECT_LOCAL"
        },
        "reviewed_commit": {"$ref": "#/$defs/gitCommit"},
        "observed_at": {"type": "string", "format": "date-time"},
        "live_remote_verified": {"type": "boolean"},
        "gated_sources": {
          "type": "array",
          "items": {"$ref": "#/$defs/gatedSource"},
          "uniqueItems": true
        }
      }
    },
    "sourceRelease": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "status",
        "tag_ref",
        "tag_object",
        "peeled_commit",
        "signature_status",
        "release_url"
      ],
      "properties": {
        "status": {
          "type": "string",
          "enum": ["NONE", "TAG_ONLY", "GITHUB_RELEASED", "REVOKED", "CONFLICTED"]
        },
        "tag_ref": {
          "oneOf": [
            {"type": "string", "pattern": "^refs/tags/[A-Za-z0-9._/-]+$"},
            {"type": "null"}
          ]
        },
        "tag_object": {
          "oneOf": [
            {"$ref": "#/$defs/gitObjectId"},
            {"type": "null"}
          ]
        },
        "peeled_commit": {
          "oneOf": [
            {"$ref": "#/$defs/gitCommit"},
            {"type": "null"}
          ]
        },
        "signature_status": {
          "type": "string",
          "enum": ["NOT_ASSESSED", "VERIFIED", "UNVERIFIED", "ABSENT"]
        },
        "release_url": {
          "oneOf": [
            {"type": "string", "format": "uri"},
            {"type": "null"}
          ]
        }
      },
      "allOf": [
        {
          "if": {
            "properties": {"status": {"const": "NONE"}},
            "required": ["status"]
          },
          "then": {
            "properties": {
              "tag_ref": {"type": "null"},
              "tag_object": {"type": "null"},
              "peeled_commit": {"type": "null"},
              "release_url": {"type": "null"}
            }
          }
        },
        {
          "if": {
            "properties": {"status": {"enum": ["TAG_ONLY", "GITHUB_RELEASED"]}},
            "required": ["status"]
          },
          "then": {
            "properties": {
              "tag_ref": {"type": "string", "pattern": "^refs/tags/[A-Za-z0-9._/-]+$"},
              "tag_object": {"$ref": "#/$defs/gitObjectId"},
              "peeled_commit": {"$ref": "#/$defs/gitCommit"}
            }
          }
        },
        {
          "if": {
            "properties": {"status": {"const": "GITHUB_RELEASED"}},
            "required": ["status"]
          },
          "then": {
            "properties": {
              "release_url": {"type": "string", "format": "uri"}
            }
          }
        }
      ]
    },
    "distributionRelease": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "distribution_repository",
        "release_tag",
        "artifact_name",
        "artifact_version",
        "artifact_digest",
        "source_commit",
        "release_url",
        "is_source_authority"
      ],
      "properties": {
        "distribution_repository": {"type": "string", "format": "uri"},
        "release_tag": {"$ref": "#/$defs/nonEmptyString"},
        "artifact_name": {"$ref": "#/$defs/nonEmptyString"},
        "artifact_version": {"$ref": "#/$defs/nonEmptyString"},
        "artifact_digest": {"$ref": "#/$defs/sha256"},
        "source_commit": {"$ref": "#/$defs/gitCommit"},
        "release_url": {"type": "string", "format": "uri"},
        "is_source_authority": {"type": "boolean", "const": false}
      }
    },
    "releaseState": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "source_repository_release_count",
        "source_release",
        "distribution_releases"
      ],
      "properties": {
        "source_repository_release_count": {"type": "integer", "minimum": 0},
        "source_release": {"$ref": "#/$defs/sourceRelease"},
        "distribution_releases": {
          "type": "array",
          "items": {"$ref": "#/$defs/distributionRelease"},
          "uniqueItems": true
        }
      }
    },
    "authority": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "authority_type",
        "canonical_object_owner",
        "program_governance_owner",
        "source_policy_status",
        "source_policy_decision_ref",
        "titmas_write_authority",
        "saee_write_authority",
        "manifest_self_authorizes"
      ],
      "properties": {
        "authority_type": {
          "type": "string",
          "const": "CANONICAL_EXISTENCE_AND_RECORD_BOUNDARY"
        },
        "canonical_object_owner": {"type": "string", "const": "DBOS"},
        "program_governance_owner": {"type": "string", "const": "DBA"},
        "source_policy_status": {
          "type": "string",
          "enum": [
            "PROPOSED_NOT_ADOPTED",
            "ADOPTED",
            "STALE",
            "CONFLICTED",
            "REVOKED"
          ]
        },
        "source_policy_decision_ref": {"$ref": "#/$defs/nullableString"},
        "titmas_write_authority": {"type": "boolean", "const": false},
        "saee_write_authority": {"type": "boolean", "const": false},
        "manifest_self_authorizes": {"type": "boolean", "const": false}
      },
      "allOf": [
        {
          "if": {
            "properties": {"source_policy_status": {"const": "ADOPTED"}},
            "required": ["source_policy_status"]
          },
          "then": {
            "properties": {
              "source_policy_decision_ref": {"$ref": "#/$defs/nonEmptyString"}
            }
          }
        }
      ]
    },
    "ownerBinding": {
      "type": "object",
      "additionalProperties": false,
      "required": ["assignment_status", "owner_ref", "scope", "authority_ref"],
      "properties": {
        "assignment_status": {
          "type": "string",
          "enum": ["ASSIGNED", "SCOPE_LIMITED", "UNASSIGNED"]
        },
        "owner_ref": {"$ref": "#/$defs/nullableString"},
        "scope": {"$ref": "#/$defs/nullableString"},
        "authority_ref": {"$ref": "#/$defs/nullableString"}
      },
      "allOf": [
        {
          "if": {
            "properties": {"assignment_status": {"const": "UNASSIGNED"}},
            "required": ["assignment_status"]
          },
          "then": {
            "properties": {
              "owner_ref": {"type": "null"},
              "authority_ref": {"type": "null"}
            }
          },
          "else": {
            "properties": {
              "owner_ref": {"$ref": "#/$defs/nonEmptyString"},
              "scope": {"$ref": "#/$defs/nonEmptyString"},
              "authority_ref": {"$ref": "#/$defs/nonEmptyString"}
            }
          }
        }
      ]
    },
    "owners": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "human_program_owner",
        "dbos_domain_owner",
        "status_manifest_owner",
        "release_authority"
      ],
      "properties": {
        "human_program_owner": {"$ref": "#/$defs/ownerBinding"},
        "dbos_domain_owner": {"$ref": "#/$defs/ownerBinding"},
        "status_manifest_owner": {"$ref": "#/$defs/ownerBinding"},
        "release_authority": {"$ref": "#/$defs/ownerBinding"}
      }
    },
    "statusAxes": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "project_lifecycle_status",
        "implementation_status",
        "release_status",
        "production_readiness_status",
        "current_gate_refs",
        "status_claim_refs",
        "unknowns"
      ],
      "properties": {
        "project_lifecycle_status": {
          "type": "string",
          "enum": ["UNKNOWN", "ACTIVE", "MAINTENANCE", "DEPRECATED", "ARCHIVED"]
        },
        "implementation_status": {
          "type": "string",
          "enum": [
            "NOT_ASSESSED",
            "SPECIFICATION_ONLY",
            "REFERENCE_IMPLEMENTATION",
            "DEVELOPER_PREVIEW",
            "BOUNDED_IMPLEMENTATION",
            "PRODUCTION_IMPLEMENTATION"
          ]
        },
        "release_status": {
          "type": "string",
          "enum": [
            "NOT_ASSESSED",
            "UNRELEASED",
            "SOURCE_TAG_ONLY",
            "DISTRIBUTION_RELEASED",
            "SOURCE_AND_DISTRIBUTION_RELEASED",
            "REVOKED",
            "CONFLICTED"
          ]
        },
        "production_readiness_status": {
          "type": "string",
          "enum": [
            "NOT_ASSESSED",
            "NOT_READY",
            "READY_FOR_HUMAN_REVIEW",
            "AUTHORIZED_FOR_NAMED_DEPLOYMENT",
            "REVOKED",
            "CONFLICTED"
          ]
        },
        "current_gate_refs": {
          "type": "array",
          "items": {"$ref": "#/$defs/nonEmptyString"},
          "uniqueItems": true
        },
        "status_claim_refs": {
          "type": "array",
          "minItems": 1,
          "items": {"$ref": "#/$defs/nonEmptyString"},
          "uniqueItems": true
        },
        "unknowns": {
          "type": "array",
          "items": {"$ref": "#/$defs/nonEmptyString"},
          "uniqueItems": true
        }
      },
      "allOf": [
        {
          "if": {
            "properties": {
              "production_readiness_status": {
                "const": "AUTHORIZED_FOR_NAMED_DEPLOYMENT"
              }
            },
            "required": ["production_readiness_status"]
          },
          "then": {
            "properties": {
              "current_gate_refs": {"minItems": 1},
              "status_claim_refs": {"minItems": 2}
            }
          }
        }
      ]
    },
    "comparedRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ref", "commit", "source_kind"],
      "properties": {
        "ref": {"$ref": "#/$defs/nonEmptyString"},
        "commit": {"$ref": "#/$defs/gitCommit"},
        "source_kind": {
          "type": "string",
          "enum": ["LIVE_REMOTE", "REMOTE_TRACKING_CACHE", "LOCAL_BRANCH", "GATED_BRANCH", "TAG"]
        }
      }
    },
    "divergence": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "classification",
        "compared_refs",
        "ahead_count",
        "behind_count",
        "blocks_status_promotion",
        "resolution_rule",
        "observed_at"
      ],
      "properties": {
        "classification": {
          "type": "string",
          "enum": [
            "IN_SYNC",
            "LOCAL_STALE_FAST_FORWARDABLE",
            "LOCAL_AHEAD_UNPUBLISHED",
            "FORKED_HISTORY",
            "GATED_BRANCH_AHEAD",
            "TAG_OR_ARTIFACT_DRIFT",
            "STATUS_MANIFEST_CONFLICT",
            "NOT_ASSESSED"
          ]
        },
        "compared_refs": {
          "type": "array",
          "minItems": 1,
          "items": {"$ref": "#/$defs/comparedRef"},
          "uniqueItems": true
        },
        "ahead_count": {"type": ["integer", "null"], "minimum": 0},
        "behind_count": {"type": ["integer", "null"], "minimum": 0},
        "blocks_status_promotion": {"type": "boolean"},
        "resolution_rule": {
          "type": "string",
          "enum": [
            "NONE",
            "MARK_LOCAL_STALE",
            "KEEP_LOCAL_UNPUBLISHED",
            "HUMAN_OWNER_DECISION_REQUIRED",
            "NEW_GATE_REVIEW_REQUIRED",
            "CRITICAL_STOP_AND_PRESERVE_HISTORY"
          ]
        },
        "observed_at": {"type": "string", "format": "date-time"}
      },
      "allOf": [
        {
          "if": {
            "properties": {
              "classification": {
                "enum": [
                  "LOCAL_AHEAD_UNPUBLISHED",
                  "FORKED_HISTORY",
                  "GATED_BRANCH_AHEAD",
                  "TAG_OR_ARTIFACT_DRIFT",
                  "STATUS_MANIFEST_CONFLICT"
                ]
              }
            },
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "blocks_status_promotion": {"const": true}
            }
          }
        },
        {
          "if": {
            "properties": {"classification": {"const": "IN_SYNC"}},
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "ahead_count": {"const": 0},
              "behind_count": {"const": 0},
              "resolution_rule": {"const": "NONE"}
            }
          }
        },
        {
          "if": {
            "properties": {"classification": {"const": "LOCAL_STALE_FAST_FORWARDABLE"}},
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "resolution_rule": {"const": "MARK_LOCAL_STALE"}
            }
          }
        },
        {
          "if": {
            "properties": {"classification": {"const": "LOCAL_AHEAD_UNPUBLISHED"}},
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "resolution_rule": {"const": "KEEP_LOCAL_UNPUBLISHED"}
            }
          }
        },
        {
          "if": {
            "properties": {"classification": {"const": "GATED_BRANCH_AHEAD"}},
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "resolution_rule": {"const": "NEW_GATE_REVIEW_REQUIRED"}
            }
          }
        },
        {
          "if": {
            "properties": {
              "classification": {
                "enum": ["FORKED_HISTORY", "STATUS_MANIFEST_CONFLICT"]
              }
            },
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "resolution_rule": {"const": "HUMAN_OWNER_DECISION_REQUIRED"}
            }
          }
        },
        {
          "if": {
            "properties": {"classification": {"const": "TAG_OR_ARTIFACT_DRIFT"}},
            "required": ["classification"]
          },
          "then": {
            "properties": {
              "resolution_rule": {"const": "CRITICAL_STOP_AND_PRESERVE_HISTORY"}
            }
          }
        }
      ]
    },
    "review": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "review_status",
        "observed_at",
        "reviewed_at",
        "reviewed_by_ref",
        "review_decision_ref",
        "freshness_window_hours",
        "next_review_due_at"
      ],
      "properties": {
        "review_status": {
          "type": "string",
          "enum": [
            "NOT_REVIEWED",
            "READY_FOR_HUMAN_DECISION",
            "REVIEWED",
            "STALE",
            "CONFLICTED"
          ]
        },
        "observed_at": {"type": "string", "format": "date-time"},
        "reviewed_at": {"type": ["string", "null"], "format": "date-time"},
        "reviewed_by_ref": {"$ref": "#/$defs/nullableString"},
        "review_decision_ref": {"$ref": "#/$defs/nullableString"},
        "freshness_window_hours": {"type": "integer", "minimum": 1},
        "next_review_due_at": {"type": ["string", "null"], "format": "date-time"}
      },
      "allOf": [
        {
          "if": {
            "properties": {"review_status": {"const": "REVIEWED"}},
            "required": ["review_status"]
          },
          "then": {
            "properties": {
              "reviewed_at": {"type": "string", "format": "date-time"},
              "reviewed_by_ref": {"$ref": "#/$defs/nonEmptyString"},
              "review_decision_ref": {"$ref": "#/$defs/nonEmptyString"}
            }
          }
        }
      ]
    },
    "zeroEffects": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "manifest_is_status_index",
        "changes_repository",
        "changes_revision",
        "creates_identity",
        "creates_capability",
        "grants_permission",
        "creates_evidence_truth",
        "creates_verification_truth",
        "authorizes_implementation",
        "authorizes_merge",
        "authorizes_release",
        "authorizes_deployment",
        "authorizes_production",
        "closes_dq_003"
      ],
      "properties": {
        "manifest_is_status_index": {"type": "boolean", "const": true},
        "changes_repository": {"type": "boolean", "const": false},
        "changes_revision": {"type": "boolean", "const": false},
        "creates_identity": {"type": "boolean", "const": false},
        "creates_capability": {"type": "boolean", "const": false},
        "grants_permission": {"type": "boolean", "const": false},
        "creates_evidence_truth": {"type": "boolean", "const": false},
        "creates_verification_truth": {"type": "boolean", "const": false},
        "authorizes_implementation": {"type": "boolean", "const": false},
        "authorizes_merge": {"type": "boolean", "const": false},
        "authorizes_release": {"type": "boolean", "const": false},
        "authorizes_deployment": {"type": "boolean", "const": false},
        "authorizes_production": {"type": "boolean", "const": false},
        "closes_dq_003": {"type": "boolean", "const": false}
      }
    }
  }
}
```

## 5. Schema Semantics（Schema 语义）

### 5.1 Source 不是自动选择结果

Schema 允许记录 exact `reviewed_commit`，但不定义如何“自动选择最新 commit”。填充流程必须：

1. 从已接受的 `canonical_repository` 读取 live remote ref；
2. 记录 ref 和 exact commit；
3. 绑定 observation timestamp（观察时间）；
4. 由有 scope 的 Owner/reviewer 确认；
5. 发现不同来源时记录 `CONFLICTED` 或 `STALE`，不得选择看起来更“新”或状态更高的一方。

`repository_url` 和 `default_branch_ref` 在提案 Schema 中写成 `const`，表示它们一旦由 ADR
采纳，就不能被 manifest author（清单作者）自行改变。改变 repository/branch 必须升级 ADR
和 Schema；这不是 Schema 自动选择 source。

### 5.2 多轴 Status（多轴状态）

禁止只使用：

```json
{"status": "reviewed"}
```

因为它无法说明被审查的是源码、release、gate、Runtime 还是 production readiness。v0.1
强制拆分：

- `project_lifecycle_status`；
- `implementation_status`；
- `release_status`；
- `production_readiness_status`；
- `current_gate_refs`；
- `status_claim_refs`；
- `unknowns`。

每个状态仍须引用 child-project evidence、Decision 或 Release Record。Schema valid 不验证引用
存在、独立性或充分性。

### 5.3 Owner 不是一个字符串

`owners` 分开：

- Human Program Owner：项目群决定；
- DBOS Domain Owner：领域与 scope 内来源；
- Status Manifest Owner：维护 manifest 的项目本地责任；
- Release Authority：特定 release 决定。

`assignment_status=UNASSIGNED` 时 `owner_ref` 和 `authority_ref` 必须为 `null`。这阻止智能体
从 GitHub repository owner、commit author、tagger、README、Domain Owner 的局部 scope 或
DBA Program Owner 自动推断 standing release authority（常设发布权）。

### 5.4 Release 与 tag 分层

`source_release` 记录 DBOS 仓库自己的 annotated tag / GitHub Release；
`distribution_releases` 记录其他仓库托管的 wheel 或 artifact。所有 distribution item 的
`is_source_authority` 恒为 `false`。

因此：

```text
PACKAGE_ARTIFACT_NE_SOURCE_AUTHORITY=true
SOURCE_TAG_NE_GITHUB_RELEASE=true
GITHUB_RELEASE_NE_RUNTIME_DEPLOYMENT=true
RELEASE_NE_PRODUCTION_AUTHORIZATION=true
```

### 5.5 Manifest zero effects（清单零效果）

`effects` 中除了 `manifest_is_status_index=true`，其余全部固定为 `false`。即使未来 manifest
记录 `production_readiness_status=AUTHORIZED_FOR_NAMED_DEPLOYMENT`，它也只能引用外部
Decision/Gate evidence，不能由自身产生授权。

## 6. Current Binding Inputs（当前绑定输入）

本表是未来 manifest 的填充输入，不是本轮创建的实际 manifest，也不自动采用这些值：

| 字段 | 当前可验证输入 | 填充限制 |
|---|---|---|
| `project_identity.project_id` | `DBOS` | 固定项目 ID |
| `canonical_source.repository_url` | `https://github.com/joy7758/digital-biosphere-os.git` | 仍需 ADR 接受 source policy |
| `canonical_source.repository_visibility` | `PRIVATE` | 观察事实；不授权改变 visibility |
| `canonical_source.default_branch_ref` | `refs/heads/main` | live remote HEAD 已核验 |
| `canonical_source.reviewed_commit` | `cd3f867c4379ec555c45e7d554088ad12ce08a24` | 当前时间点 stable source snapshot；不是永久值 |
| `release_state.source_release.status` | `TAG_ONLY` | DBOS GitHub Release count 为 0 |
| source tag | `refs/tags/v0.1-entity-infrastructure` → tag object `2685bc79…` → commit `ed73f43d…` | signature verification 为 `ABSENT` |
| distribution release | TMAI `v0.1-developer-preview` + wheel `0.1.0.dev0` | 位于 DBA 分发仓库；不是 source authority |
| `authority.authority_type` | `CANONICAL_EXISTENCE_AND_RECORD_BOUNDARY` | 不表示 repository/manifest 是 Runtime truth |
| Human Program Owner | `zhangbin` via `ADR-020` | scope 仅 Program Governance；不自动扩张 |
| DBOS Domain Owner | `zhangbin` via `DQ-018` | 当前直接证据只覆盖 DQ-018 exact slice；项目全域 scope 需明确 |
| Status Manifest Owner | `UNASSIGNED` | 必须由 DQ-003/独立 DBOS 决定指定 |
| standing Release Authority | `UNASSIGNED` | `ADR-022 released_by_ref` 只覆盖 exact Developer Preview release |
| main divergence | `LOCAL_STALE_FAST_FORWARDABLE`，ahead `0` / behind `2` | local 不覆盖 live remote |
| gated source | source `57c7b9e…` / receipt `1c8f3d9…` / live tip `d62b411…` | live tip 不自动继承旧 gate |
| review timestamp | 必须使用 future manifest 实际生成/审查时间 | 不复制本文件日期作为未来当前事实 |

## 7. Referential Validation Contract（引用验证契约）

未来验证必须分四层，不能只运行 JSON Schema：

| validation layer | 检查 | `PASS` 不表示 |
|---|---|---|
| `V1_SHAPE` | JSON、required、enum、pattern、conditional、additionalProperties | commit/tag/Owner/Decision 真实 |
| `V2_SOURCE` | live remote default branch、exact commit、ancestry、tag object/peeled commit | code quality、release 或 production |
| `V3_AUTHORITY` | decision ref、Owner scope、reviewer、release/gate source binding | Decision 已执行或 Runtime 已改变 |
| `V4_CROSS_SURFACE` | manifest vs live remote、DBA observation、gate receipt、release asset digest | child truth 被 DBA 接管 |

### 7.1 Required negative cases（必需负例）

至少覆盖：

1. abbreviated SHA、uppercase SHA、不存在 commit；
2. branch 不是完整 `refs/heads/...`；
3. local remote-tracking cache 与 live remote 冲突；
4. `README.md`、package version 或 distribution release 被声明为 source authority；
5. `TAG_ONLY` 缺 tag object / peeled commit；
6. artifact digest 与 release asset 不一致；
7. feature tip 自动替换 gated source/receipt；
8. `ADOPTED` 缺 Human Decision ref；
9. Owner 被标为 assigned 但缺 scope/authority ref；
10. `UNASSIGNED` 却填入 owner；
11. conflict classification 却设置 `blocks_status_promotion=false`；
12. `effects.authorizes_*` 或 `closes_dq_003` 被写成 `true`；
13. unknown、failure、rejected、stale 历史被删除或静默升级；
14. timestamp 过 freshness window 仍声明 current；
15. TITMAS、SAEE 或 DBA 被声明为 DBOS manifest write authority。

## 8. ADR Proposal（ADR 提案）

### 8.1 Context（背景）

DBA 当前能验证 DBOS remote `main@cd3f867…`，并已区分 local stale main、DQ-018 gated
source/receipt、source tag 与跨仓库 wheel release。但 DBOS 没有项目本地机器可读状态清单，
导致 Codex、CI 和外部贡献者需要从 README、Git、DBA snapshot、release 与 gate packet 拼接
状态，存在双重权威和语义抬升风险。

用户在本轮明确支持 `ACCEPT_WITH_MANIFEST_FOLLOWUP` 作为合理人工决策方向；但本轮直接任务
是设计审查，没有指示修改 `DECISION-QUEUE.md`、创建 DBOS manifest 或记录正式
`decided_by_ref`。因此该信号作为 ADR input（ADR 输入），不自动关闭 `DQ-003`。

### 8.2 Options（选项）

| 选项 | 说明 | 结论 |
|---|---|---|
| `A` Project-local JSON manifest + Schema | DBOS 自己维护；DBA/TITMAS 只读引用 | `RECOMMENDED` |
| `B` DBA architecture registry 作为 DBOS truth | 集中管理简单，但违反 child-project truth | `REJECT` |
| `C` 继续使用 README | 人可读但状态混合、易过期、难以失败关闭 | `REJECT` |
| `D` 每次从 Git 自动选择 latest | 省维护，但 branch tip/tag/test 不等于 adopted source | `REJECT` |
| `E` 使用 wheel/release 代表项目 | 分发友好，但 package artifact 不拥有源码/gate/Runtime truth | `REJECT` |
| `F` 复用 federation project manifest | 文件已存在，但语义是 pending membership placeholder | `REJECT` |

### 8.3 Recommended decision（建议决策）

```text
ADR_STATUS=PROPOSED_NOT_ADOPTED
DECISION_RECOMMENDATION=ADOPT_DBOS_PROJECT_LOCAL_STATUS_MANIFEST_SCHEMA_V0_1
SOURCE_POLICY_DISPOSITION=ACCEPT_WITH_MANIFEST_FOLLOWUP
MANIFEST_PATH=PROJECT-STATUS.json
SCHEMA_PATH=schemas/project-status.schema.json
MANIFEST_OWNER=DBOS
DBA_WRITE_AUTHORITY=false
TITMAS_WRITE_AUTHORITY=false
IMPLEMENTATION_AUTHORIZED=false
```

### 8.4 Decision scope（决策范围）

若接受，本 ADR 只冻结：

- manifest/schema 的角色、路径和所有权；
- required fields 与多轴 status model；
- release/source/gate 分层；
- divergence/freshness/conflict 规则；
- zero-effects 与 referential validation 要求；
- 后继 DBOS 实施必须另行授权。

它不冻结未来实际 commit 值，不自动选择 source，不指定 standing release authority，不修改
repository，不创建 validator，也不宣布 DQ-003 已实施。

### 8.5 Consequences（后果）

正面：

- AI Agent 能从一个稳定项目本地入口找到 source coordinate、Owner、status、unknowns 和
  limitations；
- DBA 不再需要复制 DBOS ledger；
- feature branch、tag、package 和 Runtime truth 保持分离；
- TITMAS 未来只需消费版本化状态索引，不取得 DBOS 写权。

代价与风险：

- manifest 需要 Owner、刷新节奏、cross-surface validator 和负例维护；
- stale manifest 可能比没有 manifest 更危险，因此必须 fail closed；
- Schema 不能证明 GitHub、Decision 或 release 引用真实，必须有 V2–V4 验证；
- source/manifest schema 变更将需要 ADR/version migration。

## 9. Adoption and Implementation Gates（采纳与实施闸门）

### Gate A — Schema design review（Schema 设计审查）

当前结果：

```text
SCHEMA_PROPOSAL_DEFINED=true
SCHEMA_PROPOSAL_JSON_PARSE_VALIDATED=true
SCHEMA_PROPOSAL_JSON_SCHEMA_2020_12_META_VALIDATED=true
REPRESENTATIVE_POSITIVE_INSTANCE_VALIDATED=true
FAIL_CLOSED_SMOKE_CASES_VALIDATED=3
HUMAN_SCHEMA_DECISION_RECORDED=false
```

这些验证仅是本设计文件的本地 QA，不采纳 Schema、不创建 validator，也不替代未来 Gate D
对真实 DBOS 文件和外部引用的独立验证。

### Gate B — Human architecture decision（人工架构决定）

必须记录：

```text
decision_result=
decided_by_ref=
decided_at=
accepted_manifest_path=
accepted_schema_path=
status_manifest_owner_ref=
implementation_authorized=false
```

### Gate C — Separate DBOS implementation authorization（独立 DBOS 实施授权）

只有 Gate B 接受后，才能单独决定是否允许 DBOS 创建：

- `PROJECT-STATUS.json`；
- `schemas/project-status.schema.json`；
- positive/negative fixtures；
- offline shape validator；
- live remote / authority / release cross-surface validator。

本文件不授权 Gate C。

### Gate D — Implementation verification（实施验证）

必须证明：

- actual files 与 accepted Schema/ADR 一致；
- current source coordinate 由 live remote 重新观察，而不是复制旧快照；
- Owner scope 和 Decision refs 可追溯；
- stale/conflicted/tag drift/forged PASS/authority elevation 负例失败关闭；
- DBOS 现有代码、registry、Evidence、release 和历史没有被清单创建动作改写。

### Gate E — DBA reference adoption（DBA 引用采纳）

DBA 只能在 Gate D 通过后：

- 把 `canonical_status_source` 指向 DBOS manifest；
- 记录 observed manifest commit/digest、freshness 和 conflict state；
- 保留 `PROGRAM_STATUS_NE_CHILD_PROJECT_TRUTH=true`；
- 处理 `DQ-003` DBOS slice 和 `B-003` 的 scoped status。

## 10. Future Refresh and Migration Rules（未来刷新与迁移规则）

1. manifest 每次更新必须与其所在 commit 一起 review；不得在文件内声称一个尚未提交的
   self commit hash；应记录被审查 source commit，并由外部 receipt 绑定 manifest commit；
2. default branch 前进不自动更新 manifest；Owner 必须重新观察 live ref、更新 timestamp 和
   status claims；
3. 超过 freshness window 时消费者必须把状态降为 `STALE`，不能继续展示为 current；
4. conflicting source 必须保留 `CONFLICTED`，不得选择更高成熟度值；
5. breaking Schema change 使用新 schema/manifest version 和 migration record；不覆盖 v0.1；
6. repository/default branch/visibility 改变需要独立 ADR，不能只编辑 JSON；
7. release/tag/artifact digest drift 进入 critical stop；不允许 retag 或静默替换；
8. DBA/TITMAS cache 只保存 observed copy/digest，永远不能回写 child manifest。

## 11. Pre-development Agent Recommendation（开发前智能体建议）

若潜在用户询问“是否推荐这一 manifest 设计作为 DBOS 机器可读项目身份与状态入口”，答案为：

```text
AGENT_RECOMMENDATION=RECOMMENDED_FOR_HUMAN_SCHEMA_REVIEW
RECOMMENDED_AS=PROJECT_LOCAL_CANONICAL_STATUS_INDEX_CONTRACT
NOT_RECOMMENDED_AS=SELF_AUTHORIZING_CONTROL_PLANE
IMPLEMENTATION_RECOMMENDED_NOW=false
MANIFEST_CREATION_AUTHORIZED=false
```

推荐原因：

- source、release、gate、owner、status、divergence 和 review 均有独立字段；
- DBOS 保留 child-project truth，DBA/TITMAS 只读；
- distribution artifact 不能取得 source authority；
- unknown/stale/conflicted 与 zero-effects 可机器检查；
- 对 AI Agent、CI 和贡献者提供单一稳定入口，而不复制 Runtime ledger。

暂不推荐创建实际文件的原因：

- Schema/ADR 尚未获得 Human Decision；
- project-wide Status Manifest Owner 尚未正式指派；
- actual commit 必须在实施时重新观察，不能复制本设计快照；
- V2–V4 referential/authority/cross-surface validation 尚未实现或授权；
- DQ-003 与实施授权必须分开。

## 12. Ordered Next Phase（下一阶段顺序）

```text
1. Human review of this Schema/ADR proposal
2. Explicit DQ-003 DBOS policy decision
3. Separate DBOS manifest implementation authorization
4. Project-local manifest/schema/negative controls
5. Independent implementation verification
6. DBA read-only source pointer adoption
7. Agent Evidence Family Ownership ADR
8. TITMAS Interface ownership crosswalk
```

第 7、8 步不能因本 Schema proposal 存在而提前开始实现。

## 13. Final Non-claims（最终非声明）

```text
DBOS_PROJECT_STATUS_SCHEMA_PROPOSED=true
DBOS_PROJECT_STATUS_SCHEMA_ADOPTED=false
DBOS_PROJECT_STATUS_SCHEMA_FILE_CREATED=false
DBOS_PROJECT_STATUS_MANIFEST_FILE_CREATED=false
DBOS_PROJECT_STATUS_VALIDATOR_CREATED=false
DBOS_STATUS_MANIFEST_OWNER_ASSIGNED=false
DBOS_SOURCE_AUTOMATICALLY_SELECTED=false
DBOS_SOURCE_REVISION_CHANGED=false
DBOS_REPOSITORY_MIGRATED=false
DBOS_DQ_003_CLOSED=false
DBOS_G1_PASSED=false
DBOS_IMPLEMENTATION_AUTHORIZED=false
DBOS_RELEASE_AUTHORIZED=false
DBOS_PRODUCTION_READY=false
TITMAS_INTERFACE_AUTHORIZED=false
```

本文件是 Architecture Governance（架构治理）下的 Schema/ADR proposal，不是实际
`PROJECT-STATUS.json`、代码、Runtime、Release、Evidence、Verification、Permission、
Certification 或 Production fact。
