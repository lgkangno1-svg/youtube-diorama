# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-29 KST**
Baseline inspected for this iteration: `main@b9e8382df1fb906ae3cf43781ac64e3b331602e9`

Durable current-state handoff for `lgkangno1-svg/youtube-diorama`. Every material change updates this file in the same branch/PR; true NO-OP does not churn it.

## Start-of-run contract

Before material work: inspect latest main/recent PRs → read this handoff → `PRODUCT_CHARTER.md` → cross-check `START_HERE.md`, `CURRENT_STANDARD.md`, docs/22/23/27, NEXT_EPISODE/current manifest, benchmark/backlog/ledger. Newer explicit user direction and latest merged state override stale scheduled wording.

Document roles:
- `PROJECT_HANDOFF.md`: current state / decisions / failures / learning / next priorities
- `PRODUCT_CHARTER.md`: durable purpose / priority order / improvement criteria
- `CURRENT_STANDARD.md`: executable production/QC/operator rules
- manifests + ledgers: episode plan + observed evidence

## Latest user priority clarification — 2026-08-29

The user explicitly clarified:
- Nano Banana is available free in their Google usage context.
- Stop centering development on Nano Banana cost protection.
- Focus primarily on **video quality and content quality**.
- Also optimize **how the user should make the videos, convenience, fast production, and practical efficiency**.

Durable priority order is now:
1. video/content quality
2. viewer outcome / recognizable channel identity
3. production convenience and speed
4. paid-video reroll/credit efficiency
5. free-image cost policing

Existing image-cost fail-closed guards remain as harmless safety rails, but further cost-gate hardening/research/documentation is deprioritized unless the user reports a real change/problem. Paid Veo generation and publishing still require explicit user action.

`PRODUCT_CHARTER.md` and `CURRENT_STANDARD.md` were synchronized in this iteration to prevent future AIs from returning to repeated free-image cost-gate work.

## Durable product intent

Japanese-target healing Shorts: realistic handcrafted miniature cooking/making with one or two cream/pale-ginger feline front paws replacing the visual role of human hands.

Non-negotiable:
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline grip
- hero normally 5–20mm and <=0.50 paw width
- miniature process is the protagonist
- high-oblique maker view by default; top-down/side macro allowed
- literal first-person POV not mandatory
- calm tactile long takes / close ASMR
- no AI-cat job/character-performance regression

## New quality-first content gate

Before paid video, every episode should make these explicit:
- **HOOK**: first 1–2s immediately communicate tiny + paws + making
- **TRANSFORMATION**: visible state change per scene, not motion for motion's sake
- **SCALE PROOF**: shot where paw/object contrast is strongest
- **PAYOFF**: finished/steam/crack/gloss/serving reason to stay
- **NOVELTY/JAPAN FIT**: why this subject now and what makes it distinct

If one is weak, improve premise/shot/action rather than adding runtime.

## Fast-production operator target

Normal interface remains:
```text
다음 영상 준비해줘
```

The prepared output should minimize user assembly work:
- complete topic/rationale/runtime choice
- exact-order KF prompts
- exact-order G prompts
- invariant settings/negative constraints already included
- one obvious `지금 할 것` at a time
- clear PASS/FAIL criteria
- manifest/NEXT_EPISODE/handoff already synchronized

Tooling improvements should target:
- lower time-to-first-valid-G1
- fewer manual interventions per episode
- fewer prompt corrections before G1
- fewer rerolls per finished episode

Do not add warning/documentation layers unless they materially improve quality, speed, paid-video efficiency, or safety.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**
Title: `猫の前足で作る、12mmの焼きいも。`
Manifest: `episodes/TK-005.yaml`
Runtime tier: `immersive_h40`
Current non-Ultra first-pass ceiling: up to 4 Veo 3.1 Lite generations / 40 video credits

Visual intent:
- Mini Forest-style high-oblique maker view
- paws only
- 12mm yakiimo dramatically smaller than paw
- same tray/warmer/serving niche through KF0→KF4
- zero-cut calm takes
- G1 `nudge`, G2 `press`, G3 `slide`, G4 `slide`

Continuity:
- G1 KF0→KF1
- G2 actual saved G1 PASS frame→KF2
- G3 actual saved G2 PASS frame→KF3
- G4 only if still justified: actual saved G3 PASS frame→KF4

## Canonical validation state

- candidate selector fail-closed for <=0.50 paw-width scale and feline-safe actions
- canonical manifest/bundle semantic entry is `tools/validate_maker_view_manifest.py`
- every paid scene declares exactly one safe `paw_action_family`
- `maker_view_failure` / `character_failure` are current learning fields; `pov_failure` is compatibility-only
- non-first-person maker view is not a failure by itself

These safety gates stay; current priority is no longer spending iterations polishing them unless a real failure appears.

## Flow / production baseline

Current paid-video strategy remains Progressive Spend:
```text
strong visual/keyframe continuity PASS
→ G1 only
→ quality QC
→ actual native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if independent payoff remains worthwhile
```

Actual Flow UI at paid generation time remains final truth for model/mode/output count/displayed cost. No automatic paid generation/publishing.

Nano Banana/reference frames should now be treated primarily as a **free quality/continuity tool available to the user**, not as a cost-risk research target. Build the strongest KF0 and sequential destinations efficiently.

## Current learning

One real preflight failure remains:
- full cat/body visible
- hero scale too large
- human-like tool-use risk

Interpretation: observer maker-view is fine; character framing, weak scale and human-like manipulation are failures.

No trustworthy public 24h/72h Tiny Cat Kitchen sample yet. Do not learn from placeholders.

Future real production should additionally record when practical:
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1

## Research / candidate state

Evidence saturation remains active. TK-005 / IDEA-009 remains current production choice. 月見 and 新米塩むすび remain strong future seasonal classes. No new research/backlog churn was needed for this user-priority correction.

## Current roadmap / next priorities

1. **Stop spending iterations on Nano Banana free-cost guard polishing unless a real problem is reported.**
2. Audit TK-005 specifically for hook strength, tactile transformation, scale proof and final payoff before paid generation.
3. Improve KF0→KF4 prompts/visual anchors for miniature realism and continuity, using the user's free Nano Banana access efficiently.
4. Improve G1 prompt/first-last-frame plan to maximize first-pass quality.
5. Make generated operator pack more copy/paste-ready and reduce the number of decisions/clicks the user must make.
6. When real production begins, measure preparation time/manual interventions/prompt corrections in addition to video credits/rerolls.
7. Generate G1 only after visual preflight passes; inspect actual output before G2.
8. Record real 24h/72h audience results and use them to improve content/runtimes/actions.

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

### 2026-08-29 — quality/speed priority correction
Baseline: `main@b9e8382df1fb906ae3cf43781ac64e3b331602e9`.

Changed:
- `PRODUCT_CHARTER.md`: made video/content quality, viewer outcome, production convenience/speed, then paid-video efficiency the explicit priority order; recorded that Nano Banana is free for the user's Google usage and repeated cost-gate development is deprioritized
- `CURRENT_STANDARD.md`: added HOOK/TRANSFORMATION/SCALE PROOF/PAYOFF/NOVELTY quality gate, fast-preparation operator target, and operational speed metrics
- synchronized this handoff

Why:
- recent iterations over-focused on preventing free-image credit leakage; the user explicitly wants development attention redirected to what viewers see and how quickly/easily a high-quality Short can be made

Production impact:
- TK-005 remains H40 / up to 4 paid Lite generations / current 40-credit non-Ultra ceiling
- no Flow/Veo credits spent; no publishing
- next improvement work should be content/prompt/operator quality, not more Nano Banana cost-gate polishing

### 2026-08-29 — previous operational hardening
- normal operator surfaces currently contain Nano Banana/no-charge safety wording
- learning semantics, scene-action validation, maker-view adapter and continuity rules remain in force
