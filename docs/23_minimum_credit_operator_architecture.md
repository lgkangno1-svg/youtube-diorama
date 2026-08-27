# 23 — Minimum-Credit Operator Architecture

목표: 사용자가 매번 주제, 대본, Flow 프롬프트, 편집 순서를 고민하지 않고 **한 문장 → 무료 planned-KF preflight → 필요한 generation만 순차 실행 → 실제 성과 학습**으로 끝내게 한다.

관련 source of truth:
- `PROJECT_HANDOFF.md` — 현재 진행상태/인수인계
- `CURRENT_STANDARD.md` — 최신 production 기준
- `docs/22_continuous_episode_learning_engine.md` — 연구/학습 루프
- `docs/24_hero_cat_brand_identity.md` — hero cat/world
- `docs/25_pov_paws_microworld_grammar.md` — POV/scale grammar
- `docs/26_flow_ui_mode_preflight.md` — 새 생성 vs edit UI
- `docs/29_planned_keyframe_continuity_chain.md` — planned KF continuity

## 사용자 인터페이스

사용자는 평소:

```text
다음 영상 준비해줘
```

라고만 말한다. ChatGPT가 research/history를 보고 novelty-safe episode, runtime, manifest, NEXT_EPISODE를 준비한다.

사용자는 로컬에서:

```powershell
./tools/make_next_short.ps1
```

을 실행한다.

## Gate A — 0-credit planned keyframe continuity

Paid Veo 전에 **manifest의 모든 planned KF를 같은 세계 안에서 먼저 연결해 검수**한다.

2026-08-28 공식 Flow 도움말 재확인 기준:
- `Nano Banana 2 Lite`는 no-charge 이미지 생성/편집 기본 옵션으로 안내된다.
- 하지만 실제 Flow UI의 active model + displayed cost가 최종 source of truth다.

운영 순서:

```text
Flow image generation
→ active image model + displayed cost 확인
→ no-charge일 때만 무료 preflight로 사용
→ KF0 master anchor 생성
→ POV / paws / scale / camera / fixed props / lighting QC
→ KF1은 승인된 KF0을 edit/refine 또는 reference/ingredient로 파생
→ KF2는 승인된 KF1에서 파생
→ KF3/KF4...도 바로 이전 승인 KF에서 순차 파생
→ manifest-required planned KF 전체 PASS
→ 그 뒤에만 paid G1
```

**KF1+를 독립 fresh text-to-image lottery로 만들지 않는다.**

보존 우선순위:
1. true first-person camera
2. paw fur/anatomy/count
3. hero-object-to-paw scale
4. workbench geometry
5. warmer/tray/niche 등 fixed props와 화면 위치
6. lighting/lens/DOF
7. 음식/물체 상태는 manifest가 요구한 부분만 변화

다음이면 `KEYFRAME DRIFT FAIL`로 paid G1을 중단한다.
- camera angle/height drift
- paw identity/anatomy drift
- hero scale drift
- fixed prop 등장/삭제/큰 이동
- workbench/lighting가 다른 세트처럼 보임

무료라고 해도 장식용 대안을 무한 생성하지 않는다. **manifest가 요구하는 KF만 필요한 만큼 만든다.**

## Paid Flow settings

생성 직전 실제 UI 확인:

```text
NEW VIDEO GENERATION
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

2026-08-28 공식 Google Flow 도움말 기준:
- Google AI Pro: 1,000 credits/month
- Veo 3.1 Lite 4/6/8s + Extend: non-Ultra 10 credits/generation
- First + Last frames: Lite 4/6/8s 지원
- 1080p upscale: Plus/Pro/Ultra 0 credits

기존 영상의 `수정 사항 설명` / Omni Flash video edit 화면을 G1/G2/G3/G4 생성 화면으로 착각하지 않는다.

## Progressive Spend

```text
planned KF chain PASS
→ G1 only
→ QC
→ PASS 시 Flow native Save frame으로 actual last usable frame 저장
→ G2 only after G1 PASS
→ QC + Save frame
→ G3 only after G2 PASS
→ G4 only if immersive_h40 + G3 PASS + independent world-resolution value
```

G2/G3/G4를 미리 생성하지 않는다.

### G1 — 누적 10 credits (현재 기준)

QC:
- POV
- paws only
- scale
- feline anatomy
- fixed-prop continuity
- one primary action
- 0/1-cut calm long-take behavior

구조적으로 틀리면 G2 금지.

### G2/G3 — 누적 20/30

이전 PASS clip의 **실제 마지막 usable frame**을 Flow native `Save frame`으로 저장해 다음 First frame으로 사용한다.

금지:
- browser screenshot
- 재인코딩 still
- prettier planned KF를 actual bridge로 대체

### G4 — 누적 40, 조건부

다음을 모두 만족할 때만:
- G3 PASS
- runtime mode = `immersive_h40`
- 독립적인 serving/world-resolution/afterglow beat가 실제로 남아 있음

금지:
- 길이 맞추기
- 이미 끝난 payoff 반복
- 남은 credits 소진

## Planned KF와 actual saved frame의 역할

```text
Planned KF chain
KF0 → edit/reference → KF1 → edit/reference → KF2 ...
```

목적: 미래 endpoint들이 같은 camera/paw/scale/world를 공유하도록 한다.

```text
Actual video frame chain
G1 PASS actual frame → Save frame → G2 First
G2 PASS actual frame → Save frame → G3 First
```

목적: paid scene 사이의 실제 영상 연속성을 잇는다.

- planned KF = destination / target state
- actual saved frame = continuity bridge

둘을 바꾸지 않는다.

## Runtime — H30/H40는 credit tier

`compact_h30`과 `immersive_h40`의 숫자는 **first-pass credit ceiling**을 뜻한다. 최종 초 길이 목표가 아니다.

### compact_h30
- 정확히 3 × 8s Lite scenes = raw 24s
- 현재 30-credit first-pass ceiling
- 기본 final 약 **24~27s**
- scale reveal → making → payoff 3 beat로 완결될 때

### immersive_h40
- 정확히 4 × 8s Lite scenes = raw 32s
- 현재 40-credit first-pass ceiling
- 기본 final 약 **32~35s**
- G4가 독립적인 world-resolution 가치를 가질 때만

자연스러운 slowdown은 manifest의 허용 범위 안에서만 사용한다. 정적/keyframe hold는 `editorial_seconds`에 명시된 경우에만 사용한다. `max_total_static_hold_seconds`는 자동 패딩 예산이 아니다.

현재 validator는 generated motion + 허용 slowdown + **명시된** hold로 도달할 수 없는 target을 paid generation 전에 FAIL 처리한다.

48~60s는 실제 채널 retention/engaged-views-per-credit가 지지하기 전에는 기본값이 아니다. 필요하면 더 많은 독립 motion beat/generation 전략으로 별도 설계한다.

## Paw-action grammar

선호:
- nudge
- press
- pat
- roll
- steady
- slide
- tap

피함:
- tongs/chopsticks/knife를 fingers처럼 grip
- human pinch
- wrist twist

도구가 꼭 필요하면 넓은 면을 paw pad로 눌러 이동하게 재설계한다.

## 8초 generation 문법

> **1 calm tactile primary action + optional 1 passive micro-payoff**

```text
0~1.5s  paw approaches tiny object
1.5~6s  one press / roll / slide / nudge action
6~8s    paw stops; steam/crack/gloss/crumb continues
```

Production manifest는 반드시:
- `max_visual_cuts_per_8s_generation: 0` 또는 `1`
- `preferred_action_count_per_generation: 1`

을 명시해야 하며, 기본 Tiny Cat Kitchen 스타일은 0컷 long take다.

## Audio

기본:
- no narration
- no generated music
- quiet close ASMR

영상 motion이 좋고 audio만 나쁘면 영상 reroll보다 후편집 SFX 교체를 우선한다.

## 결과를 보여줄 때

```text
G1 만들었어. 봐줘
```

ChatGPT 판정:
- `PASS`
- `EDITABLE`
- `REROLL`
- `STOP`

shorthand:
- `POV FAIL`
- `SCALE FAIL`
- `ANATOMY FAIL`
- `CAMERA FAIL`
- `KEYFRAME DRIFT FAIL`
- `FRAME CHAIN FAIL`
- `PADDING FAIL`

## 학습

실제 데이터만 기록한다.

제작:
- actual credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy/continuity failures
- failed action type
- usable motion seconds
- final runtime
- audio replacement

콘텐츠:
- Stayed to watch
- APV
- engaged views
- subscribers
- comments
- 가능하면 beat drop-off

장기 KPI:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

핵심 원칙: **무료 단계에서 해결 가능한 continuity 문제와 편집 단계에서 해결 불가능한 runtime 산술 오류를 paid Veo reroll로 넘기지 않는다.**
