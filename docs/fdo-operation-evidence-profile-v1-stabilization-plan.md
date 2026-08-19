---
title: TITMAS FDO Operation Evidence Profile v1 stabilization plan
status: DESIGN_ONLY_WAITING_FOR_HUMAN_APPROVAL
historical_record: 21.T11966/fdo-operation-evidence-profile-v0-1
schema_semantic_change_approved: false
implementation_approved: false
---

# TITMAS FDO Operation Evidence Profile v1 stabilization plan

## Outcome and boundary

This program designs a separate **TITMAS Operation Evidence Profile v1.0
candidate** while preserving
`21.T11966/fdo-operation-evidence-profile-v0-1` as immutable historical
experimental evidence. It does not rewrite, alias, redirect, or silently
upgrade v0.1.

The candidate name, public repository, licence, schema identity, DTR PID, and
release authority remain provisional until explicit human decisions. The word
“candidate” does not claim official FDO standardization, adoption,
endorsement, certification, conformance, or production readiness.

```text
V0_1_ROLE=IMMUTABLE_HISTORICAL_EXPERIMENTAL
V1_PATH=SEPARATE_TITMAS_CANDIDATE_LINEAGE
SCHEMA_SEMANTIC_CHANGE_APPROVED=false
IMPLEMENTATION_APPROVED=false
```

## 1. Normative scope

The v1.0 candidate should define one implementation-neutral JSON
accountability statement for **one completed or failed, policy-constrained
operation** performed by an agent or service. Its normative contract should
cover only:

- unambiguous profile/version identification;
- statement identity and emission time;
- the executing actor and primary subject;
- the operation, declared result, governing policy, and concrete constraints;
- input/output references and provenance closure;
- evidence references/artifacts and their integrity digests;
- a validation assertion whose status and limits are explicit;
- deterministic serialization/digest inputs;
- syntactic, reference-closure, consistency, and integrity validation rules;
- producer and validator obligations, deterministic diagnostics, and resource
  safety needed for cross-implementation testing.

Every normative requirement should have a stable ID such as `OE1-REQ-001`.
The JSON Schema governs machine-checkable structure; the prose specification
governs semantic requirements that JSON Schema cannot express. A conflict
between them blocks release rather than being resolved by an undocumented
precedence guess.

The program must explicitly decide whether a denied or attempted operation
that never executed is within scope. v0.1 describes an executed operation and
enumerates `succeeded`/`failed`; v1 must not broaden “one operation” by
accident.

## 2. Non-goals

The v1.0 candidate must not claim to define or provide:

- an agent runtime, workflow engine, orchestrator, registry, or governance
  platform;
- authentication, authorization, policy decision/enforcement, key management,
  or revocation;
- truth, correctness, trustworthiness, legal non-repudiation, or causal proof
  of the referenced evidence;
- a complete cryptographic trust fabric, signature format, transparency log,
  or long-term archival system;
- transport, storage, resolver, discovery, user interface, or billing
  protocols except where an identifier format is needed by the profile;
- a general event/provenance model for multiple operations or a substitute for
  domain standards;
- automatic compatibility with v0.1 or any demo record;
- official FDO adoption, certification, production safety, or regulatory
  compliance.

Evidence validation means that the supplied document satisfies the declared
contract and digest/link rules. `EVIDENCE_NE_TRUTH` and
`CONFORMANCE_NE_DEPLOYMENT_AUTHORIZATION` remain explicit claims boundaries.

## 3. Historical v0.1 preservation baseline

The current preservation candidate is the observed `agent-evidence`
`origin/main` revision:

```text
git_commit=09385f47a33273d8c72bbca9d3ae57aff0d5c0d9
spec_path=spec/execution-evidence-operation-accountability-profile-v0.1.md
spec_sha256=ba8fb0ae317d1474c60d7f77b8e8da1fab0eccb447213e2b669fe9e30413cd0e
schema_path=schema/execution-evidence-operation-accountability-profile-v0.1.schema.json
schema_sha256=cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8
installable_schema_path=agent_evidence/schema/execution-evidence-operation-accountability-profile-v0.1.schema.json
installable_schema_sha256=cadff8c3b30a47f58563fa8700bcb2aa962338bc68336907d4f228e9b2387ea8
```

These are locally verified source observations, not hashes asserted by the
current DTR record. Before archival, a human owner must confirm that this
revision is the authoritative v0.1 baseline and approve its disclosure.

Two annotated tags, `eeoap-v0.1-artifact` and `eeoap-v0.1-paper`, exist only in
the inspected local clone and dereference to commit
`96f444b7ed39b39fe9f47e428af835952e843cb0`, where the same spec/schema bytes
were observed. No matching remote tags were returned by `git ls-remote` during
this audit. They are therefore local history, **not** a public immutable anchor
or evidence of a published release.

The approved archive should contain exact bytes, file lengths, SHA-256 values,
the repository revision, a manifest, licence, citation, lifecycle statement,
and a note that v0.1 leaves canonical-digest details insufficiently specified.
No formatter, line-ending conversion, schema `$id` repair, or prose correction
may alter the historical files. Explanatory errata must be separate,
non-normative documents.

## 3A. Known v0.1 semantic and implementation gaps

These observations are inputs to v1 design. They must not be repaired in the
historical v0.1 record:

- the specification says “canonical digest” but does not name a canonical JSON
  algorithm; the observed Python function uses
  `json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=True)`,
  which is not a declaration of RFC 8785/JCS;
- the schema declares `format: date-time`, while the observed validator builds
  `Draft202012Validator(schema)` without a `FormatChecker`; current Python
  validation therefore does not establish date-time format assertion;
- duplicate checks cover constraint and evidence-reference identifiers, not a
  documented global identifier-uniqueness rule;
- provenance input/output references are compared to operation references as
  ordered lists; JSON canonicalization does not sort arrays, so v1 must decide
  list versus set, duplicate, order, and digest semantics for every array;
- `validation.status=verifiable|unverifiable` is a statement embedded in the
  object, not proof. A v1 validator must recompute results and issue a separate
  receipt;
- existing repo-local checkers are not an independent TypeScript
  implementation. Python-versus-Python comparison is development evidence
  only;
- observed scenario disagreements around temporal consistency,
  implementation-coupled evidence, ambiguous operation semantics, and outcome
  verifiability show that current passing behavior is not a v1 semantic oracle.

The v1 normative package must pin JSON Schema dialect, meta-schema, format
assertion mode, reference rules, array semantics, identifier uniqueness,
canonicalization, digest inputs, error precedence, and receipt meaning before
RC.

## 4. Canonical source and immutable revision strategy

### v0.1

- Keep the DTR PID, payload, semantics, and source history unchanged.
- After disclosure approval, publish or archive exact approved bytes in a
  content-addressed bundle; an immutable commit, signed release, and archival
  DOI are options, not current facts.
- If future governance approves a relationship, add a non-destructive
  `isPredecessorOf`/`isSuccessorOf` relationship without redirecting v0.1 or
  changing its content.
- Never use the v0.1 PID as an alias for the v1 candidate.

### v1 candidate

- Select one public canonical specification repository or archival source by
  human decision. Private development may feed it only through a
  disclosure-reviewed export.
- Pin every RC/stable artifact to a full commit and immutable tag/release.
- Generate `artifact-manifest.json` with spec/schema/corpus/tool version,
  file length, SHA-256, licence, authorship, lifecycle, and relationship data.
- Require reproducible release archives and an independent hash reproduction.
- Keep mutable `main` URLs for navigation only; citations and DTR bindings use
  immutable release/archive URLs and content hashes.

The canonical public source defines the open contract. Proprietary
implementations may remain private and are not canonical specification
sources.

## 5. Schema and versioning policy

The v1 design phase must resolve and test the following before RC:

1. Use JSON Schema 2020-12 with a new, durable canonical `$id`; never reuse the
   v0.1 `example.com` identity.
2. Use a distinct profile name/identity and an explicit semantic version. RC
   identifiers such as `1.0.0-rc.1` must not validate as stable `1.0.0` unless
   a deliberate schema rule says so.
3. Specify JSON parsing constraints, including duplicate-key rejection,
   Unicode handling, numeric bounds, maximum sizes/depth/counts, and date-time
   interpretation.
4. Normatively define canonical bytes for digests. Evaluate RFC 8785 JSON
   Canonicalization Scheme (JCS) against the domain requirements and both
   implementations; adopt it only after fixtures prove identical output.
5. Define the exact statement-core selection, ordering behavior for arrays,
   digest prefix/case, and whether locators or validation fields are included.
6. Retain closed-world validation where it supports interoperability. If
   extensions are permitted, use a namespaced, explicitly governed extension
   point rather than unconstrained top-level fields.
7. Define URI/identifier, digest, date-time, actor/subject/result, reference
   uniqueness, and reference-closure semantics in requirement-ID form.
8. Validate offline by default. A locator is data, not permission for a
   validator to fetch a network resource.

Version policy:

- patch releases correct non-semantic documentation or implementation defects
  and do not change valid/invalid instance sets;
- minor releases may add backward-compatible optional capability only when old
  validators can safely reject or ignore it under an explicit extension rule;
- any required-field, field-meaning, canonicalization, digest-input, enum, or
  validation-outcome change is breaking and requires a new major version;
- every release contains a normative changelog and machine-readable
  compatibility declaration;
- registry version, schema version, specification version, implementation
  version, and corpus version remain separate identifiers.

## 6. Compatibility and deprecation policy

- v0.1 remains retrievable and valid only against its own exact contract. A v1
  validator must report `UNSUPPORTED_PROFILE_VERSION` rather than reinterpret
  a v0.1 document.
- A migration/bridge tool may read v0.1 and emit a **new** v1 candidate
  document plus a transformation report. It must not mutate the source, claim
  lossless conversion without proof, or assert v1 conformance until the output
  independently validates.
- Compatibility claims require corpus evidence in both implementations, not
  version-number comparison.
- A deprecated field remains documented through a defined minimum support
  window and must name its replacement. Removal waits for the next major
  version.
- The historical v0.1 record is not automatically labelled deprecated or
  superseded. A future non-destructive lifecycle relationship requires a
  separate owner decision.

## 7. Positive and negative conformance corpus

Every fixture must be synthetic, licence-cleared, privacy-reviewed, immutable,
and accompanied by an expected result. Negative fixtures should isolate one
primary failure where practical. Corpus cases receive stable IDs.

### Positive corpus

| Case family | Required coverage |
|---|---|
| Minimal success | One actor, one subject, one input, one output, one policy/constraint, correct digests |
| Declared operation failure | Structurally valid failed operation, proving operation failure is not profile-validation failure |
| Multiple references/artifacts | Stable order/canonicalization and complete input/output role closure |
| Identifier/locator diversity | URI, PID/URN, opaque identifier, and non-network locator values without dereferencing |
| Unicode and time | Approved Unicode normalization behavior, offsets, UTC canonical representation, and boundary timestamps |
| Extension case | Only if an extension mechanism is approved; known namespace with deterministic handling |
| Cross-version detection | Exact v0.1 input produces `UNSUPPORTED_PROFILE_VERSION`, not a v1 success |

### Negative corpus

| Failure family | Examples |
|---|---|
| JSON/parser | Duplicate keys, invalid UTF-8, excessive depth/size, non-finite/unsafe numbers, trailing data |
| Schema | Missing required field, extra top-level property, wrong type/enum/pattern, invalid timestamp |
| Identity | Wrong profile name/version, duplicate local identifiers, empty IDs |
| Closure/role | Unresolved reference, input pointing to output role, missing constraint, mismatched subject/policy/provenance |
| Integrity | Altered reference/artifact/core, uppercase/wrong-length digest, array reordering, wrong canonical bytes |
| Validation assertion | Wrong evidence/provenance/policy link, contradictory or unknown status, validator self-claim without required result |
| Locator safety | File/network locator that must remain inert, credential-like URL, path traversal string, very long locator |
| Version/extension | v0.1 presented as v1, unknown extension, future minor/major version, collision with reserved namespace |

Each expected-result file should include `case_id`, expected validity,
validation stages, stable error codes, JSON Pointers, and applicable normative
requirement IDs. It should also include exact fixture-byte SHA-256, ordered
primary error code, complete normalized error-code set, expected canonical
bytes/digest where applicable, and resolver-manifest hash. Single-fault cases
test rule isolation; separate multi-fault cases test deterministic precedence.
Diagnostic prose may evolve; codes and requirement mappings are the
interoperability contract.

## 8. Python producer and validator

After implementation approval, the Python implementation should provide:

- typed producer API and CLI that emits deterministic v1 candidate JSON;
- validator API and CLI with stages for parse/schema, identity, reference
  closure, semantic consistency, canonicalization, and integrity;
- fail-fast and aggregate modes with the same underlying results;
- offline/no-fetch default and explicit resource limits;
- deterministic JSON validation reports with implementation name/version,
  schema/corpus hashes, error codes, JSON Pointers, and requirement IDs;
- package/source/release provenance, SBOM, licence, security policy, and
  reproducible installation;
- unit, property, mutation, fuzz, and full corpus tests.

Existing v0.1 code is research input, not automatic v1 conformance evidence.
The v1 implementation must not reuse an underspecified Python
`json.dumps(...)` behavior as a cross-language canonicalization standard.

## 9. Independent TypeScript producer and validator

The TypeScript implementation should be built by a different primary
implementer or cleanly separated workstream using only the public normative
specification, schema, and corpus—not Python source logic. It should provide
equivalent producer/validator/CLI/report capabilities on pinned supported Node
and TypeScript versions.

Independence means no shared canonicalization or validation implementation.
Third-party JSON Schema and JCS libraries may be used only after their versions,
edge behavior, licences, and corpus results are recorded. Disagreement reveals
a specification/test defect; Python output is not the oracle merely because it
was written first.

Neither implementation may wrap, import, subprocess, or call the other over
HTTP, share a generated validator core, or consume the other's verdict as an
oracle. They may share only the exact immutable normative specification,
schema, corpus, and golden vectors, and should have different primary owners,
toolchains, and review paths.

## 10. Cross-implementation test matrix

| Producer/input | Python validator | TypeScript validator | Required comparison |
|---|---|---|---|
| Python producer | Pass all positive cases | Pass all positive cases | Canonical bytes, digests, parsed semantics, result codes |
| TypeScript producer | Pass all positive cases | Pass all positive cases | Same |
| Hand-authored positive corpus | Pass | Pass | Identical validity and normative outcomes |
| Hand-authored negative corpus | Reject | Reject | Same primary error code/stage/requirement; allowed diagnostic-text differences documented |
| v0.1 historical fixtures | Reject as unsupported v1 | Reject as unsupported v1 | No silent upgrade |
| Mutation/fuzz corpus | No crash/hang/unauthorized fetch | No crash/hang/unauthorized fetch | Resource-limit and divergence report |
| Round-trip/metamorphic cases | Preserve defined semantics | Preserve defined semantics | No digest drift under allowed serialization changes |

Run the matrix on at least Linux and macOS, pinned Python/Node versions, and
both release archives. Any validity, canonical-byte, digest, or normative-code
disagreement blocks RC. Maintain a divergence ledger even when the defect is
in the specification or corpus rather than either implementation.
Network access should be physically disabled in the offline-validation jobs,
and repeated runs must demonstrate deterministic results.

## 11. Release-candidate gates

All gates are required:

- `RC-GOV`: owner, editor, maintainer, decision process, contribution policy,
  conflict policy, licence, and claims language approved.
- `RC-SCOPE`: every normative requirement and non-goal reviewed; no unresolved
  semantic contradiction.
- `RC-SOURCE`: public canonical source and reproducible immutable archive with
  hashes; no private URL is the only verification route.
- `RC-SCHEMA`: new durable identity, meta-schema validation, examples and prose
  aligned; exact v0.1 remains untouched.
- `RC-CANON`: canonicalization/digest rules pass every edge fixture in both
  implementations.
- `RC-CORPUS`: positive/negative corpus complete, privacy/licence-reviewed, and
  immutable.
- `RC-IMPL`: independent Python and TypeScript producers/validators published
  or otherwise available for reproducible review under approved disclosure
  terms.
- `RC-INTEROP`: full matrix has no unexplained divergence.
- `RC-SEC`: threat model, dependency/security review, fuzz/resource-limit
  evidence, disclosure policy, and no-network default verified.
- `RC-CITE`: record/spec/schema/software citations and authorship/provenance
  manifests complete.
- `RC-AGENT`: machine-readable entrypoint, version/lifecycle, use/non-use
  rules, commands, error catalogue, and claims boundaries tested with coding
  and retrieval agents.
- `RC-DTR`: registration proposal is draft/experimental, class-correct, and
  separately approved; no stable/adoption claim.

## 12. Stable-release gates

RC passage is necessary but not sufficient. Stable release additionally
requires:

- an immutable 1.0.0 specification/schema/corpus release set with reproduced
  hashes;
- two independent implementation teams and zero unexplained cross-matrix
  divergence across the support matrix;
- an independent third party has reproduced the exact release matrix from the
  public artifacts; reproduction is not automatically adoption;
- independent technical, security, governance, accessibility, and citation
  review with all blocking findings closed;
- mutation/fuzz/resource-limit thresholds defined in advance and met;
- reproducible release archives, SBOMs, provenance attestations, and archival
  identifiers actually minted and verified;
- a compatibility/deprecation policy and maintenance capacity with named
  owners and response expectations;
- at least two disclosed, independent pilot contexts or equivalent external
  reproduction evidence; pilots do not equal adoption;
- an adoption/feedback report that records failures and non-adoption as well as
  successes;
- resolved DTR class/lifecycle/relationship semantics and a separate human
  decision on stable registration or lifecycle transition;
- claim-by-claim approval of the release announcement. No claim of official
  FDO adoption, certification, or production fitness may be inferred.

## 13. DTR registration strategy

1. Migrate the existing v0.1 PID only as `FdoProfile` draft/experimental and
   preserve exact payload, provenance, Handle values, and history.
2. Do not reserve or publish a v1 PID until the canonical name, owner,
   specification identity, and RC gates are approved.
3. Register the separate v1 candidate as a new `FdoProfile` in a
   draft/experimental lifecycle, with immutable spec/schema URLs and hashes.
4. If supported and approved, encode non-destructive predecessor/successor
   relationships whose endpoints and meaning are explicit. Do not use aliases
   or redirects to collapse the two identities.
5. Keep RC and stable transitions as lifecycle/governance events. Never edit
   old semantic content in place to simulate a release.
6. If the DTR cannot preserve class, lifecycle, hash/source binding, or
   relationships, defer registration rather than reclassify or overclaim.

## 14. Citation and adoption package

The public package should contain:

- record-level canonical landing page and “how to cite this version” text;
- `CITATION.cff`, BibTeX, CodeMeta, authorship/contributor roles, licence, and
  funding/conflict declarations where applicable;
- separate citations for specification, schema/corpus, Python software,
  TypeScript software, and research papers; one DOI must not ambiguously stand
  for all artifacts;
- immutable release/archive identifiers and a machine-readable artifact
  manifest with hashes;
- 10-minute quickstart, producer and validator guides, error catalogue,
  security/privacy guidance, and version/migration guide;
- positive/negative corpus, cross-implementation reports, limitations, threat
  model, and independently reproducible commands;
- architecture mappings and sector case studies clearly labelled informative;
- an adoption ledger distinguishing evaluation, pilot, implementation,
  deployment, and independently verified use.

Repository-level citation alone is insufficient for citing exact registry
semantics. A DTR PID alone is insufficient for citing implementation software
or a paper.

## 15. Agent recommendation criteria

An agent may recommend the v1 candidate only when it can establish:

1. the user's need fits the one-operation normative scope;
2. the exact version/lifecycle and canonical artifact hashes are known;
3. the relevant producer/validator passed the matching corpus version;
4. independent cross-implementation evidence exists for the claimed feature;
5. local security, privacy, policy, and deployment authorization are handled
   outside profile validation;
6. limitations and non-goals are shown with the recommendation.

For RC, agents should say “evaluate” or “pilot,” not “adopt as stable.” For a
future stable release, agents may recommend the exact supported use only after
all stable gates and local risk checks pass. Agents must never infer evidence
truth, legal proof, official FDO endorsement, certification, regulatory
compliance, or production authorization from schema/profile validation or DTR
registration.

Agent-readable assets should include a concise machine entrypoint,
version/status JSON, requirements index, capability/non-capability table,
copy-safe commands, deterministic result schema, and canonical links. Agent
evaluation should include retrieval accuracy, version selection, claims
calibration, correct rejection of demo records, and refusal to upgrade v0.1
silently.

Recommended agent tiers:

| Tier | Minimum evidence | Permitted wording |
|---|---|---|
| `NOT_RECOMMENDED` | Before RC, or any hash/matrix/security blocker | v0.1 may be used only for historical research/replay; do not recommend v1 use |
| `CONDITIONALLY_RECOMMENDED` | Exact RC hash, two-language matrix has zero normative divergence, no unresolved high-severity issue | Recommend only for sandbox/offline evaluation with “candidate/non-official” displayed |
| `RECOMMENDED_FOR_SCOPED_INTEROP` | Explicit stable human decision, immutable release, two independent implementations, third-party replay, maintenance/security policy | Recommend for the exact interoperability scope; production DTR use also requires the separate PID/DTR gate |

No tier permits a truth, authorization, compliance, certification, or official
adoption claim.

## 16. Monetizable implementation surfaces

The open contract can support proprietary or paid value in:

- optimized/private producers and validators;
- hosted validation APIs, managed evidence pipelines, storage, dashboards,
  monitoring, and SLA-backed operations;
- enterprise connectors, sector mappings, migration/bridge tooling, and
  customer-specific policy integration;
- security hardening, deployment engineering, support, training, and
  implementation audits;
- paid execution of the public test suite and private assessment reports,
  clearly distinguished from official certification;
- reference environments and sanitized demonstrations with support guarantees.

Commercial claims must attach to the vendor implementation/service, not imply
exclusive ownership of the open specification. Third parties remain free to
build competing implementations under the approved open-artifact licence.
TITMAS must not sell official FDO status, PID control, certification authority,
or production guarantees it has not been granted.

## 17. Privacy-preserving public verification milestone

To answer the need for a partially developed verification surface while
preserving closed-source repositories, the first implementation milestone
after approval should be deliberately small:

`PVS-0 — Historical identity and runner skeleton`

- publish an approved v0.1 historical manifest with exact paths, revision,
  hashes, lifecycle, citation, and non-goals;
- publish three synthetic, non-sensitive cases: one valid statement, one
  unresolved reference, and one digest mismatch, with expected results;
- publish an implementation-neutral result schema and requirement/error IDs;
- provide either a minimal offline verification runner or a thin client for a
  documented validation API, depending on the approved disclosure model;
- run it in clean CI and publish a hashed result bundle;
- disclose no private repository structure, proprietary algorithm, secret,
  credential, customer data, or internal operational evidence.

`PVS-0` verifies packaging, hashing, privacy review, and reproducibility. It
does **not** create v1 semantics, prove independent interoperability, or make
v0.1 production-ready. Implementation remains blocked until the human choices
below are resolved.

## 18. Program work packages

| Work package | Deliverable | Entry gate | Exit evidence |
|---|---|---|---|
| `WP0` Historical preservation | Approved v0.1 archive manifest and errata boundary | Owner/disclosure approval | Independent hash reproduction |
| `WP1` Governance/scope | Charter, normative requirements, non-goals, threat model | Named editors/owners | Governance and scope review |
| `WP2` Public verification | `PVS-0`, canonical public host, citation/licence | Public repo/disclosure decision | Anonymous retrieval, clean CI, hashed results |
| `WP3` v1 schema/spec | New draft identity and aligned normative artifacts | Semantic-change authorization for new lineage | Spec/schema/corpus consistency report |
| `WP4` Python | Independent producer/validator | Implementation approval | Package, tests, provenance, corpus results |
| `WP5` TypeScript | Cleanly independent producer/validator | Public normative draft | Package, tests, provenance, corpus results |
| `WP6` Interoperability | Cross-implementation matrix and divergence ledger | WP3–WP5 ready | Zero unexplained divergence |
| `WP7` RC/adoption | RC archive, DTR draft proposal, pilots, citations | All RC gates | Human RC decision |
| `WP8` Stable candidate | Stable evidence and claims package | Stable gates complete | Separate human release/DTR decisions |

## 19. Unresolved decisions

Before any implementation, a human must decide:

1. the canonical public repository/archive and whether it is a new dedicated
   repository rather than either private development repository;
2. the exact bytes approved for public disclosure and the licence for the
   specification, schema, corpus, and runner/client;
3. the named profile owner, editors, maintainers, security contact, and release
   authority;
4. whether `PVS-0` publishes validator logic or only a thin open client and
   reproducible result bundle for a proprietary service;
5. the new v1 candidate name, identifier namespace, `$id`, extension policy,
   canonicalization algorithm, and normative requirement set;
6. acceptable Python/Node support matrices, independence criteria, security
   thresholds, and pilot evidence;
7. whether and when a new DTR PID may be requested, and which relationship
   vocabulary GWDG can preserve;
8. the boundary between a paid private assessment and any future use of the
   word “conformance”; certification remains out of scope.

## Program status

```text
FLAGSHIP_V1_STABILIZATION_PLAN_READY=true
V0_1_REWRITTEN=false
PUBLIC_VERIFICATION_SLICE_DESIGNED=true
PUBLIC_VERIFICATION_SLICE_IMPLEMENTED=false
EXTERNAL_ACTION_TAKEN=false
SCHEMA_CHANGED=false
STATUS=WAITING_FOR_HUMAN_APPROVAL
```
