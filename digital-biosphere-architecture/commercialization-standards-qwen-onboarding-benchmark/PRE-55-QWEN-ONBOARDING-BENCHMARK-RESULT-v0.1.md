# PRE-55 Qwen Onboarding Benchmark Result v0.1

```text
RESULT=FAIL_CLOSED_MODEL_NOT_FOUND
PROVIDER=ALIBABA_CLOUD_MODEL_STUDIO
MODEL=qwen3.7-plus-2026-05-26
REQUESTS_AUTHORIZED=3
REQUESTS_EXECUTED=1
REQUESTS_PASSED=0
REQUESTS_FAILED=1
REQUESTS_NOT_EXECUTED_FAIL_CLOSED=2
HTTP_STATUS=404
PROVIDER_ERROR_CODE=model_not_found
PROVIDER_ERROR_MESSAGE_CLASS=MODEL_NOT_EXIST
RETRY_FALLBACK_SUBSTITUTION_EXTRACTION_REPAIR=0
CREDENTIAL_VALUE_RECORDED=false
```

## Direct Result

`QWEN-ONBOARD-01` reached the user-provided endpoint and received a parseable outer JSON error with
HTTP 404. The Provider classified the exact requested model as `model_not_found`.

The frozen prerequisite rule then prevented `QWEN-ONBOARD-02` and `QWEN-ONBOARD-03` from being sent.
No retry, fallback, model substitution, alias inference, response extraction or JSON repair was
attempted.

This result proves only that the exact binding below did not pass at the observed time:

```text
USER_PROVIDED_BASE_URL
  + qwen3.7-plus-2026-05-26
  → FAIL_CLOSED_MODEL_NOT_FOUND
```

It does not prove that the credential is invalid, that the endpoint is unusable, or that Alibaba
Cloud Model Studio lacks a suitable model. Authentication validity remains `NOT_PROVEN` because the
request did not reach a successful inference response.

## Security and Secret Boundary

```text
SECRET_FILE_GIT_IGNORED=true
SECRET_FILE_MODE=600
CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
CREDENTIAL_VALUE_IN_PACKET=false
CREDENTIAL_VALUE_IN_GIT=false
CREDENTIAL_VALUE_IN_VALIDATION_OUTPUT=false
RAW_RESPONSE_IN_GIT=false
```

Only sanitized status, hashes and the Provider's non-secret error classification are retained.

## Next Action

```text
NEXT_ACTION=FORM_EXACT_READ_ONLY_MODEL_DISCOVERY_RECOMMENDATION
MODEL_DISCOVERY_AUTHORIZED=false
QWEN_ONBOARDING_RETRY_AUTHORIZED=false
MODEL_SUBSTITUTION_AUTHORIZED=false
```

A future bounded discovery may query the exact endpoint's OpenAI-compatible `/models` surface once,
retain only public-safe model identifiers, and then form a new exact-model benchmark
Recommendation. It must not reinterpret this failed PRE-55 request or silently substitute a model.

## Non-Effects

```text
PROVIDER_CONNECTED=false
PROVIDER_DIRECTLY_TESTED_SUCCESSFULLY=false
PROVIDER_INTEGRATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
SECURITY_REVIEW_AUTHORIZED=false
SECURITY_REVIEW_COMPLETED=false
IMPLEMENTATION_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

