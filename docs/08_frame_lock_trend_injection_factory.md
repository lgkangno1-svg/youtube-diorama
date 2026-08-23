# Frame-Lock Factory + Trend Injection Gate

작성 기준: 2026-08-24

## 이번 루프에서 수정한 약점

이전 `4-generation` 전략은 비용을 40 credits까지 낮췄지만, **generation 실패율**을 충분히 낮추지 못했다.

Google Flow 공식 기능 기준으로 Veo 3.1 Lite는 `Frames to Video: First + Last`에서 4/6/8초를 지원한다. 비용은 4/6/8초 모두 비-Ultra 10 credits / Ultra 5 credits다.

따라서 초기 탐색의 새 기본은:

> 무료 Nano Banana 2 Lite keyframes → **Start + End frame locked Veo 3.1 Lite** → 4 generations

이다.

목표는 generation 수를 더 줄이는 것이 아니라 **재생성 횟수를 줄이는 것**이다.

---

## 1. 5-Keyframe / 4-Generation 구조

한 영상에 핵심 keyframe 5개만 먼저 승인한다.

- `KF0_OPEN` — 첫 0.5초 훅
- `KF1_CONSTRAINT` — 숫자/문제 명확화
- `KF2_DANGER` — 실패 직전
- `KF3_PAYOFF` — 결과 직전 또는 완성
- `KF4_TWIST` — 캐릭터 반전 / 다음 세계 상태

그 다음 4개의 Lite generation을 연결한다.

```text
G1: KF0_OPEN       -> KF1_CONSTRAINT
G2: KF1_CONSTRAINT -> KF2_DANGER
G3: KF2_DANGER     -> KF3_PAYOFF
G4: KF3_PAYOFF     -> KF4_TWIST
```

필요한 경우 마지막 편집 프레임으로 `KF0_OPEN`을 다시 삽입해 loop를 만든다. 루프용 video generation은 만들지 않는다.

### 왜 좋은가

- clip마다 시작 외형과 종료 외형을 미리 고정
- 고양이 발/음식/도구 scale drift 감소
- 다음 clip이 이전 clip의 끝 프레임에서 자연스럽게 시작
- `완성 음식이 갑자기 달라짐`, `주방 배치가 바뀜`, `재료 수가 증식` 같은 재생성 사유 감소
- Lite 4회 = 기존 40/20-credit budget 유지

---

## 2. Ingredients 사용 규칙 변경

모든 컷에서 Ingredients를 과하게 넣지 않는다.

### 기본

- 캐릭터가 크게 보이는 `G1`, `G4`: 캐릭터 reference + frame locks
- 조리 정밀도가 중요한 `G2`, `G3`: frame locks 우선, 필요한 핵심 object reference만 사용

이유:
- references가 많을수록 prompt 제약이 충돌할 수 있음
- Start/End frame이 이미 공간/scale/lighting의 강한 anchor 역할을 함

### Ingredients-to-Video가 더 적합한 경우

- 새 캐릭터가 처음 등장
- 새로운 주방/가게 asset을 처음 소개
- 두 캐릭터의 외형을 동시에 유지해야 함

그 외에는 Start + End frame lock을 우선한다.

---

## 3. 재생성 판단 규칙

첫 결과가 완벽하지 않다고 바로 재생성하지 않는다.

### 편집으로 살린다

- 0.3~0.7초의 작은 손/발 이상
- 마지막 0.5초 object jitter
- 너무 긴 멈춤
- 약한 camera drift

방법:
- crop
- speed ramp 1.05~1.20x
- freeze
- cutaway keyframe
- sound hit

### 재생성한다

아래 중 하나면 해당 generation만 다시 만든다.

- 고양이 발이 인간 손으로 변형
- 음식 identity가 바뀜
- 핵심 숫자 제약이 깨짐 (10알 → 15알 등)
- G2/G3의 conflict가 화면에서 이해되지 않음
- G4 twist가 한눈에 이해되지 않음

### Fast / Quality 승격

- Fast: Lite의 동작 이해도가 반복적으로 부족한 **특정 한 컷**만
- Quality: 채널에서 장기간 재사용할 hero asset만

전체 영상을 Fast/Quality로 다시 만드는 방식은 금지.

---

## 4. Trend Injection Gate

캐릭터 IP만 밀면 안정적이지만 성장 속도가 느려질 수 있다.

2026-08 기준 참고 데이터:
- 일본 `AI猫にゃんこちん Official`: 약 91.8K 구독자, 최근 30일 약 +0.88M views. 캐릭터/직업/일상 세계관은 안정적인 누적 성장에 강함.
- 일본 푸드 Shorts에서는 2026-06 업로드 `流行りのモッツァレラチーズスティックつくってみた`가 데이터 확인 시 약 977K views. `流行り` + ASMR + 강한 food transformation 조합이 빠른 reach에 강한 사례.
- Miniature Room은 2026-08 `世界一小さいきゅうりの1本漬け`처럼 `세계에서 가장 작은 + 익숙한 음식` 구조를 계속 사용.

따라서 신규 게시 비율을 다음처럼 운영한다.

```text
EP A: CORE IP / 숫자 도전
EP B: CORE IP / 생활 세계관
EP C: TREND INJECTION / 현재 유행 음식
반복
```

즉 **3편 중 최소 1편은 최근 7~30일 일본 푸드/디저트 트렌드를 반영**한다.

단, 트렌드 음식만 복제하지 않는다.

```text
현재 유행 음식
+ Tiny Cat Kitchen 세계관
+ 불가능한 scale/숫자 제약
+ 고유 conflict
+ 고유 ending
```

예:

```text
유행 치즈스틱
→ 2cm cheese stick
→ 치즈가 팬보다 길게 늘어나 가게 문까지 닿음
→ 고양이가 치즈를 자르려다 작은 가게 간판까지 끌어당김
```

---

## 5. Trend 후보 점수

AI가 트렌드 후보를 조사할 때 아래 점수로 먼저 거른다.

```text
TrendScore =
  30% recent_view_velocity
+ 25% visual_transformation
+ 20% recognizability_in_Japan
+ 15% tiny_scale_comedy
+ 10% brand_or_shopping_bridge
```

### 바로 버리는 후보

- 유명하지만 화면 변형이 거의 없음
- 0.5초 안에 음식 identity가 안 보임
- 고양이 캐릭터가 없어도 내용이 완전히 동일
- 현재 유행을 그대로 재현하기만 함
- 특정 브랜드/캐릭터 IP에 의존해 권리 문제가 생길 수 있음

---

## 6. 원본성 방어 — Episode Fingerprint

기존 6개 original/IP field 외에 `episode_fingerprint`를 추가한다.

```yaml
episode_fingerprint:
  hook_mechanic: numeric_constraint | social_problem | trend_transformation | comparison
  dominant_visual: ...
  conflict_mechanic: ...
  emotional_turn: ...
  ending_mechanic: ...
```

신규 에피소드는 직전 5편과 비교해 **5개 중 최소 3개가 달라야** 한다.

이 규칙은 YouTube의 `characters put in the same situation over and over with the same outcome` 및 mass-produced template 위험을 피하기 위한 내부 가드다.

---

## 7. 사람 작업을 줄이는 단일 승인 지점

사용자가 매 scene prompt를 직접 검토하지 않게 한다.

사람이 확인할 것은 게시 전 아래 4개뿐이다.

1. 일본어 title
2. 첫 3초 hook
3. 5-keyframe contact sheet
4. 최종 35~40초 export

나머지는 episode manifest와 prompt compiler가 만든다.

---

## 8. 현재 제작 파이프라인

```text
trend scan / episode concept
→ manifest
→ prompt compiler
→ Nano Banana 2 Lite 5-keyframe contact sheet
→ human approves one contact sheet
→ 4 x Veo 3.1 Lite Start+End-frame generations
→ automated rough cut
→ final human preview
→ upload
→ analytics learning
```

목표:

> 사용자는 `컨셉 선택 + keyframe 승인 + 최종 승인`만 한다.

---

## 9. 공식 정책/기능 기준

2026-08-24 확인 기준:

- Flow: Veo 3.1 Lite 4/6/8초 및 First+Last frame 지원, 비-Ultra 10 credits/generation, Ultra 5 credits/generation.
- 무료 Flow 사용자는 일일 50 credits. 한 요청이 여러 generations를 만들 수 있으므로 `output_count = 1` 유지.
- YouTube monetization: 반복/대량생산/서로 바꿔도 되는 AI 템플릿은 `inauthentic content` 위험. 같은 캐릭터 시리즈라도 storyline/focus/concept가 materially varied 하면 허용 가능.
- Expanded YPP: 500 subscribers + 3 public uploads + 3M valid Shorts views/90d (또는 long-form 기준)로 fan funding/일부 Shopping 접근.
- Ads/Premium: 현재 1,000 subscribers + 10M valid Shorts views/90d. 2027-02-01 신규 진입 기준은 20M qualified Shorts views/90d로 변경 예정.

---

## 10. 이번 루프의 핵심 결론

이제 최적화 대상은 `영상 한 편당 credit`만이 아니다.

```text
실제 비용 = 첫 생성 credits + 실패 재생성 credits + 사람 검수 시간
```

따라서 다음 단계는:

> **40-credit 4-generation 구조를 유지하면서, 무료 keyframe 5개와 Start/End frame locking으로 reroll probability를 낮추는 것**

이다.
