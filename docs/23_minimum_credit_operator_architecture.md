# 23 — Minimum-Credit Operator Architecture

목표: 사용자가 매번 주제/대본/Flow 프롬프트/편집 순서를 고민하지 않고 **한 문장 → free planned-KF preflight → 필요한 generation만 순차 실행 → PASS clip 화질 개선 → 실제 성과 학습**으로 끝내게 한다.

## 사용자 인터페이스

```text
다음 영상 준비해줘
```

로컬:
```powershell
./tools/make_next_short.ps1
```

## Visual production intent

> **Mini Forest-style miniature making shot + human hands replaced by feline front paws only.**

- high-oblique maker view 기본
- top-down / tabletop macro / side-oblique macro 허용
- true first-person cat POV는 더 이상 필수 아님
- face/head/body/full cat 금지
- human hands/fingers/thumbs 금지
- hero object 보통 5~20mm, <=0.50 paw width
- process-first / calm tactile realism

기존 machine enum `POV_PAWS_MICROWORLD_V1`은 현재 tooling compatibility를 위해 유지한다.

## Gate A — planned keyframe continuity

Paid Veo 전에 manifest의 planned KF를 같은 세계 안에서 먼저 연결한다.

```text
Flow image model + displayed cost 확인
→ KF0 maker-view master anchor
→ paw anatomy / scale / camera / props / lighting QC
→ KF1은 KF0에서 edit/refine/reference
→ KF2는 KF1에서 파생
→ ...
→ all planned KFs PASS
→ G1 only
```

KF1+를 fresh independent text-to-image lottery로 만들지 않는다.

보존 우선순위:
1. paw fur/anatomy/count
2. maker-view camera
3. hero scale
4. workbench geometry
5. fixed props
6. lighting/lens/DOF
7. intended material state only

## Paid Flow settings

생성 직전 actual UI 확인:
```text
NEW VIDEO GENERATION
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

기존 영상 edit/Omni Flash 상태면 새 generation 화면으로 돌아간다.

## Current Flow credit eligibility note — 2026-08-29

Google Flow 공식 도움말 기준:
- 비구독 계정은 50 Flow credits/day를 무료로 받으며 Veo 3.1 Lite/Fast/Quality generation에 사용할 수 있다.
- 무료 daily credits는 유료 Plus/Pro/Ultra 계정에 추가로 stack되지 않는다.
- Veo 3.1 Lite는 non-Ultra 10 credits/generation, Ultra 5 credits/generation이다.
- **1080p upscale은 Plus/Pro/Ultra에서 현재 0 credits이며, 비구독 계정에는 제공되지 않는다.**

운영 원칙:
- TK-005 같은 `immersive_h40`은 non-Ultra 기준 first pass 40 credits가 그대로다.
- 무료 tier를 쓰더라도 여러 output/reroll을 미리 생성하지 않는다.
- 실제 subscription state와 Flow UI displayed cost가 언제나 최종 truth다.

## Progressive Spend

```text
planned KF chain PASS
→ G1 only
→ QC
→ PASS: Flow native Save frame
→ G2 only after G1 PASS
→ G3 only after G2 PASS
→ G4 only if immersive_h40 + G3 PASS + independent world-resolution value
```

다음 scene First frame은 previous PASS clip의 actual native saved frame이다.

## PASS-only 1080p finishing step

공식 문서상 Plus/Pro/Ultra에서 1080p upscale이 0 credits이므로, quality-per-credit를 높이는 후단 단계로 사용한다.

규칙:
- QC-PASS clip만 대상으로 한다.
- 가능하면 전체 continuity chain이 끝난 뒤 upscale한다.
- 다음 scene의 First frame은 upscaled/re-encoded export가 아니라 기존 QC-PASS clip의 native Save frame을 계속 사용한다.
- FAIL/reroll 예정 clip은 upscale하지 않는다.
- 실행 직전 UI가 실제로 0 credits를 표시할 때만 한다.
- upscale은 reroll이나 추가 generation을 정당화하지 않는다.

## QC priorities

- maker-view composition
- paws only
- tiny scale
- feline anatomy
- fixed-prop continuity
- one primary action
- 0/1-cut calm long-take behavior

구조적으로 틀리면 다음 spend 금지.

## Runtime

H30/H40는 first-pass credit tier.

### compact_h30
- 3 × 8s = raw 24s
- current first-pass ceiling 30 credits
- final 보통 24~27s

### immersive_h40
- 4 × 8s = raw 32s
- current first-pass ceiling 40 credits
- final 보통 32~35s
- G4는 독립적인 serving/world-resolution/afterglow beat일 때만

runtime padding 금지.

## Paw-action grammar

선호:
- nudge
- press
- pat
- roll
- steady
- slide
- tap
- push

피함:
- human pinch
- tongs/chopsticks/knife grip
- precise twist

Mini Forest의 사람 손동작을 그대로 복사하지 말고 feline-safe 동작으로 재설계한다.

## 8초 generation

> **1 calm tactile primary action + optional 1 passive material payoff**

Production manifest:
- `max_visual_cuts_per_8s_generation: 0` or `1`
- `preferred_action_count_per_generation: 1`

기본은 0-cut long take.

## Audio

- no narration
- no generated music
- quiet close miniature ASMR

좋은 motion + 나쁜 audio라면 video reroll보다 edit replacement.

## Learning

실제 값만 기록:
- credits/rerolls
- G1~G4 first-pass success
- maker-view/camera failure
- scale/anatomy/continuity failure
- failed action type
- usable motion seconds
- final runtime
- Stayed to watch / APV / engaged views / subscribers / comments

장기 KPI:
```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

핵심 원칙:

> **무료 단계에서 continuity 문제를 제거하고, paid Veo는 PASS-gated로 최소화하며, 이미 통과한 결과는 현재 무료인 1080p upscale을 활용해 generation 추가 없이 전달 화질을 높인다.**
