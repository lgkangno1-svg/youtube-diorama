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
    camera = data.get("camera_grammar") or {}
    runtime = data.get("runtime_strategy") or {}
    flow = data.get("flow_strategy") or {}
    scenes = data.get("scenes") or []

    if brand.get("hero_cat") != "HERO_CAT_V1":
        errors.append("brand_identity.hero_cat must be HERO_CAT_V1")
    if brand.get("kitchen_world") != "KITCHEN_WORLD_V1":
        errors.append("brand_identity.kitchen_world must be KITCHEN_WORLD_V1")
    if brand.get("shorts_visual_grammar") != "POV_PAWS_MICROWORLD_V1":
        errors.append("brand_identity.shorts_visual_grammar must be POV_PAWS_MICROWORLD_V1")

    if camera.get("mode") != "first_person_cat_pov":
        errors.append("camera_grammar.mode must be first_person_cat_pov")
    visible = camera.get("visible_cat_parts") or []
    if visible != ["front_paws_only"]:
        errors.append("camera_grammar.visible_cat_parts must be [front_paws_only]")
    if camera.get("hide_face_head_body") is not True:
        errors.append("camera_grammar.hide_face_head_body must be true")

    ratio = camera.get("hero_object_paw_width_ratio")
    if not (isinstance(ratio, list) and len(ratio) == 2):
        errors.append("camera_grammar.hero_object_paw_width_ratio must be [min,max]")
    else:
        try:
            lo, hi = float(ratio[0]), float(ratio[1])
            if lo <= 0 or hi <= 0 or lo > hi or hi > 0.50:
                errors.append("hero object must remain <=0.50 of one visible paw width")
        except (TypeError, ValueError):
            errors.append("camera_grammar.hero_object_paw_width_ratio must contain numbers")

    if flow.get("primary_model") != "veo-3.1-lite":
        errors.append("flow_strategy.primary_model must be veo-3.1-lite")
    if int(flow.get("output_count", 0) or 0) != 1:
        errors.append("flow_strategy.output_count must be 1")

    max_gens = int(flow.get("max_lite_generations_first_pass", 0) or 0)
    runtime_mode = str(runtime.get("mode") or "compact_h30")
    if max_gens > 4:
        errors.append("first-pass Lite generations must be <=4")
    if len(scenes) > 4:
        errors.append("manifest must contain at most 4 first-pass production scenes")

    if max_gens == 4 or len(scenes) == 4:
        if runtime_mode != "immersive_h40":
            errors.append("4-generation first pass requires runtime_strategy.mode=immersive_h40")
        if int(runtime.get("minimum_distinct_motion_beats", 0) or 0) < 4:
            errors.append("immersive_h40 requires minimum_distinct_motion_beats >=4")
        if not str(runtime.get("fourth_beat_value") or "").strip():
            errors.append("immersive_h40 requires a documented fourth_beat_value; G4 cannot be padding")

    for i, scene in enumerate(scenes, 1):
        if int(scene.get("generation_seconds", 0) or 0) != 8:
            errors.append(f"G{i} generation_seconds must be 8")

    expected_starts = {
        2: "ACTUAL_LAST_USABLE_FRAME_G1",
        3: "ACTUAL_LAST_USABLE_FRAME_G2",
        4: "ACTUAL_LAST_USABLE_FRAME_G3",
    }
    for index, expected in expected_starts.items():
        if len(scenes) >= index and str(scenes[index - 1].get("start_frame", "")) != expected:
            errors.append(f"G{index} must start from {expected}")

    serialized = yaml.safe_dump(data, allow_unicode=True).lower()
    for legacy_token in (
        "white_socked_orange_cat",
        "orange_cat_paw",
        "white-socked orange cat",
        "same orange tabby cat",
    ):
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
