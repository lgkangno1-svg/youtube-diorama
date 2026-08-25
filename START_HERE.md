# Tiny Cat Kitchen — START HERE

목표: 사용자가 매번 주제·대본·Flow 프롬프트를 고민하지 않고 **한 문장 → 준비 완료 → Flow에서 필요한 generation만 순차 생성 → 24h/72h 학습**을 반복한다.

## 사용자가 평소 말할 것은 원칙적으로 하나

```text
다음 영상 준비해줘.
```

소재를 직접 정하고 싶을 때만:

```text
이번엔 미니 라멘으로 만들어줘.
```

그 외의 조사·선정·대본·Flow 설계·기록은 시스템이 담당한다.

---

## 0. Source of truth

- `CURRENT_STANDARD.md` — 최신 production 기준
- `docs/22_continuous_episode_learning_engine.md` — 연구/학습 루프
- `docs/23_minimum_credit_operator_architecture.md` — 최소 조작/크레딧 구조
- `docs/24_hero_cat_brand_identity.md` — 고양이/주방 identity
- `research/benchmark_log.csv` — 성공 메커니즘 기억
- `ideas/episode_backlog.yaml` — 후보와 점수
- `analytics/learning_ledger.csv` — 실제 제작비/성과/학습
- `production/NEXT_EPISODE.txt` — 지금 만들 episode

---

## 1. ChatGPT가 먼저 하는 일

`다음 영상 준비해줘`를 받으면:
- 최근 일본/글로벌 AI cat / miniature / ASMR / relaxing Shorts 확인
- 일본 계절/문화/식품/소셜 신호 확인
- 경쟁작을 복제하지 않고 성공 원리만 추출
- 실제 production/24h/72h 기록 확인
- 후보 재점수화
- 최근 5편 fingerprint 중복 제거
- 다음 episode 1개 선택
- 일본어 title/hook
- narration 필요 여부
- 3개의 느린 8초 action 설계
- episode manifest 생성/수정
- `production/NEXT_EPISODE.txt` 갱신

후보만 보고 싶다면:

```powershell
python tools/select_next_episode.py --top 3
```

점수 1위가 자동 제작되는 것은 아니다. 최신 근거와 originality를 마지막으로 확인한다.

---

## 2. 로컬에서 사용자가 하는 일

준비가 끝난 뒤 Windows PowerShell에서:

```powershell
./tools/make_next_short.ps1
```

에피소드 번호를 외울 필요가 없다. 스크립트가 `production/NEXT_EPISODE.txt`를 읽는다.

자동 생성:
- `generated/TK-XXX_bundle.md`
- `generated/TK-XXX_flow_pack.md`
- `generated/TK-XXX_edit_plan.md`
- `generated/TK-XXX_publish_pack.md`

이 준비 단계는 Flow/LLM/API 크레딧을 쓰지 않는다.

---

## 3. Flow 크레딧 사용 전 — Gate A

먼저 무료 image/reference/keyframe을 확인한다.

현재 channel identity:
- `HERO_CAT_V1`: cream + pale ginger 고양이, 둥근 amber eyes, pink nose, beige linen apron
- 실제 feline paws, human fingers/thumbs 금지
- `KITCHEN_WORLD_V1`: 따뜻한 나무/도자기, 부드러운 자연광, 아늑한 일본풍 미니 주방

체크:
- hero cat 얼굴/털색/앞치마가 동일한가
- 인간 손가락/엄지가 생기지 않았는가
- 주방/팬/접시/음식 scale이 유지되는가
- 첫 1초에 무엇을 하는지 이해되는가
- 장면이 차분하고 단순한가

**identity나 anatomy가 틀리면 Veo를 생성하지 않는다.**

---

## 4. 기본 Flow 예산 — Progressive Spend H30

생성 직전 Flow UI에서 반드시 확인:

```text
Veo 3.1 Lite
9:16
8 seconds
output count = 1
10 credits / generation 표시
```

현재 Google AI Pro 기준 공식표와 UI가 위 조건일 때:

```text
G1 = 10 credits
PASS 후 G2 = +10
PASS 후 G3 = +10
first-pass max = 약 30 credits
```

**G1/G2/G3를 한꺼번에 만들지 않는다.**

- G1 실패 → G2/G3 금지
- G2 실패 → G3 금지
- 작은 timing/crop → 편집
- 구조적 identity/action 실패 → 해당 generation만 reroll 검토
- premise가 약함 → 추가 spend 중단

Flow 가격/기능은 바뀔 수 있으므로 실제 생성 직전 UI 표시값을 확인한다.

---

## 5. Sequential Frame Chain

기본 연속성:

```text
FREE OPEN FRAME
  ↓
G1 8s
  ↓ save actual last usable frame
G2 First frame
  ↓
G2 8s
  ↓ save actual last usable frame
G3 First frame
  ↓
G3 8s
```

새 generation마다 긴 텍스트로 같은 고양이를 다시 설명하는 것보다 **직전 실제 usable frame을 이어주는 것**을 우선한다.

한 8초 generation은:

> 1 calm primary action + optional 1 micro-beat

빠른 montage, 여러 utensil 동시 사용, 준비→완성까지 한 clip에 몰아넣는 방식은 피한다.

---

## 6. 오디오

기본:

```text
No narration
No generated music
Quiet room tone + isolated natural ASMR
```

Flow 오디오가 깨끗하면 사용한다. 영상은 좋은데 소리만 이상하면 **영상 재생성 금지**하고 후편집 SFX로 교체한다.

나레이션은 화면만으로 이해가 어렵거나 캐릭터/payoff가 실제로 좋아질 때만 일본어 0~2문장을 사용한다.

---

## 7. 최종 영상

기본 목표:
- 약 28~36초
- 움직임이 계속 있는 healing pacing
- 40초를 맞추려고 정지화면을 길게 늘리지 않음

리듬 예:

```text
0~1초      즉시 이해되는 hook
1~8초      느린 준비/행동
8~16초     변화/조리
16~24초    작은 위험/해결
24~30초    payoff
마지막      여운/작은 개그/세계관 변화
```

---

## 8. 생성 결과를 다시 보여줄 때

가장 간단하게:

```text
G1 만들었어. 봐줘.
```

영상/스크린샷만 첨부한다.

ChatGPT 판단:
- `PASS` → 다음 generation
- `EDITABLE` → regeneration 없이 편집으로 해결
- `REROLL` → 해당 scene만 수정
- `STOP` → 추가 credit 중단

---

## 9. 업로드 후 학습

24h/72h에 가능한 범위에서 기록:
- Stayed to watch
- APV
- engaged views
- subscribers
- comments
- actual Flow credits
- rerolls
- G1/G2/G3 first-pass success
- usable motion seconds
- continuity/failed action type
- audio kept/replaced

장기 목표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

성공한 음식 자체가 아니라 성공한 **hook/action/pacing/audio/ending mechanism**을 다음 episode에 반영한다.

---

# 가장 간단한 실제 사용법

```text
1. ChatGPT: "다음 영상 준비해줘"
2. PowerShell: ./tools/make_next_short.ps1
3. Flow: G1만 생성
4. ChatGPT: "G1 만들었어. 봐줘"
5. PASS일 때만 G2 → G3
6. 업로드 후 Studio 수치/스크린샷 공유
```

핵심:

> 사용자는 아이디어와 프롬프트를 관리하지 않는다. 시스템은 연구·기억·생산준비·비용통제·성과학습을 담당하고, 사용자는 생성 버튼과 최종 취향 판단에 집중한다.
