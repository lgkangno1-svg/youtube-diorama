# Flow Credit Packing Lab — 한 생성에서 최대 컷 회수하기

작성 기준: 2026-08-24
상태: **LAB / 실전 검증 전**
목표: Google Flow / Veo 3.1 Lite의 `generation당 과금` 구조를 이용해 1회 생성에서 여러 usable shot을 회수한다.

## 공식 비용 전제

- Veo 3.1 Lite 4s / 6s / 8s = 동일하게 10 credits (non-Ultra), 5 credits (Ultra)
- 비용은 request당이 아니라 **generation당**
- 한 요청에서 output을 여러 개 만들면 각각 generation으로 과금될 수 있으므로 `output_count = 1` 유지
- Lite는 First + Last frame 4/6/8초 지원
- Google의 Veo 3.1 공식 prompt guide는 **Timestamp prompting으로 한 generation 안에 여러 shot을 배치하는 workflow**를 공식 예시로 제시
- Scenebuilder의 trim/reorder 자체는 새 video generation이 아니다

핵심:

> 4초와 8초 가격이 같으므로 경제성 기준 기본 길이는 8초다. 8초 안을 비워두지 말고 여러 편집 가능한 shot으로 채운다.

---

# 전략 A — Timestamp Multi-shot Packing (권장 1순위)

하나의 8초 9:16 full-frame generation 안에 4개의 2초 shot을 만든다.

예:

```text
[00:00-00:02] Extreme macro. Cat paw taps the pearl-sized egg cup beside the tiny pan. Static camera.
[00:02-00:04] Overhead macro. Exactly ten rice grains slide into the tiny pan. Hard cut.
[00:04-00:06] Side macro. One ketchup drop hits the rice and sizzles. Hard cut.
[00:06-00:08] Extreme macro. The thin omelet edge almost tears. Hold the danger at the end.

No dialogue. No music. Minimal neutral room tone only. Keep the same cat fur, pan, kitchen and food scale. Each timestamp is a distinct editorial shot; use clean hard cuts, no morphing transitions.
```

Google 공식 prompt guide가 timestamp multi-shot sequence를 한 generation 안에서 사용하는 예시를 제공하므로, collage보다 먼저 테스트한다.

## 장점

- 한 generation = 최대 4 full-resolution shot 후보
- 9:16 해상도를 전부 사용
- 같은 세계/캐릭터를 한 generation 안에 유지하기 쉬움
- 10 credits로 4 shot이면 nominal 2.5 credits/shot
- 생성 audio를 버리면 편집 순서를 자유롭게 바꿀 수 있음

## 위험

- 복잡한 action을 2초 안에 끝내려 하면 실패율 증가
- 모델이 hard cut 대신 연속 camera move로 해석할 수 있음
- 너무 많은 서로 다른 장소/캐릭터를 넣으면 continuity가 무너짐

## 규칙

- 1 generation당 장소 1개
- 주인공 1개체
- cookware/food state change는 단순하게
- 2초 shot 하나에 핵심 action 1개
- 대사/음악 생성 금지
- 복잡한 카메라 무브보다 static / macro / overhead / side angle 위주

---

# 전략 B — 20-credit Dual Timestamp Pack (가장 공격적인 full-frame 방식)

TK-001 같은 35~40초 Short를 다음처럼 실험한다.

## Generation A — 8초 / 10 credits

4 shots:
1. OPEN
2. CONSTRAINT
3. PROGRESS
4. DANGER

## Generation B — 8초 / 10 credits

4 shots:
1. RECOVERY
2. ASSEMBLY
3. PAYOFF
4. RESOLUTION

총:

```text
2 Lite generations = 20 credits
8 full-frame micro-shots
+ 무료 keyframe 5장
+ editor zoom/freeze/punch-in/replay
= 약 28~38초 final Short 목표
```

35~45초를 반드시 채우려고 AI footage를 늘이지 않는다. Shorts는 필요한 만큼 짧게 편집하고, 20-credit 영상의 retention이 40-credit 영상과 비슷하면 20-credit 방식이 승자다.

## First+Last + Timestamp 결합 실험

Flow UI에서 First+Last frame을 넣고 그 사이 prompt에 timestamps를 사용해볼 가치가 있다.

예:

```text
First frame = KF0_OPEN
Last frame = KF2_DANGER

[00:00-00:02] opening action...
[00:02-00:04] constraint reveal...
[00:04-00:06] cooking progress...
[00:06-00:08] arrive exactly at the supplied danger last frame.
```

중요: Google은 First+Last와 Timestamp를 각각 공식 workflow로 설명하지만 **두 기능의 결합 품질을 보장하는 공식 문구는 확인하지 못했다.** 따라서 LAB 테스트 후 승격한다.

---

# 전략 C — 30-credit Hybrid (현재 가장 현실적인 승격 후보)

20-credit 방식에서 Hero/Resolution 품질이 약할 경우:

```text
Generation A: timestamp 4 shots = 10
Generation B: timestamp 4 shots = 10
Generation C: dedicated full-frame Hero + Resolution = 10
Total = 30 credits
```

이 구조가 40-credit 4-frame-lock 방식보다 25% 저렴하면서도, 가장 중요한 음식 Hero와 결말은 별도 full-frame source를 확보한다.

권장 사용:
- 첫 파일럿
- 음식 질감이 중요한 episode
- character resolution이 중요할 때

---

# 전략 D — 2×2 Quad Video Packing (공격적 B-roll 압축 실험)

9:16 master를 정확히 2×2로 분할하면 각 quadrant도 9:16이다.

예:

```text
1080×1920 master
→ 540×960 top-left
→ 540×960 top-right
→ 540×960 bottom-left
→ 540×960 bottom-right
```

따라서 8초짜리 한 generation에서 4개의 독립적인 세로 micro-action을 동시에 움직이게 한 뒤, export 후 4등분해서 최대 4개의 8초 B-roll source로 회수할 수 있다.

이론상:

```text
1 generation = 8 actual seconds
4 quadrant crops = 최대 32 quadrant-seconds source
10 credits / 32 source-seconds = 0.3125 credits per source-second
```

일반 full-frame은:

```text
10 credits / 8 source-seconds = 1.25 credits per source-second
```

즉 **성공할 경우 source-second 기준 약 4배 압축**이다.

## Quad Prompt 기본형

```text
A locked 2x2 split-screen contact grid with four equal portrait 9:16 panels, clear fixed borders, no object may cross panel boundaries, no camera movement, each panel is an independent miniature Japanese kitchen micro-shot using the same orange tabby cat paws and same miniature cookware.

TOP LEFT: cat paw gently taps a tiny egg cup.
TOP RIGHT: one ketchup drop lands on ten rice grains.
BOTTOM LEFT: a tiny wooden spatula stirs the rice once.
BOTTOM RIGHT: cat paw taps a parsley leaf beside the finished dish.

All four panels remain spatially locked for the full 8 seconds. No panel transitions. No zoom. No text. No dialogue. No music. Minimal neutral room tone only; generated audio will be discarded in post.
```

## Quad는 이런 컷에만 사용

- paw tap
- ingredient drop
- single stir
- steam
- plate slide
- parsley / garnish reaction
- static product/tool B-roll

## Quad 금지

- Hero food reveal
- 얼굴/캐릭터 감정이 중요한 shot
- 복잡한 조리 변형
- 여러 object가 panel 사이를 오가는 action
- 긴 camera movement
- 중요한 text / 숫자 표시

## 품질 문제

Quad crop은 master의 1/4 픽셀만 사용하므로 full-frame보다 세부 품질이 낮다.

유료 Flow에서 1080p upscale이 0 credits라면 **master를 먼저 1080p upscale → crop**한다. crop 후 540×960이면 local 2× upscale로 1080×1920 export할 수 있다. 단, AI upscaler는 털/음식 질감을 과도하게 만들어낼 수 있으므로 Hero shot에는 쓰지 않는다.

---

# 오디오는 Flow에서 경제적으로 분리하지 않는다

Veo 3.1은 prompt 기반 synchronized audio를 만들 수 있지만, quad 방식에서는 네 panel의 audio가 하나의 master soundtrack으로 합쳐지므로 crop으로 분리할 수 없다.

따라서 경제형 pipeline의 원칙:

```text
Flow generated audio = 폐기
Voice / music = Flow에서 생성하지 않음
SFX = 후편집 reusable library
```

재사용 SFX library 예:
- tiny_sizzle.wav
- paw_tap_wood.wav
- ceramic_click.wav
- wooden_spatula_scrape.wav
- tiny_leaf_rustle.wav
- soft_roomtone.wav
- micro_pop.wav

한 번 만들어두고 episode마다 볼륨/타이밍만 바꾼다.

Timestamp full-frame에서 생성 audio가 정확하게 맞는 경우만 예외적으로 살릴 수 있다.

---

# 무료 keyframe을 영상처럼 활용

Nano Banana 2 Lite keyframe은 video credits를 쓰지 않으므로 final edit의 20~30%까지 활용 가능하다.

한 keyframe을:
- 0.6~1.0초 digital push-in
- 0.4초 cliffhanger freeze
- 0.5초 reaction hold
- 0.5~0.8초 macro crop pan
- 마지막 loop frame

으로 사용한다.

단, 같은 정지 화면을 1.5초 이상 오래 유지하지 않는다.

---

# 비용 비교

## SAFE — 기존

```text
4 × Lite 8s = 40 credits
```

가장 높은 endpoint continuity.

## RECOMMENDED LAB

```text
2 × timestamp multi-shot Lite = 20 credits
+ 필요 시 dedicated hero Lite = 10
= 20~30 credits
```

## AGGRESSIVE QUAD HYBRID

```text
1 × timestamp full-frame = 10
1 × 2x2 quad B-roll = 10
= 20 credits
```

단, Quad가 실패하면 추가 generation으로 절감분이 사라지므로 **동일 prompt를 계속 reroll하지 않는다.** 1회 실패 시 timestamp full-frame으로 fallback.

---

# 가장 중요한 과금 함정

## 하지 말 것 1 — output 여러 개

`Give me 4 variations` 또는 output_count 4는 한 request라 해도 generation별 과금될 수 있다. 비용 절감 아님.

## 하지 말 것 2 — 4초 생성

Lite 4초와 8초 가격이 동일하므로 특별한 이유가 없으면 8초 사용.

## 하지 말 것 3 — Quality로 문제 해결

Quality 1회 = 100 credits. 초기 채널에서는 10-credit Lite 10회와 같은 비용이다.

## 하지 말 것 4 — Omni Flash edit로 사소한 수정

영상 edit 1회 = 40 credits. crop/freeze/speed/overlay/SFX 문제는 editor에서 해결.

## 하지 말 것 5 — Extend를 절약 수단으로 착각

Lite Extend도 generation당 10 credits이므로 새 generation보다 싸지 않다. continuity가 꼭 필요한 경우에만 사용.

---

# TK-001 실험 프로토콜

동일 episode를 실제로 두 방식으로 비교한다.

## Version E20
- 2 timestamp Lite generations
- 최대 20 credits
- audio discard
- 5 free keyframes 활용

## Version E30
- E20 + dedicated Hero/Resolution Lite 1개
- 최대 30 credits

40-credit SAFE 버전은 E20/E30이 continuity QC를 통과하지 못할 때만 제작한다.

비교 지표:
- usable shots per generation
- rerolls required
- total credits spent
- human editing minutes
- continuity defects
- final 24h Stayed to watch
- final 24h APV

승격 조건:

> E20 또는 E30이 SAFE 대비 retention이 유의하게 나쁘지 않고, reroll 포함 평균 credits가 낮으면 새 default로 승격한다.
