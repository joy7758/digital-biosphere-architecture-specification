# PVS-0 citation examples

## Citation state

These examples cite the exact public Git commit. No DOI, Zenodo record,
GitHub Release, or Git tag exists for this package at preparation time. Do not
insert a guessed, reserved, or example DOI into a publication, paper, dataset,
software package, or registry record.

The creator name and ORCID are taken from the exact commit's `CITATION.cff` and
still require human confirmation before a Zenodo upload. Authorship metadata
does not determine copyright ownership or publication authority.

## BibTeX

```bibtex
@dataset{zhang_titmas_pvs0_2026,
  author       = {Zhang, Bin},
  title        = {TITMAS 21.T11966 Five-Record Public Verification Slice PVS-0 Candidate},
  year         = {2026},
  version      = {PVS-0-candidate+fe7c1c2},
  publisher    = {GitHub},
  url          = {https://github.com/joy7758/titmas-fdo-public-verification/tree/fe7c1c2e0787fc753953209dfbc53b105406fad5},
  urldate      = {2026-08-04},
  note         = {Historical experimental public-verification candidate; no DOI assigned}
}
```

If the human-approved Zenodo resource type becomes `software`, change the
entry type to `@software` and reconcile the source `CITATION.cff` before
publication. Do not make that metadata change silently.

## APA style

Zhang, B. (2026). *TITMAS 21.T11966 five-record public verification
slice PVS-0 candidate* (PVS-0-candidate+fe7c1c2) [Data set and bounded
verification software]. GitHub.
https://github.com/joy7758/titmas-fdo-public-verification/tree/fe7c1c2e0787fc753953209dfbc53b105406fad5

## Short citation

Zhang (2026), *TITMAS FDO PVS-0 candidate*, commit `fe7c1c2`.

## After a DOI is actually created

Only after Zenodo publication is authorized, completed, and independently
verified should the assigned DOI replace the GitHub-only publication locator.
Keep the exact source commit in the version or note field so the archived bytes
remain unambiguous. The final citation must be copied from the published Zenodo
record and checked against the approved creator, title, type, version, and
license metadata; this file intentionally contains no DOI placeholder that
could be mistaken for a real identifier.

When discussing an individual registry record, cite that record's full Handle
PID and exact classification separately. Do not cite the shared `21.T11966`
prefix as though it were a single standard.
