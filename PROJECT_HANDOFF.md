# Tiny Cat Kitchen — PROJECT HANDOFF

Last update: **2026-08-28 KST**  
Baseline inspected before this change: `main@616d6b75db6efb3bfdcaee4b57591aa1327acd1b`

This is the durable handoff source of truth for `lgkangno1-svg/youtube-diorama`. Another AI/developer must be able to continue from GitHub without prior chat history. Every material repository change must update this file in the same branch/PR. True NO-OP research should not churn it.

## Development execution policy

`AGENTS.md` is authoritative for repository-development execution.

Current policy:
- repository development is performed directly by the active Chat/Codex development session
- do **not** delegate coding, planning, debugging, refactoring, review, architecture, repository exploration, test repair, or unattended development loops to OpenCode Go
- `.opencode/opencode.json` intentionally contains no `opencode-go/*` development routing
- stale chat/automation/model-routing wording never overrides latest merged `AGENTS.md`

## Mission

Build a Japanese-target Shorts operating system, not merely an AI-cat generator.

Normal user interface:

```text
다음 영상 준비해줘
```

System responsibility:
- research current Japanese/global AI-cat, miniature, ASMR, relaxing-food and adjacent signals
- identify timely but novelty-safe episode candidates
- maintain episode manifest and `production/NEXT_EPISODE.txt`
- prepare deterministic local Flow/edit/publish packs
- minimize paid-generation failure with free/no-charge preflight where currently supported
- learn from real production and 24h/72h YouTube results

User local entrypoint:

```powershell
./tools/make_next_short.ps1
```

Never spend Flow credits, generate paid video, or publish to YouTube without explicit user action.

## Viewer-facing identity

Default visual grammar: `POV_PAWS_MICROWORLD_V1`.

- true first-person cat POV
- only cream + pale-ginger feline front paws near the lower edge
- no face/head/body/full-cat reveal
- hero object normally 5–20mm and <=0.50 of one visible paw width
- macro miniature diorama workbench
- mostly locked camera
- one calm tactile primary action + at most one passive micro-payoff per 8s generation
- preferred paw actions: nudge, press, pat, roll, steady, slide, tap
- no human fingers/thumbs/human-like tool grip
- no rapid montage or third-person chef framing

Core appeal: the viewer should feel like the cat handling an impossibly tiny world. Scale contrast and tactile calm matter more than showing a cat face.

Canonical identity docs:
- `CURRENT_STANDARD.md`
- `docs/24_hero_cat_brand_identity.md`
- `docs/25_pov_paws_microworld_grammar.md`

## Flow / Veo baseline

Official Google Flow Help rechecked **2026-08-28**:
- Google AI Pro: 1,000 Flow credits/month
- Veo 3.1 Lite 4s/6s/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames remain supported for Lite modes covered by current official model docs
- output count = 1
- 1080p upscaling = 0 credits for Plus/Pro/Ultra
- actual Flow UI active model/mode/output count/displayed cost remains generation-time source of truth

Current official credit table also lists Omni Flash at higher costs than Veo Lite, so do not confuse existing-video Omni Flash edit mode with standard new-video generation.

Canonical operator docs:
- `docs/23_minimum_credit_operator_architecture.md`
- `docs/26_flow_ui_mode_preflight.md`
- `docs/29_planned_keyframe_continuity_chain.md`

## Gate A — planned keyframe continuity

**This is mandatory before paid G1.**

```text
Flow image generation/editing
→ check active image model + displayed cost
→ use a no-charge path only when the UI confirms it
→ create KF0 master visual anchor
→ QC POV / paws / scale / camera / fixed props / lighting
→ derive KF1 from approved KF0 using edit/refine/reference
→ derive KF2 from approved KF1
→ continue sequentially through all manifest-required planned KFs
→ all planned KFs PASS
→ only then generate G1
```

Hard rule: KF1+ must not be independent fresh text-to-image lottery tickets when the previous approved KF can anchor continuity.

Preserve across planned KF chain:
- paw fur/anatomy
- first-person camera/lens
- hero-object scale
- workbench geometry
- fixed props
- lighting/material language

Only intended food/material state should change.

QC shorthand: `KEYFRAME DRIFT FAIL`.

Important distinction:
- planned KF = scene destination / target state
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

Never substitute a prettier planned target KF for the actual previous PASS frame in the paid-scene chain.

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

- latest-main / recent-PR / `AGENTS.md` / handoff-first work-start order
- direct Chat/Codex repository-development policy
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

## Latest fix — START_HERE planned-keyframe execution order

Problem found on **2026-08-28** after re-reading latest main:
- `CURRENT_STANDARD.md`, `docs/29_planned_keyframe_continuity_chain.md`, generated Flow Pack logic, and this handoff already required `KF0 → KF1 → ... → final KF` continuity PASS before paid G1.
- `START_HERE.md` still contained older wording equivalent to `FREE OPEN FRAME → G1` and its simplest user workflow jumped directly from local pack creation to G1.
- Because `START_HERE.md` is an operator-facing source of truth, this could cause the user or a new AI to skip KF1+ continuity preflight even though the deeper standard was correct.

Fix:
- make `AGENTS.md` explicit in the work-start order
- replace old one-frame Gate A wording with the full planned KF0→KFn chain
- require later KFs to derive from the previous approved KF
- explicitly separate planned target KFs from actual `Save frame` continuity bridges
- update the simplest real-use sequence so paid G1 happens only after the entire planned KF chain PASSes
- add `KEYFRAME DRIFT FAIL` / `FRAME CHAIN FAIL` to the operator shorthand

Expected effect: fewer accidental paid generations against incompatible endpoints and less operator ambiguity, with no extra paid video credits.

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

2026-08-28 research check:
- additional Japanese sweet-potato and Tsukimi retail launches remain same-class evidence already saturated in the repository
- they do not change candidate rank, publish timing, evidence class, production mechanics, or NEXT_EPISODE
- therefore research/backlog files are intentionally unchanged this run

Current candidate state:
- `IDEA-009` yakiimo → realized as TK-005; blocked as future repeat
- `IDEA-001` 8mm 月見だんご → priority future candidate
- `IDEA-010` 8mm 新米塩むすび → future candidate backed by current reservation/arrival behavior
- `IDEA-002` gummy → blocked against a recent equivalent conflict/ending structure

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
2. create/approve KF0 master anchor using a UI-confirmed no-charge image path
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
7. then re-weight runtime/action/idea priors

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

Stale chat or automation wording never overrides newer merged repository state.

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

### 2026-08-28 — START_HERE synchronized with planned KF chain
Baseline `main@616d6b75db6efb3bfdcaee4b57591aa1327acd1b`.

Changed:
- fixed stale Gate A wording that could skip planned KF1+
- made KF0→KFn derivation/QC mandatory before paid G1 in the top-level operator guide
- distinguished planned target frames from actual native Save-frame continuity bridges
- synchronized simplest real-use flow and failure shorthand
- synchronized this handoff

Verified:
- `CURRENT_STANDARD.md` already had the correct planned-keyframe order
- official Flow credit table remains Veo 3.1 Lite 4/6/8s + Extend = 10 credits/generation for non-Ultra as checked 2026-08-28
- same-class Japanese autumn retail news is saturated and does not justify research/backlog churn

Unchanged:
- NEXT_EPISODE = TK-005
- immersive_h40 / four Lite scenes / current 40-credit first-pass ceiling
- candidate ranking
- no Flow credits spent
- no paid generation or publishing

### Earlier 2026-08-27 work
- development executor policy synchronization
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
