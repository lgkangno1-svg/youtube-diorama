# Engaged-View Truth Layer — 2026-08-24 Shorts Analytics Change

작성 기준: 2026-08-24

## 왜 이 문서가 최우선인가

2026-08-24부터 YouTube는 Shorts를 포함한 모든 형식에서 **영상이 재생되기 시작하는 순간 public view를 카운트**한다.

하지만 YouTube 공식 도움말은 동시에 다음을 명확히 한다.

- YPP 수익은 Shorts의 `engaged views` 기준을 계속 사용
- YPP 자격은 `qualified Shorts views` 기준을 계속 사용
- `Engaged views`는 Shorts에서 시청자가 초기 몇 초를 넘겨 계속 본 횟수이며 loop는 제외
- `Stayed to watch`는 Shorts를 보고 남은 비율 vs swipe-away 비율
- Average view duration / average percentage viewed는 engaged views와 해당 watch time을 기반으로 계산

공식 출처:
- https://support.google.com/youtubecreatorstudio/answer/2991785
- https://support.google.com/youtubecreatorstudio/answer/12220281
- https://support.google.com/youtube/answer/72851

따라서 2026-08-24 이후에는 **public views를 바이럴 학습의 1순위 KPI로 사용하지 않는다.**

---

# 1. Tiny Cat Kitchen의 새로운 KPI 계층

## Tier A — 제작 의사결정 핵심

1. `Stayed to watch (%)`
   - 첫 1~3초의 swipe-stop 능력
   - 훅/첫 프레임/첫 움직임 판단

2. `Average percentage viewed (%)`
   - 시작 후 얼마나 끝까지 보는지
   - 영상 길이와 중간 사건 구조 판단

3. `Engaged views`
   - 실제로 초기 몇 초를 넘겨 본 핵심 Shorts 소비량
   - public views보다 YPP/실질 성과에 가까운 신호

4. `Subscribers gained per 1,000 engaged views`
   - 단순 시청이 아니라 IP 전환 능력

## Tier B — 보조

5. Likes per 1,000 engaged views
6. Comments per 1,000 engaged views
7. Shares per 1,000 engaged views (Studio export에서 확보 가능할 때)
8. Unique viewers / returning viewers
9. Shorts feed traffic share

## Tier C — 참고만

10. Public views

public views는 distribution 규모를 보는 참고치로만 사용한다.
2026-08-24 이전 데이터와 이후 데이터를 raw views 하나로 직접 비교하지 않는다.

---

# 2. 영상 진단 매트릭스

절대 임계값을 외부 채널에서 가져와 맹목적으로 적용하지 않는다. 같은 채널, 비슷한 길이, 최근 cohort 안에서 상대 비교한다.

## A. Stayed to watch 낮음 / APV 높음

해석:
- 들어온 사람은 잘 보는데 첫 1~3초에서 많은 사람이 넘김

수정 대상:
- 첫 프레임
- 훅 문장
- 첫 0.5초 행동
- 크기 대비
- 물체 위치

Flow 대응:
- 전체 4-generation 재생성 금지
- OPEN keyframe만 다시 만들거나 편집으로 첫 0.5~1초 재구성

## B. Stayed to watch 높음 / APV 낮음

해석:
- 클릭/멈춤은 잘 만들었지만 중간이 약함

수정 대상:
- 8~15초 갈등
- 15초 클리프행어
- 중간 반복 동작 삭제
- payoff 위치 앞당기기

Flow 대응:
- DANGER/PAYOFF 구간만 재설계

## C. Stayed to watch 높음 / APV 높음 / 구독 전환 낮음

해석:
- 영상은 좋지만 캐릭터/IP 기억성이 약함

수정 대상:
- 고양이의 반복 성격
- creator signature
- 다음 세계관 떡밥
- 같은 마을/가게의 누적 변화

## D. Stayed to watch 낮음 / APV 낮음

해석:
- 소재 또는 구조 가설 자체가 약할 가능성

대응:
- Flow 크레딧 추가 투입 금지
- 같은 음식의 Quality 승격 금지
- 새 훅 가설 또는 새 소재로 이동

---

# 3. 24h / 72h 판단 규칙

초기 숫자는 처리 지연이 있을 수 있으므로 게시 직후 몇 시간 데이터로 결론을 내리지 않는다.

### 24시간
- 첫 훅 진단
- Stayed to watch
- APV
- engaged views
- subs / 1k engaged

### 72시간
- 동일 길이 cohort 내 상대 순위
- 신규 vs 재방문 시청자
- traffic source
- 댓글 내용에서 다음 메뉴/캐릭터 요구

한 영상의 public view만 보고 24시간 안에 같은 포맷 5편을 추가 제작하지 않는다.

---

# 4. Aug 24 데이터 경계 규칙

2026-08-24 이전과 이후의 `views`는 정의가 달라질 수 있으므로 장기 시계열에서 한 열로 비교하지 않는다.

```text
pre_2026-08-24 public views
!=
post_2026-08-24 public views
```

비교가 필요하면 다음을 우선한다.

- engaged views
- Stayed to watch
- average percentage viewed
- subscribers per 1,000 engaged views

---

# 5. 최소 수동 입력 포맷

YouTube Studio에서 각 Short마다 아래 값만 복사하면 된다.

```csv
episode_id,published_at,public_views,engaged_views,stayed_to_watch_pct,avg_percentage_viewed_pct,likes,comments,subscribers_gained
TK-001,2026-08-25T12:00:00+09:00,0,0,0,0,0,0,0
```

이후 `tools/score_shorts_experiments.py`가 파생지표와 상대 순위를 계산한다.

---

# 6. 크레딧 절약과 직접 연결되는 의사결정

분석 목표는 '좋은 영상 찾기'가 아니라 **어느 부분만 고치면 되는지 찾기**다.

```text
Hook failure
→ OPEN keyframe / first-second edit only

Middle retention failure
→ DANGER/PAYOFF redesign only

IP conversion failure
→ creator signature / lore only

All weak
→ stop spending credits on that hypothesis
```

이 원칙으로 `40-credit prototype → 데이터 → 필요한 부분만 수정`을 유지한다.

---

# 7. 최근 경쟁 채널에서 얻는 운영 시사점

2026년 8월에도 Miniature Cooking Ideas는 높은 빈도로 업로드하며 대규모 일일 조회를 유지하지만, 최근 업로드 다수는 유사한 `Satisfying ASMR + Mini Food` 제목 구조를 반복한다. 반대로 일본의 오래된 Miniature Cooking 채널은 2024년 이후 신규 업로드가 멈춰 최근 30일 성장이 사실상 정체되어 있다.

우리의 차별점은 업로드 수를 따라가는 것이 아니다.

> **같은 미니요리 만족감을 유지하면서, 고양이 캐릭터의 목적·갈등·세계 상태 변화가 누적되는 IP형 Shorts를 적은 생성비로 테스트한다.**

참고:
- https://socialblade.com/youtube/handle/miniaturecookingideas
- https://digitalcreators.jp/channel/ja/UC9MuMVvvZhIWXTCeH4AKKEA/

---

# 최종 규칙

2026-08-24 이후 Tiny Cat Kitchen의 실험 승자는 `public views`가 아니라 아래 네 항목의 조합으로 판단한다.

1. Stayed to watch
2. Average percentage viewed
3. Engaged views
4. Subscribers per 1,000 engaged views

**조회수 카운트 방식이 바뀌어도, 우리가 최적화하는 것은 '재생 시작'이 아니라 '멈춰 보고, 끝까지 보고, 다시 보러 오는 사람'이다.**
