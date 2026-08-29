#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parent


class OperatorCardFirstPathTests(unittest.TestCase):
    def test_make_next_short_surfaces_operator_card_as_primary_action(self) -> None:
        source = (TOOLS / "make_next_short.ps1").read_text(encoding="utf-8")
        self.assertIn("YOUR NEXT ACTION", source)
        self.assertIn("production/${EpisodeId}_OPERATOR_CARD.md", source)
        self.assertIn("Operator Card is the primary fast-production surface", source)
        self.assertIn("hook → visible transformation → scale proof → payoff", source)

    def test_make_short_prefers_operator_card_but_keeps_generated_fallbacks(self) -> None:
        source = (TOOLS / "make_short.ps1").read_text(encoding="utf-8")
        self.assertIn("PRIMARY RUNBOOK", source)
        self.assertIn("production/${EpisodeId}_OPERATOR_CARD.md first", source)
        self.assertIn("Fallback/reference only", source)
        self.assertIn("generated/${EpisodeId}_bundle.md", source)
        self.assertIn("generated/${EpisodeId}_flow_pack.md", source)


if __name__ == "__main__":
    unittest.main()
