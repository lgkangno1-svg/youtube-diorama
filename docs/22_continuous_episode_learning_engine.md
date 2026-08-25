# Continuous Episode Learning Engine

목표: **벤치마크 → 시즌 선행 신호 → POV paw-only 아이디어 → 저실패 Flow 제작 → 24h/72h 성과 → 다음 episode**가 한 저장소에서 누적되게 한다.

Source of truth:
- production: `CURRENT_STANDARD.md`
- operator/credits: `docs/23_minimum_credit_operator_architecture.md`
- character/world: `docs/24_hero_cat_brand_identity.md`
- Shorts framing/scale: `docs/25_pov_paws_microworld_grammar.md`
- candidates: `ideas/episode_backlog.yaml`
- learning: `analytics/learning_ledger.csv`

## 1. Research loop

매 회차:
1. 일본/글로벌 AI-cat, miniature, ASMR, relaxing-food, adjacent Shorts의 의미 있는 성공 메커니즘만 확인
2. 경쟁작의 제목/줄거리/브랜드/결말은 복제하지 않음
3. 앞으로 2~6주의 일본 시즌/기념일/제철/문화/소셜 신호를 선행 스캔
4. Flow 공식 가격/기능 재확인
5. 실제 Tiny Cat Kitchen production failures와 24h/72h performance 확인
6. 근거가 있을 때만 backlog/docs/tools/manifests 갱신

의미 있는 새 근거가 없으면 repo를 바꾸지 않는다.

## 2. Backlog scoring

`ideas/episode_backlog.yaml` 9축 base score:
- benchmark evidence 10
- Japan relevance 10
- healing fit 15
- visual satisfaction 15
- Flow reliability 20
- originality 10
- worldbuilding 5
- audience demand 5
- expected credit efficiency 10

계절형 후보에는 bounded `Seasonal Search Lead` boost를 최대 +8만 추가한다. `research/seasonal_evidence.yaml` 근거가 stale/missing이면 boost=0.

기본 seasonal timing prior:
- peak 22~35일 전: early lead
- peak 8~21일 전: strongest lead
- peak 0~7일 전: strong final lead
- peak 기간: valid but lower
- post-peak: small tail

달력만으로 production 우선순위를 올리지 않는다.

## 3. POV_PAWS_MICROWORLD production prior

기본 Shorts는 **고양이를 보는 영상이 아니라 고양이 자신의 1인칭 시점**이다.

후보가 다음에 적합할수록 production prior를 높인다.
- front paws only
- hero object 5~20mm 또는 화면상 paw width의 15~50%
- paw-to-object scale contrast가 첫 1초에 읽힘
- nudge / press / pat / roll / steady / slide / tap으로 만들 수 있음
- 한 8초 clip에 1 primary tactile action
- macro texture/steam/crack/gloss payoff가 있음

다음은 reliability prior를 낮춘다.
- third-person full-cat framing이 필요한 아이디어
- tongs/chopsticks/knife를 사람 손처럼 grip해야 함
- precise pinch/twist
- 다중 캐릭터/군중
- hero object가 커서 miniature 감각이 약함

## 4. Episode creation loop

사용자 입력:

```text
다음 영상 준비해줘
```

ChatGPT 처리:
1. benchmark + Japan seasonal signal 확인
2. production + analytics history 확인
3. backlog 재평가
4. 최근 5개 fingerprint 중복 제거
5. POV paw-only / tiny-scale 적합 후보 우선
6. H30 vs immersive H40 결정
7. episode manifest 생성/수정
8. `production/NEXT_EPISODE.txt` 갱신

## 5. Runtime learning — H30 vs H40

초기 prior:

```text
compact_h30
3×8s Lite raw motion
→ final 약 30~36s
→ 3개의 독립 beat로 완결

immersive_h40
4×8s Lite raw motion
→ final 약 38~46s
→ 4번째 beat가 world-resolution / serving / afterglow처럼 독립 가치가 있음
```

G4는 단순 runtime padding이면 금지한다. 48~60초는 실제 channel retention data가 지지할 때만 실험한다.

학습 목표는 "긴 게 좋은가"가 아니라:
- stayed-to-watch
- APV
- engaged views / credit
- subscribers / 100 credits

를 H30/H40에서 비교하는 것이다.

## 6. Progressive Spend

생성 직전 official Flow docs + 실제 UI를 확인한다.

현재 2026-08-25 운영 기준:
- Google AI Pro: 1,000 credits / billing cycle
- Veo 3.1 Lite 4/6/8s + Extend: non-Ultra 10 credits/generation
- output_count=1
- 1080p upscale: Plus/Pro/Ultra 0 credits

진행:

```text
FREE frame/reference preflight
→ G1 only
→ POV/SCALE/ANATOMY/QC
→ save actual last usable frame
→ G2 only after PASS
→ QC
→ G3 only after PASS
→ H30 complete if story is complete
→ G4 only if immersive_h40 and G3 PASS
```

## 7. Learning ledger

`analytics/learning_ledger.csv`에 가능한 경우 기록:
- idea origin / benchmark mechanic / hypothesis
- narration mode
- flow strategy + runtime mode
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV failure
- scale failure
- anatomy failure
- usable motion seconds
- continuity issue / failed action type
- audio replacement
- final runtime
- beat drop-off note
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

placeholder 0을 실패 데이터처럼 학습하지 않는다.

## 8. Current observed production lesson

2026-08-25 사용자 Flow test에서 **third-person full-cat + body visible + object scale too large**가 실제로 발생했다.

따라서 다음을 hard gate로 승격한다.
- true first-person camera
- front paws only
- hero object <= 0.50 paw width
- human-like tool grip 회피

이 실패는 음식 소재 문제로 보지 않는다. `camera/framing/scale/action grammar` 문제로 학습한다.

## 9. Long-term optimization

장기 지표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

성공한 음식 자체는 복제하지 않는다. 성공한 **scale hook / tactile action / pacing / ASMR / world-resolution mechanism**만 다음 episode prior에 반영한다.

최종 목표:

> **시청자가 고양이의 앞발이 된 듯한 시점에서 믿기 어려울 만큼 작은 세계를 조심스럽게 만드는 감각에 빠져드는 Shorts를 가장 적은 실패 generation으로 만든다.**
