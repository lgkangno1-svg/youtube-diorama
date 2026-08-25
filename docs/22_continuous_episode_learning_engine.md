# Continuous Episode Learning Engine

목표: 사용자가 매번 주제를 고민하거나 프롬프트를 다시 설계하지 않아도 **벤치마크 → 아이디어 → 저실패 Flow 제작 → 업로드 → 24h/72h 성과학습 → 다음 아이디어**가 한 저장소에서 누적되도록 한다.

현재 production 기준은 `CURRENT_STANDARD.md`, 최소조작 기준은 `docs/23_minimum_credit_operator_architecture.md`, 캐릭터 identity는 `docs/24_hero_cat_brand_identity.md`를 우선한다.

## 1. 역할 분리

### ChatGPT / research loop
담당:
- 최근 일본/글로벌 AI cat / miniature cooking / ASMR / relaxing Shorts 벤치마킹
- 성공 영상의 주제를 복사하지 않고 성공 메커니즘만 추출
- 일본 계절/문화/식품/편의점/소셜 신호 확인
- 실제 Tiny Cat Kitchen 제작 실패율과 24h/72h 성과 확인
- 후보 생성/재평가/만료 처리
- 최근 5개 episode fingerprint와 중복 검토
- narration이 실제로 이득인지 episode별 판단
- episode YAML 작성/수정
- `production/NEXT_EPISODE.txt` 갱신

금지:
- 경쟁 영상의 제목/줄거리/브랜드/결말 그대로 복제
- 조회수만 보고 포맷 복제
- 같은 고양이 + 음식명만 바꾸는 템플릿 생산
- Flow 크레딧 자동 사용
- 사용자 승인 없이 YouTube 게시

### 로컬 deterministic tools
담당:
- backlog score 계산
- originality validation
- Flow prompt pack
- healing edit plan
- publish pack
- metrics/credit-efficiency scoring

반복 문서 작성에 LLM/API 비용을 쓰지 않는다.

---

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

핵심 규칙:

> 성공한 소재가 아니라 성공한 메커니즘을 기억한다.

예:
- 특정 브랜드의 고양이 식당을 복사하지 않는다.
- `recognizable role → instantly understood tiny-world situation`을 추출한다.
- 특정 상품의 디자인을 복사하지 않는다.
- `texture transformation → satisfying payoff`만 학습한다.

---

## 3. Idea Backlog — 현재 9축 scoring

`ideas/episode_backlog.yaml`이 점수의 source of truth다.

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

각 후보 field score는 0..20이며 가중 합산한다.

특히 실제 제작 전에는 **Flow reliability + expected credit efficiency**를 중요하게 본다. 같은 수준의 아이디어라면 다음 특성이 유리하다.
- 주인공 1마리
- 핵심 소품/음식 상태가 적음
- 한 8초 clip에 한 primary action
- 상태 변화가 눈에 보임
- 복잡한 군중/다중 캐릭터/빠른 변신 없음
- 실제 previous generation frame으로 continuity를 이어갈 수 있음

단, 싸게 만들 수 있다는 이유만으로 시각적 payoff가 약한 아이디어를 선택하지 않는다.

점수 확인:

```powershell
python tools/select_next_episode.py --top 3
```

점수 1위는 자동 제작 명령이 아니다. 최신 일본 신호, 최근 5편 fingerprint, 실제 production history를 마지막으로 확인한 뒤 manifest로 승격한다.

---

## 4. Episode Creation Loop

사용자 기본 입력:

```text
다음 영상 준비해줘.
```

ChatGPT 처리:
1. benchmark log / current Japanese signal 확인
2. production + analytics history 확인
3. backlog 갱신
4. top candidates 비교
5. originality fingerprint 검토
6. 가장 좋은 후보 1개 선택
7. HERO_CAT_V1 / KITCHEN_WORLD_V1 continuity 확인
8. episode YAML 생성/수정
9. narration decision
10. Progressive Spend H30 기준 장면 설계
11. `production/NEXT_EPISODE.txt` 갱신

사용자가 소재를 지정하면 후보로 넣되, Flow reliability나 originality가 낮으면 더 안전한 변형안을 사용한다.

---

## 5. Production Loop — Progressive Spend

로컬에서:

```powershell
./tools/make_next_short.ps1
```

이 명령은 현재 `production/NEXT_EPISODE.txt`를 읽어 필요한 bundle / Flow pack / edit plan / publish pack을 만든다. Flow/LLM/API를 자동 호출하지 않는다.

현재 Google AI Pro 운영 기준은 생성 직전 공식 문서와 실제 Flow UI를 재확인한다. 현재 기본값:
- Veo 3.1 Lite
- 9:16
- 8 sec
- output_count=1
- 10 credits/generation when UI confirms it
- Plus/Pro/Ultra 1080p upscale 0 credits

진행 순서:

```text
free keyframe/reference preflight
→ G1 only
→ QC
→ save actual last usable frame
→ G2 only after PASS
→ QC
→ save actual last usable frame
→ G3 only if still needed
```

30 credits는 first-pass target이지 선결제 quota가 아니다. G1이 실패하면 뒤의 20 credits를 쓰지 않는다.

---

## 6. Brand / Character Continuity

캐릭터 source of truth:

`docs/24_hero_cat_brand_identity.md`

현재 기본은 `HERO_CAT_V1` + `KITCHEN_WORLD_V1`이다.

Identity failure는 구조적 실패로 취급한다.
- 다른 털색/얼굴 비율
- apron identity 소실
- human hand/finger anatomy
- 주방 material/light language의 큰 drift

음식 디테일이 좋아도 hero identity가 무너지면 다음 generation으로 진행하지 않는다.

G2/G3에서는 길어진 텍스트로 캐릭터를 다시 설명하기보다 직전 실제 usable frame을 First frame으로 사용하는 것을 우선한다.

---

## 7. Learning Memory

`analytics/learning_ledger.csv`

가능한 경우 기록:
- idea origin / benchmark mechanic / hypothesis
- narration mode
- actual Flow credits
- rerolls
- G1/G2/G3 first-pass success
- usable motion seconds
- continuity failure type
- failed action type
- Flow audio kept/replaced
- final runtime
- 24h/72h Stayed to watch
- APV
- engaged views
- subscribers
- comments

placeholder 또는 아직 관측 시간이 안 지난 0값을 실패 데이터처럼 학습하지 않는다.

장기 최적화 지표:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

조회수 하나만으로 production prior를 변경하지 않는다.

---

## 8. 학습 규칙

예:

```text
opening scale reveal → STW strong
middle wrapping action → APV drop + reroll
```

다음 학습:
- scale-reveal hook 원리는 유지
- wrapping을 더 단순한 action으로 교체
- 같은 음식/줄거리 자체는 복제하지 않음

또는:

```text
one-paw liquid pour → first-pass success high
steam payoff → comments/APV good
```

다음 아이디어에서 해당 **production mechanic**의 prior를 높인다.

실제 데이터가 충분하지 않으면 점수를 과도하게 변경하지 않는다.

---

## 9. Continuous Research Loop

정기 연구는:
1. 최신 성공/급상승 인접 콘텐츠 확인
2. 일본 최신 계절/음식/소셜 신호 확인
3. Google Flow 공식 가격/기능 변경 확인
4. benchmark log에 의미 있는 메커니즘만 기록
5. backlog 후보 추가/재평가/만료
6. analytics learning과 모순 여부 확인
7. production standard를 바꿀 근거가 있을 때만 문서/도구 변경

**의미 있는 새 근거나 운영 불일치가 없으면 repo를 수정하지 않는다.**

---

## 10. 콘텐츠 포트폴리오

한 종류만 반복하지 않는다.

추천 rotation:

```text
A. miniature cooking satisfaction
B. cat job / tiny shop worldbuilding
C. numerical or physical experiment
D. Japanese seasonal/trend injection
E. quiet daily-life / emotional episode
F. audience-selected candidate
```

같은 conflict + ending family를 연속 반복하지 않는다.

---

## 11. 사용자 실제 인터페이스

평소에는:

```text
다음 영상 준비해줘.
```

한 줄이면 된다.

ChatGPT가 조사/선정/manifest/NEXT_EPISODE까지 준비하고, 사용자는 로컬에서:

```powershell
./tools/make_next_short.ps1
```

만 실행한다.

그 뒤 Flow에서는 G1을 먼저 만들고 결과를 공유한다. ChatGPT가 `PASS / EDITABLE / REROLL / STOP`으로 판단한 뒤 다음 spend를 결정한다.

장기 목표:

> 사용자는 취향과 최종 품질 판단만 하고, 시스템이 연구·기억·생산준비·비용통제·성과학습을 담당한다.
