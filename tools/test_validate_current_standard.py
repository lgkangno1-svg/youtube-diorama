#!/usr/bin/env python3
from __future__ import annotations

import copy
import unittest

from validate_current_standard import validate


def base_manifest() -> dict:
    return {
        "episode_id": "TK-TEST",
        "brand_identity": {
            "hero_cat": "HERO_CAT_V1",
            "kitchen_world": "KITCHEN_WORLD_V1",
            "shorts_visual_grammar": "POV_PAWS_MICROWORLD_V1",
        },
        "camera_grammar": {
            "mode": "first_person_cat_pov",
            "visible_cat_parts": ["front_paws_only"],
            "hide_face_head_body": True,
            "hero_object_paw_width_ratio": [0.2, 0.3],
        },
        "runtime_strategy": {
            "mode": "compact_h30",
            "minimum_distinct_motion_beats": 3,
        },
        "flow_strategy": {
            "primary_model": "veo-3.1-lite",
            "output_count": 1,
            "max_lite_generations_first_pass": 3,
            "non_ultra_credit_budget_first_pass": 30,
            "narration_policy": "none_by_default",
        },
        "keyframes": {
            "KF0_OPEN": "approved opening frame",
            "KF1_TARGET": "approved first target",
            "KF2_TARGET": "approved second target",
            "KF3_TARGET": "approved final target",
        },
        "scenes": [
            {
                "id": "G1",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "KF0_OPEN",
                "end_frame": "KF1_TARGET",
            },
            {
                "id": "G2",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "ACTUAL_LAST_USABLE_FRAME_G1",
                "end_frame": "KF2_TARGET",
            },
            {
                "id": "G3",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "ACTUAL_LAST_USABLE_FRAME_G2",
                "end_frame": "KF3_TARGET",
            },
        ],
    }


class ManifestSpendConsistencyTests(unittest.TestCase):
    def test_valid_compact_h30_passes(self) -> None:
        self.assertEqual(validate(base_manifest()), [])

    def test_declared_generation_count_must_match_scenes(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["max_lite_generations_first_pass"] = 4
        errors = validate(data)
        self.assertTrue(any("must equal the number of manifest scenes" in error for error in errors))

    def test_credit_budget_must_match_generation_ceiling(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["non_ultra_credit_budget_first_pass"] = 40
        errors = validate(data)
        self.assertTrue(any("must match the current Lite first-pass ceiling" in error for error in errors))

    def test_compact_h30_cannot_silently_gain_g4(self) -> None:
        data = base_manifest()
        data["scenes"].append(
            {
                "id": "G4",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "ACTUAL_LAST_USABLE_FRAME_G3",
                "end_frame": "KF4_TARGET",
            }
        )
        data["keyframes"]["KF4_TARGET"] = "approved fourth target"
        data["flow_strategy"]["max_lite_generations_first_pass"] = 4
        data["flow_strategy"]["non_ultra_credit_budget_first_pass"] = 40
        errors = validate(data)
        self.assertIn("compact_h30 must declare exactly 3 scenes and 3 first-pass Lite generations", errors)

    def test_immersive_h40_requires_exact_four_scene_spend_plan(self) -> None:
        data = base_manifest()
        data["runtime_strategy"] = {
            "mode": "immersive_h40",
            "minimum_distinct_motion_beats": 4,
            "fourth_beat_value": "quiet world resolution",
        }
        errors = validate(data)
        self.assertIn("immersive_h40 must declare exactly 4 scenes and 4 first-pass Lite generations", errors)

    def test_scene_ids_and_required_frames_fail_closed(self) -> None:
        data = copy.deepcopy(base_manifest())
        data["scenes"][1]["id"] = "G9"
        data["scenes"][1]["end_frame"] = ""
        errors = validate(data)
        self.assertIn("scene 2 id must be G2", errors)
        self.assertIn("G2 first_plus_last requires end_frame", errors)

    def test_referenced_keyframe_must_exist(self) -> None:
        data = base_manifest()
        data["scenes"][1]["end_frame"] = "KF2_CRCK"
        errors = validate(data)
        self.assertIn(
            "G2 end_frame references undefined keyframe KF2_CRCK; define it in manifest.keyframes before preparing Flow files",
            errors,
        )

    def test_keyframe_prompt_must_not_be_empty(self) -> None:
        data = base_manifest()
        data["keyframes"]["KF2_TARGET"] = ""
        errors = validate(data)
        self.assertIn("keyframe KF2_TARGET must contain a non-empty prompt", errors)


if __name__ == "__main__":
    unittest.main()
