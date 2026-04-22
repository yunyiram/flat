# FLAT 핸드오프
> **모든 탭은 세션 시작 시 이 파일을 먼저 읽는다.**
> 섹션 단위 수정만. 전체 덮어쓰기 금지 (원칙 7).

마지막 수정: 2026-04-22 코드탭 cont.68 Part 2 축소판 완료 — SleeveComp sweatshirt sleeveOpening SFD 10cm 적용 (cuffHalfW override, g.sfdCuffHalf 5.19px), cuffWidth 10.54px 수치 검증, crewTee 회귀 0, 16 preset NaN 0. 기획탭 sweep 대기.

---

## 📌 핵심 원칙 (양쪽 공유)

1. **수학적 정확성(internal) + 시각적 자연스러움(external)** 동시 충족.
2. **프리셋=시작점, 디테일=토글, 파라미터=슬라이더, 스타일=aesthetic 조합.**
3. **카테고리=construction+인식.** 차단 대신 안내.
4. **현실 과대평가 금지.** "구현됨" ≠ "앞에 내밀 수 있음".
5. **영감이 생산으로 변하는 순간이 보인다.** 트레이싱 프리즈.
6. **검증 가능한 산출물 없으면 "완료" 판정 금지.**
7. **HANDOFF 전체 덮어쓰기 금지.** 섹션 단위 수정만. 수정 전 백업.
8. **용어 분리.** Stage=전략, Phase=구현.
9. **[cont.67 확장] 반복 피드백 = 아키텍처 문제 신호.** 국소 상수 분리도 primitive 안 상수 분배일 수 있음. geometry 수식 재구축(옵션 H) 정답.
10. **[신규] 시각 검수는 샘플 아닌 전수 자동.** sweep이 "실무 기준 미달" 포착 증명됨.
11. **[신규] 기획탭 자율성.** 방향만 받고 A/B/C 떠넘기기 금지. 일반 상식 질문은 내가 근거 찾아 제안.
12. **[cont.67 말미] 공룡기업 공개 데이터 적극 활용.** Layer 1 (브랜드) → Layer 2 (ISO/ASTM/NHANES) → Layer 3 (AI agent). 직접 수집/추정 전에 웹 검색 먼저.
13. **[cont.67 말미 Part 3] 자동 진행 모드 (묵시적 OK).** 이람은 지적/수정/중단/전환 4가지만. `docs/flat_preset_expansion_workflow.md` 참조. **[Part 3 말미 재정의]** 자동 cycle 대상이 **preset 확장이 아니라 UX/UI 매력도 작업**으로 pivot (원칙 14 적용).
14. **[신규 cont.67 말미 Part 3] 매력도가 정확도 앞서는 구간이 있다.** 3D 연동 이전 구간에서는 **UX/UI 매력도 우선.** 실무 정확도는 **factory validation 통과 수준까지만.** 그 이상 에너지는 UX/UI로.
    - **근거:** Tailornova 13년 + YC + parametric tech = $186K/년 (기술 ROI 낮음). Raspberry AI $28.5M = 시각화 투자. FLAT 강점 = 이람 비주얼 디렉터 10년 + 쉬운 UX. 옵션 H sweatshirt 코드 작업은 3D 오면 재구성될 interim fix.
    - **적용:**
      - sweatshirt: cont.68 Part 2 **축소판 완주** (sleeveOpening rib 조임만 SFD 필수, bicep 선택, 이상 DEFER) → "보여줄만" 수준 확인 → 종료
      - crewTee/hoodie §6.3/6.4: **제안서 + reference_data 병합 유지** (Phase 4 canonical), **코드 구현 DEFER**
      - polo/shirt/blazer/dress 원칙 13 자동 cycle: **보류** (Phase 4로 DEFER)
      - 기획탭 주 작업 **UX/UI 매력도로 pivot** (Phase 3A)
    - **참조:** `plan.md` — Phase 2 축소 / Phase 3A UX/UI 신규 / Phase 3B factory / Phase 4 3D+옵션 H 통합

---

## 🚨 최우선 — 지금 진행 중 (cont.67 말미 Part 3 완전 마무리)

### 🟢 cont.67 말미 Part 3 완료 (2026-04-22)

1. ✅ **원칙 14 등록** — 이람 메타 선언 "3D 이전엔 매력도 우선, 정확도는 validation 통과까지만, 보여지는 것에 집중"
2. ✅ **plan.md 전면 재조정** — Phase 2 축소 (sweatshirt "개선 가시화" 수준으로, 실무 수준 목표 → Phase 3B/4) + Phase 3A UX/UI 집중 신규 + Phase 3B factory 최소 요구 + Phase 4 3D+옵션 H 나머지 흡수
3. ✅ **HANDOFF 원칙 14 sync** (이 문서)
4. ✅ **코드탭 cont.68 Part 2 지시 축소** — 아래 "🔴 기획 → 코드" 섹션 참조

### 🔥 최우선 블록 1 — 코드탭 cont.68 Part 2 축소판

**원칙 14 적용. 기존 지시문 `docs/flat_code_tab_cont68_option_h_sweatshirt.md` 범위 축소:**

| 항목 | 축소 전 | 축소 후 (원칙 14) |
|---|---|---|
| SleeveComp bicep SFD | 필수 | **선택** (여유 있으면) |
| SleeveComp sleeveOpening (rib 조임) SFD | 필수 | **필수** (이람 피드백 핵심, "리브 조이지 않음" 해결) |
| Cuff rib 세로 영역 렌더 | 필수 | **선택** |
| Sleeve 곡선/cap 모양 개선 | 필수 | **DEFER → Phase 4** |
| 기타 SleeveComp 정밀화 | 필수 | **DEFER → Phase 4** |

**코드탭 자율 범위 (원칙 11):** `sleeveOpening` 하나만 SFD 10cm (bicep 대비 0.40) 적용 성공하면 Part 2 완료 판정. 이람 눈에 "팔이 좁아지는 모양이 자연스럽나?" 정도만 확인.

**검증:** crewTee 회귀 0, 16×3 sweep NaN 0, sweatshirt 렌더: cuff 영역이 sleeveOpening < bicep 으로 좁아짐 가시화.

**push 후:** 기획탭 재sweep → 이람 before/after 비교 → "개선 가시화 OK" 또는 "더 필요" → Phase 2 (a) 완료 판정.

### 🔥 최우선 블록 2 — Phase 3A UX/UI 1순위 결정 (이람)

`plan.md` Phase 3A 후보 6개 중 **"가장 먼저 끌어올리고 싶은 것 1개"** 이람 선택 → 기획탭이 상세 방향 문서화 → 코드탭이 구현. 나머지는 순차.

6개 후보:
1. 카드 피드 비주얼 폴리시 (첫 5초 훅)
2. 트레이싱 프리즈 애니메이션 (IR 덱 커버와 연동)
3. cascade 시각화 부드러움 (아하 모먼트)
4. 대화 UX Phase 1 (FLAT이 먼저 말한다)
5. 컬러/마테리얼 바리에이션 전환
6. 데모 영상 60초 시나리오 (YC/S.STAGE 직접)

**내 추천:** 6 (데모 영상 60초). 5/3-4 마감 직접. 나머지 1~5가 영상 안에 녹아들므로 "영상 시나리오" 잡으면 다른 것들의 구현 우선순위 자동 결정.

### 🔥 블록 대기 — 이람 sweatshirt before/after 검수

코드탭 cont.68 Part 2 축소판 push + 기획탭 재sweep 후.

---

## 🔴 기획 → 코드

### cont.67 말미 Part 3 완전 마무리 핵심 (2026-04-22)

**원칙 14 등록 + Phase pivot:**
- preset 확장 cycle (polo/shirt/blazer/dress) → **Phase 4로 DEFER**
- crewTee/hoodie 코드 구현 → **Phase 4 3D와 동기**
- 기획탭 자율 작업 대상이 preset 조사 → **UX/UI 매력도 작업**으로 변경
- sweatshirt는 "보여줄만" 수준까지만 (Part 2 축소판 완주)

**코드탭 cont.68 Part 2 지시 축소 (위 🔥 블록 1 참조):**

기존 `docs/flat_code_tab_cont68_option_h_sweatshirt.md` §4 "SleeveComp sweatshirt 분기" 부분에서:
- **필수 남김**: `sleeveOpening` (rib 조임) SFD 10cm 적용. `SleeveComp`에 `isSweatshirt` 분기 추가 후 cuff 렌더 X 좌표를 `sfdCuffHalf ≈ 5.2px` 로 제약.
- **선택**: bicep SFD, cuff rib 세로 영역 시각화.
- **DEFER → Phase 4**: sleeve 곡선/cap 정밀화, 다른 preset SleeveComp 분기.

**병행 OK**: cont.66 Q3 중립 작업 b (PDF POM 시각 검증).

### cont.67 답변 (유지)

Q1 Phase 3-tier 동의 / Q2 Six Atomic (다) / Q3 b만

### 확정 문서 (cont.67 말미 Part 3 완전 마무리)

| 분류 | 문서 | 비고 |
|---|---|---|
| **전략** | flat_competitive_analysis_v5.md / flat_the_one_tool_scope.md / flat_strategy_brief_v3.md / flat_code_tab_handoff_v5.md / flat_phase_review_2026-04-20.md | Zero Translation / 파이프라인 / 로드맵 / 철학 / 3D |
| **설계 철학** | flat_design_philosophy_v1.0/1.1/1.2.md / flat_ux_architecture_v1.md | 원칙 1-14 + 대화 UX + 트레이싱 프리즈 + 넥 3축 + 카드피드 |
| **구조** | flat_category_restructure_final.md | 5카테고리 + HS코드 + Active Mode |
| **비주얼/칼라** | flat_visual_direction_review.md / flat_collar_direction.md / collar_geometry_cheatsheet.md / szkutnicka_collar_reference_map.md | 비례/방향/ratio/매핑 |
| **레퍼런스** | reference_data.md | §1-5 + §6.1 T + §6.2 sweat + §6.3 crewTee + §6.4 hoodie + §6.5 향후 (Phase 4 canonical) + §6.6 티어 |
| | reference_donnanno_vol3.md / fashionpedia_ch5_textile_notes.md | Phase 4 활용 |
| **도구 (문서)** | flat_designer_feedback_guide.md / flat_sweatshirt_pom_proposal.md / flat_crewTee_pom_proposal.md / flat_hoodie_pom_proposal.md | 제안서 모음 |
| | flat_code_tab_cont68_option_h_sweatshirt.md | 코드탭 지시문 (Part 2 축소판으로 해석) |
| | **flat_preset_expansion_workflow.md** | **Phase 4 활용 (지금 실행 보류)** |
| **검수 도구** | tools/audit/inspect_flat.py / gallery.html / sweep_matrix.py / sweep/prod/*.png | 단일/전수 검수 + baseline |
| **연구 도구** | **tools/preset_research.html** v1.1 | 수동 fallback (Phase 4 활용) |

### 산출물 (docs/deliverables/)

| 파일 | 상태 |
|---|---|
| flat_levelup_application.docx | 4/17 제출 완료 |
| flat_ir_v4.3.pptx | 최신 |
| flat_yc_s26_application_draft.md | 5/4 전 숫자 반영 필요 |

### 보류 (Phase 4로 이동)

- 옵션 H 나머지 preset 코드 (crewTee/hoodie/polo/shirt/blazer/bomber/trench/cardigan/dress)
- 칼라 22종 재감사
- 앞/뒤 비대칭, 패턴메이킹 정확도
- 원칙 13 자동 preset cycle (polo/shirt/blazer/dress 제안서 작성)

### POM 질문 답변 체인 (cont.65→66→67→68)

- **(나) ✅ cont.66:** Spec/PDF/POM/CM_MAP 4곳 SFD 통일 (commit 4b5dd2d)
- **★ cont.67:** BodyComp.geometry() 확장 = 옵션 H 방향
- **★ cont.68 Part 1 (b7b3b46):** BodyComp body/rib/armhole SFD + shoulder FLAT convention (절충)
- **★ cont.68 Part 2 축소판 (착수 대기):** SleeveComp sweatshirt sleeveOpening만 필수. bicep 선택. 이상 DEFER.
- **Phase 4:** 3D 연동과 함께 전면 재구성 (현재 SFD 데이터 canonical로 활용)

---

## 🔵 코드 → 기획

### 🟢 cont.68 옵션 H Part 2 축소판 완료 (2026-04-22, commit 대기)

**작업:** `SleeveComp.draw()` L2924 `cuffHalfW` 분기 — `S.presetName==='sweatshirt' && g.sfdCuffHalf` 일 때 `g.sfdCuffHalf`(=5.19px, SFD 10cm half)로 override. 기존 `sleeveCapW*taperFactor*lenTaper` 로직은 그대로 다른 15 preset 사용.

**원칙 14 축소 범위 준수:**
- ✅ **필수:** sleeveOpening (rib 조임) SFD 적용 — 이람 피드백 "리브 조이지 않음" 직접 해결
- ⏸ **선택 스킵:** bicep SFD (기존 sleeveCapW 유지)
- ⏸ **선택 스킵:** cuff rib 세로 영역 별도 렌더
- 🔒 **DEFER → Phase 4:** sleeve cap/곡선 정밀화, 다른 preset 옵션 H

**수치 검증 (DOM 실측, 원칙 6):**
| 항목 | Before (cont.68 Part 1) | After (Part 2 축소판) |
|---|---|---|
| sweatshirt cuff width (L+R 대칭) | ~72px (sleeveCapW × 0.725) | **10.54px** (2 × g.sfdCuffHalf 5.19) |
| bicep ratio (cuff / sleeveCapW) | 1.00 | ~0.23 |
| crewTee halfBody | 55 | **55** (회귀 0) |
| crewTee shoulderW | 46 | **46** (회귀 0) |
| 16 preset sweep NaN | 0 | **0** |
| 16 preset sweep undefined | 0 | **0** |

**소매 시각 결과:** cap(armhole)에서 bicep까지는 기존 sleeveCapW 기반 넓이, bicep→cuff는 5.19px로 급격히 좁아짐. raglan + straight + rib cuff + long sleeve 조합에서 "rib cuff 조임" 가시화. cont.67 sweep baseline 대비 명확한 차이 기대.

**원칙 11 자율 판단:**
- sweatshirt 판정은 `S.presetName==='sweatshirt'` 명시 체크 (cont.68 Part 1과 동일 트리거)
- bicep SFD 적용 안 함 — 축소판 지시 "sleeveOpening만 필수" 준수. 결과가 자연스럽지 않으면 Phase 4에서 추가
- sleeveShape 'bell'/'bishop' 등의 특수 shape에서도 override 적용되지만 sweatshirt default shape='straight' 이므로 무영향

**미완 (Phase 4 DEFER):**
- bicep SFD, cuff rib 세로 시각화, sleeve cap 모양 개선
- crewTee/hoodie/polo/shirt/blazer 등 다른 preset 옵션 H
- 칼라 22종 재감사

**다음 (기획탭):** push 후 sweep 재실행 → `tools/audit/sweep/post_option_h/sweatshirt_*_*.png` 생성 → 이람 before/after 비교 → Phase 2 (a) 완료 판정.

### 🟢 cont.68 옵션 H Part 1 완료 (2026-04-22, commit b7b3b46)

**작업:** SFD_POM.sweatshirt.M + SFD_VSCALE/HSCALE + S.presetName + BodyComp.geometry() + BodyComp.armholeY() sweatshirt 분기.

**절충 (원칙 11):** body/rib/armhole SFD, shoulder/neck/slope FLAT convention.

**검증:** crewTee 회귀 0, 16×3 sweep NaN 0, 드롭숄더 + hem rib 가시화.

**미완 (Part 2 축소판 대상):** sleeveOpening rib 조임.

**다음:** 기획탭 (B)안 OK → **축소판 지시로 범위 좁힘** (원칙 14, 2026-04-22 Part 3 말미). sleeveOpening만 SFD 필수, bicep 선택, 이상 DEFER.

### ✅ cont.66 지시 완료 (commit d98f5b2 + 4b5dd2d)

### 🚨 cont.65 성과 — 원칙 10 증명

### 코드 현황

- 엔진 v0.26s-5 + cont.66 이슈A + cont.66 SFD + cont.68 Part 1 + cont.68 Part 2 축소판
- commit d98f5b2 + 4b5dd2d + b7b3b46 + **cont.68 Part 2 commit 대기**
- ✅ sleeveOpening SFD 10cm (rib 조임) 적용 — cuffWidth 10.54px 수치 검증
- Part 2 후 DEFER: 다른 preset 옵션 H 구현, 칼라 재감사 등 → Phase 4

### 📸 감사 방법

- ✅ 전수 sweep + 갤러리
- ✅ DOM 실측
- ✅ **옵션 H 검증:** `sweep/prod/` vs `sweep/post_option_h/`

---

## 🟡 양쪽 공유 TODO (cont.67 말미 Part 3 완전 마무리 기준)

| 항목 | 기획 | 코드 | 상태 |
|---|---|---|---|
| sweatshirt SFD §6.2 + 이람 OK | ✅ | — | 완료 |
| crewTee §6.3 자동 병합 | ✅ Part 3 | — | 완료 (암묵 OK) |
| hoodie §6.4 자동 병합 | ✅ Part 3 | — | 완료 (암묵 OK) |
| 옵션 H Part 1 (BodyComp) | — | ✅ b7b3b46 | 완료 |
| 옵션 H Part 2 축소판 (SleeveComp sleeveOpening) | 축소 지시 명시 | ✅ commit 대기 | 완료 (cuff 10.54px 검증) |
| **🔥 기획탭 재sweep (Part 2 후)** | Part 2 후 | — | 착수 가능 |
| **🔥 이람 sweatshirt before/after 검수** | sweep 후 | — | 대기 |
| **🔥 Phase 3A UX/UI 1순위 결정 (이람)** | 질문 대기 | — | 최우선 |
| preset_expansion_workflow.md (Phase 4 활용) | ✅ | — | 완료 (보류 중) |
| 원칙 12·13·14 등록 | ✅ | — | 완료 |
| preset_research.html v1.1 | ✅ | — | 완료 |
| plan.md 전면 재조정 | ✅ Part 3 | — | 완료 |
| 중립 작업 b (PDF POM 검증) | ✅ Q3 | 시각 확인 | Part 2와 병행 OK |
| **Phase 4 DEFER 항목** | polo/shirt/blazer/dress cycle | crewTee/hoodie/polo 등 코드 | 3D 연동 시 |
| **콘텐츠 자동화 (원칙 14 재포지셔닝)** | FLAT 브랜드 톤 문서 + 포맷 1개 선택 | ✅ daily 수집 + /content-review 스킬 | 기획 답변 대기 |
| IR v4.3 비주얼 검수 | 📝 이람 | — | 대기 |
| YC 지원서 숫자 반영 | 📝 이람 | — | 5/4 전 |
| 1분 데모 영상 | Phase 3A 1순위 후 | 캡처 | 5/3-4 |
| 디자이너 인터뷰 3명 | 📝 이람 | — | 5월 전 |
| factory validation | 성수동 섭외 (Phase 3B) | 검증 output | 5월 |

---

## 🟢 cont.67 최종 완료 로그 (Part 1 + 2 + 3 완전 마무리)

| 항목 | 상태 |
|---|---|
| sweep_matrix.py + 96 baseline | ✅ |
| 이람 검수 (48/48 미달) | ✅ |
| 원칙 9/10/11/12/13/14 등록 | ✅ |
| 옵션 H 방향 + Part 1 구현 | ✅ b7b3b46 |
| Sweatshirt 16 POM + §6.2 + 이람 OK | ✅ |
| crewTee 14 POM + §6.3 (암묵 OK) | ✅ Part 3 |
| hoodie 18 POM + §6.4 (암묵 OK) | ✅ Part 3 |
| preset_expansion_workflow.md | ✅ (Phase 4 활용) |
| **원칙 14 등록 + Phase 전면 재조정** | ✅ Part 3 완전 마무리 |
| plan.md Phase 2 축소 + 3A 신규 + 3B factory + 4 통합 | ✅ |
| 칼라 22종 감사 과대평가 주석 | ✅ |
| 코드탭 cont.68 지시문 + 축소판 해석 | ✅ |
| preset_research.html v1.1 | ✅ |
| 코드탭 cont.68 Part 1 회신 (B) OK → 축소 | ✅ |
| HANDOFF 원칙 14 + Phase pivot sync | ✅ 이 문서 |

---

## 📂 파일 구조 (cont.67 말미 Part 3 완전 마무리)

```
/Users/yiram/Claude/flat/
├── HANDOFF.md          ← cont.67 말미 Part 3 완전 마무리 (이 파일, 원칙 14 + Phase pivot sync)
├── plan.md              ← Phase 2 축소 + 3A UX/UI 신규 + 3B factory + 4 3D+옵션 H 통합
├── progress.md
├── flat-v6.html         ← cont.68 Part 1 (b7b3b46)
├── docs/
│   ├── reference_data.md                              ← §6.2/6.3/6.4 (Phase 4 canonical)
│   ├── flat_sweatshirt_pom_proposal.md                ★
│   ├── flat_crewTee_pom_proposal.md                   ★
│   ├── flat_hoodie_pom_proposal.md                    ★
│   ├── flat_preset_expansion_workflow.md              ★ (Phase 4 활용, 지금 보류)
│   ├── flat_code_tab_cont68_option_h_sweatshirt.md    ★ (Part 2 축소판으로 해석)
│   ├── flat_phase_review_2026-04-20.md
│   ├── audit_cont65_sweep.md
│   ├── [기타 확정 md 15종]
│   ├── archive/
│   └── deliverables/
└── tools/
    ├── preset_research.html              v1.1 (Phase 4 활용)
    └── audit/
        ├── inspect_flat.py / gallery.html / sweep_matrix.py
        └── sweep/
            ├── prod/*.png (96)           ★ cont.67 baseline (before)
            └── post_option_h/            ← cont.68 Part 2 축소판 후 생성

/mnt/user-data/outputs/
└── flat_sweep_bundle.zip                 ← cont.67
```

---

## 📏 규칙

1. 기획탭 → `docs/` + HANDOFF "기획→코드"
2. 코드탭 → `progress.md` + HANDOFF "코드→기획"
3. 세션 시작 → "HANDOFF.md 읽어줘"
4. 결정 필요 → HANDOFF에 질문 (원칙 13에 의해 자동 진행 가능하나, 원칙 14에 의해 지금은 UX/UI로 범위 pivot)
5. 수정 시 "마지막 수정" 갱신
6. **비주얼 "완료" → DOM 실측 재검증 (원칙 6)**
7. **전체 덮어쓰기 금지. 섹션 단위. 백업 (원칙 7)**
8. **Stage=전략, Phase=구현 (원칙 8)**
9. **반복 피드백 시 magic number 중단 (원칙 9)**
10. **시각 검수 전수 자동 기본 (원칙 10)**
11. **기획탭 자율. 일반 상식 질문은 내가 근거 찾아 제안 (원칙 11)**
12. **공룡기업 공개 데이터 먼저. Layer 1 → 2 → 3 (원칙 12)**
13. **자동 진행 모드. 묵시적 OK 전제. 지적/수정/중단/전환만 (원칙 13, 대상 UX/UI로 pivot)**
14. **매력도가 정확도 앞서는 구간. 3D 이전엔 UX/UI 우선, 정확도는 validation 통과 수준까지. preset 확장 코드는 Phase 4 DEFER (원칙 14)**
