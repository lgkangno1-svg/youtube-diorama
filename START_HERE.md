# Tiny Cat Kitchen — START HERE

목표: 사용자가 매번 주제·대본·Flow 프롬프트를 고민하지 않고 **한 문장 → 준비 완료 → Flow에서 필요한 generation만 순차 생성 → 24h/72h 학습**을 반복한다.

## 작업 시작 전 가장 먼저

다른 AI/개발자가 중간에 수정했을 수 있으므로 이전 대화 기억을 최신 상태라고 가정하지 않는다.

1. 최신 `main` SHA와 최근 PR/commit 확인
2. **`PROJECT_HANDOFF.md`를 먼저 읽어 현재 개발 의도·완료 상태·NEXT 작업을 복구**
3. 아래 source of truth를 교차 확인
4. 충돌/회귀 위험을 확인한 뒤에만 수정 시작

## 사용자가 평소 말할 것

```text
다음 영상 준비해줘
```

소재를 직접 정하고 싶을 때만:

```text
이번엔 미니 라멘으로 만들어줘
```

그 외의 조사·선정·대본·Flow 설계·기록은 시스템이 담당한다.

## Source of truth

- `PROJECT_HANDOFF.md` — **개발 의도 / 목표 / 현재 완료 상태 / 앞으로의 플랜 / 인수인계 change log**
- `CURRENT_STANDARD.md` — 최신 production 기준
- `docs/22_continuous_episode_learning_engine.md` — 연구/학습 루프
- `docs/23_minimum_credit_operator_architecture.md` — 최소 조작/크레딧 구조
- `docs/24_hero_cat_brand_identity.md` — 고양이/주방 identity
- `docs/25_pov_paws_microworld_grammar.md` — **Shorts 1인칭 앞발-only / 초소형 scale 문법**
- `docs/26_flow_ui_mode_preflight.md` — **Flow 새 생성 vs 기존 영상 수정 상태 / 모델·길이·비용 preflight**
- `docs/27_research_evidence_saturation_gate.md` — research no-churn / evidence saturation
- `research/benchmark_log.csv` — 성공 메커니즘 기억
- `ideas/episode_backlog.yaml` — 후보와 점수
- `analytics/learning_ledger.csv` — 실제 제작비/성과/학습
- `production/NEXT_EPISODE.txt` — 지금 만들 episode

## Tiny Cat Kitchen의 영상은 이렇게 보여야 함

> **시청자가 고양이가 된 것처럼 작업대를 내려다본다. 화면 아래에는 앞발만 보이고, 발보다 훨씬 작은 5~20mm 음식/물건을 조심스럽게 만든다.**

반드시:
- true first-person cat POV
- cream + pale ginger 앞발 1~2개만 등장
- 얼굴/머리/몸통/full cat 금지
- hero object가 한 앞발 폭의 절반 이하로 보임
- macro miniature diorama
- 고양이 발은 nudge / press / roll / slide / tap 위주
- human fingers/thumbs/grip 금지

예쁘더라도 다음이면 FAIL:
- 고양이가 카운터 뒤에 서서 요리함
- 정면에서 고양이를 바라보는 third-person shot
- 음식/팬이 paw와 비슷하거나 더 큼
- full kitchen establishing shot 때문에 tiny scale가 안 읽힘

## ChatGPT가 `다음 영상 준비해줘`를 받으면

- 최신 일본/글로벌 AI-cat / miniature / ASMR / relaxing Shorts 확인
- 앞으로 2~6주 일본 시즌/기념일/제철 신호 확인
- 경쟁작을 복제하지 않고 성공 원리만 추출
- production/24h/72h 기록 확인
- POV paw-only와 tiny-scale에 맞는 후보만 우선
- 최근 fingerprint 중복 제거
- 다음 episode 선택
- H30 vs H40 runtime gate 선택
- 일본어 title/hook
- narration 필요 여부
- episode manifest 생성/수정
- `production/NEXT_EPISODE.txt` 갱신
- **material repo 변경이 있으면 `PROJECT_HANDOFF.md`도 같은 branch/PR에서 갱신**

후보만 확인:

```powershell
python tools/select_next_episode.py --top 3
```

## 사용자가 로컬에서 하는 일

```powershell
./tools/make_next_short.ps1
```

자동 생성:
- `generated/TK-XXX_bundle.md`
- `generated/TK-XXX_flow_pack.md`
- `generated/TK-XXX_edit_plan.md`
- `generated/TK-XXX_publish_pack.md`

이 단계는 Flow/LLM/API 크레딧을 쓰지 않는다.

## Gate A — 무료 frame 먼저

영상 생성 전에 opening/target frame을 검수한다.

체크:
- 1인칭인가?
- 앞발만 보이는가?
- 얼굴/몸통이 안 보이는가?
- object가 paw보다 압도적으로 작은가?
- human fingers/thumbs가 없는가?
- 첫 1초에 "너무 작아서 귀엽다"가 읽히는가?

하나라도 구조적으로 틀리면 Flow video를 만들지 않는다.

## Flow 기본 설정

생성 직전 실제 UI에서 확인:

```text
새 영상 generation 상태
Veo 3.1 Lite
9:16
8 seconds 또는 현재 mode가 8s-only임을 확인
output count = 1
표시 비용 = 현재 공식표/실제 UI와 일치
```

**기존 영상을 열어둔 수정 화면은 G1/G2/G3 생성 화면이 아니다.** `수정 사항 설명` 계열 입력창이나 `Omni Flash` video-edit 상태가 보이면 먼저 standard 새 동영상 generation 화면으로 돌아간다. 현재 공식 Flow 문서상 Omni Flash video edit는 Veo Lite 생성보다 훨씬 비싸므로, 이를 10-credit G scene으로 착각하지 않는다.

4s/6s/8s selector가 안 보인다고 바로 오류로 판단하지 않는다. Veo Lite의 Ingredients/References-to-Video와 Extend는 8s-only일 수 있고, 기존 영상 edit 상태에서도 UI가 다르게 보일 수 있다. **duration selector 자체보다 active model + generation mode + output count + displayed cost 확인을 우선한다.** 자세한 절차는 `docs/26_flow_ui_mode_preflight.md`.

## Runtime / credit 선택

### compact_h30

```text
G1 8s = 10
PASS → G2 = +10
PASS → G3 = +10
first-pass ceiling = 30 credits
final ≈ 30~36s
```

3개 독립 beat로 완결될 때 사용.

### immersive_h40

```text
G1 → G2 → G3 모두 PASS
독립적인 4번째 world-resolution beat가 있을 때만 G4 = +10
first-pass ceiling = 40 credits
final ≈ 38~46s
```

4번째 scene은 길이 패딩이 아니라 작은 세계의 여운/serving/resolution이어야 한다.

48~60초는 실제 retention 데이터가 지지하기 전에는 기본 목표가 아니다.

## Sequential Frame Chain

```text
FREE OPEN FRAME
↓
G1 8s
↓ actual last usable frame
G2
↓ actual last usable frame
G3
↓ actual last usable frame
G4 only if immersive_h40
```

새 generation마다 고양이 얼굴을 다시 설명하지 않는다. 직전 actual frame으로 POV/paw/scale를 이어간다.

## 한 8초 scene

> **1 calm tactile action + optional 1 micro-payoff**

좋은 동작:
- paw nudges a tiny cup
- paw presses a tiny dough ball
- paw rolls one tiny ingredient
- paw slides a miniature plate
- paw taps one garnish

나쁜 동작:
- paw grips chopsticks/tongs like a hand
- 여러 도구를 동시에 사용
- 준비→조리→완성→먹기 전부 한 번에

## 오디오

기본:

```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

영상은 좋은데 소리만 이상하면 영상 재생성 금지. 후편집 SFX로 교체한다.

## 생성 결과를 다시 보여줄 때

```text
G1 만들었어. 봐줘
```

영상/스크린샷만 첨부.

ChatGPT 판단:
- `PASS`
- `EDITABLE`
- `REROLL`
- `STOP`

구조적 실패 shorthand:
- `POV FAIL`
- `SCALE FAIL`
- `ANATOMY FAIL`
- `CAMERA FAIL`
- `PADDING FAIL`

## 업로드 후 학습

24h/72h에 가능한 범위에서 기록:
- Stayed to watch
- APV
- engaged views
- subscribers
- comments
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy failure
- failed action type
- usable motion seconds
- final duration

장기 목표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

특히 `30~36s compact_h30`과 `38~46s immersive_h40`을 비교해 실제 채널에 맞는 몰입 길이를 학습한다.

## Handoff persistence gate

repo를 실제로 수정하는 모든 material 작업은 `PROJECT_HANDOFF.md`를 같은 branch/PR에서 갱신해야 완료로 본다.

로컬 검증:

```powershell
python tools/validate_handoff_update.py --base origin/main
```

이 검사는 GitHub Actions를 필요로 하지 않는다.

최소 갱신 대상:
- 현재 개발 완료 상태
- 현재 제작 상태 / NEXT_EPISODE
- 새로 확정된 중요한 결정/실패/학습
- 다음 작업 우선순위
- change log

의미 있는 개선이 없어 repo를 NO-OP으로 유지한 회차는 handoff도 억지로 수정하지 않는다.

# 가장 간단한 실제 사용법

```text
1. ChatGPT: "다음 영상 준비해줘"
2. PowerShell: ./tools/make_next_short.ps1
3. Flow: 새 동영상 generation 상태인지 확인 → G1만 생성
4. ChatGPT: "G1 만들었어. 봐줘"
5. PASS일 때만 G2 → G3 → 필요하면 G4
6. 업로드 후 Studio 수치/스크린샷 공유
```

핵심:

> **고양이를 보여주는 영상이 아니라, 고양이의 앞발이 된 시점에서 믿기 어려울 만큼 작은 것을 만드는 경험을 판다.**
