#!/usr/bin/env python3
from __future__ import annotations

import unittest

from build_flow_pack import build, frame_input_instruction


class FlowFrameInputMapTests(unittest.TestCase):
    def test_actual_frame_token_becomes_explicit_operator_instruction(self) -> None:
        text = frame_input_instruction("ACTUAL_LAST_USABLE_FRAME_G1", role="First frame")
        self.assertIn("ACTUAL saved last usable frame from G1", text)
        self.assertIn("Do not substitute a planned keyframe", text)

    def test_keyframe_token_remains_free_reference(self) -> None:
        text = frame_input_instruction("KF2_CRACK", role="Last frame")
        self.assertIn("approved FREE target/reference keyframe `KF2_CRACK`", text)

    def test_missing_frame_fails_closed(self) -> None:
        text = frame_input_instruction("", role="First frame")
        self.assertIn("STOP", text)
        self.assertIn("repair the manifest", text)

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

        self.assertIn("Sequential-frame operator rule", output)
        self.assertIn("First frame: use the approved FREE target/reference keyframe `KF0_OPEN`", output)
        self.assertIn("First frame: upload the ACTUAL saved last usable frame from G1", output)
        self.assertIn("After G1 PASS", output)
        self.assertIn("G1_last_usable.png", output)
        self.assertIn("FRAME CHAIN FAIL", output)


if __name__ == "__main__":
    unittest.main()
