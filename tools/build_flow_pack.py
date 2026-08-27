#!/usr/bin/env python3
"""Build a low-token Google Flow prompt pack from one episode YAML manifest.

The output is deterministic. It never spends Flow credits.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

POV_STYLE = (
    "True first-person POV of the cat itself, vertical 9:16, camera at the cat's working position looking slightly down at the tabletop. "
    "Only one or two cream-and-pale-ginger real feline front paws may enter from the bottom edge. "
    "Never show the cat's face, eyes, ears, head, chest, torso, tail or full body. "
    "The hero food or object must look absurdly tiny compared with one paw, preferably about 15-50 percent of visible paw width. "
    "Macro miniature diorama workbench, shallow depth of field, warm natural light, tactile realistic materials and physics. "
    "No human hands, no fingers, no thumbs, no extra limbs, no text, no logos, no watermark. "
    "Feline paws nudge, press, pat, roll, steady, slide or tap; they do not grip tools like human hands."
)

LOCK = (
    "Preserve exact paw fur pattern, first-person camera position, cookware, hero-object scale, workbench layout, lighting and food/object state. "
    "Do not enlarge the hero object, reveal the cat's body, create human-like gripping, duplicate props, or morph ingredients unless the action explicitly requires it."
)


def humanize(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("_", " ").strip()


def get_scene_seconds(scene: dict[str, Any]) -> int:
    value = scene.get("generation_seconds", 8)
    try:
        value = int(value)
    except (TypeError, ValueError):
        value = 8
    return value if value in {4, 6, 8} else 8


def ordered_keyframes(data: dict[str, Any]) -> list[str]:
    explicit = list((data.get("keyframes") or {}).keys())
    if explicit:
        return explicit
    return ["KF0_OPEN", "KF1_TRANSFORM", "KF2_PAYOFF", "KF3_WORLD_RESOLUTION"]


def frame_text(data: dict[str, Any], name: str) -> str:
    explicit = (data.get("keyframes") or {}).get(name)
    if explicit:
        return humanize(explicit)
    return humanize(name)


def scale_clause(data: dict[str, Any]) -> str:
    grammar = data.get("camera_grammar") or {}
    mm = grammar.get("hero_object_size_mm")
    ratio = grammar.get("hero_object_paw_width_ratio")
    parts = []
    if isinstance(mm, list) and len(mm) == 2:
        parts.append(f"Hero object target size is roughly {mm[0]}-{mm[1]} mm")
    elif data.get("constraint"):
        parts.append(f"Episode scale constraint: {humanize(data.get('constraint'))}")
    if isinstance(ratio, list) and len(ratio) == 2:
        parts.append(f"it should read as about {ratio[0]}-{ratio[1]} of one visible paw width")
    if not parts:
        return "Make the hero object immediately read as much smaller than one paw."
    return "; ".join(parts) + "."


def frame_input_instruction(frame_name: Any, *, role: str) -> str:
    """Turn manifest frame tokens into explicit operator input instructions.

    The manifest intentionally uses symbolic ACTUAL_LAST_USABLE_FRAME_Gn tokens so
    planned continuity never pretends to know the real generated frame. The Flow
    pack should translate those tokens into an action the operator can perform.
    """
    token = str(frame_name or "").strip()
    if not token:
        return f"{role}: not specified in manifest — STOP and repair the manifest before spending credits."

    prefix = "ACTUAL_LAST_USABLE_FRAME_"
    if token.startswith(prefix):
        source_scene = token[len(prefix) :]
        return (
            f"{role}: upload the ACTUAL saved last usable frame from {source_scene}. "
            "Do not substitute a planned keyframe or regenerate the previous scene just to create a cleaner bridge."
        )

    if token.startswith("KF"):
        return f"{role}: use the approved FREE target/reference keyframe `{token}` from this pack."

    return f"{role}: use the manifest-specified frame source `{token}` after visually confirming it is the intended approved input."


def next_scene_uses_actual_frame(scenes: list[dict[str, Any]], index: int, scene_id: str) -> bool:
    if index + 1 >= len(scenes):
        return False
    next_start = str((scenes[index + 1] or {}).get("start_frame") or "")
    return next_start == f"ACTUAL_LAST_USABLE_FRAME_{scene_id}"


def build(data: dict[str, Any]) -> str:
    episode_id = data["episode_id"]
    refs = ", ".join(data.get("references", [])) or "HERO_CAT_V1_PAWS, POV_PAWS_MICROWORLD_V1, KITCHEN_WORLD_V1"
    strategy = data.get("flow_strategy", {}) or {}
    runtime = data.get("runtime_strategy", {}) or {}
    scenes = data.get("scenes", []) or []
    kfs = ordered_keyframes(data)
    planned = int(strategy.get("max_lite_generations_first_pass") or len(scenes) or 3)
    non_ultra = int(strategy.get("non_ultra_credit_budget_first_pass") or planned * 10)
    pacing = humanize(strategy.get("pacing") or "healing motion dense")
    max_cuts = strategy.get("max_visual_cuts_per_8s_generation")
    narration_policy = humanize(strategy.get("narration_policy") or "none by default")
    audio_policy = humanize(strategy.get("audio_policy") or "close tactile ASMR")
    scale = scale_clause(data)

    lines: list[str] = [
        f"# {episode_id} — Flow Pack",
        "",
        "> Deterministic prompt pack. No LLM rewrite, Flow generation, or upload is performed here.",
        "",
        "## Flow UI preflight — do this before every paid generation",
        "",
        "- Confirm you are in NEW VIDEO GENERATION, not an existing-video edit/modify screen.",
        "- If the prompt says the equivalent of 'describe changes', an existing clip is open for editing, or Omni Flash is active for video edit, STOP and return to the standard new-video prompt box.",
        "- Open generation settings → Video → explicitly select Veo 3.1 Lite.",
        "- Confirm 9:16 and output count = 1.",
        "- Prefer 8s. If the 4s/6s/8s selector is absent, verify whether the selected mode is an official 8s-only mode rather than assuming an error.",
        "- Confirm the displayed credit cost before pressing Generate. Never treat Omni Flash video edit as a 10-credit Lite scene.",
        "- See docs/26_flow_ui_mode_preflight.md for the current UI-state decision rule.",
        "",
        "## Fixed settings",
        "",
        "- Primary model: Veo 3.1 Lite",
        "- Video output count: 1",
        "- Aspect ratio: 9:16",
        "- Preferred generation length: 8s",
        "- Shorts visual grammar: POV_PAWS_MICROWORLD_V1",
        f"- Frame mode: {humanize(strategy.get('frame_mode') or 'sequential actual end frame plus target last')}",
        f"- References: {refs}",
        f"- Pacing: {pacing}",
        f"- Runtime mode: {humanize(runtime.get('mode') or 'compact h30')}",
        f"- Narration policy: {narration_policy}",
        f"- Audio policy: {audio_policy}",
        f"- Scale gate: {scale}",
        "- A beautiful third-person full-cat chef shot is a FAIL for this channel's default Shorts grammar.",
        "- Keep First+Last continuity shots on Lite; do not spend the next generation until the previous one passes QC.",
        "",
        "## Sequential-frame operator rule",
        "",
        "- A token like `ACTUAL_LAST_USABLE_FRAME_G1` is NOT an image to generate. It means: after G1 passes QC, save the real last usable frame from that generated clip and upload that saved image as the next scene's First frame.",
        "- Never replace an actual-frame token with the prettier planned target keyframe. Planned keyframes define destinations; actual saved frames carry continuity forward.",
        "- If the previous scene did not PASS, do not create its continuity frame for the purpose of unlocking the next spend. Fix/reroll only the failed scene first.",
        "- When a next scene depends on the current scene's actual frame, save it immediately after PASS with a clear local filename such as `G1_last_usable.png`.",
        "",
        "## Production-card approval",
        "",
        f"- Title: {data.get('title', '')}",
        f"- Hook: {data.get('hook', '')}",
        f"- Approve the {len(kfs)} free keyframes/contact sheet before spending video credits",
        f"- First-pass ceiling: {planned} Lite generations = {non_ultra} displayed-credit units when Flow still shows 10 per 8s Lite generation",
        "- A fourth generation is allowed only when it is an independent motion/world-resolution beat, never runtime padding.",
        "- Do not create multiple outputs in one request.",
        "",
        f"## {len(kfs)} keyframes",
        "",
    ]

    for kf in kfs:
        lines += [
            f"### {kf}",
            "",
            "```text",
            f"{frame_text(data, kf)}. {scale} {POV_STYLE}",
            "```",
            "",
        ]

    lines += [f"## {len(scenes)} video generations", ""]

    for index, scene in enumerate(scenes):
        scene_id = scene.get("id", "G")
        generation_type = humanize(scene.get("generation_type") or "first plus last")
        action = humanize(scene.get("action"))
        guard = humanize(scene.get("action_guard"))
        seconds = get_scene_seconds(scene)
        pacing_clause = (
            "Use one calm continuous tactile action with no unnecessary camera change. Let the tiny material response remain visible after the paw stops."
            if "healing" in pacing
            else "Keep motion simple, legible and physically plausible."
        )
        cut_clause = (
            f" Maximum visual cuts in this {seconds}s generation: {max_cuts}."
            if max_cuts is not None
            else ""
        )

        if generation_type == "extend":
            source_scene = scene.get("source_scene", "previous 8s scene")
            lines += [
                f"### {scene_id}: EXTEND {source_scene} ({seconds}s operation)",
                "",
                f"- Source clip: use the QC-PASS output from `{source_scene}` only.",
                "- Spend gate: do not extend a failed or merely planned scene.",
                "",
                "```text",
                f"Continue seamlessly from the supplied source clip. Action: {action}. Guard: {guard}. {pacing_clause}{cut_clause} "
                f"{scale} {LOCK} {POV_STYLE} No dialogue. No music. Keep only tiny close ASMR appropriate to the visible action.",
                "```",
                "",
            ]
        else:
            start = scene.get("start_frame", "")
            end = scene.get("end_frame", "")
            lines += [
                f"### {scene_id}: {start} → {end} ({seconds}s)",
                "",
                "**Operator inputs before Generate**",
                "",
                f"- {frame_input_instruction(start, role='First frame')}",
                f"- {frame_input_instruction(end, role='Last frame')}",
                "- Re-check: Veo 3.1 Lite / 9:16 / output 1 / displayed cost / correct new-video generation mode.",
                "",
                "```text",
                f"Animate naturally from the supplied first frame to the supplied last frame in {seconds} seconds. Action: {action}. Guard: {guard}. "
                f"{pacing_clause}{cut_clause} {scale} {LOCK} {POV_STYLE} "
                "No dialogue. No music. Quiet room tone with only small close tactile ASMR if it renders cleanly.",
                "```",
                "",
            ]
            if next_scene_uses_actual_frame(scenes, index, str(scene_id)):
                lines += [
                    f"**After {scene_id} PASS**",
                    "",
                    f"- Save the actual last usable frame from {scene_id} now; the next scene requires it as First frame.",
                    f"- Suggested local filename: `{scene_id}_last_usable.png`.",
                    f"- Do not generate the next scene until this saved frame has been visually checked for POV, scale, paw anatomy, prop state and camera continuity.",
                    "",
                ]

    lines += [
        "## QC shorthand",
        "",
        "- POV PASS: first-person + paws only + tiny object reads instantly",
        "- SCALE FAIL: hero object is not dramatically smaller than the paw",
        "- CHARACTER FAIL: face/head/body/full cat becomes visible",
        "- ANATOMY FAIL: fingers/thumbs/human grip",
        "- CAMERA FAIL: third-person chef composition",
        "- PADDING FAIL: extra generation adds duration but no independent beat",
        "- UI MODE FAIL: existing-video edit/Omni Flash edit was mistaken for a new Veo Lite scene",
        "- FRAME CHAIN FAIL: next scene used a planned keyframe or wrong still instead of the previous PASS scene's actual saved last usable frame",
        "",
        "## Failure escalation",
        "",
        "1. Minor timing/audio defect: repair in edit; do not reroll good motion.",
        "2. POV/scale/anatomy structural defect: reroll only that scene after repairing the relevant first/last frame or simplifying the action.",
        "3. If a paw must grip like a hand for the concept to work, redesign the action to nudge/press/slide instead of spending more credits.",
        "4. Never generate G2/G3/G4 proactively before the previous generation passes.",
        "5. Do not buy G4 merely to reach a target duration; use it only for a distinct world-resolution or tactile payoff beat.",
        "6. If Flow opens an existing-video edit mode or Omni Flash video edit, return to new-video generation and re-check model/mode/cost before spending.",
        "7. If the required previous-scene actual frame was not saved, recover it from the PASS clip before continuing; do not substitute the planned target frame.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    data = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    output = build(data)
    out = args.out or Path("generated") / f"{data['episode_id']}_flow_pack.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
