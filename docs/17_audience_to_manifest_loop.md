# Audience-to-Manifest Loop — 댓글/스티커를 다음 에피소드 데이터로 쓰기

작성 기준: 2026-08-24

## 목적

Tiny Cat Kitchen의 다음 아이디어를 매번 사람이 새로 고민하거나 LLM에게 브레인스토밍시키지 않는다.

YouTube가 2026-07-07 공식 블로그에서 Shorts의 Poll Sticker, Q&A Sticker, Add Yours, Video Replies를 조회수를 팬으로 바꾸는 상호작용 기능으로 권장했다. 특히 Poll/Q&A는 다음 콘텐츠 수요를 직접 수집하고, Video Reply는 원댓글 작성자에게 알림이 가며 댓글 피드 안에서도 연결된다.

공식 참고:
- https://blog.youtube/creator-and-artist-stories/grow-youtube-channel-interactive-shorts/
- https://support.google.com/youtube/answer/11914225

핵심 원칙:

> **Audience signal → idea seed → originality validation → Flow spend**

시청자 요청을 바로 제작하지 않는다. 아이디어 씨앗으로만 사용하고 기존 `unique_goal / unique_conflict / unique_ending / episode_fingerprint` 검증을 통과한 경우에만 Flow 크레딧을 쓴다.

---

## 1. 3편 순환 포맷

### A — Poll episode

목적:
- 다음 음식 후보 A/B를 빠르게 결정
- 추측 대신 실제 시청자 선호 사용

예:

```text
次に3cmで作るなら？
ラーメン / 寿司
```

주의:
- 승리한 음식만 가져온다.
- 직전 영상의 갈등/결말/컷 구조까지 복제하지 않는다.

### B — Q&A episode

목적:
- 예상하지 못한 소재를 수집
- 별도 LLM 브레인스토밍 토큰 절약

예:

```text
10粒だけで作ってほしい料理は？
```

운영:
- 반복해서 등장하는 명사/문제만 후보로 기록
- 한 명의 매우 특이한 제안보다 여러 시청자가 반복한 요구를 우선
- 제작 전 originality validator 통과 필수

### C — Video Reply episode

목적:
- 댓글을 실제 세계관 사건으로 승격
- 시청자가 `내 댓글이 다음 화가 될 수 있다`고 학습하게 만들기

좋은 트리거:
- 구체적인 다음 손님 제안
- 새 메뉴 + 새 문제를 동시에 만드는 댓글
- 기존 세계관 설정을 자연스럽게 확장하는 질문

나쁜 트리거:
- `라멘 해주세요`처럼 음식명만 바뀌는 요청
- 직전 영상과 같은 갈등/결말을 요구하는 댓글
- 단지 댓글에 답하기 위해 거의 같은 영상을 다시 만드는 경우

---

## 2. 한 영상에 상호작용 장치를 많이 넣지 않는다

원칙:

> **1 episode = 1 primary interaction mechanic**

Poll + Q&A + 긴 댓글 CTA를 동시에 넣지 않는다.

이유:
- 시청자 행동 요청이 분산됨
- 마지막 payoff가 CTA에 먹힘
- 채널이 성장 해킹 템플릿처럼 보일 수 있음

기본 pinned comment는 유지할 수 있지만, interactive sticker가 있는 경우 generic like/subscribe CTA는 제거한다.

---

## 3. Episode YAML

각 episode에 선택적으로 아래 필드를 둔다.

```yaml
audience_loop:
  mode: poll
  question: "次に3cmで作るなら？"
  options: ["ラーメン", "寿司"]
  next_manifest_seed: winning_option_becomes_candidate_food_but_requires_new_conflict_and_resolution
```

지원 mode:
- `poll`
- `q&a`
- `video_reply`

`tools/build_publish_pack.py`가 이 값을 읽어 Studio/모바일에서 해야 할 상호작용 작업을 자동으로 출력한다.

---

## 4. 현재 첫 3편 배치

### TK-001 — Poll

```text
次に3cmで作るなら？
ラーメン / 寿司
```

목적:
- 첫 파일럿에서 바로 다음 음식 수요 확보

### TK-002 — Q&A

```text
10粒だけで作ってほしい料理は？
```

목적:
- 숫자제약 시리즈의 다음 규칙을 시청자가 공급

### TK-003 — Video Reply

트리거:
- 다음 손님 또는 비 오는 밤 메뉴를 제안하면서 새로운 사건이 생길 수 있는 구체 댓글

목적:
- `고양이 식당 세계관`에서 시청자가 손님/메뉴 설정에 개입

---

## 5. 비용 절감 효과

기존:

```text
새 영상 아이디어 필요
→ 사람이 고민
→ LLM 브레인스토밍
→ 후보 정리
→ Flow 제작
```

변경:

```text
Poll/Q&A/댓글
→ 실제 수요가 있는 idea seed
→ deterministic originality validation
→ 통과한 후보만 Flow 제작
```

Flow 크레딧 자체 가격은 바뀌지 않지만 **수요 없는 아이디어에 40 credits를 쓰는 확률을 낮추는 것**이 실제 비용 절감 효과다.

---

## 6. 팬 전환 효과

YouTube 공식 가이드의 핵심은 `views do not automatically equal fans`이다.

따라서 다음 KPI를 기존 리텐션 지표와 별도로 본다.

- poll 참여 수 / engaged views
- Q&A 응답 수 / engaged views
- 댓글 중 다음 episode로 사용 가능한 구체 제안 비율
- Video Reply 이후 해당 원댓글/후속 영상의 댓글 증가
- subscribers per 1,000 engaged views

조회수만 높은 영상보다 **다음 행동을 만드는 영상**을 IP 성장 승자로 평가한다.

---

## 7. YPP / 원본성 안전장치

YouTube는 자동화 도구나 템플릿 사용 자체를 금지하지 않는다. 최종 영상에 독창적인 창작 방향과 실제 엔터테인먼트/교육 가치가 있어야 한다.

따라서 audience-driven episode도 다음을 반드시 바꾼다.

- goal
- conflict
- resolution
- dominant visual
- creator signature

시청자가 같은 음식을 요청했더라도 위 요소가 새롭지 않으면 제작하지 않는다.

---

## 8. 운영 결론

> **다음 메뉴를 AI에게 묻기 전에 시청자에게 먼저 묻는다.**

이 구조는 동시에 세 가지를 개선한다.

1. 아이디어 생성에 쓰는 사람 시간과 LLM 토큰 감소
2. 실제 수요가 있는 소재만 Flow 크레딧 투입
3. 조회수를 반복 방문/댓글/구독으로 전환해 Tiny Cat Kitchen을 캐릭터 IP로 강화
