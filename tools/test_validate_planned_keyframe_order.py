#!/usr/bin/env python3
from __future__ import annotations

import copy
import unittest
from pathlib import Path

import yaml

from validate_current_standard import validate

ROOT = Path(__file__).resolve().parent.parent
TK005 = ROOT / "episodes" / "TK-005.yaml"


def tk005_manifest() -> dict:
    return yaml.safe_load(TK005.read_text(encoding="utf-8")) or {}


class PlannedKeyframeOrderTests(unittest.TestCase):
    def test_current_tk005_chain_passes(self) -> None:
        self.assertEqual(validate(tk005_manifest()), [])

    def test_defined_but_wrong_scene_target_fails_closed(self) -> None:
        data = copy.deepcopy(tk005_manifest())
        data["scenes"][1]["end_frame"] = "KF3_OPEN"
        errors = validate(data)
        self.assertIn(
            "G2 end_frame must follow planned keyframe order: expected KF2_CRACK, got KF3_OPEN",
            errors,
        )

    def test_g1_must_start_from_first_planned_keyframe(self) -> None:
        data = copy.deepcopy(tk005_manifest())
        data["scenes"][0]["start_frame"] = "KF1_WARM"
        errors = validate(data)
        self.assertIn("G1 must start from the first planned keyframe KF0_OPEN", errors)

    def test_all_first_plus_last_chain_rejects_decorative_extra_keyframe(self) -> None:
        data = copy.deepcopy(tk005_manifest())
        data["keyframes"]["KF5_UNUSED"] = "unused decorative target that should not exist"
        errors = validate(data)
        self.assertTrue(
            any("must define exactly one opening KF plus one ordered target KF per scene" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
