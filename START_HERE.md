# Tiny Cat Kitchen — START HERE

목표: 사용자가 매번 주제·대본·Flow 프롬프트를 재구성하지 않고 **한 문장 → quality-first episode 준비 → Operator Card 한 장 → KF0/KF1 → 실제 PASS frame 기반 next target → 필요한 Veo generation만 순차 실행 → 실제 성과/제작시간 학습**을 반복한다.

## 작업 시작 전

1. 최신 `main` SHA와 최근 PR/commit 확인
2. `PROJECT_HANDOFF.md` 확인
3. `PRODUCT_CHARTER.md` 확인
4. `CURRENT_STANDARD.md`, docs/22/23/27, NEXT_EPISODE, current manifest, benchmark/backlog/ledger 교차 확인
5. 최신 explicit user direction + merged state가 오래된 대화/자동화/legacy enum보다 우선

문서 역할:
- `PROJECT_HANDOFF.md` = 현재 상태/결정/실패/다음 우선순위
- `PRODUCT_CHARTER.md` = 장기 목적/창작 정체성/개선 판단 기준
- `CURRENT_STANDARD.md` = 현재 실행 규칙
- episode manifest/ledger = 해당 영상 계획과 관측값

## 현재 우선순위

1. 영상/내용 퀄리티
2. viewer outcome / 채널 정체성
3. 제작 편의성·속도
4. paid-video reroll/credit 효율
5. free-image 비용 가드

Nano Banana는 사용자의 현재 Google 사용 환경에서 무료로 사용할 수 있다. 이미지 단계는 비용 방어보다 quality/continuity 도구로 적극 활용한다.

## 사용자가 평소 말할 것

```text
다음 영상 준비해줘
```

ChatGPT/repo가 준비해야 할 것:
- 소재/선택 이유/Japan fit
- runtime tier
- HOOK / TRANSFORMATION / SCALE PROOF / PAYOFF
- exact-order image/target prompts
- exact-order G prompts
- 한 장짜리 `production/<EPISODE>_OPERATOR_CARD.md`
- manifest + NEXT_EPISODE + material handoff sync

## 정상 사용자 경로

로컬:
```powershell
./tools/make_next_short.ps1
```

**PRIMARY RUNBOOK은 현재 episode의 Operator Card다.** Generated bundle/flow pack은 기술 참고/비상 fallback이다.

현재 TK-005:
```text
production/TK-005_OPERATOR_CARD.md
NOW = 가장 강한 KF0 scale-hook anchor 한 장 만들기
```

## Tiny Cat Kitchen 최신 정체성

> **Mini Forest처럼 아주 작은 음식/물건을 실제로 만드는 힐링 미니어처 영상에서 사람 손 자리만 고양이 앞발이 대신한다.**

필수:
- cream/pale-ginger feline front paws 1~2
- no face/head/body/full cat
- no human hands/fingers/thumbs
- no human-like feline grip
- hero object 보통 5–20mm, <=0.50 paw width
- handcrafted miniature realism
- process-first tactile making
- calm long take / close ASMR

카메라 기본: high-oblique maker view → top-down/side macro. Literal cat-eye first-person POV는 필수가 아니다. `POV_PAWS_MICROWORLD_V1`은 compatibility token이다.

## Content Quality Gate

Paid video 전에 episode가 다음을 명확히 보여야 한다.

1. **HOOK** — 첫 1–2초에 tiny + paws + making이 즉시 읽힘
2. **TRANSFORMATION** — 각 scene에 보이는 상태 변화가 있음
3. **SCALE PROOF** — paw/hero 크기 대비가 강하게 보임
4. **PAYOFF** — 끝까지 볼 이유가 되는 완성/steam/crack/gloss/serving 결과
5. **NOVELTY/JAPAN FIT** — 지금 만들 이유와 독창성이 있음

약한 항목이 있으면 장면 수를 늘리지 말고 premise/shot/action을 개선한다.

## Gate A — G1 전에 first pair만 준비

기본값:
```text
strong KF0 maker-view anchor
→ paws / scale / camera / props / lighting QC
→ KF1을 승인 KF0에서 파생
→ KF0/KF1 PASS
→ G1 only
```

**KF2/KF3를 G1 전에 미리 만들지 않는다.**

## Actual-frame target rebasing

Google Flow는 저장한 video frame을 future generation의 start/end frame으로 사용할 수 있다. 따라서 next target도 actual PASS footage에서 파생한다.

```text
G1 PASS
→ native Save frame
→ actual G1 frame에서 KF2 생성
→ G2 PASS
→ native Save frame
→ actual G2 frame에서 KF3 생성
→ G3
```

Manifest의 KF2/KF3/KF4 설명은 destination state다. 미리 생성해야 한다는 뜻이 아니다.

장점:
- actual paw/camera/scale/props/light를 그대로 이어감
- speculative KF와 real footage mismatch 감소
- time-to-first-valid-G1 단축
- 불필요한 사전 이미지 작업 감소

Adaptive H40의 optional KF4는 동일하게 actual G3 PASS frame에서만 파생한다.

## Paid Flow baseline

생성 직전 실제 UI 확인:
```text
Veo 3.1 Lite
9:16
8 seconds
output count = 1
displayed cost = current UI truth
```

Paid generation/publishing은 사용자 명시 행동 없이는 하지 않는다.

## Progressive Spend

```text
KF0/KF1 PASS
→ G1 only
→ quality QC
→ PASS: native Save frame
→ actual PASS frame에서 next target 생성
→ G2 only after G1 PASS
→ repeat for G3
→ G1-G3를 함께 보고 complete면 STOP
→ G4가 실제로 더 좋아질 때만 actual G3 frame에서 KF4 + optional G4
```

H30/H40는 first-pass paid tier이지 final runtime 약속이 아니다.
- compact_h30: 3×8s raw, 보통 24–27s final
- immersive_h40: 3 core beats + optional fourth candidate, 최대 4×8s raw

## 한 8초 scene

> **1 calm tactile primary action + optional 1 passive material payoff**

선호: `nudge / press / pat / roll / steady / slide / tap / push`.

피함: pinch / precise twist / human tool grip / 여러 active gesture / rapid montage.

## 결과 QC 우선순위

1. opening premise/scale readability
2. real miniature-making realism
3. natural paw anatomy/action
4. satisfying tactile transformation
5. continuity
6. calm but non-boring pacing
7. payoff strength

구조 FAIL: full cat/body, human anatomy, human-like grip, weak scale, maker-view collapse, major continuity drift.

## 오디오

기본:
```text
No narration
No generated music
Quiet room tone + close tiny ASMR
```

좋은 motion + 나쁜 audio면 video reroll보다 후편집 교체.

## Learning

실제 값만 기록:
- credits/rerolls/G-stage first-pass
- maker-view/character/scale/anatomy/continuity failures
- failed action / usable motion seconds / final runtime
- 24h/72h Stayed to watch / APV / engaged views / subscribers / comments
- preparation minutes
- manual interventions
- prompt corrections before G1
- time-to-first-valid-G1
- actual-frame rebasing 후 continuity correction/reroll 변화

장기 목표:
```text
higher content quality
+ higher engaged views / paid credit
+ higher subscribers / paid credit
+ lower preparation time / manual work
```
