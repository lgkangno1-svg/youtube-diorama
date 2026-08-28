# 24 — Hero Cat Brand Identity

목표: 고양이 identity는 유지하되 **Shorts에서는 고양이 캐릭터를 보여주지 않고 앞발만 작업 손처럼 사용**한다.

Shorts framing의 source of truth는 `docs/25_pov_paws_microworld_grammar.md`다.

## HERO_CAT_V1

브랜드 자산용 전체 외형:
- cream fur base
- soft pale ginger/orange markings
- round amber/dark eyes
- small pink nose
- soft round face
- beige/light-linen apron
- real feline paws, no human fingers/thumbs

프로필/배너에서는 얼굴/전신을 보여줄 수 있다.

## Shorts용 identity

Shorts에서 중요한 identity는 얼굴이 아니라 **같은 앞발의 털색/패턴/해부학적 일관성**이다.

```text
HERO_CAT_V1_PAWS: one or two cream-and-pale-ginger real feline front paws only; no face, head, torso, tail or full body; no human fingers, thumbs or human-like grip
```

### 최신 framing 원칙

- Mini Forest류 miniature cooking에서 사람 손이 들어오는 자리에 feline paws가 들어온다.
- true first-person cat-eye camera는 필수가 아니다.
- 기본은 high-oblique maker view.
- top-down / tabletop macro / side-oblique macro도 허용.
- cat face/head/body/full cat은 Shorts에서 보이지 않는다.
- 앞치마도 Shorts에 억지로 노출하지 않는다.
- 고양이 직업극/캐릭터 연기보다 **작은 것을 실제로 만드는 과정**이 주인공이다.

## KITCHEN_WORLD_V1

- cozy handcrafted miniature Japanese-inspired workbench/kitchen
- warm honey/cream palette
- tiny ceramic cookware and wooden diorama props
- soft natural/window light
- uncluttered composition
- calm premium healing mood
- real miniature craftsmanship over toy-like plastic appearance

넓은 주방 establishing shot보다 작업대의 작은 재료와 앞발 동작이 우선이다.

## Continuity priority — Shorts

1. front paws only; face/head/body hidden
2. real feline paw anatomy
3. Mini Forest-style maker-view composition
4. hero object clearly smaller than paw
5. same camera/workbench geometry
6. miniature cookware/prop continuity
7. lighting/material language
8. episode-specific food state

음식이 예뻐도 full-cat chef shot이면 FAIL이다.

## Paw action rule

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
- chopsticks/tongs/knife human grip
- thumb/index pinch
- human wrist twist

사람 손이 하던 복잡한 조작은 고양이 발에 그대로 복제하지 말고 feline-safe push/press/slide 동작으로 바꾼다.

## Prompt rule

각 독립 keyframe/G1에는 다음 의미를 유지한다.

```text
realistic miniature cooking maker-view; only HERO_CAT_V1 front paws replace human hands; no face/head/body/full cat; absurdly tiny food/object; handcrafted miniature set; calm tactile realism
```

G2/G3/G4는 previous PASS clip의 actual saved frame으로 다음을 계승한다.
- paw fur pattern
- camera position
- workbench
- miniature scale
- food state
- light/material language

## Versioning

현재 machine-compatible labels:
- character identity: `HERO_CAT_V1`
- Shorts legacy enum: `POV_PAWS_MICROWORLD_V1`
- semantic visual intent: `mini_forest_style_paws_only_miniature_making`
- world identity: `KITCHEN_WORLD_V1`

legacy enum 이름에 `POV`가 남아 있어도 **true first-person을 다시 강제하지 않는다.** 실제 production semantics는 CURRENT_STANDARD와 docs/25가 우선한다.
