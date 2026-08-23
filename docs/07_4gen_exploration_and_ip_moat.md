# 4-Generation Exploration Gate + Character IP Moat

작성 기준: 2026-08-24

## 핵심 변경

초기 3편의 기본 비용을 다시 낮춘다.

기존 최신안:
- 무료 이미지 preflight
- Veo 3.1 Lite 5 generations
- 비-Ultra 50 credits

새 탐색안:
- Nano Banana 2 Lite를 **명시적으로 선택**해 keyframe/ingredient preflight
- Veo 3.1 Lite **4 generations**
- 비-Ultra 40 credits / Ultra 20 credits
- 나머지 4~6초는 keyframe punch-in, freeze, macro crop, reaction hold, opening-frame loop를 편집에서 만든다
- 성과가 확인된 포맷만 5번째 generation 또는 Quality hero asset으로 승격

Google Flow 공식 기준에서 Veo 3.1 Lite는 4/6/8초 모두 비-Ultra 10 credits, Ultra 5 credits다. 즉 초 수보다 generation 수가 비용의 핵심이다.

## 1. 왜 4 generations인가

첫 3편의 목적은 완성품 생산량이 아니라 `어떤 훅/스토리 구조가 먹히는지` 찾는 것이다.

4 × 8초 = 32초의 실제 모션을 확보한다.
여기에 다음 편집 요소를 사용하면 35~38초 Shorts가 가능하다.

- OPEN keyframe 0.6~1.0초
- 위험 순간 freeze 0.3~0.5초
- PAYOFF keyframe macro punch-in 0.5~0.8초
- reaction hold 0.5초
- opening frame loop 0.7~1.0초

초기 탐색 영상에서 38~40초를 억지로 채우기 위해 10 credits를 추가로 쓰지 않는다.

## 2. 4-generation 표준

### G1 — Hook + Constraint
첫 8초 안에 `고양이 + 숫자/비정상 제약 + 행동 시작`을 함께 처리한다.

### G2 — Progress + Danger
조리 진행과 실패 조건을 하나의 동작으로 합친다.

### G3 — Recovery + Final Risk
첫 문제 해결 후 마지막 성공 직전까지 진행한다.

### G4 — Payoff + Character Twist
완성 보상과 고양이의 예상 밖 행동을 같은 generation에서 끝낸다.

별도 CTA/루프/리액션 generation은 금지한다.

## 3. 승격 게이트

5번째 generation을 쓰는 조건은 아래 중 하나다.

- 4-generation 편집으로 의미 전달이 불가능
- 핵심 훅과 payoff 사이에 논리적 단절이 생김
- 첫 게시 데이터에서 포맷 자체가 승리 신호를 보였고 재제작 가치가 있음

Quality 100-credit 승격은 다음 조건에서만 허용한다.

- 채널 대표 썸네일/프로필/브랜드 자료로 장기간 재사용
- Lite 재생성보다 명확한 사업 가치가 있는 hero asset

## 4. 이미지 모델 선택 안전장치

Flow 도움말은 Nano Banana 2 Lite를 no-charge 기본 이미지 모델로 설명하지만, 컴퓨터 표준 프롬프트 UI는 Nano Banana Pro가 기본으로 표시될 수 있다.

따라서 preflight 때는 자동/기본값을 신뢰하지 말고:

1. Generation type = Image
2. Model = **Nano Banana 2 Lite** 명시 확인
3. Output count = 1
4. keyframe 승인 후에만 Video로 이동

이 규칙으로 이미지 단계에서 불필요한 유료/고급 모델 사용을 막는다.

## 5. Flow 기능 선택 규칙

- Ingredients/References to Video는 Veo 3.1 Lite/Fast에서 **8초 영상**에 사용
- First frame만 필요하면 Lite의 4/6/8초 Frames-to-Video 사용 가능
- First + Last frame은 Lite에서 4/6/8초 사용 가능
- Extend는 모든 Veo 3.1 8초 영상에 대해 **Lite로만** 수행
- character/voice reference가 꼭 필요한 특수편이 아니면 Omni Flash를 기본값으로 쓰지 않는다

캐릭터 일관성이 중요한 G1/G4는 Ingredients 또는 frame reference를 우선 사용하고, 중간 조리 컷은 불필요한 reference 입력을 줄여 prompt 충돌을 피한다.

## 6. IP Moat — 양산형 AI 채널 방어

YouTube는 같은 캐릭터 시리즈 자체는 허용하지만, 각 영상의 substance가 materially varied 해야 한다. 같은 상황과 같은 결말을 반복하면 inauthentic content 위험이 있다.

따라서 `unique_goal / unique_conflict / unique_ending` 외에 아래 필드를 episode manifest에 추가한다.

```yaml
ip_story_guard:
  character_motivation: ...
  world_state_change: ...
  callback_or_new_lore: ...
```

정의:
- `character_motivation`: 오늘 고양이가 왜 이 행동을 하는가
- `world_state_change`: 영상이 끝난 뒤 작은 세계에서 무엇이 달라졌는가
- `callback_or_new_lore`: 기존 설정을 발전시키거나 새 설정 하나를 추가

같은 음식을 바꿔 끼우는 것만으로 새 에피소드로 인정하지 않는다.

## 7. 캐릭터 브랜딩 방향

경쟁 일본 AI 고양이 채널은 캐릭터에게 성격, 직업, 친구 관계, 생활 형편을 부여하고 굿즈/LINE 스탬프까지 확장한다.

우리도 익명 `고양이 앞발`보다 반복 기억되는 캐릭터로 발전시킨다.

초기 최소 설정:
- 작은 일본 마을의 초보 요리사
- 급하지만 정교한 손맛
- 완성 음식보다 이상한 부재료를 먼저 고르는 버릇
- 가게를 키우기 위한 작은 목표가 있음

이름은 첫 3편 데이터가 쌓이기 전까지 확정하지 않아도 되지만, 에피소드마다 성격/목적은 유지한다.

## 8. 수익화 전략 보강

2026년의 최우선 목표는 단순 광고 RPM이 아니라 **500-subscriber expanded YPP tier에 빨리 도달해 fan funding, Creator Partnerships, select Shopping 접근 가능성을 확보하는 것**이다.

현재 공식 기준:
- 500 subscribers + 최근 90일 공개 업로드 3개 + 3M valid/qualified Shorts views 또는 3,000 watch hours
- 광고/Premium 본격 진입은 1,000 subscribers + 10M Shorts views 또는 4,000 watch hours
- 2027-02-01 신규 광고/Premium 신청자는 20M Shorts views 또는 8,000 watch hours로 강화
- 2027-02-01 이후 Shorts Creator Pool 월 수익은 최근 90일 10M qualified Shorts views 유지가 필요

따라서 2026년 안에 `500-tier → 1,000/10M` 진입을 우선한다.

YouTube Shopping Affiliate는 한국과 일본이 지원 국가지만 YPP, subscriber threshold, 채널 성격 등 별도 조건을 충족해야 하므로 자동 활성화를 가정하지 않는다.

## 9. AI 공개

포토리얼한 Tiny Cat Kitchen은 실제로 발생하지 않은 현실적인 장면을 생성하므로 AI use disclosure를 기본 `Yes`로 유지한다.

YouTube 공식 안내상 이 공개 자체는 추천 노출이나 수익화 자격을 떨어뜨리지 않는다.

## 10. 탐색 → 승자 생산 루프

```text
cheap keyframes
→ 4 Lite generations
→ 35~38초 편집
→ 게시
→ retention / swipe / comments 분석
→ 승자만 5th generation 또는 hero Quality 승격
→ 다음 에피소드 manifest에 학습 반영
```

핵심 원칙:

> 실패 가능성이 높은 가설에는 40 credits만 쓴다. 증명된 포맷에만 추가 크레딧을 쓴다.
