# Tiny Cat Kitchen — START HERE

이 프로젝트의 목표는 사용자가 매번 주제·대본·프롬프트를 고민하지 않고, **벤치마크 기반 아이디어 → 약 30 Flow credits의 힐링 Short → 24h/72h 학습 → 더 나은 다음 영상**을 반복하는 것이다.

## 사용자가 평소 입력할 말은 원칙적으로 1개

```text
다음 영상 만들어줘.
```

또는 소재를 지정하고 싶을 때만:

```text
이번엔 미니 라멘으로 만들어줘.
```

그 외의 아이디어 연구와 제작 설계는 시스템이 담당한다.

---

## 0. 아이디어는 성공 영상을 벤치마킹해서 ChatGPT가 먼저 만든다

기준 문서: `docs/22_continuous_episode_learning_engine.md`

기억 저장소:
- `research/benchmark_log.csv` — 잘된 영상에서 추출한 성공 메커니즘
- `ideas/episode_backlog.yaml` — 현재 제작 후보와 점수
- `analytics/learning_ledger.csv` — 실제 제작비/성과/학습 기록

ChatGPT가 담당:
- 최근 일본/글로벌 AI 고양이·미니어처 요리·ASMR·힐링 Shorts 벤치마킹
- 일본 계절/문화/식품/소셜 트렌드 확인
- 경쟁 영상의 주제를 복사하지 않고 성공 원리만 추출
- episode 후보 생성 및 점수 갱신
- 최근 5편과 originality fingerprint 비교
- 다음 episode 1개 선택
- 일본어 title / hook
- goal / conflict / resolution
- 기본 무나레이션 여부 결정
- 필요할 때만 사용자가 녹음할 일본어 1~2문장 작성
- 3개의 느린 8초 힐링 동작 설계
- ASMR/SFX cue 설계
- episode YAML 생성/수정

후보 점수만 보고 싶다면:

```powershell
python tools/select_next_episode.py --top 3
```

단, 점수 1위가 자동 제작되는 것은 아니다. ChatGPT가 최신 근거와 최근 에피소드 중복을 마지막으로 확인한 뒤 manifest로 승격한다.

---

## 1. Episode 준비

ChatGPT가 GitHub의 `episodes/TK-XXX.yaml`을 준비한 뒤 Windows PowerShell에서:

```powershell
./tools/make_short.ps1 TK-XXX
```

또는:

```powershell
python tools/build_episode_bundle.py episodes/TK-XXX.yaml
```

이 명령은 LLM/API/Flow를 호출하지 않는다.

자동 생성:
- `generated/TK-XXX_bundle.md` — 사람이 볼 제작 카드
- `generated/TK-XXX_flow_pack.md` — Flow 복붙용 프롬프트
- `generated/TK-XXX_edit_plan.md` — 힐링 편집 타임라인
- `generated/TK-XXX_publish_pack.md` — YouTube 제목/설명/CTA/공개 체크

---

## 2. Flow 크레딧 사용 전

무료/저비용 이미지 단계에서 keyframe/contact sheet를 먼저 확인한다.

체크:
- 같은 주황색 고양이/흰 양말 앞발인가
- 인간 손가락/엄지가 없는가
- 주방, 팬, 접시 스케일이 유지되는가
- 첫 1초에 무엇을 하는 영상인지 이해되는가
- 장면이 너무 빠르거나 복잡하지 않은가

**이미지 단계에서 마음에 들지 않으면 Veo를 생성하지 않는다.**

---

## 3. 기본 Flow 예산 — H30

기본값:

```text
Veo 3.1 Lite
9:16
8 seconds
output count = 1
3 generations
```

비-Ultra 기본 목표:

```text
G1 = 10 credits
G2 = 10 credits
G3 또는 Extend = 10 credits
합계 = 약 30 credits
```

각 8초 generation은:
- 느린 핵심 행동 1개
- 필요하면 보조 beat 1개까지
- 2초마다 장면전환하는 montage 금지
- 힐링 pacing 유지

Flow 가격/기능은 변경될 수 있으므로 시스템이 공식 정보를 주기적으로 재검증하고, 실제 생성 직전 UI 표시 비용도 확인한다.

---

## 4. 오디오 기본 정책

기본값은 **무나레이션 + ASMR**.

Flow 생성 오디오는 깨끗하면 사용할 수 있지만 다음 문제가 있으면 버린다.
- 장면과 맞지 않는 소리
- 과한 음악
- 뒤섞인 효과음
- 순간적인 음색 변화
- Extend 접점에서 소리가 튐

재사용 SFX 예:
- tiny paw tap
- soft kitchen room tone
- tiny pan sizzle
- wooden spatula scrape
- ceramic click
- tiny chopping
- water pour
- rain ambience

나레이션은 영상 이해나 캐릭터성이 실제로 좋아질 때만 사용한다. 사용자가 직접 녹음하며 보통 일본어 1문장, 최대 2문장 정도만 사용한다.

---

## 5. 실패했을 때 전체 재생성부터 하지 않는다

```text
작은 타이밍/구도 문제
→ 편집으로 수리

한 장면의 고양이 발/스케일/행동이 구조적으로 잘못됨
→ 그 generation만 Lite 1회 reroll

같은 행동이 반복 실패
→ 프롬프트를 길게 만들지 말고 행동 단순화 / keyframe 수정

전체 premise가 약함
→ 추가 Flow 지출 중단
```

30 credits는 first-pass 목표 예산이지 반드시 다 써야 하는 최소치가 아니다.

---

## 6. 최종 영상

권장 길이:
- 약 28~36초
- 억지로 40초 이상 늘리지 않음

기본 리듬:

```text
0~1초      즉시 이해되는 hook visual
1~8초      느린 준비/행동
8~16초     조리/변화
16~24초    작은 위험/해결
24~30초    완성/보상
마지막      여운, 작은 개그 또는 세계관 변화
```

힐링은 정지화면이 많은 것이 아니라 **느린 움직임이 계속 존재하는 것**이다.

---

## 7. 업로드 후 학습

24시간과 72시간에 YouTube Studio 수치를 기록한다.

중요:
- Stayed to watch
- Average percentage viewed
- subscribers / 1,000 engaged views
- comments / 1,000 engaged views
- 실제 Flow credits / rerolls

```powershell
python tools/score_shorts_experiments_v2.py analytics/shorts_metrics_v2.csv
```

그리고 결과를 `analytics/learning_ledger.csv`에 누적한다.

학습 원칙:
- hook만 약함 → OPEN 원리만 수정
- 중간 retention 약함 → 중간 동작/위기 단순화
- retention 좋고 구독 약함 → 캐릭터/lore 강화
- 재생성률 높음 → 다음 아이디어에서 Flow 난이도 낮춤
- 모두 약함 → 해당 premise에 Flow 추가 지출 금지
- 성공 음식 자체를 복제하지 않고 **성공한 메커니즘**을 다음 아이디어에 반영

---

# 가장 간단한 실제 사용법

평소에는 ChatGPT에:

```text
다음 영상 만들어줘.
```

라고만 하면 된다.

ChatGPT가 벤치마킹 → 아이디어 선택 → episode package를 GitHub에 준비한다.

그 뒤 사용자는:

```powershell
./tools/make_short.ps1 TK-XXX
```

을 실행하고 생성된 bundle/Flow pack대로 **기본 3회의 Flow 생성**을 한다.

핵심 운영 원칙:

> AI는 연구·창작·판단에 사용하고, 반복 문서 작업은 코드로 처리하며, Flow는 검증된 최종 motion에만 크레딧을 쓴다. 업로드 결과는 다시 기억해서 다음 영상의 아이디어와 제작 난이도를 개선한다.
