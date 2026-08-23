#!/usr/bin/env python3
"""Build a low-token Google Flow prompt pack from one episode YAML manifest.

Usage:
  python tools/build_flow_pack.py episodes/TK-001.yaml
  python tools/build_flow_pack.py episodes/TK-001.yaml --out generated/TK-001_flow_pack.md

Requires: PyYAML
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


STYLE = (
    "Photorealistic miniature Japanese kitchen, vertical 9:16, macro lens, shallow depth of field, "
    "warm natural light, realistic food texture and physics. Same orange tabby cat with white-sock "
    "feline front paws. No human fingers, no thumbs, no extra limbs, no text, no logos, no watermark."
)

LOCK = (
    "Preserve exact cat fur pattern, cookware, food scale, kitchen layout and lighting between start and end frames. "
    "Do not duplicate, remove or morph ingredients unless the action explicitly requires it."
)


def humanize(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("_", " ").strip()


def get_scene(data: dict[str, Any], scene_id: str) -> dict[str, Any]:
    for scene in data.get("scenes", []):
        if scene.get("id") == scene_id:
            return scene
    return {}


def get_scene_action(data: dict[str, Any], scene_id: str) -> str:
    return humanize(get_scene(data, scene_id).get("action"))


def get_scene_seconds(data: dict[str, Any], scene_id: str) -> int:
    value = get_scene(data, scene_id).get("generation_seconds", 8)
    try:
        value = int(value)
    except (TypeError, ValueError):
        value = 8
    return value if value in {4, 6, 8} else 8


def resolution_value(data: dict[str, Any]) -> str:
    return humanize(
        data.get("resolution")
        or data.get("character_twist")
        or data.get("originality_guard", {}).get("unique_ending")
        or data.get("payoff")
    )


def frame_text(data: dict[str, Any], name: str) -> str:
    explicit = data.get("keyframes", {}).get(name)
    if explicit:
        return humanize(explicit)

    if name == "KF4_RESOLUTION":
        legacy = data.get("keyframes", {}).get("KF4_TWIST")
        if legacy:
            return humanize(legacy)

    fallback = {
        "KF0_OPEN": f"opening visual for hook: {data.get('hook', '')}; show the constraint immediately",
        "KF1_CONSTRAINT": f"constraint clearly visible: {humanize(data.get('constraint') or data.get('core_question'))}",
        "KF2_DANGER": f"danger moment: {humanize(data.get('midpoint_risk') or data.get('originality_guard', {}).get('unique_conflict'))}",
        "KF3_PAYOFF": f"payoff visual: {humanize(data.get('payoff'))}",
        "KF4_RESOLUTION": f"ending resolution visual: {resolution_value(data)}",
    }
    return fallback[name]


def build(data: dict[str, Any]) -> str:
    episode_id = data["episode_id"]
    refs = ", ".join(data.get("references", [])) or "master cat, kitchen, cookware references"

    kfs = ["KF0_OPEN", "KF1_CONSTRAINT", "KF2_DANGER", "KF3_PAYOFF", "KF4_RESOLUTION"]
    transitions = [
        ("G1", "KF0_OPEN", "KF1_CONSTRAINT"),
        ("G2", "KF1_CONSTRAINT", "KF2_DANGER"),
        ("G3", "KF2_DANGER", "KF3_PAYOFF"),
        ("G4", "KF3_PAYOFF", "KF4_RESOLUTION"),
    ]

    lines: list[str] = []
    lines += [
        f"# {episode_id} — Flow Pack",
        "",
        "> Generated deterministically from the episode manifest. Do not ask an LLM to rewrite unless a scene fails.",
        "",
        "## Fixed settings",
        "",
        "- Model: Veo 3.1 Lite",
        "- Video output count: 1",
        "- Aspect ratio: 9:16",
        "- Frame mode: First + Last",
        "- References: " + refs,
        "- Use Nano Banana 2 Lite for keyframes",
        "- Reserve the upper overlay-safe area; do not place the only critical visual cue at the very top edge",
        "- Compatibility lock: keep First + Last clips on Veo 3.1 Lite; current Google Flow matrix lists Fast First + Last as coming soon",
        "",
        "## Production-card approval",
        "",
        f"- Title: {data.get('title', '')}",
        f"- Hook: {data.get('hook', '')}",
        "- Approve the five keyframes below as one contact sheet before spending video credits",
        "- First-pass budget: four Lite generations; on a free non-subscriber account reserve the remaining 10 daily credits for one post-QC reroll",
        "",
        "## 5 keyframes",
        "",
    ]

    for kf in kfs:
        lines += [
            f"### {kf}",
            "",
            "```text",
            f"{frame_text(data, kf)}. {STYLE}",
            "```",
            "",
        ]

    lines += ["## 4 video generations", ""]

    for scene_id, start, end in transitions:
        action = get_scene_action(data, scene_id)
        seconds = get_scene_seconds(data, scene_id)
        lines += [
            f"### {scene_id}: {start} → {end} ({seconds}s)",
            "",
            "```text",
            f"Animate naturally from the supplied first frame to the supplied last frame in {seconds} seconds. Action: {action}. "
            f"Keep the motion simple, legible and physically plausible. {LOCK} {STYLE} Natural cooking ASMR only; no speech.",
            "```",
            "",
        ]

    fp = data.get("episode_fingerprint", {})
    if fp:
        lines += ["## Originality fingerprint", ""]
        for key, value in fp.items():
            lines.append(f"- {key}: {humanize(value)}")
        lines.append("")

    narration = data.get("creator_signature", {})
    lines += [
        "## Creator signature layer",
        "",
        "Add narration/captions in post; do not spend Flow credits generating dialogue unless the episode specifically requires it.",
        f"- narrator_angle: {humanize(narration.get('narrator_angle') or 'one concise observation or joke unique to this episode')}",
        f"- signature_line: {narration.get('signature_line') or 'write one short Japanese line that could not be pasted unchanged onto another episode'}",
        "- Keep this layer brief; its purpose is authorship, character voice, and retention, not explaining every visible action.",
        "",
        "## Failure escalation — preserve frame lock",
        "",
        "1. Minor defect: fix in editor with crop, freeze, speed adjustment, or keyframe cutaway.",
        "2. Structural defect: reroll only that G-scene with Veo 3.1 Lite.",
        "3. Repeated failure: simplify the action or repair its start/end keyframes, then reroll Lite.",
        "4. Do NOT treat Fast as a drop-in First+Last upgrade: current Google Flow support lists Fast First+Last as coming soon.",
        "5. Use Fast/Quality only for a separate shot where losing the two-endpoint lock is acceptable and the current Flow UI supports the chosen mode.",
        "6. Use Gemini Omni Flash video edit only when one 40-credit edit is expected to replace at least four Lite rerolls or supplies a uniquely needed edit capability.",
        "",
        "## Final human approval",
        "",
        "Approve only the final export after continuity, hook readability, creator signature, resolution, and upload metadata are checked.",
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
