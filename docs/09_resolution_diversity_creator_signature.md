# Resolution Diversity + Creator Signature Standard

작성 기준: 2026-08-24

## 이번 루프에서 발견한 핵심 약점

기존 포맷은 매 영상 끝에 `unexpected choice / twist`를 넣는 것을 강하게 권장했다.

하지만 YouTube의 현재 수익화 정책은 다음 유형을 명시적으로 위험하다고 본다.

- characters put in the same situation over and over with the same outcome
- templated storylines with minimal variation
- AI-generated content using generic or unoriginal templates that looks mass-produced
- formulaic shock/surprise used mainly to manufacture views

따라서 `고양이가 마지막에 음식 대신 엉뚱한 것을 고른다`를 채널 시그니처로 매번 반복하면, 시청자 입장에서도 예상 가능해지고 장기적으로는 inauthentic-content 심사에도 불리할 수 있다.

새 원칙:

> **반전은 선택 사항이다. 모든 에피소드는 대신 고유한 resolution을 가져야 한다.**

---

## 1. KF4 이름 변경

기존:

```text
KF4_TWIST
```

새 기본:

```text
KF4_RESOLUTION
```

가능한 resolution 유형:

1. `comedy_twist` — 예상 밖 행동
2. `proof_resolution` — 숫자/규칙 성공을 눈으로 검증
3. `emotional_resolution` — 관계나 세계 상태가 바뀜
4. `transformation_resolution` — 전/후 변화가 최대치에 도달
5. `choice_resolution` — A/B 중 하나를 선택
6. `lore_resolution` — 가게/캐릭터 세계관에 새 사실이 생김
7. `failure_resolution` — 실패 자체가 다음 이야기의 원인이 됨
8. `satisfying_resolution` — 조리/배치/질감의 완성감으로 끝냄

최근 5편 안에서 같은 resolution family를 3회 이상 쓰지 않는다.

---

## 2. 창작자 서명 레이어

Flow 영상 자체에는 speech를 생성하지 않는 기존 원칙을 유지한다.

대신 후편집에서 각 영상에 **짧은 일본어 한 줄**을 넣는다.

목적:

- 사람이 만든 채널이라는 창작자 관점 강화
- 같은 AI 템플릿으로 보이는 위험 감소
- 캐릭터의 말투/유머 축적
- 시청자가 채널 특유의 문장을 기억하게 함
- Flow에서 대사를 생성하느라 생기는 크레딧/연속성 비용 제거

manifest:

```yaml
creator_signature:
  narrator_angle: ...
  signature_line: "..."
```

규칙:

- 다른 에피소드에 그대로 붙여도 자연스러운 일반 문장 금지
- 화면을 장황하게 설명하지 않음
- 1~2문장, 보통 3초 이내
- 캐릭터를 과하게 유아화하지 않음
- 일본 10~20대가 자연스럽게 받아들일 구어체 우선

예:

```text
TK-001: そこまで作って、パセリなんだ。
TK-002: 10粒、ちゃんと全員います。
TK-003: 0人だった夜に、最初の一杯が出ました。
```

세 문장은 같은 캐릭터를 쓰지만 관점과 감정 기능이 서로 다르다.

---

## 3. AI disclosure overlay 대응

YouTube는 2026년 5월부터 photorealistic AI Shorts의 AI disclosure를 영상 위에 직접 overlay할 수 있다고 안내한다.

따라서 첫 프레임에서 가장 중요한 시각 정보 하나를 화면 최상단 가장자리에만 배치하지 않는다.

실무 규칙:

- 첫 0.5초 핵심 물체는 중앙 60% 안에 둔다.
- 제목 역할을 하는 생성 텍스트는 영상 안에 만들지 않는다.
- 중요한 숫자 제약은 VO/caption + 실제 보이는 물체 수로 중복 전달한다.
- Flow compiler가 `upper overlay-safe area`를 확보하도록 기본 지시한다.

AI disclosure 자체는 YouTube가 추천이나 수익화 자격을 제한하지 않는다고 명시하므로 숨기지 않는다.

---

## 4. 비용 의사결정 게이트

2026-08-24 공식 Flow 기준:

- Veo 3.1 Lite 4/6/8s: non-Ultra 10 credits / Ultra 5
- Fast: 20 / 10
- Quality 8s: 100
- Gemini Omni Flash video edit: 40 credits

따라서:

```text
minor defect
→ editor fix / crop / freeze / keyframe cutaway

structural defect in one clip
→ one Lite reroll (10/5)

Lite motion repeatedly fails
→ one Fast upgrade (20/10)

Gemini Omni Flash edit
→ only when a single 40-credit edit is likely to replace >=4 Lite rerolls
   OR when the edit capability itself is uniquely needed

Quality
→ reusable hero asset after the format has already proven itself
```

`Omni edit로 간단히 고치기`는 기본값이 아니다.

---

## 5. 자동 originality gate

새 episode를 만든 뒤 LLM에게 다시 비평시키기 전에 로컬 deterministic validator를 먼저 실행한다.

```bash
python tools/validate_episode_originality.py episodes/TK-003.yaml
```

검사:

- creator_signature 존재
- KF4_RESOLUTION 존재
- 직전 5편 대비 fingerprint 5개 중 최소 3개 차이
- conflict + ending pair 중복 여부

이 검사는 AI token을 쓰지 않는다.

---

## 6. 현재 3편의 resolution 분산

### TK-001

```text
family: comedy_twist
ending: 오므라이스 대신 파슬리
```

### TK-002

기존 `파 한 조각만 가져감`을 삭제.

```text
family: proof_resolution
ending: 최종 10알이 모두 살아 있다는 것을 시각적으로 검증 + 만족스러운 앞발 톡
```

숫자 도전의 본질을 결말에서 다시 보상한다.

### TK-003

기존 `작은 그릇 선택`을 단순 개그가 아니라 감정적 장면으로 수정.

```text
family: emotional_resolution
ending: 첫 손님에게 큰 그릇을 내고, 고양이는 작은 그릇 옆에서 같은 김을 쬠
```

첫 세 편의 결말 기능이 서로 완전히 달라진다.

---

## 7. 최신 경쟁 신호 반영

2026-08 현재 확인한 참고 신호:

- 일본 `AI猫にゃんこちん Official`은 약 91.8K 구독자, 최근 30일 약 0.88M 조회로 여전히 성장 중이다. 최신 상위 콘텐츠는 요리 하나보다 `休日ルーティン`처럼 캐릭터의 생활/성격을 보여주는 방향도 강하다.
- 전통 `Miniature Cooking ミニチュア料理` 채널은 최근 업로드가 없고 30일 성장이 사실상 정체되어 있다.
- `Miniature Room`은 2026-08-12 `世界一小さいきゅうりの1本漬け`처럼 극단적 스케일 + 계절/일상 맥락을 계속 사용한다.
- 2026-08 하순 일본 Z세대용 신상품 기사에서는 배, 고구마/밤, 편의점 신작, 9월 3일 グミの日를 앞둔 제품들이 강하게 노출되고 있다.

따라서 Trend Injection은 음식 이름만 복사하지 않고 아래 세 종류로 확장한다.

```text
A. food trend
B. seasonal/cultural moment
C. character lifestyle situation
```

8월 말~9월 초 후보 예:

- 梨 / 和梨 texture
- 芋・栗 early-autumn transformation
- グミの日 직전 tiny gummy experiment
- 여름 끝 야시장/축제 정리
- 비 오는 심야 식당

브랜드 제품 디자인이나 캐릭터 IP를 그대로 재현하지 않고, `맛/계절/행동 구조`만 가져온다.

---

## 8. 수익화 관련 교정

Expanded YPP의 500 subscriber / 3M Shorts tier는 fan funding과 일부 Shopping 조기 접근에 중요하다.

다만 **Creator Partnerships 자체는 기능별 안내가 서로 다르게 표현되고 있다.** 현재 한국용 Creator Partnerships 도움말은 광고 수익 공유 자격이 있는 YPP 크리에이터를 최소 요건으로 안내한다. 따라서 `500명 도달 즉시 브랜드 문의 탭이 열린다`고 운영 계획에 확정적으로 가정하지 않는다.

브랜드 수익 전략은 두 경로로 분리한다.

```text
Before full ad-share eligibility:
- public business contact
- original IP portfolio
- direct/outbound brand pitches when appropriate
- own products / eligible Shopping features after expanded YPP

After ad-share eligibility and Creator Partnerships access:
- channel insight sharing
- Media Kit / desired rate settings where available
- advertiser discovery
```

YouTube 공식 시스템을 기다리는 것과 직접 브랜드 포트폴리오를 만드는 것을 별개로 운영한다.

---

## 9. 현재 최종 원칙

```text
같은 캐릭터 ≠ 같은 이야기
같은 주방 ≠ 같은 결말
같은 4-generation factory ≠ 같은 창작물
```

factory는 생산 비용을 표준화하고,
**goal / conflict / emotional function / resolution / creator voice는 매편 달라져야 한다.**
