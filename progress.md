# Progress Log

## 2026-05-13 (cont.72 Part 7-15) — 전체 audit + 자율 batch 종합 (누락 방지 #5 — progress.md 빠짐없이 기록)

> ⚠️ **누락 인정:** progress.md가 Part 8까지만 기록 / Part 7 + Part 9-15 미기록 발견 (cont.72 Part 16). 본 항목으로 종합 기록.

### Part 7 — 전체 프로젝트 audit (commit 1a90f65)
이람 push "넘어갈 수 없는 퀄리티인데 완료된 작업 찾아내". 원칙 4 적용.
- inventory § 8 "Quality-Insufficient 영역" 신설 — 12+ 영역
- plan.md "49 presets" → 실제 34 / "108 compat" → 작동 검증 미흡 등
- Sixatomic 흡수 정정: UI 메타-패턴 50% / 도메인 깊이 0%

### Part 9 — MCP 대안 실험 A/B (commit 별도, docs/archive/)
이람 spec docs/incoming/mcp_alternatives_experiment.md.
- 실험 A (DesktopCommander): ❌ 실격 (설치 SIGKILL, read 계열 미작동 / write_file·edit_block·get_file_info ✅)
- 실험 B (git sync): ✅ 잠정 합격 (B1 local 0.03s, timeout 0)
- 권장: B 즉시 채택 + A sudo 재시도 / RCA 사고 6번 추가
- 사고 자기 보고: "No response requested" 2회 재발 (사고 6번 패턴)

### Part 10 — S14 Phase 1 implement (commit 별도)
cont.73 spec docs/spec_S14_customise_seams.md.
- data/seams/ 8 파일 신설 (index + 7 group = 27 area)
- collar 4 / collar_stand 4 / cuff 4 / sleeve 5 / pocket 3 / side_seam 2 / singles 5
- tbd 10 (factory validation 5월 후 default), 27/28 모호 case A 가정
- B6.1/B6.2 lift-and-shift 패턴

### Part 11 — Body size mapping audit 정정 (commit 별도)
- hipFlare 실제 정상 작동 (코드 L2302-2306) — Part 8 T4 검증 부족 (case 다양화 X)
- 진짜 갭 = waist input 미사용 (변수 선언만)
- inventory § 8 D + plan.md 정정

### Part 12 — D-2 audit + B6.5 spec + CARD_DATA fuzzy fix (commit 별도)
- inventory § 8 D-2 신설 — 검증 부족 17 영역 (self-audit의 self-audit)
- B6.5 factoryTerm i18n 통합 spec 신설
- CARD_DATA fuzzy match audit: Card 3/4 잘못 매핑 발견
  → fix 3-layer: 가중치 +2 + targetPresetName 명시 + fallback

### Part 13 — 분업 자가검증 + Compat 정정 (commit 별도)
- HANDOFF "🔵 Part 13" — 검증 부족 17 영역 분담 (코드탭 8 / Cowork 5 / 기획탭+이람 12)
- 분업 평가: Cowork 탭 활용 미흡 (실제로는 진행 중 — 이람 확인)
- Compat 6 system 27 rule (plan.md "108+21+3=132 / 12 system" 4-5배 부풀림 정정)
- fabric DB 41 정합 검증 (missing 0)

### Part 14 — B6.5 Phase 1 + sweep_matrix.py (commit 별도)
- data/factory_terms_i18n_mapping.json — 60 용어 → 18 UI / 26 PDF / 6 확장 필요
- tools/audit/sweep_matrix.py 1차 minimal (cont.65 sweep_matrix.py 부재 정정)
  - 5 axes / 16 preset × 6 sleeveLength = 96 case JSON

### Part 15 — B6.5 Phase 2+3 (commit 23번째)
- LANG.ko_factory section (19 entries / 6 카테고리)
- UI "공장" 토글 버튼 + setLang + t() fallback
- 병기 형식 default C (표준어 + 현장어 괄호)

### cont.72 누적 commit (Part 16 시점)
23 commit: S1/S2/S5/S8 + B6.1/B6.2 lift-and-shift + S14 Phase 1 + B6.5 Phase 1-3 + 보강 8 + micro 3 + audit + 누락 방지 5단 + sweep_matrix.py

### 검증 부족 17 → 진척
- ✅ 해소: CARD_DATA fuzzy (Part 12) / Compat 카운트 (Part 13) / fabric DB (Part 13) / 봉제 현장용어 i18n (Part 14-15) / Body waist 정정 (Part 11)
- 🟣 Cowork 분담: 22 collar 시각 / 27-28 모호 / M1-M7 / 108 sixatomic 비교
- 🔴 기획탭+이람: CascadeVis / Hint / S8 검수 / Skirt-Pants 시각 / S15-S16 spec / 데모
- ⏸ preview 의존: Style Overlay / CM toggle / Extended / Pocket Y (preview MCP 회복 시)

### push
- Part 7-15 모두 commit 완료 (별도 commit 9건)
- 본 progress.md 종합 기록 = Part 16 commit 대기

### 다음
- HANDOFF "🟡 양쪽 공유 TODO" 표 Part 13-15 등록 (누락 방지 #5)
- inventory § 7 후속 TODO 갱신 (B6.5 해소)
- 외부 의존 (Cowork / 기획탭 spec / Phase 3B / 데모) 대기

---

## 2026-05-06 (cont.72 Part 8) — "가능한 건 다 하자" 자율 batch (T1+T2+T3+T4+B+T6)

### 지시문
이람 cont.72 = "자율 4건 이상으로 보여. 가능한 건 다 하자. 아니면 자율도를 높일 스크롤링/스크래핑/자료 찾는 프로그램 만들까?"

### 자율 가능 영역 30+ 발굴 후 batch 진행

#### T1. 빠른 win (commit f693bfc)
- plan.md "Current Status" 정정 (49 → 34, 11 항목 ⚠️)
- i18n EN sleeve.capped 누락 정정 (318/318 100%)
- docs/copy_guide.md 신설 (S4 spec source — sixatomic audit Section 6 6 톤 규칙)
- 한국어 1글자 깨짐 검증 (모든 파일 U+FFFD 0)

#### T2-T3. 작동/시각 sweep (commit 336f063)
- Style Overlay 7/7 작동
- CM toggle (cm ↔ inch) ✓
- Hint system / Pocket Y / Extended Range 9 / Compat system 6 / SpecModule.update ✓
- ⚠️ Body size input mapping 미흡 (88/68/92 입력 fitW 변경 0) → Part 11 정정
- ⚠️ plan.md "12 compat systems" 부정확 (실제 6) → Part 13 정정
- Skirt 8 / Pants 10 / 22 collar / Sleeve shape 10 자동 검증 모두 통과
- fabric DB 41 정확 / Design Elements 14 button

#### T4. 도메인 검증 + 봉제 현장용어 (commit 8677f83)
- Body size mapping 정밀 검증: chest slider 갱신 / hipFlare → Part 11 정정
- data/factory_terms.json 신설 (60 용어 / 8 카테고리)
- plan.md "i18n EN/KO + 봉제 현장용어 자동 병기 (factoryTerm{})" 명시 / 코드 미통합 인정
- 후속: B6.5 신설 → Part 12-15에서 spec + Phase 1-3 implement

#### T5. 카테고리 분류 6 데이터 추가 — 보류 그대로 (Phase 4 동기)

#### B. 자율 도구 spec 신설 (commit 3bdbef0)
- docs/flat_scraper_tools_spec.md — 5 도구 우선순위
- → Part 14에서 sweep_matrix.py 1차 implement

#### T6. 누락 방지 #3 신설 (commit 3bdbef0)
- docs/flat_cont_audit_template.md (cont 단위 audit 표 양식)
- 누락 방지 시스템 5/5 완료

### 검증
| 항목 | 결과 |
|---|---|
| 96 case sweep | NaN 0 / Exception 0 ✅ |
| crewTee/sweatshirt 회귀 | baseline 동일 ✅ |
| i18n 318/318 | ✅ |
| 한국어 깨짐 | 0 ✅ |

### push
- T1: f693bfc / T2-T3: 336f063 / T4: 8677f83 / B+T6: 3bdbef0

---

## 2026-05-06 (cont.72 Part 6) — micro 보강 3건 (skirt/pants 메타 + slider 검증 + self_check F 그룹)

### 지시문
이람 cont.72 = "자율 가능한 micro 보강" 진행.

### 보강 3건 ✅

**1. skirt/pants 메타-그룹 적용 (S8 후속 #2 해소)**
- skirt panel: skirt-design / skirt-fit / skirt-details 3 메타 헤더 추가
- pants panel: pants-design / pants-fit / pants-details 3 메타 헤더
- 합계 메타 9 (top 3 + skirt 3 + pants 3)

**2. skirt/pants slider ↺ 검증 (S5 후속 #2 해소)**
- skirt slider 3개 + pants slider 3개 모두 ↺ 자동 추가 ✅

**3. flat_self_check_template.md F 그룹 5 항목 추가 (누락 방지 #4 해소)**
- v1.0 → v1.1, F. 누락 검증 (F1 메모리 / F2 docs / F3 archive RCA / F4 기획탭 작업 / F5 M1-M7)

### push
- commit b8cc8e3 + c904d08 (TODO 표 누락 갱신 보강)

---

## 2026-05-06 (cont.72 Part 5) — 재검 + 자율 보강 5건

### 재검 (모두 통과)
- B6.2 정합 0 mismatch / 96 sweep 0/0 / 회귀 0

### 5 자율 보강 (S2/S5/S8 후속 TODO 해소)
1. CARD_DATA presetIdx fuzzy match (findClosestPresetIdx) → Part 12에서 가중치+명시 매핑 보강
2. collar 22 (data-neck=B) dft 마커 (NECKFINISH_TO_COLLAR 매핑)
3. opening 12 (data-neck=C) dft 마커 (CLOSURE_TO_OPENING 매핑)
4. slider thumb default indicator (.slider-default-mark)
5. 메타-그룹 collapse 상태 localStorage save/restore

### push
- commit 454c461

---

## 2026-04-28 (cont.72 Part 4) — "전부 합시다" 자율 batch: K (inventory) + F (B6.1 lift-and-shift) + G/J/A 보류 결정

### K. 누락 방지 inventory 신설 ✅
`docs/cont72_full_inventory.md` 신설 (single source of truth).

### F. B6.1 rules.json lift-and-shift ✅
6 sample rule (hard 3 + soft 3) + index + cross_category.

### G/J/A 보류
- G. B6.3 fabrics — 이미 외부 분리 완료
- J. 카테고리 분류 6 코드 — Phase 4 옵션 H 동기
- A. Loader 도입 — Phase 5 SaaS 동기 (단일 HTML 원칙)

### push
- commit 6faa879

---

## 2026-04-28 (cont.72 Part 3) — B6.2 lift-and-shift: PresetModule.DB → JSON 분리

### 자율 결정
- Lift-and-shift: 현 schema + 현 enum + 현 cat 그대로
- 9 카테고리 파일 (tshirts/polo/shirtsBlouses/knitwear/sweatshirts/dress/outerwear/skirt/pants)
- Loader 미도입 (PresetModule.DB inline 유지, 회귀 0)

### 구현
data/presets/ 신설 — index.json + 9 파일 / 34 preset (16 top + 8 skirt + 10 pants)

### 검증
- 9 JSON valid / 34 preset DB 정합 mismatchCount 0 / 회귀 0

### push
- commit 9f2234f
