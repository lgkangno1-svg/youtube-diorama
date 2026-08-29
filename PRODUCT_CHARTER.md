# Tiny Cat Kitchen — PRODUCT CHARTER

Status: **Durable product intent / decision standard**
Owner intent refreshed: **2026-08-29 KST**

This is the durable decision charter for `lgkangno1-svg/youtube-diorama`.

Precedence:
1. newer explicit user instruction
2. latest merged `PROJECT_HANDOFF.md` / repository state
3. this charter for durable intent
4. `CURRENT_STANDARD.md` and specialized docs for implementation
5. legacy prompts/enums/notes

## 1. Product purpose

Tiny Cat Kitchen is a Japanese-target YouTube Shorts production system for **high-quality, calming, highly watchable miniature cooking/making videos where the visual role of human hands is naturally performed by a cat's front paws**.

Desired reaction:
> "This looks like a beautifully made real miniature process video, except tiny cat paws are making it. It is absurdly small, tactile, cute, satisfying and relaxing."

AI is an invisible production tool. The product is the miniature world, tactile process, scale contrast, paw interaction and viewing experience — not AI spectacle or cat roleplay.

## 2. User priority order — 2026-08-29 clarification

When trade-offs exist, optimize in this order:

1. **video quality and content quality** — concept, hook, miniature scale, tactile satisfaction, continuity, pacing, payoff, originality and Japanese audience fit
2. **viewer outcome** — retention/engaged views/subscriber conversion and repeatable channel identity
3. **production convenience and speed** — reduce clicks, prompt writing, remembering settings, file handling and avoidable waiting
4. **generation efficiency** — prevent rerolls and unnecessary paid video generations while preserving quality
5. **image-generation cost policing** only when it can actually affect the workflow

The user has explicitly stated that Nano Banana image generation is available to them for free through their Google usage. Therefore **do not spend future development cycles repeatedly hardening, documenting or researching Nano Banana cost gates unless the user reports that access/cost changed or the issue directly blocks production**.

This does not authorize paid video generation. Veo/Flow paid-video spend remains explicit-user-action only.

A technically elegant cost guard is not an improvement if it consumes development attention that would be better spent improving the actual Short or making production faster.

## 3. Core creative thesis

> **Mini Forest-like realistic miniature making, but replace the human hands with believable feline front paws.**

Preserve abstract mechanics only:
- handcrafted miniature realism
- extreme tiny-scale contrast
- process-first composition
- tactile transformation
- calm legible pacing
- macro/maker-view intimacy
- satisfying physical payoff
- close ASMR / healing mood

Never copy another creator's exact title, plot/sequence, branded package, distinctive set, signature composition or ending.

## 4. Non-negotiable visual identity

- one or two cream/pale-ginger feline front paws
- no cat face/head/torso/full body
- no human hand/fingers/thumb
- no human-like paw grip
- hero object normally 5–20mm and <=0.50 paw width
- realistic miniature workbench/diorama
- making process visually dominant
- default camera: high-oblique maker view; top-down or side/tabletop macro when better
- literal cat-eye first-person POV is not required

Legacy `POV` labels are compatibility tokens only and must never restore mandatory first-person framing.

## 5. Content-quality standard

Every episode should have a simple visual sentence that can be understood without narration:

```text
recognizable tiny subject
→ one or more satisfying material transformations
→ clear miniature-scale contrast with paws
→ visually rewarding finished/payoff state
```

Before production, prefer concepts with:
- an immediately legible first-frame premise
- a strong tactile action that Veo can render reliably
- visible state change, not merely movement
- a payoff worth staying for
- Japanese seasonal/cultural relevance when it genuinely strengthens demand
- enough originality to feel like Tiny Cat Kitchen rather than a copied trend

Do not add scenes just to increase runtime. Every G scene must earn its generation through a distinct visual transformation or resolution beat.

## 6. Motion / pacing / audio

Default paid 8-second scene:
> **one primary feline-safe tactile action + at most one passive material payoff**

Preferred active verbs: `nudge / press / pat / roll / steady / slide / tap / push`.

Default edit: calm long take, zero/few cuts, no rapid montage, no artificial runtime padding.

Default audio: no narration, no generated music, quiet room tone + isolated close ASMR. A short user-recorded Japanese line is optional only when it materially improves comprehension/voice/payoff. If motion is good and audio alone is poor, fix audio in post rather than rerolling valuable motion.

## 7. Production convenience and speed

The system should shift preparation work away from the user and into ChatGPT/repository tooling.

The ideal normal interaction remains:

```text
User: 다음 영상 준비해줘
```

ChatGPT/system should then do the planning work:
1. inspect latest repo/handoff/charter/standard and actual production history
2. research only enough fresh evidence to improve the decision
3. choose an original next episode and runtime tier
4. design the hook, tactile transformations, payoff and scene order
5. prepare the complete Flow-ready prompt/keyframe/scene pack
6. keep prompts in exact execution order and make each step copy/paste-ready
7. update manifest, `production/NEXT_EPISODE.txt` and material handoff state
8. leave the user with the minimum necessary actions and clear PASS/FAIL checkpoints

Operator-design target:
- one command to prepare the episode
- one obvious current step at a time
- no need for the user to reconstruct prompts from multiple docs
- no repeated manual entry of invariant negative prompts/settings
- no unnecessary confirmation for free planning/preflight work
- explicit confirmation/action remains required before paid Veo generation or publishing

When improving tooling, prefer reducing **time-to-first-valid-G1** and **manual interventions per finished Short**, not adding more warnings or documentation layers.

## 8. Production economics

The goal is not the cheapest possible video. Optimize the sustainable combination of quality, viewer response, production speed, learning speed and paid-video efficiency.

Primary outcome metrics:
- engaged views / credit
- subscribers / 100 credits
- usable motion seconds / credit

Add operational efficiency metrics when real data becomes available:
- preparation minutes / episode
- manual operator interventions / episode
- prompt corrections before G1
- time-to-first-valid-G1
- rerolls / finished episode

Do not optimize `credits/video` or `minutes/video` in isolation if quality or audience outcome degrades.

## 9. Paid-video spend and continuity

Paid Veo generation remains progressive:

```text
planned visual/keyframe continuity PASS
→ G1 only
→ QC
→ save actual last usable frame
→ G2 only after G1 PASS
→ repeat
```

G4 is not automatic; it must add independent world-resolution/serving/afterglow value.

Continuity is first-class. Preserve paw appearance/anatomy, hero scale, workbench geometry, fixed props, camera family, lighting and food/object state. Planned keyframes are destinations; actual previous PASS saved frames are continuity bridges.

Never spend paid Flow/Veo credits or publish without explicit user action.

## 10. Structural failures

Reject/redesign for:
- cat face/head/body/full-cat character framing
- cat acting a human job/role
- human hands/fingers/thumbs
- human-like feline tool grip
- weak tiny-scale contrast
- implausible paw anatomy
- uncontrolled prop/camera/world drift
- making process becoming secondary to character spectacle
- rapid AI montage destroying tactile readability

Observational/non-first-person maker view is not itself a failure.

## 11. Research and learning

Research Japanese/global miniature cooking, ASMR, relaxing food, AI-cat and adjacent Shorts to extract abstract success mechanics. Research is useful only when it changes a content, production or ranking decision; respect evidence saturation.

Record real episode evidence:
- Flow video credits/rerolls/G-stage first-pass success
- usable motion seconds
- failure class/action type
- final runtime/audio replacement
- 24h/72h Stayed to watch, APV, engaged views, subscribers, comments
- when practical: preparation time and number of manual interventions

Use repeated real evidence to improve concepts, hook structure, actions, runtime, prompts and workflow. Do not rewrite strategy after one noisy datapoint.

## 12. Decision test for future improvements

Before merging a material improvement ask:
1. Does it improve or protect actual video/content quality?
2. Does it strengthen Tiny Cat Kitchen's paws-only miniature identity and tiny-scale readability?
3. Does it improve the hook, tactile transformation, payoff, pacing or continuity?
4. Does it improve expected viewer outcome per paid credit?
5. Does it make the episode faster/easier for the user to produce?
6. Does it reduce rerolls or manual interventions without lowering quality?
7. Is it based on real learning or meaningful non-saturated evidence?
8. Does it avoid competitor-expression copying?
9. Does it preserve user control over paid video generation/publishing?
10. Is the documentation surface proportional to the actual value of the change?

If a proposed change mainly adds another cost warning/check for a resource the user already has free access to, and does not improve quality, speed or paid-video efficiency, **deprioritize it**.

## 13. Anti-goals

Do not drift toward:
- generic/full-cat/talking-cat roleplay
- spectacle-first AI transformations
- human-like paw dexterity
- maximizing runtime/scenes/research volume
- excessive process bureaucracy
- repeatedly polishing free-image cost guards
- maximizing automation at the expense of paid-spend control
- blindly minimizing credits/video
- copying competitor episodes
- repeatedly changing standards without production evidence

## 14. Definition of success

Near term:
- first seconds instantly communicate `cat paws + absurdly tiny real miniature making`
- coherent, beautiful episodes with low preventable reroll rate
- user can reach a valid G1 quickly without prompt engineering or repository administration

Medium term:
- identify reliable subjects/hooks/actions/payoffs/runtimes from real results
- reduce preparation time and manual interventions while increasing engaged views and subscriber conversion per paid credit
- establish recognizable recurring world continuity without cat-roleplay drift

Long term:
> **Build a distinctive, scalable Japanese-target healing Shorts channel whose signature is believable cat paws quietly making absurdly tiny things, with a production system that continuously improves content quality, viewer response and creation speed while controlling paid-video waste.**

## 15. Documentation maintenance

```text
PRODUCT_CHARTER.md  = durable why / product priorities / decision criteria
PROJECT_HANDOFF.md  = current state / learning / changes / next priorities
CURRENT_STANDARD.md = executable production/QC/operator rules
manifests + ledgers = episode plan + observed evidence
```

Update this charter only for durable intent/priorities. Every material repository change still synchronizes `PROJECT_HANDOFF.md`; executable rule changes also update `CURRENT_STANDARD.md`. True NO-OPs do not churn documentation.
