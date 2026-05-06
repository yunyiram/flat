# FLAT cont 단위 audit 표 양식 (누락 방지 #3)

> **목적:** 매 cont 종료 시 빠짐없는 작업/검증 기록 양식.
> **이람 cont.72 push:** "지난번에 몇번이나 누락" 신뢰 손상 패턴 방지.
> **누락 방지 시스템 #3** (HANDOFF "🛡 누락 방지 시스템" 명시).
> **버전:** v0.1 — 2026-05-06 cont.72 Part 8 자율 신설.

---

## 1. 적용 시점

**의무:**
- 매 cont 종료 직전 (commit 전)
- 큰 batch 작업 (5+ commit) 종료 시
- 이람 push back 후 재검 시

**선택:**
- 작은 micro 보강 (단일 commit)에서는 self_check_template만으로 충분

---

## 2. 표 양식 (cont 단위)

매 cont 끝에 progress.md / HANDOFF "🔵 코드 → 기획" 섹션에 다음 양식 명시.

### 2.1 작업 요약

| 작업 | 위치 | 상태 | 검증 |
|---|---|---|---|
| 신규 함수/모듈 | flat-v6.html L?? | ✅/⚠️/❌ | 96 sweep / DOM 실측 / 시각 / 회귀 baseline |
| 신규 데이터 | data/?.json | ✅ | json valid + DB 정합 mismatchCount |
| 신규 문서 | docs/?.md | ✅ | force-tracked / link 정합 |
| HANDOFF 갱신 | "🔵 코드 → 기획" | ✅ | 백업 + 섹션 단위 |
| inventory 갱신 | docs/cont72_full_inventory.md | ✅ | 해당 영역 status 변경 |
| 🟡 양쪽 공유 TODO 표 갱신 | HANDOFF L?? | ✅ | 신규 항목 등록 / 해소 항목 strikethrough |

### 2.2 회귀 baseline 검증

| 영역 | baseline | 현재 |
|---|---|---|
| crewTee halfBody / shoulderW | 55 / 46 (cont.68) | ?? |
| sweatshirt halfBody / shoulderW / sfdCuffHalf | 60.20 / 59.17 / 5.19 (cont.68 Part 2) | ?? |
| 16 preset × 6 sleeve length sweep | NaN 0 / Exception 0 | ?? |
| Console errors | 0 | ?? |

### 2.3 데이터 정합성

| 데이터 | 소스 | 검증 |
|---|---|---|
| 16 top preset (PresetModule.DB) | flat-v6.html L5174 | data/presets/ 정합 |
| 8 skirt preset (SKIRT_DB) | L5223 | data/presets/skirt.json |
| 10 pants preset (PANTS_DB) | L5283 | data/presets/pants.json |
| i18n EN/KO 318 keys | LANG.en/ko | enMissing 0 / koMissing 0 |
| 22 collar enum | data-neck="B" | NECKFINISH_TO_COLLAR 매핑 |
| 41 fabric DB | data/fabrics.json | 항목 카운트 |
| 60 봉제 현장용어 | data/factory_terms.json | structure/sewing/.../fabric 8 카테고리 |

### 2.4 후속 TODO 등록

| 항목 | 사유 | 우선순위 | 의존 |
|---|---|---|---|
| (예) gender 토글 spec | S1 후속 — Women's matrix 활성화 | 중 | 이람/spec |
| (예) Loader 도입 | B6.2 후속 | 저 | Phase 5 SaaS |

### 2.5 누락 방지 self-check (cont.72 신설 F 그룹)

매 cont 끝 응답에 명시 공개:
- ✅/❌ F1 메모리 28+ 항목 cross-check
- ✅/❌ F2 docs/ 안 관련 문서 cross-check
- ✅/❌ F3 archive/ 사고 RCA 인지
- ✅/❌ F4 cont.N 기획탭 작업 인지 (HANDOFF 헤더)
- ✅/❌ F5 M1-M7 미확인 항목 영향 검토

---

## 3. 적용 사례 (cont.72 Part 7-8 예시)

### Part 7 (전체 audit)

| 작업 | 위치 | 상태 |
|---|---|---|
| inventory § 8 신설 | docs/cont72_full_inventory.md | ✅ Quality-Insufficient 영역 12+ 등록 |
| HANDOFF "🚨 Part 7" 섹션 | HANDOFF.md | ✅ |
| commit 1a90f65 | git | ✅ |

### Part 8 T1-T4 (자율 batch)

| 작업 | 검증 |
|---|---|
| plan.md "Current Status" 정정 | 49→34, 11 항목 ⚠️ |
| i18n sleeve.capped 정정 | 318/318 100% |
| docs/copy_guide.md 신설 | force-tracked, 6 톤 규칙 |
| 한국어 깨짐 검증 | flat-v6.html / data/ / HANDOFF / inventory / progress / plan U+FFFD 0 |
| Style Overlay 7 sweep | 7/7 작동 |
| CM toggle | cm ↔ inch ✓ |
| Body size mapping | chest 갱신 ✓ / hipFlare 미작동 ⚠️ |
| Compat system 카운트 | 6 system (plan.md 12 부정확) |
| Skirt 8 sweep | NaN 0 / Exc 0 |
| Pants 10 sweep | NaN 0 / Exc 0 |
| 22 collar sweep | NaN 0 / Exc 0 |
| Sleeve shape 10 sweep | NaN 0 / Exc 0 |
| fabric DB 41 정확 | plan.md 정합 |
| data/factory_terms.json 신설 | 60 용어 / 8 카테고리 |
| commit f693bfc / 336f063 / 8677f83 | git |

---

## 4. 변경 이력

- **2026-05-06 v0.1**: 코드탭 cont.72 Part 8 자율 신설. 누락 방지 시스템 #3 적용 (4/5 → 5/5 완료).

---

## 5. 참조

- 누락 방지 시스템: `HANDOFF.md` "🛡 누락 방지 시스템" 섹션
- Self-check 양식: `docs/flat_self_check_template.md` v1.1 (E + F 그룹)
- Inventory: `docs/cont72_full_inventory.md` § 8 Quality-Insufficient
- 세션 SOP: `docs/flat_session_sop.md`
- 환경 매트릭스: `docs/flat_env_matrix.md` v1.1
- 탭 인계 양식: `docs/flat_tab_handoff_template.md`
