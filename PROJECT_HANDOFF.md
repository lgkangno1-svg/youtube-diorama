# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-27 KST**  
Baseline inspected before this change: `main@eab9cc1b304a74e26d45906b33467b625ffdba05`

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
- Flow can save a paused generated-video frame directly into the project with the native `Save frame` action; that saved frame can then be used as an ingredient, start frame, or end frame

Do not confuse an existing-video edit / Omni Flash modify screen with standard new-video generation.

Canonical operator docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`

## Progressive Spend

```text
FREE keyframe/reference preflight
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

- source-of-truth work-start order
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- manifest-aware H30/H40 guidance
- scene-count/generation-count/credit-budget consistency validation
- required 8s production scene length for current grammar
- keyframe map/reference integrity
- non-empty action/action_guard for every paid scene
- explicit zero-cut preservation in generated prompts
- actual-last-frame First-frame mapping
- **native Flow `Save frame` bridge instructions for every sequential PASS scene**
- progressive-spend PASS dependency validation
- sequential-chain metadata validation
- novelty/authenticity gate against repeated recent hook/conflict/ending fingerprints
- seasonal evidence saturation/no-churn gate
- bundle-level current-standard validation
- local handoff update guard
- regression tests for core production invariants

## Latest material change — native Flow frame bridge

Official Flow documentation confirms a generated clip can be opened, paused on a frame, and that exact frame can be saved into the project with `Save frame`, after which it can be reused as a start/end frame.

Before this change the generated Flow Pack only said to “save the actual last usable frame” and suggested a local PNG filename. That left room for an operator to use a browser screenshot, screen capture, downloaded/re-encoded still, or reconstructed target frame. Those alternatives can change pixels/crop/compression/state and undermine the purpose of sequential continuity.

Fix in `tools/build_flow_pack.py`:
- after a scene PASS, explicitly instruct: open the PASS clip → pause on exact last usable frame → hover → click native `Save frame`
- use that saved Flow project asset as the next First frame
- screenshots/re-encoded/recreated stills are now explicitly discouraged when native Save frame is available
- `FRAME CHAIN FAIL` includes using the wrong non-native bridge asset
- recovery instruction reopens the PASS clip and saves the correct frame rather than rerolling or substituting a planned target

Regression coverage in `tools/test_build_flow_pack.py` now requires these instructions to remain present.

This is a 0-credit operator/tooling improvement. It changes no episode story, runtime, ranking, generation count, or spend ceiling.

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

Fresh 2026-08-27 research still does not justify ranking, evidence-class, or NEXT_EPISODE changes. Same-class Tsukimi/autumn retail announcements are saturated and are not recorded merely to create commits.

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`  
First-pass ceiling: 4 Lite generations / 40 credits

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

Highest-value next real-world step: **generate TK-005 G1 only and QC it.** Automation must not spend that credit for the user.

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
1. approve free opening/target frames
2. run local preparation/validation
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

1. TK-005 actual G1 production/QC data
2. confirm warmer + distant serving niche + tray + paw + camera layout survives G1
3. verify zero-cut long-take behavior in real Flow output
4. verify native Save frame → next First frame continuity in practice
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

Newer merged repository state overrides stale chat or automation wording.

## Safety / invariants

- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no human fingers/thumbs/tool-grip regression
- no undefined/missing KF improvisation
- no blank paid-scene action/action_guard
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
→ free frame preflight
→ progressive Flow generation
→ native Save frame actual-frame continuity chain
→ edit/export
→ upload
→ 24h/72h learning
→ next episode prior update
```

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer camera/continuity rerolls, less operator judgment, and fewer repeated story fingerprints — not by commit count.

## Change log

### 2026-08-27 — Native Flow Save-frame bridge
Baseline `main@eab9cc1b304a74e26d45906b33467b625ffdba05`.

Changed:
- convert ambiguous “save last usable frame” guidance into Flow-native `Save frame` steps
- require that native saved project asset as the preferred next-scene First frame
- discourage screenshot/re-encoded/recreated continuity stills
- add regression assertions for the native bridge instructions
- synchronize this handoff

Verified:
- official Flow documentation explicitly supports saving a paused video frame to the project and reusing it as start/end frame
- Veo 3.1 Lite 4/6/8s pricing and First+Last support remain unchanged on 2026-08-27
- NEXT_EPISODE remains TK-005
- immersive_h40 and 40-credit first-pass ceiling unchanged
- fresh seasonal research does not justify candidate/ranking changes

No Flow credits spent, no paid generation, no publishing.

### Earlier 2026-08-27 work
- full TK-005 warmer + serving-niche static-prop continuity
- G1 warmer continuity fix
- bundle-level current-standard validation
- progressive-spend/sequential-chain manifest validation
- explicit zero-cut prompt preservation
- scene-action/keyframe integrity gates
- runtime-aware operator guidance
- explicit First/Last actual-frame mapping
- deterministic novelty/authenticity gate
