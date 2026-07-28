# First Contribution Guide

## 1. Choose a bounded contribution

Pick one [Starter Task](community/STARTER_TASKS.md) or draft a
[Proposal](specifications/templates/proposal.md). Do not create a real Issue
until the Human Owner authorizes the public contribution surface.

## 2. Declare scope

- developer value;
- files and object owners affected;
- sources and exact versions;
- tests and failure behavior;
- AI assistance and human accountability;
- prohibited claims.

## 3. Validate

```bash
python3 TITMAS/conformance/harness.py
python3 -m unittest discover -s TITMAS/conformance/tests -v
python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
git diff --check
```

## 4. Review

Use [the review process](community/REVIEW_PROCESS.md). Review does not create
Authority or adoption.

## 5. Know the current limits

No public contribution, Maintainer, community, Stable specification,
certification or release is authorized.
