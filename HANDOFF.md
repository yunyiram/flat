# FLAT 핸드오프
> **모든 탭은 세션 시작 시 이 파일을 먼저 읽는다.**
> 섹션 단위 수정만. 전체 덮어쓰기 금지 (원칙 7).

마지막 수정: 2026-04-21 코드탭 cont.66 전체 리뷰 + Phase 재조정 제안 + Six Atomic 96장 확인 보고

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

## 🚨 최우선 — 이번 주 실행 (cont.66)

### Push 지시 (코드탭이 즉시 실행)

**다 묶어서 한 번에 push:**

1. **버그 1 (underarm dashed):** 로컬에 이미 수정됨, production에만 존재 → 그냥 push
2. **버그 2 (?demo URL):** cont.65 로컬에 수정됨 (`PresetModule.apply(0)` 추가) → 그냥 push
3. **이슈 A (어깨 gap):** 옵션 B 적용 — sleeve fill이 armpit 안쪽으로 overlap (단기 봉합)
4. **이슈 B (cuff 각도):** 옵션 F **보류**. 옵션 G(preset별 `sleeve.tiltK`/`capRatio` 파라미터 분리)로 재설계 task 신설. 이번 push에 포함 안 됨. `cuffTiltK=0.45`, `innerShorten=armholeH*0.10` 현상 유지.
5. **cont.63 90° 블렌딩:** 롤백 재검토 대상으로 이동 (이람 보고: Outerwear OK vs Crew Tee 퇴보 → cTilt 공식이 프리셋별 영향 다름). sweep 결과 보고 결정.

### Push 후 필수

- 기획탭이 `python3 tools/audit/inspect_flat.py crew long` 재검증 (원칙 6)
- 아웃커머·크루티 양쪽 DOM + 확대 비교 (원칙 10 시각 검수)
- regression 확인 후에만 다음 단계 진입

---

## 🔴 기획 → 코드

### 2026-04-21 이람 재보고 — Outerwear OK vs Crew Tee 퇴보 (2장 스크린샷)

**관찰:** Outerwear V-neck(Cardigan/Funnel/Blazer/Bomber/Trench 중 어느 것인지 미확인, cont.64 질문)의 소매는 좋음. Crew Tee Round neck의 소매는 이전 대비 퇴보.

**이람 원문:** "소맷단 부분만 일단 말한 거긴 함. 크루티 고친 게 이번껀데, 아우터 소매는 좋음. 그러니까 퇴보한 거임. 이거 근데 반복해서 여러번 줬던 피드백이라서, 나도 어떻게 대답해야할지 판단이 안 섬."

**기획탭 해석:**
- 같은 `cuffTiltK=0.45` 전역 상수가 프리셋별 비례 차이 때문에 서로 다른 결과 → **원칙 9 발동 조건 충족**
- cont.63 "롤백 불필요" 이전 판정 번복 — 퇴보 증거 있음
- 이슈 B의 옵션 F(또 다른 magic number 조정)는 같은 악순환 반복. 옵션 G로 전환.

### 옵션 G (신규) — preset별 sleeve 파라미터 분리

현재 (전역):
```
cuffTiltK = 0.45
innerShorten = armholeH * 0.10
```

바꿔야 할 형태 (프리셋별):
```js
preset.crewTee.sleeve = { tiltK: 1.0,  capRatio: 0.35 }  // 얕은 cap
preset.blazer.sleeve  = { tiltK: 0.4,  capRatio: 0.50 }  // 깊은 cap
preset.hoodie.sleeve  = { tiltK: 0.8,  capRatio: 0.30 }
preset.cardigan.sleeve = { tiltK: 0.5, capRatio: 0.45 }
// ... 16 preset 각각
```

이게 "B방식 숨은 3D skeleton"의 첫 단계. 각 프리셋이 실제로 다른 armhole/sleeve 해부학을 가진다는 걸 데이터로 인정.

**G는 이번 push에 포함 X.** sweep 갤러리 결과 → 프리셋별 필요 값 실측 → 그 다음 반영.

### 2026-04-20~21 Phase 전체 검토 (유지)

→ `docs/flat_phase_review_2026-04-20.md`
→ `tools/audit/inspect_flat.py`
→ `docs/archive/HANDOFF-20260421-cont63-backup.md`

**핵심:** MVP 시연 차단 = Phase 1 비주얼 퀄리티. 크루티 1종도 버그·퇴보로 미완성. 3D 전략 A→B→C (B는 C 디딤돌).

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
| **레퍼런스** | reference_data.md | Armstrong/Szkutnicka/Abling + Kent 실측 §5 |
| | reference_donnanno_vol3.md | 재킷/코트/케이프 (Stage 3+) |
| | fashionpedia_ch5_textile_notes.md | Fabric DB (Stage 2) |
| **도구** | flat_designer_feedback_guide.md | 5월 인터뷰 질문 세트 |

### 산출물 (docs/deliverables/)

| 파일 | 상태 |
|---|---|
| flat_levelup_application.docx | 4/17 제출 완료 |
| flat_ir_v4.1/v4.2.pptx | 이전 |
| **flat_ir_v4.3.pptx** | 최신 (숫자 수정) |
| flat_yc_s26_application_draft.md | 5/4 전 숫자 반영 필요 |

### 파일 구조

- `docs/` = 확정 17종
- `docs/archive/` = 구버전 + README + `HANDOFF-20260421-cont63-backup.md`
- `docs/deliverables/` = 산출물
- `tools/audit/inspect_flat.py` = DOM 실측 스크립트

### 보류

- 칼라/소맷단/스커트/팬츠 — Phase 3+
- eton/bertha/puritan/wing — Stage 3+
- TOPS 카테고리

### POM 질문 답변 (cont.65 → 기획탭 → 코드탭)

**(가) resolved:** SpecModule.GRADE에 17개 POM (A-Q) 이미 구현됨 확인. 내 원 TODO "11→17 확장"은 내 오해.

**(나) 신규 task:** POM 공식을 SFD 실측 베이스로 재조정. 현재 `bodyLen=45` 기본값 vs SFD M 사이즈 실측 71cm, 11cm 갭. `reference_data.md §6` 기반 16 preset 기본값 일괄 조정. Stage 2 factory validation 전 완료 권장.

**(다) 17개 POM 상태 유지.** 추가 rows는 지금 불필요.

---

## 🔵 코드 → 기획

### ✅ cont.66 지시 전체 실행 완료 (2026-04-21 저녁, commit d98f5b2 push)

**실행한 cont.64 지시 5건:**

1. ✅ **버그 1 (underarm dashed)** — production에 이미 없는 상태로 push됨 (cont.62 수정이 이번 push에 포함)
2. ✅ **버그 2 (?demo URL)** — cont.65 `PresetModule.apply(0)` 추가가 이번 push에 포함. 로컬 검증: `?demo` 접속 직후 Crew Tee short rib 확인.
3. ✅ **이슈 A 옵션 B** — 구현 방식 수정 후 성공:
   - 1차 시도 (armpit 안쪽으로 extra L points 연장) — 실패. Body 안쪽 여분은 같은 색 덮기라 gap 원인인 body/sleeve 바깥쪽 lens 영역을 덮지 못함.
   - 2차 시도 (body armhole reverse curve 추가) — 성공. `flat-v6.html` L2997-3006: sleeve fill path 뒤에 `C${armX+(-dir)*ahH*0.01},${uaY-ahH*0.12} ${oSx+(-dir)*ahH*0.12},${oSy+ahH*0.28} ${oSx},${oSy}` 추가. sleeve fill이 body armhole과 정확히 같은 curve로 닫힘 → gap 원천 제거.
   - Stroke는 별도 path로 분리 (fill="none" stroke) — outline은 원래 모양 유지.
   - Set-in 전용. Raglan/Kimono는 armhole 없음 → 조건 스킵.
4. ✅ **이슈 B 옵션 F 보류 / 옵션 G 대기** — `cuffTiltK=0.45`, `innerShorten=armholeH*0.10` 현상 유지. 이번 push 미포함.
5. 📋 **cont.63 90° 블렌딩** — 롤백 재검토 대상 유지. sweep 갤러리 결과 후 결정 (기획탭 다음 세션).

**검증:**
- 시각: 카드 0 navy 확대 (카드피드 IR 경로) + 엔진 뷰 crewTee long sleeve navy 확대 → 어깨 gap 완전 제거 확인
- 전수: 16 preset × 3 color = 48 조합 NaN/undefined/exception **0**
- Raglan 대조군: Card 4 green 어깨 gap 원래 없음, 변화 없음

**Push 후 필수 (기획탭 액션):**
- `python3 tools/audit/inspect_flat.py crew long` 재검증 (원칙 6)
- 아웃커머·크루티 DOM + 확대 비교 (원칙 10)
- regression 확인 후 다음 단계 (옵션 G, cont.63 롤백 판정, POM (나) 공식 재조정 등) 진입

**이번 push 내용 (commit d98f5b2, cont.58~66 누적):**
- cont.58 리브 해칭/버튼-넥 겹침 / cont.59 커프 독립 좌표계 / cont.60 polo 전용 / cont.61 커프 완화+polo v2 / cont.62 underarm dashed 제거 / cont.63 소매 끝 블렌딩 (롤백 재검토) / cont.65 `?demo` 초기화 / cont.66 이슈 A 옵션 B

**한계 / 다음 남은 일:**
- cont.63 블렌딩의 프리셋별 영향 여전히 전역 상수 기반 → 옵션 G 대기
- POM (나) 공식 재조정 Stage 2 전 반영 (구현 대기)

**추가 작업 (push 후 중립):**
- **A. svgB back view 이슈 A 적용 확인** — SleeveComp.draw가 isBack 양쪽 호출 + sweep svgB error 0 → 적용됨 확정
- **B. 카드피드 card 1/2/3 (set-in) gap 해소 검증** — 3장 side-by-side 확대 → 모두 자연스러움 (Card 0 navy 이미 확인, Card 4 raglan은 원래 무영향)
### 🟠 cont.66 말미 — 전체 리뷰 + Phase 재조정 제안 (기획탭 핑퐁 대기)

**이람 2026-04-21 저녁 지시:**
> "지원사업은 내가 기획탭이랑 알아서 할테니 일단은 flat 의 완벽을 기하자. 기획탭 전략 되는대로 올릴게"
> "phase 재조정에 대한 의견은 좋고, 기획탭이랑 핑퐁하면서 신중을 기하자."

→ **코드탭 모드 전환**: flat 엔진 자체 완성도 집중. 지원사업 task 제외. Phase 재조정은 기획탭 OK 후 plan.md 반영.

#### 1) 프로젝트 전체 스냅샷 (오늘 기준)

| 지표 | 값 |
|---|---|
| flat-v6.html | 6,968줄 (단일 HTML) |
| 확정 docs | 19개 |
| 최근 push | cont.66 두 번 (d98f5b2, 4b5dd2d) |
| S.STAGE 마감 | 5/3 (12일 남음) |
| YC S26 마감 | 5/4 (13일 남음) |
| Factory validation | 5월 (~3-6주) |

**비주얼 퀄리티 변화 (이람 2026-04-17 검수 → cont.66 이후):**
- 크루티 밝은 색 ✅ → ✅ (SFD 수치 추가)
- 크루티 **컬러링 어깨 gap** ❌ → ✅ (cont.66 옵션 B)
- 소맷단 stitch 위치 ❌ → ✅ (cont.62)
- ?demo URL Shirt state ❌ → ✅ (cont.65)
- POM 공식 실무 Size M 미준수 → ✅ (cont.66 SFD)
- 소맷단 cuff 해부학 ❌ → ❌ (옵션 G 대기)
- 셔츠/기타 칼라 ❌ → Phase 3+ (Six Atomic 6종 실측 준비됨 ↓)

#### 2) Phase 재조정 제안 (기획탭 검토 요청)

현재 `plan.md` Phase 2는 4줄:
```
- polo 칼라 전용 렌더러
- 1분 데모 영상
- IR 덱 커버 (이람 비주얼)
- YC 지원서 최종
```

cont.66 이후 현실에 맞게 3-tier 구조 제안:

```
Phase 2 — 투자자 Red Loop 진입 (NOW → 5/3-4)

├─ [CODE] 코드탭 완료분
│   ✅ polo 전용 renderer (cont.60)
│   ✅ 크루티 컬러링 (어깨 gap + ?demo + SFD POM)
│   ✅ underarm dashed 제거 (production 반영)
│
├─ [HUMAN] 이람 직접 작업
│   ❌ IR 덱 커버 (트레이싱 프리즈 비주얼 제작)
│   ❌ 1분 데모 영상 (QuickTime 캡처)
│   ❌ YC 지원서 숫자 최종
│
└─ [PLAN+CODE] 기획탭↔코드탭 협업 (대기)
    📋 sweep 갤러리 (sweep_matrix.py 기획탭 → gallery.html 코드탭 준비됨)
    📋 옵션 G 설계 (preset별 sleeve.tiltK) → 구현
    📋 cont.63 블렌딩 롤백 판정
```

**장점**: 책임 주체가 명확해서 서로 블록 안 됨. 이람 작업 진행 중에도 코드탭 중립 진전 가능.

**단점**: 기존 plan.md는 task 중심. 3-tier 주체 중심은 철학 다름. 기획탭이 용어 체계 맞춰야 할지 판단 필요.

→ **기획탭 OK 주면 plan.md 반영. 수정 말라 하면 HANDOFF에만 기록하고 plan.md 기존 유지.**

#### 3) Six Atomic 96장 스크린샷 확인 보고

**이람 2026-04-21:** "Six Atomic 스크린샷은 로컬 파일에 폴더명으로 있어"

**sixatomic/ 폴더 내용 (2026-04-21 확인):**
- 기존 자료 3종 (cont.62에서 사용): Tech Pack PDF (1.7MB, 4p), DXF (1MB), DXF zip
- **스크린샷 96장** (2026-04-13 10:24-10:35, 약 11분 촬영)

**샘플 1장 내용 (10:24:05):**
- Six Atomic 앱 "Generate pattern" 화면
- "Select Design Options" — Shoulder Seam (regular/forward), Neckline Style (crew/vee/scoop), Product Length, Slit Depth, Pocket, Sleeve Length/Fabric/Hem, Body Fit, Hem Style, Front/Back Hem 등 **전방위 디자인 토글 갤러리**

**즉 96장 = 칼라 6종 대체가 아니라 Six Atomic 앱의 전체 design option UI 스크린샷**. cont.62 Kent 실측처럼:
- 칼라 7종 (Kent/Spread/Cutaway/Button Down/Band/Semi Spread/Semi Cutaway)
- Shoulder seam 2종
- Neckline 3종
- Sleeve 종류 + placket + cuff
- Pocket 9-13cm 등
- Body fit / Neck fit / Back hem 등

모두 실측/참조 가능. **FLAT 도식화 레퍼런스 보물창고**.

#### 4) 기획탭 판단 요청 (핑퐁 포인트)

Six Atomic 96장 활용 방향 3가지 옵션:

- **(가)** 원래 계획대로 **칼라 6종만 실측** → `reference_data.md §5` 확장 → Phase 3 셔츠 칼라 재설계 기반. 작업량 ~1-2시간.
- **(나)** **전방위 실측** — 칼라 + shoulder + neckline + sleeve + pocket + hem 등. Phase 3 패턴사 신뢰도 실측 기반. 작업량 ~1일.
- **(다)** 기획탭이 **필요한 토글만 pick** 후 지정. 코드탭은 지정된 것만 실측.

**내 권장**: (다). 기획탭이 sweep 갤러리/옵션 G 먼저 설계 중이므로, 칼라 재설계 시점·범위를 기획탭이 정하는 게 자연스러움. 나는 **대기 상태에서 "언제 뭘 실측하라" 지시만 기다림.**

#### 5) 기획탭 전략 올라오기까지 코드탭 중립 작업 후보

지원사업 제외 + flat 완성도 집중 원칙에서 할 수 있는 것:

- **a.** 다른 shape 분기 (puff/bell/bishop/lantern/peasant/legmutton/pagoda/dolman) 이슈 A 옵션 B 적용 — 현재 straight/raglan만 적용됨. 같은 body armhole curve를 모든 shape에 확장. 로 리스크 (성공 패턴 복제). 원칙 9 범위 밖 (magic number 아님, 구조 확장).
- **b.** PDF export 5-page tech pack + 작업지시서 1p에서 SFD POM 수치 재검토 (cont.66 POM 변경이 PDF에도 일관되게 반영됐는지 시각 확인)
- **c.** 카드 피드 raglan card 4 확대 퀄리티 체크 (IR 덱 커버에 쓸 가능성)
- **d.** 코드 주석 정리 (cont.57~66 누적)
- **e.** `inspect_flat.py` 로컬 대응 확장 (localhost 옵션 추가, 기획탭 도구 호환)

**a가 가장 value 높음** — 이슈 A를 전 shape에 확장. 근데 원칙 6 "자의적 개선 금지" 걸릴 수 있음. 기획탭 OK 확인 전 보류.

→ **결정**: 기획탭 전략 올 때까지 **a~e 전부 대기**. 새 지시 없으면 push 추가 없음.

---

- **D. POM (나) SFD 실측 공식 재조정 ✅ (원칙 11 자율 판단)** — `reference_data.md §6` SFD Size M 베이스 공식 3곳 통일:
  - `CM_MAP` L1968-1976 (슬라이더 cm 표시)
  - `SpecModule.updateTop` L4965-4982 (스펙시트 Graded Spec)
  - POM diagram L5356-5373 (엔진 내 visualization)
  - PDF export L5737-5762 (5-page tech pack Page 3 spec)
  - **검증**: crewTee default (S.bodyLen=45, chest=50, sleeveLength=32 etc.) → Size M 컬럼 SFD 정확 매칭:
    Body Len 71, Chest half 53, Shoulder 47, Sleeve Len 22, Armhole 24, Across F 41, Across B 43, Neck W 21, Front Drop 10, Back Drop 2-3, Slv Open 18
  - 16 preset sweep NaN/undefined 0
  - **렌더 SVG 무영향** (BodyComp.geometry() 별개 좌표계)
  - Stage 2 factory validation 전 완료 권장 task 조기 완료

- **C. 시각 sweep 갤러리 HTML 초안 작성 ✅** — `tools/audit/gallery.html` (원칙 10 Step 2 대비)
  - 48 tile (16 preset × 3 color)
  - side-by-side slot (prod PNG vs local PNG placeholder)
  - 3 flag 버튼 (✓ OK / ✗ 퇴보 / ? 모르겠음) + 메모 input → localStorage 저장
  - Filter: view (front/back/both), color, sleeveType (setin/raglan), flag
  - Export: `regression_list.md` 다운로드 (플래그 → 마크다운 변환)
  - PNG 경로 규약: `tools/audit/sweep/prod/{preset}_{color}_{view}.png`, `.../local/...`
  - 기획탭 다음 세션 `sweep_matrix.py` 작성 시 이 경로에 PNG 저장하면 gallery.html이 자동으로 매칭

### 🚨 cont.65 성과 + 한계 (2026-04-21)

**성과:**
1. 버그 1 진단 — 로컬 수정 이미 있음, 단순 push 문제
2. 버그 2 수정 — `PresetModule.apply(0)` 추가 (L6938-6945)
3. 48조합 sweep (`docs/audit_cont65_sweep.md`) — DOM stats 0건, color invariance ✅
4. 이슈 A·B 진단 + 옵션 제시 + **push 보류 (원칙 6 준수)**
5. 자의적 개선 자백 — cont.63 블렌딩이 이슈 노출 원인일 수 있음

**한계:**
- Sweep이 DOM stats만 — 시각 비교 없음 → 이람 "퇴보" 발견 못 잡음
- cuffTiltK / innerShorten 전역 상수 고수 (옵션 G 미제안)
- Back view (svgB) 개별 검수 없음

### cont.63 90° 블렌딩 — 롤백 재검토 (2026-04-21 번복)

**이전 판정 (기획탭 오전):** 롤백 불필요. 각짐 유지 실측 확인.
**번복 사유 (기획탭 저녁):** 이람 재보고 — Outerwear OK, Crew Tee 퇴보. cTilt 공식이 프리셋별 다른 결과.
**신규 방향:** sweep 갤러리로 어느 프리셋에서 퇴보 발생하는지 확정 → 결정.

### cont.62 "underarm dashed 제거 완료" 철회 (유지)

cont.65 재검증으로 원인 판명: production 단순 push 안 됨. 다음 push에 포함.

### Six Atomic Kent 칼라 실측 (cont.62, 유지)

Aspect 1.44, spread 60.8°, Stand:Fall 1:1. `reference_data.md §5`. 6종 미실측은 이람 액션 대기.

### 코드 현황

- 엔진 v0.26s-5 (cont.63 적용) + polo v2
- Phase 1A 11/11 + 1B 14/14, Phase 2 polo 마무리
- cont.62 dashed 제거: 로컬만, push 필요
- cont.63 블렌딩: **롤백 재검토 대상** (이전 "불필요" 번복)
- cont.65: 이슈 A·B 진단 완료, push 보류

### 📸 감사 방법

- ❌ 축소 + NaN만
- ✅ SVG clone 1400px 확대
- ✅ Glass Factory 1:1 비교
- ✅ 기획탭 DOM 실측 (`tools/audit/inspect_flat.py`)
- ✅ **[신규] 시각 sweep + side-by-side 갤러리** (원칙 10, 다음 기획탭 세션 구축)

---

## 🟡 양쪽 공유 TODO

| 항목 | 기획 | 코드 | 상태 |
|---|---|---|---|
| 🔥 push (버그1+2+이슈A-옵션B) | ✅ 지시 확정 | **✅ cont.66 완료 (d98f5b2)** | 완료 |
| 🔥 Push 후 DOM 재검증 | **기획탭 대기** | — | 다음 기획탭 세션 |
| 시각 sweep 갤러리 구축 | 기획탭 다음 세션 | — | 1순위 |
| cont.63 블렌딩 롤백 여부 | sweep 결과 후 | — | 대기 |
| 이슈 B 옵션 G 설계 | 기획탭 | 구현 대기 | sweep 후 |
| POM (나) 공식 재조정 | reference_data §6 | **✅ cont.66 완료 (push 대기)** | Stage 2 전 → 조기 완료 |
| 콘텐츠 자동화 cron 검수 | 📝 이람 | — | 대기 |
| IR v4.3 비주얼 검수 | 📝 이람 | — | 대기 |
| YC 지원서 숫자 반영 | 📝 이람 | — | 5/4 전 |
| 디자이너 인터뷰 3명 | 📝 이람 | — | 5월 전 |
| Six Atomic 6종 스크린샷 | 📝 이람 | 실측 대기 | 지금 가능 |
| 1분 데모 영상 | 스크립트 ✅ | 캡처? | 5/3-4 전 |
| factory validation | 성수동 | 검증 output | 5월 |

---

## 🟢 기획탭 다음 세션 할 일 (cont.64 말미에 선언)

**목적:** 이람 눈 부담 90% 감축. 자동이 찾고, 이람은 플래그만.

**Step 1: sweep 스크립트 확장**
- `tools/audit/inspect_flat.py` → 전체 매트릭스 (16 preset × 4 sleeveLen × 3 cuff × 3 color ≈ 수백 조합)
- 결과 PNG를 `/home/claude/sweep/{preset}_{sleeve}_{cuff}_{color}.png` 구조화 저장

**Step 2: Side-by-side 갤러리 HTML 생성**
- 왼쪽 production URL, 오른쪽 로컬 (or 이전 커밋) 렌더
- 이람이 눈으로 훑고 "OK / 퇴보 / 모르겠음" 3버튼 플래그

**Step 3: Invariant 테스트 초기 버전**
- `tools/audit/invariants.py` 신설
- 규칙 예: "모든 sleeveLen에서 cuff edge가 소매축에 수직 (±5°)"
- "body fill과 sleeve fill 사이 gap 0px"
- 깨진 조합 자동 리스트업

**Step 4: 플래그 리스트 → HANDOFF 자동 업데이트**
- `regression_list.md` 신설
- 다음 코드탭 세션이 이 리스트만 보면 고칠 곳 명확

---

## 📂 파일 구조

```
/Users/yiram/Claude/flat/
├── HANDOFF.md
├── progress.md / plan.md
├── docs/
│   ├── [확정 md 17종]
│   ├── flat_phase_review_2026-04-20.md
│   ├── audit_cont65_sweep.md  ← cont.65 DOM sweep
│   ├── archive/
│   │   ├── README.md
│   │   └── HANDOFF-20260421-cont63-backup.md
│   └── deliverables/
├── tools/
│   └── audit/
│       ├── inspect_flat.py  ← 단일 조합 DOM 실측
│       ├── gallery.html     ← [cont.66] side-by-side flag viewer (48 tile, localStorage, regression_list.md export)
│       ├── sweep_matrix.py  ← [신규 예정] 전체 매트릭스 PNG 생성
│       └── invariants.py    ← [신규 예정] 규칙 테스트
├── data/ / ref/ / trends/
└── flat-v6.html
```

## 📏 규칙

1. 기획탭 → `docs/` + HANDOFF "기획→코드" 섹션만
2. 코드탭 → `progress.md` + HANDOFF "코드→기획" 섹션만
3. 세션 시작 → "HANDOFF.md 읽어줘"
4. 결정 필요 → HANDOFF에 질문
5. 수정 시 "마지막 수정" 갱신
6. **비주얼 "완료" → 기획탭 DOM 실측 재검증 (원칙 6)**
7. **전체 덮어쓰기 금지. 섹션 단위. 수정 전 백업 (원칙 7)**
8. **Stage=전략, Phase=구현 (원칙 8)**
9. **[신규] 반복 피드백 시 magic number 조정 중단. 전역성 의심 (원칙 9)**
10. **[신규] 시각 검수는 전수 자동 기본. 매 push마다 sweep + 갤러리 (원칙 10)**
11. **[신규] 기획탭은 방향만 받고 실행은 자율. A/B/C 선택지 떠넘김 금지 (원칙 11)**
