#!/usr/bin/env python3

import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


PILOT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PILOT_ROOT))

import validate_agent_audit


class AgentAuditValidationTests(unittest.TestCase):
    def test_negative_result_is_valid_and_fail_closed(self):
        result = validate_agent_audit.validate()
        self.assertEqual("PASS_WITH_RECORDED_NEGATIVE_RESULT", result["status"])
        self.assertFalse(result["stage5_private_preview_operational"])
        self.assertEqual(0, result["automatic_retry_count"])

    def test_unknown_review_cannot_become_operational(self):
        original = validate_agent_audit.load

        def altered(name):
            value = original(name)
            if name == "sanitized-agent-pilot-audit.json":
                value = copy.deepcopy(value)
                value["stage5_private_preview_operational"] = True
            return value

        with patch.object(validate_agent_audit, "load", side_effect=altered):
            with self.assertRaises(ValueError):
                validate_agent_audit.validate()

    def test_retry_count_cannot_be_elevated(self):
        original = validate_agent_audit.load

        def altered(name):
            value = original(name)
            if name == "sanitized-agent-pilot-audit.json":
                value = copy.deepcopy(value)
                value["automatic_retry_count"] = 1
            return value

        with patch.object(validate_agent_audit, "load", side_effect=altered):
            with self.assertRaises(ValueError):
                validate_agent_audit.validate()


if __name__ == "__main__":
    unittest.main()
