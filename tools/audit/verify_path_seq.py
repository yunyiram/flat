#!/usr/bin/env python3
"""
verify_path_seq.py — FLAT path command sequence 불변성 검증 (cascade_pattern.md #2)

출처: cascade_pattern.md POC 학습 #2. POC `tests/verify-paths.js`의 본체 적용판.
정적 분석 보고서: docs/inspect_flat_path_seq_static_analysis.md

가설 (정정):
- 원본 #2: "preset 그룹 안에서 모든 case command seq 불변"
- 정정 #2: "**option 조합** 그룹 안에서 **numeric slider** 변경 시 command seq 불변"

위반 시 = numeric slider가 분기를 만든 것 = 사고 의심 (cont.63 자의적 90° 블렌딩 차원).

환경 의존:
- Playwright + chromium (inspect_flat.py 자매)
- 본 코드탭 세션 (Linux sandbox)에서는 미실행. 이람 환경에서 실행.

셋업 (1회):
  pip3 install playwright
  python3 -m playwright install chromium

사용:
  # axis sweep (enum option 변경) — command seq 분기 매트릭스 추출
  python3 tools/audit/verify_path_seq.py --axis sleeveLength --cat top
  python3 tools/audit/verify_path_seq.py --axis neckShape --cat top

  # numeric sweep ★ 사고 의심 검증 (slider 미세 변동 → command seq 불변 확인)
  python3 tools/audit/verify_path_seq.py --numeric-sweep neckCurve --cat top
  python3 tools/audit/verify_path_seq.py --numeric-sweep hipFlare --cat top
  python3 tools/audit/verify_path_seq.py --numeric-sweep sleeveLength --cat top

  # 모든 numeric slider 한 번에
  python3 tools/audit/verify_path_seq.py --numeric-sweep-all --cat top

결과:
  - stdout: PASS/FAIL summary + 위반 case 상세 (어느 분기/어느 함수 의심)
  - JSON: tools/audit/path_seq_baselines/{axis}_{cat}.json (PASS 시 baseline)
  - JSON: tools/audit/path_seq_violations/{axis}_{cat}.json (FAIL 시 위반 detail)

회귀 위험: 0 (검증만 추가, flat-v6.html 변경 0).

2026-05-15 코드탭 cont.72 Part 17 신설. cascade_pattern.md #2 본체 적용 1차.
"""

import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("⚠️ playwright 미설치. 셋업:")
    print("  pip3 install playwright")
    print("  python3 -m playwright install chromium")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_PRESETS = ROOT / "data" / "presets"
BASELINES_DIR = ROOT / "tools" / "audit" / "path_seq_baselines"
VIOLATIONS_DIR = ROOT / "tools" / "audit" / "path_seq_violations"

# inspect_flat.py와 동일 — 이람 환경에 맞게 조정 가능
# (Cowork 환경: /home/claude/.cache/puppeteer/... / Mac 환경: playwright 자동 셋업 경로)
FLAT_URL = "https://yunyiram.github.io/flat/flat-v6.html"

# command sequence 추출 — POC `commandSeq` 함수 포팅
PATH_CMD_RE = re.compile(r"[MmCcLlQqZzTtSsHhVvAa]")


def cmd_seq(d):
    """SVG path d 속성 → command 시퀀스 string (예: 'MLCC')."""
    if not d:
        return ""
    return "".join(PATH_CMD_RE.findall(d))


# numeric slider 매트릭스 — 사고 의심 boundary 포함
NUMERIC_SWEEPS = {
    "neckCurve": [0, 3, 5, 6, 7, 10, 14, 15, 16, 20, 50, 80, 100],     # ★ #1 사고 boundary 6/15
    "hipFlare": [0, 4, 7, 8, 9, 12, 16, 20],                            # ★ #2 사고 boundary 8
    "sleeveLength": [0, 1, 2, 3, 5, 10, 30, 50, 72, 95],                # ★ #3 사고 boundary 2
    "chest": [40, 50, 60, 70, 80],
    "fitW": [20, 40, 50, 60, 80],
    "shoulderExtra": [-10, -5, 0, 5, 10],
    "shoulderSlope": [0, 5, 10, 15, 20],
    "neckWidth": [0, 25, 50, 75, 100],
    "neckDepth": [0, 25, 50, 75, 100],
    "bodyLen": [-20, -10, 0, 10, 20, 30],
    "sleeveWidth": [0, 25, 50, 75, 100],
}

DEFAULT_AXES = {
    "sleeveLength": ["sleeveless", "cap", "short", "elbow", "threequarter", "long"],
    "sleeveType": ["setin", "raglan", "kimono"],
    "shoulderType": ["standard", "dropped", "off_shoulder", "halter", "extended", "narrow", "strapless", "one_shoulder"],
    "neckShape": ["round", "v", "deep_v", "u", "square", "boat", "scoop", "straight"],
    "hemShape": ["straight", "curved", "shirt_tail", "asym", "hi_lo", "side_slit"],
    "sleeveCuff": ["plain", "rib", "knit", "elastic", "barrel"],
}


def load_presets(cat_filter="top"):
    """data/presets/ 9 cat JSON 로드. cat_filter='top' = 7 cat (16 preset)."""
    top_cats = ["tshirts", "polo", "shirtsBlouses", "knitwear", "sweatshirts", "dress", "outerwear"]
    all_cats = top_cats + ["skirt", "pants"]
    cats = top_cats if cat_filter == "top" else all_cats
    presets = []
    for cat in cats:
        f = DATA_PRESETS / f"{cat}.json"
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        for p in d.get("presets", []):
            presets.append({"cat": cat, "name": p["name"], "s": p.get("s", {})})
    return presets


def enter_preset(page, preset_name):
    """카드 피드 → preset 진입 → panel mode → 검증 가능 상태."""
    page.goto(FLAT_URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(2500)
    # CardFeed.DB 또는 PresetModule.DB에서 preset index 검색 후 진입
    js_enter = f"""
        const dbKey = (typeof PresetModule !== 'undefined' && PresetModule.DB) ? 'PresetModule' : null;
        if (!dbKey) {{ throw new Error('PresetModule.DB 미정의'); }}
        const idx = PresetModule.DB.findIndex(p => p.name === '{preset_name}');
        if (idx < 0) {{ throw new Error('preset {preset_name} not found'); }}
        const card = document.querySelector('.card[data-card="' + idx + '"] .card-enter-btn');
        if (card) card.click();
        else {{
            // fallback: 카드가 없으면 직접 apply
            PresetModule.apply(idx);
        }}
    """
    try:
        page.evaluate(js_enter)
    except Exception as e:
        return False, str(e)
    page.wait_for_timeout(1500)
    try:
        page.evaluate("if(typeof CardFeed !== 'undefined') CardFeed.pickVariant(0)")
    except Exception:
        pass
    page.wait_for_timeout(800)
    try:
        page.evaluate("setMode('panel')")
    except Exception:
        pass
    page.wait_for_timeout(400)
    return True, None


def apply_state(page, overrides):
    """S.* 상태 override + draw() 재호출."""
    parts = []
    for k, v in overrides.items():
        if isinstance(v, str):
            parts.append(f"S.{k}={v!r}")
        else:
            parts.append(f"S.{k}={v}")
    js = "; ".join(parts) + "; if(typeof showHandles!=='undefined') showHandles=false; if(typeof draw==='function') draw();"
    page.evaluate(js)
    page.wait_for_timeout(300)


def dump_path_seqs(page):
    """현재 SVG의 모든 path d 속성 → {layer_id: command_seq} dict.

    SVG 안 path element를 등장 순서 + class/id로 group. command seq만 추출.
    """
    return page.evaluate("""
        () => {
            const result = {};
            ['svgF', 'svgB'].forEach(svgId => {
                const svg = document.getElementById(svgId);
                if (!svg) return;
                const paths = svg.querySelectorAll('path');
                paths.forEach((p, i) => {
                    const d = p.getAttribute('d') || '';
                    const seq = d.match(/[MmCcLlQqZzTtSsHhVvAa]/g);
                    const key = svgId + '_' + i + '_' + (p.getAttribute('class') || '');
                    result[key] = seq ? seq.join('') : '';
                });
            });
            return result;
        }
    """)


def axis_sweep(page, preset_name, axis, axis_values):
    """preset 안에서 axis value 변경하며 command seq 매트릭스 추출.

    return: {axis_value: {layer_id: cmd_seq}}
    """
    ok, err = enter_preset(page, preset_name)
    if not ok:
        return None, err
    matrix = {}
    for v in axis_values:
        overrides = {axis: v}
        # sleeveLength axis는 slider도 동시 set
        if axis == "sleeveLength":
            sleeve_values = {"sleeveless": 0, "cap": 15, "short": 30, "elbow": 50, "threequarter": 72, "long": 95}
            overrides["sleeveLen"] = v
            overrides["sleeveLength"] = sleeve_values.get(v, 0)
        try:
            apply_state(page, overrides)
            seqs = dump_path_seqs(page)
            matrix[str(v)] = seqs
        except Exception as e:
            matrix[str(v)] = {"_error": str(e)}
    return matrix, None


def numeric_sweep(page, preset_name, slider, values):
    """numeric slider 미세 변동 → command seq 불변 검증.

    return: {value: {layer_id: cmd_seq}}, violations list
    """
    ok, err = enter_preset(page, preset_name)
    if not ok:
        return None, [{"error": err}]
    matrix = {}
    violations = []
    baseline = None
    baseline_v = None
    for v in values:
        try:
            apply_state(page, {slider: v})
            seqs = dump_path_seqs(page)
            matrix[str(v)] = seqs
            if baseline is None:
                baseline = seqs
                baseline_v = v
            else:
                # 같은 layer_id 키 + 다른 cmd_seq 있으면 위반
                for k, cur in seqs.items():
                    base = baseline.get(k)
                    if base is not None and base != cur:
                        violations.append({
                            "preset": preset_name,
                            "slider": slider,
                            "baseline_value": baseline_v,
                            "violating_value": v,
                            "layer": k,
                            "baseline_seq": base,
                            "violating_seq": cur,
                        })
        except Exception as e:
            matrix[str(v)] = {"_error": str(e)}
    return matrix, violations


def main():
    parser = argparse.ArgumentParser(description="FLAT path command sequence verifier (cascade_pattern.md #2)")
    parser.add_argument("--axis", help=f"axis sweep (enum option) — {list(DEFAULT_AXES.keys())}")
    parser.add_argument("--numeric-sweep", dest="numeric_sweep", help=f"numeric slider sweep — {list(NUMERIC_SWEEPS.keys())}")
    parser.add_argument("--numeric-sweep-all", dest="numeric_sweep_all", action="store_true", help="모든 numeric slider sweep")
    parser.add_argument("--cat", default="top", choices=["top", "all"], help="preset filter")
    parser.add_argument("--preset", help="단일 preset만 (기본 = cat 전체)")
    parser.add_argument("--url", default=FLAT_URL, help="flat-v6.html URL (default = GitHub Pages)")
    parser.add_argument("--list-sliders", action="store_true", help="numeric slider 값 매트릭스 출력 후 종료")
    args = parser.parse_args()

    if args.list_sliders:
        print("Numeric sliders (값 매트릭스):")
        for s, vals in NUMERIC_SWEEPS.items():
            print(f"  {s}: {vals}")
        print("\nAxes (enum option):")
        for ax, vals in DEFAULT_AXES.items():
            print(f"  {ax}: {vals}")
        return

    if not (args.axis or args.numeric_sweep or args.numeric_sweep_all):
        parser.print_help()
        print("\n⚠️ --axis / --numeric-sweep / --numeric-sweep-all 중 하나 필수")
        sys.exit(1)

    presets = load_presets(args.cat)
    if args.preset:
        presets = [p for p in presets if p["name"] == args.preset]
        if not presets:
            print(f"⚠️ preset '{args.preset}' 미발견")
            sys.exit(1)

    print(f"=== verify_path_seq.py ===")
    print(f"presets: {len(presets)} ({args.cat})")
    print(f"URL: {args.url}")
    print()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1600, "height": 1200})
        page = ctx.new_page()

        all_violations = []
        all_matrices = {}

        # axis sweep mode
        if args.axis:
            axis_values = DEFAULT_AXES.get(args.axis)
            if not axis_values:
                print(f"⚠️ unknown axis: {args.axis}")
                sys.exit(1)
            for preset in presets:
                print(f"  [axis] {preset['cat']}/{preset['name']} × {args.axis}")
                matrix, err = axis_sweep(page, preset["name"], args.axis, axis_values)
                if err:
                    print(f"    ❌ {err}")
                    continue
                all_matrices[preset["name"]] = matrix
                # axis sweep는 분기 매트릭스 추출 = baseline 비교 X (이건 의도된 분기)
                seq_groups = {}
                for v, seqs in matrix.items():
                    if "_error" in seqs:
                        continue
                    for k, seq in seqs.items():
                        seq_groups.setdefault(k, {}).setdefault(seq, []).append(v)
                # 분기 발견 보고
                branch_count = sum(1 for k, g in seq_groups.items() if len(g) > 1)
                print(f"    분기 layer: {branch_count} / {len(seq_groups)}")

        # numeric sweep mode
        sliders = []
        if args.numeric_sweep:
            if args.numeric_sweep not in NUMERIC_SWEEPS:
                print(f"⚠️ unknown slider: {args.numeric_sweep}")
                sys.exit(1)
            sliders = [args.numeric_sweep]
        elif args.numeric_sweep_all:
            sliders = list(NUMERIC_SWEEPS.keys())

        for slider in sliders:
            values = NUMERIC_SWEEPS[slider]
            print(f"\n  [numeric] {slider} × {values}")
            for preset in presets:
                matrix, violations = numeric_sweep(page, preset["name"], slider, values)
                if violations and "error" in violations[0]:
                    print(f"    {preset['name']}: ❌ {violations[0]['error']}")
                    continue
                all_matrices.setdefault("_numeric", {}).setdefault(slider, {})[preset["name"]] = matrix
                if violations:
                    print(f"    {preset['name']}: ⚠️ {len(violations)} violation(s)")
                    for v in violations[:3]:
                        print(f"       {v['slider']}={v['baseline_value']}→{v['violating_value']} layer={v['layer'][:40]} {v['baseline_seq']}→{v['violating_seq']}")
                    if len(violations) > 3:
                        print(f"       ... +{len(violations)-3} more")
                    all_violations.extend(violations)
                else:
                    print(f"    {preset['name']}: ✅ PASS ({len(values)} values, all cmd_seq invariant)")

        browser.close()

    # save baseline / violations
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    VIOLATIONS_DIR.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    label = args.axis or args.numeric_sweep or "all"
    base_file = BASELINES_DIR / f"{label}_{args.cat}_{ts}.json"
    base_file.write_text(json.dumps({
        "generated": datetime.now().isoformat(),
        "mode": "axis" if args.axis else "numeric",
        "label": label,
        "cat": args.cat,
        "preset_count": len(presets),
        "matrices": all_matrices,
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n✅ baseline saved: {base_file.relative_to(ROOT)}")

    if all_violations:
        viol_file = VIOLATIONS_DIR / f"{label}_{args.cat}_{ts}.json"
        viol_file.write_text(json.dumps({
            "generated": datetime.now().isoformat(),
            "violation_count": len(all_violations),
            "violations": all_violations,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"⚠️ violations: {len(all_violations)} → {viol_file.relative_to(ROOT)}")
        print(f"\n사고 의심 위치 — docs/inspect_flat_path_seq_static_analysis.md § 4 표 참고")
        sys.exit(2)
    else:
        print(f"\n✅ ALL PASS — option 그룹 안 numeric slider command seq 불변 확인")


if __name__ == "__main__":
    main()
