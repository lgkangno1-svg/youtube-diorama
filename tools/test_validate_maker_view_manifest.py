#!/usr/bin/env python3
from __future__ import annotations

import copy
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


def adaptive_h40_manifest() -> dict:
    data = current_manifest()
    data["runtime_strategy"] = {
        "mode": "immersive_h40",
        "minimum_distinct_motion_beats": 3,
        "fourth_beat_optional_after_g3": True,
        "fourth_beat_value": "quiet world resolution only if real G3 still benefits",
    }
    data["keyframes"]["KF4_TARGET"] = "approved optional fourth target"
    data["scenes"].append(
        {
            "id": "G4",
            "generation_type": "first_plus_last",
            "generation_seconds": 8,
            "start_frame": "ACTUAL_LAST_USABLE_FRAME_G3",
            "end_frame": "KF4_TARGET",
            "action": "one paw slides the tray into a quiet final niche",
            "action_guard": "same tray and maker view; no padding or new cookware",
            "paw_action_family": ["slide"],
        }
    )
    data["flow_strategy"]["max_lite_generations_first_pass"] = 4
    data["flow_strategy"]["non_ultra_credit_budget_first_pass"] = 40
    data["flow_strategy"]["progressive_spend_gate"]["g4_requires_g3_pass"] = True
    data["flow_strategy"]["sequential_chain"]["g4_start_source"] = "save_actual_last_usable_frame_from_G3"
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

    def test_adaptive_h40_allows_three_core_beats_plus_optional_g4_plan(self) -> None:
        self.assertEqual(validate(adaptive_h40_manifest()), [])

    def test_adaptive_h40_rejects_mandatory_four_core_beat_semantics(self) -> None:
        data = adaptive_h40_manifest()
        data["runtime_strategy"]["minimum_distinct_motion_beats"] = 4
        errors = validate(data)
        self.assertTrue(any("minimum_distinct_motion_beats = 3" in e for e in errors))

    def test_adaptive_h40_requires_explicit_after_g3_value_gate(self) -> None:
        data = adaptive_h40_manifest()
        data["runtime_strategy"]["fourth_beat_optional_after_g3"] = False
        errors = validate(data)
        self.assertTrue(any("fourth_beat_optional_after_g3 = true" in e for e in errors))

    def test_h40_adapter_does_not_mutate_current_manifest(self) -> None:
        data = adaptive_h40_manifest()
        before = copy.deepcopy(data)
        self.assertEqual(validate(data), [])
        self.assertEqual(data, before)


if __name__ == "__main__":
    unittest.main()
