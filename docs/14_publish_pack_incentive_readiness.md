# Zero-LLM Publish Pack + Incentive Readiness

작성 기준: 2026-08-24

## 왜 추가했는가

현재 제작 파이프라인은 Flow 프롬프트와 원본성 검증은 자동화되어 있지만, 업로드 직전마다 사람이 제목·설명·고정댓글·AI 공개·브랜드 관련 체크를 다시 정리해야 했다. 이 단계는 Flow 크레딧을 쓰지 않으면서도 반복 노동과 실수를 줄일 수 있는 영역이다.

또 YouTube는 2026년 8월 YPP 개편 공지에서 향후 Shorts 대상 Shopping 보너스, 브랜드딜 인센티브, 문화 트렌드 활성화 보너스 같은 새 프로그램을 예고했다. 세부 자격은 아직 공개되지 않았으므로, 지금은 추측해서 콘텐츠를 바꾸지 않고 episode 단위의 창작 근거·트렌드 근거·상업 관계 여부를 깔끔히 기록하는 쪽이 안전하다.

## 실행

```bash
python tools/build_publish_pack.py episodes/TK-001.yaml
```

생성 결과:

```text
generated/TK-001_publish_pack.md
```

포함 항목:
- 복붙용 YouTube 제목
- 설명
- 고정 댓글
- AI 사용 공개 체크
- paid promotion 체크
- 제품 태그/Shopping 오남용 방지
- 원본성 기록
- 24h / 72h 성과 입력 리마인더

## 원칙

1. 포토리얼 Tiny Cat Kitchen은 AI use disclosure = YES를 기본값으로 둔다.
2. AI 공개 자체는 YouTube가 추천 또는 수익화 자격을 제한하지 않는다고 안내한다.
3. 브랜드가 금전, 무료 제품 또는 기타 가치를 제공한 경우에만 paid promotion을 표시한다.
4. Shopping/affiliate는 실제 YouTube Studio 자격과 제품 관계를 확인한 경우에만 사용한다.
5. 아직 세부 기준이 발표되지 않은 2026년 신규 Shorts 인센티브를 추측해 콘텐츠를 양산하지 않는다.
6. 모든 episode는 `creator_signature`, `unique_goal`, `unique_conflict`, `unique_ending`을 유지해 YPP의 inauthentic-content 리스크를 낮춘다.

## 최근 경쟁/포맷 신호

2026년 8월 일본에서 AI猫にゃんこちん Official은 약 9.18만 구독자, 최근 30일 +800명, 약 88만 조회로 캐릭터 IP형 콘텐츠가 계속 반응을 얻고 있다. 반면 전통 Miniature Cooking 일본 채널은 2024년 이후 신규 업로드가 거의 없어 현재 성장성이 낮다.

또 최근 일본 Shorts에서 `おかずが全部グミ`처럼 일상의 규칙을 한 번 뒤집는 단순하고 즉시 이해되는 설정이 수백만 조회를 얻은 사례가 확인됐다. 여기서 복제할 것은 구미 자체가 아니라 다음 구조다.

```text
0.5초 안에 이해되는 평범한 규칙
→ 한 가지 규칙만 극단적으로 뒤집음
→ 즉시 보이는 시각적 이상함
→ 짧은 해결/반응
```

Tiny Cat Kitchen 적용 시 음식/고양이 캐릭터 디자인을 복제하지 않고 `세계 규칙 한 가지 뒤집기`를 새로운 hook family 후보로만 사용한다.

## 현재 Flow 비용 결론

공식 Google Flow 기준은 변동 없음:
- Veo 3.1 Lite: 4/6/8초, non-Ultra 10 credits / Ultra 5
- Fast: 20 / 10
- Quality: 8초 100
- 무료 비구독: 일 50 credits
- Lite First+Last 지원, Fast First+Last는 아직 Coming soon

따라서 현재의 `4 Lite frame-locked generations = 40 credits + 10-credit reserve`가 여전히 합리적이다.

## 다음 단계

새 episode manifest에 필요할 때만 아래를 추가한다.

```yaml
publishing:
  description_line: "이 에피소드에만 맞는 짧은 일본어 설명"
  audience_prompt: "이 에피소드 결말과 직접 연결된 질문"
  hashtags: ["#Shorts", "#ミニチュア料理", "#猫", "#AI猫"]
```

필드를 생략해도 publish pack generator가 안전한 기본값을 만든다. LLM 재작성은 premise가 바뀔 때만 사용한다.
