# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-29 Quality-first + Operator-Card-First Fast Loop + Mini Forest Paw-Only Making + Adaptive H40 Progressive Spend**

## 0. 우선순위 / 문서 거버넌스

장기 목적은 `PRODUCT_CHARTER.md`, 현재 상태는 `PROJECT_HANDOFF.md`, 이 문서는 실제 실행 규칙이다.

우선순위:
1. 영상/내용 퀄리티
2. 시청성과/채널 정체성
3. 제작 편의성·속도
4. paid-video reroll/credit 효율
5. 무료 이미지 비용 가드

Nano Banana는 사용자의 현재 Google 환경에서 무료로 사용할 수 있다. 기존 model/UI cost 확인은 안전망으로만 유지하고, 실제 문제가 다시 생기지 않는 한 비용 가드 자체를 개발의 중심으로 삼지 않는다. Paid Veo generation/publishing은 항상 사용자 명시 행동이 필요하다.

## 1. 핵심 영상 경험

> **Mini Forest처럼 실제로 아주 작은 음식/물건을 만드는 미니어처 힐링 영상에서 사람 손 자리만 자연스러운 고양이 앞발이 대신한다.**

필수:
- cream/pale-ginger front paws 1~2
- face/head/body/full cat 금지
- human hands/fingers/thumbs 및 human-like paw grip 금지
- hero object 보통 5~20mm, <=0.50 paw width
- realistic handcrafted miniature workbench
- process-first tactile making
- calm long take / macro intimacy / close ASMR

카메라 우선순위: high-oblique maker view → top-down macro → side/tabletop macro → 필요할 때만 first-person-like. Literal first-person은 필수가 아니다. Legacy `POV_PAWS_MICROWORLD_V1`은 compatibility token이다.

## 2. Content Quality Gate

Paid video 전에 episode는 다음을 명확히 해야 한다.
1. **HOOK** — 첫 1~2초에 `tiny + cat paws + making`이 즉시 읽히는가?
2. **TRANSFORMATION** — 각 scene에서 무엇이 실제로 어떻게 변하는가?
3. **SCALE PROOF** — paw/object 대비가 가장 강한 shot은 무엇인가?
4. **PAYOFF** — 마지막까지 볼 이유가 되는 완성/steam/crack/gloss/serving 결과가 있는가?
5. **NOVELTY/JAPAN FIT** — 왜 지금 일본 타깃에 맞고 기존/경쟁 episode와 무엇이 다른가?

하나라도 약하면 runtime이나 scene을 늘리지 말고 premise/shot/action을 먼저 개선한다.

## 3. Candidate / manifest fail-closed identity gate

Candidate selector와 canonical manifest validator는 계속 다음을 막는다.
- hero scale >0.50 paw width
- human-dexterity actions
- full-cat/character-performance drift
- paid scene에 active action 0개 또는 2개 이상

Safe action family: `nudge / press / pat / roll / steady / slide / tap / push`.

Canonical production validation entry: `tools/validate_maker_view_manifest.py`.

### Adaptive H40 semantic gate

`immersive_h40`는 **4회 generation을 반드시 쓰는 모드가 아니라 최대 4회의 first-pass ceiling**이다.

Current manifest semantics:
- `minimum_distinct_motion_beats: 3` = G1→G3가 이미 완결된 core Short여야 함
- `fourth_beat_optional_after_g3: true` = G4는 real G3를 본 뒤 재판단
- `fourth_beat_value` = optional G4가 실제로 추가할 독립적 resolution value
- manifest에는 optional G4 candidate를 미리 기술할 수 있지만, 존재 자체가 spend permission은 아님

Legacy structural validator가 과거 H40 plan shape를 위해 `minimum_distinct_motion_beats >=4`를 기대하는 부분은 maker-view adapter 내부에서만 compatibility translation한다. Current user-facing manifest에 mandatory-G4 semantics를 되살리지 않는다.

## 4. Operator-Card-First Fast Preparation Loop

정상 인터페이스:
```text
사용자: 다음 영상 준비해줘
로컬: ./tools/make_next_short.ps1
```

ChatGPT/repo가 준비해야 할 결과:
- 다음 소재와 선택 이유
- runtime tier
- HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF
- KF0→KFn exact-order prompts
- G1→G3/필요시 G4 exact-order Flow prompts
- invariant negative constraints/settings
- 각 단계의 `지금 할 것` 1개와 PASS/FAIL 기준
- manifest + `production/NEXT_EPISODE.txt` + material handoff sync

### Primary production surface

`production/${EPISODE_ID}_OPERATOR_CARD.md`가 존재하면 **그 파일이 사용자의 primary runbook**이다.

`./tools/make_next_short.ps1`과 `./tools/make_short.ps1`은 Operator Card를 가장 먼저 보여주고 사용자가 그 카드의 `NOW/current action`만 수행하도록 안내해야 한다.

Generated bundle/flow-pack은 기술 reference/fallback이다.

Operator UX 원칙:
- 한 번에 다음 행동 하나를 가장 명확하게 보여준다.
- 프롬프트는 copy/paste-ready.
- 같은 설정/negative prompt를 여러 곳에서 재조립시키지 않는다.
- 무료 visual preflight에 불필요한 confirmation을 늘리지 않는다.
- paid Veo generation 직전에는 user action을 유지한다.

Tooling KPI:
- time-to-first-valid-G1
- manual interventions / episode
- prompt corrections before G1
- rerolls / finished episode

## 5. Keyframe / visual continuity

Nano Banana/reference frame은 비용 절감보다 **좋은 KF0 anchor와 연속된 destination frame을 빠르게 만드는 품질 도구**로 사용한다.

기본 core path:
```text
KF0 strong maker-view anchor
→ paws / scale / camera / props / lighting QC
→ KF1을 승인 KF0에서 파생
→ KF2를 KF1에서 파생
→ core ending KF까지 순차 파생
→ core visual continuity PASS
→ G1 only
```

KF1+를 unrelated fresh lottery frame으로 만들지 않는다.

### Lazy optional-target rule

Adaptive H40에서 G4가 optional이면 **G4 target KF를 G1 전에 미리 만들지 않아도 된다.**

예: TK-005
```text
KF0→KF3 core PASS
→ G1→G3 progressive generation
→ real G3를 보고 core가 complete면 STOP
→ G4가 실제로 더 좋아질 때만 actual G3 PASS saved frame에서 KF4 파생
→ optional G4
```

이 규칙은 불필요한 pre-production 작업을 줄이고, 아직 존재하지 않는 real G3를 상상해서 fourth scene을 과설계하는 것을 막는다.

## 6. Flow / Veo paid baseline

Paid generation 직전 실제 Flow UI의 active model/mode/output count/displayed cost를 확인한다.

기본:
```text
Veo 3.1 Lite
9:16
8 seconds
output count = 1
```

Progressive Spend:
```text
core visual/keyframe chain PASS
→ G1 only
→ quality QC
→ actual last usable native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G1-G3 together review
→ complete면 STOP
→ optional G4 only if real G3 still benefits from independent payoff
```

구조적 FAIL 후 다음 paid scene 금지. Actual previous PASS native saved frame이 continuity bridge다.

- compact_h30: 3×8s raw, current non-Ultra ceiling 30 credits
- immersive_h40: **3 core scenes + optional fourth candidate**, current non-Ultra ceiling up to 40 credits

H30/H40는 first-pass paid-video ceiling이지 final runtime 약속이 아니다.

## 7. 8초 scene grammar

> **1 calm tactile primary action + optional 1 passive material payoff**

`paw_action_family`는 paid scene당 정확히 하나.

기본 timing 예:
```text
0–1.5s premise/scale readable; paw settles or begins gently
1.5–6s one clear tactile transformation
6–8s paw still; steam/crack/gloss/crumb/sizzle payoff continues
```

기본 `max_visual_cuts_per_8s_generation: 0`.

피함: pinch / precise twist / human tool grip / 여러 active gesture / rapid montage.

## 8. Paid output QC — 영상 가치 우선

1. 첫 프레임/초반에 premise와 scale이 즉시 읽히는가?
2. 실제 miniature making처럼 보이고 AI-cat 연기처럼 보이지 않는가?
3. paw anatomy/동작이 자연스러운가?
4. tactile transformation이 만족스럽고 명확한가?
5. 이전 clip과 scale/props/camera/lighting continuity가 유지되는가?
6. 8초가 지루하지 않으면서도 급하지 않은가?
7. payoff가 다음 scene 또는 완결을 기대하게 만드는가?

구조 FAIL: face/body/full cat, human hands, human-like grip, weak scale, maker-view collapse, major continuity drift.

## 9. Audio / finishing

기본: no narration, no generated music, quiet room tone + close ASMR.

Motion이 좋고 audio만 나쁘면 reroll 대신 후편집 교체. Eligible Flow UI에서 1080p upscale이 0 credits로 표시되면 continuity chain 완료 후 QC-PASS clip에만 적용할 수 있다. Upscaled/re-encoded export는 next-scene continuity bridge로 쓰지 않는다.

## 10. Research / episode choice

Primary benchmark: realistic miniature cooking/making, handcrafted tiny-food process, relaxing tactile ASMR. AI-cat channels은 paw/anatomy/reliability 보조 신호만 사용한다.

추출: hook mechanics, hand-centric composition, scale contrast, tactile transformation, pacing, seasonal timing, payoff.

복제 금지: exact title/plot/branded package/distinctive set/ending.

Evidence saturation 유지. 새 근거가 ranking/timing/content mechanic/production mechanic/actual learning을 바꾸지 않으면 기록을 늘리지 않는다.

## 11. 현재 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

`猫の前足で作る、12mmの焼きいも。`

- `immersive_h40`
- G1→G3 = complete core story
- G4 = optional after real G3 review only
- maximum 4 Lite scenes / current non-Ultra ceiling 40 video credits
- before G1, only KF0→KF3 core targets need PASS
- KF4 is deferred; if G4 is justified, derive KF4 from actual saved G3 PASS frame
- same tray / warmer / serving niche
- G1 `nudge`, G2 `press`, G3 `slide`, optional G4 `slide`
- no direct pinch/grab
- zero-cut long take
- primary runbook: `production/TK-005_OPERATOR_CARD.md`

현재 실제 첫 행동:
> **Operator Card의 NOW 섹션대로 KF0 하나를 만들고, scale hook과 miniature realism을 승인한다.**

## 12. Learning

기록:
- video credits / rerolls / G-stage first-pass
- maker-view/character/scale/anatomy/continuity failures
- failed action type / usable motion seconds / final runtime / audio replacement
- 24h/72h Stayed to watch / APV / engaged views / subscribers / comments
- preparation minutes / manual interventions / prompt corrections before G1 / time-to-first-valid-G1

장기 목표:
```text
higher content quality
+ higher engaged views / paid credit
+ higher subscribers / paid credit
+ lower preparation time and manual work
```
