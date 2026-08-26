# 26 — Flow UI Mode Preflight

목표: Google Flow에서 **새 Veo 생성 화면과 기존 영상 수정 화면을 혼동해 잘못된 모델/크레딧을 쓰는 사고**를 막는다.

## 2026-08-26 공식 Flow 재확인

Google Flow Help 기준:
- 표준 새 동영상 생성에서는 prompt box의 모델 이름을 열고 `Video`를 선택한 뒤 `aspect ratio / output count / model / generation length`를 설정한다.
- Veo 3.1 Lite는 Text-to-Video, First Frame, First+Last Frame에서 4s/6s/8s를 지원한다.
- Ingredients/References-to-Video는 Veo 3.1 Lite에서 8s only다.
- Extend는 Veo 3.1 source 중 8s clip 기반이며 Lite로 연장한다.
- Veo 3.1 Lite 4s/6s/8s는 non-Ultra 기준 generation당 10 credits다.
- Gemini Omni Flash의 일반 생성은 4s/6s/8s/10s이며 길이에 따라 15/20/25/30 credits다.
- Gemini Omni Flash의 uploaded/generated video edit는 길이와 무관하게 40 credits다.

공식 source:
- https://support.google.com/flow/answer/16353334
- https://support.google.com/flow/answer/16352836
- https://support.google.com/flow/answer/16526234
- https://support.google.com/flow/answer/16935718

## 가장 중요한 운영 규칙 — 먼저 현재 UI 상태를 판별

### NEW VIDEO GENERATION 상태

다음이면 새 Veo generation을 진행할 수 있다.

```text
prompt box에서 model/generation settings를 열 수 있음
→ Video 선택
→ Veo 3.1 Lite 선택
→ 9:16
→ output count = 1
→ generation length = 8s 또는 해당 mode가 8s-only임을 확인
→ 표시 credit cost 확인
```

Tiny Cat Kitchen 기본값은 비용이 같은 4/6/8 중 **8s**다. 더 긴 usable motion을 얻기 위해서이며, 4s/6s를 쓸 특별한 이유가 없으면 선택하지 않는다.

### EXISTING VIDEO EDIT 상태

다음 신호가 보이면 새 G1/G2/G3 generation 화면으로 간주하지 않는다.

```text
기존 영상 하나가 편집 대상으로 열려 있음
prompt가 "수정 사항 설명" 계열임
하단 모델이 Omni Flash임
기존 영상의 특정 구간/버전을 수정하는 UI임
```

이 상태에서 Tiny Cat Kitchen의 다음 G scene을 만들지 않는다. 특히 **Omni Flash edit는 현재 40 credits/edit**이므로, 10-credit Veo Lite G1이라고 착각하면 안 된다.

해야 할 일:
1. 기존 clip edit 화면에서 나간다.
2. 프로젝트의 standard prompt box / 새 video generation 상태로 돌아간다.
3. generation settings → Video → Veo 3.1 Lite를 명시적으로 선택한다.
4. 9:16 / output 1 / length 또는 8s-only mode를 확인한다.
5. 표시 비용을 보고 나서만 생성한다.

## duration selector가 안 보일 때

`4s / 6s / 8s`가 안 보인다는 이유만으로 Flow 오류라고 판단하지 않는다.

가능한 원인:
- 기존 영상 edit/modify 상태
- Ingredients/References-to-Video처럼 현재 Veo Lite에서 8s-only인 mode
- Extend처럼 8s-only인 mode
- 지역/기능 rollout 차이
- generation settings panel이 닫혀 있음

따라서 **duration selector 존재 여부보다 active model + generation mode + displayed cost가 더 중요한 preflight**다.

## Tiny Cat Kitchen 생성 전 5초 체크

```text
1. 지금 새 영상 생성 상태인가?  (기존 영상 수정 상태면 STOP)
2. Video model = Veo 3.1 Lite인가?
3. Aspect ratio = 9:16인가?
4. Output count = 1인가?
5. 8s 선택 또는 해당 mode가 8s-only이며, 표시 비용이 예상과 맞는가?
```

하나라도 확실하지 않으면 generate를 누르지 않는다.

## Progressive Spend와의 관계

이 preflight는 Gate A의 일부다. 즉 비용 구조는:

```text
Gate A-0: POV/keyframe QC = 0 credits
Gate A-1: Flow UI mode/model/cost QC = 0 credits
G1: PASS 후에만 1 generation
G2: G1 PASS 후
G3: G2 PASS 후
G4: immersive_h40 + G3 PASS + independent beat일 때만
```

목표는 단순히 10 credits를 아끼는 것이 아니라 **잘못된 UI mode에서 25~40 credits를 써버리는 사고를 방지하는 것**이다.
