#!/usr/bin/env python3
"""Fail closed when an episode manifest does not match the current Tiny Cat Kitchen production standard."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"
CURRENT_NON_ULTRA_LITE_CREDITS_PER_GENERATION = 10
KEYFRAME_INDEX_RE = re.compile(r"^KF(\d+)(?:_|$)")
MAX_ALLOWED_VISUAL_CUTS_PER_8S = 1


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


def strict_manifest_int(value: Any) -> int | None:
    """Accept only YAML/Python integer scalars; reject bools, floats and numeric strings."""
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    return value


def to_float(value: Any, *, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def keyframe_index(name: str) -> int | None:
    match = KEYFRAME_INDEX_RE.match(name)
    return int(match.group(1)) if match else None


def explicit_editorial_hold_seconds(data: dict[str, Any], max_static: float) -> float:
    """Count only explicitly declared editorial holds; never assume padding exists."""
    editorial = data.get("editorial_seconds") or {}
    if not isinstance(editorial, dict):
        return 0.0
    total = 0.0
    for value in editorial.values():
        seconds = to_float(value, default=0.0)
        if seconds > 0:
            total += seconds
    return min(total, max(0.0, max_static))


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    brand = data.get("brand_identity") or {}
    camera = data.get("camera_grammar") or {}
    runtime = data.get("runtime_strategy") or {}
    flow = data.get("flow_strategy") or {}
    post = data.get("post_production") or {}
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

    output_count = strict_manifest_int(flow.get("output_count"))
    if output_count != 1:
        errors.append("flow_strategy.output_count must be the integer 1")

    raw_max_cuts = flow.get("max_visual_cuts_per_8s_generation")
    max_cuts = strict_manifest_int(raw_max_cuts)
    if max_cuts is None:
        errors.append("flow_strategy.max_visual_cuts_per_8s_generation must be an integer 0 or 1")
    elif max_cuts < 0 or max_cuts > MAX_ALLOWED_VISUAL_CUTS_PER_8S:
        errors.append(
            "flow_strategy.max_visual_cuts_per_8s_generation must be 0 or 1 for calm long-take pacing"
        )

    preferred_actions = strict_manifest_int(flow.get("preferred_action_count_per_generation"))
    if preferred_actions != 1:
        errors.append("flow_strategy.preferred_action_count_per_generation must be the integer 1")

    indexed_keyframes: dict[int, str] = {}
    duplicate_keyframe_indices: set[int] = set()
    if not isinstance(keyframes, dict) or not keyframes:
        errors.append("manifest must define non-empty keyframes for approved free First/Last frame targets")
        keyframes = {}
    else:
        for keyframe_name, keyframe_prompt in keyframes.items():
            name = str(keyframe_name or "")
            index = keyframe_index(name)
            if index is None:
                errors.append(f"keyframe name must start with KF<number>: {keyframe_name}")
            elif index in indexed_keyframes:
                duplicate_keyframe_indices.add(index)
                errors.append(
                    f"keyframe numeric index KF{index} is duplicated by {indexed_keyframes[index]} and {name}"
                )
            else:
                indexed_keyframes[index] = name
            if not str(keyframe_prompt or "").strip():
                errors.append(f"keyframe {keyframe_name} must contain a non-empty prompt")

    if not isinstance(scenes, list) or not scenes:
        errors.append("manifest must contain at least one production scene")
        scenes = []

    raw_max_gens = flow.get("max_lite_generations_first_pass")
    max_gens_value = strict_manifest_int(raw_max_gens)
    if max_gens_value is None:
        errors.append("flow_strategy.max_lite_generations_first_pass must be an integer")
        max_gens = 0
    else:
        max_gens = max_gens_value

    raw_budget = flow.get("non_ultra_credit_budget_first_pass")
    budget_value = strict_manifest_int(raw_budget)
    if budget_value is None:
        errors.append("flow_strategy.non_ultra_credit_budget_first_pass must be an integer")
        declared_budget = -1
    else:
        declared_budget = budget_value

    runtime_mode = str(runtime.get("mode") or "compact_h30")
    scene_count = len(scenes)

    if max_gens <= 0:
        errors.append("flow_strategy.max_lite_generations_first_pass must be a positive integer")
    elif max_gens > 4:
        errors.append("first-pass Lite generations must be <=4")

    if scene_count > 4:
        errors.append("manifest must contain at most 4 first-pass production scenes")

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

    progressive_gate = flow.get("progressive_spend_gate") or {}
    required_pass_gates = {
        "g2_requires_g1_pass": scene_count >= 2,
        "g3_requires_g2_pass": scene_count >= 3,
        "g4_requires_g3_pass": scene_count >= 4,
    }
    for gate_name, required in required_pass_gates.items():
        if required and progressive_gate.get(gate_name) is not True:
            errors.append(f"flow_strategy.progressive_spend_gate.{gate_name} must be true")
    if progressive_gate.get("stop_if_pov_scale_anatomy_or_premise_fails") is not True:
        errors.append(
            "flow_strategy.progressive_spend_gate.stop_if_pov_scale_anatomy_or_premise_fails must be true"
        )
    if progressive_gate.get("reroll_only_structural_failure") is not True:
        errors.append("flow_strategy.progressive_spend_gate.reroll_only_structural_failure must be true")

    sequential_chain = flow.get("sequential_chain") or {}
    expected_chain_sources = {
        2: "save_actual_last_usable_frame_from_G1",
        3: "save_actual_last_usable_frame_from_G2",
        4: "save_actual_last_usable_frame_from_G3",
    }
    for scene_index, expected_source in expected_chain_sources.items():
        if scene_count >= scene_index:
            scene = scenes[scene_index - 1] or {}
            if str(scene.get("generation_type") or "first_plus_last") == "first_plus_last":
                key = f"g{scene_index}_start_source"
                if sequential_chain.get(key) != expected_source:
                    errors.append(f"flow_strategy.sequential_chain.{key} must be {expected_source}")

    if runtime_mode == "compact_h30":
        if scene_count != 3 or max_gens != 3:
            errors.append("compact_h30 must declare exactly 3 scenes and 3 first-pass Lite generations")
    elif runtime_mode == "immersive_h40":
        if scene_count != 4 or max_gens != 4:
            errors.append("immersive_h40 must declare exactly 4 scenes and 4 first-pass Lite generations")
        minimum_beats = strict_manifest_int(runtime.get("minimum_distinct_motion_beats"))
        if minimum_beats is None:
            errors.append("runtime_strategy.minimum_distinct_motion_beats must be an integer")
        elif minimum_beats < 4:
            errors.append("immersive_h40 requires minimum_distinct_motion_beats >=4")
        if not str(runtime.get("fourth_beat_value") or "").strip():
            errors.append("immersive_h40 requires a documented fourth_beat_value; G4 cannot be padding")
    elif scene_count == 4 or max_gens == 4:
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

        generation_seconds = strict_manifest_int(scene.get("generation_seconds"))
        if generation_seconds != 8:
            errors.append(f"{expected_id} generation_seconds must be the integer 8")

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

            for role, frame_token in (("start_frame", start_frame), ("end_frame", end_frame)):
                if frame_token.startswith("KF") and frame_token not in keyframes:
                    errors.append(
                        f"{expected_id} {role} references undefined keyframe {frame_token}; "
                        "define it in manifest.keyframes before preparing Flow files"
                    )
        elif generation_type == "extend" and not str(scene.get("source_scene") or "").strip():
            errors.append(f"{expected_id} extend requires source_scene")

    # Runtime feasibility is a no-padding invariant. H30/H40 denote the current
    # 30/40-credit first-pass ceilings, not guaranteed 30/40-second final lengths.
    # Only generated motion, allowed natural slowdown, and explicitly declared
    # editorial holds may contribute to the maximum target runtime.
    if scenes:
        raw_motion = sum(max(0.0, to_float((scene or {}).get("generation_seconds"), default=0.0)) for scene in scenes)
        speed_range = post.get("preferred_playback_speed_range", [1.0, 1.0])
        min_speed = 1.0
        max_speed = 1.0
        speed_range_valid = True
        if not (isinstance(speed_range, list) and len(speed_range) == 2):
            errors.append("post_production.preferred_playback_speed_range must be [min,max]")
            speed_range_valid = False
        else:
            try:
                min_speed = float(speed_range[0])
                max_speed = float(speed_range[1])
            except (TypeError, ValueError):
                errors.append("post_production.preferred_playback_speed_range must contain numbers")
                speed_range_valid = False

        if speed_range_valid:
            if min_speed <= 0 or min_speed > 1.0:
                errors.append("post_production.preferred_playback_speed_range minimum must be >0 and <=1.0")
                speed_range_valid = False
            if max_speed <= 0 or max_speed > 1.0:
                errors.append("post_production.preferred_playback_speed_range maximum must be >0 and <=1.0")
                speed_range_valid = False
            if min_speed > max_speed:
                errors.append("post_production.preferred_playback_speed_range must satisfy min <= max")
                speed_range_valid = False

        if not speed_range_valid:
            # Invalid playback metadata must never increase the calculated runtime
            # allowance. Fall back to 1.0x for conservative feasibility math.
            min_speed = 1.0

        max_static = max(0.0, to_float(post.get("max_total_static_hold_seconds"), default=0.0))
        explicit_holds = explicit_editorial_hold_seconds(data, max_static)
        feasible_max = (raw_motion / min_speed if min_speed > 0 else raw_motion) + explicit_holds

        preferred_runtime = runtime.get("target_final_runtime_seconds") or post.get("preferred_final_runtime_seconds")
        if isinstance(preferred_runtime, list) and len(preferred_runtime) == 2:
            target_min = to_float(preferred_runtime[0], default=0.0)
            target_max = to_float(preferred_runtime[1], default=0.0)
            if target_min <= 0 or target_max < target_min:
                errors.append("final runtime target must be a positive [min,max] range")
            elif target_min > feasible_max + 0.05:
                errors.append(
                    "final runtime target is infeasible without padding: "
                    f"minimum {target_min:.1f}s exceeds feasible ~{feasible_max:.1f}s from generated motion, "
                    "allowed slowdown, and explicitly declared holds"
                )

        length_target = to_float(data.get("length_target_seconds"), default=0.0)
        if length_target > feasible_max + 0.05:
            errors.append(
                "length_target_seconds is infeasible without padding: "
                f"{length_target:.1f}s exceeds feasible ~{feasible_max:.1f}s"
            )

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

    all_first_plus_last = bool(scenes) and all(
        str((scene or {}).get("generation_type") or "first_plus_last") == "first_plus_last"
        for scene in scenes
    )
    if all_first_plus_last and keyframes and not duplicate_keyframe_indices:
        expected_indices = list(range(scene_count + 1))
        actual_indices = sorted(indexed_keyframes)
        if actual_indices != expected_indices:
            errors.append(
                "all-first_plus_last manifests must define contiguous planned keyframe indices "
                f"KF0..KF{scene_count} exactly; found {actual_indices}"
            )
        if all(index in indexed_keyframes for index in expected_indices):
            g1_start = str((scenes[0] or {}).get("start_frame") or "")
            expected_start = indexed_keyframes[0]
            if g1_start != expected_start:
                errors.append(f"G1 must start from planned keyframe index KF0 ({expected_start})")
            for index, scene in enumerate(scenes, 1):
                expected_end = indexed_keyframes[index]
                actual_end = str((scene or {}).get("end_frame") or "")
                if actual_end != expected_end:
                    errors.append(
                        f"G{index} end_frame must target planned keyframe index KF{index}: "
                        f"expected {expected_end}, got {actual_end or '<missing>'}"
                    )

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
