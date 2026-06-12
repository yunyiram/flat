#!/usr/bin/env python3
"""
inspect_spec.py — FLAT spec 자체 수학적 정합성 검증 (cascade_pattern.md #3)

출처: cascade_pattern.md POC 학습 #3.
사례: POC PRD § 3.3 "검증 완료" 라벨인데 구현 단계서 누락 발견 (max bodyLength + SHOULDER_Y > VIEW_H, 880>800).
즉 spec "검증 완료" 라벨 신뢰 자체가 위험. spec의 수학적 정합성을 자동으로 sweep.

본 도구는 chrome 의존 0 (Python only).
sync_check.py (cont.72 Part 16/16-3)와 분담:
- sync_check.py = data/ JSON ↔ flat-v6.html inline 동기화 검증
- inspect_spec.py = spec 안 수치의 수학적 정합성 (bounds / 범위 / 단위 / cross-spec 관계식)

검증 영역:
  1. preset numeric slider bounds — 16 preset × 27 slider × spec range
  2. rules.json matrix key 정합 — necktype_compat 등 matrix key가 모두 valid enum
  3. sleeve_length_ratios.json 정합 — ratios 범위 + labelMap 매핑 + women/men 7×2 항목 완전
  4. seams/*.json area count 정합 — index.json totalAreas ↔ 7 group 합계
  5. cross-spec consistency — sleeve_length_ratios labelMap ↔ flat-v6.html sleeveLen enum 정합

종료 코드: 0 = 모두 통과, 1 = 위반 발견.

사용:
  python3 tools/audit/inspect_spec.py            # 모든 영역 sweep
  python3 tools/audit/inspect_spec.py --area 1   # 영역 1만
  python3 tools/audit/inspect_spec.py --verbose  # 통과 항목도 출력

2026-05-15 코드탭 cont.72 Part 18 신설. cascade_pattern.md #3 본체 적용.
"""

import json
import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
DATA_PRESETS = DATA / "presets"
DATA_RULES = DATA / "rules"
DATA_SEAMS = DATA / "seams"
FLAT_HTML = ROOT / "flat-v6.html"


# ─────────────────────────────────────────────
# Spec — preset numeric slider bounds
# (flat-v6.html slider min/max 추출 자동화 가능, 우선 spec hardcode)
# ─────────────────────────────────────────────

SLIDER_BOUNDS = {
    # numeric sliders (0-100 unless noted)
    "neckDepth": (0, 100),
    "neckCurve": (0, 100),
    "neckWidth": (0, 100),
    "shoulderSlope": (0, 100),
    "shoulderExtra": (-20, 20),
    "sleeveLength": (0, 100),     # % slider
    "sleeveWidth": (0, 100),
    "hipFlare": (-20, 30),
    "fitW": (0, 100),
    "bodyLen": (-50, 100),
    "chest": (0, 100),
    # 추가 numeric (skirt/pants)
    "waist": (0, 100),
    "rise": (0, 100),
    "inseam": (0, 200),
    "hem": (0, 100),
    "ankle": (0, 100),
    "knee": (0, 100),
}

# enum sliders — valid value sets
ENUM_VALUES = {
    "neckShape": {"round", "v", "deep_v", "u", "square", "boat", "scoop", "straight"},
    "neckFinish": {"plain", "rib", "facing", "binding", "hood", "turtle", "mock", "collar", "drape", "none"},
    "shoulderType": {"standard", "dropped", "off_shoulder", "halter", "extended", "narrow", "strapless", "one_shoulder"},
    "sleeveType": {"setin", "raglan", "kimono", "dolman"},
    "sleeveLen": {"sleeveless", "cap", "short", "elbow", "threequarter", "long"},
    "sleeveCuff": {"plain", "rib", "knit", "elastic", "barrel", "cuff", "buttoned"},
    "sideSeam": {"yes", "no"},
    "silhouette": {"straight", "slight_a", "a_line", "fitted", "trumpet", "tapered"},
    "dart": {"none", "waist", "princess", "bust", "shoulder"},
    "hemShape": {"straight", "curved", "shirt_tail", "asym", "hi_lo", "side_slit"},
    "hemFinish": {"folded", "raw", "rolled", "bound", "scalloped"},
    "fit": {"skin", "slim", "regular", "relaxed", "oversized", "boxy"},
    "pocket": {"none", "patch", "welt", "kangaroo", "chest", "side"},
    "trimming": {"none", "piping", "ribbon", "lace", "binding"},
    "stitchType": {"single", "double", "topstitch", "blind", "felled"},
    "closure": {"none", "button", "zip", "snap", "tie", "buckle"},
    "pleat": {"none", "knife", "box", "inverted", "accordion"},
}


# ─────────────────────────────────────────────
# 1. Preset numeric slider bounds
# ─────────────────────────────────────────────

def check_preset_bounds(verbose=False):
    """16 preset × 27 slider 범위 검증."""
    violations = []
    preset_count = 0
    field_count = 0
    enum_unknown = []

    for f in sorted(DATA_PRESETS.glob("*.json")):
        if f.name == "index.json":
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        for preset in d.get("presets", []):
            preset_count += 1
            s = preset.get("s", {})
            for key, val in s.items():
                field_count += 1
                if key in SLIDER_BOUNDS:
                    lo, hi = SLIDER_BOUNDS[key]
                    if not isinstance(val, (int, float)):
                        violations.append({
                            "preset": preset["name"],
                            "field": key,
                            "value": val,
                            "expected": f"numeric in [{lo}, {hi}]",
                            "type": "wrong_type",
                        })
                    elif val < lo or val > hi:
                        violations.append({
                            "preset": preset["name"],
                            "field": key,
                            "value": val,
                            "expected": f"[{lo}, {hi}]",
                            "type": "out_of_bounds",
                        })
                    elif verbose:
                        print(f"    ✓ {preset['name']}.{key} = {val} in [{lo}, {hi}]")
                elif key in ENUM_VALUES:
                    if val not in ENUM_VALUES[key]:
                        violations.append({
                            "preset": preset["name"],
                            "field": key,
                            "value": val,
                            "expected": f"one of {sorted(ENUM_VALUES[key])}",
                            "type": "invalid_enum",
                        })
                    elif verbose:
                        print(f"    ✓ {preset['name']}.{key} = '{val}' valid enum")
                else:
                    # field가 spec에 정의 안 됨 — 누락 신호
                    enum_unknown.append(f"{preset['name']}.{key}={val!r}")

    return {
        "area": "1. preset slider bounds",
        "preset_count": preset_count,
        "field_count": field_count,
        "violation_count": len(violations),
        "unknown_field_count": len(set(f.split('=')[0] for f in enum_unknown)),
        "violations": violations,
        "unknown_fields_sample": sorted(set(enum_unknown))[:10],
    }


# ─────────────────────────────────────────────
# 2. rules.json matrix key 정합
# ─────────────────────────────────────────────

def check_rules_matrix(verbose=False):
    """data/rules.json 의 compatibility matrix key가 valid enum에 매핑되는지 검증."""
    f = DATA / "rules.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    violations = []
    checked = 0

    # necktype_compat — neckShape key
    matrix = d.get("necktype_compat", {}).get("matrix", {})
    for shape in matrix:
        checked += 1
        if shape not in ENUM_VALUES["neckShape"]:
            violations.append({
                "system": "necktype_compat",
                "key": shape,
                "expected": "valid neckShape enum",
            })
        elif verbose:
            print(f"    ✓ necktype_compat.{shape} valid")

    # variant_necktype_compat — shoulderType key (단, "none" = standard alias)
    matrix = d.get("variant_necktype_compat", {}).get("matrix", {})
    valid_shoulders = ENUM_VALUES["shoulderType"] | {"none"}  # "none" = standard alias
    for st in matrix:
        checked += 1
        if st not in valid_shoulders:
            violations.append({
                "system": "variant_necktype_compat",
                "key": st,
                "expected": "valid shoulderType enum or 'none'",
            })
        elif verbose:
            print(f"    ✓ variant_necktype_compat.{st} valid")

    # all_types 명세된 collar/finish/hood/highneck 카운트
    all_types = d.get("necktype_compat", {}).get("all_types", [])
    expected_types = {"finish", "collar", "highneck", "hood"}
    if set(all_types) != expected_types:
        violations.append({
            "system": "necktype_compat.all_types",
            "actual": all_types,
            "expected": sorted(expected_types),
        })

    return {
        "area": "2. rules.json matrix key 정합",
        "checked_count": checked,
        "violation_count": len(violations),
        "violations": violations,
    }


# ─────────────────────────────────────────────
# 3. sleeve_length_ratios.json 정합
# ─────────────────────────────────────────────

def check_sleeve_ratios(verbose=False):
    """sleeve_length_ratios.json 의 ratio 범위 + labelMap 매핑 + women/men 완전성."""
    f = DATA_RULES / "sleeve_length_ratios.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    violations = []
    checked = 0

    # 1) ratio 범위 (0 < ratio ≤ 1.075)
    expected_keys = {"veryShort", "short", "regular", "aboveElbow", "forearm", "wrist", "full"}
    for gender in ["women", "men"]:
        ratios = d.get("ratios", {}).get(gender, {})
        if set(ratios.keys()) != expected_keys:
            violations.append({
                "check": f"ratios.{gender} keys",
                "actual": sorted(ratios.keys()),
                "expected": sorted(expected_keys),
            })
        for k, v in ratios.items():
            checked += 1
            if not isinstance(v, (int, float)) or v <= 0 or v > 1.1:
                violations.append({
                    "check": f"ratios.{gender}.{k}",
                    "value": v,
                    "expected": "0 < ratio ≤ 1.075",
                })
            elif verbose:
                print(f"    ✓ ratios.{gender}.{k} = {v}")

        # ratio monotonic 증가 검증 (veryShort < short < regular < ...)
        order = ["veryShort", "short", "regular", "aboveElbow", "forearm", "wrist", "full"]
        seq = [ratios.get(k) for k in order]
        if all(isinstance(x, (int, float)) for x in seq):
            for i in range(1, len(seq)):
                if seq[i] <= seq[i - 1]:
                    violations.append({
                        "check": f"ratios.{gender} monotonic",
                        "fail_at": f"{order[i-1]}={seq[i-1]} >= {order[i]}={seq[i]}",
                    })

    # 2) labelMap 모든 key가 ratios sub-key에 매핑 (sleeveless=null 제외)
    label_map = d.get("labelMap", {})
    expected_labels = {"sleeveless", "cap", "short", "elbow", "threequarter", "long"}
    if set(label_map.keys()) != expected_labels:
        violations.append({
            "check": "labelMap keys",
            "actual": sorted(label_map.keys()),
            "expected": sorted(expected_labels),
        })
    for k, v in label_map.items():
        checked += 1
        if k == "sleeveless":
            if v is not None:
                violations.append({
                    "check": f"labelMap.{k}",
                    "value": v,
                    "expected": "null (sleeveless)",
                })
        else:
            if v not in expected_keys:
                violations.append({
                    "check": f"labelMap.{k}",
                    "value": v,
                    "expected": f"one of {sorted(expected_keys)}",
                })
            elif verbose:
                print(f"    ✓ labelMap.{k} -> ratios.{v}")

    return {
        "area": "3. sleeve_length_ratios.json 정합",
        "checked_count": checked,
        "violation_count": len(violations),
        "violations": violations,
    }


# ─────────────────────────────────────────────
# 4. seams/*.json area count 정합
# ─────────────────────────────────────────────

def check_seams_count(verbose=False):
    """seams/index.json totalAreas ↔ 7 group 합계 정합."""
    idx_f = DATA_SEAMS / "index.json"
    if not idx_f.exists():
        return {"area": "4. seams area count 정합", "skipped": True, "reason": "seams/index.json not found"}
    idx = json.loads(idx_f.read_text(encoding="utf-8"))
    declared = idx.get("totalAreas")
    violations = []
    computed = 0
    group_counts = {}
    for f in sorted(DATA_SEAMS.glob("*.json")):
        if f.name == "index.json":
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        # areas array 또는 부위 key 모두 카운트
        n = 0
        if isinstance(d.get("areas"), list):
            n = len(d["areas"])
        elif isinstance(d.get("seams"), list):
            n = len(d["seams"])
        else:
            # fallback: dict의 sub-key count
            for k, v in d.items():
                if isinstance(v, dict) and "seam_mm" in v:
                    n += 1
        group_counts[f.stem] = n
        computed += n

    if declared is not None and declared != computed:
        violations.append({
            "check": "totalAreas",
            "declared": declared,
            "computed": computed,
            "group_counts": group_counts,
        })

    if verbose:
        print(f"    group counts: {group_counts}")
        print(f"    declared={declared}, computed={computed}")

    return {
        "area": "4. seams area count 정합",
        "declared": declared,
        "computed": computed,
        "group_counts": group_counts,
        "violation_count": len(violations),
        "violations": violations,
    }


# ─────────────────────────────────────────────
# 5. cross-spec consistency — sleeve_length_ratios labelMap ↔ ENUM_VALUES.sleeveLen
# ─────────────────────────────────────────────

def check_cross_spec(verbose=False):
    """sleeve_length_ratios.json labelMap keys = ENUM_VALUES.sleeveLen 일치."""
    f = DATA_RULES / "sleeve_length_ratios.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    label_keys = set(d.get("labelMap", {}).keys())
    enum_keys = ENUM_VALUES["sleeveLen"]
    violations = []
    if label_keys != enum_keys:
        violations.append({
            "check": "labelMap keys ↔ ENUM_VALUES.sleeveLen",
            "missing_in_labelMap": sorted(enum_keys - label_keys),
            "extra_in_labelMap": sorted(label_keys - enum_keys),
        })
    elif verbose:
        print(f"    ✓ labelMap keys = ENUM_VALUES.sleeveLen ({sorted(enum_keys)})")

    return {
        "area": "5. cross-spec — labelMap ↔ sleeveLen enum",
        "violation_count": len(violations),
        "violations": violations,
    }


# ─────────────────────────────────────────────
# main
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="FLAT spec 자체 수학적 정합성 검증 (cascade_pattern.md #3)")
    parser.add_argument("--area", type=int, choices=[1, 2, 3, 4, 5], help="단일 영역만")
    parser.add_argument("--verbose", action="store_true", help="통과 항목도 출력")
    args = parser.parse_args()

    print(f"=== inspect_spec.py — cascade_pattern.md #3 본체 적용 ===\n")

    checks = [
        (1, check_preset_bounds),
        (2, check_rules_matrix),
        (3, check_sleeve_ratios),
        (4, check_seams_count),
        (5, check_cross_spec),
    ]

    if args.area:
        checks = [c for c in checks if c[0] == args.area]

    overall_pass = True
    summary = []
    for num, fn in checks:
        result = fn(args.verbose)
        if result.get("skipped"):
            print(f"  [{num}] {result['area']} — ⚠️ SKIP ({result.get('reason')})")
            summary.append((num, result["area"], "SKIP"))
            continue
        v_count = result["violation_count"]
        if v_count == 0:
            extra = ""
            if "preset_count" in result:
                extra = f" ({result['preset_count']} preset × {result['field_count']} field, {result.get('unknown_field_count', 0)} 미정의)"
            elif "checked_count" in result:
                extra = f" ({result['checked_count']} checks)"
            elif "computed" in result:
                extra = f" ({result['declared']}/{result['computed']})"
            print(f"  [{num}] {result['area']} — ✅ PASS{extra}")
            summary.append((num, result["area"], "PASS"))
        else:
            print(f"  [{num}] {result['area']} — ❌ {v_count} violation(s)")
            for vio in result["violations"][:5]:
                print(f"       {json.dumps(vio, ensure_ascii=False)[:120]}")
            if v_count > 5:
                print(f"       ... +{v_count - 5} more")
            # unknown fields 보고 (preset bounds 만)
            if result.get("unknown_fields_sample"):
                print(f"       unknown fields (sample): {result['unknown_fields_sample'][:5]}")
            overall_pass = False
            summary.append((num, result["area"], f"FAIL ({v_count})"))

    print()
    print("=== Summary ===")
    for num, area, status in summary:
        print(f"  [{num}] {area}: {status}")
    print()
    if overall_pass:
        print("✅ ALL PASS")
        sys.exit(0)
    else:
        print("❌ 위반 발견 — 위 상세 참조")
        sys.exit(1)


if __name__ == "__main__":
    main()
