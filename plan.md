# Project Plan — FLAT 의류 도식화 엔진

## Goal
파라메트릭 SVG 기반 의류 도식화 자동 설계 앱. 단일 HTML 파일, 설치 불필요.
"선이 숫자인 유일한 garment design tool" — 스케치=spec=pattern data.

> 📌 구 version history (v0.4~v0.25)는 `docs/archive/plan_history_v0.19-0.25.md` 로 분리됨 (2026-04-21 cont.64).
> 이 파일은 **현재 진행 중 Phase와 Next Up** 만 유지.

## Current Status (v0.25 + cont.68 Part 1)

### 숫자 (cont.72 Part 7 audit 정정 — 이전 "검증 완료" 표시 정확성 점검)

> ⚠️ **cont.72 audit 인정** — 일부 카운트는 추정/부정확 / 일부 작동 검증 미흡 (`docs/cont72_full_inventory.md` § 8 Quality-Insufficient 영역 참조).

- **34 presets** (16 top + 8 skirt + 10 pants), 7 cat 데이터 분류 (5 cat UI는 Phase 6 DEFER)
  - ※ 이전 "49 presets (31 top)" 표기 = 부정확 (추정치). 실제 PresetModule.DB 16. spec v0.2 32 preset 확장 후속 (Phase 4)
- **27 compat rules (6 system)** — cont.72 Part 13 정정 (이전 "108 + 21 + 3 = 132 (12 system)" 표기 부정확): NECKTYPE_COMPAT 3 / SHOULDER_NECKTYPE_COMPAT 3 / DETAIL_NECKTYPE_COMPAT 1 / SHOULDER_DETAIL_COMPAT 3 / COLLAR_COMPAT 8 / NECK_BC_BLOCKED 9 = 27 rule, 6 system. 작동 케이스 자동 검증 진행. ⚠️ 도메인 비교 (sixatomic carve-out) 후속 Cowork 분담
- **41 fabric DB** (EN/KO, GSM, season, stretch, garment fit) — ✅ cont.72 Part 13 검증: 41 entry 모두 name.en/ko/gsm/season/stretch/id 정합 (missing 0)
- **14 design elements**, **7 style overlays**, **18 collar params**
- **17 POM** (A-Q) + XS-XL grading + tolerance + 시접(S/A) per area — sweatshirt §6.2 적용 / crewTee/hoodie §6.3-6.4 코드 미적용 (Phase 4) ※ sixatomic 28 부위 시접 (S14 spec) 대비 11 부위 미흡
- **i18n**: EN/KO ⚠️ 봉제 현장용어 자동 병기 매핑 정합성 미검증 (cont.72 audit)
- **3축 분리**: shoulderType 8 / strapType 6 / neckShape 8 — 데이터 분리 ⚠️ UI 적용 검증 미흡
- **PDF**: 5-page tech pack + 1-page 한국 작업지시서 — 출력 작동 ⚠️ 실무 패턴사 사용 검증 X (Phase 3B 의존)
- **Factory Viewer**: read-only URL + share link ⚠️ 작동 검증 미흡 (이람 직접 사용 X)
- **CascadeVis**: SVG morph animation + 11-step demo — 동작 ⚠️ 시각 매력도 미흡 (cont.65 sweep audit 영역)
- **Body size input** → auto slider mapping (bust/hip → chest/hipFlare). hipFlare 정상 작동 (cont.72 Part 11 정정). ⚠️ **waist input 변수 선언만 / 매핑 미구현** (도메인 결정 필요 — silhouette tapered? 별도 slider?)
- **★ cont.67:** reference_data.md §6.2 sweatshirt + §6.3 crewTee + §6.4 hoodie SFD 16/14/18 POM
- **★ cont.68 Part 1:** BodyComp.geometry() sweatshirt 분기 (body/rib/armhole SFD + shoulder FLAT convention 절충)
- **★ cont.69-72:** S1/S2/S5/S8 (UI 메타-패턴) + B6.2 lift-and-shift (34 preset / 9 cat JSON) + B6.1 lift-and-shift (6 sample rule) + 보강 8건 + 누락 방지 시스템 5단

### 배포
- **Demo URL**: https://yunyiram.github.io/flat/
- **Repo**: https://github.com/yunyiram/flat (public)

### 도메인 로직 분리 완료 ✅
```
data/
├── rules.json     14KB
├── presets.json    36KB
├── params.json     20KB
└── fabrics.json    19KB
                    89KB  "알맹이" — CTO rewrite 시에도 보존
```

### ⚠️ GPL 경고
- ❌ Valentina/Seamly2D (GPL-3.0) — 코드 한 줄도 복사 금지
- ✅ FreeSewing (MIT) — 참고 가능, 출처 표기
- 원칙: 영감은 자유, 코드 복사는 금지

## 최근 완료 (cont.58 ~ cont.68, 요약)

### DONE — cont.61~65: 소매 좌표 체계 재설계 + cuff 독립 + 시각 감사
v0.26s (소매), v0.26s-2 (cuff), v0.26s-3 (polo v2), v0.26s-5 (cont.63 90° 블렌딩), cont.65 audit.

### DONE — cont.66: 버그 fix + POM SFD 재조정 ✅
commit d98f5b2 (버그1/2/이슈A 옵션B) + commit 4b5dd2d (POM SFD 재조정 4곳 통일, 스펙/PDF만).

### DONE — cont.67: sweep 파이프라인 + 이람 검수 + 옵션 H 방향 ✅
- sweep_matrix.py + 96장 baseline → 48 tile 전부 실무 미달 판정
- Sweatshirt 16 POM (이람 OK) + crewTee 14 POM + hoodie 18 POM (암묵 OK, reference_data §6.2/6.3/6.4 병합)
- 원칙 9/10/11/12/13 등록
- preset_expansion_workflow.md + preset_research.html 저장
- 코드탭 cont.68 지시문 저장

### DONE — cont.68 Part 1 (commit b7b3b46, 2026-04-22): BodyComp sweatshirt 분기 ✅
- SFD_POM.sweatshirt.M 상수, SFD_VSCALE/HSCALE 역산, S.presetName 필드
- BodyComp.geometry() sweatshirt 분기 — body/rib/armhole SFD + shoulder/neck/slope FLAT convention (절충, 원칙 11 자율)
- BodyComp.armholeY() sweatshirt 분기
- 검증: crewTee 회귀 0, 16×3 sweep NaN 0

**미완:** 팔 품 + 커프 조임 — SleeveComp primitive.

### DONE — cont.72 Part 6 (commit 대기, 2026-05-06): micro 보강 3건 ✅
- skirt/pants 메타-그룹 6 헤더 (S8 후속 #2 해소)
- skirt/pants slider ↺ 6개 검증 (S5 후속 #2 해소)
- flat_self_check_template.md v1.1 — F 그룹 5 항목 (누락 방지 #4)
- S2/S5/S8 자율 후속 모두 해소 (S2는 Phase 의존만)
- 검증: 메타 9개 / sweep 0/0 / 회귀 0 / console 0

### DONE — cont.72 Part 5 (commit 대기, 2026-05-06): 재검 + 자율 보강 5건 ✅
- 재검: B6.2 정합 0 mismatch / 96 sweep 0/0 / 회귀 0
- 5 자율 보강 (S2/S5/S8 후속 TODO 해소):
  1. CARD_DATA presetIdx fuzzy match (findClosestPresetIdx)
  2. collar 22 (data-neck=B) dft 마커 (NECKFINISH_TO_COLLAR 매핑)
  3. opening 12 (data-neck=C) dft 마커 (CLOSURE_TO_OPENING 매핑)
  4. slider thumb default indicator (.slider-default-mark)
  5. 메타-그룹 collapse 상태 localStorage save/restore
- 검증: 96 sweep 0/0, 회귀 0, console 0, 시각 정상
- Sixatomic 흡수 진척: S1/S2/S5/S8 + 보강 5건 완료. 후속 TODO 8건 → 3건 (Phase/spec 의존만)

### DONE — cont.72 Part 4 (commit 대기, 2026-04-28): "전부" batch — K (inventory) + F (B6.1 lift-and-shift) ✅
- K: `docs/cont72_full_inventory.md` 신설 — 코드/데이터/spec/메모리/사고/TODO single source of truth (누락 방지 시스템 #2)
- F: B6.1 rules.json lift-and-shift — 6 sample rule (hard 3 + soft 3) + index + cross_category. spec sheet § 4 prototype 그대로
- G/J/A 자율 보류: G fabrics 이미 외부 / J 카테고리 분류 6 = Phase 4 옵션 H 동기 / A Loader = Phase 5 SaaS 동기 (단일 HTML 원칙)
- 사고 (m) 적용: 떠넘기기 X — 자율 결정 + 보류 사유 명시

### DONE — cont.72 Part 3 (commit 대기, 2026-04-28): B6.2 lift-and-shift ✅
- data/presets/ 신설 (9 카테고리 × 34 preset). PresetModule.DB / SKIRT_DB / PANTS_DB → JSON 분리
- 자율 결정 (사고 m 떠넘기기 X): 현 schema/enum/cat 그대로, loader 미도입 (회귀 0)
- 후속: Loader 도입 / 5 카테고리 reorganize / sixatomic enum 표준화 / 32 preset 확장 / B6.1 + B6.3 + B6.4 implement
- 검증: 9 JSON valid, 34 preset DB 정합 mismatchCount 0, 회귀 0

### DONE — cont.72 Part 2 (commit 대기, 2026-04-28): S6 skip + S8 카테고리 메타-그룹 ✅
- S6 자율 skip — FLAT 슬라이더+토글 양방향 동기화 (P3=A + S5)가 sixatomic Custom보다 우월. over-engineer 회피 (원칙 14)
- S8: Design / Fit / Details 3 메타-그룹 헤더 추가
  - Design = Garment + Style Overlay + Presets
  - Fit = Neckline + Shoulder + Sleeve + Body + Hem + Fit
  - Details = Detail + Design Elements (default collapsed)
- 핵심 자율: DOM 순서 기반 sweep (compareDocumentPosition) — Presets nested 구조에서도 정확
- 검증: 96 case sweep NaN/Exc 0, 회귀 0, S2 dft + S5 ↺ 동시 작동 OK, console errors 0

### DONE — cont.72 (commit ececbbd, 2026-04-28): tops_tees 미분류 추출 보고 ✅
- cont.72 1순위 차단 해제 (cont.71에서 요청)
- 핵심 정정: spec v0.2 가정 "약 10개 미분류" → 실제 cat:'tshirts'는 crewTee 1개만
- flat-v6.html PresetModule.DB 16 preset 전체 cat 분류 표 + 차이 분석을 HANDOFF "🔵 코드→기획"에 작성

### DONE — cont.69 Part 3 (commit c7a91a0, 2026-04-28): S5 Revert per-input ✅
- `flat-v6.html` 단일 파일 변경 (CSS .sl-revert + 4 신규 함수: getCurrentDefaults / revertSliderToDefault / initSliderRevertButtons / updateSliderRevertOpacity + slider input/PresetModule apply/CardFeed pickVariant 모두 hook)
- 18 slider 모두 1:1 ↺ 자동 추가, default 일치 시 흐림 / changed 시 강조
- 자율 결정: PresetModule.DB(S2 데이터) 재사용, slider thumb indicator는 후속
- 검증: 96 case sweep NaN/Exc 0, 회귀 0, ↺ 동작 정상, EN/KO tooltip, console errors 0

### DONE — cont.69 Part 2 (commit 대기, 2026-04-28): S2 Default 마커 + Reset 버튼 ✅
- `flat-v6.html` 단일 파일 변경 (CSS dft dot + Reset 버튼 + state currentPresetIdx + updateRecommendedMarkers/resetToDefault + i18n + CardFeed 진입 hook)
- 자율 결정: `garment_defaults.json` 신설 X — PresetModule.DB(16 preset) 기존 데이터 활용 + 라벨 톤 "Default/기본값" (실무 검증 전 과대평가 회피)
- 검증: 96 case sweep NaN/Exc 0, 회귀 0, 16 preset dft 정확성 100%
- 이람 검수: A 옵션 OK + "후속 보강 메모 잊지 말고" 강조
- **후속 TODO (HANDOFF 표 등록):** collar 22종 dft (data-neck B), opening 12종 dft (data-neck C), CARD_DATA presetIdx 매핑, 라벨 "Recommended" 격상 (Phase 3B 후), 슬라이더 indicator (S5)

### DONE — cont.69 (commit 471caa4, 2026-04-28): S1 Sleeve length ratio model ✅
- `data/rules/sleeve_length_ratios.json` 신설 — women+men matrix, labelMap, garmentDefault, futureWork
- `flat-v6.html`: i18n EN/KO sleeve labels 괄호 병기 (`Cap (Very Short)`, `Long (Wrist)` 등) + ratio const 블록 (SIDE_ARM_LENGTH_DEFAULT=53, defaultGender='men', sleeveLenRatioToCm())
- 결정 묶음 (이람 OK): P1=A+괄호 / P2=A(53cm) / P3=A(양방향 동기화 보존) / P4=A'(women+men, default Men's) / P5=B(슬라이더값 유지) / P6=A(자율)
- 회귀 정합성: Men's Regular 0.385×53=20.4cm ≈ 현 short 20.7cm (−0.3cm 깔끔)
- 검증: 96 case sweep NaN/undef/Exc 0, crewTee/sweatshirt baseline 동일, console errors 0
- 이람 검수: 슬라이더+토글 양방향 ✅ / cuff 어색함은 Phase 4 합의 그대로 (S1 회귀 0)
- **TODO 보존:** Women's matrix 활성화 (gender 토글 spec 별도, 잊지 말기)

---

## Red Loop 경로 (2026-04-22 재정렬, cont.67 말미 Part 3 반영)

> **★ 전략 전환 (cont.67 말미 Part 3, 원칙 14):**
> 3D 연동 이전 구간에서는 **매력도(UX/UI/비주얼)가 실무 정확도 앞선다.** 현재 옵션 H는 3D 오면 재구성될 interim fix. 정확도는 **factory validation 통과 수준까지만.** 그 이상 에너지는 UX/UI로.
>
> **근거:** Tailornova 13년 + YC + parametric tech = $186K/년. 기술이 승리 보장 안 함. Raspberry AI $28.5M도 "시각화"에 쓰임 — 투자자 first impression은 매력도. FLAT의 강점 = 이람의 비주얼 디렉터 10년 경험 + 쉬운 UX. 3D 와서 기술 재구성될 때 그때 쥐잡듯이 정확도 잡음.

### ✅ Phase 1A — 데모 UI (완료)
- [x] 넥 3축, 컬러 10색, 카드 피드, GitHub Pages 배포

### ✅ Phase 1B — 프레젠테이션 + 퀄리티 (완료)
- [x] 트레이싱페이퍼, 컬러 3변형, 다크 스트로크, 대화 L1
- [x] 라인웨이트, 리브, 암홀, 플래킷 — cont.67 재평가로 과대평가 인정
- [x] 커프 각도 통일, 버튼/넥 겹침, 칼라 매핑

### Phase 2 — 투자자 Red Loop 진입 (NOW → 5/3-4)
> 목표: S.STAGE + YC 데모에서 "선=숫자"가 5초 안에 전달됨
> **완료 조건 (cont.67 말미 Part 3 축소):**
>   - (a) **sweatshirt 개선 가시화** (이람 전/후 비교에서 "확연 개선" OK) — **실무 수준 도달은 Phase 3B/4 이후**
>   - (b) IR 덱 + 1분 데모 + YC 지원서 완성
>   - (c) factory validation 섭외 확정
>   - (d) **★ 신규 UX/UI 매력도 1순위 항목 완료** (Phase 3A의 첫 항목 — 이람 결정)
>
> 근거: 원칙 14. sweatshirt "실무 수준"까지 파면 나머지 15 preset도 같은 깊이 요구 → 3D 연동 시 재구성 → sunk cost. Phase 2는 "방향성 증명 + 매력 최대"로 축소.

**[CODE] 코드탭 완료분**
- [x] cont.60 Polo 렌더러, cont.66 옵션 B, cont.66 ?demo URL, cont.66 underarm, cont.66 POM SFD
- [x] cont.67 tools/audit/gallery.html
- [x] cont.68 Part 1 — BodyComp sweatshirt 분기 (commit b7b3b46)
- [x] **cont.68 Part 2 축소판** — SleeveComp cuffHalfW 분기 (commit 71b7400). sleeveOpening SFD 10cm 적용.

**[HUMAN] 이람 직접 작업**
- [ ] IR 덱 커버 (트레이싱 프리즈 비주얼 제작)
- [ ] 1분 데모 영상 (QuickTime 캡처) — Phase 3A UX/UI 1순위 항목 완료 후
- [ ] YC 지원서 숫자 최종 (5/4 전)
- [x] 96 tile sweep 검수 (cont.67 48/48 미달 판정)
- [ ] **옵션 H sweatshirt Part 2 구현 후 before/after 비교** — 개선 가시화 OK?
- [ ] **UX/UI 매력도 1순위 항목 결정** (Phase 3A 진입 조건)

**[PLAN+CODE] 기획탭↔코드탭 협업**
- [x] sweep 파이프라인, sweatshirt/crewTee/hoodie SFD §6 병합
- [x] **코드탭 cont.68 Part 2 축소판**: SleeveComp sweatshirt `cuffHalfW` 분기 — sleeveOpening SFD 반영 (commit 71b7400). cuffWidth 10.54px 수치 검증, 16 preset NaN 0, crewTee 회귀 0.
- [ ] 기획탭 sweep 재실행 → post_option_h 비교
- [ ] 이람 "개선 가시화" 판정 → Phase 2 (a) 완료

### Phase 3A — UX/UI 매력도 집중 (5/3 전 가능한 한) ★ 신규

> 목표: 투자자가 FLAT 데모에서 "와" 를 이끌어내는 시각/인터랙션 폴리시.
> 원칙: 이람 비주얼 디렉터 강점 활용. 옵션 H 정확도 작업보다 우선.

**후보 (이람 1순위 결정):**
- [ ] (i) **카드 피드 비주얼 폴리시** — 첫 5초 훅, 타이포그래피, 여백, 전환 타이밍
- [ ] (ii) **트레이싱 프리즈 애니메이션** — 영감→생산 순간의 시그니처 모먼트 (IR 덱 커버와 연동)
- [ ] (iii) **cascade 시각화 부드러움** — 슬라이더 → 실시간 도식화 변형. "아하 모먼트" 극대화
- [ ] (iv) **대화 UX Phase 1 완성도** — FLAT이 먼저 말한다. 톤/타이밍/선택지
- [ ] (v) **컬러/마테리얼 바리에이션 전환** — 한 preset이 3~4 variation 되는 비주얼
- [ ] (vi) **데모 영상 60초 시나리오 + 시각적 훅 재설계** — YC/S.STAGE용

**이람 action:** 위 6개 중 **1개를 "가장 먼저 끌어올리고 싶은 것"** 선택 → 기획탭이 상세 방향 문서화 → 코드탭이 구현. 나머지는 순차.

### Phase 3B — factory validation + 실무 최소 요구 (5월)

> 목표: 패턴사가 FLAT output을 작업지시서로 쓸 수 있는 **최소 수준 확인**.
> 원칙 14: "실무 수준"은 validation 통과에 필요한 수준까지. 나머지는 3D 이후.

- [ ] 성수동 샘플실 2곳 + 동대문 패턴사 1곳 섭외 (이람)
- [ ] 현재 PDF tech pack + 작업지시서로 인터뷰 — "쓸 수 있나/부족한 건 뭔가"
- [ ] **가장 critical한 피드백 1~2개만 fix** — 전부 고치려 하지 말 것 (3D 이후로 DEFER 권장)
- [ ] 인터뷰 결과 → Phase 4 3D 로드맵에 반영

### Phase 4 — 3D 연동 + 옵션 H 나머지 preset (5월 이후)

> 이 시점이 "쥐잡듯이 정확도 잡는" 진짜 순간.
> 현재 primitive geometry 전면 재구성. SFD POM 테이블은 그대로 활용 (3D에서도 canonical).

- [ ] **3D 로드맵 Phase 1**: 2D body overlay (SVG 기반, 현재 FLAT 유지)
- [ ] **3D 로드맵 Phase 2**: Three.js + react-three/fiber lightweight 3D — Parafashion 참고
- [ ] **3D 로드맵 Phase 3**: 개인 치수 기반 3D avatar
- [ ] **3D 로드맵 Phase 4**: fit simulation (옷감 물성)
- [ ] **옵션 H 나머지 preset 구현** (3D 연동과 동기) — crewTee/hoodie/polo/shirt/blazer/bomber/trench/cardigan/dress
- [ ] **칼라 22종 재감사** (옵션 H + 3D 이후)

**참조:** github.com/afilahkle/3D-Clothing-Configurator, parafashion.vercel.app

### Phase 5 — AI + 트렌드 (3D 안정화 후)
- 트렌드 파라미터화 (delta vector + intensity)
- Claude API 자연어 입력 (대화 UX Phase 2)
- 바디 스캔 API 연동 → 파라미터 자동 주입

### Phase 6 — SaaS 전환
- 파일 분할 (ES Module + Vite)
- 인증/저장/결제 (Supabase + Stripe)
- 무료/Pro $19/Team $49/Factory $99

### Phase 7 — 선으로 디자인 (SaaS 이후)
- 봉제선 쪼개기, 선 추가, 베지어 핸들 직접 드래그

### DEFER → 3D 이후 또는 SaaS
- 옵션 H 나머지 preset (crewTee/hoodie/polo/shirt/...) 코드 구현 → Phase 4
- 7프리셋 × 칼라 조합 퀄리티 패스 → Phase 4
- 앞/뒤 비대칭, 패턴메이킹 정확도 → Phase 4
- 핸들 스냅핑, 성별 토글, Active Mode, HS 코드 → Phase 6
- 카테고리 5분할 UI 구조 변경 → Phase 6

### DROP
- ~~패턴→도식화 역방향~~ → Phase 5+ API 연동
- ~~패턴 메이킹~~ → Valentina/FreeSewing 연동
- ~~작도(construction drawing)~~ → 별도 도구

### 기획탭 자율 작업 (원칙 13 자동 진행, 코드탭 구현 없이)

> preset SFD 테이블은 3D에서도 canonical data. 제안서 + reference_data 병합은 계속.
> **코드탭 구현 지시 중단.** Phase 4에서 일괄 구현.

- [ ] polo cycle (Lacoste + Uniqlo DRY-EX + Ralph Lauren)
- [ ] shirt cycle (Six Atomic Kent §5 + SFD)
- [ ] blazer cycle (Donnanno Vol.3 §p.14~)
- [ ] bomber cycle (Alpha MA-1)
- [ ] trench cycle (Burberry)
- [ ] dress cycle (5 dress preset)
- [ ] cardigan cycle

## 마감
- **경기 레벨업**: 4/17 제출 완료 ✅
- **S.STAGE**: 5/3 (풀 데모 + 1분 영상)
- **YC S26**: 5/4 (풀 데모 + 지원서)
- **Factory validation**: 5월 (Phase 3B)
- **3D 연동 착수**: 5월 이후 (Phase 4)

## 칼라 22종 시각 감사 결과 (2026-04-17)

> ⚠️ **cont.67 재평가:** 48 tile 전부 실무 미달 판정 → "✅ 실무 수준/양호" 과대평가였음.
> **cont.67 말미 Part 3 재정리:** 칼라 재감사는 **Phase 4 (3D 이후)**. 지금은 보류.

| 등급 (2026-04-17, 재감사 Phase 4) | 칼라 | 비고 |
|---|---|---|
| ~~✅ 실무 수준~~ | notched, shawl, peaked, round_lapel | 라펠 그룹 |
| ~~✅ 양호~~ | shirt, band, funnel, hood, turtle, mock | 독자 렌더러 |
| ~~✅ 양호~~ | camp/convertible, sailor, cowl, bow, peter | 형태 있음 |
| ⚠️ 중복 매핑 | polo → shirt | cont.60 해결됨 |
| ⚠️ 형태 약함 | eton, bertha, puritan, wing | 크기/비례 구분 어려움 |
