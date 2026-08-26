# 29 — Analytics Truth Model

목표: **YouTube 24h/72h 성과와 Flow 제작비/QC 데이터가 서로 다른 CSV에 흩어져 다음 episode 학습에서 빠지는 것을 막는다.**

## 두 파일의 역할

### `analytics/shorts_metrics_v2.csv`

Raw observation table.

한 행은 한 episode의 한 observation horizon이다.

허용 horizon:
- 24h
- 72h

기록:
- published_at
- public_views
- engaged_views
- stayed_to_watch_pct
- avg_percentage_viewed_pct
- likes
- comments
- subscribers_gained

규칙:
- 실제 YouTube Studio 값만 입력
- 미래 24h/72h 행을 0으로 미리 만들지 않음
- placeholder 0을 실패처럼 해석하지 않음
- 24h는 24h끼리, 72h는 72h끼리 비교

### `analytics/learning_ledger.csv`

**Canonical combined decision memory.**

다음 episode / runtime / action / credit prior를 바꾸는 자동·수동 판단은 이 파일을 기준으로 한다.

한 observation row에는 가능한 범위에서 다음을 함께 보존한다.

Production truth:
- actual Flow credits
- rerolls
- runtime mode
- G1/G2/G3/G4 first-pass result
- POV/scale/anatomy failure
- usable motion seconds
- continuity issue
- failed action type
- audio replacement
- final runtime

Audience truth:
- observation_hours
- public_views
- engaged_views
- stayed_to_watch_pct
- avg_percentage_viewed_pct
- subscribers_gained
- comments

## Publish 후 절차

```text
actual upload
→ 24h Studio snapshot
→ shorts_metrics_v2.csv에 실제값 기록
→ 같은 24h 값을 learning_ledger.csv의 해당 episode/horizon에 반영
→ 72h에도 동일
→ 같은 horizon끼리 비교
→ engaged views/credit와 subscribers/100 credits를 다음 판단에 사용
```

`shorts_metrics_v2.csv`에만 쓰고 끝내면 안 된다. 그러면 production cost/QC와 audience performance가 분리되어 continuous learning loop가 불완전해진다.

반대로 `learning_ledger.csv`만 임의 숫자로 채우지 않는다. Studio에서 확인한 raw snapshot을 먼저 근거로 남긴다.

## Placeholder 정책

템플릿 편의를 위한 아래 형태는 금지한다.

```text
TK-XXX,...,24,0,0,0,0,0,0,0
TK-XXX,...,72,0,0,0,0,0,0,0
```

실제 0 view/0 engaged가 관측된 경우에는 실제 관측임을 구분할 수 있는 상태/근거와 함께 기록해야 한다. 아직 시간이 오지 않았거나 Studio를 확인하지 않았다면 행 자체를 만들지 않는다.

## 최적화 목적

우선순위:

```text
usable motion / credit
engaged views / credit
subscribers / 100 credits
```

`public_views`만으로 episode winner를 정하지 않는다.

## 변경 금지 원칙

- production metrics와 audience metrics를 서로 다른 진실처럼 운영하지 않음
- 24h와 72h를 같은 cohort로 직접 순위 비교하지 않음
- missing 값을 0으로 자동 변환해 실패로 학습하지 않음
- 한 편 결과만으로 H30/H40 또는 특정 action family를 확정하지 않음
