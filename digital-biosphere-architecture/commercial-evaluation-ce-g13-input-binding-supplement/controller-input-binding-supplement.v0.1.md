# CE-G13 Controller Input Binding Supplement v0.1

## Status

`FROZEN_CANDIDATE_NOT_VALIDATED_NOT_AUTHORIZED_NOT_EXECUTED`

This document supplements
`commercial-evaluation-ce-g13-offline-contract/controller-procedure.v0.1.md`. It is a
non-executable contract.

## Immutable base

The 28-file base package must continue to match:

```text
DIRECTORY=commercial-evaluation-ce-g13-offline-contract
PACKAGE_MANIFEST_SHA256=be7b0db4f0f349f8898f749e8ee0f4bd6a3407c79acbe33b415da081ff9ea9ed
BASE_PACKAGE_MUTATION_ALLOWED=false
```

## Future input-binding sequence

Only a later Human Decision may authorize this sequence:

1. verify the immutable base and validated supplement digests;
2. retrieve at most 16 same-origin resources within 3,000,000 decoded entity-body bytes;
3. request `Accept-Encoding: identity` and reject encoded bodies;
4. preserve raw decoded entity-body hashes and byte counts;
5. apply the frozen sanitization profile without dynamic or model-generated rewriting;
6. persist the exact UTF-8 sanitized text and its byte hash in one public input bundle;
7. assemble each role request from ordered, hash-bound components;
8. persist the secret-free exact request JSON before the Provider call;
9. make one exact `qwen3.7-max` request per role with no retry or fallback;
10. persist direct response JSON, request capture and every failure;
11. emit exactly the 26 future output files declared by the output-manifest template.

## Exact byte rules

- `raw_body_sha256`: SHA-256 over HTTP decoded entity-body bytes received with
  `Accept-Encoding: identity`.
- `sanitized_text_sha256`: SHA-256 over the UTF-8 bytes of the persisted `sanitized_text` JSON
  value after JSON decoding.
- `sanitized_request_payload_sha256`: SHA-256 over the UTF-8 bytes of the persisted exact,
  secret-free request JSON string after JSON decoding.
- file hashes: SHA-256 over exact persisted file bytes with no post-hash formatting.
- a hash is never recomputed from a semantically equivalent reserialization.

## Role input order

```text
S01 = ROOT_SEED, CUSTOMER_PROBLEM, ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE
S02 = ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE
S03 = ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE
S04 = ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE, VALIDATED_REUSE_PLAN
S05 = ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE,
      S01_RESPONSE, S02_RESPONSE, S03_RESPONSE, S04_RESPONSE
```

S04 and S05 consume persisted result files, not conversation state. No role receives hidden local
files, private repositories, search results, unbound summaries or a prior model conversation.

## Stop conditions

Fail closed before the next side effect on:

- non-identity content encoding;
- unsupported MIME or invalid strict UTF-8;
- forbidden control characters or secret-bearing material;
- same-origin, redirect, request-count or byte-budget violation;
- missing, repeated, reordered or hash-mismatched input component;
- requested or returned model other than `qwen3.7-max`;
- non-direct JSON, Schema failure, retry, fallback, substitution, extraction or repair;
- extra, missing, renamed, changed or self-hashed output;
- failure deletion or overwrite.

This candidate creates no Runtime, Agent, Entity, Capability, Permission or Evidence Truth.
