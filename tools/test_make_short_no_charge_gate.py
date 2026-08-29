#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


class MakeShortNoChargeGateTests(unittest.TestCase):
    def test_make_short_does_not_call_keyframes_unconditionally_free(self) -> None:
        source = (Path(__file__).resolve().parent / "make_short.ps1").read_text(encoding="utf-8")

        self.assertIn("Nano Banana 2 Lite", source)
        self.assertIn("UI currently shows no charge", source)
        self.assertIn("STOP instead of spending image credits", source)
        self.assertNotIn("Approve the free keyframes/contact sheet", source)


if __name__ == "__main__":
    unittest.main()
