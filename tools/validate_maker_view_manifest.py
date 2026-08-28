#!/usr/bin/env python3
"""Canonical maker-view adapter around the legacy structural manifest validator.

The repository still carries compatibility enum values such as
`POV_PAWS_MICROWORLD_V1` / `first_person_cat_pov`, but the accepted product
semantics are Mini Forest-style observational miniature making with feline
front paws only. This adapter fail-closes on those current semantics first,
then delegates the remaining structural/runtime/spend checks to the mature
legacy validator without letting its compatibility-only POV field regress the
creative standard.
"""
from __future__ import annotations

import argparse
import copy
from typing import Any

from validate_current_standard import load_episode, validate as validate_structural

CURRENT_VISUAL_INTENT = "mini_forest_style_paws_only_miniature_making"
CURRENT_CAMERA_SEMANTIC = "mini_forest_style_observational_maker_view"
CURRENT_STOP_GATE = "stop_if_maker_view_scale_anatomy_or_premise_fails"
LEGACY_STOP_GATE = "stop_if_pov_scale_anatomy_or_premise_fails"
SAFE_PAW_ACTIONS = {"nudge", "press", "pat", "roll", "steady", "slide", "tap", "push"}


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    brand = data.get("brand_identity") or {}
    camera = data.get("camera_grammar") or {}
    flow = data.get("flow_strategy") or {}
    progressive_gate = flow.get("progressive_spend_gate") or {}
    scenes = data.get("scenes") or []

    if brand.get("visual_intent") != CURRENT_VISUAL_INTENT:
        errors.append(
            f"brand_identity.visual_intent must be {CURRENT_VISUAL_INTENT}; "
            "legacy POV enum names are compatibility labels only"
        )

    if camera.get("semantic_override") != CURRENT_CAMERA_SEMANTIC:
        errors.append(
            f"camera_grammar.semantic_override must be {CURRENT_CAMERA_SEMANTIC}"
        )
    if camera.get("first_person_required") is not False:
        errors.append(
            "camera_grammar.first_person_required must be false; literal cat-eye POV is optional, not mandatory"
        )
    preferred_angles = camera.get("preferred_angles") or []
    if not isinstance(preferred_angles, list) or "high_oblique_maker_view" not in preferred_angles:
        errors.append(
            "camera_grammar.preferred_angles must include high_oblique_maker_view"
        )

    if progressive_gate.get(CURRENT_STOP_GATE) is not True:
        errors.append(
            f"flow_strategy.progressive_spend_gate.{CURRENT_STOP_GATE} must be true"
        )
    if progressive_gate.get(LEGACY_STOP_GATE) is True:
        errors.append(
            f"legacy progressive-spend gate {LEGACY_STOP_GATE} must not be active on a current maker-view manifest"
        )

    # Candidate-level action safety is not enough: a manifest can be edited after
    # selection. Fail closed again at the final paid-generation boundary so every
    # scene explicitly declares exactly one feline-safe active action family.
    if not isinstance(scenes, list) or not scenes:
        errors.append("manifest must contain production scenes with explicit paw_action_family")
    else:
        for i, scene in enumerate(scenes, 1):
            scene_id = str((scene or {}).get("id") or f"G{i}")
            action_family = (scene or {}).get("paw_action_family")
            if not isinstance(action_family, list) or len(action_family) != 1:
                errors.append(
                    f"{scene_id}.paw_action_family must contain exactly one active action"
                )
                continue
            action = str(action_family[0] or "").strip().lower()
            if action not in SAFE_PAW_ACTIONS:
                errors.append(
                    f"{scene_id}.paw_action_family action '{action}' is not feline-safe; "
                    f"allowed: {', '.join(sorted(SAFE_PAW_ACTIONS))}"
                )

    if errors:
        return errors

    # Reuse the existing mature structural validator for runtime, credit,
    # keyframe, sequential-frame, narration, and scene invariants. Translate
    # only the two compatibility fields that validator historically expected.
    structural_data = copy.deepcopy(data)
    structural_camera = structural_data.setdefault("camera_grammar", {})
    structural_camera["mode"] = "first_person_cat_pov"
    structural_gate = structural_data.setdefault("flow_strategy", {}).setdefault(
        "progressive_spend_gate", {}
    )
    structural_gate[LEGACY_STOP_GATE] = True

    return validate_structural(structural_data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_id")
    args = parser.parse_args()

    data = load_episode(args.episode_id)
    errors = validate(data)
    if errors:
        print(f"CURRENT MAKER-VIEW STANDARD FAIL — {args.episode_id}")
        for error in errors:
            print(f"- {error}")
        print("Refresh this manifest before preparing Flow files. No credits were spent.")
        raise SystemExit(2)

    print(f"CURRENT MAKER-VIEW STANDARD PASS — {args.episode_id}")


if __name__ == "__main__":
    main()
