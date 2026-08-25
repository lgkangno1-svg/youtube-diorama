#!/usr/bin/env python3
from datetime import date
import unittest

from select_next_episode import final_score, seasonal_adjustment


DEFAULTS = {
    "max_boost_points": 8,
    "default_lead_days": 35,
    "default_tail_days": 7,
}


def candidate(candidate_id: str, **seasonality):
    return {
        "id": candidate_id,
        "seasonality": seasonality,
    }


def ledger(candidate_id: str, checked_at: str = "2026-08-25", max_age_days: int = 14):
    return {
        "default_max_age_days": max_age_days,
        "evidence": {
            candidate_id: {
                "checked_at": checked_at,
            }
        },
    }


class SeasonalRankingTests(unittest.TestCase):
    def test_dated_event_prefers_pre_peak_sweet_spot(self) -> None:
        item = candidate(
            "IDEA-T",
            peak_start="2026-09-25",
            peak_end="2026-09-25",
            lead_days=35,
            tail_days=5,
            searchability=20,
        )
        evidence = ledger("IDEA-T", checked_at="2026-09-01", max_age_days=30)

        early, early_phase, early_evidence = seasonal_adjustment(
            item, date(2026, 9, 1), DEFAULTS, evidence
        )
        sweet, sweet_phase, sweet_evidence = seasonal_adjustment(
            item, date(2026, 9, 10), DEFAULTS, evidence
        )
        peak, peak_phase, peak_evidence = seasonal_adjustment(
            item, date(2026, 9, 25), DEFAULTS, evidence
        )

        self.assertEqual((early, early_phase), (3.6, "early-lead:24d"))
        self.assertEqual((sweet, sweet_phase), (8.0, "sweet-spot:15d"))
        self.assertEqual((peak, peak_phase), (5.6, "in-peak"))
        self.assertTrue(early_evidence.startswith("evidence-fresh:"))
        self.assertTrue(sweet_evidence.startswith("evidence-fresh:"))
        self.assertTrue(peak_evidence.startswith("evidence-fresh:"))
        self.assertGreater(sweet, peak)
        self.assertGreater(peak, early)

    def test_too_early_gets_no_calendar_only_boost(self) -> None:
        item = candidate(
            "IDEA-T",
            peak_start="2026-12-24",
            lead_days=35,
            searchability=20,
        )
        boost, phase, evidence_state = seasonal_adjustment(
            item,
            date(2026, 8, 25),
            DEFAULTS,
            ledger("IDEA-T"),
        )
        self.assertEqual(boost, 0.0)
        self.assertTrue(phase.startswith("too-early:"))
        self.assertEqual(evidence_state, "evidence-fresh:0d")

    def test_broad_food_season_can_enter_rotation_just_before_start(self) -> None:
        item = candidate(
            "IDEA-T",
            peak_start="2026-09-01",
            peak_end="2026-10-31",
            lead_days=21,
            searchability=17,
        )
        boost, phase, evidence_state = seasonal_adjustment(
            item,
            date(2026, 8, 25),
            DEFAULTS,
            ledger("IDEA-T"),
        )
        self.assertEqual((boost, phase), (5.8, "final-lead:7d"))
        self.assertEqual(evidence_state, "evidence-fresh:0d")

    def test_stale_evidence_disables_only_seasonal_boost(self) -> None:
        item = candidate(
            "IDEA-T",
            peak_start="2026-09-25",
            peak_end="2026-09-25",
            lead_days=35,
            searchability=20,
        )
        boost, phase, evidence_state = seasonal_adjustment(
            item,
            date(2026, 9, 20),
            DEFAULTS,
            ledger("IDEA-T", checked_at="2026-08-25", max_age_days=14),
        )
        self.assertEqual(boost, 0.0)
        self.assertEqual(phase, "final-lead:5d")
        self.assertEqual(evidence_state, "evidence-stale:26d")

    def test_missing_evidence_disables_only_seasonal_boost(self) -> None:
        item = candidate(
            "IDEA-T",
            peak_start="2026-09-25",
            searchability=20,
        )
        boost, phase, evidence_state = seasonal_adjustment(
            item,
            date(2026, 9, 10),
            DEFAULTS,
            {"default_max_age_days": 14, "evidence": {}},
        )
        self.assertEqual(boost, 0.0)
        self.assertEqual(phase, "sweet-spot:15d")
        self.assertEqual(evidence_state, "evidence-missing")

    def test_final_score_is_capped(self) -> None:
        self.assertEqual(final_score(96.0, 8.0), 100.0)


if __name__ == "__main__":
    unittest.main()
