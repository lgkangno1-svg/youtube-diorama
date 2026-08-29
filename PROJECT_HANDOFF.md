# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@1a52f249b3d5ca1b432d3f16f52976266f84a6a0`

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
Current non-Ultra first-pass ceiling: up to 4 Veo 3.1 Lite generations / 40 video credits
Primary operator runbook: `production/TK-005_OPERATOR_CARD.md`

Quality intent:
- HOOK: first 1–2s instantly read as feline paws + absurdly tiny 12mm yakiimo + real miniature making
- TRANSFORMATION: warm/darken → crack/steam → golden center → optional quiet serving resolution
- SCALE PROOF: hero roughly 18–32% of visible paw width
- PAYOFF: bright golden center + steam; G4 only if serving niche adds independent satisfaction
- same tray / warmer / serving niche / camera / paw identity through the chain

Scene actions:
- G1 `nudge`
- G2 `press`
- G3 `slide`
- G4 `slide` only if value-gated after real G3

Continuity:
- G1 KF0→KF1
- G2 actual saved G1 PASS frame→KF2
- G3 actual saved G2 PASS frame→KF3
- G4 actual saved G3 PASS frame→KF4 only if still justified

## Material improvement in this iteration — source-of-truth docs no longer point back to cost-first workflow

Problem found after inspecting merged PR #68:
- `CURRENT_STANDARD.md`, `PRODUCT_CHARTER.md`, the operator scripts and this handoff already define quality/content → viewer outcome → production speed → paid-video efficiency as the priority.
- however, `START_HERE.md` still described the normal path around generic generated packs and a cost-led Gate A, without making the episode Operator Card the primary execution surface.
- `docs/23_minimum_credit_operator_architecture.md`, despite being a required source-of-truth file on every loop, still framed the architecture primarily as minimum-credit/free-KF optimization.
- `docs/22_continuous_episode_learning_engine.md` still optimized mainly around failures/credits and did not carry the new operator-speed metrics or Operator-Card-First creation loop.
- because scheduled/future AIs are explicitly told to cross-check these files every run, this disagreement could regress development back toward cost guards and away from video quality / fast creation even though implementation had already moved on.

Corrected:
- `START_HERE.md`
  - now states the durable priority order up front
  - makes `production/<EPISODE>_OPERATOR_CARD.md` the PRIMARY RUNBOOK and generated bundle/flow-pack fallback/reference
  - adds the content quality gate: HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / NOVELTY-JAPAN FIT
  - treats Nano Banana as a quality/continuity tool in the user's current free-access context
  - adds preparation-time/manual-intervention learning targets
- `docs/23_minimum_credit_operator_architecture.md`
  - legacy filename retained for links, but heading/purpose now explicitly Quality-First Fast Operator Architecture
  - normal workflow is one command → one Operator Card → strong KF chain → progressive paid generation
  - paid efficiency remains protected without letting cost minimization dominate product decisions
  - adds `time-to-first-valid-G1`, manual interventions and prompt corrections as operator metrics
- `docs/22_continuous_episode_learning_engine.md`
  - creation loop now requires the exact-order Operator Card as a first-class artifact
  - learning loop includes hook/scale/transformation/payoff hypotheses plus production-speed evidence
  - official Flow re-check is triggered when production assumptions need changing rather than becoming the focus of every loop

Why material:
- these are mandatory cross-check documents, so semantic drift here can steer every future automated iteration
- the update reduces the chance that another AI optimizes the wrong proxy
- it aligns product intent, operator implementation and learning loop without changing TK-005 or spending credits

Production impact:
- no change to TK-005 concept, H40 ceiling, scene actions, candidate ranking or paid authorization
- no Flow/Veo credits spent
- no publishing

## Canonical validation / safety state

- candidate selector fail-closed for <=0.50 paw-width scale and feline-safe actions
- canonical manifest/bundle semantic entry is `tools/validate_maker_view_manifest.py`
- every paid scene declares exactly one safe `paw_action_family`
- `maker_view_failure` / `character_failure` are current learning fields; `pov_failure` compatibility-only
- non-first-person maker view is not a failure by itself
- actual previous PASS native saved frame is the next-scene continuity bridge
- structural FAIL stops the next paid scene

These gates remain. Current improvement focus is content/operator quality unless a real regression appears.

## Research / evidence state

Fresh 2026-08-29 research rechecked current miniature/ASMR and Japanese sweet-potato signals:
- a Japanese miniature-cooking channel snapshot still shows an active ~198K-subscriber / ~62M-view category presence and prior ~19-second miniature Shorts, reinforcing the already-known value of immediately legible tiny-food process
- fresh late-August Japanese sweet-potato retail launches continue to confirm autumn timing
- these are same-class/saturated signals and did not change TK-005 ranking, runtime or production mechanics, so `research/benchmark_log.csv` and backlog were intentionally not churned

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
- 24h/72h Stayed to watch/APV/engaged views/subscribers/comments

## Current roadmap / next priorities

1. Keep source-of-truth docs aligned with the quality-first Operator-Card-First workflow; do not return to cost-guard polishing without a real problem.
2. Run `./tools/make_next_short.ps1`; it should point directly to `production/TK-005_OPERATOR_CARD.md`.
3. Do only the Operator Card NOW action first: make the strongest KF0 scale-hook anchor.
4. Derive KF1→KF4 sequentially; reject scale/camera/prop drift before paid video.
5. Generate G1 only after visual continuity passes; judge first-1–2s readability and feline-safe nudge quality.
6. PASS → native Save frame → continue progressively.
7. After real G3, keep G4 only if it adds independent resolution value.
8. Record production-time/manual-intervention data so the next tooling improvement targets actual friction rather than guessed friction.
9. Use real 24h/72h audience results to adjust hook/action/runtime priors.

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

### 2026-08-29 — quality-first operating-system alignment
Baseline: `main@1a52f249b3d5ca1b432d3f16f52976266f84a6a0`.

Changed:
- `START_HERE.md`: Operator Card is now the documented primary runbook; quality gate + speed metrics added
- `docs/23_minimum_credit_operator_architecture.md`: legacy filename retained but architecture redefined as quality-first/fast-production, with paid efficiency as a constraint rather than the product goal
- `docs/22_continuous_episode_learning_engine.md`: Operator Card + content-quality hypotheses + operator-speed metrics added to the learning loop
- synchronized this handoff

Why:
- mandatory source-of-truth docs were semantically lagging behind PRs #66–#68 and could steer future scheduled improvements back toward cost-first optimization

Production impact:
- TK-005 remains H40 / up to four paid Lite scenes / current 40-credit non-Ultra ceiling
- no paid generation/publishing

### 2026-08-29 — Operator-Card-First normal path
- normal scripts surface episode Operator Card before bundle/flow-pack

### 2026-08-29 — TK-005 quality operator card
- explicit HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF / JAPAN FIT
- exact-order copy/paste KF/G prompts

### 2026-08-29 — quality/speed priority correction
- video/content quality → viewer outcome → production speed/convenience → paid-video efficiency → free-image cost policing
