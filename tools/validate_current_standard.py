#!/usr/bin/env python3
"""Fail closed when an episode manifest does not match the current Tiny Cat Kitchen production standard."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"


def load_episode(episode_id: str) -> dict[str, Any]:
    path = EPISODES / f"{episode_id}.yaml"
    if not path.exists():
        raise SystemExit(f"Missing episode manifest: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    brand = data.get("brand_identity") or {}
    flow = data.get("flow_strategy") or {}
    scenes = data.get("scenes") or []
    exception = bool(flow.get("verified_winner_exception"))

    if brand.get("hero_cat") != "HERO_CAT_V1":
        errors.append("brand_identity.hero_cat must be HERO_CAT_V1")
    if brand.get("kitchen_world") != "KITCHEN_WORLD_V1":
        errors.append("brand_identity.kitchen_world must be KITCHEN_WORLD_V1")
    if flow.get("primary_model") != "veo-3.1-lite":
        errors.append("flow_strategy.primary_model must be veo-3.1-lite")
    if int(flow.get("output_count", 0) or 0) != 1:
        errors.append("flow_strategy.output_count must be 1")

    max_gens = int(flow.get("max_lite_generations_first_pass", 0) or 0)
    if max_gens > 3 and not exception:
        errors.append("first-pass Lite generations must be <=3 unless verified_winner_exception=true")
    if len(scenes) > 3 and not exception:
        errors.append("manifest has more than 3 production scenes without verified winner exception")

    for i, scene in enumerate(scenes[:3], 1):
        if int(scene.get("generation_seconds", 0) or 0) != 8:
            errors.append(f"G{i} generation_seconds must be 8")

    if len(scenes) >= 2 and str(scenes[1].get("start_frame", "")) != "ACTUAL_LAST_USABLE_FRAME_G1":
        errors.append("G2 must start from ACTUAL_LAST_USABLE_FRAME_G1")
    if len(scenes) >= 3 and str(scenes[2].get("start_frame", "")) != "ACTUAL_LAST_USABLE_FRAME_G2":
        errors.append("G3 must start from ACTUAL_LAST_USABLE_FRAME_G2")

    serialized = yaml.safe_dump(data, allow_unicode=True).lower()
    for legacy_token in ("white_socked_orange_cat", "orange_cat_paw", "white-socked orange cat"):
        if legacy_token in serialized:
            errors.append(f"legacy hero-cat description found: {legacy_token}")

    narration = str(flow.get("narration_policy", data.get("post_production", {}).get("narration_default", ""))).lower()
    if narration and "none" not in narration:
        errors.append("default narration must remain none unless the selected episode explicitly documents a justified exception")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_id")
    args = parser.parse_args()

    data = load_episode(args.episode_id)
    errors = validate(data)
    if errors:
        print(f"CURRENT STANDARD FAIL — {args.episode_id}")
        for error in errors:
            print(f"- {error}")
        print("Refresh this manifest before preparing Flow files. No credits were spent.")
        raise SystemExit(2)

    print(f"CURRENT STANDARD PASS — {args.episode_id}")


if __name__ == "__main__":
    main()
