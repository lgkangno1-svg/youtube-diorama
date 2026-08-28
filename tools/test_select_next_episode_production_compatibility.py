#!/usr/bin/env python3
import unittest

from select_next_episode import production_compatible


def candidate(**overrides):
    data = {
        "visual_grammar": "POV_PAWS_MICROWORLD_V1",
        "hero_scale": "12mm; 0.18-0.32 paw width",
        "paw_action_family": ["nudge", "steady", "slide"],
        "runtime_prior": "immersive_h40",
    }
    data.update(overrides)
    return data


class ProductionCompatibilityTests(unittest.TestCase):
    def test_current_maker_view_candidate_passes(self) -> None:
        self.assertEqual(production_compatible(candidate()), (True, "maker-view-compatible"))

    def test_legacy_enum_alone_does_not_excuse_human_like_action(self) -> None:
        ok, reason = production_compatible(candidate(paw_action_family=["pinch", "slide"]))
        self.assertFalse(ok)
        self.assertEqual(reason, "unsafe-paw-action:pinch")

    def test_candidate_over_half_paw_width_fails(self) -> None:
        ok, reason = production_compatible(candidate(hero_scale="18mm; 0.55 paw width"))
        self.assertFalse(ok)
        self.assertEqual(reason, "hero-scale-too-large:0.55-paw-width")

    def test_missing_paw_width_ratio_fails_closed(self) -> None:
        ok, reason = production_compatible(candidate(hero_scale="12mm tiny object"))
        self.assertFalse(ok)
        self.assertEqual(reason, "paw-width-ratio-missing")

    def test_supported_compact_runtime_passes(self) -> None:
        ok, reason = production_compatible(
            candidate(hero_scale="8mm; <=0.35 paw width", paw_action_family=["roll", "tap"], runtime_prior="compact_h30")
        )
        self.assertTrue(ok)
        self.assertEqual(reason, "maker-view-compatible")


if __name__ == "__main__":
    unittest.main()
