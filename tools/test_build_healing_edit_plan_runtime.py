#!/usr/bin/env python3
from __future__ import annotations

import unittest

from build_healing_edit_plan import build


def manifest() -> dict:
    return {
        "episode_id": "TK-RUNTIME",
        "runtime_strategy": {
            "mode": "compact_h30",
            "target_final_runtime_seconds": [24, 27],
        },
        "post_production": {
            "preferred_playback_speed_range": [0.92, 1.0],
            "target_motion_density_pct_min": 80,
            "max_total_static_hold_seconds": 3,
            "narration_default": "none",
        },
        "scenes": [
            {"id": "G1", "purpose": "one", "generation_seconds": 8},
            {"id": "G2", "purpose": "two", "generation_seconds": 8},
            {"id": "G3", "purpose": "three", "generation_seconds": 8},
        ],
    }


def adaptive_h40_manifest() -> dict:
    data = manifest()
    data["runtime_strategy"] = {
        "mode": "immersive_h40",
        "target_final_runtime_seconds": [24, 35],
        "minimum_distinct_motion_beats": 3,
        "fourth_beat_optional_after_g3": True,
        "fourth_beat_value": "quiet same-world serving resolution if real G3 still benefits",
    }
    data["scenes"].append(
        {"id": "G4", "purpose": "optional four", "generation_seconds": 8}
    )
    return data


class HealingEditRuntimeTests(unittest.TestCase):
    def test_no_editorial_seconds_means_no_invented_holds(self) -> None:
        output = build(manifest())
        self.assertIn("Explicit editorial hold budget: 0.0s", output)
        self.assertNotIn("hero micro-detail hold", output)
        self.assertNotIn("quiet loop return", output)

    def test_runtime_mode_is_credit_tier_not_duration_promise(self) -> None:
        output = build(manifest())
        self.assertIn("mode name tracks first-pass credit tier, not promised final seconds", output)

    def test_explicit_hold_is_allowed_and_counted(self) -> None:
        data = manifest()
        data["editorial_seconds"] = {"opening_keyframe_hold": 0.5}
        output = build(data)
        self.assertIn("Explicit editorial hold budget: 0.5s", output)
        self.assertIn("OPEN scale-reveal keyframe", output)

    def test_infeasible_target_warns_instead_of_padding(self) -> None:
        data = manifest()
        data["runtime_strategy"]["target_final_runtime_seconds"] = [30, 36]
        output = build(data)
        self.assertIn("Runtime feasibility note", output)
        self.assertIn("Do not add fake holds", output)

    def test_adaptive_h40_core_plan_excludes_optional_g4_timeline(self) -> None:
        output = build(adaptive_h40_manifest())
        self.assertIn("Generated motion source in this core plan: 24.0s", output)
        self.assertIn("G1 — one", output)
        self.assertIn("G2 — two", output)
        self.assertIn("G3 — three", output)
        self.assertNotIn("G4 — optional four", output)
        self.assertIn("Adaptive H40: this plan intentionally includes only G1-G3", output)
        self.assertIn("## Optional G4 decision — after real G3 only", output)
        self.assertIn("derive its target from the actual saved G3 PASS frame", output)

    def test_non_optional_four_scene_plan_still_includes_g4(self) -> None:
        data = adaptive_h40_manifest()
        data["runtime_strategy"]["fourth_beat_optional_after_g3"] = False
        output = build(data)
        self.assertIn("Generated motion source in this core plan: 32.0s", output)
        self.assertIn("G4 — optional four", output)
        self.assertNotIn("## Optional G4 decision — after real G3 only", output)


if __name__ == "__main__":
    unittest.main()
