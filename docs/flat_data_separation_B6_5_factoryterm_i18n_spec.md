# FLAT B6.5 factoryTerm i18n 통합 spec

## v0.1 — 2026-05-12 cont.72 Part 12 코드탭 자율 신설

> **목적:** plan.md "i18n EN/KO + 봉제 현장용어 자동 병기 (factoryTerm{})" 명시 항목 — 현재 미구현. data/factory_terms.json (60 용어, cont.72 Part 8 T4) 신설했지만 LANG.ko 통합은 후속 spec 영역.
> **연관 spec:** B6.1 rules / B6.2 presets / B6.3 fabrics / B6.4 parametric / **B6.5 factoryTerm i18n**
> **선행 자산:** `data/factory_terms.json` v0.1 (60 용어 / 8 카테고리)
> **이람 brand voice 무관 영역만:** 매핑 source 정리 + 통합 메커니즘 spec. 표현 다듬기는 이람 후속.

---

## 0. 근거

- **plan.md 명시:** "i18n EN/KO + 봉제 현장용어 자동 병기 (factoryTerm{})" — 현재 데이터 신설만 / LANG.ko 통합 X
- **메모리 reference_factory_terms.md:** 서울의류협동조합 봉제용어 / 국립언어원 감수 / 60 용어
- **cont.72 Part 7 self-audit § 8 D:** "봉제 현장용어 자동 병기 매핑 정확성 미검증" 등록
- **cont.72 Part 8 T4:** data/factory_terms.json 신설 (60 용어 / 8 카테고리)
- **factory validation 5월:** 공장 작지서 소통 시 현장 용어 필수 — plan.md 명시
- **목표:** PDF 작업지시서 + Factory Viewer KO 모드에서 자동 병기

---

## 1. 적용 layer

### 1.1 3 layer 분리

| Layer | 위치 | 적용 |
|---|---|---|
| Layer 1 | `LANG.ko.{section}.{key}` | 일반 KO 표준어 유지 (현재 그대로). 예: `collar: '칼라'` |
| Layer 2 | `LANG.ko_factory.{section}.{key}` (신규) | 봉제 현장용어 layer. 예: `collar: '칼라 (에리)'` 또는 `'에리'` |
| Layer 3 | `data/factory_terms.json` | 매핑 source (cont.72 Part 8 T4 신설) |

### 1.2 사용자 모드 전환

```
[현재] LANG = en / ko
[B6.5 후] LANG = en / ko / ko_factory
```

- `setLang('ko_factory')` 추가 → 모든 UI 라벨이 현장 용어로 표시
- 또는 `setLangMode('factory')` toggle — KO + ko_factory 통합 (병기 형식)

### 1.3 병기 형식 옵션

| 형식 | 예시 | 사용 케이스 |
|---|---|---|
| A. 단독 표준어 | `칼라` | 일반 사용자 / 디자이너 |
| B. 단독 현장어 | `에리` | 공장 / 봉제사 |
| C. 병기 (표준어 메인) | `칼라 (에리)` | 디자이너 + 공장 협업 |
| D. 병기 (현장어 메인) | `에리 (Collar)` | 공장 + 디자이너 협업 |

**추천 default:** C (표준어 메인 + 현장어 괄호) — 이람 brand voice 영역, 후속 결정.

---

## 2. 데이터 매핑 schema

### 2.1 i18n LANG.ko_factory schema

```js
LANG.ko_factory = {
  sleeve: {
    cuff: '소대 구찌',  // Sleeve Opening, factory_terms.json structure.소대구찌
    capped: '캡슬리브',  // 일반 KO 유지 (현장어 없음)
    // ...
  },
  body: {
    sideSeam: '와끼',  // factory_terms.json structure.와끼
    // ...
  },
  neck: {
    collarLabel: '에리',  // factory_terms.json structure.에리
    // ...
  },
  detail: {
    pocket: '구찌',  // factory_terms.json pocket.구찌 (Welt Pocket)
    welt: '하꼬 주머니',
    barTack: '간도메',  // factory_terms.json sewing_technique.간도메
    // ...
  },
  closure: {
    button: '돗도',  // factory_terms.json closure.돗도 (Snap)
    single: '가다마이',  // factory_terms.json closure.가다마이 (Single Breasted)
    double: '요마이',  // factory_terms.json closure.요마이
    // ...
  },
  stitch: {
    single: '본봉',  // factory_terms.json stitch.본봉 (Single Needle Lock Stitch)
    overlock: '오바로크',
    // ...
  }
};
```

### 2.2 매핑 자동 생성

`data/factory_terms.json` 의 각 entry → LANG.ko_factory key 매핑 함수:

```js
function buildFactoryLangFromTerms(terms) {
  const ft = {};
  for (const category of Object.keys(terms.terms)) {
    for (const [factoryKey, entry] of Object.entries(terms.terms[category])) {
      // entry.en → 매칭 i18n key 추적
      // entry.factoryKey → LANG.ko_factory 매핑
    }
  }
  return ft;
}
```

**한계:** factory_terms.json은 `factoryKey → en/ko_standard` 매핑. i18n key (예: `sleeve.cuff`)와는 1:1 매핑 X. **수동 매핑 표 필요.**

### 2.3 수동 매핑 표 (B6.5 implement 시 작성)

| i18n 경로 | LANG.ko (표준) | LANG.ko_factory (현장) | factory_terms 경로 |
|---|---|---|---|
| sleeve.cuff | 소매단 | 소대 구찌 | structure.소대구찌 |
| body.sideSeam | 옆선 | 와끼 | structure.와끼 |
| neck.collarLabel | 칼라 | 에리 | structure.에리 |
| detail.welt | 웰트 포켓 | 하꼬 주머니 | pocket.하꼬주머니 |
| detail.barTack | 바텍 | 간도메 | sewing_technique.간도메 |
| ... | (수동 매핑 ~50 entry) | | |

---

## 3. UI 토글

### 3.1 헤더에 KO/KO-Factory 추가

```html
<button class="mode-btn on" id="langEn" onclick="setLang('en')">EN</button>
<button class="mode-btn" id="langKo" onclick="setLang('ko')">KO</button>
<button class="mode-btn" id="langKoFactory" onclick="setLang('ko_factory')">KO 공장</button>
```

또는 KO 모드 안 sub-toggle:
```
KO [표준어 ⓘ] [현장어 ⓘ]
```

### 3.2 PDF tech pack 적용

Construction Notes 영역에 병기:
```
Sleeve Cuff (소매단 / 소대 구찌) ............... 1.00 cm
Pocket Bar Tack (바텍 / 간도메) ................ 0.5 cm
```

factory validation 5월에 공장에 전달 시 현장어 통합 PDF = 직접 가치.

---

## 4. 구현 단계

### Phase 1: 데이터 매핑 표 작성 (B6.5 spec implement 시작점)

- `data/factory_terms_i18n_mapping.json` 신설 — 수동 매핑 표 (예상 ~50 entry)
- factory_terms.json + i18n key 1:1 매핑
- factoryNote 필드 있는 항목 우선 매핑

### Phase 2: LANG.ko_factory 생성

- `flat-v6.html` LANG에 ko_factory 추가
- 매핑 표 기반 자동 생성 또는 수동 작성
- 적용 영역: sleeve / body / neck / detail / closure / stitch / fabric

### Phase 3: UI 토글

- 헤더에 KO/KO-Factory 모드 추가
- `setLang('ko_factory')` → applyLang() 호출 → 모든 data-i18n 갱신
- 또는 sub-toggle (병기 형식)

### Phase 4: PDF 통합 (factory validation 후)

- pdfWorkOrder() 한국어 작업지시서에 병기 적용
- 공장 측 가독성 검증 (Phase 3B 인터뷰)

---

## 5. 코드탭 자율 가능 / 이람 결정 분리

### 코드탭 자율 (B6.5 spec implement)

- ✅ Phase 1 매핑 표 작성 (factory_terms.json + i18n key 1:1)
- ✅ Phase 2 LANG.ko_factory 생성 (자동 또는 수동 매핑)
- ✅ Phase 3 UI 토글 구현
- ✅ 검증 (매핑 정합 + sweep 회귀)

### 이람 결정 영역

- 병기 형식 (A/B/C/D) — brand voice
- 표현 다듬기 (예: '단작' vs '단작 (Placket)') — 디렉터 보이스
- KO 모드 안 sub-toggle vs 별도 KO 공장 모드
- 공장 검증 기준 (Phase 3B 인터뷰 후)

---

## 6. 검증 기준

### 6.1 정합성

- [ ] 매핑 표 모든 entry의 factory_terms 경로 실제 존재 확인
- [ ] LANG.ko_factory 키가 LANG.ko 키와 1:1 대응 (i18n 318 keys 보장)
- [ ] `setLang('ko_factory')` 호출 시 모든 data-i18n 갱신 (enMissing 0)

### 6.2 회귀

- [ ] 기존 LANG.en/ko 동작 영향 0
- [ ] 96 case sweep NaN 0 / Exception 0
- [ ] crewTee/sweatshirt baseline 회귀 0

### 6.3 도메인

- [ ] 공장 인터뷰 (Phase 3B) 시 현장어 정확성 확인
- [ ] 표준어 ↔ 현장어 매핑이 봉제사 인지에 정확

---

## 7. 의존성

| 영역 | 관계 |
|---|---|
| factory_terms.json | ✅ 작성 완료 (cont.72 Part 8 T4) |
| i18n LANG.ko 318 keys | ✅ 100% coverage (cont.72 Part 8 T1) |
| B6.2 presets schema 정합 | 무관 (별도 layer) |
| Phase 3B factory validation | 5월 후 — 현장어 정확성 검증 가치 |
| PDF tech pack | factory validation 후 통합 |

---

## 8. 작업량

| 단계 | 작업량 |
|------|--------|
| spec 본문 (이 문서) | ✅ 완료 (cont.72 Part 12 코드탭 자율) |
| Phase 1 매핑 표 (~50 entry) | 1-2 세션 |
| Phase 2 LANG.ko_factory 생성 | 1 세션 |
| Phase 3 UI 토글 | 1 세션 |
| Phase 4 PDF 통합 | factory validation 후 1 세션 |

**총 implement:** 3-5 세션 (Phase 1-3) + factory validation 후 1 세션 (Phase 4)

---

## 9. 변경 이력

- **2026-05-12 v0.1**: 코드탭 cont.72 Part 12 자율 신설. plan.md 명시 항목 응답. factory_terms.json (60 용어) + i18n 통합 메커니즘 spec. 이람 brand voice 무관 영역만.

---

## 10. 다음 단계

1. **이람:** spec read 또는 수정
2. **코드탭:** Phase 1 매핑 표 신설 (`data/factory_terms_i18n_mapping.json`)
3. **이람:** 병기 형식 결정 (A/B/C/D)
4. **코드탭:** Phase 2-3 implement
5. **Phase 3B factory validation:** 현장어 정확성 검증 → Phase 4 PDF 통합
