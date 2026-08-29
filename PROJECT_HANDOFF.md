# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@5761758e7ff9809ecf6d98840e59ff7be7338fcc`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. A true NO-OP must not churn it.

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
- Mini Forest-style high-oblique maker view
- front paws only where human hands normally enter
- 12mm yakiimo dramatically smaller than paw
- same tray / warmer / serving niche through KF0→KF4
- zero-cut calm long takes
- one active paw-safe action per generation + optional passive payoff
- scene action families: G1 `nudge`, G2 `press`, G3 `slide`, G4 `slide`

Paid continuity:
- G1: KF0 → KF1
- G2: actual saved G1 PASS frame → KF2
- G3: actual saved G2 PASS frame → KF3
- G4 only if still justified: actual saved G3 PASS frame → KF4

## Material improvement in this iteration — no-charge keyframe gate now survives into generated bundle

Problem found after inspecting the latest merged one-command path:
- `tools/make_next_short.ps1` correctly requires `Nano Banana 2 Lite` plus a visible no-charge UI state before planned KF work.
- `tools/build_flow_pack.py` also contains the detailed fail-closed image preflight.
- however, the generated top-level `${episode_id}_bundle.md` produced by `tools/build_episode_bundle.py` still told the operator to approve “free keyframes/contact sheet” without carrying the model + displayed-cost requirement.
- a user who reopened only the bundle later could therefore miss the newer fail-closed preflight and treat an image-model change as automatically free.

Corrected:
- generated bundle Approval A now says planned keyframes are approved only after Flow is set to `Nano Banana 2 Lite` **and** the UI confirms no charge.
- if the active image model or displayed keyframe cost is different or unclear, the bundle itself tells the operator to STOP and not treat Gate A as free.
- regression coverage in `tools/test_build_episode_bundle_runtime.py` now fails if this protection disappears or the old generic “Approve ... free keyframes/contact sheet” wording returns.

Why this matters:
- the simple user workflow produces artifacts that may be reopened independently of the PowerShell console.
- cost/safety gates must be self-contained in those artifacts, not only transient terminal output.
- this closes a realistic preflight credit-leak path without changing episode content or adding generations.

Production impact:
- no change to TK-005 story, ranking, runtime, keyframes, scene count, paw actions, video model, or 40-credit first-pass ceiling.
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

Learning semantics:
- current structural camera/framing fields are `maker_view_failure` and `character_failure`
- scale/anatomy/continuity remain separate failure classes
- `pov_failure` is deprecated compatibility data only
- non-first-person maker view is not a failure by itself

## Flow / spend baseline

Official Google Flow pages rechecked on 2026-08-29:
- Veo 3.1 Lite 4s/6s/8s: 10 credits/generation for non-Ultra, 5 for Ultra
- free non-subscriber accounts receive 50 Flow credits/day; these do not stack on paid Plus/Pro/Ultra allocations
- Nano Banana 2 Lite is documented in Flow Help as the default image model available at no charge
- actual active model, feature eligibility and UI displayed cost remain final truth

Current operator sequence:

```text
Flow image preflight:
Nano Banana 2 Lite + UI confirms no charge
→ KF0 maker-view master anchor
→ derive KF1→KFn sequentially
→ all planned KFs PASS

Paid video:
→ Veo 3.1 Lite / 9:16 / 8s / output 1 / displayed cost verified
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

Current interpretation:
- observer/non-first-person maker-view itself is not a failure
- full-cat/body character framing is `character_failure`
- workbench/process framing collapse is `maker_view_failure`
- weak tiny scale is `scale_failure`

No trustworthy public 24h/72h Tiny Cat Kitchen performance sample yet. Do not learn from placeholders/theoretical zeros.

## Research / candidate state

Primary benchmark class:
- realistic miniature cooking/making
- handcrafted tiny-food process
- relaxing tactile ASMR

AI-cat channels remain secondary only for paw/anatomy/reliability evidence. Never copy exact title, plot, branded product/package, distinctive set/dish styling, or ending.

Evidence saturation remains active. Same-class promotional/retail signals do not justify commits unless they change ranking, timing, evidence class, production mechanics, Flow assumptions, freshness, or actual production learning.

2026-08-29 cross-check:
- sweet-potato/yakiimo evidence remains saturated and still supports TK-005
- current Japanese sweet-potato event/menu signals are same-class and do not change ranking or production mechanics
- 月見 remains a strong next seasonal class but does not invalidate prepared TK-005
- no benchmark/backlog churn was justified in this iteration

Candidate state:
- TK-005 / IDEA-009 remains current production choice
- IDEA-001 月見 and IDEA-010 新米塩むすび remain strong future seasonal candidates

## Current roadmap / next priorities

1. Keep all production entry points routed through `validate_maker_view_manifest.py`.
2. Keep one-safe-action-per-scene validation fail-closed.
3. Keep KF preflight no-charge fail-closed in **every operator artifact**: Nano Banana 2 Lite + UI confirms no charge before image generation/editing.
4. Run current maker-view manifest/bundle path for TK-005 when the user executes `./tools/make_next_short.ps1`.
5. Create/approve TK-005 KF0 master anchor in real Flow, then derive KF1→KF4 sequentially.
6. Generate G1 only after planned KF chain passes.
7. QC maker-view / paws-only / scale / anatomy / fixed props / zero-cut behavior.
8. PASS → save actual native usable final frame → continue progressively.
9. Record actual credits, rerolls, usable motion, G-stage pass/fail, failure class.
10. After upload, record 24h/72h Stayed to watch, APV, engaged views, subscribers, comments.
11. Use accumulated real evidence to adjust actions, runtimes, scores, and spend strategy.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs
- no human-like paw grip
- no candidate hero-scale ratio >0.50 paw width without documented exception
- no paid scene without exactly one safe `paw_action_family`
- no keyframe spend when no-charge image model/cost is not confirmed
- generated bundle/Flow guidance must not call planned KFs generically free without the no-charge gate
- no paid G1 before planned KF continuity passes
- no next paid scene after prior structural failure
- actual previous PASS native saved frame is the continuity bridge
- upscaled/re-encoded exports are not continuity bridges
- non-first-person maker view is not a failure by itself
- no runtime padding
- no research churn after saturation
- no unrelated repository modifications
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — generated-bundle no-charge KF gate
Baseline: `main@5761758e7ff9809ecf6d98840e59ff7be7338fcc`.

Changed:
- `tools/build_episode_bundle.py`: carry Nano Banana 2 Lite + UI no-charge fail-closed requirement into generated bundle Approval A
- `tools/test_build_episode_bundle_runtime.py`: regression guard against generic-free keyframe wording
- synchronized this handoff

Why:
- the terminal had the safe rule, but a later-opened generated bundle could omit it and become a credit-leak bypass

Production impact:
- TK-005 remains H40 / four Lite video generations / 40-credit non-Ultra first-pass ceiling
- no episode/ranking/keyframe/runtime changes
- no credits spent; no publishing

### 2026-08-29 — no-charge image preflight operator gate
- `make_next_short.ps1` requires Nano Banana 2 Lite + UI no-charge confirmation before KF work

### 2026-08-29 — learning maker-view failure semantics
- added `maker_view_failure` and `character_failure`; deprecated `pov_failure` to compatibility-only fallback

### 2026-08-29 — scene-level paw-action fail-closed validation
- required exactly one safe `paw_action_family` per paid scene

### 2026-08-29 — zero-credit 1080p PASS finishing
- added PASS-only post-continuity upscale guidance

### 2026-08-29 — canonical bundle maker-view validation path
- routed bundle creation through `validate_maker_view_manifest.py`

### 2026-08-29 — candidate selector maker-view safety gates
- enforced <=0.50 paw-width scale and feline-safe action allowlist before ranking

### 2026-08-29 — sweet-potato search-demand evidence
- added distinct search-behavior evidence; TK-005 remained top-ranked

### 2026-08-28 — product governance
- added `PRODUCT_CHARTER.md` and durable document-role rules
