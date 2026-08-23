# 72시간 성장·수익화·저크레딧 Loop Engineering 계획

작성 기준: 2026-08-24

## 목표 우선순위

1. 사용자 작업시간 최소화
2. Google Flow 크레딧 낭비 최소화
3. 영상 퀄리티와 캐릭터 일관성 최대화
4. 일본 10~20대의 Viewed vs Swiped Away / 완주율 / 재시청률 최대화
5. 500명 + 300만 Shorts 조회 기반 조기 YPP/Shopping 진입을 우선 목표로 설정
6. 1,000명 + 1,000만 Shorts 조회의 광고수익 조건도 병행
7. 2027-02-01 신규 YPP 광고/Premium 기준 강화 전에 가능한 한 빨리 채널 성장
8. 대량생산형 AI 채널처럼 보이지 않도록 각 에피소드에 고유한 사건·목적·결말을 부여

---

# 1. Google Flow 크레딧 절약 원칙

공식 비용 기준(변경 가능):
- Veo 3.1 Lite: 일반 10 credits / Ultra 5 credits per generation
- Veo 3.1 Fast: 일반 20 / Ultra 10
- Veo 3.1 Quality: 100
- Gemini Omni Flash 8초 생성: 25
- 생성 영상 수정: 40
- 유료 요금제 1080p upscale: 0

## 절대 원칙

> **Quality로 탐색하지 않는다. Lite로 구조를 찾고 Quality는 승격한다.**

45초 영상 6클립 기준:
- Lite 1회 통과: 일반 약 60 credits
- Fast 1회 통과: 약 120
- Quality 전체: 약 600
- 5 Lite + Hero 1 Quality: 약 150

따라서 Quality 전체 생성은 금지한다.

## 권장 3단계 생성

### PASS A — PREVIS
- 대본/스토리보드/카메라 구도를 텍스트와 정지 이미지로 먼저 확정
- 영상 생성 전에 장면별 `시작 프레임`, `끝 프레임`, `행동 1개`를 확정
- 한 장면에 행동을 2~3개 넣지 않음

### PASS B — MOTION TEST
- Veo 3.1 Lite
- 출력 1개만 생성
- 각 장면 8초 생성 후 편집에서 필요한 5~7초만 사용
- 목적: 고양이 발 해부학, 크기, 도구, 카메라, 물리 확인

### PASS C — SELECTIVE UPGRADE
다음 경우에만 재생성:
1. 사람 손가락이 생김
2. 음식/도구 크기 변화
3. 캐릭터 털 무늬 변화
4. 핵심 사건이 보이지 않음
5. 마지막 반전이 전달되지 않음

Quality 사용 허용:
- 최종 완성 음식 Hero Shot
- 썸네일 후보 프레임으로 쓸 장면
- Lite/Fast로 2회 이상 실패한 핵심 컷

---

# 2. 크레딧 절약을 위한 장면 설계

## 기존 방식
6개의 독립 장면을 매번 새로 생성.

문제:
- 캐릭터 변화
- 주방 변화
- 이전 상태를 모델이 잊음
- 재생성 증가

## 개선 방식

### A. 고정 Reference Pack
한 번 만든 뒤 모든 영상에서 사용:
- CAT_MASTER_FRONT
- CAT_MASTER_PAWS
- KITCHEN_MASTER_WIDE
- KITCHEN_MASTER_COUNTER
- PAN_MASTER
- PLATE_MASTER
- PROP_SCALE_REFERENCE

### B. Episode-specific 음식 Reference
영상마다 2~3개만 추가:
- RAW_FOOD
- MID_STATE
- FINAL_FOOD

### C. Start/End frame 우선
가능한 장면은 텍스트만으로 만들지 말고 프레임을 지정해 `어디서 시작해서 어디로 끝날지`를 잠근다.

### D. One Clip = One Motion
좋은 예:
- 앞발이 계란볼을 팬 쪽으로 민다.
- 계란 가장자리를 들어 올린다.
- 파슬리를 가져간다.

나쁜 예:
- 계란을 깨고, 젓고, 굽고, 뒤집고, 접시에 옮긴다.

행동 수를 줄이면 형태 붕괴와 재생성이 감소한다.

---

# 3. 사람이 해야 하는 일을 최소화하는 콘텐츠 공장

## 사람에게 남길 결정은 3개만

매일 사용자가 선택할 것:
1. 오늘 만들 메뉴
2. 최종 후보 영상 A/B 중 선택
3. 업로드 여부

나머지는 자동화 대상.

## AI가 처리할 작업

```text
트렌드 조사
→ 아이디어 스코어링
→ 제목 5개
→ 훅 5개
→ 45초 대본
→ 장면 JSON/YAML
→ Flow 프롬프트
→ 일본어 VO
→ 자막
→ 파일명
→ 설명/태그
→ 썸네일 프레임 후보
→ 업로드 후 지표 분석
→ 다음 영상 개선
```

---

# 4. Episode Manifest 방식

모든 영상은 자유형 문서가 아니라 하나의 manifest를 가진다.

예:

```yaml
episode_id: TK-001
food: omurice
constraint: 3cm
hook: 猫の手に卵を渡した結果…
length_target: 45
format: experiment
open_loops:
  - 0: can_the_cat_make_it
  - 12: will_the_egg_tear
  - 30: who_is_it_for
payoff: parsley_twist
loop_end: return_egg_cup_to_start
scenes:
  - id: S1
    purpose: hook
    action: paw_pushes_egg_cup
    model: veo_3_1_lite
    duration_generation: 8
    keep_seconds: 7
```

이 manifest를 Codex/Antigravity가 읽어 파일과 프롬프트를 자동 생성하게 한다.

---

# 5. Codex 역할

Codex는 영상 자체보다 `제작 운영체제`를 담당한다.

권장 자동화:
- `episodes/TK-001.yaml` 입력
- Flow용 scene prompt 6개 자동 생성
- 일본어 VO 텍스트 생성
- SRT/VTT 자동 생성
- FFmpeg concat 명령 자동 생성
- 업로드 파일명 자동 생성
- YouTube description 템플릿 생성
- 영상별 실험 변수 기록
- YouTube Analytics CSV/API 결과를 읽어 다음 영상 점수 계산

Codex가 수정하면 GitHub에 기록해 실험 이력을 남긴다.

---

# 6. Antigravity 역할

Antigravity는 사람이 시각적으로 확인해야 하는 작업에 집중한다.

- 캐릭터 reference 비교
- 장면 A/B 시각 검수
- Flow 프롬프트 수정
- 썸네일 프레임 선택
- 일본어 자막 위치/크기 확인

원칙:
> Codex = 반복 가능한 자동화 / Antigravity = 시각적 최종 검수

---

# 7. YouTube 수익화 전략

## 1단계 — 광고보다 500명/300만을 먼저 노림

현재 확대 YPP의 조기 진입 기준은:
- 구독자 500명
- 최근 90일 공개 업로드 3개
- 최근 90일 Shorts 300만 조회 또는 장문 시청시간 요건

목표:
> **첫 돈은 Shorts 광고보다 Shopping/팬펀딩/브랜드 연결 구조에서 만든다.**

## 2단계 — 1,000명/1,000만 Shorts

현재 광고/Premium 수익 진입 목표:
- 구독자 1,000명
- 최근 90일 1,000만 qualified public Shorts views

2027-02-01부터 신규 진입 조건은 2,000만 Shorts views로 강화될 예정이므로 2026년에 최대한 빨리 검증한다.

## 3단계 — 상품 연결

초기에는 상품을 억지로 넣지 않는다.

팬이 생긴 뒤:
- 작은 프라이팬
- 미니어처 키트
- 조명
- 주방 가젯
- 토스터
- 커피머신
- 일본 간식

등을 스토리 안에 자연스럽게 넣는다.

---

# 8. AI 콘텐츠 수익화 방어

YouTube는 반복·대량생산·템플릿형 AI 콘텐츠를 `inauthentic content`로 판단할 수 있다.

따라서 매 영상은 최소 3가지가 달라야 한다.

1. **목표** — 무엇을 해결하는가
2. **사건** — 중간에 어떤 문제가 생기는가
3. **결말** — 고양이가 어떤 선택을 하는가

단순히 음식명만 바꾸고 같은 대본/컷 순서를 반복하지 않는다.

추가로 포토리얼 AI 장면은 업로드 시 YouTube Studio의 AI use/altered synthetic disclosure 여부를 검토한다. AI 사용 공개 자체는 수익화 자격을 제한하지 않는다고 YouTube가 안내한다.

---

# 9. 72시간 Loop Engineering

## LOOP 0 — 현재
- 전략 문서 정리
- 첫 파일럿 확정
- Flow 프롬프트 정리
- 경쟁 채널 구조 정리
- 크레딧 절약 구조 적용

## LOOP 1 — 0~12시간
목표: 제작 실패 비용 최소화

검토:
- Reference pack 개선
- 장면당 행동 수 축소
- Lite에서 실패하는 문장 제거
- 시작/끝 프레임을 어디에 쓸지 분류
- 파일럿 3개를 production-ready manifest로 전환

## LOOP 2 — 12~24시간
목표: 바이럴 가능성 최대화

검토:
- 일본 Shorts 최신 트렌드
- 경쟁 채널 최근 상위 영상
- 첫 프레임 패턴
- 제목 길이
- 35/45/60초 길이 실험
- 댓글 유도 문장

## LOOP 3 — 24~48시간
목표: 자동화

구축/설계:
- Episode YAML → prompts
- Japanese VO/SRT 생성
- FFmpeg 자동 조립
- 파일명/메타데이터 생성
- 성과 기록 CSV
- 다음 영상 자동 추천

## LOOP 4 — 48~72시간
목표: 수익화/확장

검토:
- Shopping 가능한 포맷
- 협찬이 붙을 수 있는 가젯형 에피소드
- 캐릭터 IP 이름/로고/반복 행동
- 시리즈 3개로 축소
- 30일 계획 중 저성과 가능성이 높은 아이디어 제거
- 상위 예상 10개에 제작 리소스 집중

---

# 10. 매 Loop의 자기검증 질문

모든 개선 후 다시 아래를 묻는다.

1. 이 변경으로 사용자의 클릭/수작업이 줄었는가?
2. Flow 생성 횟수가 줄었는가?
3. 첫 1초가 더 강해졌는가?
4. 15초 이후에 볼 이유가 있는가?
5. 마지막에 재시청할 이유가 있는가?
6. 이전 영상과 실질적으로 다른 사건이 있는가?
7. 일본 시청자가 설명 없이 이해할 수 있는가?
8. 상품/협찬과 연결할 수 있는가?
9. 이 작업은 자동화할 수 있는가?
10. 결과가 나쁘면 어떤 변수 하나를 다음 영상에서 바꿀 것인가?

3개 이상 개선되지 않으면 변경을 채택하지 않는다.

---

# 11. 현재 최우선 제작 3개

## TK-001 — 3cm 오므라이스
검증: 캐릭터 + 기본 리텐션 + 반전.

## TK-002 — 쌀 10알 볶음밥
검증: 숫자 제약형 바이럴 가능성.

## TK-003 — 비 오는 날 작은 우동집
검증: 세계관/감성 스토리형 가능성.

세 영상의 결과를 비교해 이후 30일의 비중을 결정한다.

---

# 12. 핵심 운영 철학

> **많이 만드는 것이 목표가 아니다. 적은 Flow 생성으로 승률 높은 영상을 반복해서 만드는 것이 목표다.**

> **AI가 반복 노동을 하고, 사람은 최종 선택만 한다.**

> **매 영상이 하나의 실험이며, 다음 영상은 이전 데이터의 수정본이다.**
