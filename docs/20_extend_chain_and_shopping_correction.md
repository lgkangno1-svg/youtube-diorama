# H30-X Extend Chain + Shopping Correction

작성 기준: 2026-08-24

## 1. 왜 다시 바꾸는가

기존 H30은 Veo 3.1 Lite 8초 영상 3개를 각각 독립 생성했다.

```text
G1 First+Last 8s
G2 First+Last 8s
G3 First+Last 8s
= 30 credits non-Ultra / 15 Ultra
```

비용은 낮지만 G3를 새 장면으로 다시 시작할 때 카메라 위치, 팬 위치, 음식 상태, 고양이 발 자세가 미세하게 바뀌는 실패 가능성이 남는다.

Google Flow 공식 기능표에서 모든 Veo 3.1 8초 영상은 Extend 대상이 될 수 있고, Extend는 Veo 3.1 Lite로 수행한다. Lite Extend 비용은 일반 Lite generation과 동일하게 10 credits non-Ultra / 5 credits Ultra다.

따라서 같은 30크레딧에서 독립 장면 수를 하나 줄이는 실험이 가능하다.

## 2. H30-X 후보 구조

```text
G1 First+Last 8s
OPEN → PREP

G2 First+Last 8s
COOK → DANGER

G3 Extend G2 8s
RECOVERY → ASSEMBLY → RESOLUTION
```

비용:
- non-Ultra: 10 + 10 + 10 = 30 credits
- Ultra: 5 + 5 + 5 = 15 credits

기존 H30과 명목 비용은 같다.

차이:
- 4개 keyframe → 3개 keyframe
- 세 번째 장면의 독립적인 시작 상태 생성 제거
- DANGER → RECOVERY의 움직임 연속성을 모델이 직접 이어갈 수 있음
- 사용자 storyboard/keyframe 승인량 감소

## 3. 이 방식이 적합한 장면

Extend를 우선 검토:
- 같은 장소
- 같은 카메라 방향
- 같은 고양이
- 같은 음식/도구
- 앞 장면의 행동을 그대로 이어가는 경우

예:

```text
계란 가장자리가 찢어질 듯함
→ 같은 팬에서 계란이 살아남음
→ 같은 접시에 천천히 올림
```

독립 First+Last 장면 유지:
- 방/가게 위치가 바뀜
- 낮 → 밤 등 큰 조명 변화
- 완전히 다른 카메라 구도
- 음식 상태를 정확한 특정 이미지로 끝내야 함
- Hero food shot의 최종 모양을 강하게 고정해야 함

## 4. 중요한 제한

Extend는 비용 절감 마법이 아니다. 비용은 세 번째 Lite generation과 동일하다.

목적은:

> 같은 30크레딧으로 continuity failure와 사람의 setup 작업을 줄이는 것.

따라서 Extend output이 나쁘다고 다음을 동시에 만들지 않는다.

```text
Extend reroll
+
독립 G3 First+Last
```

순서:
1. Extend 한 번 사용
2. minor 오류면 편집으로 살림
3. 구조적 실패면 Extend 한 번만 재시도하거나 독립 G3로 fallback
4. 두 경로를 동시에 선생성 금지

## 5. 오디오

Extend 경계의 native audio continuity는 공식 지원 문서에서 품질 보장이 명시되어 있지 않으므로 비용 전략에 포함시키지 않는다.

기본:
- 각 생성의 깨끗한 cooking ASMR은 사용 가능
- Extend 경계가 어색하면 native audio를 과감히 교체
- room tone / tiny sizzle / wood scrape / ceramic click을 reusable library에서 sound bridge로 사용
- narration은 기본 없음

즉 영상 continuity는 Flow가 담당하고, 오디오 continuity는 편집에서 싸게 해결한다.

## 6. 현재 TK-001 적용

TK-001은 H30-X trial로 변경했다.

```text
KF0 OPEN
KF1 CONSTRAINT
KF2 DANGER

G1 KF0 → KF1
G2 KF1 → KF2
G3 Extend G2
```

G3 목표:
- 계란 회복
- 밥 위 조립
- 증기 여운
- 파슬리 선택

첫 결과가 unusable하면 manifest fallback에 따라 G3만 정상 Lite First+Last 방식으로 생성한다.

## 7. Flow 공식 비용/기능 재확인

2026-08-24 Google Flow Help 기준:
- Veo 3.1 Lite: 4s / 6s / 8s = 10 credits non-Ultra, 5 Ultra
- Lite Extend = 동일 비용
- 무료 비구독자는 하루 50 Flow credits
- 비용은 request가 아니라 generation당
- 하나의 request가 2개 영상을 만들면 2 generation 비용이 발생할 수 있으므로 output count = 1 유지
- First+Last: Lite 지원
- Fast First+Last: Coming soon
- 모든 Veo 3.1 8s 영상은 Extend 가능, Extend는 Lite 사용
- Nano Banana 2 Lite는 no-charge image model

## 8. Shopping 수익화 계획 교정

초기 문서에서 `500명 Expanded YPP → Shopping`을 너무 넓게 해석할 위험이 있었다.

현재 YouTube 공식 도움말 기준:

### 500 subscribers Expanded YPP
가능한 Shopping은 **자사 상품 홍보**가 핵심이다.

필요 조건:
- 500 subscribers
- 최근 90일 public uploads 3개
- 3M qualified Shorts views/90d 또는 3,000 qualified watch hours
- 기타 YPP 요건

### 다른 브랜드 상품 Shopping
별도 조건이다.

현재 공식 안내 예시:
- 10,000 subscribers
- 4,000 qualified watch hours 또는 10M qualified Shorts views
- 지원 channel country/region 조건
- 현재 안내된 대상 지역에는 KR, ID, US가 명시됨
- Made for Kids 등 추가 제한 존재

따라서 Tiny Cat Kitchen의 초기 수익화 forecast에서 다음을 금지한다.

```text
500 subscribers = 다른 브랜드 affiliate 자동 개방
일본 시청자 타깃 = 일본 Shopping affiliate 자동 가능
```

실제 Studio의 Earn/Shopping eligibility를 source of truth로 사용한다.

## 9. 수익화 우선순위 수정

YPP 이전:
1. business contact
2. original character/IP proof
3. 반복 가능한 reach/retention 데이터
4. 직접 브랜드 협업용 media kit

500명 Expanded YPP:
1. fan funding
2. own-product Shopping이 실제 활성화되면 사용
3. Creator Partnerships가 Studio에서 열리면 활용

10k 및 해당 Shopping 자격 충족 이후:
- 다른 브랜드 상품 태깅/affiliate를 실제 Studio eligibility 확인 후 사용

## 10. 다음 의사결정

H30-X를 이론만으로 기본값으로 확정하지 않는다.

TK-001에서 비교할 것:
- G2→G3 visual continuity
- G3 usable seconds
- 고양이 발/팬/음식 scale drift
- Extend 경계 편집 난이도
- native audio 사용 가능 여부

판단:

```text
Extend가 독립 G3보다 setup이 적고 usable continuity가 좋음
→ 다음 continuity-heavy episode에 H30-X 적용

Extend가 resolution 제어를 크게 떨어뜨림
→ 기존 3 × First+Last H30 유지
```

핵심:

> **크레딧을 더 줄이지 못하더라도, 같은 크레딧으로 재생성 확률과 사람의 setup을 줄이면 실제 제작비는 내려간다.**
