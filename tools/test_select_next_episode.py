#!/usr/bin/env python3
from datetime import date
import unittest

from select_next_episode import final_score, seasonal_adjustment


DEFAULTS = {
    "max_boost_points": 8,
    "default_lead_days": 35,
    "default_tail_days": 7,
}


class SeasonalRankingTests(unittest.TestCase):
    def test_dated_event_prefers_pre_peak_sweet_spot(self) -> None:
        config = {
            "peak_start": "2026-09-25",
            "peak_end": "2026-09-25",
            "lead_days": 35,
            "tail_days": 5,
            "searchability": 20,
        }
        early, early_phase = seasonal_adjustment(config, date(2026, 8, 25), DEFAULTS)
        sweet, sweet_phase = seasonal_adjustment(config, date(2026, 9, 10), DEFAULTS)
        peak, peak_phase = seasonal_adjustment(config, date(2026, 9, 25), DEFAULTS)

        self.assertEqual((early, early_phase), (3.6, "early-lead:31d"))
        self.assertEqual((sweet, sweet_phase), (8.0, "sweet-spot:15d"))
        self.assertEqual((peak, peak_phase), (5.6, "in-peak"))
        self.assertGreater(sweet, peak)
        self.assertGreater(peak, early)

    def test_too_early_gets_no_calendar_only_boost(self) -> None:
        config = {
            "peak_start": "2026-12-24",
            "lead_days": 35,
            "searchability": 20,
        }
        boost, phase = seasonal_adjustment(config, date(2026, 8, 25), DEFAULTS)
        self.assertEqual(boost, 0.0)
        self.assertTrue(phase.startswith("too-early:"))

    def test_broad_food_season_can_enter_rotation_just_before_start(self) -> None:
        config = {
            "peak_start": "2026-09-01",
            "peak_end": "2026-10-31",
            "lead_days": 21,
            "searchability": 17,
        }
        boost, phase = seasonal_adjustment(config, date(2026, 8, 25), DEFAULTS)
        self.assertEqual((boost, phase), (5.8, "final-lead:7d"))

    def test_final_score_is_capped(self) -> None:
        self.assertEqual(final_score(96.0, 8.0), 100.0)


if __name__ == "__main__":
    unittest.main()
