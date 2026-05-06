# FLAT 카피 가이드 (S4 spec source)

> **목적:** 모든 옵션 카드 / 슬라이더 라벨 / 토글 라벨 / 메타카피의 톤 표준.
> **참조 spec:** `docs/sixatomic_implementation_specs.md` Section 4 (S4)
> **참조 audit:** `docs/sixatomic_pattern_generate_audit.md` Section 6 (카피 톤 분석)
> **버전:** v0.1 — 2026-05-06 cont.72 Part 7 코드탭 자율 신설 (이람 brand voice 후속 보강)

---

## 0. 위치

이 문서는 **코드탭 작성 영역 (source 정리)**. 이람 brand voice 영역은 별도 후속:
- 코드탭 (이 문서): 6 톤 규칙 source + 적용 매트릭스 + 자동 검증 가능 영역
- 이람 (후속): 디렉터 보이스 / 한국어 표현 다듬기 / 패션 업계 어휘 선택

---

## 1. 6 톤 규칙 (sixatomic audit Section 6 흡수)

### Rule 1. 명령형 단정조

**예측이 아닌 사실 선언.**

| ✅ Good | ❌ Bad |
|---|---|
| "Side seam ends 3.0 cm above hip level." | "Side seam might end around 3 cm above hip" |
| "Sleeve length is 53.0 cm at Wrist." | "Sleeve goes to wrist roughly" |
| "Body fit is Regular (50% ease)." | "Default fit is normal" |

### Rule 2. 정확한 수치 + 단위

**`cm` / `°` / `%` 모두 소수점 첫째 자리까지.**

| 영역 | 형식 | 예시 |
|---|---|---|
| 길이 | X.X cm | `45.0 cm`, `3.0 cm` |
| 각도 | X.X° | `40.0°`, `32.0°` |
| 비율 | XX.X% | `50.0%`, `35.3%` |
| ratio (sleeve length) | 0.XXX | `0.353`, `1.000` |

**FLAT 적용 검증:** SD 정의의 fmt 함수 결과 (sleeveLength 22, neckDepth 10 등) — 정수 + 단위 표시 통일.

### Rule 3. 상대 비교 대신 절대 수치

**"조금 짧음" / "약간 넓음" 금지. 절대 수치.**

| ✅ Good | ❌ Bad |
|---|---|
| "Above hip 3.0 cm" | "Slightly above hip" |
| "Bicep 25.0 cm" | "Roomy bicep" |
| "Neck depth 10.0 cm" | "Deep neck" |

**FLAT 예외:** 슬라이더 라벨 (Short / Regular / Long) — enum형 라벨은 OK. 단 라벨 옆 수치 표시 필수 (`Short (Regular) (32)` 형식).

### Rule 4. 목적/맥락 한 줄

**왜 이 옵션을 선택할지 한 줄로.**

| 옵션 | ✅ Good 한 줄 |
|---|---|
| Halter neckline | "Suitable for sleeveless / open back styles." |
| Raglan sleeve | "Stretch / sport friendly construction." |
| Drop shoulder | "Relaxed / oversized silhouettes." |

**적용 위치:** 옵션 카드 일러스트 아래 / 토글 hover tooltip / spec sheet 메타.

### Rule 5. 부정 / 제약 솔직

**할 수 없는 것 / 비표준 영역도 솔직 명시.**

| ✅ Good | ❌ Bad |
|---|---|
| "Polo doesn't support sleeveless." | (메시지 없이 토글 disabled만) |
| "Sweatshirt definition includes sleeves." | "Some restrictions apply" |
| "Won't be smaller than 85.0% of bust." | (제약 숨김) |

**FLAT 적용:** B6.1 rules.json의 `effect.message.en/ko` 필드. cont.72 Part 4 6 sample rule 모두 이 패턴.

### Rule 6. 헤더 메타카피로 layer 분리

**섹션 헤더 한 줄 — 이 영역이 영향 안 미치는 곳 명시.**

| 섹션 | 메타카피 |
|---|---|
| Design | "Big decisions — silhouette, category, style." |
| Fit | "Size decisions — body fit, neck fit, ease." |
| Details | "Detail toggles — pockets, dart, closure." |
| Advanced | "Custom adjustments. Most users won't need these." |

**FLAT 적용 위치:** S8 메타-그룹 헤더 (Design / Fit / Details). 현재 라벨만 / **메타카피 미적용** ← 후속.

---

## 2. 적용 매트릭스 (FLAT 영역별)

| 영역 | Rule 1-6 적용 | 현 상태 |
|---|---|---|
| 옵션 카드 (토글) | 1, 2, 3, 4, 5 | ⚠️ 토글 텍스트만 (한 줄 맥락 없음) — S4 후속 |
| 슬라이더 라벨 | 1, 2, 3 | ✅ SD 함수로 enum 라벨 + 수치 (cont.69 Part 5 보강) |
| 슬라이더 cm 입력 | 2 | ✅ CM_MAP 정수 표시 |
| Spec sheet | 1, 2, 3, 4 | ✅ graded XS-XL + tolerance |
| Hint system (sleeveSkin/Wide 등) | 1, 4, 5 | ⚠️ 일부 메시지만 / 정확성 미검증 |
| Compat rule 메시지 | 1, 4, 5 | ✅ B6.1 6 sample (en/ko 둘 다) |
| 메타-그룹 헤더 | 6 | ⚠️ 라벨만 (Design/Fit/Details) — 메타카피 미적용 |
| Style Overlay 라벨 | 4 | ⚠️ 라벨만 (Casual/Formal/...) — 한 줄 맥락 없음 |
| 데모 영상 / IR 덱 | 1-6 | 📝 이람 영역 |
| FLAT 브랜드 톤 (`docs/flat_content_voice.md`) | 메타 | ❌ 미작성 (이람 의존) |

---

## 3. 자동 검증 가능 영역 (코드탭 자율)

### 3.1 수치 + 단위 정합성 검증

```python
# tools/audit/copy_check.py (제안)
import re
# 슬라이더 fmt 결과 검증 — cm 표시는 정수만
# 예: sleeveLength=32 → "22cm" (round) — Rule 2
# 단위 X 표기 (예: "22" 만): 부정 패턴
for k,v in SLIDER_FMT_RESULTS.items():
    if not re.search(r'\d+(\.\d+)?(cm|°|%)$', v):
        warn(f'단위 누락: {k}={v}')
```

### 3.2 i18n 텍스트 길이 검증

- 옵션 카드 카피 ≤ 80자 (sixatomic 패턴)
- 토글 버튼 라벨 ≤ 30자
- Hint 메시지 ≤ 100자

### 3.3 절대 수치 / 상대 표현 검출

- "약간 / 조금 / 살짝 / slightly / about / roughly" 키워드 검색 → Rule 3 위반 후보 표시.

---

## 4. 우선순위

### 4.1 즉시 자율 가능
- ⚠️ 메타-그룹 메타카피 추가 (S8 후속, "Design / Fit / Details" 라벨에 한 줄 맥락 추가)
- ⚠️ Hint system 메시지 검증 (Rule 1, 4, 5 적용)
- ⚠️ Style Overlay 라벨에 한 줄 맥락

### 4.2 이람 brand voice 의존 (후속)
- 옵션 카드 카피 재작성 (모든 토글에 한 줄 맥락)
- FLAT 브랜드 톤 문서 (`flat_content_voice.md`)
- 한국어 표현 다듬기 (디렉터 보이스 / 패션 업계 어휘)

### 4.3 자동 검증 도구 (B 라인 spec 후속)
- `tools/audit/copy_check.py` 신설
- i18n 텍스트 길이 / 단위 정합성 / 상대 표현 검출

---

## 5. 변경 이력

- **2026-05-06 v0.1**: 코드탭 cont.72 Part 7 자율 신설. audit Section 6 6 톤 규칙 그대로 + FLAT 적용 매트릭스 + 자동 검증 가능 영역. **이람 brand voice 후속 보강 대기.**
