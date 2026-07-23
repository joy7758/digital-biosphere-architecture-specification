# PR-G2A Native Linux x86_64 Validation Supplement Attestation

```text
attestation_id=TMAI-PR-G2A-NATIVE-LINUX-X86-64-VALIDATION-ATTESTATION-20260723-014
decision_reference=DQ-018
review_gate=PR-G2A
attested_dba_commit=c1f83bcd5a09432128f347339a642c9f065e385d
attested_dba_tree=3688146ab946b6be865fd44d8e153664401ee5ae
dbos_receipt_commit=ff1752cb3bb01ff67538bb04b3c7517fbcee3269
dba_supplement_remote_attested=true
human_security_review_complete=false
pr_g2a_ready_for_human_review=false
pr_g2a_human_review_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Attested Scope（证明范围）

本 attestation 对 DBA branch `codex/production-observability-baseline` 的 predecessor commit
`c1f83bc…` 进行非自引用绑定。fresh GitHub clone 精确检出该 commit，工作树 clean；新增的
native Linux x86_64 validation supplement、机器可读 JSON 及其对 DBOS receipt `ff1752c…`
的引用均可从远端重现。

| surface | exact remote binding |
|---|---|
| DBA repository / branch | `joy7758/digital-biosphere-architecture-specification` / `codex/production-observability-baseline` |
| predecessor commit / tree | `c1f83bcd5a09432128f347339a642c9f065e385d` / `3688146ab946b6be865fd44d8e153664401ee5ae` |
| supplement Markdown | 4,410 bytes / `sha256:55e5abd61a3e72771255c7994feec5ef5f5c4ab4e15ccd847fb7e2355ff45645` |
| supplement JSON | 3,472 bytes / `sha256:84eb44461161f1d611caa49e954af50ac7d900c5a50d93599337ba5607c33f91` |
| DBOS native receipt | `ff1752cb3bb01ff67538bb04b3c7517fbcee3269` / source `23c8f0878058f29e733b6f164572ac157c6c7d1c` |

## Remote Verification（远端复验）

```text
fresh_remote_clone=PASS
exact_predecessor_commit=PASS
clean_worktree=PASS
json_parse=PASS
markdown_links=866
missing_markdown_links=0
governance_invariants=PASS
native_dbos_receipt_binding=PASS
```

这些结果只证明 DBA governance receipt（治理回执）可远端追溯。它们不重复执行 DBOS
workload，也不代替独立 Human Security Review。

## Agent Recommendation（智能体建议）

```text
verdict=CONDITIONALLY_RECOMMENDED
recommended_as=REMOTE_ATTESTED_NATIVE_VALIDATION_INPUT_FOR_INDEPENDENT_HUMAN_SECURITY_REVIEW
next_recommended_gate=INDEPENDENT_HUMAN_SECURITY_REVIEW
not_recommended_as=PR_G2A_APPROVED_FULL_PR_G2_PRODUCTION_SERVICE_SLO_HA_OR_DURABILITY_EVIDENCE
```

## Authority Boundary（权力边界）

```text
REMOTE_ATTESTATION_NE_HUMAN_SECURITY_REVIEW=true
REMOTE_ATTESTATION_NE_GATE_APPROVAL=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_HUMAN_REVIEW_APPROVED=false
DQ_019_STATUS=BLOCKED_INPUT
DQ_020_STATUS=BLOCKED_INPUT
DQ_021_STATUS=BLOCKED_INPUT
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

本 attestation 不授权 PR、merge、main、release、deployment、Collector、listener、production
database、Agent、DBOS Runtime、Entity、Permission、canonical Evidence 或 SAEE output。
