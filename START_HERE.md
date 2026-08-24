# Tiny Cat Kitchen — START HERE

이 문서는 사용자가 매번 복잡한 프롬프트나 파일 구조를 기억하지 않고, **약 30 Flow credits를 기본 예산으로 고품질 힐링 Shorts 1편을 제작하는 표준 작업순서**다.

## 사용자에게 필요한 입력은 원칙적으로 1개

ChatGPT에게 다음처럼 말한다.

```text
다음 Tiny Cat Kitchen 영상 만들어줘.
```

또는 소재를 지정하고 싶으면:

```text
다음 영상은 미니 라멘으로 해줘.
```

ChatGPT가 담당할 것:
- 최근 일본 트렌드/기존 채널 데이터와 충돌 여부 판단
- episode goal / conflict / resolution 설계
- 일본어 title / hook
- 무나레이션 여부 결정
- 나레이션이 필요하면 사용자가 녹음할 짧은 일본어 대본 제시
- 3개의 8초 힐링 동작 설계
- ASMR/SFX cue 설계
- episode YAML 생성/수정
- 기존 최근 5편과 originality fingerprint 비교

반복 작업은 로컬 스크립트가 담당한다.

---

## 1. Episode 준비

ChatGPT가 GitHub의 `episodes/TK-XXX.yaml`을 준비한 뒤 Windows PowerShell에서:

```powershell
./tools/make_short.ps1 TK-001
```

또는 기존 Python 명령:

```powershell
python tools/build_episode_bundle.py episodes/TK-001.yaml
```

이 명령은 LLM/API/Flow를 호출하지 않는다.

자동 생성:
- `generated/TK-001_bundle.md` — 사람이 볼 제작 카드
- `generated/TK-001_flow_pack.md` — Flow 복붙용 프롬프트
- `generated/TK-001_edit_plan.md` — 힐링 편집 타임라인
- `generated/TK-001_publish_pack.md` — YouTube 제목/설명/CTA/공개 체크

---

## 2. Flow 크레딧 사용 전

먼저 무료/저비용 이미지 단계에서 keyframe/contact sheet를 확인한다.

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

비-Ultra 기본 예산:

```text
G1 = 10 credits
G2 = 10 credits
G3 또는 Extend = 10 credits
합계 = 30 credits
```

각 8초 generation은:
- 느린 핵심 행동 1개
- 필요하면 보조 beat 1개까지
- 2초마다 장면전환하는 montage 금지
- 힐링 pacing 유지

Flow 공식 비용은 바뀔 수 있으므로 생성 직전 Flow Settings에서 실제 비용을 확인한다.

---

## 4. 오디오 기본 정책

기본값은 **무나레이션 + ASMR**.

Flow 생성 오디오는 깨끗하면 사용할 수 있지만 다음 문제가 있으면 버린다.
- 장면과 맞지 않는 소리
- 과한 음악
- 뒤섞인 효과음
- 순간적인 음색 변화
- Extend 접점에서 소리가 튐

후편집 reusable SFX 예:
- tiny paw tap
- soft kitchen room tone
- tiny pan sizzle
- wooden spatula scrape
- ceramic click
- tiny chopping
- water pour
- rain ambience

나레이션은 영상 이해/캐릭터성이 실제로 좋아질 때만 사용한다.
사용자가 직접 녹음하며 보통 일본어 1~2문장만 사용한다.

---

## 5. 실패했을 때 절대 전체 재생성부터 하지 않는다

```text
작은 타이밍/구도 문제
→ 편집으로 수리

한 장면의 고양이 발/스케일/행동이 구조적으로 잘못됨
→ 그 generation만 Lite 1회 reroll

같은 행동이 반복 실패
→ 프롬프트를 길게 만들지 말고 행동을 단순화 / keyframe 수정

전체 premise가 약함
→ 추가 Flow 지출 중단
```

30 credits는 목표 예산이지 반드시 다 써야 하는 최소치가 아니다.

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

## 7. 업로드 후

24시간과 72시간에 YouTube Studio 수치를 기록한다.

중요:
- Stayed to watch
- Average percentage viewed
- subscribers / 1,000 engaged views
- comments / 1,000 engaged views

실행:

```powershell
python tools/score_shorts_experiments_v2.py analytics/shorts_metrics_v2.csv
```

결과에 따라 다음 편을 수정한다.

- hook만 약함 → OPEN만 변경
- 중간 retention 약함 → 중간 동작/위기만 변경
- retention 좋고 구독 약함 → 캐릭터/lore 강화
- 모두 약함 → 해당 premise에 Flow 추가 지출 금지

---

# 가장 간단한 실제 사용법

매번 사용자는 ChatGPT에 아래 둘 중 하나만 보내면 된다.

```text
다음 Tiny Cat Kitchen 영상 만들어줘.
```

또는

```text
이번엔 3cm 라멘으로 만들어줘.
```

ChatGPT가 episode package를 GitHub에 준비한 뒤, 사용자는:

```powershell
./tools/make_short.ps1 TK-XXX
```

을 실행하고 생성된 `generated/TK-XXX_bundle.md`와 `generated/TK-XXX_flow_pack.md`를 따라 Flow에서 **3번만 생성**하는 것을 기본 목표로 한다.

핵심 운영 원칙:

> AI는 창작과 판단에만 사용하고, 반복 문서 작업은 코드로 처리하며, Flow는 최종 motion에만 크레딧을 쓴다.
