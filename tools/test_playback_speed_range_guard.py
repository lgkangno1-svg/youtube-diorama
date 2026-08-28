#!/usr/bin/env python3
from __future__ import annotations

import copy
import unittest

from test_validate_current_standard import base_manifest
from validate_current_standard import validate


class PlaybackSpeedRangeGuardTests(unittest.TestCase):
    def test_valid_range_passes(self) -> None:
        data = copy.deepcopy(base_manifest())
        data["post_production"] = {"preferred_playback_speed_range": [0.92, 1.0]}
        self.assertEqual(validate(data), [])

    def test_reversed_range_fails(self) -> None:
        data = copy.deepcopy(base_manifest())
        data["post_production"] = {"preferred_playback_speed_range": [1.0, 0.92]}
        errors = validate(data)
        self.assertIn("post_production.preferred_playback_speed_range must satisfy min <= max", errors)

    def test_maximum_above_realtime_fails(self) -> None:
        data = copy.deepcopy(base_manifest())
        data["post_production"] = {"preferred_playback_speed_range": [0.92, 1.10]}
        errors = validate(data)
        self.assertIn(
            "post_production.preferred_playback_speed_range maximum must be >0 and <=1.0",
            errors,
        )

    def test_malformed_range_fails_closed(self) -> None:
        data = copy.deepcopy(base_manifest())
        data["post_production"] = {"preferred_playback_speed_range": [0.92]}
        errors = validate(data)
        self.assertIn("post_production.preferred_playback_speed_range must be [min,max]", errors)

    def test_non_numeric_range_fails_closed(self) -> None:
        data = copy.deepcopy(base_manifest())
        data["post_production"] = {"preferred_playback_speed_range": ["slow", 1.0]}
        errors = validate(data)
        self.assertIn("post_production.preferred_playback_speed_range must contain numbers", errors)


if __name__ == "__main__":
    unittest.main()
