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
            "max_visual_cuts_per_8s_generation": 0,
            "preferred_action_count_per_generation": 1,
            "progressive_spend_gate": {
                "g2_requires_g1_pass": True,
                "g3_requires_g2_pass": True,
                "stop_if_pov_scale_anatomy_or_premise_fails": True,
                "reroll_only_structural_failure": True,
            },
            "sequential_chain": {
                "g2_start_source": "save_actual_last_usable_frame_from_G1",
                "g3_start_source": "save_actual_last_usable_frame_from_G2",
            },
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
                "action": "one paw nudges the tiny tray a few millimeters",
                "action_guard": "front paws only; preserve tiny scale; no gripping",
            },
            {
                "id": "G2",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "ACTUAL_LAST_USABLE_FRAME_G1",
                "end_frame": "KF2_TARGET",
                "action": "one paw steadies the tray while the surface changes slowly",
                "action_guard": "same POV and scale; one calm action; no tool grip",
            },
            {
                "id": "G3",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "ACTUAL_LAST_USABLE_FRAME_G2",
                "end_frame": "KF3_TARGET",
                "action": "one paw slides the finished tray into the serving position",
                "action_guard": "same tray and camera; no new prop; no full cat",
            },
        ],
    }


class ManifestSpendConsistencyTests(unittest.TestCase):
    def test_valid_compact_h30_passes(self) -> None:
        self.assertEqual(validate(base_manifest()), [])

    def test_long_take_cut_limit_must_be_declared(self) -> None:
        data = base_manifest()
        del data["flow_strategy"]["max_visual_cuts_per_8s_generation"]
        errors = validate(data)
        self.assertIn(
            "flow_strategy.max_visual_cuts_per_8s_generation must be an integer 0 or 1",
            errors,
        )

    def test_rapid_cut_manifest_fails_closed(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["max_visual_cuts_per_8s_generation"] = 2
        errors = validate(data)
        self.assertIn(
            "flow_strategy.max_visual_cuts_per_8s_generation must be 0 or 1 for calm long-take pacing",
            errors,
        )

    def test_one_cut_is_allowed_for_non_montage_exception(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["max_visual_cuts_per_8s_generation"] = 1
        self.assertEqual(validate(data), [])

    def test_cut_limit_float_does_not_coerce_to_integer(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["max_visual_cuts_per_8s_generation"] = 0.0
        errors = validate(data)
        self.assertIn(
            "flow_strategy.max_visual_cuts_per_8s_generation must be an integer 0 or 1",
            errors,
        )

    def test_preferred_action_count_must_remain_one(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["preferred_action_count_per_generation"] = 2
        errors = validate(data)
        self.assertIn("flow_strategy.preferred_action_count_per_generation must be the integer 1", errors)

    def test_preferred_action_count_fraction_does_not_truncate_to_one(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["preferred_action_count_per_generation"] = 1.5
        errors = validate(data)
        self.assertIn("flow_strategy.preferred_action_count_per_generation must be the integer 1", errors)

    def test_output_count_bool_does_not_coerce_to_one(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["output_count"] = True
        errors = validate(data)
        self.assertIn("flow_strategy.output_count must be the integer 1", errors)

    def test_declared_generation_count_must_match_scenes(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["max_lite_generations_first_pass"] = 4
        errors = validate(data)
        self.assertTrue(any("must equal the number of manifest scenes" in error for error in errors))

    def test_generation_count_fraction_does_not_truncate(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["max_lite_generations_first_pass"] = 3.5
        errors = validate(data)
        self.assertIn("flow_strategy.max_lite_generations_first_pass must be an integer", errors)

    def test_credit_budget_must_match_generation_ceiling(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["non_ultra_credit_budget_first_pass"] = 40
        errors = validate(data)
        self.assertTrue(any("must match the current Lite first-pass ceiling" in error for error in errors))

    def test_credit_budget_float_does_not_coerce(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["non_ultra_credit_budget_first_pass"] = 30.0
        errors = validate(data)
        self.assertIn("flow_strategy.non_ultra_credit_budget_first_pass must be an integer", errors)

    def test_generation_seconds_float_does_not_coerce(self) -> None:
        data = base_manifest()
        data["scenes"][0]["generation_seconds"] = 8.0
        errors = validate(data)
        self.assertIn("G1 generation_seconds must be the integer 8", errors)

    def test_compact_h30_cannot_silently_gain_g4(self) -> None:
        data = base_manifest()
        data["scenes"].append(
            {
                "id": "G4",
                "generation_type": "first_plus_last",
                "generation_seconds": 8,
                "start_frame": "ACTUAL_LAST_USABLE_FRAME_G3",
                "end_frame": "KF4_TARGET",
                "action": "one paw slides the tray into a quiet final niche",
                "action_guard": "same tray and POV; no padding or new cookware",
            }
        )
        data["keyframes"]["KF4_TARGET"] = "approved fourth target"
        data["flow_strategy"]["max_lite_generations_first_pass"] = 4
        data["flow_strategy"]["non_ultra_credit_budget_first_pass"] = 40
        data["flow_strategy"]["progressive_spend_gate"]["g4_requires_g3_pass"] = True
        data["flow_strategy"]["sequential_chain"]["g4_start_source"] = "save_actual_last_usable_frame_from_G3"
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

    def test_keyframe_name_requires_numeric_index(self) -> None:
        data = base_manifest()
        prompt = data["keyframes"].pop("KF2_TARGET")
        data["keyframes"]["KF_TARGET_TWO"] = prompt
        data["scenes"][1]["end_frame"] = "KF_TARGET_TWO"
        errors = validate(data)
        self.assertIn("keyframe name must start with KF<number>: KF_TARGET_TWO", errors)
        self.assertTrue(any("contiguous planned keyframe indices" in error for error in errors))

    def test_keyframe_numeric_index_must_be_unique(self) -> None:
        data = base_manifest()
        data["keyframes"]["KF2_ALT"] = "duplicate numeric target"
        errors = validate(data)
        self.assertIn(
            "keyframe numeric index KF2 is duplicated by KF2_TARGET and KF2_ALT",
            errors,
        )

    def test_keyframe_mapping_reorder_does_not_change_semantic_sequence(self) -> None:
        data = base_manifest()
        original = data["keyframes"]
        data["keyframes"] = {
            "KF2_TARGET": original["KF2_TARGET"],
            "KF0_OPEN": original["KF0_OPEN"],
            "KF3_TARGET": original["KF3_TARGET"],
            "KF1_TARGET": original["KF1_TARGET"],
        }
        self.assertEqual(validate(data), [])

    def test_missing_keyframe_index_fails_closed(self) -> None:
        data = base_manifest()
        data["keyframes"].pop("KF2_TARGET")
        data["keyframes"]["KF4_TARGET"] = "wrong fourth target"
        data["scenes"][1]["end_frame"] = "KF4_TARGET"
        errors = validate(data)
        self.assertIn(
            "all-first_plus_last manifests must define contiguous planned keyframe indices KF0..KF3 exactly; found [0, 1, 3, 4]",
            errors,
        )

    def test_scene_action_must_not_be_empty(self) -> None:
        data = base_manifest()
        data["scenes"][0]["action"] = ""
        errors = validate(data)
        self.assertIn("G1 action must be non-empty before paid generation", errors)

    def test_scene_action_guard_must_not_be_empty(self) -> None:
        data = base_manifest()
        data["scenes"][2]["action_guard"] = "  "
        errors = validate(data)
        self.assertIn("G3 action_guard must be non-empty before paid generation", errors)

    def test_g2_must_require_g1_pass(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["progressive_spend_gate"]["g2_requires_g1_pass"] = False
        errors = validate(data)
        self.assertIn("flow_strategy.progressive_spend_gate.g2_requires_g1_pass must be true", errors)

    def test_structural_failure_stop_gate_is_required(self) -> None:
        data = base_manifest()
        del data["flow_strategy"]["progressive_spend_gate"]["stop_if_pov_scale_anatomy_or_premise_fails"]
        errors = validate(data)
        self.assertIn(
            "flow_strategy.progressive_spend_gate.stop_if_pov_scale_anatomy_or_premise_fails must be true",
            errors,
        )

    def test_sequential_chain_metadata_must_match_actual_frame_policy(self) -> None:
        data = base_manifest()
        data["flow_strategy"]["sequential_chain"]["g3_start_source"] = "planned_KF2_target"
        errors = validate(data)
        self.assertIn(
            "flow_strategy.sequential_chain.g3_start_source must be save_actual_last_usable_frame_from_G2",
            errors,
        )

    def test_extend_scene_does_not_require_saved_still_chain_metadata(self) -> None:
        data = base_manifest()
        data["scenes"][1] = {
            "id": "G2",
            "generation_type": "extend",
            "generation_seconds": 8,
            "source_scene": "G1",
            "action": "continue the same tiny warming motion",
            "action_guard": "preserve POV and scale; no camera cut or new prop",
        }
        del data["flow_strategy"]["sequential_chain"]["g2_start_source"]
        self.assertEqual(validate(data), [])

    def test_runtime_target_cannot_require_padding(self) -> None:
        data = base_manifest()
        data["runtime_strategy"]["target_final_runtime_seconds"] = [30, 36]
        data["length_target_seconds"] = 33
        data["post_production"] = {
            "preferred_playback_speed_range": [0.92, 1.0],
            "max_total_static_hold_seconds": 3,
        }
        errors = validate(data)
        self.assertTrue(any("final runtime target is infeasible without padding" in error for error in errors))
        self.assertTrue(any("length_target_seconds is infeasible without padding" in error for error in errors))

    def test_runtime_target_may_use_natural_slowdown_without_padding(self) -> None:
        data = base_manifest()
        data["runtime_strategy"]["target_final_runtime_seconds"] = [24, 27]
        data["length_target_seconds"] = 26
        data["post_production"] = {
            "preferred_playback_speed_range": [0.92, 1.0],
            "max_total_static_hold_seconds": 3,
        }
        self.assertEqual(validate(data), [])

    def test_only_explicit_editorial_holds_extend_feasible_runtime(self) -> None:
        data = base_manifest()
        data["runtime_strategy"]["target_final_runtime_seconds"] = [28, 29]
        data["length_target_seconds"] = 28
        data["post_production"] = {
            "preferred_playback_speed_range": [0.92, 1.0],
            "max_total_static_hold_seconds": 3,
        }
        data["editorial_seconds"] = {"opening_keyframe_hold": 2.0}
        self.assertEqual(validate(data), [])


if __name__ == "__main__":
    unittest.main()
