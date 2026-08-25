# Continuous Episode Learning Engine

목표: 사용자가 매번 주제를 고민하거나 프롬프트를 다시 설계하지 않아도 **벤치마크 → 아이디어 → POV microworld 제작 → 업로드 → 24h/72h 성과학습 → 다음 아이디어**가 한 저장소에서 누적되도록 한다.

현재 production 기준은 `CURRENT_STANDARD.md`, 최소조작 기준은 `docs/23_minimum_credit_operator_architecture.md`, character/world는 `docs/24_hero_cat_brand_identity.md`, Shorts framing은 `docs/25_pov_paws_microworld_grammar.md`를 우선한다.

## 1. 역할 분리

### ChatGPT / research loop

담당:
- 최근 일본/글로벌 AI cat / miniature cooking / ASMR / relaxing Shorts 벤치마킹
- 성공 영상의 제목/줄거리/브랜드/결말을 복제하지 않고 성공 메커니즘만 추출
- 일본 계절/문화/식품/소셜 신호 확인
- 앞으로 2~6주의 seasonal opportunity 선행 스캔
- Tiny Cat Kitchen actual production 실패율과 24h/72h 성과 확인
- POV paw-only / scale-cuteness 적합 후보 우선
- 후보 생성/재평가/만료 처리
- 최근 5개 episode fingerprint와 중복 검토
- H30 vs H40 runtime gate 판단
- narration이 실제로 이득인지 episode별 판단
- episode YAML 작성/수정
- `production/NEXT_EPISODE.txt` 갱신

금지:
- 경쟁 영상 exact copy
- 조회수만 보고 포맷 복제
- 같은 tiny food만 바꾼 템플릿 생산
- Flow 크레딧 자동 사용
- 사용자 승인 없이 YouTube 게시

### deterministic tools

담당:
- backlog score 계산
- seasonal lead-time ranking
- current-standard validation
- originality validation
- Flow prompt pack
- healing edit plan
- publish pack
- metrics/credit-efficiency scoring

## 2. Benchmark Memory

`research/benchmark_log.csv`

가능한 범위에서 저장:
- 관측일 / 시장 / 출처
- 업로드일 / views / likes / comments / duration
- hook mechanic
- story mechanic
- dominant visual
- audio style
- pacing
- abstractable lesson
- `copy_forbidden=true`

핵심:

> 성공한 소재가 아니라 성공한 메커니즘을 기억한다.

Tiny Cat Kitchen에 특히 유용한 mechanic:
- immediate scale contrast
- tactile transformation
- macro texture payoff
- calm continuity
- tiny-world serving/resolution
- paws-as-scale-reference

## 3. Idea Backlog

`ideas/episode_backlog.yaml`이 9축 base score의 source of truth다.

현재 weights:
- benchmark evidence: 10
- Japan relevance: 10
- healing fit: 15
- visual satisfaction: 15
- Flow reliability: 20
- originality: 10
- worldbuilding: 5
- audience demand: 5
- expected credit efficiency: 10

각 후보 field는 0..20.

실제 제작 전 우선순위:
- POV first-person에서 자연스럽게 보이는가
- hero object를 5~20mm 수준으로 축소해도 읽히는가
- paw가 human-like grip 없이 조작 가능한가
- 한 8초에 하나의 tactile action으로 분해 가능한가
- endpoint/state change가 눈에 보이는가
- 직전 actual frame으로 continuity를 이어갈 수 있는가

싸게 만들 수 있다는 이유만으로 시각적 payoff가 약한 아이디어를 선택하지 않는다.

## 4. Seasonal Search Lead

계절성은 9축 base score를 덮어쓰지 않고 bounded timing boost로만 작동한다.

기본 prior:

```text
peak 36일+ 전   → 0
peak 22~35일 전 → early lead
peak 8~21일 전  → strongest lead
peak 0~7일 전   → strong final lead
peak 기간       → valid
post-peak tail  → small residual
```

`research/seasonal_evidence.yaml`의 최신 일본 근거가 stale/missing이면 seasonal boost를 0으로 처리한다.

달력 날짜만으로 제작하지 않는다.

## 5. Episode Creation Loop

사용자 기본 입력:

```text
다음 영상 준비해줘
```

ChatGPT 처리:
1. benchmark / current Japanese signal 확인
2. next 2~6 week seasonal scan
3. production + analytics history 확인
4. backlog 갱신
5. top candidates 비교
6. originality fingerprint 검토
7. `POV_PAWS_MICROWORLD_V1` 적합성 검토
8. scale-cuteness / paw-action reliability 검토
9. H30 vs H40 runtime gate 선택
10. HERO_CAT_V1_PAWS / KITCHEN_WORLD_V1 continuity 확인
11. episode YAML 생성/수정
12. narration decision
13. `production/NEXT_EPISODE.txt` 갱신

## 6. Visual Grammar Learning

기본 Shorts:

> true first-person cat POV + front paws only + absurdly tiny hero object + macro diorama + tactile ASMR

구조적 실패로 기록:
- `pov_failure`: third-person / 외부 observer camera
- `scale_failure`: object가 paw 대비 충분히 작아 보이지 않음
- `anatomy_failure`: fingers/thumbs/human grip
- `character_failure`: face/head/body/full cat reveal

좋은 paw action prior:
- nudge
- press
- pat
- roll
- steady
- slide
- tap

나쁜 prior:
- chopsticks/tongs/knife grip
- pinch
- wrist twist

반복 production data에서 특정 action의 failure rate가 높으면 아이디어 score의 Flow reliability prior를 낮춘다.

## 7. Production Loop — Progressive Spend

로컬:

```powershell
./tools/make_next_short.ps1
```

준비 단계는 Flow/LLM/API를 자동 호출하지 않는다.

생성 직전 실제 Flow UI를 확인한다.

현재 기본 settings:
- Veo 3.1 Lite
- 9:16
- 8 sec
- output_count=1
- displayed cost 확인

진행:

```text
free keyframe/reference preflight
→ G1 only
→ POV/SCALE/ANATOMY/QC
→ actual last usable frame
→ G2 after PASS
→ QC
→ G3 after PASS
→ QC
→ G4 only when immersive_h40 has independent fourth beat
```

## 8. Runtime Learning

초기 hypothesis:

### compact_h30
- 3×8s raw motion
- final 약 30~36s
- 3-beat complete process

### immersive_h40
- 4×8s raw motion
- final 약 38~46s
- 4번째 world-resolution / serving / afterglow beat가 실제 가치가 있을 때

48~60s는 초기 default가 아니다.

실제 데이터가 쌓이면 비교:
- runtime_mode
- final_length_seconds
- Stayed to watch
- APV
- engaged views / credit
- subscribers / 100 credits
- beat_dropoff_note

길이가 긴 쪽의 APV가 조금 낮더라도 engaged views/credit 또는 subscribers/credit가 좋아질 수 있으므로 한 지표만으로 결론내리지 않는다.

## 9. Learning Memory

`analytics/learning_ledger.csv`

기록 가능 항목:
- idea origin / benchmark mechanic / hypothesis
- narration mode
- flow strategy / runtime mode
- actual Flow credits
- rerolls
- G1/G2/G3/G4 first-pass success
- POV/scale/anatomy failure
- usable motion seconds
- continuity issue
- failed action type
- Flow audio replaced 여부
- final runtime
- beat drop-off note
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

placeholder 또는 관측 시간이 안 지난 0값을 실패 데이터처럼 학습하지 않는다.

장기 최적화:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

## 10. 학습 예

```text
paw-to-10mm-object scale reveal → STW strong
paddle grip attempt → anatomy reroll
```

다음:
- scale-reveal hook prior 유지/상향
- grip action은 press/slide로 변환
- 같은 음식/줄거리는 복제하지 않음

또는:

```text
38~44s immersive_h40 → APV slightly lower
but engaged views/credit + subscribers/credit higher
G4 world-resolution receives positive comments
```

다음:
- 4번째 beat가 독립적 worldbuilding 가치가 있는 episode에서 H40 prior 유지
- 단순 process에는 H30 유지

## 11. Continuous Research Loop

정기 연구:
1. 최신 성공/급상승 인접 콘텐츠 확인
2. 일본 최신 계절/음식/소셜 신호 확인
3. 앞으로 2~6주 seasonal lead 확인
4. Google Flow 공식 가격/기능 변경 확인
5. benchmark log에 의미 있는 메커니즘만 기록
6. backlog 후보 추가/재평가/만료
7. actual production learning과 모순 여부 확인
8. production standard를 바꿀 근거가 있을 때만 문서/도구 변경

의미 있는 새 근거나 운영 불일치가 없으면 repo를 수정하지 않는다.

## 12. 사용자 실제 인터페이스

평소에는:

```text
다음 영상 준비해줘
```

한 줄이면 된다.

사용자는 생성 결과를:

```text
G1 만들었어. 봐줘
```

라고 보내면 된다.

ChatGPT가 `PASS / EDITABLE / REROLL / STOP` 및 `POV FAIL / SCALE FAIL / ANATOMY FAIL / CAMERA FAIL / PADDING FAIL`로 판단한다.

장기 목표:

> 사용자는 최종 취향과 생성 버튼에 집중하고, 시스템은 일본 타이밍·아이디어·POV scale grammar·production cost·runtime·성과학습을 담당한다.
