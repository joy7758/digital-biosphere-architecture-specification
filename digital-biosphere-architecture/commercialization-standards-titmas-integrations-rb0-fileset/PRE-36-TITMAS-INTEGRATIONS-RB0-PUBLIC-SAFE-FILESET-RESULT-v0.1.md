# PRE-36 TITMAS Integrations RB0 Public-safe Fileset Result v0.1

## Result

```text
PRE36_RESULT=PASS_WITH_PRE37_MANIFEST_SCHEMA_GAP_RETAINED
PRE36_CANDIDATE_FILES_CREATED_IN_DBA=9
PRE36_CANDIDATE_COMMIT=3dbb37d95a2494d02af750b0fa4599d84581ede3
PRE36_EXECUTABLE_SOURCE_FILES=0
PRE36_PACKAGE_METADATA_FILES=0
PRE36_TEST_FILES=0
PRE36_TARGET_FILES_CREATED=0
PRE36_TARGET_FILES_MODIFIED=0
PRE36_NETWORK_REQUESTS_EXECUTED=0
PRE36_LIVE_MODEL_REQUESTS_EXECUTED=0
PRE36_CREDENTIAL_READS_EXECUTED=0
PRE36_LICENSE_ADOPTED=false
PRE36_REPOSITORY_BASELINE_APPLIED=false
PRE36_IMPLEMENTATION_CREATED=false
PRE36_PROVIDER_SUPPORTED=false
PRE36_CONFORMANCE_EXECUTED=false
PRE36_RELEASE_AUTHORIZED=false
```

## Validation

- exact candidate fileset: `9/9`;
- executable source files: `0`;
- package metadata files: `0`;
- test files: `0`;
- Apache License 2.0 candidate matched the local known standard text exactly;
- Apache candidate SHA-256:
  `2191d05c6ee7c145480916b745bd020484adb61653be943c43cff10bc22927a1`;
- machine entry Schema meta-valid: `true`;
- machine entry instance valid: `true`;
- implementation declaration template valid against the adopted DBA Schema:
  `true`;
- README / AGENTS / llms zero-state consistency: `true`;
- local absolute path and common secret-value pattern matches: `0`;
- target `joy7758/titmas-integrations` HEAD and dirty count unchanged.

Machine evidence:

- [validation result](pre36-rb0-fileset-validation-result.v0.1.json);
- [execution receipt](pre36-rb0-fileset-execution-receipt.v0.1.json).

## Retained gap

`PRE36-GAP-001` remains open: the exact adopted implementation declaration
template contains a relative Schema reference, but the PRE-34 target file
manifest does not include that Schema as a target file.

PRE-37 must choose one explicit resolution before target application:

1. add the exact Schema to the target application scope; or
2. adopt a self-contained stable Schema reference and revalidate the template.

Therefore:

```text
PRE37_EXACT_FILESET_REVIEW_READY=true
TARGET_APPLICATION_READY=false
LICENSE_ADOPTION_READY=false
```

## Boundary

The result proves only that the nine DBA candidates are public-safe and
internally consistent for the stated checks. It does not adopt a license,
modify the target repository, create an implementation, support a provider,
execute conformance, pass `CS-G0`, authorize a commercial offering,
certification or release.
