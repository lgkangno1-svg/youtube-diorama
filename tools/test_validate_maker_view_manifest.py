#!/usr/bin/env python3
from __future__ import annotations

import unittest

from test_validate_current_standard import base_manifest
from validate_maker_view_manifest import validate


def current_manifest() -> dict:
    data = base_manifest()
    data["brand_identity"]["visual_intent"] = "mini_forest_style_paws_only_miniature_making"
    data["camera_grammar"]["semantic_override"] = "mini_forest_style_observational_maker_view"
    data["camera_grammar"]["first_person_required"] = False
    data["camera_grammar"]["preferred_angles"] = [
        "high_oblique_maker_view",
        "top_down_macro",
        "tabletop_oblique_macro",
    ]
    gate = data["flow_strategy"]["progressive_spend_gate"]
    gate.pop("stop_if_pov_scale_anatomy_or_premise_fails")
    gate["stop_if_maker_view_scale_anatomy_or_premise_fails"] = True
    for scene in data["scenes"]:
        scene["paw_action_family"] = ["slide"]
    return data


class MakerViewManifestValidationTests(unittest.TestCase):
    def test_current_maker_view_manifest_passes(self) -> None:
        self.assertEqual(validate(current_manifest()), [])

    def test_literal_first_person_is_not_required(self) -> None:
        data = current_manifest()
        data["camera_grammar"]["mode"] = "maker_view"
        self.assertEqual(validate(data), [])

    def test_old_pov_stop_gate_cannot_replace_current_gate(self) -> None:
        data = current_manifest()
        gate = data["flow_strategy"]["progressive_spend_gate"]
        gate.pop("stop_if_maker_view_scale_anatomy_or_premise_fails")
        gate["stop_if_pov_scale_anatomy_or_premise_fails"] = True
        errors = validate(data)
        self.assertTrue(any("stop_if_maker_view_scale_anatomy_or_premise_fails" in e for e in errors))
        self.assertTrue(any("legacy progressive-spend gate" in e for e in errors))

    def test_missing_maker_view_semantic_override_fails_closed(self) -> None:
        data = current_manifest()
        data["camera_grammar"].pop("semantic_override")
        errors = validate(data)
        self.assertTrue(any("semantic_override" in e for e in errors))

    def test_first_person_required_true_fails_closed(self) -> None:
        data = current_manifest()
        data["camera_grammar"]["first_person_required"] = True
        errors = validate(data)
        self.assertTrue(any("first_person_required must be false" in e for e in errors))

    def test_missing_scene_action_family_fails_closed(self) -> None:
        data = current_manifest()
        data["scenes"][0].pop("paw_action_family")
        errors = validate(data)
        self.assertTrue(any("G1.paw_action_family must contain exactly one" in e for e in errors))

    def test_multiple_active_actions_fail_closed(self) -> None:
        data = current_manifest()
        data["scenes"][0]["paw_action_family"] = ["press", "slide"]
        errors = validate(data)
        self.assertTrue(any("G1.paw_action_family must contain exactly one" in e for e in errors))

    def test_human_dexterity_action_fails_closed(self) -> None:
        data = current_manifest()
        data["scenes"][0]["paw_action_family"] = ["pinch"]
        errors = validate(data)
        self.assertTrue(any("not feline-safe" in e for e in errors))

    def test_structural_checks_are_still_delegated(self) -> None:
        data = current_manifest()
        data["flow_strategy"]["output_count"] = 2
        errors = validate(data)
        self.assertIn("flow_strategy.output_count must be the integer 1", errors)


if __name__ == "__main__":
    unittest.main()
