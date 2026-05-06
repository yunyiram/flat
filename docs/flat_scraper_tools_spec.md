# FLAT Scraper Tools Spec (자율도 향상 — B 라인)

> **목적:** 코드탭 자율도 향상을 위한 스크롤링/스크래핑/자료 검색 자동화 도구.
> **이람 cont.72 제안:** *"자율도를 높일 스크롤링, 스크래핑, 자료 찾는 프로그램을 flat 용도로 하나 만들까?"*
> **버전:** v0.1 — 2026-05-06 cont.72 Part 8 자율 신설 (이람 OK 후 implement)
> **연관:** 콘텐츠 자동화 라인 (`docs/content_handoff.md`) 별도 워크스트림 / 본 spec은 코드탭 도구 영역

---

## 0. 솔직 우선순위 검토

### 0.1 이미 보유한 도구 (활용 미흡 영역)

| 도구 | 활용 |
|---|---|
| `mcp__Claude_in_Chrome__*` | sixatomic v2 audit (cont.69 cowork tab) — **자동화 X, 매번 수동** |
| `mcp__plugin_chrome-devtools-mcp__*` | 미활용 |
| `mcp__Claude_Preview__*` | 자체 검증 — ✅ cont.69-72 활용 중 |
| `WebFetch` / `WebSearch` | 매 세션 수동 검색 |
| `tools/audit/inspect_flat.py` | 부분 작성 (cont.65 audit 시 사용) |
| Bash + python3 | 메모리 read / 파일 검증 (cont.72 Part 8 한국어 깨짐 검증 등) |

### 0.2 자동화 가치 영역 (반복 작업)

| 작업 | 빈도 | 자동화 가치 |
|---|---|---|
| sixatomic 사이트 라이브 audit | 매 cowork 세션 | ★★★ (Section 13/14/16 정밀 채록 의무) |
| 5 AI techpack 사이트 모니터링 | 주 1회+ | ★★ (경쟁 신기능 추적) |
| 패턴 도서 (Donnanno/Armstrong/Abling) 데이터 추출 | Phase 4 진입 시 | ★★★ (옵션 H 확장 시) |
| 봉제 현장용어 사이트 모니터 | 분기 | ★ (60 용어 보유, 추가 발굴 명분 적음) |
| 자체 preview 자동 sweep + 캡처 | 매 commit 후 | ★★ (회귀 시각 검증) |
| 책 스캔본 OCR | 1회성 | ★★ (메모리 인덱스 자동화) |

### 0.3 새 도구 신설 vs 기존 활용

**솔직 결론:** 이미 보유한 MCP/preview/Bash 도구로 80% 커버 가능. **새 도구 신설보다 wrapper 스크립트 + 활용 표준화**가 효율.

**권장 우선순위:**
1. **`tools/audit/auto_sweep.py`** ★★★ — preview 자동 sweep + 캡처 (cont.65 sweep 도구 부재 정정)
2. **`tools/scraper/sixatomic_audit.py`** ★★ — Chrome MCP wrapper로 라이브 audit 자동화
3. **`tools/scraper/competitor_monitor.py`** ★ — 5 사이트 주간 변경 감지
4. **`tools/scraper/book_ocr.py`** ★★ — Phase 4 진입 시 (현재 우선순위 ↓)

---

## 1. 디렉터리 구조

```
tools/
├─ audit/                      # 기존 (cont.65~)
│  ├─ inspect_flat.py          # ✅ 부분 작성 (cont.65)
│  ├─ gallery.html             # ✅ cont.67
│  ├─ auto_sweep.py            # ❌ 신설 권장 ★ (cont.65 sweep_matrix.py 정정)
│  └─ copy_check.py            # ❌ S4 후속 (copy_guide.md § 3 참조)
└─ scraper/                    # 신설 폴더
   ├─ sixatomic_audit.py       # Chrome MCP wrapper, cowork tab 자동화
   ├─ competitor_monitor.py    # 5 AI techpack 사이트 변경 감지
   ├─ book_ocr.py              # 패턴 도서 OCR (Phase 4)
   └─ factory_terms_sync.py    # 봉제 현장용어 사이트 모니터
```

---

## 2. 핵심 도구 spec

### 2.1 tools/audit/auto_sweep.py ★★★

**목적:** preview에서 모든 garment × sleeve length × collar 자동 sweep + PNG 캡처. cont.65 sweep_matrix.py 부재 정정.

**입력:**
- `garment`: 'top'/'skirt'/'pants'/'dress'/'outerwear' 또는 'all'
- `axis`: 'sleeveLength' / 'collar' / 'shoulderType' 등 sweep 차원
- `outDir`: PNG 저장 경로

**출력:**
- `tools/audit/sweep/{date}/{cat}_{preset}_{axis}_{value}.png` (각 case PNG)
- `tools/audit/sweep/{date}/index.html` (gallery)

**자동 검증:**
- NaN/undefined/Exception 0
- console errors 0
- DOM SVG path validation

**구현:** Python + Claude Preview MCP wrapper (또는 Playwright)

**작업량:** 1세션

### 2.2 tools/scraper/sixatomic_audit.py ★★

**목적:** sixatomic Pattern Generator 자동 audit. Section 13 (28 부위 시접) / Section 14 (이중 측정) 정밀 채록.

**입력:**
- `category`: 'tshirt'/'shirt'/'polo' 등
- `gender`: 'women'/'men'

**출력:**
- `docs/sixatomic_{cat}_{gender}_{date}.md` 자동 생성
- 모든 wizard step (Style/Design/Materials/Seams/Sizes/Notes) 채록

**구현:** Chrome MCP `find` + `read_page` + `click` 시퀀스 + 텍스트 추출

**작업량:** 2-3세션 (정밀 selector 매핑 필요)

### 2.3 tools/scraper/competitor_monitor.py ★

**목적:** 5 AI techpack 사이트 (Tier 0-4 + Fabra/Raspberry) 주간 변경 감지.

**입력:** `data/competitor_sites.json` (URL 리스트)

**출력:**
- `tools/scraper/snapshots/{date}/{site}.html` (HTML 스냅샷)
- `tools/scraper/diff_{date}.md` (이전 대비 변경 요약)

**구현:** WebFetch + diff + 변경 키워드 추출

**작업량:** 2세션

### 2.4 tools/scraper/book_ocr.py ★★ (Phase 4)

**목적:** 책 스캔본/ 폴더 PDF/이미지 OCR + 메모리 인덱싱.

**입력:** PDF/JPG 파일

**출력:** `메모리 reference_book_{name}.md` 자동 생성 (해당 도서 핵심 내용)

**구현:** Tesseract / Claude Vision

**작업량:** 3세션 (Phase 4 진입 시)

### 2.5 tools/scraper/factory_terms_sync.py ★

**목적:** 봉제 현장용어 사이트 (서울의류협동조합 / hydnstudio) 변경 감지 + 신규 용어 추가.

**입력/출력:** `data/factory_terms.json` (cont.72 Part 8 신설) 갱신

**작업량:** 1세션

---

## 3. implement 우선순위 (이람 OK 후)

| 순위 | 도구 | 가치 | 작업량 | 진행 시점 |
|---|---|---|---|---|
| 1 | tools/audit/auto_sweep.py | ★★★ | 1 | cont.73 또는 다음 자율 batch |
| 2 | tools/scraper/sixatomic_audit.py | ★★ | 2-3 | sixatomic v3 audit 필요 시 |
| 3 | tools/audit/copy_check.py | ★ | 1 | S4 spec 후속 |
| 4 | tools/scraper/competitor_monitor.py | ★ | 2 | Phase 3B factory validation 시 |
| 5 | tools/scraper/book_ocr.py | ★★ | 3 | Phase 4 진입 시 |
| 6 | tools/scraper/factory_terms_sync.py | ★ | 1 | factory_terms.json 갱신 필요 시 |

**총 작업량:** 10-12세션 (모두 implement 시).

---

## 4. 단일 HTML 원칙 정합

**flat-v6.html 단일 HTML 원칙 (CLAUDE.md):** Phase 5 SaaS 전환 전까지 유지. tools/ 폴더 도구는 **외부 도구**라 단일 HTML 원칙과 무관. 신설 OK.

---

## 5. 변경 이력

- **2026-05-06 v0.1**: 코드탭 cont.72 Part 8 자율 신설. 이람 제안 응답. **이람 OK 후 우선순위별 implement**.

---

## 6. 다음 단계

1. **이람**: spec read + 우선순위 확인 / 또는 "1번부터 implement" OK
2. **코드탭**: 우선순위 1 (auto_sweep.py) 부터 implement
3. **Phase별 활용:**
   - cont.73+ 자율 batch: auto_sweep.py + copy_check.py
   - Phase 3B (5월 factory validation): competitor_monitor.py
   - Phase 4 (3D 연동): book_ocr.py
