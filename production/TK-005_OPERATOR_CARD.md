# TK-005 — Fast Quality Operator Card

Purpose: make `猫の前足で作る、12mmの焼きいも。` with the fewest unnecessary steps while maximizing continuity and first-pass quality.

This card never spends Flow/Veo credits automatically. Paid video generation happens only when the user explicitly chooses Generate in Flow.

## Quality target

The Short must read first as a real handcrafted miniature cooking video, with believable feline front paws replacing human hands.

Core story must be complete in **G1→G3**:

> impossible 12mm scale → gentle warming → crack + steam → golden-center reveal

**G4 is optional.** Only add it after watching real G3 if sliding the same tray into the already-visible serving niche creates a genuinely better ending.

Keep one world throughout: same cream/pale-ginger paws, wooden workbench, thumbnail-sized ceramic tray, tabletop warmer, upper-right serving niche, warm natural light, shallow macro DOF.

Non-negotiable:
- 1–2 feline front paws only
- no face/head/body/full cat
- no human fingers/thumbs or human-like grip
- yakiimo remains about 18–32% of one visible paw width
- calm maker-view, no rapid montage

---

# NEW FAST CONTINUITY RULE

Do **not** prebuild KF2/KF3 before G1.

Google Flow officially supports saving a video frame and reusing that saved frame as a future start/end frame. Use that capability to re-anchor every next target to what Veo actually produced.

Core execution:

```text
KF0 → derive KF1 → G1
G1 PASS → Save frame → derive KF2 from ACTUAL G1 saved frame → G2
G2 PASS → Save frame → derive KF3 from ACTUAL G2 saved frame → G3
G3 PASS → watch core → STOP if complete
optional only: derive KF4 from ACTUAL G3 saved frame → G4
```

Why:
- less pre-G1 work
- fewer speculative keyframes that may no longer match real footage
- next target inherits actual paw fur, camera, props, scale and lighting
- each generation solves a smaller continuity correction

The manifest's KF2/KF3 text remains the **desired destination state**, not a requirement to create those images before G1.

---

# NOW — create KF0 only

## KF0 prompt — copy/paste

```text
Realistic handcrafted miniature cooking scene, vertical 9:16, stable high-oblique macro maker view over a tiny wooden workbench. Only two cream-and-pale-ginger real feline front paws enter naturally from the lower side edges where human hands normally would. Never show cat face, eyes, ears, head, chest, torso, tail or full body. Between the paws sits one absurdly tiny 12mm purple sweet potato on a thumbnail-sized ceramic roasting tray. The sweet potato must read as only about 18–32% of one visible paw width. A tiny tabletop warmer is already fixed just ahead of the tray. A tiny wooden serving niche is already visible in the far upper-right and must remain part of the same set. Real miniature materials, warm natural light, shallow macro depth of field, tactile food realism, calm handcrafted diorama detail. No human hands, fingers, thumbs, extra limbs, text, logos, watermark, tongs or human-like paw grip. The miniature workbench and tiny food are the subject; do not turn this into a cat character shot.
```

### KF0 PASS

PASS only if all are true:
- 1–2 paws only; no face/head/body
- sweet potato instantly looks absurdly smaller than paw
- tray, warmer and upper-right niche fit naturally in one tiny workspace
- paws look feline, not furry human hands
- high-oblique maker view
- frame is already visually satisfying before animation

If weak, fix KF0. Do not move forward.

---

# KF1 — derive from approved KF0

```text
Keep this exact approved image and miniature world. Change only the food state and tray position needed for the next beat: the same tiny ceramic tray is now a few millimeters closer to the same tabletop warmer, and the same 12mm purple sweet potato looks gently warmed with slightly darker skin. Keep the sweet potato dramatically smaller than either paw. Keep the same high-oblique maker-view camera, same paws, same tray, same warmer, same upper-right serving niche, same workbench geometry, same warm light and same shallow depth of field. Do not add or remove props. No cat face/head/body, no human fingers, no gripping, no character-performance framing.
```

PASS: same photograph a few seconds later.

**Only KF0 + KF1 need approval before G1.**

---

# G1 — first paid checkpoint

Flow settings immediately before Generate:
- Veo 3.1 Lite
- 9:16
- 8 seconds
- output count 1
- First frame = KF0
- Last frame = KF1

```text
Animate naturally from supplied KF0 to supplied KF1 over 8 seconds. Keep the camera locked in the same calm high-oblique macro maker view. Make the impossible scale readable immediately: the 12mm purple sweet potato stays clearly visible between much larger feline front paws. Begin the single paw movement gently without a long dead hold. One feline front paw slowly nudges only the edge of the thumbnail-sized ceramic roasting tray a few millimeters toward the already-present tiny tabletop warmer and stops. The sweet potato itself barely shifts; its skin becomes subtly warmer and slightly darker by the end. Exactly one active paw action: one slow tray nudge. No grabbing, pinching, lifting, tool grip or second gesture. Keep the same paw fur, anatomy, tray, warmer, serving niche, workbench, scale, lens and lighting. Never show cat face/head/body or human hands/fingers/thumbs. No camera cut, zoom or dramatic movement. No dialogue and no music. Quiet room tone with tiny ceramic-on-wood movement and subtle close miniature heat/food ASMR only if clean.
```

### G1 PASS
- scale reads immediately
- feline-looking motion; no grip
- sweet potato does not inflate
- no body reveal
- props/camera stay fixed
- one calm continuous shot

PASS → Flow native **Save frame** on the last usable frame.

FAIL structurally → stop. Do not generate G2.

---

# AFTER G1 PASS — create KF2 from the ACTUAL saved G1 frame

Use the actual saved G1 frame as the image to edit/reference. Do not derive KF2 from old planned KF1.

```text
Preserve this exact actual G1 ending frame: same feline paw fur and anatomy, same high-oblique camera, exact workbench geometry, ceramic tray, tabletop warmer, upper-right serving niche, lighting, lens and current 12mm scale. Change only the food/material state needed for the next beat. The same tiny sweet potato now has one small natural crack in its skin and one very thin curl of steam. One feline front paw may lightly steady the edge of the tiny tray from the side without gripping it. Keep the sweet potato under one third of paw width. No new props, no human anatomy, no cat face/head/body, no camera change.
```

PASS: it looks like the **actual G1 frame a few seconds later**, with one crack + subtle steam and no scale inflation.

---

# G2 — crack + steam

First frame = actual saved G1 PASS frame  
Last frame = newly approved KF2 derived from that same actual frame

```text
Continue seamlessly from the supplied actual saved G1 PASS frame toward supplied KF2 over 8 seconds. Preserve the exact high-oblique maker-view camera, paw fur/anatomy, tiny 12mm scale, ceramic tray, warmer, upper-right serving niche, workbench and warm lighting. One feline paw gently presses only the edge of the tiny ceramic tray to steady it and then becomes still. While it is held steady, the sweet-potato skin slowly darkens, one small natural crack appears, and one thin wisp of steam escapes. Exactly one active paw action: one gentle steadying press. The crack and steam are passive material payoff, not extra paw actions. Paw never picks up, pinches or grips the food. No cat face/head/body, no human fingers/thumbs, no camera cut, no new props. Quiet close miniature ASMR, no dialogue, no music.
```

PASS → native Save frame.

FAIL structurally → stop. Do not generate G3.

---

# AFTER G2 PASS — create KF3 from the ACTUAL saved G2 frame

Use the actual saved G2 frame as the source.

```text
Preserve this exact actual G2 ending frame: same paws, high-oblique maker-view camera, workbench, ceramic tray, tabletop warmer, upper-right serving niche, lighting, lens and current tiny scale. Change only the final core food state and a few millimeters of tray position. Move the same tray slightly away from the warmer. Widen the existing single crack naturally just enough to reveal a bright warm golden sweet-potato center with soft steam. Do not create a new cut, tool, plate or prop. Paws remain partial working limbs only. The food must still be under one third of one paw width. No face/head/body, no human fingers or grip. This frame must look satisfying enough to end the Short here.
```

PASS: it looks like the **actual G2 frame a few seconds later**, with a complete golden-center payoff.

---

# G3 — complete core payoff

First frame = actual saved G2 PASS frame  
Last frame = newly approved KF3 derived from that same actual frame

```text
Continue seamlessly from the supplied actual saved G2 PASS frame toward supplied KF3 over 8 seconds. Preserve the exact same miniature world, high-oblique camera, paw identity, scale, tray, warmer, serving niche, workbench and lighting. One feline front paw slowly slides the same tiny ceramic tray only a few millimeters away from the heat and stops. After the paw stops, residual warmth passively widens the existing single crack and reveals a bright soft golden center with gentle steam. Exactly one active paw action: one slow tray slide. The golden-center reveal and steam are passive material payoff. No pinching or touching the sweet potato directly, no human-like grip, no cat face/head/body, no new props, no cut or zoom. Calm close tactile ASMR only, no dialogue or music. The final frame must feel complete enough to end the Short here.
```

PASS → native Save frame.

## STOP AND WATCH G1→G3 TOGETHER

If the golden-center reveal already feels complete, **finish here**. Normal final runtime will be roughly 24–27s depending on edit.

Only continue if real footage clearly benefits from one more same-world closure beat.

---

# OPTIONAL G4 — only after real G3 proves it is useful

If G4 is justified, derive KF4 from the actual saved G3 PASS frame.

```text
Preserve this exact actual G3 ending frame, miniature set, paws, camera, lighting, lens, warmer, ceramic tray and 12mm finished yakiimo. Move only the same tray into the wooden serving niche that has already been visible in the upper-right since the opening. The warmer stays exactly where it was. One feline front paw rests naturally near the tray edge after the slide; soft warm steam continues from the golden-center crack. Introduce no new plate, bowl, cookware, shelf, stall, customer or cat body. This is a quiet resolution in the same world, not a new scene.
```

Then:
- First frame = actual saved G3 PASS frame
- Last frame = approved KF4

```text
Continue seamlessly from the supplied actual saved G3 PASS frame toward KF4 over 8 seconds. Preserve the exact same high-oblique miniature-maker camera, paw fur/anatomy, 12mm yakiimo, ceramic tray, warmer, serving niche, workbench, scale, lighting and lens. One feline front paw slowly slides the same ceramic tray containing the finished cracked golden-center yakiimo into the wooden serving niche that has been visible since the opening shot, then the paw stops and rests naturally near the edge. Exactly one active action: one tray slide. After it stops, only soft warm steam continues. Do not introduce a plate, bowl, cookware, shelf, stall, customer, eating action, paw withdrawal gesture or new camera angle. No cat face/head/body, no human hands/fingers/thumbs, no cut. Quiet close miniature ASMR, no dialogue, no music.
```

---

# Final edit

Preferred runtime is adaptive:
- strong G1→G3 only: roughly 24–27s
- G4 genuinely improves ending: roughly 32–35s

Rules:
- no logo intro
- strongest impossible-scale frame immediately
- mostly native speed; 0.92–1.00x only if natural
- no runtime padding
- sound bridges may hide generation boundaries
- replace broken generated audio instead of rerolling good motion

## One-line workflow

```text
KF0 → KF1 → G1 PASS/Save → derive KF2 from actual G1 → G2 PASS/Save → derive KF3 from actual G2 → G3 PASS/Save → watch core → STOP if complete → only then derive KF4 from actual G3 + optional G4.
```
