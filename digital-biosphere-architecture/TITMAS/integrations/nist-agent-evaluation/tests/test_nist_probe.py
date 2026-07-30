import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

import pytest


ADAPTER_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ADAPTER_ROOT / "examples"
VALIDATOR_PATH = ADAPTER_ROOT / "validator.py"
SPEC = importlib.util.spec_from_file_location("titmas_nist_probe", VALIDATOR_PATH)
assert SPEC and SPEC.loader
PROBE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = PROBE
SPEC.loader.exec_module(PROBE)


def fixture(name: str) -> Path:
    return EXAMPLES / name


def write_variant(tmp_path: Path, source_name: str, mutate) -> Path:
    source = fixture(source_name)
    value = json.loads(source.read_text(encoding="utf-8"))
    mutate(value)
    target = tmp_path / source.name
    target.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    evidence_source = EXAMPLES / "evidence"
    evidence_target = tmp_path / "evidence"
    shutil.copytree(evidence_source, evidence_target)
    return target


def test_passes_normal_execution():
    evaluation = PROBE.evaluate_probe(
        fixture("case-004-successful-verification.json")
    )
    assert evaluation.result == PROBE.PASS
    assert set(evaluation.checked_dimensions) == {
        "Identity",
        "Authorization",
        "Tool Invocation",
        "Execution Trace",
        "Outcome",
        "Integrity",
        "Auditability",
    }


def test_fails_unauthorized_tool_call():
    evaluation = PROBE.evaluate_probe(
        fixture("case-001-unauthorized-tool-call.json")
    )
    assert evaluation.result == PROBE.FAIL_UNAUTHORIZED_TOOL_CALL


def test_fails_missing_evidence():
    evaluation = PROBE.evaluate_probe(
        fixture("case-002-missing-evidence.json")
    )
    assert evaluation.result == PROBE.FAIL_MISSING_EVIDENCE


def test_fails_modified_evidence_hash():
    evaluation = PROBE.evaluate_probe(
        fixture("case-003-evidence-tampering.json")
    )
    assert evaluation.result == PROBE.FAIL_EVIDENCE_TAMPERING
    assert "does not match computed digest" in evaluation.reasons[0]


def test_fails_evidence_only_unauthorized_tool_with_recomputed_hash(tmp_path):
    variant = write_variant(
        tmp_path,
        "case-004-successful-verification.json",
        lambda value: None,
    )
    evidence_path = tmp_path / "evidence" / "case-004-execution-evidence.json"
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    evidence["tool_invocations"][0]["tool"] = "shell.exec"
    evidence_path.write_text(
        json.dumps(evidence, indent=2) + "\n",
        encoding="utf-8",
    )

    value = json.loads(variant.read_text(encoding="utf-8"))
    value["evidence_reference"]["sha256"] = (
        "sha256:" + hashlib.sha256(evidence_path.read_bytes()).hexdigest()
    )
    variant.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    evaluation = PROBE.evaluate_probe(variant)
    assert evaluation.result == PROBE.FAIL_UNAUTHORIZED_TOOL_CALL
    assert "evidence:shell.exec" in evaluation.reasons[0]


def test_fails_outcome_mismatch(tmp_path):
    def change_outcome(value):
        value["observed_behavior"]["outcome"] = {
            "status": "FAILURE",
            "result_digest": "sha256:" + ("f" * 64),
        }

    variant = write_variant(
        tmp_path,
        "case-004-successful-verification.json",
        change_outcome,
    )
    evaluation = PROBE.evaluate_probe(variant)
    assert evaluation.result == PROBE.FAIL_OUTCOME_MISMATCH


def test_declared_verification_result_is_not_trusted(tmp_path):
    def forge_declared_result(value):
        value["verification_result"] = "FAIL_OUTCOME_MISMATCH"

    variant = write_variant(
        tmp_path,
        "case-004-successful-verification.json",
        forge_declared_result,
    )
    evaluation = PROBE.evaluate_probe(variant)
    assert evaluation.result == PROBE.PASS


def test_schema_rejects_unknown_top_level_fields(tmp_path):
    def add_unknown(value):
        value["official_nist_approval"] = True

    variant = write_variant(
        tmp_path,
        "case-004-successful-verification.json",
        add_unknown,
    )
    evaluation = PROBE.evaluate_probe(variant)
    assert evaluation.result == PROBE.ERROR_INVALID_PROBE


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        (
            "case-001-unauthorized-tool-call.json",
            "FAIL_UNAUTHORIZED_TOOL_CALL",
        ),
        ("case-002-missing-evidence.json", "FAIL_MISSING_EVIDENCE"),
        ("case-003-evidence-tampering.json", "FAIL_EVIDENCE_TAMPERING"),
        ("case-004-successful-verification.json", "PASS"),
    ],
)
def test_example_expected_results_match_computed_results(name, expected):
    value = json.loads(fixture(name).read_text(encoding="utf-8"))
    assert value["verification_result"] == expected
    assert PROBE.evaluate_probe(fixture(name)).result == expected
