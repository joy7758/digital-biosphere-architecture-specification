# PRE-37 RB0 Target Mapping and Template Schema Gap Review Result v0.1

## Result

```text
PRE37_RESULT=PASS_PRE38_HUMAN_DECISION_REVIEW_READY_NOT_AUTHORIZED
PRE37_PLANNING_COMMIT=b29213e29f3a62749d35f65c243ae3abd21b9ddd
PRE37_TARGET_PATHS_MAPPED=10
PRE37_MANIFEST_SOURCE_DIGESTS_MATCH=10
PRE37_SCHEMA_REFERENCES_RESOLVED=2
PRE37_PATH_COLLISIONS=0
PRE37_PATH_TRAVERSAL=0
PRE37_EXTERNAL_REPOSITORY_MODIFICATIONS=0
PRE37_NETWORK_REQUESTS=0
PRE37_LIVE_MODEL_REQUESTS=0
PRE37_CREDENTIAL_READS=0
PRE38_HUMAN_DECISION_REVIEW_READY=true
PRE38_DECISION_RECORDED=false
LICENSE_ADOPTED=false
TARGET_MODIFICATION_AUTHORIZED=false
TARGET_APPLICATION_EXECUTED=false
```

## Gap resolution

PRE-37 比较了三条路径：

1. 原 recommendation Option A 把 Schema 放在 `schemas/`：拒绝，因为 template 的
   `./implementation-declaration-template.schema.v0.1.json` 不会解析到该目录；
2. corrected Option A 把 exact Schema 放在仓库根目录：推荐，因为相对引用可解析且
   PRE-35 adopted template bytes/digest 不变；
3. Option B 修改 template reference：只有建立新 template revision、Schema revision 和
   adoption Decision 后才有效。

推荐候选：

```text
RECOMMENDED_GAP_RESOLUTION=A_CORRECTED_ROOT_RELATIVE_PATH
SCHEMA_TARGET_PATH=implementation-declaration-template.schema.v0.1.json
TARGET_FILE_COUNT=10
TEMPLATE_BYTES_CHANGED=false
ADOPTED_TEMPLATE_DIGEST_PRESERVED=true
RESOLUTION_ADOPTED=false
```

## Validated planning packet

- [candidate-to-target mapping](candidate-to-target-mapping.v0.1.json)；
- [Schema gap matrix](schema-gap-options-matrix.v0.1.json)；
- [revised manifest candidate](revised-target-file-manifest.v0.2.json)；
- [license decision input](license-adoption-decision-input.v0.1.json)；
- [target application plan](target-application-plan-candidate.v0.1.json)；
- [rollback plan](rollback-plan-candidate.v0.1.json)；
- [PRE-38 packet](pre38-decision-packet.v0.1.json)；
- [machine validation result](pre37-offline-validation-result.v0.1.json)；
- [execution receipt](pre37-execution-receipt.v0.1.json)。

## Boundary

PRE-37 只完成离线审查和 PRE-38 决策准备。它没有采纳 license、修改 target、应用 RB0、
创建 package/source/tests/runtime、支持 provider、执行 conformance、通过 `CS-G0`、
授权商业 Offering、Certification 或 Release。
