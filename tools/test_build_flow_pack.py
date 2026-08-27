#!/usr/bin/env python3
from __future__ import annotations

import unittest

from build_flow_pack import build, frame_input_instruction, keyframe_creation_instruction, ordered_keyframes


class FlowFrameInputMapTests(unittest.TestCase):
    def test_actual_frame_token_becomes_explicit_operator_instruction(self) -> None:
        text = frame_input_instruction("ACTUAL_LAST_USABLE_FRAME_G1", role="First frame")
        self.assertIn("Flow's native `Save frame` action", text)
        self.assertIn("Do not substitute a planned keyframe", text)
        self.assertIn("browser screenshot", text)

    def test_keyframe_token_remains_free_reference(self) -> None:
        text = frame_input_instruction("KF2_CRACK", role="Last frame")
        self.assertIn("approved FREE target/reference keyframe `KF2_CRACK`", text)

    def test_missing_frame_fails_closed(self) -> None:
        text = frame_input_instruction("", role="First frame")
        self.assertIn("STOP", text)
        self.assertIn("repair the manifest", text)

    def test_first_keyframe_is_master_anchor(self) -> None:
        text = keyframe_creation_instruction(["KF0_OPEN", "KF1_TARGET"], 0)
        self.assertIn("master visual anchor", text)
        self.assertIn("KF0_OPEN", text)

    def test_later_keyframe_derives_from_previous_reference(self) -> None:
        text = keyframe_creation_instruction(["KF0_OPEN", "KF1_TARGET"], 1)
        self.assertIn("Derive `KF1_TARGET` from the approved `KF0_OPEN`", text)
        self.assertIn("image reference/ingredient", text)
        self.assertIn("Preserve paw fur", text)

    def test_numeric_kf_order_overrides_yaml_mapping_order(self) -> None:
        data = {
            "keyframes": {
                "KF2_PAYOFF": "payoff",
                "KF0_OPEN": "opening",
                "KF1_TRANSFORM": "transform",
            }
        }
        self.assertEqual(
            ordered_keyframes(data),
            ["KF0_OPEN", "KF1_TRANSFORM", "KF2_PAYOFF"],
        )

    def test_build_uses_numeric_kf_chain_after_yaml_reorder(self) -> None:
        data = {
            "episode_id": "TK-KF-ORDER",
            "title": "test",
            "hook": "test",
            "camera_grammar": {"hero_object_paw_width_ratio": [0.2, 0.3]},
            "flow_strategy": {
                "max_lite_generations_first_pass": 2,
                "non_ultra_credit_budget_first_pass": 20,
                "pacing": "healing_motion_dense",
                "max_visual_cuts_per_8s_generation": 0,
            },
            "keyframes": {
                "KF2_TARGET": "target two",
                "KF0_OPEN": "opening",
                "KF1_TARGET": "target one",
            },
            "scenes": [
                {
                    "id": "G1",
                    "generation_type": "first_plus_last",
                    "generation_seconds": 8,
                    "start_frame": "KF0_OPEN",
                    "end_frame": "KF1_TARGET",
                    "action": "one slow slide",
                },
                {
                    "id": "G2",
                    "generation_type": "first_plus_last",
                    "generation_seconds": 8,
                    "start_frame": "ACTUAL_LAST_USABLE_FRAME_G1",
                    "end_frame": "KF2_TARGET",
                    "action": "one slow press",
                },
            ],
        }
        output = build(data)
        self.assertLess(output.index("### KF0_OPEN"), output.index("### KF1_TARGET"))
        self.assertLess(output.index("### KF1_TARGET"), output.index("### KF2_TARGET"))
        self.assertIn("Derive `KF1_TARGET` from the approved `KF0_OPEN`", output)
        self.assertIn("Derive `KF2_TARGET` from the approved `KF1_TARGET`", output)

    def test_build_maps_sequential_inputs_and_save_gate(self) -> None:
        data = {
            "episode_id": "TK-TEST",
            "title": "test",
            "hook": "test",
            "camera_grammar": {
                "hero_object_size_mm": [10, 12],
                "hero_object_paw_width_ratio": [0.2, 0.3],
            },
            "flow_strategy": {
                "max_lite_generations_first_pass": 2,
                "non_ultra_credit_budget_first_pass": 20,
                "pacing": "healing_motion_dense",
                "max_visual_cuts_per_8s_generation": 0,
            },
            "keyframes": {
                "KF0_OPEN": "opening",
                "KF1_TARGET": "target one",
                "KF2_TARGET": "target two",
            },
            "scenes": [
                {
                    "id": "G1",
                    "generation_type": "first_plus_last",
                    "generation_seconds": 8,
                    "start_frame": "KF0_OPEN",
                    "end_frame": "KF1_TARGET",
                    "action": "one slow slide",
                },
                {
                    "id": "G2",
                    "generation_type": "first_plus_last",
                    "generation_seconds": 8,
                    "start_frame": "ACTUAL_LAST_USABLE_FRAME_G1",
                    "end_frame": "KF2_TARGET",
                    "action": "one slow press",
                },
            ],
        }
        output = build(data)

        self.assertIn("Gate A — FREE keyframe preflight", output)
        self.assertIn("Nano Banana 2 Lite", output)
        self.assertIn("displayed cost", output)
        self.assertIn("0-credit preflight", output)
        self.assertIn("STOP rather than assuming the keyframe is free", output)
        self.assertIn("continuity chain, not independent lottery tickets", output)
        self.assertIn("Derive `KF1_TARGET` from the approved `KF0_OPEN`", output)
        self.assertIn("image reference/ingredient", output)
        self.assertIn("KEYFRAME DRIFT FAIL", output)
        self.assertIn("Sequential-frame operator rule", output)
        self.assertIn("First frame: use the approved FREE target/reference keyframe `KF0_OPEN`", output)
        self.assertIn("First frame: use the ACTUAL frame saved from the QC-PASS G1 clip with Flow's native `Save frame` action", output)
        self.assertIn("After G1 PASS", output)
        self.assertIn("pause on the exact last usable frame", output)
        self.assertIn("click `Save frame`", output)
        self.assertIn("G1_last_usable", output)
        self.assertIn("Do not use a screenshot/re-encoded still", output)
        self.assertIn("FRAME CHAIN FAIL", output)
        self.assertIn("Maximum visual cuts in this 8s generation: 0.", output)

    def test_missing_cut_limit_does_not_invent_one(self) -> None:
        data = {
            "episode_id": "TK-CUTS-UNSET",
            "title": "test",
            "hook": "test",
            "camera_grammar": {"hero_object_paw_width_ratio": [0.2, 0.3]},
            "flow_strategy": {
                "max_lite_generations_first_pass": 1,
                "non_ultra_credit_budget_first_pass": 10,
                "pacing": "healing_motion_dense",
            },
            "keyframes": {"KF0": "open", "KF1": "target"},
            "scenes": [
                {
                    "id": "G1",
                    "generation_type": "first_plus_last",
                    "generation_seconds": 8,
                    "start_frame": "KF0",
                    "end_frame": "KF1",
                    "action": "one slow slide",
                }
            ],
        }
        output = build(data)
        self.assertNotIn("Maximum visual cuts in this 8s generation:", output)


if __name__ == "__main__":
    unittest.main()
