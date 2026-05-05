# FLAT 전체 인벤토리 — cont.72 single source of truth

> **목적:** 누락 방지. 모든 작업/문서/메모리/spec/preset의 status 단일 source.
> **갱신 의무:** 매 cont마다. 항목 추가 시 표 행 추가 + status 갱신.
> **참조 의무:** 매 세션 시작 시 SOP 단계 1에서 read.

**버전:** v0.1 — 2026-04-28 cont.72 (이람 push back 후 누락 방지 시스템 신설)

---

## 1. 코드 자산 (flat-v6.html)

| 영역 | 위치 | 상태 | 회귀 baseline | 후속 |
|---|---|---|---|---|
| BodyComp.geometry sweatshirt 분기 | L2138 (cont.68 Part 1) | ✅ b7b3b46 | halfBody 60.20 / shoulderW 59.17 / sfdArmholeH 71.4 | 다른 preset 옵션 H Phase 4 |
| BodyComp.armholeY sweatshirt 분기 | L2179 (Part 1) | ✅ | sfdArmholeH 적용 | — |
| SleeveComp cuffHalfW sweatshirt 분기 | L2960 (Part 2 축소판) | ✅ 71b7400 | cuffWidth 10.54px | bicep SFD / cap 정밀화 Phase 4 |
| SLEEVE_LENGTH_RATIOS const | L1387~ (S1, cont.69) | ✅ 471caa4 | women/men matrix, default men's | women 활성화 (gender 토글 spec) |
| Default 마커 (.tb.dft) + Reset 버튼 | L48~/L334 (S2) | ✅ 1e97270 | 15 dft 정확 | collar 22 / opening 12 dft 미적용 |
| Slider revert ↺ (.sl-revert) | L66~/L1294 (S5) | ✅ c7a91a0 | 18 ↺ 자동 | thumb dot indicator |
| 메타-그룹 (Design/Fit/Details) | L48~/L347~ (S8) | ✅ cafaec2 | 3 그룹, Details collapsed | localStorage / skirt-pants |
| Sleeve length 라벨 (괄호 병기) | L560/L709/L776 | ✅ | EN/KO 정합 | — |
| PresetModule.DB inline | L5174~ | ⚠️ inline 유지 (B6.2 lift-and-shift 후 source는 JSON) | — | Loader 도입 시 제거 |
| SKIRT_DB / PANTS_DB inline | L5223/L5283 | ⚠️ 동일 | — | 동일 |

## 2. 데이터 자산 (data/)

| 파일 | 상태 | 카운트 | 비고 |
|---|---|---|---|
| data/rules.json | ✅ inline 사용 | 14KB | B6.1 spec 작성 (코드탭 implement 미완) |
| data/presets.json | ⚠️ deprecated (B6.2 신설 후) | 36KB | data/presets/ 가 source of truth |
| data/params.json | ✅ inline 사용 | 20KB | B6 별도 spec 영역 |
| data/fabrics.json | ✅ inline 사용 | 19KB | B6.3 spec 미작성 |
| data/neck_system.json | ✅ inline 사용 | 7.97KB | — |
| data/README.md | ✅ | — | gitignore 예외 (`!data/README.md`) |
| data/rules/sleeve_length_ratios.json | ✅ S1 471caa4 | women+men matrix | gender 토글 미도입 |
| data/presets/index.json | ✅ B6.2 9f2234f | 9 카테고리 메타 | — |
| data/presets/{cat}.json (9 파일) | ✅ B6.2 9f2234f | 34 preset (16 top + 8 skirt + 10 pants) | enum 표준화 / schema 정합 후속 |

## 3. spec 자산 (docs/)

| spec | 상태 | 내용 |
|---|---|---|
| flat_data_separation_presets_spec.md (B6.2 v0.2) | ✅ 작성 (cont.71) / ✅ implement lift-and-shift (cont.72 Part 3) | 32 preset 확장 / 5 카테고리 reorganize 후속 |
| flat_data_separation_rules_spec.md (B6.1 v0.1) | ✅ 작성 (cont.72 기획탭) / ❌ implement 미완 | hard/soft 분류 + 카테고리별 분할 |
| B6.3 fabrics.json spec | ❌ 미작성 | fabric DB 분리 |
| B6.4 parametric 주석 spec | ❌ 미작성 (옵션) | 베지어/cascade 공식 주석 문서 |
| sixatomic_pattern_generate_audit.md (Section 1-22) | ✅ 작성 (cont.69 cowork) | Section 13/14/16 미흡수 |
| sixatomic_implementation_specs.md (S1-S13) | ✅ 작성 / ⚠️ S1/S2/S5/S8 implement, S3/S4/S7 미완, S6 skip, S9/S10/S11 Phase 4+, S12/S13 DEFER, **S14/S15/S16 미작성** |
| flat_design_philosophy_v1.0/1.1/1.2.md | ✅ 원칙 1-17 등록 | — |
| flat_ux_architecture_v1.md | ✅ | 넥 3축 + 카드피드 |
| flat_category_restructure_final.md | ✅ 5 카테고리 + HS코드 + Active Mode | UI 5분할 미적용 (Phase 6) |
| flat_strategy_brief_v3.md | ✅ | — |
| flat_competitive_analysis_v5.md | ✅ Zero Translation | — |
| flat_the_one_tool_scope.md | ✅ IN/OUT | — |
| flat_phase_review_2026-04-20.md | ✅ Stage/Phase | — |
| flat_session_sop.md (cont.69 Group 2) | ✅ 작성 | **호출 강제 미합의** ★ |
| flat_self_check_template.md (cont.69 Group 2) | ✅ 작성 / ⚠️ E 항목 5개 신설 (cont.72) | 매 작업 명시 의무 |
| flat_tab_handoff_template.md (cont.69 Group 2) | ✅ | — |
| flat_env_matrix.md v1.0 → v1.1 (cont.71/72) | ✅ 작성 / ⚠️ 코드탭 인지 미흡 | — |
| flat_collar_direction.md + szkutnicka_collar_reference_map.md | ✅ 작성 / ⚠️ Phase 4 재감사 | — |
| reference_data.md §6.2/6.3/6.4 | ✅ §6.2 적용 (sweatshirt) / ⚠️ §6.3 crewTee §6.4 hoodie 미적용 (Phase 4) | — |
| flat_sweatshirt_pom_proposal.md | ✅ 적용 | — |
| flat_crewTee_pom_proposal.md | ✅ 작성 / ⚠️ 코드 미적용 (Phase 4) | — |
| flat_hoodie_pom_proposal.md | ✅ 작성 / ⚠️ 코드 미적용 (Phase 4) | — |
| flat_preset_expansion_workflow.md v1.1 | ✅ Phase 4 활용 | — |
| flat_designer_feedback_guide.md | ⚠️ Phase 3B factory validation 활용 | — |
| flat_visual_direction_review.md | ⚠️ cont.67 sweep audit 통합 | — |
| reference_donnanno_vol3.md | 🔒 Phase 4 활용 | — |
| fashionpedia_ch5_textile_notes.md | ⚠️ Phase 4 | — |
| collar_geometry_cheatsheet.md | ⚠️ Phase 4 | — |
| audit_cont65_sweep.md | ✅ Phase 1B 과대평가 reset | — |
| cont68_review_inventory.md | ✅ cont.68 Step 0a | — |
| content_handoff.md | ⚠️ 콘텐츠 자동화 라인 (별도 워크스트림) | flat_content_voice.md 미작성 |
| **cont72_full_inventory.md** (이 문서) | ✅ cont.72 신설 | single source of truth |

## 4. 메모리 자산 (~/.claude/projects/-Users-yiram-Claude-flat/memory/)

| 카테고리 | 메모리 | 상태 |
|---|---|---|
| Reference | armstrong / abling | ⚠️ Phase 4 |
| | pattern_sources / engine_patterns | 🔒 학습 자료 |
| | learning_sources / remaining_study | 🔒 학습 |
| | techpack_comparison | ⚠️ 분석만 |
| | factory_terms | ⚠️ i18n 정합성 미검증 |
| | sleeve_techpack_audit | 🔒 Phase 4 |
| | folder_structure | ✅ 정합 |
| | strategy_brief / ai_techpack_sites | ✅ 적용 / ⚠️ |
| | content_automation_lecture | ⚠️ 콘텐츠 라인 |
| | karpathy_skills | 🔒 참고만 |
| Project | 3d_preview / line_architecture / multiview_roadmap | 🔒 Phase 4-7 |
| | category_rework | ✅ 데이터 / ⚠️ UI 5분할 X (Phase 6) |
| | competitive_v3 | ✅ 적용 |
| | conversational_ux | ⚠️ Phase 1 부분 |
| Feedback | workflow_direction | 🔒 Phase 5+ |
| | honesty | ⚠️ 매 세션 적용 (cont.72 self-audit이 검증) |
| | visual_truth | ✅ 원칙 1 |
| | geometry_lessons / restart_over_patch | ✅ 원칙 9 |
| | handoff_first | ✅ CLAUDE.md |
| | use_local_refs | ✅ 원칙 12 |
| User | founder_profile | ✅ 컨텍스트 |

## 5. spec sheet S1-S13 진척

| spec | 상태 | commit |
|---|---|---|
| S1 sleeve length ratio | ✅ | 471caa4 |
| S2 Default 마커 | ✅ | 1e97270 |
| S3 노란 highlight | ❌ 미완 (옵션 카드 일러스트 도입 = 큰 UI 변경) | — |
| S4 카피 표준 | ❌ 미완 (이람 brand voice) | — |
| S5 Revert per-input | ✅ | c7a91a0 |
| S6 Custom 카드 | skip (FLAT 우월) | cafaec2 |
| S7 Progressive disclosure | ❌ 미완 (이람 결정 의존) | — |
| S8 카테고리 메타-그룹 | ✅ | cafaec2 |
| S9 Garment-specific schema | 🔒 Phase 4+ | — |
| S10 Material library | 🔒 Phase 5+ | — |
| S11 Body measurement profile | 🔒 Phase 4+ | — |
| S12 Quota SaaS | 🔒 Phase 5+ | — |
| S13 PLM/ERP | 🔒 Phase 5+ | — |
| **S14 Customise Seams 28 부위** ★ | ❌ spec 미작성 (기획탭 의무) | — |
| **S15 Garment spec vs Body 이중 측정** | ❌ 동일 | — |
| **S16 Multi-select grading** | ❌ 동일 | — |
| **S17 Carbon Design System** (옵션) | ❌ | — |
| **S18 외부 페이지 링크 패턴** (옵션) | ❌ | — |

## 6. 사고 RCA (archive/)

| 사고 | 출처 | 상태 |
|---|---|---|
| (a)~(l) | cont68_rca_2026-04-22.md | ✅ 원칙 15 등록 |
| (m)~(t) | cont69_env_rca_2026-04-23.md (Group 1+1.5) | ✅ 원칙 16/17 등록 |
| (u)(v)(w) | cont.70 (cont69_env_rca 통합) | ✅ cont.71 |
| (x) | cont.71 | ✅ |
| (y)(z) | cont.71/72 (한국어 깨짐 등) | ⚠️ 모니터링 |
| (k)(l)(m) cont.72 보강 | cont.72 (paste 오류 / 흡수 / 가짜 이분법) | ⚠️ 모니터링 |

## 7. 후속 보강 TODO (cont.69-72 누적)

### S1 후속
- Women's matrix 활성화 (gender 토글 spec)
- cap/short/elbow/threequarter cuff 정밀화 (Phase 4 SleeveComp 재구성)

### S2 후속
- ~~collar 22종 (data-neck=B) dft 미적용~~ ✅ cont.72 Part 5 해소
- ~~opening 12종 (data-neck=C) dft 미적용~~ ✅ cont.72 Part 5 해소
- ~~CARD_DATA presetIdx 매핑 (5 카드 모두 idx=0)~~ ✅ cont.72 Part 5 해소 (fuzzy match)
- 라벨 "Default" → "Recommended" (Phase 3B 검증 후) — 보존
- ~~슬라이더 default indicator (S5 통합)~~ ✅ cont.72 Part 5 해소

### S5 후속
- ~~slider thumb dot indicator (default 위치 시각)~~ ✅ cont.72 Part 5 해소
- skirt/pants slider 별도 검증 — 자율 후순위

### S8 후속
- ~~collapse 상태 localStorage 저장~~ ✅ cont.72 Part 5 해소
- skirt/pants 메타-그룹 — 자율 후순위

### B6.2 후속
- Loader 도입 (PresetModule.DB inline 제거 + fetch)
- 5 카테고리 reorganize (spec v0.2 정합)
- enum 표준화 (sixatomic-style)
- 32 preset 확장 (Phase 4 옵션 H 동기)
- schema 정합 (recommendedFabricIds / activeMode / isHero / difficulty)

### Sixatomic 흡수 후속 ★
- Section 13 Customise Seams 28 부위 (S14 spec 작성 필요)
- Section 14.1 Garment spec vs Body 이중 측정 (S15)
- Section 14.4 Multi-select grading XS-XL (S16)
- Section 16 A Carbon Design System reference (S17 옵션)
- Section 16 F 외부 페이지 링크 패턴 (S18 옵션)
- Sleeve Fabric / Sleeve Hem Bind / Sleeve Fit 분리 / Collar Band Construction / First Button Placement / Bust Dart / Front Detail / Hem A Line / Slit Depth / Spline / Yoke split / Placket sub-options

### cont.71 카테고리 분류 6 결정 코드 implement
- vest_sweater = KNITWEAR + OUTERWEAR — preset 추가
- mock_neck = T-SHIRTS + KNITWEAR — preset 추가
- half_zip = SWEATSHIRTS + KNITWEAR — preset 추가
- 'sweater' rename → 'pullover_sweater' (KNITWEAR Hero)
- tunic / rugby = 추가 X (파라미터로 도달)

### Phase 3B (이람 진행 중 — cont.72 명시)
- factory validation 섭외 (성수동 2 + 동대문 1)
- 디자이너 인터뷰 3명

### Phase 4 DEFER (3D 동기)
- 옵션 H 나머지 preset (crewTee/hoodie/polo/shirt/blazer/bomber/trench/cardigan/dress)
- sleeve cap/곡선 정밀화
- 칼라 22종 재감사
- cont.63 90° 블렌딩 롤백 판정
- 앞/뒤 비대칭, 패턴메이킹 정확도

### Phase 5+ DEFER
- 트렌드 파라미터화 / Claude API 자연어 / 바디 스캔 API (Phase 5)
- 파일 분할 / 인증/저장/결제 (Phase 6)
- 봉제선 쪼개기 / 선 추가 (Phase 7)

### 데모 마감 (이람 영역 — 별도 채팅)
- YC S26 지원서 (5/4)
- S.STAGE 풀 데모 + 1분 영상 (5/3)
- IR 덱 커버 (트레이싱 프리즈)

### 콘텐츠 자동화 (이람 의존)
- FLAT 브랜드 톤 문서 (`docs/flat_content_voice.md`)
- 포맷 1개 선택

---

## 8. 갱신 이력

- **2026-04-28 cont.72 v0.1**: 신설. 이람 push back 누락 방지 시스템 5단 중 #2.
