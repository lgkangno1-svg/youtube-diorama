# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected before this iteration: `main@3ceb5f41f2c1ad55fb7b64b32c741cecce75c8e6`

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

## Critical operator validation correction — 2026-08-29

A material workflow regression was found in the exact normal user path.

`./tools/make_next_short.ps1` called `tools/validate_current_standard.py` before building the production pack. That older validator still required the superseded field:

`stop_if_pov_scale_anatomy_or_premise_fails: true`

PR #56 correctly changed TK-005 to:

`stop_if_maker_view_scale_anatomy_or_premise_fails: true`

Therefore the current valid TK-005 could be rejected by the one-command workflow before any Flow work even though the manifest and current docs were semantically correct.

Correction:
- added `tools/validate_maker_view_manifest.py` as the canonical current-semantic adapter
- `make_next_short.ps1` now runs that adapter first
- the adapter requires current `visual_intent`, maker-view `semantic_override`, `first_person_required: false`, `high_oblique_maker_view`, and the new maker-view structural-failure spend gate
- it rejects an active legacy POV stop gate
- after semantic validation it delegates the mature runtime/credit/keyframe/sequential-frame/narration checks to the existing structural validator through compatibility translation only
- added `tools/test_validate_maker_view_manifest.py` to protect this behavior
- synchronized `CURRENT_STANDARD.md` in the same change

Important interpretation:
- legacy `POV_PAWS_MICROWORLD_V1` / `camera_grammar.mode: first_person_cat_pov` can remain temporarily for compatibility
- they must not make literal first-person a creative or validation requirement
- current semantics are maker-view + paws-only + tiny scale + feline-safe actions

This correction does not alter TK-005 content, runtime, scene count, credit ceiling, Flow model, or NEXT_EPISODE.

## Flow / spend baseline

Generation-time Flow UI is final truth. Current documented assumption, rechecked against official Flow documentation on 2026-08-29:
- Veo 3.1 Lite
- 9:16
- output count 1
- non-Ultra: 10 credits/generation
- Ultra: 5 credits/generation
- no-subscription tier: 50 credits/day, not additive to paid-plan allocations
- Flow image preflight may use the currently offered no-charge image option only when the actual UI shows no charge / 0 credits

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

Fresh 2026-08-29 research check:
- additional yakiimo event/texture signals reinforce tactile autumn relevance but do not change TK-005 ranking, timing, or mechanics
- current Mini Forest adjacent performance evidence remains consistent with the already-recorded cultural-timing miniature-food benchmark and does not justify duplicate benchmark rows
- therefore benchmark/backlog were intentionally not churned

Candidate state:
- TK-005 / IDEA-009 remains the strongest current production choice
- IDEA-001 月見 remains a strong secondary seasonal candidate
- IDEA-002 グミの日 and IDEA-006 栗ご飯 remain secondary candidates
- no score/rank change justified without stronger creator-performance, behavioral demand, or Tiny Cat Kitchen production evidence

## Legacy manifest caution

Recent manifests TK-001–TK-004 contain pre-correction production concepts/statuses, including older character/story or human-like manipulation assumptions. They are historical/planning artifacts, not authority over the current standard.

The normal production path must fail closed unless the selected NEXT_EPISODE manifest satisfies the current maker-view adapter. Do not revive an old `ready-for-flow`, `planned`, or `priority_trend_window` manifest solely from its historical status without refreshing it to current maker-view semantics first.

## Current roadmap / next priorities

1. Run the current maker-view manifest validation path for TK-005 before local pack preparation.
2. Create and approve TK-005 KF0 master anchor in real Flow.
3. Confirm it reads as genuine miniature making with paws replacing hands, not an AI-cat character scene.
4. Derive KF1→KF4 sequentially with stable paws/scale/camera/props/lighting.
5. Generate G1 only after the planned KF chain passes.
6. QC maker-view, paws-only identity, tiny scale, anatomy, fixed props, zero-cut behavior.
7. On PASS, save the actual usable final frame and continue progressively.
8. Record actual credits, rerolls, usable motion, G-stage pass/fail and failure class.
9. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers and comments.
10. Use real accumulated evidence to adjust action grammar, runtime tiers, candidate scoring and spend strategy.
11. Keep the user-facing workflow simpler over time, not more complicated.

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

### 2026-08-29 — canonical maker-view validator / one-command workflow fix
Baseline: `main@3ceb5f41f2c1ad55fb7b64b32c741cecce75c8e6`.

Changed:
- added `tools/validate_maker_view_manifest.py`
- added regression tests for maker-view semantics and structural-validator delegation
- changed `tools/make_next_short.ps1` to use the current maker-view validation path
- updated `CURRENT_STANDARD.md` with the canonical validation contract
- synchronized this handoff in the same branch

Why:
- the previous validator still required the obsolete `stop_if_pov...` gate, while TK-005 correctly uses `stop_if_maker_view...`; the user's normal command could therefore reject the current NEXT_EPISODE

Production impact:
- restores compatibility between current accepted maker-view semantics and the one-command prep workflow
- no change to TK-005 selection, H40 runtime, four-generation/40-credit first-pass ceiling, scene actions, Flow settings, audio, or NEXT_EPISODE
- no Flow credits spent; no publishing

Research verification:
- current yakiimo and Mini Forest-adjacent evidence does not change ranking/mechanics and was not added due saturation
- official Flow assumptions were rechecked; generation-time UI remains final truth

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
