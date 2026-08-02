# D19 ER-1 Deterministic Self-Healing Demo

The fixture represents a stale derived task registry. The source registry is
unchanged. The bounded runner detects the mismatch, creates three alternatives
(MINIMAL_REPAIR, ALTERNATIVE_REPAIR, NO_CHANGE_BASELINE), selects the
minimal deterministic regeneration, validates it, prepares rollback evidence
and emits a lineage package.

The runner writes only to an explicit caller-provided directory. Tests use a
temporary directory. No network, credentials, Runtime, database, production
resource or P0-10 path is involved.

    python3 TITMAS/agent-native/evolution/evolution.py demo \
      --output /tmp/titmas-d19-demo

The command is a reference demonstration, not an autonomous production repair.
