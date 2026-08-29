# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-29 Quality-first + Fast Operator Loop + Mini Forest Paw-Only Making + Progressive Paid Spend**

## 0. 문서 거버넌스 / 우선순위

장기 목적은 `PRODUCT_CHARTER.md`, 현재 상태는 `PROJECT_HANDOFF.md`, 이 문서는 실제 실행 규칙이다.

최신 사용자 지시에 따라 개선 우선순위는:
1. 영상/내용 퀄리티
2. 시청성과/채널 정체성
3. 제작 편의성·속도
4. paid-video reroll/credit 효율
5. 무료 이미지 비용 가드

사용자는 Google 사용 환경에서 Nano Banana 이미지를 무료로 사용할 수 있다고 명시했다. **Nano Banana 비용 가드 자체를 더 고도화하는 작업은 중단/후순위화한다.** 기존 fail-closed 안내는 안전망으로 유지하되, 실제 비용 문제가 다시 보고되지 않는 한 여기에 개발 시간을 쓰지 않는다.

Paid Veo generation/publishing은 여전히 사용자 명시 행동 없이는 금지한다.

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

카메라 우선순위: high-oblique maker view → top-down macro → side/tabletop macro → 필요할 때만 first-person-like. Literal first-person은 필수가 아니다.

## 2. Content Quality Gate — paid video 전에 먼저 해결

각 episode는 paid generation 전에 다음 5가지를 한 문장씩 명확히 해야 한다.

1. **HOOK** — 첫 1~2초에 무엇이 `tiny + cat paws + making`을 즉시 이해시키는가?
2. **TRANSFORMATION** — 각 scene에서 재료/물체 상태가 실제로 무엇에서 무엇으로 변하는가?
3. **SCALE PROOF** — paw와 hero object의 대비가 어느 shot에서 가장 강하게 보이는가?
4. **PAYOFF** — 마지막까지 볼 이유가 되는 완성/steam/crack/gloss/serving 결과는 무엇인가?
5. **NOVELTY/JAPAN FIT** — 왜 지금 일본 타깃에게 맞고, 기존/경쟁 episode와 무엇이 다른가?

이 중 하나라도 약하면 장면을 추가하지 말고 premise/shot/action을 먼저 개선한다.

Scene은 단순 움직임이 아니라 **보이는 상태 변화**를 만들어야 한다. G4는 길이 채우기가 아니라 독립 payoff/world-resolution 가치가 있을 때만 허용한다.

## 3. Candidate / manifest fail-closed identity gate

Candidate selector와 canonical manifest validator는 계속 다음을 막는다.
- hero scale >0.50 paw width
- human-dexterity actions
- full-cat/character-performance drift
- paid scene에 active action 0개 또는 2개 이상

Safe action family: `nudge / press / pat / roll / steady / slide / tap / push`.

Legacy `POV_PAWS_MICROWORLD_V1`은 compatibility token일 뿐 창작 방향이 아니다.

Canonical production validation entry: `tools/validate_maker_view_manifest.py`.

## 4. Fast Preparation Loop

목표는 사용자가 여러 문서를 읽거나 프롬프트를 조립하지 않게 하는 것이다.

사용자:
```text
다음 영상 준비해줘
```

ChatGPT/repo가 준비해야 할 결과:
- 다음 소재와 선택 이유
- runtime tier
- HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF
- KF0→KFn exact-order prompts
- G1→G3/필요시 G4 exact-order Flow prompts
- invariant negative constraints/settings를 매번 다시 고민하지 않도록 pack에 포함
- 각 단계의 `지금 할 것` 1개와 PASS/FAIL 기준
- manifest + `production/NEXT_EPISODE.txt` + material handoff sync

사용자 로컬:
```powershell
./tools/make_next_short.ps1
```

Operator UX 원칙:
- 한 번에 다음 행동 하나를 가장 명확하게 보여준다.
- 프롬프트는 copy/paste-ready여야 한다.
- 같은 설정/negative prompt를 사용자가 여러 곳에서 재조립하게 하지 않는다.
- 무료 planning/keyframe 단계에서 불필요한 confirmation을 늘리지 않는다.
- paid Veo generation 직전에는 명확한 user action을 유지한다.

앞으로 tooling 개선 KPI:
- time-to-first-valid-G1
- manual interventions / episode
- prompt corrections before G1
- rerolls / finished episode

## 5. Keyframe / visual continuity

Nano Banana keyframe/reference 작업은 품질·연속성 preflight로 적극 활용한다. 사용자가 무료로 사용할 수 있으므로 **비용 자체보다 좋은 KF0 anchor와 연속된 destination frames를 빠르게 만드는 데 집중**한다.

```text
KF0 strong maker-view anchor
→ paws / scale / camera / props / lighting QC
→ KF1을 승인 KF0에서 파생
→ KF2를 KF1에서 파생
→ 필요한 KFn까지
→ visual continuity PASS
→ G1 only
```

KF1+를 unrelated fresh lottery frame으로 만들지 않는다.

기존 image-cost safety check는 남겨두지만, 사용자의 무료 접근이 유지되는 한 반복적인 비용 확인/문서 작업이 제작 흐름을 지배하면 안 된다.

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
visual/keyframe chain PASS
→ G1 only
→ QC
→ actual last usable frame native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if manifest/runtime still justifies independent payoff
```

구조적 FAIL 후 다음 paid scene 금지. Actual previous PASS native saved frame이 continuity bridge다.

H30/H40는 first-pass paid-video tier이지 final runtime 약속이 아니다.
- compact_h30: 3×8s raw, current non-Ultra ceiling 30 credits
- immersive_h40: 4×8s raw, current non-Ultra ceiling 40 credits

## 7. 8초 scene grammar

> **1 calm tactile primary action + optional 1 passive material payoff**

`paw_action_family`는 paid scene당 정확히 하나.

좋은 예:
```text
0–1.5s  premise/scale immediately readable; paw settles
1.5–6s  one clear tactile transformation
6–8s    paw becomes still; steam/crack/gloss/crumb/sizzle payoff continues
```

기본 `max_visual_cuts_per_8s_generation: 0`.

피함: pinch / precise twist / human tool grip / 여러 active gesture / rapid montage.

## 8. QC 우선순위

Paid output QC는 단순 기술 PASS보다 **영상 가치**를 먼저 본다.

1. 첫 프레임/초반에 premise와 scale이 즉시 읽히는가?
2. 실제 miniature making처럼 보이는가, AI-cat 연기처럼 보이지 않는가?
3. paw anatomy/동작이 자연스러운가?
4. tactile transformation이 만족스럽고 명확한가?
5. 이전 clip과 scale/props/camera/lighting continuity가 유지되는가?
6. 8초가 지루하지 않으면서도 급하지 않은가?
7. payoff가 다음 scene 또는 완결을 기대하게 만드는가?

구조 FAIL: face/body/full cat, human hands, human-like grip, weak scale, maker-view collapse, major continuity drift.

## 9. Audio / finishing

기본: no narration, no generated music, quiet room tone + close ASMR.

Motion이 좋고 audio만 나쁘면 reroll 대신 후편집 교체.

Eligible Flow UI에서 1080p upscale이 0 credits로 표시되면 continuity chain 완료 후 QC-PASS clip에만 적용할 수 있다. Upscaled/re-encoded export는 next-scene continuity bridge로 사용하지 않는다.

## 10. Research / episode choice

Primary benchmark: realistic miniature cooking/making, handcrafted tiny-food process, relaxing tactile ASMR. AI-cat channels은 paw/anatomy/reliability 보조 신호만.

추출: hook mechanics, hand-centric composition, scale contrast, tactile transformation, pacing, seasonal timing, payoff. Exact title/plot/branded package/distinctive set/ending 복제 금지.

Evidence saturation 유지. 새 근거가 ranking/timing/content mechanic/production mechanic/actual learning을 바꾸지 않으면 기록을 늘리지 않는다.

## 11. 현재 제작 상태

`production/NEXT_EPISODE.txt` = **TK-005**

`猫の前足で作る、12mmの焼きいも。`

- `immersive_h40`
- up to 4 Lite scenes / current non-Ultra first-pass ceiling 40 video credits
- KF0→KF4 planned continuity
- same tray / warmer / serving niche
- scene actions: G1 `nudge`, G2 `press`, G3 `slide`, G4 `slide`
- no direct pinch/grab
- zero-cut long take

다음 실제 제작의 초점은 비용 가드가 아니라:
1. TK-005 HOOK/SCALE PROOF가 KF0에서 즉시 읽히게 만들기
2. KF0→KF4의 miniature realism/props/lighting continuity 높이기
3. 각 G scene의 tactile transformation과 payoff를 더 명확하게 하기
4. G1을 한 번에 PASS시킬 prompt/first-last-frame 품질 높이기
5. 실제 제작 시간/수정 횟수/reroll을 기록해 다음 episode를 더 빨리 만들기

## 12. Learning

기존 기록:
- video credits / rerolls / G-stage first-pass
- maker-view/character/scale/anatomy/continuity failures
- failed action type / usable motion seconds / final runtime / audio replacement
- 24h/72h Stayed to watch / APV / engaged views / subscribers / comments

추가 운영 학습:
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1

장기 목표:
```text
higher content quality
+ higher engaged views / paid credit
+ higher subscribers / paid credit
+ lower preparation time and manual work
```
