# tools/audit/ — FLAT 검증 자동화 도구 인덱스

> **cont.72 Part 16 자율 영역 K 신설.** 누적 7 도구, 모두 회귀 0 (read-only).
> **목적:** "검증 없이 완료 판정 금지" (원칙 6) + "시각 검수는 샘플이 아닌 전수 자동" (원칙 10) 구현.

---

## 도구 매트릭스

| 도구 | 검증 영역 | 회귀 | 의존 | cont |
|---|---|---|---|---|
| `sync_check.py` | 7 영역 (preset DB↔JSON / fabric↔JSON / B6.1 sample rules / CARD targetPresetName / seams / factoryTerms / params) | 0 | Python 3 (stdlib only) | cont.72 Part 16 A2/A4/C |
| `compat_sweep.py` | 6 system 27 rule 정적 sweep + COLLAR_COMPAT 8×5 매트릭스 + NECK_BC 9 pair | 0 | Python 3 | cont.72 Part 16 D |
| `style_overlay_sweep.py` | 7 Style Overlay 정의/i18n EN+KO/deltas+overrides 완전성 | 0 | Python 3 | cont.72 Part 16 E |
| `sweep_matrix.py` | sleeve length 5 axes / 96 case JSON (cont.65 부재 정정 1차 minimal) | 0 | Python 3 | cont.72 Part 14 |
| `inspect_flat.py` | DOM 실측 (Playwright 기반, cont.65) | 0 | Playwright | cont.65 |
| `verify_path_seq.py` | path 빌더 sequence 검증 (cascade_pattern.md #2 본체 적용 dynamic verifier) | 0 | Playwright | cont.72 Part 17 |
| `gallery.html` | sweep 결과 시각 검수 갤러리 (이람 검수) | 0 | 브라우저 | cont.67 |

## 실행 패턴

### 1. 전체 정합성 빠른 점검 (회귀 0, 1-2초)

```bash
cd /Users/yiram/Claude/flat
python3 tools/audit/sync_check.py
python3 tools/audit/compat_sweep.py
python3 tools/audit/style_overlay_sweep.py
```

각 도구 종료 코드: 0 = PASS, 1 = FAIL. CI 게이트 가능.

### 2. DOM 실측 (preview 회복 시)

```bash
python3 tools/audit/inspect_flat.py --url 'http://localhost:8000/flat-v6.html?demo'
python3 tools/audit/verify_path_seq.py --axis sleeveLen
python3 tools/audit/verify_path_seq.py --numeric-sweep neckCurve
```

### 3. sweep + 갤러리 (이람 검수)

```bash
python3 tools/audit/sweep_matrix.py
open tools/audit/gallery.html
```

---

## 도구별 baseline (cont.72 Part 16 시점)

### sync_check.py 7 영역

| 영역 | baseline | 검증 |
|---|---|---|
| preset DB ↔ JSON | 34/34 (16 top + 8 skirt + 10 pants) | inline names == JSON names (exact match) |
| fabric ↔ JSON | 41/41 | FabricModule.DB name == JSON name |
| B6.1 sample rules | 6 system / 6 rule | data/rules/ 6 file (cont.72 Part 4 sample lift-and-shift) |
| CARD targetPresetName | 5 카드 모두 명시 | Card 0/1/2 crewTee / 3 hoodie / 4 sweatshirt (cont.72 Part 12 fix) |
| seams (S14 Phase 1) | 7 file / 27 area / tbd 27 | data/seams/ (cont.72 Part 10) |
| factoryTerms (B6.5) | declared 68 / computed 68 / mapping 50 / ko_factory 19 | data/factory_terms.json + ko_factory LANG section |
| params (B6.4) | 20 top keys / state_defaults 62 / inline S 62 정확 일치 | data/params.json + inline `S = {...}` |

### compat_sweep.py 6 system

| System | rule count |
|---|---|
| NECKTYPE_COMPAT | 3 (boat / straight / square) |
| SHOULDER_NECKTYPE_COMPAT | 3 (halter / off_shoulder / one_shoulder) |
| DETAIL_NECKTYPE_COMPAT | 1 (keyhole) |
| SHOULDER_DETAIL_COMPAT | 3 (halter / off_shoulder / one_shoulder) |
| COLLAR_COMPAT | 8 (round / v / deep_v / u / square / boat / scoop / straight) |
| NECK_BC_BLOCKED | 9 pair |
| **Total** | **27** (cont.72 Part 13 정정값) |

COLLAR_COMPAT 차단 매트릭스: 12/40 cells (30%) — neckShape × collarGroup 호환성 명시.

### style_overlay_sweep.py 7 style

| Style | deltas | overrides | sample override |
|---|---|---|---|
| casual | 2 | 2 | dart:'none' |
| formal | 3 | 3 | dart:'bust' |
| military | 2 | 4 | pocket:'cargo' |
| workwear | 2 | 3 | pocket:'chest_two' |
| sport | 2 | 4 | sleeveType:'raglan' |
| minimal | 0 | 5 | pocket:'none' (의도된 pure subtractive) |
| romantic | 2 | 2 | sleeveShape:'puff' |

---

## CI 통합 (Phase 4+)

`.github/workflows/audit.yml` (TODO Phase 4 시점):

```yaml
- run: python3 tools/audit/sync_check.py
- run: python3 tools/audit/compat_sweep.py
- run: python3 tools/audit/style_overlay_sweep.py
```

3 도구 모두 PASS = 회귀 0 보장. 실패 시 commit 차단.

---

## 후속 (자율 영역)

| 도구 | 추가 검증 후보 |
|---|---|
| `sync_check.py` | i18n EN/KO 정합 (F 자율 영역) / preset schema 정합 (G 자율 영역) / extended_ranges sync (H) |
| `compat_sweep.py` | DOM 발동 검증 (Playwright + Puppeteer, 18건 잔존) |
| `style_overlay_sweep.py` | 시각 매력도 sweep (이람 검수 영역, 원칙 14) |
| 새 도구 | `pom_check.py` (POM A-Q 17 ↔ params.json pom_formulas 10 정합) |

---

*cont.72 Part 16 자율 영역 K — 2026-05-15 코드탭*
*tools/audit/ 인덱스, 회귀 0, 모든 도구 BASH 1줄 실행 가능*
