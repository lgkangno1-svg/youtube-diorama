# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@1bfe81535616d5371cfbc08201eedad04b592a93`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer must be able to continue from GitHub without prior chat history. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Mission

Build a Japanese-target Shorts operating system, not merely an AI-cat generator. The normal user interface remains:

```text
다음 영상 준비해줘
```

The system should research current Japanese/global signals, choose a novelty-safe episode, prepare the manifest and `production/NEXT_EPISODE.txt`, generate deterministic local operator packs, and learn from production plus 24h/72h YouTube results. The user runs:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Viewer-facing identity

Default grammar: `POV_PAWS_MICROWORLD_V1`.

- true first-person cat POV
- only cream + pale-ginger real feline front paws near the lower edge
- no face/head/body/full-cat reveal
- hero object normally 5–20mm and <=0.50 of one paw width
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
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite supports 4s/6s/8s
- Ingredients/References can be 8s-only
- output count = 1
- 1080p upscaling = 0 credits for Plus/Pro/Ultra
- actual Flow UI active model/mode/output count/displayed cost remains final generation-time truth
- Flow can save a paused generated-video frame directly into the project with native `Save frame`
- Flow image generation supports adding existing images as references/ingredients
- Nano Banana image editing supports iterative edit/refine workflows and keeps prior versions in history/stack
- `Nano Banana 2 Lite` is currently described by official Flow help as a no-charge image generation/editing option

Because UI/costs can change, model names are not permanent pricing promises. Always verify the current Flow UI before generation.

Canonical operator docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `docs/29_planned_keyframe_continuity_chain.md`

## Gate A — zero-credit planned keyframes

Before any paid Veo generation:

```text
Flow image generation
→ active image model + displayed cost 확인
→ use no-charge path only when UI confirms it
→ create KF0 as master visual anchor
→ QC POV / paws / scale / camera / fixed props / lighting
→ derive KF1 from approved KF0 using image edit/refine or reference/ingredient
→ derive KF2 from approved KF1
→ continue sequentially for required planned KFs
→ only then proceed to G1
```

### New hard rule: planned keyframes are a continuity chain

Do **not** create KF0/KF1/KF2/KF3/KF4 as unrelated fresh text-to-image lottery tickets.

For KF1+:
- open/edit/refine the prior approved KF, or
- add the prior approved KF back to the Flow image prompt as a reference/ingredient
- change only the state required by the manifest
- preserve paw fur/anatomy, camera, hero-object scale, workbench geometry, fixed props, lighting and lens language

If a later planned KF drifts, repair it while image generation is still no-charge. Do not ask paid Veo to interpolate between incompatible endpoints.

QC shorthand: `KEYFRAME DRIFT FAIL`.

This planned-image chain is separate from the paid-video actual-frame chain:

```text
planned KF chain: KF0 → edit/reference → KF1 → edit/reference → KF2 ...
actual video chain: G1 PASS actual frame → Save frame → G2 First → ...
```

Planned KFs are destinations. Actual saved frames are continuity bridges.

## Progressive Spend

```text
FREE planned keyframe/reference preflight
→ G1 only
→ QC
→ save actual last usable frame with Flow native Save frame
→ G2 only after G1 PASS
→ QC
→ G3 only after G2 PASS
→ G4 only if immersive_h40 explicitly needs an independent world-resolution beat and G3 PASSed
```

Never substitute a prettier planned KF for the actual previous PASS frame when chaining paid scenes.

## Runtime policy

`compact_h30`:
- exactly 3 first-pass Lite scenes
- 30-credit current first-pass ceiling
- final roughly 30–36s

`immersive_h40`:
- exactly 4 first-pass Lite scenes
- 40-credit current first-pass ceiling
- final roughly 38–46s
- G4 must add independent serving/world-resolution/afterglow value

48–60s is not default until real channel retention and engaged-views-per-credit data supports it.

## Audio policy

Default:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

If motion is good and audio alone is bad, replace audio in edit rather than rerolling the video. Use a short user-recorded Japanese line only when it materially improves comprehension, character voice, or payoff.

## Deterministic production safeguards already built

- latest-main / recent-PR / handoff-first work-start order
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- zero-credit image-keyframe model/cost preflight
- **planned keyframe continuity chain: KF0 master anchor → edit/reference derived KF1+**
- manifest-aware H30/H40 guidance
- scene-count/generation-count/credit-budget consistency validation
- required 8s production scene length for current grammar
- keyframe map/reference integrity
- non-empty action/action_guard for every paid scene
- explicit zero-cut preservation in generated prompts
- actual-last-frame First-frame mapping
- native Flow `Save frame` bridge instructions for every sequential PASS scene
- progressive-spend PASS dependency validation
- sequential-chain metadata validation
- novelty/authenticity gate against repeated recent hook/conflict/ending fingerprints
- seasonal evidence saturation/no-churn gate
- bundle-level current-standard validation
- local handoff update guard
- regression tests for core production invariants

## Latest material change — planned keyframe continuity chain

Problem:
- planned KF0–KFn were previously listed as separate image prompts
- an operator could generate each from scratch, producing different paw identity, camera, prop placement, scale or lighting
- First+Last Veo would then need to interpolate both the intended food-state change and accidental world/camera changes, increasing drift/reroll risk

Fix:
- `tools/build_flow_pack.py` now explicitly tells the operator to create KF0 as the master anchor
- every later KF is derived from the prior approved KF through Flow image edit/refine or image reference/ingredient reuse
- the generated pack adds `KEYFRAME DRIFT FAIL`
- `tools/test_build_flow_pack.py` protects the new continuity instructions
- `docs/29_planned_keyframe_continuity_chain.md` documents the rationale and operator rule

Expected impact:
- same number of planned KFs
- no extra paid-video credits
- lower endpoint mismatch before G1
- fewer continuity/camera/prop rerolls per usable second

No story, candidate score, runtime, NEXT_EPISODE, or paid-generation budget changed.

## Research / idea policy

Sources:
- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`

Score ideas on benchmark evidence, Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand, and expected credit efficiency.

Never copy exact competitor titles, plots, branded products/packages, or endings. Extract only abstract mechanics: hook, scale contrast, tactile action, pacing, visual payoff, seasonal timing, and worldbuilding.

Do not keep committing same-class seasonal PR/news after evidence saturation unless it changes ranking, NEXT_EPISODE, timing, evidence class, production mechanics, freshness, Flow assumptions, or actual Tiny Cat Kitchen learning.

Current candidate state:
- `IDEA-009` yakiimo → realized as TK-005; blocked as future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate supported by current rice-reservation/arrival behavior
- `IDEA-002` gummy → currently blocked against a recent equivalent conflict/ending structure

Fresh 2026-08-27 research did not justify ranking, evidence-class, publish timing, or NEXT_EPISODE changes. Same-class Tsukimi/autumn retail announcements remain saturated and are not recorded merely to create commits.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`  
First-pass ceiling: 4 Lite generations / 40 credits under the currently verified non-Ultra Lite rate

Beats:
1. impossible-scale reveal — 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual warmth widens the crack and reveals golden center
4. same tray slides into the already-visible tiny serving niche; paws withdraw; steam remains

Continuity/action rules:
- same roasting tray G1–G4
- same fixed miniature tabletop warmer KF0–KF4
- same small serving niche upper-right KF0–KF4
- no surprise new cookware/shelf/stall structure
- no direct pinch/grab of sweet potato
- KF0 = master planned image anchor
- KF1→KF4 = sequential edit/reference derivations from previous approved planned KF
- G2 First = Flow-native saved actual last usable frame from G1 PASS
- G3 First = Flow-native saved actual last usable frame from G2 PASS
- G4 First = Flow-native saved actual last usable frame from G3 PASS
- every G scene has explicit action + action_guard
- zero-cut constraint remains literal in generated prompts

Highest-value next real-world step remains **generate/approve the TK-005 planned KF chain, then generate G1 only and QC it.** Automation must not spend that credit for the user.

## Production learning available

`analytics/learning_ledger.csv` currently contains one real preflight failure:
- third-person/full-cat framing
- body visible
- scale too large
- human-like tool-use risk

Hard response:
- true first-person camera
- front paws only
- hero object <=0.50 paw width
- prefer nudge/press/slide over gripping

There is not yet enough public 24h/72h performance data. Never treat placeholder zeroes as observations.

Long-term KPIs:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## Roadmap

### Phase A — TK-005 production truth
1. run local preparation/validation
2. create KF0 master anchor using current no-charge image path after checking UI cost
3. derive/approve KF1→KF4 from each prior approved KF using image edit/reference chaining
4. generate G1 only
5. QC POV / scale / anatomy / camera / action / zero-cut behavior / warmer+niche continuity
6. on PASS, save actual last usable G1 frame with Flow native `Save frame`
7. continue G2 → G3 → justified G4 only through progressive gates
8. record actual credits, rerolls, usable seconds and failure type

### Phase B — first public Shorts learning
At 24h/72h record Stayed to watch, APV, engaged views, subscribers, comments, final runtime, credits and rerolls.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 on APV, engaged views/credit, subscribers/100 credits and beat drop-off.

### Phase D — operator simplification
Keep reducing manual judgment so `다음 영상 준비해줘` remains sufficient. Update tooling only when actual Flow behavior or production evidence changes.

### Phase E — worldbuilding expansion
Only after performance evidence supports it, expand tiny-stall, rainy-shop, after-hours bakery, seasonal ritual and other distinct worlds without repeating the same story fingerprint.

## Next priorities

1. TK-005 planned KF0→KF4 continuity validation in real Flow
2. TK-005 actual G1 production/QC data
3. confirm zero-cut long-take behavior in real Flow output
4. verify actual-last-usable-frame continuity in practice
5. record actual credits/rerolls/usable motion
6. obtain first public 24h/72h sample
7. only then re-weight runtime/action/idea priors

More same-class retail PR collection is not a priority.

## Work-start order

Always inspect in this order:
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
- no independent fresh-generation planned KF1+ when an approved prior KF can anchor edit/reference continuity
- no substitute planned frame for an actual previous PASS frame
- no undefined/missing KF improvisation at production time
- no paid scene with blank action or blank action_guard
- no silent loss of an explicit `0`-cut scene constraint
- no next-scene spend after previous-scene failure
- no scene-count/runtime/credit mismatch
- no padding G4 merely to hit a duration
- no reroll of good motion for audio-only defects
- no placeholder analytics treated as real observations
- do not modify Cali or unrelated repositories

## Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ POV/tiny-scale production-safe manifest
→ spend/runtime/keyframe/action/cut consistency PASS
→ planned KF continuity chain PASS
→ progressive Flow generation
→ actual-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next episode prior update
```

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer continuity/camera rerolls, less operator judgment, and fewer repeated story fingerprints — not by commit count.

## Change log

### 2026-08-27 — Planned keyframe continuity chain
Baseline `main@1bfe81535616d5371cfbc08201eedad04b592a93`.

Changed:
- KF0 becomes master visual anchor
- KF1+ are derived from the previous approved KF through Flow edit/refine or image reference/ingredient reuse
- generated Flow Pack includes the rule and `KEYFRAME DRIFT FAIL`
- add regression coverage and `docs/29_planned_keyframe_continuity_chain.md`
- synchronize this handoff

Verified:
- official Flow image help supports iterative editing and adding existing images as prompt references
- no Flow/Veo pricing assumption change was required
- TK-005 directly benefits because warmer/niche/paw/camera continuity is critical across KF0–KF4

Unchanged:
- NEXT_EPISODE = TK-005
- immersive_h40 / four Lite scenes / current 40-credit first-pass ceiling
- no paid generation or publishing

### Earlier 2026-08-27 work
- zero-credit keyframe cost preflight
- Flow native `Save frame` sequential bridge
- TK-005 fixed warmer/niche continuity
- zero-cut prompt preservation
- scene-action integrity gate
- keyframe-reference integrity gate
- manifest spend consistency fail-closed gate
- runtime-aware operator guidance
- IDEA-010 new-rice onigiri candidate
- deterministic novelty/authenticity gate
