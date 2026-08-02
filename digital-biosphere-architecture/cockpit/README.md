# Program Governance Cockpit — read-only source bridge

This directory extends the existing DBA Program Governance Cockpit. It is not
a second cockpit, Runtime, control plane, status authority, or evidence store.

The first registered project source is `titmac-scout`:

- canonical machine identity: `titmac-scout`;
- conversation alias only: `tiamas-scout`;
- canonical status owner: `joy7758/titmac-scout`;
- access: `READ_ONLY`;
- refresh: `ON_DEMAND`;
- failure behavior: stale, unavailable, revision-drift, digest-drift, or invalid
  sources fail closed.

The adapter stores only a projection containing the source reference, exact
revision and tree, status-file digest, bounded summary, freshness, and retrieval
time. Raw evolution runs, patch variants, sandbox outputs, model output,
credentials, and private runtime data remain with the source repository.

## Agent entry

```bash
python3 cockpit/read_only_status_adapter.py \
  --project-id titmac-scout \
  --local-repository /path/to/titmac-scout \
  --candidate \
  --output cockpit/projections/titmac-scout.json

python3 -m unittest discover -s cockpit/tests -v
```

The candidate flag reads the exact pinned Draft PR branch from the source
registry. The canonical `main` source remains authoritative only after a
separate merge decision. A candidate projection must never be presented as a
merged, released, deployed, adopted, certified, or production-ready state.
