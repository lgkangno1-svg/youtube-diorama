# Zero-Waste Flow Factory — 5-Generation Production Protocol

작성 기준: 2026-08-24

## 이번 개선의 핵심

기존 6개 영상 생성 구조를 기본값으로 두지 않는다.

Google Flow 공식 기준:
- 비구독 사용자는 매일 50개의 무료 Flow credits를 받음
- Veo 3.1 Lite는 비-Ultra 10 credits / Ultra 5 credits per generation
- Flow credits는 request가 아니라 **generation 단위**로 차감됨
- 한 request가 2개 generation을 만들 수 있으므로 output 수를 반드시 확인해야 함
- Nano Banana 2 Lite는 Flow의 frame/ingredient 제작용 무료 기본 이미지 모델
- Veo 3.1 Lite는 4s/6s/8s 영상 및 First/First+Last frame, Ingredients/References, Extend에 활용 가능
- 모든 Veo 3.1 8초 영상 Extend는 Lite로 수행

따라서 첫 패스의 표준을 아래로 바꾼다.

> **무료 키프레임 → Lite 5 generation → 편집으로 38~40초 → 실패한 컷만 재생성**

비-Ultra 첫 패스 비용: 50 credits
Ultra 첫 패스 비용: 25 credits

무료 사용자도 하루 무료 크레딧 안에서 파일럿 1편의 전체 모션 테스트를 끝낼 수 있다.

---

## 1. 왜 45초 고정에서 38~40초로 줄이는가

Flow는 Lite 4초, 6초, 8초가 모두 generation당 같은 10 credits다.
짧은 클립을 만든다고 크레딧이 싸지지 않는다.

따라서 비용을 줄이는 가장 큰 레버는 `초 수`가 아니라 **generation 수**다.

기존:
- 6 × Lite = 60 credits

개선:
- 5 × Lite = 50 credits

약 17% 절감.

클리프행어 freeze 0.3~0.5초, 음식 Hero hold 0.5초, 오프닝 키프레임 재사용 1초 등을 편집에서 활용하면 별도 CTA/루프 영상 생성이 필요 없다.

영상이 꼭 45초일 필요가 없는 파일럿에서는 38~40초를 우선 테스트한다. 리텐션이 좋아지면 이후 45~60초 스토리형으로 확장한다.

---

## 2. Flow 실행 전 무료 Preflight

영상 생성 전에 Nano Banana 2 Lite로 다음 5장의 keyframe을 만든다.

1. OPEN — 고양이 앞발 + 제약 조건이 한 프레임에 보임
2. CONSTRAINT — 쌀 10알/계란 1방울/3cm 같은 숫자가 시각적으로 명확
3. DANGER — 실패 직전 상태
4. PAYOFF — 완성 음식
5. TWIST — 고양이의 예상 밖 선택 직전

검수 항목:
- 같은 털 무늬인가
- 같은 주방인가
- 도구 크기가 같은가
- 음식 크기가 유지되는가
- 인간 손가락이 없는가
- 첫 프레임이 음소거 상태에서도 이해되는가

하나라도 실패하면 동영상이 아니라 **무료 이미지 단계에서 수정**한다.

---

## 3. 5-Generation 표준 구조

### G1 — Hook
목표: 1초 안에 `고양이 + 비정상적 제약` 동시 인식.

### G2 — Constraint / Setup
목표: 재료나 규칙을 보여주고 다음 위험을 예고.

### G3 — Cliffhanger
목표: 가장 실패하기 쉬운 한 동작만 생성.

### G4 — Recovery / Final Risk
목표: 첫 위험 해결 후 마지막 성공 직전까지 이동.

### G5 — Payoff + Twist
목표: 완성 음식 공개 후 고양이의 예상 밖 선택까지 한 장면에서 해결.

CTA용 별도 영상은 만들지 않는다.
CTA는 G5 후반 VO/자막 위에 얹고 마지막 0.5~1초는 OPEN keyframe을 재사용해 루프한다.

---

## 4. Output Count 방어

Flow 공식 도움말은 하나의 request가 여러 generation을 만들 수 있다고 명시한다.

따라서 생성 전 체크리스트:
- output/generation 수: 1
- 모델: Lite
- 영상 비율: 9:16
- 필요한 경우에만 Ingredients/References
- 8초가 필요한 장면만 8초

`2 outputs로 후보를 한 번에 뽑기`는 금지한다.
A/B가 필요하면 첫 결과가 구조적으로 실패했을 때만 두 번째 generation을 사용한다.

---

## 5. 재생성 의사결정

### Lite 10 credits를 다시 쓰는 경우
- 캐릭터 해부학 오류
- 스케일 드리프트
- 핵심 행동이 전달되지 않음
- continuity가 깨짐

### Gemini Omni Flash edit 40 credits를 고려할 경우
클립의 90%가 매우 좋고 한 부분만 수정하면 살릴 수 있으며, Lite 재생성을 여러 번 할 가능성이 높은 경우에만 고려.

기본값은 여전히 Lite 재생성이다.

### Quality 100 credits 사용 조건
- Lite/Fast로 대체가 불가능한 핵심 Hero Shot
- 썸네일/브랜드 대표 장면으로 장기간 재사용할 자산

Quality는 탐색 모델이 아니라 **승격 모델**이다.

---

## 6. Extend 사용 규칙

8초 Veo 3.1 영상은 Lite로 Extend할 수 있다.

Extend는 독립 생성보다 연속성 유지에 유리할 수 있으므로 다음 상황에서 A/B 테스트한다.
- 같은 주방에서 하나의 행동이 이어지는 장면
- 카메라와 조명을 절대 바꾸고 싶지 않을 때
- 캐릭터 외형 드리프트가 독립 생성에서 반복될 때

단, Extend 역시 generation 비용이 있으므로 **비용 절감 목적이 아니라 재생성률 감소 목적**으로만 사용한다.

---

## 7. 수익화 목표 재정렬

### 현재 2026년
확대 YPP 조기 진입:
- 500 subscribers
- 최근 90일 공개 업로드 3개
- 3M qualified Shorts views / 90 days 또는 3,000 qualified watch hours

이 단계에서 가능한 주요 기능은 fan funding 및 일부 Shopping 기능이며, 자체 상품 홍보가 포함될 수 있다.

광고/Premium 진입:
- 1,000 subscribers
- 10M qualified public Shorts views / 90 days 또는 4,000 qualified watch hours

### 2027-02-01부터 신규 광고/Premium 진입
- 1,000 subscribers 유지
- 20M qualified Shorts views / 90 days 또는 8,000 qualified watch hours

따라서 2026년의 핵심 사업 KPI:
1. 500 + 3M으로 확대 YPP 진입
2. 1,000 + 10M으로 광고/Premium 진입을 가능한 한 앞당김

### Shopping 주의
`500명 달성 = 즉시 타 브랜드 Affiliate 수익`으로 가정하지 않는다.
타 브랜드 YouTube Shopping Affiliate는 YPP 가입, 구독자 기준, 국가, 채널 성격 등 별도 자격이 있으며 Studio에서 실제 참여 가능 여부를 확인해야 한다.
한국과 일본은 현재 지원 국가에 포함된다.

초기 현금화 우선순위:
1. YPP 이전에도 가능한 합법적 직접 브랜드 협업 기회 탐색
2. 500-tier 진입 후 Super Thanks/멤버십/자체상품 등 실제 활성화된 기능 활용
3. Studio에서 Shopping Affiliate 자격이 열리면 미니 주방/가젯 에피소드와 연결
4. 1,000 + 10M 광고/Premium

---

## 8. AI 채널의 원본성 방어

YouTube의 `inauthentic content` 정책은 자동화 자체를 금지하지 않는다.
문제는 최종 영상이 대량생산·반복·상호교환 가능한 콘텐츠처럼 보이는 경우다.

모든 episode manifest에 아래 세 필드를 강제한다.

```yaml
originality_guard:
  unique_goal: ...
  unique_conflict: ...
  unique_ending: ...
```

추가 룰:
- 같은 conflict + ending 조합을 다음 5편 안에 재사용 금지
- 음식만 바꾸고 동일 컷 순서/동일 반전을 반복 금지
- 5편 중 최소 1편은 순수 조리형이 아닌 세계관형
- 5편 중 최소 1편은 가젯/도구형
- 5편 중 최소 1편은 댓글 결과를 실제 다음 사건에 반영

YouTube는 AI를 사용해 만든 고유 캐릭터와 서사가 창작자의 독창성을 보여주는 경우 수익화 가능한 예시로 안내한다.

---

## 9. AI 공개

포토리얼한 Tiny Cat Kitchen은 실제로 발생하지 않은 사실적인 장면을 AI로 생성하므로 YouTube Studio의 AI use disclosure를 `Yes`로 처리하는 것을 기본값으로 둔다.

공개 자체는 추천 노출이나 수익화 자격을 제한하지 않는다고 YouTube가 명시한다.

---

## 10. 사용자 수작업 최소화

사용자가 매 영상 직접 해야 할 일은 최종적으로 아래 3개만 남긴다.

1. 오늘 제작할 episode 선택
2. 실패 재생성 여부 또는 최종 A/B 선택
3. 업로드 승인

Codex/자동화가 처리할 것:
- manifest 생성
- keyframe prompt 생성
- 5개 Flow prompt 생성
- VO/SRT
- FFmpeg timeline
- metadata
- experiment log
- 업로드 후 지표 비교

Flow UI에서 반복 입력해야 하는 공통 reference/negative prompt는 프로젝트 단위 고정 자산으로 관리한다.

---

## 11. 현재 생산 기준

TK-001, TK-002, TK-003 모두 첫 패스 최대 5 Lite generations로 변경.

첫 테스트 순서:
1. TK-001 — 기본 캐릭터/리텐션 검증
2. TK-002 — 숫자 제약 훅 검증
3. TK-003 — 세계관형 검증

세 편의 비교가 끝날 때까지 30편 전체를 대량 생성하지 않는다.

이유:
> 실패 포맷 30편을 싸게 만드는 것보다, 승리 포맷 3개를 먼저 찾는 것이 가장 큰 비용 절감이다.
