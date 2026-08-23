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


def get_scene_action(data: dict[str, Any], scene_id: str) -> str:
    for scene in data.get("scenes", []):
        if scene.get("id") == scene_id:
            return humanize(scene.get("action"))
    return ""


def frame_text(data: dict[str, Any], name: str) -> str:
    explicit = data.get("keyframes", {}).get(name)
    if explicit:
        return humanize(explicit)

    fallback = {
        "KF0_OPEN": f"opening visual for hook: {data.get('hook', '')}; show the constraint immediately",
        "KF1_CONSTRAINT": f"constraint clearly visible: {humanize(data.get('constraint') or data.get('core_question'))}",
        "KF2_DANGER": f"danger moment: {humanize(data.get('midpoint_risk') or data.get('originality_guard', {}).get('unique_conflict'))}",
        "KF3_PAYOFF": f"payoff visual: {humanize(data.get('payoff'))}",
        "KF4_TWIST": f"ending visual: {humanize(data.get('character_twist') or data.get('originality_guard', {}).get('unique_ending'))}",
    }
    return fallback[name]


def build(data: dict[str, Any]) -> str:
    episode_id = data["episode_id"]
    refs = ", ".join(data.get("references", [])) or "master cat, kitchen, cookware references"

    kfs = ["KF0_OPEN", "KF1_CONSTRAINT", "KF2_DANGER", "KF3_PAYOFF", "KF4_TWIST"]
    transitions = [
        ("G1", "KF0_OPEN", "KF1_CONSTRAINT"),
        ("G2", "KF1_CONSTRAINT", "KF2_DANGER"),
        ("G3", "KF2_DANGER", "KF3_PAYOFF"),
        ("G4", "KF3_PAYOFF", "KF4_TWIST"),
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
        lines += [
            f"### {scene_id}: {start} → {end}",
            "",
            "```text",
            f"Animate naturally from the supplied first frame to the supplied last frame. Action: {action}. "
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

    lines += [
        "## Human approval only",
        "",
        f"1. Title: {data.get('title', '')}",
        f"2. Hook: {data.get('hook', '')}",
        "3. Approve the 5-keyframe contact sheet",
        "4. Approve final export",
        "",
        "If one generation fails, regenerate only that generation. Never regenerate the full episode by default.",
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
