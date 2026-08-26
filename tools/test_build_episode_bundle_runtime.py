#!/usr/bin/env python3
"""Small regression checks for manifest-aware runtime guidance."""
from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).with_name("build_episode_bundle.py")
    spec = importlib.util.spec_from_file_location("build_episode_bundle", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load build_episode_bundle.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()

    h30 = module.runtime_guidance({"runtime_strategy": {"mode": "compact_h30"}, "scenes": [{}, {}, {}]})
    assert "compact_h30" in h30
    assert "finish after G3" in h30
    assert "do not add a G4" in h30

    h40 = module.runtime_guidance(
        {
            "runtime_strategy": {
                "mode": "immersive_h40",
                "fourth_beat_value": "quiet world-resolution",
            },
            "scenes": [{}, {}, {}, {}],
        }
    )
    assert "immersive_h40" in h40
    assert "G4" in h40
    assert "quiet world-resolution" in h40
    assert "Do not drop it merely to force H30" in h40

    adaptive = module.runtime_guidance({"runtime_strategy": {"mode": "custom"}, "scenes": [{}, {}]})
    assert "custom" in adaptive
    assert "2 planned scene(s)" in adaptive
    assert "do not assume a fixed H30 or H40" in adaptive

    print("PASS: runtime guidance follows manifest mode")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
