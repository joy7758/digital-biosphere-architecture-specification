# First Contribution Guide

## 1. Choose a bounded contribution

Pick one [Starter Task](community/STARTER_TASKS.md) or draft a
[Proposal](specifications/templates/proposal.md). The GitHub templates are
installed only on the independent
[Activation PR branch](community/github-activation-templates/README.md).
Public Issue and Pull Request submission becomes active only after that PR is
merged.

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

Limited repository contribution is authorized but not active until the
Activation PR merges. No permanent Maintainer, established community, Stable
specification, certification or Release is created. A submitted contribution
does not grant Authority and is not accepted until Human Maintainer
disposition.
