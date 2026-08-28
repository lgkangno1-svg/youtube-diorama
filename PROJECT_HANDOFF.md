# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected before this iteration: `main@80500b2dc295ad9dec6f2723bebdbcd7b5e4e0f5`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OP research must not churn it.

## Start-of-run contract

Before every material run:
1. inspect latest `main` SHA and recent commits/PRs
2. read this handoff
3. read `PRODUCT_CHARTER.md`
4. cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, current manifest, benchmark/backlog/ledger
5. newest explicit user direction + latest merged repository state override stale scheduled-prompt wording

Document roles:
- `PROJECT_HANDOFF.md` = current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md` = durable product purpose / identity / economics / improvement criteria
- `CURRENT_STANDARD.md` = executable production/QC/Flow/selection rules
- manifests + ledgers = episode plan + observed evidence

Sync policy:
- material change → handoff
- production/QC/Flow/selection rule change → current standard
- durable purpose/identity/economics philosophy change → product charter
- true NO-OP → no documentation churn

## Durable product intent

Tiny Cat Kitchen is a Japanese-target healing Shorts system for realistic miniature cooking/making where human hands are naturally replaced by feline front paws.

Non-negotiable:
- cream/pale-ginger front paws only, normally 1–2
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline tool grip
- absurdly tiny hero object, normally 5–20mm and <=0.50 paw width
- handcrafted miniature workbench/diorama realism
- process-first tactile making
- calm long-take ASMR
- default high-oblique maker view; top-down/side-oblique allowed
- literal cat-eye first-person POV is not mandatory
- no AI-cat human-job/character-performance regression

Primary optimization is **usable motion/credit, engaged views/credit, subscribers/100 credits**, not simply minimum credits/video.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: 4 Veo 3.1 Lite generations / 40 credits
Expected final: ~32–35s if all four beats remain independently useful

Visual intent:
- stable Mini Forest-style high-oblique maker view
- front paws only where human hands normally would enter
- 12mm yakiimo dramatically smaller than paw
- same tray / warmer / serving niche through KF0→KF4
- zero-cut calm long takes
- one active paw-safe action per generation + optional passive payoff
- explicit scene action families: G1 `nudge`, G2 `press`, G3 `slide`, G4 `slide`
- G4 = tray slide, then passive steam only

Paid continuity:
- G1: KF0 → KF1
- G2: actual saved G1 PASS frame → KF2
- G3: actual saved G2 PASS frame → KF3
- G4 only if still justified: actual saved G3 PASS frame → KF4

## Material improvement in this iteration — scene-level paw-action fail-closed gate

A production safety gap was found after candidate-level action gating was added:
- `tools/select_next_episode.py` already rejects unsafe candidate mechanics such as pinch/twist/grip.
- But an episode manifest can be edited after candidate selection.
- Before this change, `validate_maker_view_manifest.py` did not independently require a machine-readable safe action family for every paid G scene.
- Therefore a later manifest edit could reintroduce a human-dexterity action or multiple active paw actions and still reach the paid-generation boundary.

Corrected:
- `validate_maker_view_manifest.py` now requires every scene to declare `paw_action_family` with **exactly one** active action.
- Allowed set: `nudge / press / pat / roll / steady / slide / tap / push`.
- Missing action family, more than one active action, or unsupported action such as `pinch` now fails closed before Flow preparation.
- Passive material payoffs such as steam/crack/gloss are not counted as active paw actions.
- `episodes/TK-005.yaml` now declares G1 `nudge`, G2 `press`, G3 `slide`, G4 `slide` explicitly.
- regression tests cover missing, multi-action and unsafe-action failures.
- `CURRENT_STANDARD.md` synchronized in the same branch.

Why this matters:
- candidate safety alone is insufficient because manifests are durable/editable artifacts.
- the final paid-generation boundary now enforces the core `one calm tactile primary action + optional passive payoff` rule structurally rather than relying only on prose.
- this reduces avoidable anatomy/tool-use failures and reroll credits.

Production impact:
- no change to TK-005 story, selection, H40, keyframes, Flow model, scene count or 40-credit non-Ultra ceiling.
- no Flow credits spent.
- no publishing.

## Canonical validation / selection state

Candidate selection:
- `tools/select_next_episode.py` is fail-closed
- hero-scale ratio max must be <=0.50 paw width
- candidate paw actions must stay in `nudge / press / pat / roll / steady / slide / tap / push`
- unsupported human-dexterity actions are rejected before ranking
- legacy `POV_PAWS_MICROWORLD_V1` is compatibility-only

Manifest / bundle validation:
- canonical production semantic gate is `tools/validate_maker_view_manifest.py`
- all production bundle entry points route through it
- every paid scene must declare exactly one safe `paw_action_family`
- `validate_current_standard.py` is internal structural/runtime validation behind the adapter, not a direct current-semantic entry point
- legacy POV values may remain only as compatibility data and cannot restore mandatory literal first-person framing

## Flow / spend baseline

Official Google Flow Help rechecked 2026-08-29:
- Veo 3.1 Lite: non-Ultra 10 credits/generation, Ultra 5 credits/generation
- non-subscriber: 50 free Flow credits/day
- Plus/Pro/Ultra: 1080p upscale currently 0 credits
- non-subscriber: 1080p upscale unavailable
- actual UI model/mode/output count/displayed cost = generation-time final truth

Progressive Spend:

```text
free/no-charge planned KF chain PASS
→ G1 only
→ QC
→ native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if runtime/manifest still justifies independent final value
→ continuity chain complete
→ eligible subscription + UI shows 0 credits: QC-PASS clips may be upscaled to 1080p
```

Never spend Flow credits, generate paid video, or publish without explicit user action.

## Current learning

One real preflight failure remains recorded:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Correct interpretation:
- observer/maker-view itself is not a failure
- body reveal + character-performance framing + weak miniature scale is the failure
- maker-view + paws-only + tiny workpiece is desirable

No trustworthy public 24h/72h Tiny Cat Kitchen performance sample yet. Do not learn from placeholders/theoretical zeros.

## Research / candidate state

Primary benchmark class:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat channels remain secondary only for narrow paw/anatomy/reliability evidence. Never copy exact title, plot, branded product/package, distinctive set/dish styling, or ending.

Evidence saturation remains active. Same-class promotional/retail signals do not justify commits unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual production learning.

2026-08-29 cross-check:
- sweet-potato/yakiimo evidence remains saturated and still supports TK-005
- fresh 月見 product/event signals confirm IDEA-001 timing but do not outrank or invalidate the current prepared TK-005 production state
- benchmark/backlog were intentionally not churned
- official Flow pricing remains: Lite 10 non-Ultra / 5 Ultra; 1080p upscale 0 for paid Plus/Pro/Ultra

Candidate state:
- TK-005 / IDEA-009 remains current production choice
- IDEA-001 月見 and IDEA-010 新米塩むすび remain strong future seasonal candidates

## Current roadmap / next priorities

1. Keep all production entry points routed through `validate_maker_view_manifest.py`.
2. Keep one-safe-action-per-scene manifest validation fail-closed.
3. Run current maker-view manifest/bundle path for TK-005 when the user executes `./tools/make_next_short.ps1`.
4. Create/approve TK-005 KF0 master anchor in real Flow.
5. Derive KF1→KF4 sequentially with stable paws/scale/camera/props/lighting.
6. Generate G1 only after planned KF chain passes.
7. QC maker-view / paws-only / scale / anatomy / fixed props / zero-cut behavior.
8. PASS → save actual native usable final frame → continue progressively.
9. After chain completion, if eligible and UI shows 0 credits, upscale QC-PASS clips to 1080p before final editing/export.
10. Record actual credits, rerolls, usable motion, G-stage pass/fail, failure class.
11. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers, comments.
12. Use accumulated real evidence to adjust actions, runtimes, scores, and spend strategy.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs
- no human-like paw grip
- no candidate hero-scale ratio >0.50 paw width without documented exception
- no unsafe candidate paw-action family through selector
- no paid scene without exactly one safe `paw_action_family`
- no paid G1 before planned KF continuity passes
- no next paid scene after prior structural failure
- actual previous PASS native saved frame is the continuity bridge
- upscaled/re-encoded exports are not continuity bridges
- non-first-person maker view is not a failure by itself
- no direct production entry point to legacy structural validator
- no runtime padding
- no research churn after saturation
- no unrelated repository modifications
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — scene-level paw-action fail-closed validation
Baseline: `main@80500b2dc295ad9dec6f2723bebdbcd7b5e4e0f5`.

Changed:
- required exactly one machine-readable safe `paw_action_family` per paid scene in `validate_maker_view_manifest.py`
- added regression coverage for missing, multiple and unsafe action families
- annotated TK-005 G1/G2/G3/G4 with `nudge / press / slide / slide`
- synchronized `CURRENT_STANDARD.md` and this handoff

Why:
- prevents post-selection manifest edits from reintroducing human-dexterity or multi-action prompts immediately before paid Flow generation

Production impact:
- TK-005 remains H40 / four Lite generations / 40-credit non-Ultra first-pass ceiling
- no content/ranking/keyframe/runtime changes
- no credits spent; no publishing

### 2026-08-29 — zero-credit 1080p PASS finishing
- documented official Plus/Pro/Ultra 1080p upscale at current 0-credit cost
- added PASS-only, post-continuity upscale rule

### 2026-08-29 — canonical bundle maker-view validation path
- routed bundle creation through `validate_maker_view_manifest.py`
- preserved structural/runtime validation behind the current-semantic adapter

### 2026-08-29 — candidate selector maker-view safety gates
- enforced <=0.50 paw-width scale and feline-safe action allowlist before ranking

### 2026-08-29 — canonical maker-view manifest validator
- aligned one-command manifest validation with Mini Forest-style maker-view semantics

### 2026-08-29 — TK-005 maker-view spend-gate correction
- replaced stale active POV stop-gate wording with maker-view semantics

### 2026-08-29 — sweet-potato search-demand evidence
- added a distinct search-behavior evidence class; TK-005 remained top-ranked

### 2026-08-28 — product governance
- added `PRODUCT_CHARTER.md`
- wired charter into the improvement loop
- established Mini Forest-style miniature making + feline front paws replacing human hands as canonical visual identity
