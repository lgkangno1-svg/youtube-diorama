# Frame-Lock Compatibility + Credit Reserve + Hype Growth Standard

작성 기준: 2026-08-24

## 이번 루프에서 발견한 핵심 교정

기존 전략은 `Veo 3.1 Lite First+Last → 실패 시 Fast 승격`을 품질 단계처럼 취급했다.

하지만 Google Flow 공식 모델 지원표의 현재 상태는 다음과 같다.

- Veo 3.1 Lite: First + Last frame 지원, 4s / 6s / 8s
- Veo 3.1 Fast: First + Last frame은 `Coming soon`
- Veo 3.1 Lite / Fast는 Ingredients/References to Video를 지원하지만 이는 8초 중심의 별도 모드다.

따라서 **frame-locked continuity가 중요한 컷을 Fast로 바꾸는 것은 동일 모드의 단순 품질 승격이 아니다.**

Tiny Cat Kitchen처럼 고양이 발, 팬, 음식 크기, 주방 레이아웃의 endpoint continuity가 중요한 프로젝트에서는 이 차이가 실제 재생성 비용보다 더 중요하다.

---

## 1. 수정된 실패 처리 순서

```text
1. minor artifact
   → editor fix

2. 한 컷의 구조적 실패
   → 같은 First+Last keyframe으로 Veo 3.1 Lite 1회 reroll

3. 반복 실패
   → action을 단순화하거나 start/end keyframe 자체를 수정
   → Lite reroll

4. Fast/Quality
   → 두 endpoint lock을 포기해도 되는 별도 hero insert / first-frame-only / reference shot에만 검토
```

즉:

> **Frame lock이 필요하면 Lite를 지킨다. 품질 승격보다 continuity를 우선한다.**

Fast가 향후 공식적으로 First+Last를 지원하면 이 규칙을 다시 검토한다.

---

## 2. 현재 Flow 크레딧 팩트

2026-08-24 Google 공식 기준:

- 비구독자: 50 Flow credits / day
- Plus: 200 / month
- Pro: 1,000 / month
- Ultra $100: 10,000 / month
- Ultra $200: 25,000 / month

Generation cost:

- Veo 3.1 Lite 4/6/8s: non-Ultra 10 / Ultra 5
- Fast 4/6/8s: 20 / 10
- Quality 8s: 100
- Gemini Omni Flash: 4s 15 / 6s 20 / 8s 25 / 10s 30
- Gemini Omni Flash video edit: 40
- 1080p upscale: paid Plus/Pro/Ultra 0 credits; non-subscriber unavailable

중요:

- 비용은 request가 아니라 **generation당** 차감된다.
- 요청 하나가 결과 2개를 만들면 2 generation 비용이 될 수 있으므로 `output_count = 1`을 유지한다.
- 무료 50크레딧은 첫 generation이 refresh cycle을 트리거한다.
- 남은 무료 크레딧은 이월되지 않는다.

---

## 3. 무료 계정에 최적화된 하루 운영

Tiny Cat Kitchen 첫 패스:

```text
G1 = Lite 10
G2 = Lite 10
G3 = Lite 10
G4 = Lite 10
----------------
base = 40 credits
reserve = 10 credits
```

이 마지막 10을 **처음부터 5번째 scene에 쓰지 않는다.**

순서:

1. 4개 scene 생성
2. 하나의 타임라인으로 붙임
3. 전체를 본 뒤 치명적인 실패 1개만 선정
4. 그 컷만 10-credit reroll
5. 네 컷이 모두 usable이면 추가 generation 없이 종료

무료 계정에서는 이게 가장 단순한 `하루 한 편 초안 + 한 번의 보험` 구조다.

---

## 4. 사람이 승인하는 횟수를 4회 → 2회로 축소

기존:

1. title
2. hook
3. keyframes
4. final

새 구조:

### Approval A — Production Card
한 번에 묶어서 본다.

- title
- hook
- 5-keyframe contact sheet
- resolution family
- creator signature
- 예상 credit budget

승인 기준은 단 하나:

> `첫 화면부터 이해되고, 다섯 장만 봐도 다른 에피소드와 구분되는가?`

### Approval B — Final Export

- 첫 0.5초 swipe-stop
- 해부학적으로 정상적인 고양이 발
- scale continuity
- creator signature
- ending
- AI disclosure / upload metadata

중간 scene prompt 텍스트는 사람이 직접 읽고 승인하지 않는 것을 기본값으로 한다.

---

## 5. Hype를 500-subscriber 이후 성장 레버로 추가

YouTube의 현재 Hype 기능은 지원 지역에서 **YPP에 가입한 500~500,000 subscriber의 성장 채널**을 대상으로 한다.

신규 영상은 게시 후 7일 동안 시청자가 Hype할 수 있고, 국가별 leaderboard 및 Hype badge/발견 기회가 생길 수 있다.

따라서 Expanded YPP에 진입한 뒤에는 모든 영상에서 `좋아요/구독`을 반복 요청하지 않는다.

대신 채널의 중요한 IP 에피소드나 시즌 오프닝에서만:

```text
この店、続いてほしかったらHypeして。
```

같은 **스토리 내부 CTA**를 테스트한다.

조건:

- Hype가 실제 채널/지역에 활성화된 경우만 사용
- every-video CTA로 만들지 않음
- 댓글 CTA와 동시에 여러 요청을 쌓지 않음
- 가장 세계관 가치가 큰 영상에서만 집중

---

## 6. 수익화 경로를 더 정확히 분리

### 500 subscriber Expanded YPP

공식 기준:

- 500 subscribers
- 최근 90일 public uploads 3개
- 3M qualified Shorts views / 90d 또는 3,000 qualified long-form watch hours

가능성이 열리는 것:

- memberships
- Super Thanks 등 fan funding
- own store / own products 중심의 Shopping 기능
- Hype eligibility(지원 지역/기능 상태 확인)

### Other-brand YouTube Shopping Affiliate

이 기능은 **별도의 Affiliate eligibility**를 가진다.

한국과 일본은 현재 지원 국가 목록에 들어가지만:

- YPP 가입
- YPP subscriber threshold
- 채널/파일럿 조건
- Made for Kids 여부 등

별도 조건을 적용한다.

따라서 내부 전략에서:

```text
500 subscribers == other-brand affiliate guaranteed
```

로 계산하지 않는다.

Studio에 실제 Affiliate 초대/자격이 보이는 시점부터 제품 태깅 수익을 KPI에 넣는다.

---

## 7. Tiny Cat Kitchen의 수익화 우선순위

```text
Phase 0
→ 조회수/캐릭터 IP
→ business contact + 브랜드가 보기 쉬운 포트폴리오

Phase 1
→ Expanded YPP 500 / 3M
→ fan funding + own-product/eligible Shopping + Hype

Phase 2
→ 1,000 / 10M (2026 현재 full Shorts ads/Premium)

Phase 3
→ 실제 Shopping Affiliate / Creator Partnerships / 직접 브랜드딜
→ 미니 주방 가젯, 식품, 편의점/음식 브랜드와 구조적으로 연결
```

2027-02-01부터 신규 full ads/Premium Shorts 진입 기준이 20M qualified Shorts views / 90d로 올라갈 예정이므로, **2026년에 1,000 / 10M에 도달할 수 있다면 전략적 가치가 크다.**

---

## 8. 콘텐츠/브랜드 구조에 미치는 영향

브랜드 협찬을 받기 쉬운 영상을 따로 만들 필요가 없다.

기본 세계관을 다음처럼 설계한다.

```text
cat kitchen
→ tiny cookware
→ ingredients
→ convenience store / market
→ appliance / gadget
→ seasonal menu
```

이 구조는 나중에 자연스럽게 다음 카테고리를 받을 수 있다.

- 조리도구
- 미니/소형 가전
- 식품 브랜드
- 편의점 신상품
- 일본 계절 음식
- 캐릭터 굿즈

핵심은 제품을 억지로 광고하는 게 아니라 **고양이 세계 안에서 원래 쓰던 물건의 자리를 브랜드 제품이 차지하도록 하는 것**이다.

---

## 9. 다음 자동 검토 조건

향후 루프에서 아래가 바뀌면 즉시 전략을 재검토한다.

1. Flow Fast가 First + Last frame을 정식 지원
2. Lite/Fast/Quality credit cost 변경
3. 무료 50-credit 정책 변경
4. YouTube Shopping Affiliate subscriber threshold 명확화/변경
5. Hype 지원 국가/Shorts 적용 범위 변경
6. 2027 YPP transition 세부사항 변경

현재 최우선 원칙:

> **저렴한 모델을 쓰는 것보다, 지원되는 모드를 정확히 써서 재생성을 막는 것이 더 싸다.**
