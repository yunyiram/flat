#!/usr/bin/env python3
"""
sweep_matrix.py — FLAT preset × axis sweep matrix 생성

cont.72 Part 13 자율 도구 1순위 (cont.65 sweep_matrix.py 부재 정정).
docs/flat_scraper_tools_spec.md § 2.1 spec.

현재 minimal (data extract only):
- PresetModule.DB / SKIRT_DB / PANTS_DB 추출 (data/presets/ JSON 기반)
- preset × axis sweep matrix 생성 (예: 16 preset × 6 sleeveLength = 96 case)
- JSON output (PNG 캡처는 후속 — preview MCP 회복 또는 headless chrome 추가 시)

사용:
  python3 tools/audit/sweep_matrix.py [--axis sleeveLength] [--cat top|all] [--out tools/audit/sweep.json]

후속 (preview 회복 시 PNG 통합):
- Playwright/Puppeteer headless capture
- DOM 실측 자동화
- gallery.html 자동 생성
"""

import json
import os
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_PRESETS = ROOT / "data" / "presets"

SLEEVE_LENGTHS = ["sleeveless", "cap", "short", "elbow", "threequarter", "long"]
SLEEVE_VALUES = {"sleeveless": 0, "cap": 15, "short": 30, "elbow": 50, "threequarter": 72, "long": 95}

DEFAULT_AXES = {
    "sleeveLength": SLEEVE_LENGTHS,
    "sleeveType": ["setin", "raglan", "kimono"],
    "shoulderType": ["standard", "dropped", "off_shoulder", "halter", "extended", "narrow", "strapless", "one_shoulder"],
    "fit": ["skin", "slim", "regular", "relaxed", "oversized", "boxy"],
    "neckShape": ["round", "v", "deep_v", "u", "square", "boat", "scoop", "straight"],
}


def load_presets(cat_filter="top"):
    """data/presets/{cat}.json 로드. cat_filter='top' = top wear 7 cat (16 preset)."""
    top_cats = ["tshirts", "polo", "shirtsBlouses", "knitwear", "sweatshirts", "dress", "outerwear"]
    all_cats = top_cats + ["skirt", "pants"]
    cats = top_cats if cat_filter == "top" else all_cats

    presets = []
    for cat in cats:
        f = DATA_PRESETS / f"{cat}.json"
        if not f.exists():
            print(f"  ⚠️ skip: {f}")
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        for p in d.get("presets", []):
            presets.append({
                "cat": cat,
                "name": p["name"],
                "s": p.get("s", {}),
            })
    return presets


def generate_sweep_matrix(axis="sleeveLength", cat_filter="top"):
    """preset × axis 조합 sweep matrix 생성."""
    presets = load_presets(cat_filter)
    axis_values = DEFAULT_AXES.get(axis)
    if not axis_values:
        raise ValueError(f"unknown axis: {axis}. supported: {list(DEFAULT_AXES.keys())}")

    cases = []
    for p in presets:
        for v in axis_values:
            case = {
                "preset_name": p["name"],
                "preset_cat": p["cat"],
                "axis": axis,
                "value": v,
                "state_override": {axis: v},
            }
            # sleeveLength axis는 slider 값도 동시 set
            if axis == "sleeveLength":
                case["state_override"]["sleeveLen"] = v
                case["state_override"]["sleeveLength"] = SLEEVE_VALUES.get(v, 0)
            cases.append(case)

    return {
        "version": "0.1",
        "generated": datetime.now().isoformat(),
        "axis": axis,
        "axis_values": axis_values,
        "cat_filter": cat_filter,
        "preset_count": len(presets),
        "axis_count": len(axis_values),
        "total_cases": len(cases),
        "cases": cases,
    }


def main():
    parser = argparse.ArgumentParser(description="FLAT sweep matrix generator")
    parser.add_argument("--axis", default="sleeveLength", help=f"sweep axis ({list(DEFAULT_AXES.keys())})")
    parser.add_argument("--cat", default="top", choices=["top", "all"], help="preset filter")
    parser.add_argument("--out", default=None, help="output JSON path (default: tools/audit/sweep_{axis}.json)")
    parser.add_argument("--list-axes", action="store_true", help="list supported axes")
    args = parser.parse_args()

    if args.list_axes:
        print("Supported axes:")
        for ax, vals in DEFAULT_AXES.items():
            print(f"  {ax}: {vals}")
        return

    matrix = generate_sweep_matrix(args.axis, args.cat)

    out = Path(args.out) if args.out else (ROOT / "tools" / "audit" / f"sweep_{args.axis}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(matrix, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"✅ Sweep matrix generated:")
    print(f"   axis: {matrix['axis']}")
    print(f"   preset: {matrix['preset_count']}")
    print(f"   axis values: {matrix['axis_count']}")
    print(f"   total cases: {matrix['total_cases']}")
    print(f"   output: {out}")
    print(f"")
    print(f"후속 (preview 회복 시):")
    print(f"  - Playwright/Puppeteer로 각 case 적용 + screenshot 캡처")
    print(f"  - DOM 실측 (BodyComp.geometry / SleeveComp 등) 자동")
    print(f"  - gallery.html 자동 생성 (cont.67 96 PNG 패턴)")


if __name__ == "__main__":
    main()
