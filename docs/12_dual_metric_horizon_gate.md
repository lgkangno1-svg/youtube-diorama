# 12 — Dual-Metric Horizon Gate

작성 기준: 2026-08-24

## 목적

2026-08-24부터 YouTube의 public view는 영상이 재생되기 시작하는 순간부터 집계된다. 반면 YPP 수익은 engaged views/engaged watch hours, YPP 자격은 qualified views 기준을 유지한다.

따라서 Tiny Cat Kitchen은 **한 개의 조회수 숫자로 제작 의사결정과 브랜드 세일즈를 동시에 하지 않는다.**

---

## 1. 두 개의 계기판

### A. Internal Quality Dashboard — 제작/Flow 비용 의사결정

우선순위:
1. Stayed to watch
2. Average percentage viewed
3. Subscribers per 1,000 engaged views
4. Comments per 1,000 engaged views
5. Engaged/public ratio는 보조 진단

용도:
- 훅을 고칠지
- 중간 클리프행어를 고칠지
- IP/캐릭터 전환을 고칠지
- 해당 소재에 Flow 크레딧을 더 쓸지 말지

### B. External Reach Dashboard — 협찬/브랜드 세일즈

사용 가능 지표:
- public views
- 최근 28일/90일 public reach
- 평균 public views per Short
- 최고 public views
- 일본 시청자 비중(Studio에서 확보 가능할 때)

용도:
- 브랜드/협찬에 채널의 실제 노출 규모 설명
- media kit
- CPM이 아니라 캠페인 도달 규모 협상

**주의:** public views가 2026-08-24부터 더 빠르게 증가할 수 있으므로, 과거 기간과 동일 정의로 섞어 비교하지 않는다.

---

## 2. Horizon Gate — 24h와 72h를 섞지 않는다

기존 score script는 절대 engaged_views의 순위를 일부 사용했다. 이는 업로드 후 24시간 데이터와 72시간 데이터를 섞을 경우 노출시간 차이를 콘텐츠 품질로 오인할 수 있다.

새 규칙:
- 모든 분석 row에 `observation_hours` 필수
- 24h cohort는 24h끼리 비교
- 72h cohort는 72h끼리 비교
- 같은 episode의 24h/72h snapshot을 별도 row로 저장 가능
- horizon이 다른 row는 같은 percentile pool에 넣지 않는다

권장 snapshot:
- 24h: 빠른 훅/리텐션 진단
- 72h: 소재/세계관/구독전환 판단

---

## 3. Winner Score 변경

Flow 재투자 판단 score는 distribution scale보다 **콘텐츠 품질과 전환**을 우선한다.

```text
35% Stayed to watch percentile
35% APV percentile
20% subscribers / 1,000 engaged percentile
10% comments / 1,000 engaged percentile
```

`raw engaged views`는 winner score에서 제거한다.

이유:
- raw engaged views는 추천 노출량, 업로드 시간, 관측시간의 영향을 크게 받음
- Flow 제작 품질을 평가할 때는 swipe-stop, 완주, IP 전환이 더 직접적임
- public/engaged 절대 규모는 별도의 Reach Dashboard에서 본다

---

## 4. Credit Reinvestment Gate

### 24h

```text
STW low + APV high
→ OPEN만 수정
→ 전체 4-generation reroll 금지

STW high + APV low
→ DANGER/PAYOFF만 수정

STW low + APV low
→ 추가 Flow 크레딧 중단
```

### 72h

```text
STW/APV high + subs low
→ 캐릭터 signature/lore/callback 수정

STW/APV/sub conversion high
→ 같은 포맷을 복제하지 말고 fingerprint 3개 이상 바꾼 후 후속작 제작

public reach high + quality low
→ 브랜드 세일즈에는 reach 사례로 보관하되, 제작 포맷 승자로 지정하지 않음
```

---

## 5. 브랜드 협찬에 유리하게 쓰는 방식

YouTube는 2026-08-24의 view 정의 통일이 크리에이터가 자신의 규모와 브랜드 가치를 더 명확하게 표현하는 데 도움이 된다고 안내했다.

따라서 향후 media kit에는 다음처럼 분리한다.

```text
REACH
- 28-day public views
- median public views / Short
- top public-view Short

QUALITY
- median Stayed to watch
- median APV
- subscribers per 1,000 engaged views

AUDIENCE
- Japan share
- age bands when available
```

브랜드에게 public reach를 보여주되, 내부적으로는 engaged/qualified quality를 계속 최적화한다.

---

## 6. Flow 비용 기준은 유지

공식 Google Flow 기준 재확인:
- Veo 3.1 Lite: 4/6/8초, 비-Ultra 10 credits / Ultra 5 credits
- First + Last frame: Lite 지원, Fast는 아직 Coming soon
- 무료 비구독: 일일 50 Flow credits
- 실패 generation은 과금되지 않음
- Nano Banana 2 Lite는 무료 기본 이미지 모델

따라서 기존:

```text
5 free keyframes
→ 4 x 8s Veo 3.1 Lite frame-locked generations
→ 40 credits
→ 10-credit contingency reserve
```

는 유지한다.

---

## 7. 이번 루프의 실무 결론

1. Flow 생성 구조는 변경하지 않는다.
2. 성과 스코어에서 raw engaged volume을 제거한다.
3. 24h/72h horizon을 강제한다.
4. public views는 버리지 않고 **브랜드 세일즈용 reach metric**으로 별도 활용한다.
5. 절대 STW/APV 목표치 대신 같은 horizon의 최근 cohort 상대평가를 사용한다.

핵심 문장:

> **제작은 engaged quality로 최적화하고, 협찬은 public reach로 판매한다. 두 숫자를 섞지 않는다.**
