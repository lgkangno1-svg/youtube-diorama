# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@adad83d51df36ecec8e3a31f51c75891503709c8`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material repository change must update this file in the same branch/PR. True NO-OPs do not churn it.

## Start-of-run contract

Before material work:
1. inspect latest main SHA and recent commits/PRs
2. read this handoff
3. read `PRODUCT_CHARTER.md`
4. cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, `production/NEXT_EPISODE.txt`, current manifest, benchmark/backlog/ledger
5. newest explicit user direction + latest merged state override stale automation/chat wording

Document roles:
- `PROJECT_HANDOFF.md`: current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md`: durable purpose / priority order / improvement criteria
- `CURRENT_STANDARD.md`: executable production/QC/operator rules
- manifests + ledgers: episode plan + observed evidence

## Durable priority order

1. video/content quality
2. viewer outcome / recognizable channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

Nano Banana is free in the user's current Google usage context. Existing model/cost checks remain safety rails only. Do not spend improvement cycles polishing them unless a real problem returns. Paid Veo generation and publishing remain explicit user actions.

## Durable product intent

Japanese-target healing Shorts: realistic handcrafted miniature cooking/making with one or two cream/pale-ginger feline front paws replacing the visual role of human hands.

Non-negotiable:
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline grip
- hero normally 5–20mm and <=0.50 paw width
- miniature process is the protagonist
- high-oblique maker view default; top-down/side macro allowed
- literal first-person POV not mandatory
- calm tactile long takes / close ASMR
- no AI-cat job/character-performance regression

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**
Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: **up to** 4 Veo 3.1 Lite generations / 40 video credits
Primary operator runbook: `production/TK-005_OPERATOR_CARD.md`

### Current adaptive runtime truth

TK-005 is explicitly designed as:
- **G1→G3 = complete core Short**
- **G4 = optional after real G3 review only**
- normal final runtime if G3 is complete: roughly 24–27s
- final runtime if G4 genuinely improves closure: roughly 32–35s
- H40 is a maximum first-pass spend tier, not a requirement to spend four generations

Manifest semantics:
- `minimum_distinct_motion_beats: 3`
- `fourth_beat_optional_after_g3: true`
- optional G4 remains pre-described so the idea is ready, but its existence is not spend permission

Scene actions:
- G1 `nudge`
- G2 `press`
- G3 `slide`
- G4 `slide` only if value-gated after real G3

Continuity:
- G1 KF0→KF1
- G2 actual saved G1 PASS frame→KF2
- G3 actual saved G2 PASS frame→KF3
- optional G4 actual saved G3 PASS frame→optional KF4

## Material improvement in this iteration — H40 no longer over-prepares or semantically forces G4

Problem found after the quality-first docs were aligned:
- current docs and Operator Card said G4 is optional/value-gated after real G3.
- `episodes/TK-005.yaml` still declared four minimum beats and a 32–35s-only target.
- the old keyframe path required KF0→KF4 before G1 even though real G3 might make KF4 unnecessary.
- the legacy structural validator interpreted `immersive_h40` as a four-beat plan shape.
- after fixing those layers, a further executable mismatch was found: `tools/build_healing_edit_plan.py` still summed every manifest scene, so an optional G4 candidate would appear in the initial 32s edit timeline anyway.

Corrected:
- `tools/validate_maker_view_manifest.py`
  - current H40 semantics require 3 core beats + explicit `fourth_beat_optional_after_g3: true`
  - legacy structural validator receives compatibility-only four-beat translation internally
  - current user-facing manifest remains truthful: G4 is not mandatory
- `tools/test_validate_maker_view_manifest.py`
  - regression coverage for 3-core + optional-G4 H40
  - rejects mandatory-four-core current semantics
  - requires explicit after-G3 value gate
  - confirms adapter does not mutate current manifest
- `episodes/TK-005.yaml`
  - adaptive 24–35s target
  - G3 explicitly complete core ending
  - G4 explicitly optional after real G3 review
- `production/TK-005_OPERATOR_CARD.md`
  - pre-G1 work stops at KF0→KF3
  - KF4 intentionally deferred
  - after G3, watch G1→G3 and stop if complete
  - only if G4 improves closure, derive KF4 from the **actual G3 PASS saved frame**, then generate G4
  - G1 starts motion gently without wasting the opening on a long dead hold
- `tools/build_healing_edit_plan.py`
  - adaptive H40 initial edit plan now includes only G1→G3 core footage
  - raw/core runtime math uses 24s of generated core motion instead of assuming G4 exists
  - outputs an explicit `Optional G4 decision — after real G3 only` section
  - optional G4 is only folded into a later edit after the real G3 review justifies generation
  - removed stale true-first-person edit wording in favor of current maker-view/paws-only semantics
- `tools/test_build_healing_edit_plan_runtime.py`
  - regression coverage ensures adaptive H40 core plan contains G1/G2/G3 but not a G4 timeline entry
  - verifies 24s core source, after-G3 decision guidance, and actual-saved-G3 target derivation
  - verifies non-optional four-scene plans still include G4 normally
- `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23 synchronized with lazy optional-target behavior

Why this matters:
- directly improves video quality by forcing G3 to carry the actual payoff rather than relying on a fourth scene
- reduces unnecessary pre-production and edit-planning work
- prevents runtime padding and accidental fourth-generation pressure
- preserves a 40-credit maximum ceiling without treating 40 credits as a target
- improves continuity if G4 is used because its target is based on the actual G3 result rather than a speculative prebuilt frame

Production impact:
- no paid generation performed
- no publishing
- TK-005 remains current; same safe paw-action families
- maximum paid ceiling remains 40 credits, while a strong three-generation episode may intentionally finish at 30 credits

## Canonical validation / safety state

- candidate selector fail-closed for <=0.50 paw-width scale and feline-safe actions
- canonical manifest/bundle semantic entry is `tools/validate_maker_view_manifest.py`
- every paid scene declares exactly one safe `paw_action_family`
- `maker_view_failure` / `character_failure` are current learning fields; `pov_failure` compatibility-only
- non-first-person maker view is not a failure by itself
- actual previous PASS native saved frame is the next-scene continuity bridge
- structural FAIL stops the next paid scene
- adaptive H40 current semantic: three complete core beats, optional fourth only after real G3 review
- adaptive edit-plan generation must likewise exclude optional G4 until that review

## Research / evidence state

Fresh 2026-08-29 cross-check found current miniature/ASMR category scale and late-August Japanese sweet-potato signals still support the existing tiny-food/process/seasonality thesis. These were same-class, already-saturated signals and did not change TK-005 ranking, timing, or production mechanics, so `research/benchmark_log.csv` and backlog were intentionally not churned.

TK-005 / IDEA-009 remains current. 月見 and 新米塩むすび remain strong future seasonal candidates.

## Current learning

One real preflight failure remains recorded:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Interpretation:
- observer maker-view itself is fine
- character framing, weak scale and human-like manipulation are failures

No trustworthy public 24h/72h Tiny Cat Kitchen performance sample yet. Do not learn from placeholders.

When real production begins, record when practical:
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1
- credits/rerolls/G-stage pass-fail
- whether optional G4 was correctly skipped or used after real G3 review
- 24h/72h Stayed to watch/APV/engaged views/subscribers/comments

## Current roadmap / next priorities

1. Run `./tools/make_next_short.ps1`; it should point directly to `production/TK-005_OPERATOR_CARD.md`.
2. Make/approve KF0, then derive only KF1→KF3 before paid video.
3. Generate G1 only after core KF continuity passes; judge scale hook and feline-safe nudge quality.
4. PASS → native Save frame → G2 → PASS → G3.
5. Watch G1→G3 together. If golden-center payoff is complete, stop and edit the roughly 24–27s Short.
6. Only if real G3 clearly benefits from same-world serving closure: derive KF4 from actual saved G3 PASS frame, then generate optional G4.
7. Initial generated healing edit plan must remain core-only while G4 is unresolved.
8. Record production time/manual interventions and whether lazy optional-target planning saved work.
9. Use real 24h/72h audience results to adjust hook/action/runtime priors.

## Validation note

Local git clone/test execution was attempted in this environment but DNS could not resolve `github.com`, so local `python tools/validate_handoff_update.py --base origin/main` and unit-test execution were not available. Regression tests were added as source-level guards; branch-level GitHub diff/PR validation is required before merge.

## Safety / invariants

- no automatic paid generation
- no automatic YouTube publishing
- no exact competitor copying
- no full-cat/face/body default shots
- no human hands/fingers/thumbs or human-like paw grip
- no weak-scale regression
- no next paid scene after structural failure
- actual previous PASS native frame is continuity bridge
- no runtime padding
- no research churn after saturation
- no unrelated repository changes
- every material change synchronizes this handoff

## Change log

### 2026-08-29 — adaptive H40 core-first / lazy optional G4 target + edit-plan alignment
Baseline: `main@adad83d51df36ecec8e3a31f51c75891503709c8`.

Changed:
- maker-view validator: current H40 = 3 required core beats + explicit optional-after-G3 fourth beat; compatibility translation remains internal
- maker-view validator regression tests added
- TK-005 manifest: adaptive 24–35s, G3 complete core ending, optional G4
- TK-005 Operator Card: KF0→KF3 before G1; optional KF4 deferred until real G3 proves G4 worthwhile
- healing edit-plan builder: initial adaptive-H40 timeline is G1→G3 only; optional G4 gets an after-G3 decision section instead of automatic inclusion
- healing edit-plan regression tests added
- START_HERE / CURRENT_STANDARD / docs/22/23 synchronized
- this handoff synchronized in same branch

Why:
- old manifest/validator/keyframe/edit-plan semantics could steer the workflow toward unnecessary G4 spend and unnecessary KF4 pre-production despite the accepted adaptive-runtime policy

Production impact:
- maximum ceiling unchanged: up to 4 Lite generations / 40 non-Ultra credits
- a strong G1→G3 can intentionally finish at the three-generation level and the generated edit plan now agrees
- no credits spent; no publishing

### 2026-08-29 — quality-first operating-system alignment
- START_HERE/docs22/docs23 aligned with quality-first Operator-Card-First workflow

### 2026-08-29 — Operator-Card-First normal path
- normal scripts surface episode Operator Card before generated fallback docs

### 2026-08-29 — TK-005 quality operator card
- explicit HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / JAPAN FIT

### 2026-08-29 — quality/speed priority correction
- video/content quality → viewer outcome → production speed/convenience → paid-video efficiency → free-image cost policing
