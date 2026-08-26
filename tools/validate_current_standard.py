#!/usr/bin/env python3
"""Fail closed when an episode manifest does not match the current Tiny Cat Kitchen production standard."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"
CURRENT_NON_ULTRA_LITE_CREDITS_PER_GENERATION = 10


def load_episode(episode_id: str) -> dict[str, Any]:
    path = EPISODES / f"{episode_id}.yaml"
    if not path.exists():
        raise SystemExit(f"Missing episode manifest: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def to_int(value: Any, *, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    brand = data.get("brand_identity") or {}
    camera = data.get("camera_grammar") or {}
    runtime = data.get("runtime_strategy") or {}
    flow = data.get("flow_strategy") or {}
    scenes = data.get("scenes") or []
    keyframes = data.get("keyframes") or {}

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
    if to_int(flow.get("output_count")) != 1:
        errors.append("flow_strategy.output_count must be 1")

    if not isinstance(keyframes, dict) or not keyframes:
        errors.append("manifest must define non-empty keyframes for approved free First/Last frame targets")
        keyframes = {}
    else:
        for keyframe_name, keyframe_prompt in keyframes.items():
            if not str(keyframe_name or "").startswith("KF"):
                errors.append(f"keyframe name must start with KF: {keyframe_name}")
            if not str(keyframe_prompt or "").strip():
                errors.append(f"keyframe {keyframe_name} must contain a non-empty prompt")

    if not isinstance(scenes, list) or not scenes:
        errors.append("manifest must contain at least one production scene")
        scenes = []

    max_gens = to_int(flow.get("max_lite_generations_first_pass"))
    declared_budget = to_int(flow.get("non_ultra_credit_budget_first_pass"), default=-1)
    runtime_mode = str(runtime.get("mode") or "compact_h30")
    scene_count = len(scenes)

    if max_gens <= 0:
        errors.append("flow_strategy.max_lite_generations_first_pass must be a positive integer")
    elif max_gens > 4:
        errors.append("first-pass Lite generations must be <=4")

    if scene_count > 4:
        errors.append("manifest must contain at most 4 first-pass production scenes")

    # Spend plan must describe the exact manifest being prepared. A stale value here
    # can make the operator stop too early or spend a scene that was not intended.
    if max_gens > 0 and max_gens != scene_count:
        errors.append(
            "flow_strategy.max_lite_generations_first_pass must equal the number of manifest scenes "
            f"({max_gens} declared vs {scene_count} scenes)"
        )

    if max_gens > 0:
        expected_budget = max_gens * CURRENT_NON_ULTRA_LITE_CREDITS_PER_GENERATION
        if declared_budget != expected_budget:
            errors.append(
                "flow_strategy.non_ultra_credit_budget_first_pass must match the current Lite first-pass ceiling "
                f"({expected_budget} for {max_gens} generations at "
                f"{CURRENT_NON_ULTRA_LITE_CREDITS_PER_GENERATION} credits/generation; declared {declared_budget})"
            )

    if runtime_mode == "compact_h30":
        if scene_count != 3 or max_gens != 3:
            errors.append("compact_h30 must declare exactly 3 scenes and 3 first-pass Lite generations")
    elif runtime_mode == "immersive_h40":
        if scene_count != 4 or max_gens != 4:
            errors.append("immersive_h40 must declare exactly 4 scenes and 4 first-pass Lite generations")
        if to_int(runtime.get("minimum_distinct_motion_beats")) < 4:
            errors.append("immersive_h40 requires minimum_distinct_motion_beats >=4")
        if not str(runtime.get("fourth_beat_value") or "").strip():
            errors.append("immersive_h40 requires a documented fourth_beat_value; G4 cannot be padding")
    elif scene_count == 4 or max_gens == 4:
        # Unknown/custom runtime modes are allowed, but a 4-generation plan still needs
        # an explicit reason for the fourth spend.
        if not str(runtime.get("fourth_beat_value") or "").strip():
            errors.append("a 4-generation custom runtime requires a documented fourth_beat_value")

    allowed_generation_types = {"first_plus_last", "extend"}
    for i, scene in enumerate(scenes, 1):
        expected_id = f"G{i}"
        if str(scene.get("id") or "") != expected_id:
            errors.append(f"scene {i} id must be {expected_id}")

        generation_type = str(scene.get("generation_type") or "first_plus_last")
        if generation_type not in allowed_generation_types:
            errors.append(f"{expected_id} generation_type must be first_plus_last or extend")

        if to_int(scene.get("generation_seconds")) != 8:
            errors.append(f"{expected_id} generation_seconds must be 8")

        # A paid scene without a concrete motion instruction or a guard can still
        # produce a syntactically valid Flow Pack, but it leaves Veo to invent the
        # action/constraints and creates avoidable reroll risk. Fail before credits.
        if not str(scene.get("action") or "").strip():
            errors.append(f"{expected_id} action must be non-empty before paid generation")
        if not str(scene.get("action_guard") or "").strip():
            errors.append(f"{expected_id} action_guard must be non-empty before paid generation")

        if generation_type == "first_plus_last":
            start_frame = str(scene.get("start_frame") or "").strip()
            end_frame = str(scene.get("end_frame") or "").strip()
            if not start_frame:
                errors.append(f"{expected_id} first_plus_last requires start_frame")
            if not end_frame:
                errors.append(f"{expected_id} first_plus_last requires end_frame")

            # Any planned KF token shown in the generated Flow Pack must resolve to a
            # real approved free keyframe in this manifest. Otherwise a typo such as
            # KF2_CRCK can pass preparation and only fail when the operator is ready to
            # spend credits.
            for role, frame_token in (("start_frame", start_frame), ("end_frame", end_frame)):
                if frame_token.startswith("KF") and frame_token not in keyframes:
                    errors.append(
                        f"{expected_id} {role} references undefined keyframe {frame_token}; "
                        "define it in manifest.keyframes before preparing Flow files"
                    )
        elif generation_type == "extend" and not str(scene.get("source_scene") or "").strip():
            errors.append(f"{expected_id} extend requires source_scene")

    expected_starts = {
        2: "ACTUAL_LAST_USABLE_FRAME_G1",
        3: "ACTUAL_LAST_USABLE_FRAME_G2",
        4: "ACTUAL_LAST_USABLE_FRAME_G3",
    }
    for index, expected in expected_starts.items():
        if len(scenes) >= index:
            scene = scenes[index - 1]
            if str(scene.get("generation_type") or "first_plus_last") == "first_plus_last":
                if str(scene.get("start_frame") or "") != expected:
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
