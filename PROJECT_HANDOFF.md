# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@d6c5f206c2f6b8dd279b8190bbbbb9093ebd6e15`

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
- only cream + pale-ginger real feline front paws visible near lower edge
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
- Flow can save a paused generated-video frame directly into the project with native `Save frame`; that saved frame can then be used as an ingredient/start/end frame
- official image-model help currently describes `Nano Banana 2 Lite` as the default fast image generation/editing model **available at no charge**

Because UI/costs can change, `Nano Banana 2 Lite` is a preferred current no-charge option, not a permanent hard-coded promise. Gate A only counts as 0-credit when Flow itself shows 0/no charge before generation.

Do not confuse an existing-video edit / Omni Flash modify screen with standard new-video generation.

Canonical operator docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`

## Gate A — zero-credit planned keyframes

Before any paid Veo generation:

```text
Flow image generation
→ active image model 확인
→ prefer Nano Banana 2 Lite while UI shows no charge
→ verify displayed cost = 0 / no charge
→ generate only manifest-required KF frames
→ QC POV / paws-only / scale / anatomy / fixed props
→ only then proceed to G1
```

Rules:
- never assume a keyframe is free merely because the repository calls it a FREE KF
- if image generation shows a non-zero cost, stop and re-check model/current pricing rather than spending by accident
- do not generate decorative alternatives merely because the model is free; create only planned KF frames needed for the manifest
- reject bad POV/scale/anatomy/fixed-prop layout at image stage before any video credits are exposed

This closes a practical operator gap: earlier packs said “approve free keyframes” without telling the user how to verify that the current Flow image generation state is actually no-charge.

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

Sequential continuity always uses the real previous PASS frame as the next First frame. Never substitute a prettier planned target frame. Prefer Flow's native saved project frame over browser screenshots, screen captures, downloaded/re-encoded stills, or recreated frames.

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
- **zero-credit image-keyframe model/cost preflight**
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

## Latest material change — keyframe cost preflight

Problem:
- the repository has long called planned image keyframes “FREE” and uses them as Gate A before paid Veo clips
- the generated Flow Pack did not explicitly tell the operator which current image model is the no-charge option or require checking the UI-displayed cost before generating the KF set
- that ambiguity matters because Flow model availability/pricing can change, and the user wants a simple low-credit workflow

Fix:
- `tools/build_flow_pack.py` now starts with a dedicated `Gate A — FREE keyframe preflight` section
- it recommends `Nano Banana 2 Lite` only while Flow itself marks it available at no charge
- it requires the operator to check active image model + displayed cost before each planned KF generation
- any non-zero image cost triggers STOP/re-check instead of silent spend
- it tells the operator to create only the manifest-required KF set, not endless decorative alternatives
- `tools/test_build_flow_pack.py` now asserts this cost-preflight guidance remains present
- `docs/23_minimum_credit_operator_architecture.md` now documents the same rule

This is a 0-credit operator/tooling improvement. It changes no episode story, runtime, ranking, generation count, or paid-video ceiling.

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
- same fixed miniature tabletop warmer remains explicit KF0–KF4
- same small serving niche remains visible at the upper-right KF0–KF4
- no surprise new cookware/shelf/stall structure
- no direct pinch/grab of sweet potato
- G2 First = Flow-native saved actual last usable frame from G1 PASS
- G3 First = Flow-native saved actual last usable frame from G2 PASS
- G4 First = Flow-native saved actual last usable frame from G3 PASS
- all planned KF references resolve before preparation
- every G scene has explicit action + action_guard
- zero-cut constraint remains literal in generated prompts

Highest-value next real-world step remains **generate TK-005 G1 only and QC it.** Automation must not spend that credit for the user.

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
2. create/approve manifest-required KF0–KF4 using the current no-charge image path after checking actual UI cost
3. generate G1 only
4. QC POV / scale / anatomy / camera / action / zero-cut behavior / warmer+niche continuity
5. on PASS, use Flow native `Save frame` on the exact last usable frame
6. continue G2 → G3 → justified G4 only through progressive gates
7. record credits/rerolls/usable seconds/failure type

### Phase B — first public Shorts learning
At 24h/72h record Stayed to watch, APV, engaged views, subscribers, comments, final runtime, credits, and rerolls.

### Phase C — runtime learning
Compare compact_h30 vs immersive_h40 using APV, engaged views/credit, subscribers/100 credits, and beat drop-off.

### Phase D — operator simplification
Keep reducing manual judgment so `다음 영상 준비해줘` remains sufficient. Add tooling only when actual Flow behavior or production evidence reveals a real risk.

### Phase E — worldbuilding expansion
After performance evidence exists, expand distinct tiny stalls, rainy shops, after-hours bakery, seasonal rituals, and other worlds without repeating story fingerprints.

## Next priorities

1. TK-005 actual Gate-A KF creation/QC using a UI-confirmed no-charge image model
2. TK-005 actual G1 production/QC data
3. confirm warmer + distant serving niche + tray + paw + camera layout survives G1
4. verify zero-cut long-take behavior in real Flow output
5. verify native Save frame → next First frame continuity in practice
6. record actual credits/rerolls/usable motion
7. obtain first public 24h/72h sample
8. only then re-weight runtime/action/idea priors

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

Newer merged repository state overrides stale chat or automation wording.

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no human fingers/thumbs/tool-grip regression
- no undefined/missing KF improvisation
- no assumption that a planned image KF is free without checking actual UI cost
- no paid scene with blank action/action_guard
- no next-scene spend before previous PASS
- no stale progressive-spend or sequential-chain metadata
- no planned target frame substituted for previous actual PASS frame
- prefer Flow native saved actual frame over screenshot/re-encoded/recreated bridge assets
- no scene-count/runtime/credit mismatch
- no major static prop appearing or disappearing mid-generation when it can be fixed in planned frames
- no padding G4
- no reroll of good motion for audio-only defects
- no placeholder analytics treated as real data
- do not modify Cali or unrelated repositories

## Definition of Done

```text
current research
→ scored + novelty-safe candidate
→ POV/tiny-scale production-safe manifest
→ current-standard + originality validation PASS
→ spend/runtime/keyframe/action/cut/chain validation PASS
→ UI-confirmed 0-credit planned keyframe preflight
→ progressive Flow generation
→ native Save frame actual-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next episode prior update
```

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer camera/continuity rerolls, less operator judgment, and fewer repeated story fingerprints — not by commit count.

## Change log

### 2026-08-27 — Zero-credit keyframe cost preflight
Baseline `main@d6c5f206c2f6b8dd279b8190bbbbb9093ebd6e15`.

Changed:
- add explicit Gate-A image-model/cost verification to generated Flow Pack
- prefer Nano Banana 2 Lite only while current Flow UI marks it no-charge
- stop if displayed image-generation cost is non-zero instead of assuming planned KF is free
- limit free image generation to manifest-required keyframes
- add regression assertions for this guidance
- refresh minimum-credit operator documentation
- synchronize this handoff

Verified:
- official Flow model help currently describes Nano Banana 2 Lite as available at no charge
- official Veo 3.1 Lite 4/6/8s + Extend pricing remains 10 credits/generation for non-Ultra
- First+Last support and native Save frame behavior remain available
- fresh seasonal/adjacent research did not change candidate ranking or NEXT_EPISODE

Unchanged:
- NEXT_EPISODE = TK-005
- TK-005 story/runtime/4-generation structure
- 40-credit current first-pass video ceiling
- candidate ranking
- no credits spent, no paid generation, no publishing

### Earlier 2026-08-27 work
- native Flow Save-frame bridge
- full TK-005 warmer + serving-niche static-prop continuity
- G1 warmer continuity fix
- bundle-level current-standard validation
- progressive-spend/sequential-chain manifest validation
- explicit zero-cut prompt preservation
- scene-action/keyframe integrity gates
- runtime-aware operator guidance
- deterministic novelty/authenticity gate
