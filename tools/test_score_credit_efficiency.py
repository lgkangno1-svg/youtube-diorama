#!/usr/bin/env python3
import unittest

from score_credit_efficiency import structural_framing_failure


class StructuralFramingFailureTests(unittest.TestCase):
    def test_non_first_person_is_not_failure_when_current_fields_pass(self):
        row = {
            "pov_failure": "true",
            "maker_view_failure": "false",
            "character_failure": "false",
        }
        self.assertFalse(structural_framing_failure(row))

    def test_maker_view_failure_is_structural(self):
        row = {
            "pov_failure": "",
            "maker_view_failure": "true",
            "character_failure": "false",
        }
        self.assertTrue(structural_framing_failure(row))

    def test_character_failure_is_structural(self):
        row = {
            "pov_failure": "",
            "maker_view_failure": "false",
            "character_failure": "true",
        }
        self.assertTrue(structural_framing_failure(row))

    def test_legacy_pov_failure_remains_fallback_for_old_ledgers(self):
        row = {"pov_failure": "true"}
        self.assertTrue(structural_framing_failure(row))


if __name__ == "__main__":
    unittest.main()
