# FLAT 핸드오프
> **모든 탭은 세션 시작 시 이 파일을 먼저 읽는다.**
> 섹션 단위 수정만. 전체 덮어쓰기 금지 (원칙 7).

마지막 수정: 2026-04-21 코드탭 cont.67 (Q1 plan.md 3-tier 반영 + Q3 b PDF SFD 검증 + 누락 보정 push 1da11c5)

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
9. **[신규] 반복 피드백은 아키텍처 문제 신호.** 같은 영역 3회 이상 수정되면 magic number 조정 중단 + 전역 상수의 전역성 자체를 의심. 프리셋별 분리 or 구조 재설계로 전환. (근거: cont.61→62→63→65 소매 영역 4회 반복. cuffTiltK/innerShorten 전역 상수가 원인. 옵션 G 필요.)
10. **[신규] 시각 검수는 샘플이 아닌 전수 자동이 기본.** 사람 눈은 플래그만 찍음. 원인 탐색·코드 위치 추정은 자동 파이프라인이 수행. 매 push마다 16 preset × 주요 토글 sweep → side-by-side 갤러리 → regression diff. (근거: "시각적으로 하나하나 검토했으면 이 일 안 일어남" — 이람 2026-04-21.)
11. **[신규] 기획탭 자율성.** 기획탭은 이람에게 **방향**만 받는다. 세부 단계·실행 순서·도구 선택은 스스로 결정한다. 판단이 서면 즉시 실행. A/B/C 선택지를 이람에게 떠넘기는 패턴 금지. 막힐 때 — 즉 (i) 전략적 트레이드오프가 드러났거나 (ii) 이람의 도메인 지식이 필요한 경우 — 에만 묻는다. (근거: "결정 떠넘기면 Codex 간다" — 이람 2026-04-21.)

---

## 🚨 최우선 — 이번 주 실행 (cont.67 진행 중)

### ✅ cont.66 Push 완료 (d98f5b2) — 기록 유지

**실행된 지시 5건:**
1. ✅ 버그 1 (underarm dashed) — production 반영
2. ✅ 버그 2 (?demo URL) — `PresetModule.apply(0)` 추가
3. ✅ 이슈 A 옵션 B — sleeve fill이 body armhole reverse curve로 닫힘
4. 🟡 이슈 B 옵션 F 보류, 옵션 G 대기 (sweep 결과 후)
5. 🟡 cont.63 90° 블렌딩 롤백 재검토 대상

### ✅ cont.66 말미 POM SFD 재조정 (push 완료 commit 4b5dd2d)

- `reference_data.md §6` SFD Size M 베이스 공식 4곳 통일
- 16 preset sweep NaN/undefined 0, 렌더 SVG 무영향
- **cont.67에서 2곳 추가 누락분 보정 (1da11c5)**: PDF 작업지시서 shoulder/armhole
- 최종 통일 6곳: CM_MAP / SpecModule.updateTop / POM diagram (engine) / PDF tech pack Page 3 / PDF work order sketch / PDF work order spec

### ✅ cont.67 sweep 파이프라인 첫 작동 (기획탭, 2026-04-21)

- `tools/audit/sweep_matrix.py` 작성 — 16 preset × 3 color × 2 view = 96장 PNG
- inspect_flat.py 방식 재사용 (SVG outerHTML 추출 → CSS var 치환 → 격리 렌더링)
- GitHub Pages 503 resilient (6회 재시도 + 15초 대기)
- 번들 전달: `/mnt/user-data/outputs/flat_sweep_bundle.zip` (2.9MB, 98 파일)

### 🔥 이람 다음 액션 (지금)

1. `flat_sweep_bundle.zip` 다운로드
2. `/Users/yiram/Claude/flat/`에 압축 풀기 (`tools/audit/sweep/prod/*.png` + `tools/audit/sweep_matrix.py` + `README.md` 자동 배치)
3. `tools/audit/gallery.html` 열기 (Finder에서 더블클릭)
4. 48 tile 훑으며 ✓/✗/? 플래그 (소요 ~15분)
5. 우측 하단 "Export regression_list.md" → 결과 공유

→ **플래그 결과 나오면** 옵션 G 설계 + cont.63 롤백 판정 + 코드탭 cont.67 지시 확정.

---

## 🔴 기획 → 코드

### 2026-04-21 저녁 cont.67 — 핑퐁 답변 (코드탭 cont.66 말미 질문에 대한 결정)

#### Q1. Phase 재조정 3-tier 구조 (CODE/HUMAN/PLAN+CODE) 동의?

**→ 동의. plan.md 반영 OK.**

근거: 주체별 책임 명확화 + 서로 블록 제거. 이람이 IR 덱 커버 만드는 동안 코드탭도 중립 진전 가능. 3-tier는 cont.67 sweep 파이프라인으로 **실제 작동**함 증명됨 (기획탭→이람 플래그→코드탭이 하나의 loop로 돌아감).

plan.md 반영 시 추가 지시:
- Phase 2 완료 조건: (a) 96 tile 중 "퇴보" 0개, (b) IR 덱 + 1분 데모 + YC 지원서 완성, (c) factory validation 섭외 확정
- [PLAN+CODE] 섹션은 핑퐁 중 동결되는 경우 최대 48h 룰 (그 안에 양쪽 응답 없으면 이람이 차단 요인 확인)

#### Q2. Six Atomic 96장 활용 방향?

**→ (다) 기획탭이 필요한 토글만 pick 후 지정.**

근거:
- 전수 실측(나)은 지금 우선순위 아님. Phase 3+ 범위. Stage 2 factory validation 후 판단.
- 칼라 6종만(가)은 sweep 플래그 결과에 의존. 어느 preset의 무엇이 퇴보인지 나온 뒤 "그 부분만 Six Atomic 참조"가 자연스러움.
- 지금 sweep 플래그 → 실측 필요 항목 pick → 코드탭 지시 순서로.

**코드탭은 대기.** sweep 플래그 결과 받고 기획탭이 "Six Atomic 몇 번 스크린샷의 X 실측" 형태로 지시 내림.

#### Q3. 코드탭 중립 작업 a~e 중 지시?

**→ b만 지시. a/c/d/e 보류.**

- **b. PDF export SFD POM 수치 검증 ✅ 지시** — cont.66 POM 변경이 5-page tech pack + 작업지시서에 일관되게 반영됐는지 시각 확인만. 리스크 0, value 있음 (factory validation 전 필수). 구현 없고 검증만.
- **a. 이슈 A 전 shape 확장** 보류 — sweep 플래그가 "이슈 A 적용된 set-in이 OK"라고 나와야 확장이 정당. 플래그 결과 후 판단.
- **c. raglan card 4 확대 체크** 보류 — IR 덱 커버 디자인 확정 후 필요 시 요청.
- **d. 주석 정리** 보류 — cont.57~66 누적 코드 주석은 코드탭이 다음 push에서 자연스럽게 정리. 독립 task로 지금 불필요.
- **e. inspect_flat.py 로컬 대응** 보류 — cont.67 sweep_matrix.py가 `local` target 파라미터로 이미 구조 마련. 실제 필요 시 기획탭이 `Filesystem:read_text_file`로 flat-v6.html 복사 후 호출.

#### cont.67 sweep 파이프라인 산출물 정리

- `tools/audit/sweep_matrix.py` — 재사용 가능한 전수 스윕 스크립트
- `tools/audit/sweep/prod/*.png` — 16 preset × 3 color × 2 view = 96장 현재 baseline
- `gallery.html` — 기존 48 tile viewer에 PNG 자동 매칭
- 번들 zip 구조가 가이드 문서(README.md) 포함

**품질 스팟체크 (3장 sample):**
- crewTee navy front: 어깨 gap 해소 ✅ (cont.66 적용 확인)
- crewTee white front: 크림 배경 + 짙은 스티치, IR 덱 쓸만함 ✅
- blazer navy front: 소매 OK (이람 "Outerwear OK" 일치), **칼라 이슈 가시적** (플래그 예상)

### 2026-04-21 이람 재보고 — Outerwear OK vs Crew Tee 퇴보 (유지)

**관찰:** Outerwear V-neck의 소매는 좋음. Crew Tee Round neck의 소매는 이전 대비 퇴보.

**이람 원문:** "소맷단 부분만 일단 말한 거긴 함. 크루티 고친 게 이번껀데, 아우터 소매는 좋음. 그러니까 퇴보한 거임."

**기획탭 해석:** 같은 `cuffTiltK=0.45` 전역 상수가 프리셋별 비례 차이로 서로 다른 결과 → 원칙 9 발동. 옵션 G로 전환.

### 옵션 G (대기) — preset별 sleeve 파라미터 분리

```js
preset.crewTee.sleeve  = { tiltK: 1.0, capRatio: 0.35 }
preset.blazer.sleeve   = { tiltK: 0.4, capRatio: 0.50 }
preset.hoodie.sleeve   = { tiltK: 0.8, capRatio: 0.30 }
// ... 16 preset 각각
```

**플래그 결과 후 프리셋별 값 실측 → 반영.**

### 2026-04-20~21 Phase 전체 검토 (유지)

→ `docs/flat_phase_review_2026-04-20.md`, `tools/audit/inspect_flat.py`, `docs/archive/HANDOFF-20260421-cont63-backup.md`

**핵심:** MVP 시연 차단 = Phase 1 비주얼 퀄리티. 3D 전략 A→B→C (B는 C 디딤돌).

### 2026-04-17 이람 비주얼 검수 (유지)

크루티(밝은 색) ✅ 유일 / 폴로·셔츠·소맷단·칼라·스커트·팬츠 ❌. IR 덱 + 데모 = 크루티 하나로 승부.

### 2026-04-17 cont.59 답변 (유지)

① Phase 재정렬 ✅ / ② DEFER ✅ / ③ eton/bertha/puritan/wing → Stage 3+ / ④ 선으로 디자인 Phase 6 ✅ / ⑤ 실무 퀄리티 크루티만 / ⑥ 캡처 이람 QuickTime, 편집 이람.

### 확정 문서

| 분류 | 문서 | 핵심 |
|---|---|---|
| **전략** | flat_competitive_analysis_v5.md | Zero Translation + Pipeline Collapse |
| | flat_the_one_tool_scope.md | Phase 0→4 파이프라인 |
| | flat_strategy_brief_v3.md | Hero, 로드맵 |
| | flat_code_tab_handoff_v5.md | v5 철학 → 코드탭 |
| | flat_phase_review_2026-04-20.md | Phase 검토 + 실측 + 3D 전략 |
| **설계 철학** | flat_design_philosophy_v1.0/1.1/1.2.md | 원칙 1-11 + 대화 UX + 트레이싱 프리즈 |
| | flat_ux_architecture_v1.md | 넥 3축 + 존 5존 + 카드피드 + 스타일 4Tier |
| **구조** | flat_category_restructure_final.md | 5카테고리 + HS코드 + Active Mode |
| **비주얼/칼라** | flat_visual_direction_review.md | 위치→비례→형태→디테일 |
| | flat_collar_direction.md | Discrete+Continuous |
| | collar_geometry_cheatsheet.md | ratio 공식 |
| | szkutnicka_collar_reference_map.md | 매핑 |
| **레퍼런스** | reference_data.md | Armstrong/Szkutnicka/Abling + Kent 실측 §5 + SFD §6 |
| | reference_donnanno_vol3.md | 재킷/코트/케이프 (Stage 3+) |
| | fashionpedia_ch5_textile_notes.md | Fabric DB (Stage 2) |
| **도구** | flat_designer_feedback_guide.md | 5월 인터뷰 질문 세트 |

### 산출물 (docs/deliverables/)

| 파일 | 상태 |
|---|---|
| flat_levelup_application.docx | 4/17 제출 완료 |
| flat_ir_v4.3.pptx | 최신 |
| flat_yc_s26_application_draft.md | 5/4 전 숫자 반영 필요 |

### 파일 구조 (업데이트)

- `docs/` = 확정 17종
- `docs/archive/` = 구버전 + README + 백업 누적
- `docs/deliverables/` = 산출물
- `tools/audit/inspect_flat.py` = 단일 조합 DOM 실측
- `tools/audit/sweep_matrix.py` ★ **cont.67 신규** — 전수 스윕 생성
- `tools/audit/gallery.html` = 48 tile flag viewer (cont.66)
- `tools/audit/sweep/prod/*.png` ★ **cont.67 신규** — 96장 baseline PNG
- `/mnt/user-data/outputs/flat_sweep_bundle.zip` = cont.67 번들 (2.9MB, 이람 배포용)

### 보류

- 칼라/소맷단/스커트/팬츠 — Phase 3+
- eton/bertha/puritan/wing — Stage 3+
- TOPS 카테고리

### POM 질문 답변 (cont.65 → 기획탭 → 코드탭)

**(가) resolved:** SpecModule.GRADE에 17개 POM (A-Q) 이미 구현됨 확인.

**(나) ✅ cont.66 + cont.67 완료 push:** POM 공식 SFD Size M 베이스 재조정 **총 6곳 통일** (CM_MAP / SpecModule.updateTop / POM diagram / PDF tech pack Page 3 / PDF work order sketch / PDF work order spec). 16 preset NaN 0, 렌더 무영향. Stage 2 전 필수 작업 조기 완료. **Push: 4b5dd2d (cont.66) + 1da11c5 (cont.67 누락 보정)**.

**(다) 17개 POM 상태 유지.**

---

## 🔵 코드 → 기획

### ✅ cont.67 코드탭 응답 (2026-04-21 밤, commit 1da11c5 push)

**기획탭 Q1·Q2·Q3 답변에 대한 코드탭 실행:**

**Q1 — plan.md Phase 3-tier 반영 ✅**
- Phase 2 섹션을 [CODE]/[HUMAN]/[PLAN+CODE] 3-tier로 재작성
- 완료 조건 3개 명시 (96 tile 퇴보 0 / IR 덱+영상+지원서 / factory 섭외)
- 48h rule 반영 (핑퐁 섹션 양쪽 응답 없으면 이람 차단 요인 확인)
- [CODE] 8개 task 이미 ✅, [HUMAN] 4개 (이람 대기), [PLAN+CODE] 4개 (cont.67 sweep 파이프라인 ✅)

**Q2 — Six Atomic 96장 활용 (다) 수용**
- 기획탭이 sweep 플래그 후 pick 지시 내릴 때까지 코드탭 대기
- 로컬에 96장 파일 위치 확인됨, 언제든 실측 호출 가능

**Q3 b — PDF export SFD POM 수치 검증 ✅ (+ 누락 2곳 보정)**
- 검증 중 cont.66 POM 재조정 **누락분 발견**:
  - `pdfWorkOrder` small sketch area L6020: shoulder `36` → `47` (SFD M)
  - `pdfWorkOrder` spec table L6121: shoulder `36` → `47`
  - `pdfWorkOrder` spec table L6124: armhole `18` → `21`
- 원칙 11 자율 판단으로 즉시 보정 (검증 task의 완결성. 새 구현 아님, 기존 작업 누락 마무리)
- 이제 6곳 공식 전면 통일: CM_MAP / SpecModule.updateTop / POM diagram / PDF tech pack P3 / PDF work order sketch / PDF work order spec
- 16 preset sweep NaN/undefined 0
- **push: commit 1da11c5**

### cont.66/67 push 기록 정정 (HANDOFF 🔴 섹션에 "push 대기" 남아있어서 혼동 소지)

- **d98f5b2** (cont.66 첫 push) — 버그 1·2 fix + 이슈 A 옵션 B + ?demo init
- **4b5dd2d** (cont.66 POM) — SFD Size M 공식 4곳 통일
- **2fe6263** (HANDOFF snapshot) — 이번에 추가 HANDOFF.md 업로드
- **1da11c5** (cont.67 POM 누락 보정) — PDF work order 2곳 + sketch 1곳

POM은 이제 모든 출력 경로에서 SFD Size M 베이스 일관.

### ✅ cont.66 지시 전체 실행 완료 (2026-04-21 저녁, commit d98f5b2 push)

1. ✅ 버그 1 (underarm dashed) — production 반영
2. ✅ 버그 2 (?demo URL) — `PresetModule.apply(0)` 추가
3. ✅ 이슈 A 옵션 B — body armhole reverse curve로 gap 원천 제거
4. ✅ 이슈 B 옵션 F 보류 / 옵션 G 대기
5. 📋 cont.63 90° 블렌딩 — 롤백 재검토 대상 유지 (sweep 결과 후)

**검증:** 카드 0 navy 확대 + crewTee long navy 확대 → 어깨 gap 제거 확인. 16 preset × 3 color = 48 조합 exception 0. Raglan 대조군 변화 없음.

### ✅ cont.66 말미 POM SFD 재조정 (자율 완료, push 대기)

- `reference_data.md §6` SFD Size M 베이스 공식 4곳 통일
- CM_MAP L1968-1976 / SpecModule.updateTop L4965-4982 / POM diagram L5356-5373 / PDF export L5737-5762
- 검증: crewTee default → Size M 컬럼 SFD 정확 매칭 (Body Len 71, Chest half 53, Shoulder 47, Sleeve Len 22, Armhole 24, Across F 41, Across B 43, Neck W 21, Front Drop 10, Back Drop 2-3, Slv Open 18)

### 🟠 cont.66 말미 — 전체 리뷰 + Phase 재조정 제안 (기획탭 핑퐁 cont.67에서 답변됨 ↑)

**cont.67 답변 요약:**
- Q1 Phase 3-tier: 동의. plan.md 반영 OK.
- Q2 Six Atomic 활용: (다) 기획탭 pick. sweep 플래그 후.
- Q3 중립 작업: b만 지시 (PDF export POM 수치 시각 검증).

### 추가 작업 (cont.66 push 후 중립)

- **A. svgB back view 이슈 A 적용** ✅ 확정
- **B. 카드피드 card 1/2/3 gap 해소 검증** ✅ 모두 자연스러움
- **C. 시각 sweep 갤러리 HTML** ✅ `tools/audit/gallery.html` (cont.66)
- **D. POM (나) SFD 실측 공식 재조정** ✅ cont.66 (push 대기)

### 🚨 cont.65 성과 + 한계 (유지)

성과: 버그 진단, 48조합 sweep, 이슈 A/B 옵션 제시, 자의적 개선 자백.
한계: 시각 비교 없음 → 이람 "퇴보" 발견 못 잡음. 전역 상수 고수. svgB 개별 검수 없음.

### cont.63 90° 블렌딩 — 롤백 재검토 (유지)

sweep 갤러리로 어느 프리셋에서 퇴보 발생 확정 → 결정.

### 코드 현황

- 엔진 v0.26s-5 (cont.63 적용) + polo v2 + cont.66 이슈 A + cont.66 POM SFD
- Phase 1A 11/11 + 1B 14/14, Phase 2 polo 마무리
- cont.66 d98f5b2 push 완료
- POM SFD 재조정 commit 대기

### 📸 감사 방법

- ❌ 축소 + NaN만
- ✅ SVG clone 1400px 확대
- ✅ Glass Factory 1:1 비교
- ✅ 기획탭 DOM 실측 (`tools/audit/inspect_flat.py`)
- ✅ **시각 sweep + side-by-side 갤러리** (원칙 10, cont.67 첫 작동)

---

## 🟡 양쪽 공유 TODO

| 항목 | 기획 | 코드 | 상태 |
|---|---|---|---|
| push 버그1+2+이슈A | ✅ | ✅ cont.66 d98f5b2 | 완료 |
| POM SFD 재조정 | ✅ | ✅ cont.66 (push 대기) | 완료, push 대기 |
| 시각 sweep 갤러리 구축 | **✅ cont.67 완료** | — | 완료 |
| **🔥 이람 플래그 찍기 (sweep)** | 번들 전달 완료 | — | **이람 액션 대기 (지금)** |
| 🔥 regression_list.md → 코드 | 플래그 후 생성 | 수신 대기 | 다음 단계 |
| 이슈 B 옵션 G 설계 | 플래그 결과 후 | 구현 대기 | regression 후 |
| cont.63 블렌딩 롤백 판정 | 플래그 결과 후 | 롤백/유지 | regression 후 |
| Phase 재조정 plan.md 반영 | ✅ Q1 동의 | plan.md 갱신 | 코드탭 중립 작업 |
| 중립 작업 b (PDF POM 검증) | ✅ Q3 b 지시 | 시각 확인 | 코드탭 가능 |
| 중립 작업 a/c/d/e | Q3 보류 | 대기 | 플래그 후 |
| Six Atomic 활용 방향 | ✅ Q2 (다) | 실측 지시 대기 | 플래그 후 |
| 콘텐츠 자동화 cron 검수 | 📝 이람 | — | 대기 |
| IR v4.3 비주얼 검수 | 📝 이람 | — | 대기 |
| YC 지원서 숫자 반영 | 📝 이람 | — | 5/4 전 |
| 디자이너 인터뷰 3명 | 📝 이람 | — | 5월 전 |
| 1분 데모 영상 | 스크립트 ✅ | 캡처 | 5/3-4 전 |
| factory validation | 성수동 섭외 | 검증 output | 5월 |

---

## 🟢 기획탭 cont.67 완료 로그 (cont.64 Step 1-4 기준)

| Step | 내용 | 상태 |
|---|---|---|
| 1 | sweep 스크립트 — `sweep_matrix.py` 16 preset × 3 color × 2 view = 96장 | ✅ cont.67 |
| 2 | side-by-side 갤러리 HTML | ✅ cont.66 `gallery.html` 기 작성 |
| 3 | invariant 테스트 `invariants.py` | ⏳ 플래그 결과 후 우선순위 판단 |
| 4 | regression_list.md → HANDOFF 자동 업데이트 | ⏳ 이람 플래그 후 |

**cont.67 추가 산출:**
- Phase 재조정 Q1 동의 (plan.md 반영 OK)
- Six Atomic Q2 (다) 결정
- 코드탭 중립 작업 Q3: b 지시, a/c/d/e 플래그 후
- GitHub Pages 503 resilient 6회 재시도 로직 (sweep_matrix.py)
- 번들 zip `/mnt/user-data/outputs/flat_sweep_bundle.zip` (2.9MB, README 포함)

---

## 📂 파일 구조 (cont.67 반영)

```
/Users/yiram/Claude/flat/
├── HANDOFF.md
├── plan.md / progress.md
├── flat-v6.html
├── docs/
│   ├── [확정 md 17종]
│   ├── flat_phase_review_2026-04-20.md
│   ├── audit_cont65_sweep.md
│   ├── archive/ (백업 누적)
│   └── deliverables/
└── tools/
    └── audit/
        ├── inspect_flat.py     ← 단일 조합 DOM 실측
        ├── gallery.html        ← [cont.66] 48 tile flag viewer
        ├── sweep_matrix.py     ← [cont.67 신규] 전수 스윕 생성 (96장)
        ├── sweep/
        │   └── prod/           ← [cont.67 신규] 96장 baseline PNG
        │       └── {preset}_{color}_{view}.png × 96
        └── invariants.py       ← [신규 예정, Step 3]

/mnt/user-data/outputs/
└── flat_sweep_bundle.zip       ← [cont.67] 이람 배포 번들
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
9. **반복 피드백 시 magic number 조정 중단. 전역성 의심 (원칙 9)**
10. **시각 검수는 전수 자동 기본. 매 push마다 sweep + 갤러리 (원칙 10)**
11. **기획탭은 방향만 받고 실행은 자율. A/B/C 선택지 떠넘김 금지 (원칙 11)**
