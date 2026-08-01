#!/usr/bin/env python3
"""Minimal Stage 5 Python SDK unit tests."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SDK_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_ROOT = PROJECT_ROOT / "TITMAS" / "private-stage5-protocol-surface" / "schemas"
SPEC = importlib.util.spec_from_file_location(
    "titmas_stage5_sdk_tested", SDK_ROOT / "titmas_stage5_sdk.py"
)
assert SPEC and SPEC.loader
SDK = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SDK
SPEC.loader.exec_module(SDK)


class SDKTests(unittest.TestCase):
    def client(self, transport):
        return SDK.Stage5Client(
            "http://127.0.0.1:12345",
            "synthetic-in-memory-key",
            SCHEMA_ROOT,
            transport=transport,
        )

    def test_catalog_request(self) -> None:
        seen = []

        def transport(method, path, payload, token):
            seen.append((method, path, payload, token))
            return 200, {"specifications": []}

        result = self.client(transport).get_standard_catalog()
        self.assertEqual([], result["specifications"])
        self.assertEqual("GET", seen[0][0])

    def test_schema_preflight_blocks_extra_field_before_transport(self) -> None:
        called = False

        def transport(*args):
            nonlocal called
            called = True
            return 200, {}

        with self.assertRaises(ValueError):
            self.client(transport).submit_test_vector({"unexpected": True})
        self.assertFalse(called)

    def test_403_is_not_retried(self) -> None:
        calls = 0

        def transport(*args):
            nonlocal calls
            calls += 1
            return 403, {
                "error": {
                    "code": "TITMAS-STAGE5-403-SCOPE-DENIED",
                    "message": "Scope denied.",
                }
            }

        with self.assertRaises(SDK.TITMASClientError) as caught:
            self.client(transport).get_tasks()
        self.assertEqual("REQUEST_HUMAN_SCOPE_REVIEW", caught.exception.retry_advice)
        self.assertEqual(1, calls)

    def test_non_loopback_endpoint_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            SDK.Stage5Client(
                "https://example.invalid",
                "synthetic",
                SCHEMA_ROOT,
            )

    def test_submit_review_request(self) -> None:
        seen = []

        def transport(method, path, payload, token):
            seen.append((method, path, payload, token))
            return 200, {"success": True}

        review_payload = {
            "review_id": "STAGE5-REVIEW-12345",
            "submission_id": "stage5-submission-67890",
            "reviewer_ref": "reviewer-1",
            "provider": "OpenAI",
            "requested_model": "gpt-4",
            "returned_model": "gpt-4",
            "verdict": "PASS",
            "checks": {
                "grounding": True,
                "schema_correctness": True,
                "developer_value": True,
                "scope": True,
                "compatibility": True,
                "positive_cases": True,
                "negative_cases": True,
                "failure_behavior": True,
                "semantic_elevation": True,
                "authority_boundary": True,
                "commercial_overclaim": True
            },
            "blocking_findings": [],
            "non_blocking_findings": [],
            "required_corrections": [],
            "limitations": ["None"]
        }

        result = self.client(transport).submit_review("stage5-submission-67890", review_payload)
        self.assertEqual({"success": True}, result)
        self.assertEqual(1, len(seen))
        method, path, payload, token = seen[0]
        self.assertEqual("POST", method)
        self.assertEqual("/v1/contributions/stage5-submission-67890/reviews", path)
        self.assertEqual({"review": review_payload}, payload)


if __name__ == "__main__":
    unittest.main()
