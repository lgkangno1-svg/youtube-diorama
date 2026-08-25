# 24 — Hero Cat Brand Identity

목표: Tiny Cat Kitchen의 고양이 identity는 유지하되, **채널 자산의 full-cat 표현과 Shorts의 first-person paw-only 표현을 분리**한다.

Shorts framing의 세부 source of truth는 `docs/25_pov_paws_microworld_grammar.md`다.

## HERO_CAT_V1 — 고정 주인공 identity

채널의 기본 hero cat 외형:

- cream fur base
- soft pale ginger/orange markings
- round amber/dark eyes with clear catchlights
- small pink nose
- soft round face
- beige/light-linen apron
- 실제 고양이 발 구조: human fingers/thumbs 금지

짧은 full-cat reference phrase:

```text
HERO_CAT_V1: one cream-and-pale-ginger cat, round amber eyes, pink nose, soft round face, beige linen apron, real feline paws, no human fingers or thumbs
```

## Channel assets vs Shorts

### 프로필 / 배너

- HERO_CAT_V1 얼굴/전신을 보여줄 수 있다.
- 현재 프로필/배너의 따뜻한 miniature Japanese kitchen identity를 유지한다.
- full-cat portrait는 **브랜드 자산용**이다.

### 기본 Shorts

- `POV_PAWS_MICROWORLD_V1`을 사용한다.
- camera = true first-person cat POV.
- 화면에는 cream + pale ginger **앞발 1~2개만** 보인다.
- 얼굴, 눈, 귀, 머리, 몸통, 꼬리, full body는 보이지 않는다.
- 앞치마도 화면에 억지로 노출시키지 않는다.
- 주인공은 고양이 얼굴이 아니라 **앞발과 비교되는 초소형 음식/물체**다.

Shorts용 짧은 paw reference phrase:

```text
HERO_CAT_V1_PAWS: one or two cream-and-pale-ginger real feline front paws only, entering from the bottom edge in true first-person cat POV; no face, head, torso, full body, human fingers, thumbs or human-like grip
```

## KITCHEN_WORLD_V1 — 고정 세계

- cozy miniature Japanese-inspired wooden workbench/kitchen
- warm honey/cream palette
- small ceramic cookware and wooden diorama props
- soft natural/window light
- uncluttered composition
- calm premium healing mood

중요: Shorts에서는 **주방 전체보다 작업대의 초소형 물체가 우선**이다. 넓은 주방 establishing shot 때문에 물체가 커 보이거나 scale contrast가 약해지면 FAIL이다.

## Continuity priority — Shorts

Flow 생성 전 무료 frame/reference 검수 순서:

1. true first-person cat POV
2. front paws only; face/head/body hidden
3. real feline paw anatomy
4. hero food/object가 앞발보다 명확하게 작음
5. miniature cookware/prop scale
6. KITCHEN_WORLD_V1 lighting/material language
7. episode-specific food/action

음식이 예뻐도 3인칭 full-cat chef shot이면 FAIL이다.

## Paw action rule

고양이 발은 사람 손처럼 도구를 `grip`하지 않는다.

선호:
- nudge
- press
- pat
- roll
- steady
- slide
- tap

피함:
- chopsticks/tongs/knife를 손가락처럼 잡기
- thumb/index-finger pinch
- human wrist twist

필요한 도구는 넓은 손잡이를 발바닥으로 눌러 움직이거나, 작은 그릇/판을 밀어 간접적으로 조작하는 동작을 우선한다.

## Prompt rule

각 새 episode의 G1/독립 keyframe에는 `HERO_CAT_V1_PAWS + POV_PAWS_MICROWORLD_V1 + KITCHEN_WORLD_V1` 의미를 명시한다.

G2/G3/G4는 직전 actual last usable frame을 First frame으로 넘겨 다음을 계승한다.
- paw fur pattern
- camera POV
- workbench position
- miniature scale
- food state
- light/material language

텍스트로 full-cat identity를 반복해 얼굴이 다시 생성되게 하지 않는다.

## Channel asset rule

프로필·배너는 같은 HERO_CAT_V1의 얼굴을 보여주는 branding reference다. Shorts에서 얼굴이 안 보이는 것은 identity 충돌이 아니라 **의도된 촬영 문법**이다.

## Versioning

현재:
- character identity: `HERO_CAT_V1`
- Shorts camera/scale grammar: `POV_PAWS_MICROWORLD_V1`
- world identity: `KITCHEN_WORLD_V1`

실제 Flow 결과에서 재현성이 낮은 특징이 반복되면 production data를 근거로 version을 올린다.
