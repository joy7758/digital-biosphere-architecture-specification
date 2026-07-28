# TITMAS Agent-Native Standards Community v1.1 Human Decision Packet

All decisions below are `UNDECIDED`. `recommended_disposition` is advisory and
does not execute the action. Every decision may be `ACCEPT`, `REJECT`, or
`DEFER`.

Common evidence:

- source `6fcfd76243b94ddecff8c9aface2ed51116984cb`;
- infrastructure `76e882d`;
- pilot/review evidence `3e30af0`;
- [launch readiness](architecture/titmas-agent-native-standards-community-launch-readiness-v1.1.md);
- `TITMAS/agent-native/pilot/pilot-result.json`;
- `TITMAS/agent-native/pilot/review-disposition-v1.1.json`.

## HD-01 — Integrate v1.1 with the v1.0 branch

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=branch integration only after final CI and owner diff review
prohibited_scope=main merge, release, deployment
term=one reviewed integration attempt
revocation=source or target branch drift
risk=history conflict or semantic elevation
rollback=abort integration; retain both dedicated branches
required_evidence=clean final CI, exact diff, no unresolved High/Critical finding
```

## HD-02 — Create a mainline integration PR

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=one draft or reviewable PR from an explicitly approved branch
prohibited_scope=merge, tag, Release, announcement
term=until PR close or explicit expiry
revocation=CI failure, branch drift, new High/Critical finding
risk=public interpretation as adoption or launch
rollback=close PR without merge
required_evidence=HD-01 disposition and final branch CI
```

## HD-03 — Publish the Agent Discovery Surface

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=read-only agent-index, manifests, schemas and public-safe guides
prohibited_scope=credentials, write access, adoption or production claims
term=time-bounded preview
revocation=privacy, security, claims or source-revision defect
risk=local discovery misread as public adoption
rollback=remove public pointer while preserving history
required_evidence=privacy review, public-safe extraction inventory, owner approval
```

## HD-04 — Allow controlled external-agent access

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=read-only, synthetic, named-provider sessions with bounded inputs
prohibited_scope=personal data, credentials, GitHub writes, Authority
term=per batch with explicit expiry
revocation=provider mismatch, data leak, boundary violation
risk=external processing and uncertain model independence
rollback=terminate access and preserve failure record
required_evidence=privacy/data review, provider terms, per-batch authorization
```

## HD-05 — Allow agents to create real GitHub Issues

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=REJECT
scope=none under current v1.1
prohibited_scope=all autonomous public Issue writes
term=until a future explicit decision
revocation=not applicable while rejected
risk=noise, spam, false urgency, authority confusion
rollback=close unauthorized Issue and retain incident evidence
required_evidence=external value proof, anti-noise gate, reversible write control
```

## HD-06 — Allow agents to submit real PRs

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=REJECT
scope=none under current v1.1
prohibited_scope=public PR creation, merge, branch protection changes
term=until a future explicit decision
revocation=not applicable while rejected
risk=scope expansion, code supply-chain and reviewer burden
rollback=close unauthorized PR without merge
required_evidence=bounded effector contract, clean-room trial, accountable reviewer
```

## HD-07 — Designate a bounded Agent Maintenance Operator

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=read-only drift checks and candidate patches inside an exact lease
prohibited_scope=merge, release, stable promotion, deletion, external contact
term=per lease, maximum stated expiry
revocation=scope breach, duplicate noise, failed review
risk=maintenance activity mistaken for accepted value
rollback=expire lease and discard unadopted patch
required_evidence=multi-lineage test, noise reduction, rollback rehearsal
```

## HD-08 — Allow additional external model providers in a pilot

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=additional provider lineages under per-batch public-safe review
prohibited_scope=silent fallback, credential publication, Authority
term=one authorized comparison batch
revocation=model mismatch, provider failure, privacy concern
risk=cost, data handling and false independence claims
rollback=stop provider calls and preserve failed sessions
required_evidence=provider contract review, model identity verification, budget
```

The completed Alibaba Cloud `qwen3.7-max` sessions were within D01's internal
controlled-pilot scope; this item concerns any additional future provider batch.

## HD-09 — Publish controlled-pilot results

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=public-safe methods, metrics, limitations and negative evidence
prohibited_scope=adoption, production, certification or 99-percent autonomy claim
term=one versioned publication
revocation=source mismatch, privacy issue, misleading claim
risk=synthetic pilot overgeneralization
rollback=withdraw active publication and retain correction record
required_evidence=claims review, reproducibility check, owner sign-off
```

## HD-10 — Publish an Agent-Native Community Preview tag

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=one immutable preview tag on an owner-approved commit
prohibited_scope=stable Release, certification, deployment, community launch
term=immutable if created; authorization expires after one tag
revocation=before creation on CI or claims failure
risk=preview tag mistaken for stable release
rollback=no tag deletion after public use; publish correction/supersession instead
required_evidence=HD-01/02 disposition, final CI, release-note claims review
```

## Current authority state

```text
HUMAN_DECISIONS_EXECUTED=0
PUBLIC_AGENT_COMMUNITY_AUTHORIZED=false
PUBLIC_GITHUB_AGENT_WRITE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
```
