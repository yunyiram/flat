# FLAT 핸드오프
> **모든 탭은 세션 시작 시 이 파일을 먼저 읽는다.**
> 섹션 단위 수정만. 전체 덮어쓰기 금지 (원칙 7).

마지막 수정: 2026-04-22 코드탭 cont.68 중간 완료 (옵션 H 절충 구현 push b7b3b46, sweatshirt body/rib/armhole SFD + shoulder는 FLAT convention)

---

## 📌 핵심 원칙 (양쪽 공유)

1. **수학적 정확성(internal) + 시각적 자연스러움(external)** 동시 충족.
2. **프리셋=시작점, 디테일=토글, 파라미터=슬라이더, 스타일=aesthetic 조합.**
3. **카테고리=construction+인식.** 차단 대신 안내.
4. **현실 과대평가 금지.** "구현됨" ≠ "앞에 내밀 수 있음".
5. **영감이 생산으로 변하는 순간이 보인다.** 트레이싱 프리즈.
6. **검증 가능한 산출물 없으면 "완료" 판정 금지.** 자동 검증(NaN 0, dasharray 0)은 가능성 확인일 뿐. 실무 검증 = 이람 눈 + 기획탭 DOM 실측(`tools/audit/inspect_flat.py`) + 레퍼런스 오버레이.
7. **HANDOFF 전체 덮어쓰기 금지.** 섹션 단위 수정만. 수정 전 `docs/archive/HANDOFF-{timestamp}-*.md` 자동 백업.
8. **용어 분리.** Stage=전략 마일스톤(1-4). Phase=구현 단위(1A/1B/2/3+). 섞어 쓰지 않는다.
9. **[확장] 반복 피드백은 아키텍처 문제 신호.** 같은 영역 3회 이상 수정되면 magic number 조정 중단 + 전역 상수의 전역성 자체를 의심. **[cont.67 확장] 국소 상수 분리(옵션 G)조차 primitive geometry 안의 상수 분배일 수 있음. geometry 수식 자체가 실무 POM 근거 없이 편의값이면, 재구축(옵션 H)이 정답.**
10. **[신규] 시각 검수는 샘플이 아닌 전수 자동이 기본.** 사람 눈은 플래그만 찍음. **[cont.67 검증] sweep이 "실무 기준 미달" 포착도 가능함 증명됨.**
11. **[신규] 기획탭 자율성.** 기획탭은 이람에게 **방향**만 받는다. A/B/C 떠넘기기 금지. **[cont.67 확장] "기본 스웻셔츠 POM이 뭐야" 같은 질문 = 도메인 지식 아니라 일반 상식 범주. 웹 검색 + 공개 브랜드 사이즈 차트 + 산업 표준으로 내가 근거 제시하고 이람은 OK/NO.**

---

## 🚨 최우선 — 다음 세션 (cont.68 착수)

### ✅ cont.67 완전 마무리 (2026-04-21)

1. ✅ sweep 파이프라인 첫 작동 (`sweep_matrix.py` + 96장 PNG)
2. ✅ 이람 검수 결과 수신 (48 tile 전부 실무 미달, sweatshirt가 가장 근접)
3. ✅ 원칙 9/10/11 확장 해석 반영
4. ✅ Sweatshirt Size M 16 POM 제안 → 이람 OK
5. ✅ `docs/reference_data.md §6.2` Sweatshirt 섹션 병합 (§6.1 T-shirt 유지, §6.3 향후 preset 확장 템플릿 추가)
6. ✅ `docs/flat_sweatshirt_pom_proposal.md` 저장
7. ✅ `plan.md` Phase 2 완료 조건 재정의 (sweatshirt 1개 실무 도달 선행 조건) + Phase 3에 옵션 H 다른 preset 확장 추가 + 칼라 22종 감사 재평가 주석
8. ✅ `docs/flat_code_tab_cont68_option_h_sweatshirt.md` 저장 (코드탭 지시문)

### 🔥 다음 착수 (코드탭 cont.68) — 준비 완료

**코드탭이 할 일:** `HANDOFF.md 읽어줘` → 이 섹션 → `docs/flat_code_tab_cont68_option_h_sweatshirt.md` 전체 참조

**요약:**
- flat-v6.html에 `SFD_POM.sweatshirt.M` 상수 추가 (16 POM from `reference_data.md §6.2`)
- `BodyComp.geometry()`에 sweatshirt 분기 — SFD를 single source of truth로
- cm → 내부 단위 변환 (UNIT_SCALE ≈ 1/1.578, cont.66 POM 재조정 기준)
- 나머지 15 preset은 기존 primitive 유지 (Phase 3 확장 대상)
- 검증: 16×3 sweep NaN 0, 다른 preset 회귀 없음

**병행 가능:** Q3-b (PDF export SFD POM 시각 검증, BodyComp 무관)

---

## 🔴 기획 → 코드

### 2026-04-21 저녁 cont.67 — 3가지 핑퐁 답변 (유지)

- **Q1 Phase 재조정 3-tier:** 동의. plan.md 반영됨 (cont.66 + cont.67 세부 조정).
- **Q2 Six Atomic 96장:** (다) 기획탭 pick. 옵션 H sweatshirt 완성 → 그 다음 Six Atomic 참조해서 셔츠/칼라.
- **Q3 코드탭 중립 작업:** b만 지시 (PDF POM 검증). 옵션 H 진행 중 a/c/d/e 블록.

### ★ cont.68 착수 지시 (`docs/flat_code_tab_cont68_option_h_sweatshirt.md` 참조)

**입력:**
- `docs/reference_data.md §6.2` — Sweatshirt Size M 16 POM (이람 OK)
- `tools/audit/sweep/prod/sweatshirt_*_*.png` — baseline (before)

**코드 작업:**
- `SFD_POM.sweatshirt.M` 상수 추가
- `BodyComp.geometry()` sweatshirt 분기 (cm → 내부 단위 변환)
- 기존 15 preset 무변화
- sweep NaN/exception 0

**검증 후:**
- 기획탭 재sweep → `sweep/post_option_h/sweatshirt_*_*.png`
- 이람 before/after 비교 → Phase 2 (a) 완료 여부 판정

### 2026-04-21 이람 재보고 — Outerwear OK vs Crew Tee 퇴보 (옵션 H에 흡수)

cont.67 이람 전면 검수로 이 이슈는 **옵션 H에 흡수**. Crew Tee뿐 아니라 Outerwear 포함 48 tile 전부 실무 미달. 옵션 G → 옵션 H.

### 옵션 G (보류) — preset별 sleeve 파라미터 분리

cont.67에서 **옵션 H로 대체.** G는 옵션 H 실패 시 fallback 또는 미세 조정용.

### 확정 문서 (cont.67 마무리 기준)

| 분류 | 문서 | 핵심 |
|---|---|---|
| **전략** | flat_competitive_analysis_v5.md / flat_the_one_tool_scope.md / flat_strategy_brief_v3.md / flat_code_tab_handoff_v5.md / flat_phase_review_2026-04-20.md | Zero Translation / 파이프라인 / 로드맵 / 철학 / 3D 전략 |
| **설계 철학** | flat_design_philosophy_v1.0/1.1/1.2.md / flat_ux_architecture_v1.md | 원칙 1-11 + 대화 UX + 트레이싱 프리즈 / 넥 3축 + 카드피드 |
| **구조** | flat_category_restructure_final.md | 5카테고리 + HS코드 + Active Mode |
| **비주얼/칼라** | flat_visual_direction_review.md / flat_collar_direction.md / collar_geometry_cheatsheet.md / szkutnicka_collar_reference_map.md | 비례/방향/ratio/매핑 |
| **레퍼런스** | reference_data.md | §1-5 + §6.1 T SFD + **★ §6.2 Sweatshirt SFD (cont.67)** + §6.3 확장 템플릿 |
| | reference_donnanno_vol3.md | Stage 3+ |
| | fashionpedia_ch5_textile_notes.md | Stage 2 |
| **도구** | flat_designer_feedback_guide.md | 5월 인터뷰 |
| | **flat_sweatshirt_pom_proposal.md** ★ cont.67 | Sweatshirt 풀 제안서 (이람 OK) |
| | **flat_code_tab_cont68_option_h_sweatshirt.md** ★ cont.67 | **코드탭 cont.68 지시문** |
| **감사 도구** | tools/audit/inspect_flat.py / gallery.html | 단일/전수 검수 |
| | tools/audit/sweep_matrix.py ★ cont.67 | 16×3×2=96 PNG 생성 |
| | tools/audit/sweep/prod/*.png ★ cont.67 | baseline 96장 |

### 산출물 (docs/deliverables/)

| 파일 | 상태 |
|---|---|
| flat_levelup_application.docx | 4/17 제출 완료 |
| flat_ir_v4.3.pptx | 최신 |
| flat_yc_s26_application_draft.md | 5/4 전 숫자 반영 필요 |

### 보류 (유지)

- 칼라/소맷단/스커트/팬츠 — Phase 3+ (옵션 H 이후 재감사)
- eton/bertha/puritan/wing — Stage 3+
- TOPS 카테고리

### POM 질문 답변 (cont.65 → cont.66 → cont.67)

- **(나) ✅ cont.66 자율 완료:** SpecModule/PDF/POM diagram/CM_MAP 4곳 SFD 통일 (commit 4b5dd2d)
- **★ cont.67 확장:** BodyComp.geometry()까지 확장하는 게 옵션 H. cont.68 착수 예정

---

## 🔵 코드 → 기획

### 🟡 cont.68 옵션 H 중간 완료 (2026-04-22, commit b7b3b46 push)

**착수:** `docs/flat_code_tab_cont68_option_h_sweatshirt.md` 지시문대로 진행.

**추가된 것:**
- `SFD_POM.sweatshirt.M` 상수 (reference_data.md §6.2 이람 OK 16 POM)
- `SFD_VSCALE=2.549` / `SFD_HSCALE=1.038` (cont.66 POM 재조정에서 역산, anisotropic pixel/cm)
- `S.presetName` 필드 추가 + `PresetModule.apply`에서 명시 세팅
- `BodyComp.geometry()` sweatshirt 분기 — 기존 8 필드 + SFD 전용 7 필드 추가
- `BodyComp.armholeY()` sweatshirt 분기 — SFD armhole 28cm 직접 사용

**절충 판단 (원칙 11 자율, 지시문 §8 범위 내):**

지시문대로 SFD shoulder 51cm를 렌더에 쓰면 FLAT `BodyComp.outline()` 논리와 충돌:
- FLAT outline은 shoulder ≥ armpit 전제로 path 생성
- SFD: shoulder half 25.5cm (26.5px) < chest half 58cm (60.2px) → outline 역전
- 결과: raglan curve가 터무니없이 긴 대각선 (시각 확인 완료)

**해결 (절충):**
- **body chest / body length / armhole depth / hem rib / cuff rib = SFD**
- **shoulder / neck width / slope = FLAT 도식화 convention 유지**
- 실무 tech pack 관행: shoulder를 실제 수치보다 넓게 표현
- SFD shoulder는 cont.66 스펙시트에서 이미 정확 — 렌더는 convention, 스펙은 SFD (이중 트랙)

**근거:** 이람 피드백 핵심 "팔 품 넓음 + 리브 조이지 않음" 해결엔 body/rib만 SFD로 충분. shoulder는 이슈 아님.

**검증 (로컬):**
- crewTee 회귀 0 (halfBody 55, shoulderW 46, bodyH 181 — 완전 동일)
- 16 preset × 3 color sweep NaN/exception 0
- sweatshirt navy 렌더: drop shoulder raglan 자연스러움 + hem rib 영역 가시화 (이전 primitive 대비 확연 개선)

**미완 (다음 iteration 판정 요청):**
- 팔 품 (bicep) SFD 직접 적용 — 현재 SleeveComp는 기존 sleeveWidth primitive. SFD `sfdBicepHalf=13.0px` geometry에 있지만 SleeveComp 미참조.
- Cuff rib 조임 (sleeveOpening 5.2px) — SleeveComp cuff 렌더에 sfdCuffHalf 반영 필요.

**다음 단계 옵션 (기획탭 판단):**
1. **(B) 내 선호** — 먼저 SleeveComp sweatshirt 분기 (bicep + cuffOpen SFD) → 완성 후 재sweep. 지시문 §4.3 note 3 "cuffRibH/hemRibH 지원 렌더 경로" 맥락. 원칙 11 자율 범위로 진행 가능.
2. **(A)** 현재 상태로 이람 재sweep → "개선 정도" 판정 → 이후 SleeveComp 분기 판단.
3. **(C)** 절충 판단 반대 → BodyComp.outline까지 sweatshirt 분기 (SFD shoulder 엄격 적용). 큰 구조 변경.

**push: commit b7b3b46**

### ✅ cont.66 지시 전체 실행 완료 (2026-04-21, commit d98f5b2 + 4b5dd2d)

1. ✅ 버그 1/2 fix, 이슈 A 옵션 B, POM SFD 재조정
2. 📋 이슈 B 옵션 F 보류, cont.63 90° 블렌딩 → cont.67 옵션 H에 흡수

### 🟠 cont.66 말미 질문 → cont.67 답변됨

Q1 Phase 3-tier 동의 / Q2 Six Atomic (다) / Q3 중립 b만

### 🚨 cont.65 성과 + 한계 (유지)

시각 비교 누락 → cont.66 gallery.html + cont.67 sweep_matrix.py로 해결. **원칙 10 증명**: 전수 시각 검수로 "48 tile 전부 실무 미달" 포착.

### 코드 현황

- 엔진 v0.26s-5 + polo v2 + cont.66 이슈 A + cont.66 POM SFD (스펙/PDF)
- cont.66 d98f5b2 + 4b5dd2d push 완료
- **★ cont.68 착수 대기: `docs/flat_code_tab_cont68_option_h_sweatshirt.md` 지시문 준비됨**

### 📸 감사 방법

- ✅ 시각 sweep + side-by-side 갤러리 (원칙 10, cont.67 작동)
- ✅ 기획탭 DOM 실측 (`inspect_flat.py`)
- ✅ **옵션 H 검증: `sweep/prod/` (before) vs `sweep/post_option_h/` (after)**

---

## 🟡 양쪽 공유 TODO (cont.67 마무리 기준)

| 항목 | 기획 | 코드 | 상태 |
|---|---|---|---|
| push 버그1+2+이슈A | ✅ | ✅ cont.66 d98f5b2 | 완료 |
| POM SFD 재조정 (스펙/PDF) | ✅ | ✅ cont.66 4b5dd2d | 완료 |
| 시각 sweep 갤러리 구축 | ✅ cont.67 | — | 완료 |
| 이람 flat sweep 검수 | 번들 전달 | — | ✅ cont.67 (48/48 실무 미달) |
| Sweatshirt POM 제안 + 판정 | ✅ | — | ✅ cont.67 이람 OK |
| reference_data §6.2 sweatshirt 병합 | ✅ cont.67 | — | 완료 |
| plan.md Phase 2/3 재정렬 + 칼라 감사 주석 | ✅ cont.67 | — | 완료 |
| 코드탭 cont.68 지시문 저장 | ✅ cont.67 | — | 완료 |
| **🔥 옵션 H sweatshirt 구현 (cont.68)** | — | **착수 대기** | 최우선 |
| 기획탭 재sweep (after 비교) | cont.68 구현 후 | — | 대기 |
| **🔥 이람 before/after 검수** | after sweep 후 | — | 대기 |
| 중립 작업 b (PDF POM 검증) | ✅ Q3 b | 시각 확인 | 옵션 H와 병행 가능 |
| 중립 작업 a/c/d/e | Q3 보류 | 블록 | 옵션 H 검증 후 |
| Six Atomic 활용 (다) | ✅ Q2 | 실측 지시 대기 | sweatshirt 검증 후 |
| IR v4.3 비주얼 검수 | 📝 이람 | — | 대기 |
| YC 지원서 숫자 반영 | 📝 이람 | — | 5/4 전 |
| 1분 데모 영상 | 스크립트 ✅ | 캡처 | 옵션 H 후 녹화 |
| 디자이너 인터뷰 3명 | 📝 이람 | — | 5월 전 |
| factory validation | 성수동 섭외 | 검증 output | 5월 |

---

## 🟢 cont.67 최종 완료 로그

| 항목 | 상태 |
|---|---|
| sweep_matrix.py + 96장 PNG + 번들 | ✅ |
| 이람 검수 (48/48 실무 미달) | ✅ |
| 원칙 9·10·11 확장 해석 | ✅ |
| 옵션 H 방향 정의 | ✅ |
| Champion RW M + Gildan 18000 M 실측 웹 확보 | ✅ |
| Sweatshirt 16 POM 제안 + 이람 OK | ✅ |
| reference_data §6.2 sweatshirt 병합 | ✅ |
| flat_sweatshirt_pom_proposal.md 저장 | ✅ |
| plan.md Phase 2 완료 조건 재정의 | ✅ |
| plan.md Phase 3 옵션 H 확장 추가 | ✅ |
| plan.md 칼라 22종 감사 과대평가 주석 | ✅ |
| 코드탭 cont.68 지시문 저장 | ✅ |
| HANDOFF 섹션별 업데이트 | ✅ |

---

## 📂 파일 구조 (cont.67 최종)

```
/Users/yiram/Claude/flat/
├── HANDOFF.md          ← cont.67 마무리 (이 파일)
├── plan.md              ← cont.67 Phase 2/3 재정렬
├── progress.md
├── flat-v6.html
├── docs/
│   ├── reference_data.md                              ← §6.2 Sweatshirt SFD 추가 ★
│   ├── flat_sweatshirt_pom_proposal.md                ← ★ cont.67 신규
│   ├── flat_code_tab_cont68_option_h_sweatshirt.md    ← ★ cont.67 신규 (코드탭 지시문)
│   ├── flat_phase_review_2026-04-20.md
│   ├── audit_cont65_sweep.md
│   ├── [기타 확정 md 15종]
│   ├── archive/
│   │   ├── HANDOFF-20260421-cont66-before-cont67-sweep.md
│   │   └── [다른 백업들]
│   └── deliverables/
└── tools/
    └── audit/
        ├── inspect_flat.py
        ├── gallery.html
        ├── sweep_matrix.py                   ★ cont.67
        ├── sweep/
        │   ├── prod/*.png (96)              ★ cont.67 baseline (before)
        │   └── post_option_h/               ← cont.68 후 생성
        └── invariants.py                    ← 신규 예정

/mnt/user-data/outputs/
└── flat_sweep_bundle.zip                    ← cont.67
```

---

## 📏 규칙

1. 기획탭 → `docs/` + HANDOFF "기획→코드" 섹션만
2. 코드탭 → `progress.md` + HANDOFF "코드→기획" 섹션만
3. 세션 시작 → "HANDOFF.md 읽어줘"
4. 결정 필요 → HANDOFF에 질문
5. 수정 시 "마지막 수정" 갱신
6. **비주얼 "완료" → 기획탭 DOM 실측 재검증 (원칙 6)**
7. **전체 덮어쓰기 금지. 섹션 단위. 수정 전 백업 (원칙 7)**
8. **Stage=전략, Phase=구현 (원칙 8)**
9. **반복 피드백 시 magic number 중단. cont.67 확장: 국소 상수 분리도 primitive의 상수 분배일 수 있음. geometry 수식 자체 재구축 필요 여부 점검 (원칙 9)**
10. **시각 검수는 전수 자동 기본. 매 push마다 sweep + 갤러리 (원칙 10)**
11. **기획탭은 방향만 받고 실행 자율. "기본 X가 뭐야" 같은 일반 상식 질문은 이람한테 던지기 전에 내가 근거 찾아 제안 (원칙 11)**
