# TK-005 — Fast Quality Operator Card

Purpose: make `猫の前足で作る、12mmの焼きいも。` quickly without reconstructing the plan from multiple files.

This card does **not** spend Flow/Veo credits. Paid video generation still happens only when the user explicitly chooses Generate in Flow.

## 0. Quality target

The Short should feel like a real handcrafted miniature cooking video first, with believable feline front paws replacing human hands.

The viewer should understand within the first 1–2 seconds:

> `cat paws + absurdly tiny 12mm sweet potato + real miniature making`

Keep one world throughout: same cream/pale-ginger paws, wooden workbench, thumbnail-sized ceramic tray, tabletop warmer, upper-right serving niche, warm natural light, shallow macro depth of field.

### The five things that must survive

- **HOOK:** one 12mm purple sweet potato looks impossibly tiny between the paws before motion begins.
- **TRANSFORMATION:** warm/darken → crack/steam → golden center → quiet serving resolution.
- **SCALE PROOF:** hero remains roughly 18–32% of one visible paw width.
- **PAYOFF:** bright golden center + soft steam, then the same tray settles into the already-visible serving niche.
- **MOOD:** calm tactile miniature ASMR, not an AI-cat character performance.

## 1. NOW — create KF0 only

Use Nano Banana / Flow image generation to make the master anchor. The important thing is visual quality and continuity, not generating many alternatives.

### KF0 prompt — copy/paste

```text
Realistic handcrafted miniature cooking scene, vertical 9:16, stable high-oblique macro maker view over a tiny wooden workbench. Only two cream-and-pale-ginger real feline front paws enter naturally from the lower side edges where human hands normally would. Never show cat face, eyes, ears, head, chest, torso, tail or full body. Between the paws sits one absurdly tiny 12mm purple sweet potato on a thumbnail-sized ceramic roasting tray. The sweet potato must read as only about 18–32% of one visible paw width. A tiny tabletop warmer is already fixed just ahead of the tray. A tiny wooden serving niche is already visible in the far upper-right and must remain part of the same set for the whole episode. Real miniature materials, warm natural light, shallow macro depth of field, tactile food realism, calm handcrafted diorama detail. No human hands, fingers, thumbs, extra limbs, text, logos, watermark, tongs or human-like paw grip. The miniature workbench and tiny food are the subject; do not turn this into a cat character shot.
```

### KF0 PASS

PASS only when all are true:
- 1–2 paws only; no face/head/body
- sweet potato instantly looks absurdly smaller than paw
- tray, warmer and serving niche all fit naturally in one coherent tiny workspace
- paws look like real feline paws, not furry human hands
- camera is high-oblique maker view, not a full-cat scene
- frame already looks satisfying before animation

If KF0 is weak, fix KF0 rather than moving forward.

## 2. Derive KF1 from approved KF0

Do not start a new unrelated image. Preserve the exact paw fur, camera, lens, workbench, tray, warmer, serving niche, lighting and scale.

### KF1 change prompt

```text
Keep this exact approved image and miniature world. Change only the food state and tray position needed for the next beat: the same tiny ceramic tray is now a few millimeters closer to the same tabletop warmer, and the same 12mm purple sweet potato looks gently warmed with slightly darker skin. Keep the sweet potato dramatically smaller than either paw. Keep the same high-oblique maker-view camera, same paws, same tray, same warmer, same upper-right serving niche, same workbench geometry, same warm light and same shallow depth of field. Do not add or remove props. No cat face/head/body, no human fingers, no gripping, no character-performance framing.
```

PASS: the world looks like the same photograph a few seconds later.

## 3. Derive KF2 from KF1

### KF2 change prompt

```text
Preserve this exact miniature world, camera, paws, tray, warmer, serving niche, lighting and scale. Change only the food state: the same tiny sweet potato now has one small natural crack in its skin and one very thin curl of steam. One feline front paw may lightly steady the edge of the tiny tray from the side without gripping it. Keep the 12mm sweet potato under one third of paw width. No new props, no human anatomy, no cat face/head/body, no camera change.
```

PASS: one crack and subtle steam are clearly visible without the potato becoming larger.

## 4. Derive KF3 from KF2

### KF3 change prompt

```text
Preserve the exact same paws, high-oblique maker-view camera, workbench, tray, warmer, serving niche, lighting, lens and tiny scale. Move the same tray only a few millimeters away from the warmer. Widen the existing crack naturally just enough to reveal a bright warm golden sweet-potato center with soft steam. Do not create a new cut, tool, plate or prop. Paws remain partial working limbs only. The food must still be under one third of one paw width. No face/head/body, no human fingers or grip.
```

PASS: the golden center is the strongest visual payoff so far and continuity is intact.

## 5. Derive KF4 from KF3

### KF4 change prompt

```text
Preserve the exact same miniature set, paws, camera, lighting, lens, warmer, ceramic tray and 12mm finished yakiimo. Place the same tray inside the wooden serving niche that has already been visible in the upper-right since KF0. The warmer stays exactly where it was. One feline front paw rests naturally near the tray edge after the slide; soft warm steam continues from the golden-center crack. Introduce no new plate, bowl, cookware, shelf, stall, customer or cat body. This is a quiet resolution in the same world, not a new scene.
```

PASS: this feels like closure, not an unrelated serving setup.

## 6. Before G1

Only continue when KF0→KF4 clearly look like one continuous miniature world.

Flow paid-video settings immediately before Generate:
- NEW VIDEO GENERATION
- Veo 3.1 Lite
- 9:16
- 8 seconds
- output count 1
- First frame = approved KF0
- Last frame = approved KF1

## 7. G1 — the most important paid generation

Goal: prove the premise instantly and get one believable paw action without anatomy drift.

### G1 prompt — copy/paste

```text
Animate naturally from the supplied KF0 first frame to the supplied KF1 last frame over 8 seconds. Keep the camera locked in the same calm high-oblique macro maker view. During the opening 1–2 seconds, preserve a clear readable view of the absurdly tiny 12mm purple sweet potato between the much larger feline front paws so the miniature scale is immediately obvious. Then one feline front paw slowly nudges only the edge of the thumbnail-sized ceramic roasting tray a few millimeters toward the already-present tiny tabletop warmer and stops. The sweet potato itself barely shifts; its skin only becomes subtly warmer and slightly darker by the end. Exactly one active paw action: one slow tray nudge. No grabbing, pinching, lifting, tool grip or second gesture. Keep the same paw fur, paw anatomy, tray, warmer, upper-right serving niche, workbench, scale, lens and lighting. Never show cat face/head/body or human hands/fingers/thumbs. No camera cut, zoom or dramatic movement. No dialogue and no music. Quiet room tone with tiny ceramic-on-wood movement and very subtle close miniature heat/food ASMR only if clean.
```

### G1 PASS

PASS only if:
- first 1–2s communicates impossible tiny scale
- paw motion looks feline and physically plausible
- only the tray is nudged; no human-like grip
- sweet potato remains 12mm-looking and does not inflate
- no full cat/body reveal
- warmer/niche/workbench do not drift
- one continuous calm shot
- the ending is a credible bridge to KF1

If G1 PASS: use Flow native **Save frame** on the last usable frame. That exact saved frame becomes G2 First frame.

If G1 structurally fails: do not generate G2.

## 8. G2 — crack and steam

First frame = actual saved G1 PASS frame. Last frame = KF2.

```text
Continue seamlessly from the supplied actual saved G1 PASS frame toward the supplied KF2 target over 8 seconds. Preserve the exact high-oblique maker-view camera, paw fur/anatomy, tiny 12mm scale, ceramic tray, warmer, upper-right serving niche, workbench and warm lighting. One feline paw gently presses only the edge of the tiny ceramic tray to steady it and then becomes still. While it is held steady, the sweet-potato skin slowly darkens, one small natural crack appears, and one thin wisp of steam escapes. Exactly one active paw action: one gentle steadying press. The crack and steam are passive material payoff, not extra paw actions. Paw never picks up, pinches or grips the food. No cat face/head/body, no human fingers/thumbs, no camera cut, no new props. Quiet close miniature ASMR, no dialogue, no music.
```

PASS → native Save frame → G3 First frame.

## 9. G3 — golden-center reveal

First frame = actual saved G2 PASS frame. Last frame = KF3.

```text
Continue seamlessly from the supplied actual saved G2 PASS frame toward KF3 over 8 seconds. Preserve the exact same miniature world, high-oblique camera, paw identity, scale, tray, warmer, serving niche, workbench and lighting. One feline front paw slowly slides the same tiny ceramic tray only a few millimeters away from the heat and stops. After the paw stops, residual warmth passively widens the existing single crack and reveals a bright soft golden center with gentle steam. Exactly one active paw action: one slow tray slide. The golden-center reveal and steam are passive material payoff. No pinching or touching the sweet potato directly, no human-like grip, no cat face/head/body, no new props, no cut or zoom. Calm close tactile ASMR only, no dialogue or music.
```

After real G3, decide whether the episode already feels complete.

## 10. G4 — only if it earns its place

Use G4 only if the real G3 golden-center reveal is strong **and** moving the same tray into the already-visible niche adds a satisfying final world-resolution beat. Do not use G4 just to reach 32 seconds.

First frame = actual saved G3 PASS frame. Last frame = KF4.

```text
Continue seamlessly from the supplied actual saved G3 PASS frame toward KF4 over 8 seconds. Preserve the exact same high-oblique miniature-maker camera, paw fur/anatomy, 12mm yakiimo, ceramic tray, warmer, serving niche, workbench, scale, lighting and lens. One feline front paw slowly slides the same ceramic tray containing the finished cracked golden-center yakiimo into the wooden serving niche that has been visible since the opening shot, then the paw stops and rests naturally near the edge. Exactly one active action: one tray slide. After it stops, only soft warm steam continues. Do not introduce a plate, bowl, cookware, shelf, stall, customer, eating action, paw withdrawal gesture or new camera angle. No cat face/head/body, no human hands/fingers/thumbs, no cut. Quiet close miniature ASMR, no dialogue, no music.
```

## 11. Final edit

Preferred if all four beats are valuable: about 32–35 seconds. If G4 feels redundant, finish after G3 rather than padding.

Editing priorities:
- open immediately on strongest impossible-scale frame; no logo intro
- preserve the first visual transformation quickly enough that the opening does not feel static
- use mostly native speed; 0.92–1.00x only if motion remains natural
- hard cuts only between generations when needed; no rapid montage
- use sound bridges to hide generation boundaries
- keep clean tiny ASMR; replace broken generated audio instead of rerolling good motion

## 12. One-line operator checklist

```text
KF0 strongest scale frame → derive KF1→KF4 in same world → G1 only → PASS/Save frame → G2 → PASS/Save frame → G3 → decide if story is complete → only then G4 if it genuinely improves payoff.
```
