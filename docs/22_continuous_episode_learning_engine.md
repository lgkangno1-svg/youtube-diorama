# Continuous Episode Learning Engine

목표: 사용자가 매번 주제를 고민하거나 프롬프트를 다시 설계하지 않아도 **벤치마크 → 아이디어 → Flow 제작 → 업로드 → 성과학습 → 다음 아이디어**가 한 저장소에서 누적되도록 한다.

## 1. 역할 분리

### ChatGPT / research loop
담당:
- 최근 일본/글로벌 성공 Shorts 벤치마킹
- 성공한 영상의 주제 그 자체가 아니라 `왜 먹혔는지`를 구조로 추출
- 일본 계절/문화/식품/편의점/소셜 트렌드 확인
- 새로운 Tiny Cat Kitchen episode 후보 작성
- 최근 5개 episode fingerprint와 중복 검토
- narration이 실제로 이득인지 episode별 판단
- 새 episode YAML 작성
- 업로드 후 24h/72h 데이터를 보고 다음 가설 개선

금지:
- 경쟁 영상의 제목/줄거리/브랜드/결말 그대로 복제
- 조회수만 보고 포맷 복제
- 같은 고양이 + 음식명만 바꾸는 템플릿 생산
- Flow 크레딧 자동 사용
- 사용자 승인 없이 YouTube 게시

### 로컬 deterministic tools
담당:
- benchmark-derived backlog 점수 계산
- originality validation
- Flow prompt pack
- healing edit plan
- publish pack
- metrics scoring

반복 문서 작성에 LLM 토큰을 쓰지 않는다.

---

## 2. Benchmark Memory

`research/benchmark_log.csv`

한 성공 사례마다 다음을 저장한다.
- 관측일
- 시장
- 채널/출처
- 영상/주제
- 업로드일
- views / likes / comments / duration (확인 가능 범위)
- hook mechanic
- story mechanic
- dominant visual
- audio style
- pacing
- `abstractable_lesson`
- `copy_forbidden=true`

핵심 규칙:

> 주제를 복사하지 않고 성공 메커니즘만 기억한다.

예:
- `고양이 햄버거 가게 직원`을 그대로 만들지 않는다.
- 대신 `recognizable role → instantly understood tiny-world situation`을 학습한다.
- `M&M cake`를 그대로 만들지 않는다.
- 대신 `progressive colorful transformation → satisfying payoff`를 학습한다.

---

## 3. Idea Backlog

`ideas/episode_backlog.yaml`

후보별 최대 100점 방향:
- benchmark evidence: 20
- Japan relevance: 15
- healing fit: 20
- Flow efficiency: 20
- originality: 15
- worldbuilding: 10

Flow efficiency가 높은 아이디어:
- 주인공 1마리
- 핵심 소품 1~3개
- 8초마다 이해 가능한 느린 행동 1개
- 상태 변화가 눈에 보임
- 복잡한 군중/다중 캐릭터/빠른 변신 없음

점수 확인:

```powershell
python tools/select_next_episode.py --top 3
```

이 결과는 자동 제작 명령이 아니다. 최종 후보는 ChatGPT가 최근 5편의 fingerprint와 실제 최신 trend evidence를 다시 확인한 뒤 manifest로 승격한다.

---

## 4. Episode Creation Loop

사용자 기본 입력:

```text
다음 영상 만들어줘.
```

ChatGPT 처리:
1. 최신 benchmark log 확인
2. 필요 시 최근 성공 영상/일본 트렌드 재조사
3. backlog 갱신
4. top candidates 비교
5. 최근 5 episode fingerprint 검토
6. 가장 좋은 후보 1개 선택
7. episode YAML 생성
8. narration decision
   - `none`: ASMR only
   - `optional_one_line`: 캐릭터/IP 효과가 명확할 때만 사용자 녹음용 일본어 1문장
   - 예외적으로 2문장까지
9. H30 기준 3개의 느린 8초 scene 설계

사용자가 주제를 지정하면 지정 주제를 후보로 넣되, 성공 가능성이 떨어지면 더 좋은 변형안을 먼저 제시한다.

---

## 5. Production Loop

episode manifest가 준비되면:

```powershell
./tools/make_short.ps1 TK-XXX
```

또는:

```powershell
python tools/build_episode_bundle.py episodes/TK-XXX.yaml
```

기본 Flow target:
- Veo 3.1 Lite
- 8 sec
- output_count=1
- 3 generations
- H30
- 기본 narration 없음
- ASMR는 생성본이 깨끗할 때만 유지, 아니면 reusable SFX로 교체

30 credits는 hard quota가 아니라 first-pass target이다.

---

## 6. Learning Memory

`analytics/learning_ledger.csv`

각 episode에 대해 기록:
- 어떤 benchmark mechanic에서 출발했는가
- 어떤 hypothesis였는가
- narration 유무
- 실제 Flow credits / rerolls
- 최종 길이
- 24h/72h 품질 지표
- 어떤 audience signal이 나왔는가
- 다음에 무엇을 유지/제거할 것인가

조회수 자체보다 다음을 우선 학습한다.
- Stayed to watch
- APV
- subscriber conversion
- comment/audience interaction
- Flow 재생성률

예:

```text
달걀 노른자 close-up → STW 높음
하지만 중간 조립에서 APV 하락
Flow reroll 0

학습:
opening visual은 유지
다음 영상은 조립 단계를 더 단순화
노른자 소재 자체를 복제하지 말 것
```

즉 **승리한 소재가 아니라 승리한 원리를 누적한다.**

---

## 7. Continuous Research Loop

자동 연구 루프는 정기적으로:
1. 같은 장르 성공/급상승 사례 확인
2. 일본 최근 문화/계절/음식/소셜 신호 확인
3. benchmark log에 의미 있는 새 메커니즘만 기록
4. backlog 후보를 추가/재평가
5. 만료된 trend candidate 제거 또는 evergreen으로 재설계
6. 기존 analytics learning과 모순되는 제안을 내지 않음
7. production standard를 변경할 정도의 근거가 있을 때만 CURRENT_STANDARD를 변경

무의미한 변화가 없으면 repo를 건드리지 않는다.

---

## 8. 현재 콘텐츠 포트폴리오 원칙

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

같은 resolution family, conflict, visual grammar를 연속 반복하지 않는다.

---

## 9. 사용자가 실제로 하는 일

평소:

```text
다음 영상 만들어줘.
```

이 한 줄이면 충분한 것을 목표로 한다.

ChatGPT가:
- 아이디어 조사
- 선택 이유
- 일본어 제목/hook
- 필요 시 녹음 대본
- episode YAML
- Flow 제작 설계

까지 준비한다.

사용자는:
1. Production Card 확인
2. Flow에서 기본 3회 생성
3. 생성 영상 공유 또는 편집
4. 업로드
5. 24h/72h Studio 수치 제공

만 수행한다.

장기 목표:

> 사람이 콘텐츠 공장을 운영하는 것이 아니라, 사람은 최종 취향/품질 판단만 하고 시스템이 연구·기억·생산준비·학습을 담당한다.
