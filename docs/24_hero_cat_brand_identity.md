# 24 — Hero Cat Brand Identity

목표: Tiny Cat Kitchen의 고양이와 주방을 매 영상에서 다시 해석하지 않고, 채널 프로필·배너·Shorts가 하나의 세계로 보이게 한다.

## HERO_CAT_V1 — 고정 주인공

현재 채널의 기본 hero cat은 다음 외형을 유지한다.

- 한 마리만 등장
- cream fur base
- soft pale ginger/orange markings on forehead, ears and upper face
- round amber/dark eyes with clear catchlights
- small pink nose
- soft round face, calm curious expression
- beige/light-linen apron
- 실제 고양이 발 구조: human fingers/thumbs 금지
- 과도하게 아기 고양이처럼 만들거나 매 영상마다 품종/얼굴 비율을 바꾸지 않음

짧은 reference phrase:

```text
HERO_CAT_V1: one cream-and-pale-ginger cat, round amber eyes, pink nose, soft round face, beige linen apron, real feline paws, no human fingers or thumbs
```

## KITCHEN_WORLD_V1 — 고정 세계

- cozy miniature Japanese-inspired wooden kitchen
- warm honey/cream palette
- soft natural window light
- rounded window / warm plaster or wood wall
- small ceramic cookware and wooden utensils
- uncluttered counter
- subtle plant/seasonal accent 허용
- calm premium healing mood

계절 에피소드에서 장식은 바꿀 수 있지만 구조적 identity는 유지한다.

## Continuity priority

Flow 생성 전 무료 frame/reference 검수 순서:

1. HERO_CAT_V1 얼굴/털색/눈/코
2. beige linen apron
3. feline paw anatomy
4. KITCHEN_WORLD_V1 lighting/material language
5. cookware/food scale
6. episode-specific food/action

음식이 예쁘지만 cat identity가 다르면 FAIL이다. 작은 음식 디테일보다 채널 캐릭터 연속성을 우선한다.

## Prompt rule

각 새 episode의 first generation 또는 새로운 독립 keyframe에는 HERO_CAT_V1과 KITCHEN_WORLD_V1을 명시한다. G2/G3는 직전 실제 usable frame을 First frame으로 넘겨 identity를 이어간다.

프롬프트를 길게 늘여 동일성을 강제하지 않는다. 핵심 외형 토큰 + 실제 reference frame + sequential frame chain을 함께 사용한다.

## Channel asset rule

프로필·배너·Shorts에서 같은 hero cat을 사용한다. 프로필/배너는 채널 identity reference이며, 이후 다른 털색이나 다른 apron의 고양이를 새 기본 캐릭터로 승격하지 않는다. 의도적으로 다른 캐릭터를 추가하려면 별도의 versioned identity와 세계관 이유가 필요하다.

## Versioning

현재 기본 버전: `HERO_CAT_V1` / `KITCHEN_WORLD_V1`.

실제 Flow에서 반복적으로 재현이 어려운 특징이 발견되면 외형을 임의 변경하지 말고 production data를 근거로 v2를 제안한다.
