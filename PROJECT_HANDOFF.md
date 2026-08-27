# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-28 KST**  
Baseline inspected before this change: `main@2f637bd740d5e38c80dab99b304325b308741939`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer must be able to continue from GitHub without prior chat history. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Development execution policy

`AGENTS.md` is authoritative.

- repository development is performed directly by the active Chat/Codex session
- do not delegate coding/planning/debugging/refactoring/review/test repair/architecture/repository exploration to OpenCode Go
- latest merged repository state overrides stale chat or automation wording
- inspect latest main SHA + recent commits/PRs before every change

## Mission

Build a Japanese-target Shorts operating system, not merely an AI-cat generator.

Normal user interface:

```text
다음 영상 준비해줘
```

System responsibilities:
- research current Japanese/global AI-cat, miniature cooking, ASMR, relaxing-food and adjacent signals
- identify timely but novelty-safe episode candidates
- score ideas for Japan relevance, healing fit, visual satisfaction, Veo reliability, originality, worldbuilding, audience demand and expected usable-quality-per-credit
- maintain episode manifest + `production/NEXT_EPISODE.txt`
- generate deterministic local Flow/edit/publish packs
- minimize paid-generation failure with no-charge/free preflight where the live UI supports it
- learn from real production plus 24h/72h YouTube metrics

User local entrypoint:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Viewer-facing identity

Default grammar: `POV_PAWS_MICROWORLD_V1`.

- true first-person cat POV
- only cream + pale-ginger feline front paws near lower edge
- no face/head/body/full-cat reveal
- hero object normally 5–20mm and <=0.50 of one visible paw width
- macro miniature diorama workbench
- mostly locked camera
- one calm tactile primary action + at most one passive micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- no human fingers/thumbs/human-like gripping
- no rapid montage / no third-person chef framing

Core appeal: viewer feels like the cat handling an impossibly tiny world. Scale contrast + tactile calm matter more than showing a cat face.

Canonical identity docs:
- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

## Flow / Veo baseline

Official Google Flow Help rechecked **2026-08-28**:
- Google AI Pro: 1,000 Flow credits/month
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames remain supported for the current Lite workflow
- output count = 1
- 1080p upscaling = 0 credits for Plus/Pro/Ultra
- actual Flow UI active model/mode/output count/displayed cost is the generation-time source of truth
- Omni Flash is a different/higher-cost path; do not confuse existing-video edit mode with standard new-video generation

Canonical operator docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `docs/29_planned_keyframe_continuity_chain.md`

## Gate A — planned keyframe continuity

Mandatory before paid G1:

```text
Flow image generation/editing
→ verify active image model + displayed cost
→ use no-charge path only when UI confirms it
→ create KF0 master visual anchor
→ QC POV / paws / scale / camera / fixed props / lighting
→ derive KF1 from approved KF0
→ derive KF2 from approved KF1
→ continue sequentially through all manifest-required KFs
→ all planned KFs PASS
→ only then generate G1
```

KF1+ must not be independent fresh text-to-image lottery tickets when the prior approved KF can anchor continuity.

Preserve across the planned chain:
- paw fur/anatomy
- first-person camera/lens
- hero-object scale
- workbench geometry
- fixed props
- lighting/material language

Only intended food/material state changes.

QC shorthand: `KEYFRAME DRIFT FAIL`.

Important distinction:
- planned KF = approved scene destination / target state
- actual saved video frame = next-scene continuity bridge

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

Never substitute a prettier planned target KF for the actual previous PASS frame.

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

48–60s is not default until the channel's own retention + engaged-views-per-credit data supports it.

## Audio policy

Default:

```text
No narration
No generated music
Quiet room tone + close tiny tactile ASMR
```

If motion is good and audio alone is bad, replace audio in edit rather than rerolling video. Use a short user-recorded Japanese line only when it materially improves comprehension, character voice, or payoff.

## Deterministic safeguards already built

- latest-main / recent-PR / `AGENTS.md` / handoff-first work-start order
- POV paw-only + tiny-scale hard gates
- Flow generation-vs-edit UI preflight
- no-charge image-model/cost preflight
- planned KF0→KFn continuity chain
- manifest-aware H30/H40 guidance
- scene-count/generation-count/credit-budget consistency validation
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
- local handoff-update guard
- regression tests for core production invariants
- **planned keyframe scene-order gate: for all-First+Last manifests, G1 must start at the first ordered KF and every G scene must end at the next ordered KF; extra decorative KFs are rejected**

## Latest fix — planned keyframe scene-order gate

Problem found on **2026-08-28**:
- existing validation correctly rejected undefined `KF*` tokens
- however, a scene could still point to a **defined but wrong** target KF and pass; e.g. G2 could accidentally end at `KF3_OPEN` instead of `KF2_CRACK`
- Gate A builds KFs sequentially, so this mismatch could make the paid Flow pack interpolate toward the wrong state even though every referenced KF exists
- that creates avoidable continuity drift and reroll risk per credit

Fix:
- when every paid scene uses `first_plus_last`, require exactly one opening KF + one ordered target KF per scene
- require G1 start = first planned KF
- require G1/G2/G3/G4 end frames to follow manifest keyframe insertion order exactly
- reject unused decorative extra KFs in this all-First+Last production mode
- add regression coverage against current TK-005 plus wrong-defined-target / wrong-G1-start / extra-KF mutations

This is a 0-credit safety improvement. It does not change TK-005 story, runtime, generation count, budget or candidate ranking.

## Research / idea policy

Sources:
- `research/benchmark_log.csv`
- `research/seasonal_evidence.yaml`
- `ideas/episode_backlog.yaml`
- `ideas/novelty_signatures.yaml`
- `docs/27_research_evidence_saturation_gate.md`
- `docs/28_episode_novelty_authenticity_gate.md`

Never copy exact competitor title, plot, branded product/package or ending. Extract only abstract mechanisms: hook, scale contrast, tactile action, pacing, payoff, seasonal timing, worldbuilding.

Evidence saturation rule: do not keep committing same-class seasonal retail/PR signals after a candidate is already well supported unless the new evidence changes ranking, NEXT_EPISODE, timing, evidence class, production mechanics, freshness, Flow assumptions or real Tiny Cat Kitchen learning.

2026-08-28 research check:
- official Flow pricing/features remain unchanged for the current Lite workflow
- current Japanese sweet-potato/autumn signals continue to support the already-selected yakiimo timing but are same-class evidence already represented
- no newly found adjacent content signal changes candidate rank, production mechanic or NEXT_EPISODE
- research/backlog files intentionally remain unchanged this run

Current candidate state:
- `IDEA-009` yakiimo → realized as TK-005; blocked as future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate backed by current reservation/arrival behavior
- `IDEA-002` gummy → blocked against recent equivalent conflict/ending structure

## Current production state

`production/NEXT_EPISODE.txt` = **TK-005**

Title:

```text
猫の前足で作る、12mmの焼きいも。
```

Manifest: `episodes/TK-005.yaml`  
Runtime: `immersive_h40`  
First-pass ceiling: 4 Lite generations / current 40 credits

Planned KFs:
1. `KF0_OPEN`
2. `KF1_WARM`
3. `KF2_CRACK`
4. `KF3_OPEN`
5. `KF4_SERVE`

Paid scene destinations:
- G1: `KF0_OPEN → KF1_WARM`
- G2: actual saved G1 frame → `KF2_CRACK`
- G3: actual saved G2 frame → `KF3_OPEN`
- G4: actual saved G3 frame → `KF4_SERVE`

Beats:
1. impossible-scale reveal — 12mm purple sweet potato beside paws
2. slow roast / skin crack
3. same tray slides away; residual warmth widens crack and reveals golden center
4. same tray slides into already-visible serving niche; paws withdraw; steam remains

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

Highest-value next real-world step remains **approve TK-005 KF0→KF4 in real Flow, then generate G1 only and QC it.** Automation must not spend that credit.

## Production learning available

`analytics/learning_ledger.csv` currently has one real preflight failure:
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
1. run local preparation/validation
2. create/approve KF0 master anchor using UI-confirmed no-charge image path
3. derive/approve KF1→KF4 through sequential edit/reference chaining
4. generate G1 only
5. QC POV / scale / anatomy / camera / action / zero-cut / fixed-prop continuity
6. on PASS, native Save frame
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
7. only then re-weight runtime/action/idea priors

## Work-start order

1. latest main SHA
2. recent commits/PRs
3. `AGENTS.md`
4. `PROJECT_HANDOFF.md`
5. `START_HERE.md`
6. `CURRENT_STANDARD.md`
7. `docs/22_continuous_episode_learning_engine.md`
8. `docs/23_minimum_credit_operator_architecture.md`
9. `production/NEXT_EPISODE.txt`
10. current episode manifest
11. research/backlog/learning ledger

## Safety / invariants

- no OpenCode Go delegation for repository development while `AGENTS.md` forbids it
- no automatic Flow credit spend
- no automatic paid generation
- no automatic YouTube publish
- no exact competitor copying
- no third-person/full-cat regression
- no paid G1 before full planned KF chain PASS
- no independent fresh-generation KF1+ when prior approved KF can anchor continuity
- no planned KF substituted for previous actual PASS frame
- no defined-but-wrong ordered KF destination
- no unused decorative KF in all-First+Last manifests
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

Success is measured by first-pass success, usable motion/credit, engaged views/credit, subscribers/credit, fewer continuity/camera rerolls, less operator judgment and fewer repeated story fingerprints — not commit count.

## Change log

### 2026-08-28 — planned keyframe scene-order fail-closed gate
Baseline `main@2f637bd740d5e38c80dab99b304325b308741939`.

Changed:
- reject defined-but-wrong planned KF destinations
- enforce exactly opening KF + one ordered target per First+Last scene
- enforce G1 starts at first ordered KF
- add focused TK-005 regression tests
- synchronize this handoff

Verified assumptions:
- TK-005 already follows `KF0_OPEN → KF1_WARM → KF2_CRACK → KF3_OPEN → KF4_SERVE`
- official Flow pricing/features remain unchanged on 2026-08-28
- current Japanese autumn evidence does not justify ranking/NEXT_EPISODE changes

Unchanged:
- NEXT_EPISODE = TK-005
- immersive_h40 / four Lite scenes / current 40-credit first-pass ceiling
- candidate ranking
- no Flow credits spent
- no paid generation or publishing

### Earlier 2026-08-28 work
- START_HERE synchronized with full planned KF chain
- development executor policy synchronized with AGENTS.md
- CURRENT_STANDARD planned-keyframe synchronization
- planned keyframe continuity chain
- no-charge keyframe cost preflight
- Flow native Save frame bridge
- TK-005 fixed warmer/niche continuity
- zero-cut prompt preservation
- scene-action/keyframe/spend integrity gates
- runtime-aware operator guidance
- IDEA-010 new-rice onigiri candidate
- deterministic novelty/authenticity gate
