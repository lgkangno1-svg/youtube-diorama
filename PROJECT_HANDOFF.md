# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected before this iteration: `main@de2545d4cfa1c6ea1f25e74ba76fedb35cedc4d6`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Start-of-run contract

Before every material run:
1. inspect latest `main` SHA and recent commits/PRs
2. read this handoff
3. read `PRODUCT_CHARTER.md`
4. cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, current manifest, benchmark/backlog/ledger
5. newest explicit user direction and merged repository state override stale scheduled-prompt wording

Document roles:
- `PROJECT_HANDOFF.md` = current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md` = durable product purpose / identity / economics and improvement criteria
- `CURRENT_STANDARD.md` = executable production/QC/Flow rules
- manifests + ledgers = episode plan + observed evidence

Sync policy:
- every material change updates this handoff
- executable production/QC/Flow rule changes also update `CURRENT_STANDARD.md`
- durable purpose/identity/economics philosophy changes also update `PRODUCT_CHARTER.md`
- true NO-OP does not churn docs

## Durable product intent

Tiny Cat Kitchen is a Japanese-target healing Shorts system for realistic miniature cooking/making where **human hands are naturally replaced by feline front paws**.

Non-negotiable identity:
- cream/pale-ginger front paws only; normally 1–2
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline tool grip
- absurdly tiny hero object, normally 5–20mm and <=0.50 paw width
- handcrafted miniature workbench/diorama realism
- process-first tactile making
- calm long-take ASMR
- default high-oblique maker view; top-down/side-oblique allowed
- literal first-person cat-eye POV is **not mandatory**
- no AI-cat human-job/character-performance regression

Primary optimization is not minimum credits/video. Prefer **usable motion/credit, engaged views/credit, and subscribers/100 credits** while protecting quality and explicit user control.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: 4 Veo 3.1 Lite generations / 40 credits
Expected final: ~32–35s when all four beats remain independently useful

Visual intent:
- stable Mini Forest-style high-oblique maker view
- only front paws enter where hands normally would
- 12mm yakiimo dramatically smaller than paw
- same tray/warmer/serving niche through KF0→KF4
- zero-cut calm long takes
- one active paw-safe action per generation + optional passive material payoff
- G4 = tray slide, then passive steam only

Paid continuity chain:
- G1: KF0 → KF1
- G2: actual saved G1 PASS frame → KF2
- G3: actual saved G2 PASS frame → KF3
- G4 only if still justified: actual saved G3 PASS frame → KF4

### TK-005 manifest gate correction — 2026-08-29

The manifest still contained a stale progressive-spend field named `stop_if_pov_scale_anatomy_or_premise_fails`. Although the current tool does not consume that key and the manifest already had `first_person_required: false`, the field name could mislead a future AI/operator into treating non-first-person maker-view framing as a structural failure.

Corrected it to:
- `stop_if_maker_view_scale_anatomy_or_premise_fails: true`

Interpretation:
- observational/high-oblique maker view is valid and preferred by default
- stop spending when miniature-making composition, paws-only identity, tiny scale, anatomy, or premise structurally fails
- do **not** stop merely because the camera is not literal first-person

No camera enum/schema migration was attempted: `camera_grammar.mode: first_person_cat_pov` and `POV_PAWS_MICROWORLD_V1` remain temporarily for compatibility and are explicitly overridden by maker-view semantics. Do not migrate those piecemeal without validating tooling/schema impact.

## Flow / spend baseline

Generation-time Flow UI is final truth. Current documented assumption:
- Veo 3.1 Lite
- 9:16
- 8 seconds
- output count 1
- non-Ultra: 10 credits/generation
- Ultra: 5 credits/generation
- non-subscriber tier: 50 credits/day, not additive to paid-plan allocations

Progressive Spend:

```text
free/no-charge planned keyframe chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if runtime/manifest still justifies independent final value
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Current learning

One real preflight failure remains recorded in `analytics/learning_ledger.csv`:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Correct interpretation:
- observational/third-person maker view itself is not a failure
- body reveal + character-performance framing + weak miniature scale is the failure
- maker-view + paws-only + tiny workpiece is desirable

There is still no trustworthy public 24h/72h Tiny Cat Kitchen performance sample. Do not treat placeholders or theoretical assumptions as audience evidence.

## Research / candidate state

Primary benchmark class:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat channels are secondary evidence only for narrow paw/anatomy/reliability questions. Never copy exact competitor title, plot, branded product/package, distinctive set, dish styling, or ending.

Evidence saturation remains active. Same-class promotional/retail signals do not justify commits unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual production learning.

Accepted current demand evidence:
- 2026-08-19 Maruyanagi release citing Google Trends reports Japanese `さつまいもスイーツ` search interest rising September–December and roughly 9× summer levels in October; treat as directional because raw Trends data was not independently reproduced
- existing survey, behavioral event attendance, and multiple nationwide activations already make sweet-potato/yakiimo research saturated

Fresh 2026-08-29 research check found additional late-August sweet-potato/月見 product launches, but they are the same nationwide/promotional evidence class and do not change ranking, timing, production mechanics, or Flow assumptions. They were intentionally **not** added to the benchmark log.

Candidate state:
- TK-005 / IDEA-009 remains the strongest current production choice
- IDEA-001 月見 remains a strong secondary seasonal candidate
- IDEA-002 グミの日 and IDEA-006 栗ご飯 remain secondary candidates
- no score/rank change justified without stronger creator-performance, behavioral demand, or Tiny Cat Kitchen production evidence

## Current roadmap / next priorities

1. Create and approve TK-005 KF0 master anchor in real Flow.
2. Confirm it reads as genuine miniature making with paws replacing hands, not an AI-cat character scene.
3. Derive KF1→KF4 sequentially with stable paws/scale/camera/props/lighting.
4. Generate G1 only after the planned KF chain passes.
5. QC maker-view, paws-only identity, tiny scale, anatomy, fixed props, zero-cut behavior.
6. On PASS, save the actual usable final frame and continue progressively.
7. Record actual credits, rerolls, usable motion, G-stage pass/fail and failure class.
8. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers and comments.
9. Use real accumulated evidence to adjust action grammar, runtime tiers, candidate scoring and spend strategy.
10. Keep the user-facing workflow simpler over time, not more complicated.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs
- no human-like paw grip
- no weak miniature scale without documented exception
- no paid G1 before planned KF continuity passes
- no next paid scene after prior structural failure
- actual previous PASS frame is the continuity bridge
- non-first-person maker view is not a failure by itself
- no runtime padding for its own sake
- no research churn after saturation
- no unrelated repository modifications
- every material repository change synchronizes this handoff

## Change log

### 2026-08-29 — TK-005 maker-view spend-gate semantic correction
Baseline: `main@de2545d4cfa1c6ea1f25e74ba76fedb35cedc4d6`.

Changed:
- renamed TK-005 manifest progressive-spend key from legacy `stop_if_pov_scale_anatomy_or_premise_fails` to `stop_if_maker_view_scale_anatomy_or_premise_fails`
- synchronized this handoff in the same branch

Why:
- the old field name could reintroduce the superseded assumption that literal first-person POV is mandatory even though current accepted production grammar prefers Mini Forest-style observational maker view

Production impact:
- no change to TK-005 episode choice, H40 runtime, 4-generation/40-credit first-pass ceiling, action sequence, keyframes, audio, Flow settings, or NEXT_EPISODE
- no Flow credits spent; no publishing

Research verification:
- additional 2026-08-27/28 sweet-potato and 月見 launches are same-class promotional/nationwide activation evidence for already saturated candidates, so benchmark/backlog were not churned

### 2026-08-29 — sweet-potato search-demand evidence
- added a new search-behavior evidence class for `さつまいもスイーツ` seasonality
- TK-005 remained top-ranked; no production-rule change

### 2026-08-28 — product charter governance wiring
- made `PRODUCT_CHARTER.md` mandatory in the improvement loop
- synchronized START_HERE, docs/22, CURRENT_STANDARD and handoff governance

### 2026-08-28 — durable product charter
- added `PRODUCT_CHARTER.md` as the stable product-purpose and decision-standard document

### 2026-08-28 — Flow / operator / maker-view corrections
- clarified Flow free-tier eligibility without changing H40 spend discipline
- removed stale operator wording that treated non-first-person camera as failure
- removed mandatory first-person/cat-job semantics from actionable backlog/learning
- reduced TK-005 G4 to one active tray-slide action + passive steam
- established Mini Forest-style miniature making + feline front paws replacing human hands as the canonical visual grammar
