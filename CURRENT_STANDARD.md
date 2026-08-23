# CURRENT STANDARD — Tiny Cat Kitchen

최신 적용 기준: **2026-08-24 Frame-Lock Loop**

실제 제작 시 우선순위:

1. `docs/08_frame_lock_trend_injection_factory.md` — **현재 최우선 기준**
2. `tools/build_flow_pack.py` — episode YAML에서 Flow prompt pack 자동 생성
3. `episodes/TK-001.yaml` — 첫 파일럿
4. `episodes/TK-002.yaml` — 숫자 제약 훅 실험
5. `episodes/TK-003.yaml` — 세계관 스토리 실험
6. `docs/07_4gen_exploration_and_ip_moat.md` — 4-generation 비용 기준 참고
7. `docs/06_zero_waste_flow_factory.md` — 5-generation 승격형 참고
8. `docs/02_google_flow_scene_prompts.md` — 장면 연출 라이브러리 참고

## 현재 비용 원칙

초기 탐색 영상:

> Nano Banana 2 Lite 5-keyframe preflight → Veo 3.1 Lite **4 Start+End-frame locked generations** → 35~38초 편집

- Non-Ultra: 40 Flow credits
- Ultra: 20 Flow credits
- output count: 1
- 5개 keyframe: OPEN / CONSTRAINT / DANGER / PAYOFF / TWIST
- G1~G4는 인접 keyframe을 First + Last frame으로 고정
- CTA/loop용 별도 video generation 금지
- 5번째 generation은 승자 포맷에만 허용
- Fast는 실패한 특정 컷만 승격
- Quality는 반복 사용할 hero asset에만 허용
- 이미지 preflight는 `Nano Banana 2 Lite`를 명시적으로 확인

핵심은 40 credits보다 더 싸게 보이게 만드는 것이 아니라 **reroll을 줄여 실제 총비용을 낮추는 것**이다.

## 현재 자동화 원칙

사람이 매 scene prompt를 직접 작성하지 않는다.

```bash
pip install -r tools/requirements.txt
python tools/build_flow_pack.py episodes/TK-001.yaml
```

그러면 `generated/TK-001_flow_pack.md`가 생성된다.

사람 승인 지점은 4개뿐이다.

1. 일본어 title
2. 첫 3초 hook
3. 5-keyframe contact sheet
4. 최종 export

## 현재 성장 원칙

첫 3편은 서로 다른 가설을 검증한다.

- TK-001: 캐릭터 + 미니요리 기본 포맷
- TK-002: 숫자 제약 훅
- TK-003: 감성 세계관/스토리

그 다음부터 게시 비율 기본값:

```text
CORE IP / 숫자 도전
→ CORE IP / 생활 세계관
→ TREND INJECTION / 최근 7~30일 일본 푸드 트렌드
→ 반복
```

즉 **3편 중 최소 1편은 현재 푸드 트렌드를 Tiny Cat Kitchen 방식으로 재해석**한다.

30편을 먼저 생산하지 않는다.

## 현재 원본성 원칙

각 episode는 기존 6개 항목이 식별 가능해야 한다.

- unique_goal
- unique_conflict
- unique_ending
- character_motivation
- world_state_change
- callback_or_new_lore

그리고 `episode_fingerprint` 5개를 추가한다.

- hook_mechanic
- dominant_visual
- conflict_mechanic
- emotional_turn
- ending_mechanic

신규 에피소드는 직전 5편과 비교해 fingerprint 5개 중 최소 3개가 달라야 한다.

같은 컷 순서와 같은 결말에 음식만 교체하는 방식은 금지한다.

## 현재 수익화 우선순위

1. 500-subscriber expanded YPP tier 접근
2. fan funding / 실제 활성화된 Shopping 기능 확인
3. 캐릭터 IP와 미니 주방/가젯 브랜드 협업 가능성 축적
4. 2026년 안에 가능하면 1,000 subscribers + 10M Shorts views 광고/Premium 진입

포토리얼 AI 영상은 YouTube Studio AI use disclosure를 기본 `Yes`로 처리한다.
