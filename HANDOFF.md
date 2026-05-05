# FLAT 핸드오프
> **모든 탭은 세션 시작 시 이 파일을 먼저 읽는다.**
> 섹션 단위 수정만. 전체 덮어쓰기 금지 (원칙 7).

마지막 수정: 2026-04-28 코드탭 cont.69 Part 2 — **S2 완료 (commit 대기)**. flat-v6.html 단일 파일 변경 (CSS dft dot + Reset 버튼 + state currentPresetIdx + updateRecommendedMarkers/resetToDefault 함수 + i18n EN/KO + CardFeed 진입 hook). PresetModule.DB 활용 (JSON 신설 X, 자율). 검증 96 case sweep NaN/Exc 0, 회귀 0, dft 정확성 100%. 이람 검수 OK + "후속 보강 메모 잊지 말고" 강조. 후속 TODO 5개 등록 (collar/opening data-neck dft, CARD_DATA 매핑, 라벨 격상, 슬라이더 indicator). 이전: 2026-04-28 S1 완료. 백업: `docs/archive/HANDOFF-20260428-cont69-S1-step3-backup.md`. 마지막 수정: 2026-04-28 기획탭 cont.70 — (1) 사고 3개 발견 (cont69_env_rca 통합 DEFER, MCP timeout 6회 누적): **(u) 도메인 침범** (Claude 추천이 이람 다른 세션 영역 흡수 = 영상/지원사업, 사고 (h)/(o)와 다른 차원, C3 도메인 분리 위반) / **(v) MCP timeout 패턴화** (사고 (s) 1회 재시도 회복 부족 검증, 단 cont.70 후반 write_file 정상 회복 = 영구 아님 일시적) / **(w) 큰 파일 head/tail 분할 default** (HANDOFF 전체 read timeout, head 50/300은 성공). (2) Phase 3A UX/UI 1순위 결정 = "YC S26 및 S.STAGE 지원서 업데이트" 채팅으로 분업 이관 (영상 60초 + 지원사업 정리). (3) ✅ B6.2 presets.json 분리 spec v0.1 작성 완료 (`docs/flat_data_separation_presets_spec.md`, write_file + head 10 read 검증, 메모리 #16 도메인 로직 보존 직접 대응). (4) MCP 정상화 후 다음 세션 의무: archive/ read alive 검증 → cont69_env_rca에 사고 (u)(v)(w) 통합 + B6.2 spec full read 검증 + ★ 카테고리 분류 6항목 + KNITWEAR Hero 결정 + B6.1 (rules) / B6.3 (fabrics) 후속. 이전: 2026-04-27 기획탭 cont.69 Group 2 완료 — (1) 사고 (t) 통합 (2) 환경 매트릭스 v1.0 (`docs/flat_env_matrix.md`) (3) 자가검증 양식 v1.0 (`docs/flat_self_check_template.md`) (4) 탭 인계 양식 v1.0 (`docs/flat_tab_handoff_template.md`) (5) 세션 시작 SOP v1.0 (`docs/flat_session_sop.md`, 8단계 + 복잡도별 단축 + 환경별 분기 + 다른 3 양식 의존 관계) + 📏 규칙 3 보강 (SOP 호출 명시). 이전: 2026-04-27 기획탭 — **S1 (Sleeve length %) implement 착수 지시 추가** (🔴 기획→코드 cont.69 신규 서브섹션, cowork tab 의사결정 후속). 백업: `docs/archive/HANDOFF-20260427-S1-flat-handoff-backup.md`. 다음 코드탭 작업: spec sheet `docs/sixatomic_implementation_specs.md` Section 1 (S1) read → flat-v6.html SleeveComp 현재 로직 보고 → 이람 OK → implement → 검증. 그 이전: 2026-04-27 cowork tab — Sixatomic Pattern Generator (https://app.sixatomic.com/synthesis/pattern/generate) v2 라이브 감사 + 4종 base style diff + Materials/Seams/Sizes/Notes 풀 채록 + KS K 0051 표준 사이즈 입력 + audit md 재검 패치 + 코드탭용 atomic spec sheet (S1-S13) 신설 + **이람 의사결정 완료 (S1-S8 확정 진행, S9-S11 보류, Q2 = "좋은 것만 훔치고 취해서 더 나은 걸 만든다")**. 산출물: `docs/sixatomic_pattern_generate_audit.md` (Section 1-22), `docs/sixatomic_implementation_specs.md` (S1-S13). 백업: `docs/archive/HANDOFF-20260427-cowork-sixatomic-v2-backup.md`. 이전: 2026-04-26 기획탭 cont.69 Group 1.5 완료 — 원칙 17 (환경 정합성, 절차/시스템 설계 시점) 신규 등록, 외부 채팅 입장 절차 명문화, 규칙 9 (변형 vs 새 패턴 판정, 우로보로스 차단) 추가, 사고 (n)(o)(p)(q)(r)(s) 추가 RCA 보완 (cont69_env_rca 안 통합). 그 이전: 2026-04-26 cont.69 Group 1 (원칙 16 + RCA 2개 작성 + 사고 (m) 정정). 그 이전: 2026-04-23 cont.68 Step 0b. 그 이전: 2026-04-22 cont.68 Step 0a.

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
15. **[신규 cont.68 Step 0a] 비약 금지. 완전성 우선.**
    - **근거:** cont.68 영상 스크립트 섭부른 결합 사고. RCA: `docs/archive/cont68_rca_2026-04-22.md`
    - **6 세부규칙:**
      1. **짧은 답 ≠ 진행 허가.** 결합/진행 방식은 한 줄 질문으로 확인.
      2. **역할 분담.** 패션/비주얼 = 이람 전문, 이람 결정. 시스템/구현/도구 = 이람 배움, 내가 정답 제시 → 이람 OK. 옵션 2개 이상이면 trade-off + 추천 + 이람 OK. 단순 A/B/C 떠넘기기 금지.
      3. **"빨리 보여줘" 압박은 자체 발명.** 무시. 이람은 완성도 우선 명시.
      4. **정답이 있으면 정답.** 명확 → 그걸로. 모호 → 옵션 + 추천 + 이람 OK. 안 보임 → 조사 (원칙 11/12).
      5. **비약 4종 금지:**
         - ① 이람 응답 범위를 넘어선 결합/추가/생략
         - ② 시스템과 인스턴스 구분 안 한 동시 처리
         - ③ 기존 자산 미검토 + 신규 작성
         - ④ "이 정도면 됐다" 종결
      6. **좋아보이는 것 ≠ 좋은 것.** 충돌 시 항상 좋은 것.
         - 좋아보이는 것 = 즉각 매력, 양/속도, "효율적" 보임
         - 좋은 것 = 시스템 일관성, 기존 자산 활용, 완성도, 정합성
    - **확장 self-check 9-16개 (작업 시작 전 + 산출물 직후 두 번, 결과 응답 명시 공개):**

      **[A. 원칙 15 파생 — 매번 필수 6개]**
      - [ ] 시스템 vs 인스턴스 구분했나?
      - [ ] 기존 프로젝트 문서 read했나?
      - [ ] 이람 응답 범위 안에서 진행 중인가?
      - [ ] 좋아보이는 것 / 좋은 것 구분했나?
      - [ ] 철학 문서 정합성 검증했나? (v1.0~1.2, ux_arch_v1, decision-making rules)
      - [ ] Phase 1 / Phase 2 범위 분리했나?

      **[B. HANDOFF 운영 원칙 해당 시 6개]**
      - [ ] 원칙 4: "구현됨" ≠ "앞에 내밀 수 있음" — head:60 read = "완료" 아님
      - [ ] 원칙 6: 검증 가능한 산출물 없으면 완료 금지
      - [ ] 원칙 7: HANDOFF 섹션 단위 + 백업
      - [ ] 원칙 9: 반복 피드백 = 아키텍처 문제 (같은 영역 3회 이상 수정 중단)
      - [ ] 원칙 11: 기획탭 자율성 (A/B/C 떠넘기기 금지)
      - [ ] 원칙 14: 매력도 vs 정확도 구간 명시

      **[C. Decision-making rules 해당 시 4개]**
      - [ ] 현재 자산 과대평가 금지
      - [ ] Route B가 결국 Route A로 돌아오면 Route A 먼저
      - [ ] 탭 도메인 존중
      - [ ] 작동하는 것과 경쟁, 안 되는 건 동선에서 빼기

    - **응답 명시 의무:** 각 self-check 결과를 응답 안에 짧게 명시 공개. 자기 보고 → 감사 가능 투명 박스. 해당 없는 항목은 "해당 없음" 명시.

    - **원칙 15 ↔ 원칙 1-14 관계 표:**
      | 원칙 | 관계 | 시사점 |
      |---|---|---|
      | 1 (수학+시각) | 무관 (설계 기준) | 해당 시 별도 |
      | 2 (계층) | 무관 (설계 기준) | 해당 시 별도 |
      | 3 (카테고리 안내) | 보강 | 원칙 15가 "좋은 것" 우선 → 차단 대신 안내 강화 |
      | **4 (과대평가 금지)** | **보강** | 원칙 15 self-check "기존 자산 read" + "완성도 우선" 강화 |
      | 5 (트레이싱 프리즈) | 무관 (비주얼) | 해당 시 별도 |
      | **6 (검증 없이 완료 금지)** | **보강** | 원칙 15 "좋은 것" 우선 = 검증 후 완료 |
      | 7 (HANDOFF 섹션 단위) | 무관 (운영 절차) | 준수 |
      | 8 (Stage/Phase 분리) | 무관 (용어) | 준수 |
      | **9 (반복 피드백 = 아키텍처)** | **보강** | 원칙 15 "이 정도면 됐다 금지" = 아키텍처 재검토 신호 무시 금지 |
      | 10 (전수 자동 검수) | 무관 (검수 방법) | 원칙 6과 같이 작동 |
      | **11 (기획탭 자율성)** | **보강** | 원칙 15 "내가 정답 제시" = 떠넘기기 금지와 일치 |
      | 12 (공룡기업 데이터) | 무관 (외부 참조) | 해당 시 활용 |
      | 13 (자동 진행 모드) | **보강** | 묵시적 OK 전제 = 원칙 15 한 줄 질문과 양립, 짧은 답 해석 주의 |
      | **14 (매력도 vs 정확도)** | **보강** | Phase 구간별 정확도 기준 = 원칙 15 Phase 분리 self-check와 일치 |

    - **신규 원칙 등록 시 의무 (원칙 15 자체 적용):**
      1. 원칙 간 관계 표 작성 (보강 / 대체 / 충돌 / 무관)
      2. 적용 조건 명시 (매번 / 특정 작업 / 특정 단계)
      3. self-check 항목 확장 필요 시 추가
      4. RCA 근거 (있으면)

    - **운용 원칙:** 빠진 것 없이 / 더 나은 것 반드시 취하기 / 좋아보이는 것·좋은 것 구분, 좋은 것만 / 전체 리뷰 + 반복 검토 + 비약 없이 진행

16. **[신규 cont.69] 환경 인식 + 검증 사이클.**
    - **근거:** cont.69 첫 응답 환경 인식 누락 (HANDOFF 직접 접근 가능 환경에서 불가 선언). RCA: `docs/archive/cont69_env_rca_2026-04-23.md` (사고 1 + (a)~(m) 14개)
    - **규칙 8 본문:**
      capability/context 부재 또는 존재 선언 전:
      1. **환경 명시** — 어느 환경 (Claude 컨테이너 / 사용자 컴퓨터 Mac / 웹 / 외부 MCP)
      2. **tool_search** — 해당 환경 deferred 도구 로드 확인
      3. **실제 호출 검증** — 목록 확인 ≠ 동작 확인
      4. **실패 시 fallback** — 다른 환경 도구로 시도
    - **부속:**
      - 추측을 평서문으로 표현 금지
      - 모르면 "모름" 명시
      - self-check ✅ 표시와 본문 모순 자가검증 1회
    - **확장 self-check D 항목 (4개, 도구 호출 시 매번):**
      - [ ] D1. 환경 명시 (Claude 컨테이너 / Mac / 웹 / 외부 MCP)
      - [ ] D2. tool_search로 deferred 도구 확인
      - [ ] D3. 실제 호출로 검증 (목록 ≠ 동작)
      - [ ] D4. 추측 평서문 금지 + ✅과 본문 모순 자가검증
    - **원칙 16 ↔ 원칙 1-15 관계 표:**
      | 원칙 | 관계 | 시사점 |
      |---|---|---|
      | 1-3 (설계 기준) | 무관 | 해당 시 별도 |
      | **4 (과대평가 금지)** | **보강** | "구현됨" 단정 전 검증 = capability "있음/없음" 단정도 검증 |
      | 5 (트레이싱) | 무관 | 별도 |
      | **6 (검증 산출물)** | **보강** | 검증 메커니즘 일치 |
      | 7-8 (운영) | 무관 | 준수 |
      | 9-14 | 무관 | 별도 |
      | **15 (비약 금지)** | **독립 (다른 차원)** | 비약=추론 비약, 환경=capability 인지. self-check D 항목으로 분리 |
    - **적용 조건:** 도구 호출 시 매번 (탭/세션 무관). cont.68 규칙 1-7 (옵션 추천 + 매몰 비용 + 절충 default + push back 청산 검토 + self-check 9-16 + 이람 감사 + 메타 개선) 과 별도 작동.
    - **운용:** 사고 자가인지 신뢰도 낮음 인정 → 이람 push back이 궁극 안전망 (규칙 6).
    - **워크플로우 E''' (G+H 합의, cont.69):** 옵션 C (현 세션 인프라 구축) + 사고 발생 시 RCA + 규칙 갱신 + 현 세션 재개. 임계 조건 미정 (데이터 누적 후 결정). D-2 (새 세션 전환) 트리거 = 이람 "그만하고 싶음" 직관 (이람 영역).

17. **[신규 cont.69 Group 1.5] 환경 정합성 — 절차/시스템 설계 시점.**
    - **근거:** cont.69 Group 1 완료 후 "다음 세션 자동 진행 절차" 5단계 작성. 이람이 새 세션에 보냄. 새 세션 Claude: "체크리스트 그대로 돌면 거짓말 ✓ 5개" — 5단계 모두 새 세션 환경에서 작동 안 함. RCA: `docs/archive/cont69_env_rca_2026-04-23.md` 사고 (o).
    - **원칙 16과의 차이:**
      - 원칙 16 = 도구 호출 시점 환경 검증 (실시간 차원)
      - **원칙 17 = 절차/시스템 작성 시점 환경 정합성 (설계 차원)**
    - **규칙 본문:**
      절차/체크리스트/시스템 작성 시:
      1. **작동 환경 목록화** — 이 절차가 어느 환경에서 작동하는지 명시
      2. **타 환경 적용 가능성 검증** — 컨텍스트 0%로 시작하는 환경에서도 작동하는가
      3. **차선 절차 명문화** — 작동 안 하는 환경을 위한 fallback 절차
    - **적용 조건:** 새 절차/시스템/체크리스트 작성 시 매번. 특히 "다음 세션·탭·환경" 이관 점을 포함하는 절차.
    - **구체 적용 사례 (외부 채팅 입장 절차):** 아래 별도 섹션 참조.
    - **원칙 17 ↔ 원칙 1-16 관계 표:**
      | 원칙 | 관계 | 시사점 |
      |---|---|---|
      | 1-3 (설계) | 무관 | 면적 겹치지 않음 |
      | **4 (과대평가)** | **보강** | "자동 진행" 가정 = 자산 과대평가 |
      | 5 (트레이싱) | 무관 | 별도 |
      | **6 (검증 산출물)** | **보강** | 절차 검증 = 자체가 산출물 검증 |
      | 7-8 (운영) | 무관 | 준수 |
      | 9-14 | 무관 | 별도 |
      | **15 (비약 금지)** | **보강** | 설계 시점 비약 수단 |
      | **16 (실시간 환경 검증)** | **짝 (다른 시점)** | 16=호출 시점, 17=설계 시점 |
    - **운용:** 이람 push back이 궁극 안전망. 절차 작성 시 "이 절차가 안 작동하는 환경이 있는가" 자가검증.

---

## 🔗 외부 채팅 입장 절차 (원칙 17 구체 적용)

**외부 채팅 = FLAT 프로젝트 외부에서 시작된 채팅.** 이 환경에서는 HANDOFF.md 직접 접근 불가, 메모리 scope 제한, 프로젝트 파일 접근 불가.

### 권장 수서

1. **1순위 — 프로젝트 안 새 세션 이동.** Claude 채팅 넓이 "프로젝트 > FLAT" 안에서 새 세션 시작. HANDOFF.md 자동 첨부 + 메모리 scope 정합.
2. **2순위 — HANDOFF.md 인라인 paste 또는 업로드.** 이동 불가 시 이람이 채팅에 직접 첨부 또는 paste.
3. **3순위 — 외부 채팅에서 standalone 작업.** 이동/첨부 다 불가 시 Claude가 user preferences + 메모리 + 대화 단서로 컨텍스트 재구축. 이 환경에서는 HANDOFF 안의 상세 절차 작동 안 함 명시.

### Claude 측 의무

- 외부 채팅에 "환경 확인" 도구 호출 (규칙 8 D1) 시 프로젝트 안인지 밖인지 명시 보고
- 외부 식별 시 업로드/paste/이동 옷션 이람에 제시
- 외부 세션 수용 시 "원칙 17 적용 안 되는 환경" 명시 후 standalone 작업

### 이람 측 조치

- 새 세션 시작 전 위치 확인 (프로젝트 안/밖)
- 외부에서 시작한 채팅을 프로젝트로 이동하려면 Claude 채팅 UI에서 채팅 설정 → 프로젝트 이동

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

> **※ 별 라인 cross-ref (2026-04-27 추가):** S1 (Sleeve length %) implement는 sixatomic 흡수 라인의 **별도 우선순위로 cowork tab에서 이미 확정**. 본 6 후보(매력도 작업)와 **병렬 진행 가능** — S1 착수가 Phase 3A 1순위 결정을 막지 않음. 코드탭은 "🔴 기획 → 코드 cont.69" 서브섹션 + "🟣 외부 세션 2026-04-27" 섹션 참조하여 S1부터 진행.

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

## 🟣 외부 세션 (Cowork tab) 작업 알림

### 2026-04-27 — Sixatomic Pattern Generator v2 라이브 감사 완료

**환경:** Cowork tab (Chrome MCP + WebSearch). 코드/HANDOFF 본문 수정은 안 함, 학습 자료 신설만.

**작업 범위:**
- 4종 base style 풀 비교 (Women's T-shirt / Men's T-shirt / Women's Shirt / Men's Shirt)
- Women's Shirt 풀 wizard 완주 (Style → Design → Materials → Seams → Sizes → Notes 6단계 모두 채록)
- KS K 0051 한국 여성 표준 사이즈 + Sixatomic default profile 5종 비교 (M = 88/70/92/165 cm 권장)
- v1 audit 자체 재검 → 정정 6건 + 보강 6건 + 미확인 7건 정리

**산출물 (모두 docs/ 안, 기획탭이 1차 컨슈머):**

| 파일 | 내용 | 다음 사용 |
|---|---|---|
| `docs/sixatomic_pattern_generate_audit.md` | v1+v2+재검 패치, Section 1-22 | 기획탭 (이람) — 의사결정 input |
| `docs/sixatomic_implementation_specs.md` | 코드탭용 atomic spec S1-S13 + 우선순위 매트릭스 + 작업 흐름 | 코드탭 — 이람 결정 후 implement |

**이람 의사결정 결과 (2026-04-27 cowork tab 마무리):**
1. ✅ Section 17.1 **즉시 도입 5개**: **S1부터 1개씩 순차, 5개 다 함** (이람: "다 하긴 해야함 최선으로")
2. ✅ Section 17.4 **흡수 전략**: **"좋은 것만 훔치고 취해서 더 나은 걸 만든다"** (이람 표현 그대로 — 선택적 흡수 + 재창조)
3. 🟡 Section 17.2 **garment-specific schema (S9)**: **보류** — S1-S5 진행 중 자연스럽게 재평가. 이람: "이거 여기서 판단하는 거 맞아?" → 옳은 push back. Phase 4 가까워지면 다시 결정.
4. 🟡 **Material library / Body measurement profile 외부 분리 (S10/S11)**: 보류 (Phase 5+ 자연 재평가)

**확정 작업 순서 (코드탭 implement, spec sheet Section 0 참조):**
```
S1 (Sleeve length %) → S2/S3 묶음 (Recommended 배지 + 노란 highlight) → S4 (카피 표준)
→ S5 (Revert per-input) → S6 (Custom 카드 통합) → S7 (Progressive disclosure 작은 시작)
→ S8 (카테고리 그룹 정리) → [Phase 4 시점 S9-S11 재평가]
```

**S1부터 시작 권장 — 다음 코드탭 세션의 첫 spec 지시:**
- HANDOFF "🔴 기획→코드"에 "S1 (Sleeve length %) implement 착수" 추가하면 코드탭이 진행

**미확인 항목 7개 (다음 cowork 세션 의제):**
- audit Section 20.3 + spec sheet Section 2 참조. **M4 (Body measurement profile 상세 측정 항목)** 가 가장 중요 — S11 spec 정확도에 직접 영향.

**양탭 세션 시작 시 누락 방지 체크리스트 (audit Section 21.4 복사):**
```
□ 이 🟣 섹션 read 했는가?
□ docs/sixatomic_pattern_generate_audit.md (697줄) 존재 확인했는가?
□ docs/sixatomic_implementation_specs.md (479줄) 존재 확인했는가?
□ progress.md 최상단 cowork tab 알림 read 했는가?
□ Section 20.3 미확인 7개 (M1~M7) 다음 의제로 인지했는가?
```

**spec implement 시 코드탭 사전 절차 (원칙 4·6):**
1. CLAUDE.md → HANDOFF.md → progress.md → plan.md 순서로 read (CLAUDE.md 지침)
2. spec sheet의 해당 spec ID read
3. spec의 "대상 파일"이 명시한 flat-v6.html 영역 read → **현재 로직 보고**
4. 이람 OK 후 implement
5. 검증 (NaN/undefined/Exception 0 + sweep + DOM 실측 + 회귀)
6. /save-progress 실행
7. HANDOFF "🔵 코드→기획" 업데이트 + commit (message에 spec ID 명시)

**자체적용 self-check (원칙 15·16·17):**
- ✅ 시스템(Sixatomic 학습) vs 인스턴스(FLAT 적용) 분리 — audit + spec 분리
- ✅ 기존 자산 read — HANDOFF.md, progress.md, audit md 전체 read
- ✅ 이람 응답 범위 안 — "위 내용들 하나도 빼먹지 않도록 전달" 정확히 응답
- ✅ 좋아 보이는 것 vs 좋은 것 — 모든 spec을 "이람 OK 후 implement" 게이트
- ✅ 환경 명시 — spec sheet Section 4에 환경별 작동 가능 작업 매트릭스
- ✅ HANDOFF 백업 + 섹션 단위 추가 (전체 덮어쓰기 X)

---

## 🔴 기획 → 코드

### cont.69 — S1 (Sleeve length %) implement 착수 지시 (2026-04-27, cowork tab → 코드탭)

**컨텍스트:** 2026-04-27 cowork tab Sixatomic Pattern Generator v2 라이브 감사 결과, 이람 의사결정 = *"S1부터 1개씩 순차, 5개 다 한다 (S1→S2/S3→S4→S5→S6→S7→S8). Q2 = 좋은 것만 훔치고 취해서 더 나은 걸 만든다."* (HANDOFF "🟣 외부 세션" 섹션 2026-04-27 항목 참조)

**작업 spec:** **S1 (Sleeve length를 % of side arm length로 정량화)**

**spec 본문 — 코드탭 read 필수:** `docs/sixatomic_implementation_specs.md` Section 1 "S1" 전문

**근거 audit:** `docs/sixatomic_pattern_generate_audit.md` Section 10.2

**핵심 변경 (요약 — 상세는 spec 본문 read):**
- `flat-v6.html` SleeveComp의 sleeve length 계산을 **side arm length × ratio** 모델로 변환
- ratio 매핑 (Women's, sixatomic 채록값):
  Very Short 0.266 / Short 0.310 / **Regular 0.353 (default)** / Above Elbow 0.447 / Forearm 0.723 / Wrist 1.000 / Full 1.075
- Men's 별도 매핑: 0.290 / 0.335 / 0.385 / 0.485 / 0.780 / 1.000 / 1.075
- garment별 default 다름 (셔츠 = Wrist, T-shirt = Regular)

**대상 파일:**
- `flat-v6.html` SleeveComp 영역 (cont.68 Part 2 commit 71b7400 baseline 위에서 수정)
- `data/presets/*.json` 또는 신설 `data/rules/sleeve_length_ratios.json` (코드탭 자율 판단)

**검증 (원칙 6 — DOM 실측 + sweep + 회귀):**
- DOM 실측: 16 preset × 5 sleeve length = 80 case sweep, NaN/undefined/Exception 0
- 회귀 baseline 유지:
  - sweatshirt cuffWidth 10.54px (cont.68 Part 2)
  - crewTee halfBody 55, shoulderW 46
- 시각: ratio 0.353 적용 시 sleeve 끝점이 mid-bicep ~ 팔꿈치 위 범위에 도달

**작업량:** 1-2시간 (spec 견적)

**의존:** 없음 — S1은 가장 가벼운 win, 첫 작업

**이 spec의 후속 spec (참고용, 지금 작업 X):** S6 (Recommended 배지)에서 default = Regular = 0.353 명시 시 S1 매핑 활용

**원칙 11 코드탭 자율 범위:**
- ratio 데이터 위치 (preset.json 분산 vs `sleeve_length_ratios.json` 신설) 코드탭 판단 후 이람 OK
- SleeveComp 안 어느 라인에 적용할지 판단
- 단, **이람 OK 전 implement 금지** (`sixatomic_implementation_specs.md` 초입: "모든 spec은 이람 OK 전엔 보류. 자율 시작 금지")

**코드탭 사전 절차 7단계 (HANDOFF "🟣 외부 세션" 섹션에서 기명 — 그대로 적용):**
1. CLAUDE.md → HANDOFF.md → progress.md → plan.md read
2. `docs/sixatomic_implementation_specs.md` Section 1 (S1) read
3. `flat-v6.html` SleeveComp 영역 read → **현재 sleeve length 계산 로직 기획탭에 보고** (HANDOFF "🔵 코드 → 기획" 새 서브섹션)
4. 이람 OK 후 implement
5. 검증 (NaN/undefined/Exception 0 + 80 case sweep + DOM 실측 + 회귀 baseline 유지)
6. `/save-progress` 실행
7. HANDOFF "🔵 코드 → 기획" 업데이트 + commit (message에 spec ID 명시 — 예: `S1: sleeve length ratio model (Women's + Men's)`)

**진척 보고 위치:**
- HANDOFF "🔵 코드 → 기획" 새 서브섹션 — 현재 로직 보고 → 구현 결과
- `progress.md` 최상단 — 작업 로그

**다음 단계 (S1 완료 + 이람 검수 OK 후):** 기획탭이 S2/S3 묶음 (Recommended 배지 + 노란 highlight) 지시 추가. spec sheet Section 0 작업 순서대로 (S1 → S2/S3 → S4 → S5 → S6 → S7 → S8).

---

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

### 🟢 cont.69 Part 2 — S2 완료 (2026-04-28, commit 대기)

**작업:** Sixatomic 흡수 두 번째 spec. Recommended 배지 시스템 — A 옵션 채택 (S2만 분리, S3 큰 UI 변경은 별도 spec).

**자율 결정 (이람 OK 후):**
- garment_defaults.json **신설 X** — PresetModule.DB(16 preset) 기존 데이터 활용. 60 default 결정 부담 회피.
- 라벨 톤 = "Default/기본값" (실무 검증 전 "Recommended" 과대평가 회피, 원칙 4)
- Reset 범위 = 전체 preset 복원 1개 버튼

**구현 (flat-v6.html 단일 파일):**

| 위치 | 변경 |
|---|---|
| L47-48 CSS | `.tb` `position:relative` + `.tb.dft::after` 회색 5px dot 우상단 + `.tb.on.dft::after{display:none}` (active 자동 숨김) + `.reset-btn` |
| L334 HTML | 헤더에 `<button class="reset-btn" id="resetBtn" onclick="resetToDefault()">↺</button>` |
| L755/930 i18n | EN `reset:{title:'Reset to default'}` / KO `reset:{title:'기본값으로 복원'}` |
| L933 applyLang | data-i18n-title 처리 + 끝에 `updateRecommendedMarkers()` |
| L995 state | `currentPresetIdx, currentSkirtIdx, currentPantsIdx` 추가 |
| L1240 신규 fn | `updateRecommendedMarkers()` (top/skirt/pants 자동 분기) + `resetToDefault()` |
| L5210/5276/5300 | PresetModule.apply/applySkirt/applyPants에 currentIdx 저장 + marker 호출 |
| L6829 CardFeed.pickVariant | 진입 hook (panel 표시 후 marker 갱신) |

**검증 (preview DOM 실측):**

| 항목 | 결과 |
|---|---|
| 96 case sweep (16 preset × 6 sleeve length) | NaN 0 / Exception 0 ✅ |
| crewTee 회귀 | halfBody 55, shoulderW 46 (S1 baseline 동일) ✅ |
| sweatshirt 회귀 | halfBody 60.20, shoulderW 59.17, sfdCuffHalf 5.19 ✅ |
| 16 preset dft 정확성 | sleeveLen 100% 일치 ✅ |
| 사용자 토글 변경 → dot 즉시 갱신 | CSS .on.dft 자동 처리 ✅ |
| Reset 버튼 동작 | preset default 복원 (active + dft 일치) ✅ |
| 시각 검증 | Standard 옆 dot, Short(Regular) 옆 dot, Active엔 dot 없음 ✅ |
| Console errors | 0 ✅ |

**시각 디테일 (이람 검수 영역):** 회색 `#bbb` 5px dot, 우상단 (top:3px,right:5px). 변경 원하면 명시.

**🔥 후속 보강 TODO (이람 강조 — "잊지 말고"):**

1. **collar 22종 (`data-neck="B"`) dft 미적용** — neckFinish='collar' 등은 별도 토글 시스템 (data-p 아님). dft 마커 미적용. 후속 spec 필요.
2. **opening 12종 (`data-neck="C"`) dft 미적용** — pullover/full_button/half_placket 등 동일 이슈.
3. **CARD_DATA 진입 시 currentPresetIdx 매핑 부정확** — 5장 카드 모두 idx=0 매핑. panel에서 preset 클릭 후엔 정확. 첫 진입만 minor.
4. **라벨 격상** — Phase 3B (factory validation 5월) 검증 후 "Default" → "Recommended" 격상 가능 (실무 표준 정합 확인 시).
5. **슬라이더 Default indicator** — 현재 토글만. 슬라이더는 S5 (Revert per-input)에서 individual revert 버튼으로 처리.

**원칙 self-check (이람 요청 — 매번 명시):**
- ✅ 원칙 4 (과대평가 금지) — "Default/기본값" 톤 채택
- ✅ 원칙 6 (검증 산출물) — 96 case sweep + DOM 실측 + 시각 검수
- ✅ 원칙 9 (반복 피드백 = 아키텍처) — 신규 추가, magic number 조정 X
- ✅ 원칙 11 (자율, 떠넘기기 금지) — 데이터 위치 자율 (PresetModule.DB 활용) + 1차안 시각 디테일
- ✅ 원칙 14 (매력도 vs 정확도) — UI 매력도 작업 (Phase 3A), 실무 정확도와 분리
- ✅ 원칙 15 (비약 금지) — 시스템(메타데이터) vs 인스턴스(시각 디테일) 분리, 후속 보강 명시
- ✅ Q2 흡수 — sixatomic ⓡ 패턴 흡수 + FLAT 기존 자산 활용 (재창조)

**push:** commit 대기 — message: `S2: Default marker (dot) + Reset button — PresetModule.DB 활용`

**다음:** spec sheet Section 0 작업 순서대로 → **S5 (Revert per-input)** 추천 (S2 데이터 활용 자연스러움). 이람 priority 결정 대기.

---

### 🟢 cont.69 — S1 완료 (2026-04-28, commit 대기)

**작업:** sixatomic 흡수 첫 spec. sleeve length를 % of side arm length 모델로 흡수. FLAT 6 라벨 유지 + 보편명 괄호 병기 + women+men 매트릭스 적재 + Men's default.

**최종 결정 묶음 (이람 OK 후):** P1=A+괄호 / P2=A(53cm) / P3=A(양방향 동기화 보존) / P4=A'(women+men, default Men's) / P5=B(슬라이더값 유지, 회귀 0) / P6=A(ratios.json 자율).

**구현 (파일 2개):**

**1. `data/rules/sleeve_length_ratios.json` 신설** (`data/rules/` 폴더 신설)
- women+men 매트릭스 (7 ratio each)
- labelMap (FLAT 라벨 → sixatomic 키)
- garmentDefault (T-shirt=regular / shirt=wrist)
- displayLabels (EN/KO)
- regressionAnchors (회귀 정합성 명시)
- futureWork (gender 토글 + S11 + P5=A 전환 등)

**2. `flat-v6.html`:**
- L369 HTML 토글 버튼 텍스트 직접 update
- L560 EN sleeve / L709 EN specLabels.sleeveLen / L776 KO sleeve — 괄호 병기
- L1387 SLEEVELEN_PRESETS 위 ratio const 블록 (SIDE_ARM_LENGTH_DEFAULT, SLEEVE_LENGTH_RATIOS, LABEL_MAP, DEFAULT_GENDER='men', GARMENT_DEFAULT, sleeveLenRatioToCm())
- **SLEEVELEN_PRESETS 데이터 그대로** (P5=B 회귀 0)

**검증 (preview DOM 실측, 원칙 6):**

| 항목 | 결과 |
|---|---|
| 96 case sweep (16 preset × 6 sleeve length) | NaN 0 / undefined 0 / Exception 0 ✅ |
| crewTee 회귀 | halfBody 55, shoulderW 46 (cont.68 baseline 동일) ✅ |
| sweatshirt 회귀 | halfBody 60.20, shoulderW 59.17, sfdCuffHalf 5.19, cuffWidth 10.38 (Part 2 baseline 동일) ✅ |
| Console errors | 0 ✅ |
| 토글 버튼 EN/KO DOM 시각 | 6개 모두 괄호 병기 표시 ✅ |
| SPEC SUMMARY | `Set-in · Short (Regular) (32)` ✅ |
| Ratio 계산 검증 | Men's Regular 0.385×53=20.4cm / Women's Wrist 1.000×53=53cm ✅ |

**회귀 정합성 핵심 발견:** Men's Regular(0.385) × 53 = 20.4cm ≈ 현 short slider 30 × 0.69 = 20.7cm (−0.3cm). defaultGender='men' + P5=B 조합이 가장 깔끔.

**이람 검수 결과 (2026-04-28):**
- ✅ "슬라이더+토글 양방향 좋아" — P3=A 채택 긍정 확인
- ⚠️ "캡, 반소매, 5부, 7부 소맷단 어색" → S1 회귀 0 확인 (SleeveComp.draw 변경 X). cont.65-67 sweep audit 기존 상태 그대로. **Phase 4 (옵션 H 확장 + 3D 연동) 일괄 재구성 합의 그대로.** 부분 hack 거부 (원칙 9 cont.63 자의적 90° 블렌딩 사고 재발 방지).
- ✅ "A로 OK" — Step 6/7 진행 합의

**원칙 11 자율 판단:**
- 데이터 위치: `data/rules/` 신설 폴더로 분리 (data/는 이미 6개 JSON 분리, 동일 패턴)
- HTML L369 toggle 버튼 텍스트 직접 update: applyLang() 자동 호출 안 되는 초기 로드 시점 갭 해결
- L1951 슬라이더 라벨 함수 변경 0: P3 양방향 동기화 보존

**Women's TODO (보존, 별도 작업 필요):**
- gender 토글 도입 시 `SLEEVE_LENGTH_DEFAULT_GENDER` 동적 전환 → women's matrix 활성화
- ratios.json `futureWork[0]` 명시
- 양쪽 공유 TODO 표에 추가됨

**Phase 4 DEFER (이람 합의 그대로):**
- cap/short/elbow/threequarter cuff 형태 정밀화
- SleeveComp cap/곡선 모양 개선
- 다른 preset 옵션 H 확장 (crewTee/hoodie/polo/shirt/blazer 등)
- 칼라 22종 재감사

**push:** commit 대기 — message: `S1: sleeve length ratio model (Men's default + Women's data)`

**다음:** spec sheet Section 0 작업 순서대로 → **S2/S3 묶음 (Recommended 배지 + 노란 highlight)** 또는 Phase 3A UX/UI 1순위 결정. 이람 priority 결정 대기.

---

### 🟡 cont.69 — S1 Step 3 재검 (이람 피드백 3건 반영, 2026-04-28)

**이람 피드백 (1차 보고 후):**
1. *"투자자들이 거의 남자일 텐데."* → Men's matrix 적용 필요
2. *"셔츠에서는 쓰는 라벨 네임이 다르니까 괄호 등으로 구분 필요"* → 라벨 표시 보강
3. *"슬라이더와 토글 조정의 장점은 없애지 않는 방식으로"* → P3 양방향 동기화 보존 명시

**재검 결과 — 변경 사항 3건:**

**[변경 1] P4 → A'** (women's만 → women+men 둘 다 적재, default = Men's)

회귀 정합성 분석 (53cm 기준):

| 라벨 | Women's | Men's | 현 FLAT preset (slider × 0.69) | Men's와의 갭 |
|---|---|---|---|---|
| cap | 14.1cm | 15.4cm | 10.4cm (slider 15) | +5.0cm |
| short | 18.7cm | **20.4cm** | **20.7cm** (slider 30) | **−0.3cm ★ 거의 일치** |
| elbow | 23.7cm | 25.7cm | 34.5cm (slider 50) | −8.8cm |
| threequarter | 38.3cm | 41.3cm | 49.7cm (slider 72) | −8.4cm |
| long | 53.0cm | 53.0cm | 65.6cm (slider 95) | −12.6cm |

**Men's Regular(0.385) × 53 = 20.4cm ≈ 현 short slider 30 = 20.7cm** — 회귀 0에 가장 깔끔. P5=B 채택 시 라벨 의미 변경에도 사용자 체감 변경 0.

**Long/Wrist는 양 gender 동일 (1.000)** — gender 불문 53cm. 셔츠 default가 sixatomic 명시 Wrist이므로, 현 FLAT shirt preset slider 95 (= 65.6cm) 가 spec보다 12.6cm 길다 — P5=B 채택해서 슬라이더값 유지하면 시각 회귀 0, ratio 의미만 라벨에 적용. 향후 P5=A로 전환 시 별도 spec 권장.

데이터 schema 업데이트:
```json
{
  "sideArmLengthDefault": 53,
  "defaultGender": "men",       ← 재검 변경
  "ratios": {
    "women": { ... },
    "men":   { ... }            ← 데이터로 적재
  },
  "labelMap": { ... },
  "garmentDefault": { ... }
}
```

**[변경 2] P1 보강 — 라벨 표시에 sixatomic 보편명 괄호 병기**

i18n에 양 명칭 표시:
- EN: `Cap (Very Short)` / `Short (Regular)` / `Elbow (Above Elbow)` / `3/4 (Forearm)` / `Long (Wrist)`
- KO: `반팔 (Regular)` / `긴팔 (Wrist)` 등 — sixatomic 명칭 한글화 미정 → 영어 그대로 노출하는 게 깔끔 (이람 패션 업계 영어 친숙도)
- 또는 **EN 한 단어 대표 + 괄호로 sixatomic** 형식으로 통일: `반팔 (Short / Regular)`, `긴팔 (Long / Wrist)` 등

**셔츠-T-shirt 라벨 차이 처리:** S1에서는 universal 표시만 채택 (괄호 병기). garment-specific 별칭 (예: 셔츠 = "Long Sleeve · Barrel cuff 표준") 은 future S2 (Recommended 배지) + S4 (카피 표준) spec 도입 시 메타카피로 분리 — S1 범위 밖.

**적용 위치 (flat-v6.html):**
- L709 i18n EN `sleeveLen:{...}` — 각 항목 끝에 ` (sixatomic名)` 추가
- L922 부근 i18n KO 동일
- L1951 SD 슬라이더 라벨 함수도 같은 i18n 사용 (변경 자동 반영)
- HTML L369 토글 버튼은 `data-i18n` 키로 자동 갱신

**[변경 3] P3 양방향 동기화 보존 — 변경 0 명시**

현재 동작 그대로 유지:
- **토글 클릭** → `SLEEVELEN_PRESETS[key].sleeveLength` → `S.sleeveLength` set → 슬라이더 갱신 + L1951 라벨 함수 자동 갱신
- **슬라이더 입력** → L2059 listener → `S.sleeveLength` set → L1951 라벨 함수 자동 갱신 (현 라벨 자동 활성화)

ratio 모델은 **SLEEVELEN_PRESETS 값 결정**에만 사용 (P5=B → 현 슬라이더값 그대로 유지). 슬라이더+토글 인터랙션 자체는 변경 0. 사용자가 슬라이더로 fine-tune해서 22.5cm가 되면 라벨은 여전히 "Short (Regular)" 으로 자동 활성화 (L1951 `<42 → short` 규칙 그대로).

---

**최종 결정 묶음 (재검 후, 이람 OK 대기):**

| P# | 항목 | 옵션 | 변경 |
|---|---|---|---|
| P1 | 라벨 매핑 | A + 괄호 병기 | 라벨 표시 보강 |
| P2 | Side arm length | A (53cm 고정) | — |
| P3 | 슬라이더 동작 | A (양방향 동기화 보존) | 변경 0 명시 |
| **P4** | **Gender** | **A' (women+men 둘 다, default Men's)** | ★ Men's로 |
| P5 | Garment default | B (슬라이더값 유지) | — |
| P6 | 데이터 위치 (자율) | A (sleeve_length_ratios.json) | — |

**이람 응답 형식:** "OK" 또는 추가 수정.

---

### 🟡 cont.69 — S1 Step 3 (현재 로직 보고 + 결정 포인트, 2026-04-28, 1차 — 재검됨)

**상태:** Step 3 `flat-v6.html` SleeveComp 현재 로직 read 완료. **이람 OK 게이트 대기**. spec sheet 초입 "모든 spec은 이람 OK 전엔 보류. 자율 시작 금지" 준수.

**1. 현재 FLAT sleeve length 모델 (read 결과)**

| 위치 | 내용 |
|---|---|
| L1387 `SLEEVELEN_PRESETS` | sleeveless 0 / cap 15 / short 30 / elbow 50 / threequarter 72 / long 95 |
| L1974 `CM_MAP` | `cm = sliderVal × 0.69` → slider 100 = 69cm |
| L1951 슬라이더 라벨 | `<=2 sleeveless / <=18 cap / <42 short / <62 elbow / <82 threequarter / else long` |
| L370 슬라이더 UI | range 0~100, EXT 모드 시 0~160 |
| L2113 `SFD_POM.sweatshirt.M.sleeveLength` | 63cm (HPS→cuff) — **현재 데이터로만 존재, draw에서 미사용** (Part 2는 sleeveOpening만 SFD override) |
| L2912~2929 `SleeveComp.draw()` | `rawSl = S.sleeveLength` → `slLen = rawSl × slScale (1.0~1.9 보간)` → SVG 좌표 |
| Default per preset | crewTee/polo/sweater = `short`(30) / shirt/sweatshirt/sweater/cardigan = `long`(95) |

**2. sixatomic spec과의 갭**

| | sixatomic | FLAT |
|---|---|---|
| 라벨 수 | 7 (Cap·VeryShort·Short·Regular·AboveElbow·Forearm·Wrist·Full) | 6 (sleeveless·cap·short·elbow·threequarter·long) |
| 길이 모델 | side arm length × ratio | 슬라이더 0~100 직접 cm 매핑 |
| Body profile | KS K 0051 / Sixatomic 5 default profile → 자동 arm length | **없음** (S11 도입 예정) |
| Gender | Women's / Men's 별도 매핑 | **없음** (현재 통합) |
| Default per garment | T-shirt = Regular / Shirt = Wrist / 기타 미확인 | 위 표 |

**3. 결정 포인트 (이람 OK 필요)**

> 표기: ⭐ = 코드탭 추천. 이람이 다른 옵션 명시하지 않으면 추천 채택.

**P1. 라벨 매핑** — sixatomic 7 vs FLAT 6
- ⭐ **A. 1:1 흡수 (FLAT 6 라벨 유지):** cap→Cap or VeryShort, short→Short, elbow→AboveElbow, threequarter→Forearm, long→Wrist. VeryShort/Full은 슬라이더 직접 입력으로 표현. 라벨 변경 0, ratio 표 적용 가장 깔끔.
- B. FLAT 라벨 7개로 확장 (elbow → AboveElbow / threequarter → Forearm 분리). 토글 UI 1개 추가 + i18n 보강 필요.
- C. 라벨 유지 + ratio만 적용 (cap=0.266 등). 라벨 의미가 sixatomic과 미스매치 (cap=0.266은 sixatomic VeryShort) — 혼란.

**P2. Side arm length 정의** — Body profile 없는 현 단계
- ⭐ **A. 고정 reference 53cm:** const `SIDE_ARM_LENGTH_DEFAULT = 53` (KS K 0051 신장 165 여성 어깨~손목 표준). S11 (Body profile system) 도입 후 dynamic으로 전환 예정.
- B. Chest 등에서 파생 (예: armLen ≈ chest × 0.6). 단순하지만 부정확.
- C. 새 슬라이더 "Arm Length" 도입. S11 의존성 발생 → DEFER 권장.

**P3. Slider 동작 변경?**
- ⭐ **A. 슬라이더는 현 그대로 cm 직접 입력**, 라벨 토글 클릭 시 `Math.round(ratio × armLen / 0.69)`로 슬라이더 set. 라벨=ratio 모델, 슬라이더=fine-tune. 후방 호환 + 사용자 직관 유지.
- B. 슬라이더 자체를 ratio 0~1.075로 변환. 큰 리팩터링, CM_MAP/SD/EXT_RANGES 모두 영향.

**P4. Gender 매핑** — Men's ratio
- ⭐ **A. Women's만 first pass.** Men's matrix를 데이터로 보존하되 적용 보류 (gender 토글 도입 시 자동 활성화). FLAT 현재 gender 토글 X.
- B. Gender 토글 신규 도입. **별도 spec으로 분리 권장** (S1 범위 밖).

**P5. Garment별 default**
- A. sixatomic 명시값 직접 적용 (T-shirt=Regular=22.9cm, Shirt=Wrist=53cm). 현 default와 약간 차이 (T-shirt 21cm→22.9cm, Shirt 65.55cm→53cm). **shirt에서 13cm 짧아짐 = 회귀 위험 ↑**
- ⭐ **B. 현 SLEEVELEN_PRESETS 슬라이더 값 유지, 의미만 ratio 모델로 환산.** sleeveLength=30(short) ↔ ratio≈0.40 (53cm 기준). 회귀 0, sixatomic 흡수는 "라벨→ratio" 매핑 작업으로만.
- C. B 시작 → 추후 garment별 이람 결정 (per-preset).

**4. 코드탭 자율 판단 영역 (원칙 11)**

**P6. 데이터 위치**
- ⭐ **A. 신규 `data/rules/sleeve_length_ratios.json`** (women/men ratio matrix + garmentDefault 메타). data/는 이미 6개 JSON 분리됨, 동일 패턴.
- B. flat-v6.html 안 const 추가. 단일 파일 원칙 유지하지만 데이터/로직 결합.

**5. 매몰 비용 / 회귀 시뮬레이션**

P5=B 채택 시:
- 현 SLEEVELEN_PRESETS 6개 슬라이더 값 **그대로 보존** (의미만 변경)
- cont.68 Part 2 sweatshirt cuffWidth 10.54px **회귀 0** (cuffHalfW 분기는 SFD `g.sfdCuffHalf` 사용, sleeveLength state와 독립)
- crewTee halfBody 55, shoulderW 46 **회귀 0** (BodyComp.geometry는 sleeveLength 무관)
- 16 preset NaN/undefined 0 유지 가능

**6. 추천 묶음 채택 시 작업 흐름** (P1=A, P2=A, P3=A, P4=A, P5=B, P6=A)

```
1. data/rules/sleeve_length_ratios.json 신설:
   {
     "sideArmLengthDefault": 53,
     "ratios": {
       "women": { "veryShort": 0.266, "short": 0.310, "regular": 0.353,
                  "aboveElbow": 0.447, "forearm": 0.723, "wrist": 1.000, "full": 1.075 },
       "men":   { "veryShort": 0.290, "short": 0.335, "regular": 0.385,
                  "aboveElbow": 0.485, "forearm": 0.780, "wrist": 1.000, "full": 1.075 }
     },
     "labelMap": { "cap":"veryShort", "short":"regular",
                   "elbow":"aboveElbow", "threequarter":"forearm", "long":"wrist" },
     "garmentDefault": { "tshirt":"regular", "shirt":"wrist" }
   }
2. flat-v6.html:
   - SLEEVELEN_PRESETS 데이터 그대로 유지 (P5=B)
   - 라벨 토글 클릭 시 ratio×armLen 기반으로 슬라이더 set 함수 추가
     (단, 현 PRESET 값과 일치하는 fallback 유지 → 회귀 0)
   - sixatomic ratio matrix는 future S6/S11에서 활용
3. 검증:
   - 16 preset × 5 sleeve length 토글 = 80 case sweep
   - NaN/undefined/Exception 0
   - sweatshirt cuffWidth 10.54px / crewTee halfBody 55 회귀 baseline 유지
```

**7. 이람 응답 형식 (간결화)**

다음 중 하나로:
- "추천 묶음 OK" (P1=A·P2=A·P3=A·P4=A·P5=B·P6=A 다 채택)
- 또는 "P? = X" 형식으로 다른 옵션 선택 (예: "P5=A로, 정확도 우선")

**8. self-check (cont.68 RCA 규칙 1·6 + 원칙 15·16·17)**

- ✅ 시스템(Sixatomic 학습) vs 인스턴스(FLAT 적용) 분리 — S1만 적용, 다른 spec 안 끌어옴
- ✅ 기존 자산 read — flat-v6.html SleeveComp + SLEEVELEN_PRESETS + CM_MAP + SFD_POM read
- ✅ 이람 응답 범위 안 — "S1 implement 착수, 7단계" 그대로
- ✅ 좋아보이는 것 vs 좋은 것 — implement 바로 안 함, Step 3 게이트 준수
- ✅ 환경 명시 — Claude Code (코드탭, Mac)
- ✅ HANDOFF 백업 + 섹션 단위 수정 — `docs/archive/HANDOFF-20260428-cont69-S1-step3-backup.md`
- ✅ 자율 시작 금지 — Step 4 이람 OK 게이트 대기 명시
- ✅ A/B/C 떠넘기기 금지 (원칙 11/15) — 결정 포인트마다 trade-off + 추천(⭐) 명시

---

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
| **콘텐츠 자동화 라인** | 분리 완료 → `docs/content_handoff.md` | 자율 진행 OK | flat HANDOFF에서 제거됨 |
| **원칙 15 등록 + 사고 RCA + 인벤토리** | ✅ cont.68 Step 0a | — | 완료 |
| **원칙 16 등록 + cont.68 사고 2-4 RCA + cont.69 사고 RCA** | ✅ cont.69 Group 1 | — | 완료 |
| **세션 SOP + 환경 매트릭스 + 탭 인계 양식 + 자가검증 양식 (인프라)** | ✅ cont.69 Group 2 | — | 완료 (4/4 + 규칙 3 보강) |
| → 환경 매트릭스 v1.0 (`docs/flat_env_matrix.md`) | ✅ cont.69 Group 2 (1/4) | — | 완료 |
| → 자가검증 양식 v1.0 (`docs/flat_self_check_template.md`) | ✅ cont.69 Group 2 (2/4) | — | 완료 |
| → 탭 인계 양식 v1.0 (`docs/flat_tab_handoff_template.md`) | ✅ cont.69 Group 2 (3/4) | — | 완료 |
| → 세션 시작 SOP v1.0 (`docs/flat_session_sop.md`) | ✅ cont.69 Group 2 (4/4) | — | 완료 |
| **원칙 17 등록 + 외부 채팅 입장 절차 + 규칙 9 + 사고 (n)(o)(p)(q)(r)(s) RCA 통합** | ✅ cont.69 Group 1.5 | — | 완료 |
| **사고 (t) 통합 (사고 h 본문 한 줄 추가)** | ✅ Group 2 첫 작업 | — | 완료 |
| IR v4.3 비주얼 검수 | 📝 이람 | — | 대기 |
| YC 지원서 숫자 반영 | 📝 이람 | — | 5/4 전 |
| 1분 데모 영상 | Phase 3A 1순위 후 | 캡처 | 5/3-4 |
| 디자이너 인터뷰 3명 | 📝 이람 | — | 5월 전 |
| factory validation | 성수동 섭외 (Phase 3B) | 검증 output | 5월 |
| **🟣 Sixatomic v2 audit + spec sheet (cowork tab)** | 산출물 read + Section 17 priority 결정 | 결정 후 spec ID 단위 implement | 2026-04-27 완료, 이람 의사결정 완료 |
| **다음 cowork 세션 의제 — 미확인 7개** | M1~M7 채록 추가 | — | spec sheet Section 2 참조 |
| **S1 (Sleeve length ratio model)** | spec 결정 OK + 검수 OK | ✅ 구현 + 검증 96 case 통과 | 완료 (cont.69, commit 471caa4) |
| **S1 후속 — Women's matrix 활성화** | gender 토글 도입 spec 필요 | DEFAULT_GENDER 동적 전환 | TODO (별도 spec, 이람 잊지 말기 강조) |
| **S2 (Default 마커 + Reset 버튼)** | A 옵션 OK + 검수 OK + 후속 보강 메모 강조 | ✅ 구현 + 검증 96 case 통과 | 완료 (cont.69 Part 2, commit 대기) |
| **S2 후속 — collar 22종 (data-neck="B") dft 미적용** | spec 필요 | 별도 메커니즘 토글 처리 | TODO (이람 잊지 말기 강조) |
| **S2 후속 — opening 12종 (data-neck="C") dft 미적용** | spec 필요 | 동일 메커니즘 보강 | TODO |
| **S2 후속 — CARD_DATA 진입 시 currentPresetIdx 매핑** | spec 필요 | CARD_DATA에 presetIdx 명시 | TODO (minor) |
| **S2 후속 — 라벨 격상 "Default" → "Recommended"** | Phase 3B validation 후 | i18n update | TODO (Phase 3B 후) |
| **S2 후속 — 슬라이더 Default indicator** | S5 spec 안 통합 | individual revert 버튼 | S5에서 처리 |
| **S5 (Revert per-input) 또는 S6 (Custom 카드)** | priority 결정 대기 | spec read 후 implement | 다음 spec 후보 |
| **S1 후속 — cap/short/elbow/threequarter cuff 정밀화** | Phase 4 합의 | 옵션 H 확장 + 3D 연동 시점 | DEFER (Phase 4) |

---

## 🟢 cont.67 최종 완료 로그 (Part 1 + 2 + 3 완전 마무리)

| 항목 | 상태 |
|---|---|
| sweep_matrix.py + 96 baseline | ✅ |
| 이람 검수 (48/48 미달) | ✅ |
| 원칙 9/10/11/12/13/14 등록 | ✅ |
| 옵션 H 방향 + Part 1 구현 | ✅ b7b3b46 |
| **옵션 H Part 2 축소판 (SleeveComp sleeveOpening)** | ✅ 71b7400 |
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

## 📂 파일 구조 (cont.68 Step 0a 완료)

```
/Users/yiram/Claude/flat/
├── HANDOFF.md          ← cont.68 Step 0a 완료 (이 파일, 원칙 15 + 인벤토리 + 콘텐츠 분리)
├── plan.md              ← Phase 2 축소 + 3A UX/UI 신규 + 3B factory + 4 3D+옵션 H 통합
├── progress.md          ← 코드탭 알림 추가 (콘텐츠 라인 분리)
├── CLAUDE.md
├── flat-v6.html         ← cont.68 Part 1 (b7b3b46) + Part 2 축소판 (71b7400)
├── data/                 ← 6개 JSON (rules/presets/params/fabrics/neck_system + README) — 이전은 4개로 인지되었음
├── docs/
│   ├── reference_data.md                              ← §6.2/6.3/6.4 (Phase 4 canonical)
│   ├── flat_design_philosophy_v1.0/1.1/1.2.md         ← 원칙 + 대화 UX 신규 섹션
│   ├── flat_ux_architecture_v1.md                     ← 넓 3축 + 카드피드 + 5-zone
│   ├── flat_sweatshirt_pom_proposal.md                ★
│   ├── flat_crewTee_pom_proposal.md                   ★
│   ├── flat_hoodie_pom_proposal.md                    ★
│   ├── flat_preset_expansion_workflow.md              ★ (Phase 4 활용, 지금 보류)
│   ├── flat_code_tab_cont68_option_h_sweatshirt.md    ★ (Part 2 축소판으로 해석)
│   ├── flat_phase_review_2026-04-20.md
│   ├── audit_cont65_sweep.md
│   ├── cont68_review_inventory.md                     ★ cont.68 Step 0a 신규 (전체 파일 인벤토리)
│   ├── content_handoff.md                             ★ cont.68 Step 0a 신규 (콘텐츠 라인 분리)
│   ├── sixatomic_pattern_generate_audit.md            ★ 2026-04-27 cowork tab 신규 (v1+v2+재검, Section 1-22)
│   ├── sixatomic_implementation_specs.md              ★ 2026-04-27 cowork tab 신규 (코드탭용 atomic spec S1-S13)
│   ├── [기타 확정 md 17종]
│   ├── archive/
│   │   ├── cont68_rca_2026-04-22.md                   ★ cont.68 Step 0a 신규 (사고 RCA)
│   │   ├── flat_demo_video_60s_v0.1_PREMATURE.md      ★ cont.68 사고 산물 (archive 됨)
│   │   ├── HANDOFF-20260422-cont68-step0a-backup.md   ★ cont.68 Step 0a 신규 (백업 stub)
│   │   ├── HANDOFF-20260427-cowork-sixatomic-v2-backup.md  ★ 2026-04-27 cowork tab 신규 (sixatomic v2 작업 전 32KB 백업)
│   │   └── [10개 HANDOFF 백업 + 4개 category 이전 + 기타]
│   └── deliverables/
├── .claude/commands/                                 ← 5개 slash command (content-review/ref-check/preset-check/preview-test/save-progress)
├── trends/
│   └── daily_report.md                               ← 콘텐츠 라인 일일 수집 (코드탭 자율)
└── tools/
    ├── preset_research.html              v1.1 (Phase 4 활용)
    └── audit/
        ├── inspect_flat.py / gallery.html
        └── (⚠️ sweep_matrix.py + sweep/prod/*.png 실제 부재 — 이전 HANDOFF 표기 잘못. cont.68 Part 2 검수 시 재작성 필요)

/mnt/user-data/outputs/
└── flat_sweep_bundle.zip                 ← cont.67 (96장 PNG)
```

**파일 시스템 불일치 3건 정정 (cont.68 Step 0a 인벤토리 발견):**
1. `tools/audit/sweep_matrix.py` 실제 부재 — cont.67 sweep은 `/mnt/user-data/outputs/`에서만 실행, 로컬 미저장
2. `tools/audit/sweep/prod/*.png` 실제 부재 — zip 안에만 존재. cont.68 Part 2 검수 시 zip 풀어서 사용
3. `data/neck_system.json` (7.97KB) 존재 — memory에는 4개로 인지되어 있었음. data/ 폴더에 6개 파일 실제 존재.

---

## 📏 규칙

1. 기획탭 → `docs/` + HANDOFF "기획→코드"
2. 코드탭 → `progress.md` + HANDOFF "코드→기획"
3. 세션 시작 → **SOP 호출 (`docs/flat_session_sop.md`)**. SOP 단계 4에서 HANDOFF.md read. 외부 채팅 = SOP § 4 환경별 분기 적용 (원칙 17)
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
15. **비약 금지. 완전성 우선. 짧은 답 ≠ 진행 허가. 역할 분담. 좋아보이는 것·좋은 것 구분. 확장 self-check 9-16개 응답 명시 공개. RCA: docs/archive/cont68_rca_2026-04-22.md + cont68_principle_rca_2026-04-23.md (원칙 15)**
16. **환경 인식 + 검증 사이클. capability 선언 전 환경 명시 + tool_search + 실제 호출 검증 + fallback. 추측 평서문 금지. self-check D 항목 4개. RCA: docs/archive/cont69_env_rca_2026-04-23.md (원칙 16)**
17. **환경 정합성 (설계 시점). 절차/시스템 작성 시 작동 환경 목록화 + 타 환경 적용 가능성 검증 + 차선 절차 명문화. 외부 채팅 입장 절차 = 구체 적용 사례. RCA: docs/archive/cont69_env_rca_2026-04-23.md 사고 (o) (원칙 17)**
