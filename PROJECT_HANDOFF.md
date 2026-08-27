# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@2578b066727eec536d84cc6c1b074531fcb15221`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer must be able to continue from GitHub without prior chat history. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Mission

Build a Japanese-target Shorts operating system, not merely an AI-cat generator. The normal user interface remains:

```text
다음 영상 준비해줘
```

The system researches current Japanese/global signals, chooses a novelty-safe episode, prepares the manifest and `production/NEXT_EPISODE.txt`, generates deterministic operator packs, and learns from production plus 24h/72h YouTube results. The user runs:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Viewer-facing identity

Default grammar: `POV_PAWS_MICROWORLD_V1`.

- true first-person cat POV
- only cream + pale-ginger feline front paws near the lower edge
- no face/head/body/full-cat reveal
- hero object normally 5–20mm and <=0.50 paw width
- macro miniature diorama workbench
- mostly locked camera
- one calm tactile primary action + at most one micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- no human fingers/thumbs/human-like tool grip
- no rapid montage or third-person chef framing

Core appeal: the viewer should feel like the cat handling an impossibly tiny world. The attraction is scale contrast and tactile calm, not a cat face.

Canonical identity docs:
- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

## Flow / Veo baseline

Official Google Flow help rechecked **2026-08-27**:
- Google AI Pro: 1,000 Flow credits/month
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite supports 4s/6s/8s
- Ingredients/References to Video: Lite can be 8s-only
- output count = 1
- 1080p upscaling = 0 credits for Plus/Pro/Ultra
- Gemini Omni Flash edits are a different, higher-cost path
- Nano Banana 2 Lite is currently described as a no-charge default image generation/editing option
- actual Flow UI active model/mode/output count/displayed cost is final generation-time truth

Canonical operator docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `docs/29_planned_keyframe_continuity_chain.md`

## Gate A — planned keyframe continuity

Before any paid Veo generation:

```text
Flow image generation
→ check active image model + displayed cost
→ use no-charge path only when UI confirms it
→ create KF0 master visual anchor
→ QC POV / paws / scale / camera / fixed props / lighting
→ derive KF1 from approved KF0 using edit/refine or reference/ingredient
→ derive KF2 from approved KF1
→ continue sequentially
→ only proceed to G1 after all required planned KFs PASS
```

Hard rule: do not create KF1+ as unrelated fresh text-to-image lottery tickets when an approved previous KF can anchor continuity.

If drift occurs, repair it in the no-charge image stage. Do not make paid Veo interpolate accidental camera/world changes. QC shorthand: `KEYFRAME DRIFT FAIL`.

Planned KFs are destinations. Actual video frames are continuity bridges.

## Progressive Spend / actual-frame chain

```text
planned KF chain PASS
→ G1 only
→ QC
→ Flow native Save frame from actual last usable frame
→ G2 only after G1 PASS
→ QC
→ Save frame
→ G3 only after G2 PASS
→ G4 only if immersive_h40 explicitly needs independent world-resolution value and G3 PASSed
```

Never substitute a prettier planned KF for the actual previous PASS frame in a paid-scene chain.

## Runtime policy

`compact_h30`:
- exactly 3 first-pass Lite scenes
- current 30-credit first-pass ceiling
- final roughly 30–36s

`immersive_h40`:
- exactly 4 first-pass Lite scenes
- current 40-credit first-pass ceiling
- final roughly 38–46s
- G4 must add independent serving/world-resolution/afterglow value

48–60s is not default until the channel's own retention and engaged-views-per-credit data supports it.

## Audio policy

Default:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

If motion is good and audio alone is bad, replace audio in edit rather than rerolling video. Use a short user-recorded Japanese line only when it materially improves comprehension, character voice, or payoff.

## Deterministic safeguards already built

- latest-main / recent-PR / handoff-first work-start order
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- zero-credit image-model/cost preflight
- planned KF continuity chain
- manifest-aware H30/H40 guidance
- scene-count/generation-count/credit-budget consistency validation
- 8s scene requirement for current grammar
- keyframe map/reference integrity
- non-empty action/action_guard for every paid scene
- explicit zero-cut preservation
- actual-last-frame First-frame mapping
- Flow native Save frame bridge instructions
- progressive-spend PASS dependency validation
- sequential-chain metadata validation
- novelty/authenticity gate against repeated recent fingerprints
- seasonal evidence saturation/no-churn gate
- bundle-level current-standard validation
- local handoff update guard
- regression tests for core production invariants

## Latest material change — CURRENT_STANDARD synchronization

Problem found after PR #35:
- `PROJECT_HANDOFF.md`, `docs/23_minimum_credit_operator_architecture.md`, generated Flow Packs, and `docs/29_planned_keyframe_continuity_chain.md` had adopted the new planned-KF continuity workflow.
- root `CURRENT_STANDARD.md` still showed its older 2026-08-25 baseline and only described a generic free keyframe preflight + paid actual-frame chain.
- because `CURRENT_STANDARD.md` is a declared source of truth, a future AI/operator could follow it and regress to independent KF generation or skip the KF0→KF1→... continuity rule.

Fix:
- refresh `CURRENT_STANDARD.md` to the 2026-08-27 operating baseline
- make the no-charge image-model/cost preflight explicit
- make KF0 master anchor + KF1+ edit/reference chaining explicit
- distinguish planned target KFs from actual saved-video continuity frames
- include native `Save frame`, zero-cut long-take, current H30/H40 rules, and current TK-005 production state

This is a documentation source-of-truth consistency fix. No story, scoring, runtime, NEXT_EPISODE, or paid budget changes.

## Research / idea policy

Sources:
- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`

Score ideas on benchmark evidence, Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand, and expected credit efficiency.

Never copy exact competitor titles, plots, branded products/packages, or endings. Extract only abstract mechanisms: hook, scale contrast, tactile action, pacing, payoff, seasonal timing, worldbuilding.

Do not keep committing same-class seasonal PR/news after evidence saturation unless it changes ranking, NEXT_EPISODE, timing, evidence class, production mechanics, freshness, Flow assumptions, or real Tiny Cat Kitchen learning.

Current candidate state:
- `IDEA-009` yakiimo → realized as TK-005; blocked as future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate backed by current reservation/arrival behavior
- `IDEA-002` gummy → blocked against a recent equivalent conflict/ending structure

Fresh 2026-08-27 review did not justify ranking, evidence-class, publish-timing, or NEXT_EPISODE changes. Same-class autumn retail announcements remain saturated.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:
```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`  
First-pass ceiling: 4 Lite generations / current 40 credits

Beats:
1. impossible-scale reveal — 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual warmth widens the crack and reveals golden center
4. same tray slides into the already-visible serving niche; paws withdraw; steam remains

Continuity/action rules:
- same roasting tray G1–G4
- same fixed tabletop warmer KF0–KF4
- same serving niche upper-right KF0–KF4
- no surprise new cookware/structure
- no direct pinch/grab
- KF0 = master planned anchor
- KF1→KF4 = sequential edit/reference derivations from previous approved planned KF
- G2/G3/G4 First = Flow-native actual saved frame from previous PASS clip
- explicit action + action_guard in every G scene
- literal zero-cut constraint in generated prompt

Highest-value next real-world step: **approve TK-005 KF0→KF4 in real Flow, then generate G1 only and QC it.** Automation must not spend that credit.

## Production learning available

`analytics/learning_ledger.csv` has one real preflight failure:
- third-person/full-cat framing
- body visible
- scale too large
- human-like tool-use risk

Hard response:
- true first-person camera
- front paws only
- hero object <=0.50 paw width
- prefer nudge/press/slide over gripping

No trustworthy public 24h/72h sample exists yet. Never treat placeholder zeroes as observations.

Long-term KPIs:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## Roadmap

### Phase A — TK-005 production truth
1. local preparation/validation
2. KF0 master anchor using current no-charge image path after UI-cost check
3. derive/approve KF1→KF4 through edit/reference chaining
4. generate G1 only
5. QC POV / scale / anatomy / camera / action / zero-cut / fixed-prop continuity
6. on PASS, Save frame
7. continue G2 → G3 → justified G4 through progressive gates
8. record actual credits, rerolls, usable seconds, failure type

### Phase B — first public Shorts learning
At 24h/72h record Stayed to watch, APV, engaged views, subscribers, comments, final runtime, credits, rerolls.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 on APV, engaged views/credit, subscribers/100 credits, beat drop-off.

### Phase D — operator simplification
Keep `다음 영상 준비해줘` sufficient; reduce manual judgment only when real Flow behavior supports it.

### Phase E — worldbuilding expansion
Expand distinct worlds only after performance evidence, without repeating recent story fingerprints.

## Next priorities

1. real Flow TK-005 KF0→KF4 continuity validation
2. actual G1 production/QC
3. real zero-cut long-take behavior
4. actual saved-frame continuity
5. actual credits/rerolls/usable motion
6. first public 24h/72h sample
7. then re-weight runtime/action/idea priors

## Work-start order

1. latest main SHA
2. recent commits/PRs
3. `PROJECT_HANDOFF.md`
4. `START_HERE.md`
5. `CURRENT_STANDARD.md`
6. `docs/22_continuous_episode_learning_engine.md`
7. `docs/23_minimum_credit_operator_architecture.md`
8. `production/NEXT_EPISODE.txt`
9. current episode manifest
10. research/backlog/learning ledger

Stale chat or automation wording never overrides newer merged repository state.

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no independent fresh-generation planned KF1+ when prior approved KF can anchor continuity
- no planned KF substituted for previous actual PASS frame
- no undefined KF improvisation
- no blank action/action_guard
- no silent loss of zero-cut constraint
- no next-scene spend after previous-scene failure
- no scene-count/runtime/credit mismatch
- no padding G4
- no reroll of good motion for audio-only defects
- no placeholder analytics treated as real observations
- do not modify Cali or unrelated repositories

## Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ production-safe manifest
→ deterministic validation PASS
→ planned KF continuity PASS
→ progressive paid generation
→ actual-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next prior update
```

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer continuity/camera rerolls, less operator judgment, and fewer repeated story fingerprints — not commit count.

## Change log

### 2026-08-27 — CURRENT_STANDARD synchronized to actual production OS
Baseline `main@2578b066727eec536d84cc6c1b074531fcb15221`.

Changed:
- root `CURRENT_STANDARD.md` now reflects planned keyframe continuity, no-charge image preflight, actual Save-frame chaining, zero-cut behavior, adaptive H30/H40, and current TK-005 state
- removed the risk of a future agent following the stale 2026-08-25 production baseline
- synchronized this handoff

Verified:
- official Google Flow help still lists Veo 3.1 Lite 4/6/8s + Extend at 10 credits/generation for non-Ultra
- Lite First+Last remains 4/6/8s
- Nano Banana 2 Lite remains described as the no-charge default image option
- no candidate/NEXT_EPISODE change justified

Unchanged:
- NEXT_EPISODE = TK-005
- immersive_h40 / four Lite scenes / current 40-credit first-pass ceiling
- no paid generation or publishing

### Earlier 2026-08-27 work
- planned keyframe continuity chain
- zero-credit keyframe cost preflight
- Flow native Save frame bridge
- TK-005 fixed warmer/niche continuity
- zero-cut prompt preservation
- scene-action/keyframe/spend integrity gates
- runtime-aware operator guidance
- IDEA-010 new-rice onigiri candidate
- deterministic novelty/authenticity gate
