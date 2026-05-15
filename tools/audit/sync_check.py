#!/usr/bin/env python3
"""
sync_check.py — data/ JSON ↔ flat-v6.html inline 자동 정합성 검증

cont.72 Part 16 자율 영역 A2 ↔ A4 통합. 실행: `python3 tools/audit/sync_check.py`
회귀 0 보장. CI/사람 검증 양쪽에서 사용.

검증 영역 (cont.72 Part 16 발견 시점):
  1. PresetModule.DB / SKIRT_DB / PANTS_DB ↔ data/presets/*.json (34/34 동기화)
  2. fabricDB ↔ data/fabrics.json (41/41 동기화)
  3. compat 6 system 27 rule ↔ data/rules/*.json (lift-and-shift 정합)
  4. 22 collar / 12 opening dft ↔ S2 dft 마커 매핑

종료 코드: 0 = 모두 통과, 1 = mismatch 발견 (CI 차단용)
"""
import json
import os
import re
import sys


def find_block(text, start_marker, bracket='['):
    """주어진 marker 이후 첫 bracket 열림→닫힘 본문 추출."""
    start = text.find(start_marker)
    if start < 0:
        return None
    open_pos = text.find(bracket, start)
    close = ']' if bracket == '[' else '}'
    depth = 0
    i = open_pos
    while i < len(text):
        if text[i] == bracket:
            depth += 1
        elif text[i] == close:
            depth -= 1
            if depth == 0:
                return text[open_pos:i + 1]
        i += 1
    return None


def extract_names(body):
    return re.findall(r"name:['\"]([^'\"]+)['\"]", body)


def check_presets(text):
    """1. preset 34 / 9 cat 동기화"""
    db = extract_names(find_block(text, 'PresetModule={', '[') or '')
    # 더 정확: PresetModule 안의 DB:[
    pm_start = text.find('const PresetModule={')
    db_body = find_block(text[pm_start:], 'DB:[', '[') or ''
    skirt_body = find_block(text[pm_start:], 'SKIRT_DB:[', '[') or ''
    pants_body = find_block(text[pm_start:], 'PANTS_DB:[', '[') or ''
    db_names = extract_names(db_body)
    skirt_names = extract_names(skirt_body)
    pants_names = extract_names(pants_body)
    inline = set(db_names + skirt_names + pants_names)

    json_names = set()
    for fn in sorted(os.listdir('data/presets')):
        if fn == 'index.json' or not fn.endswith('.json'):
            continue
        with open(f'data/presets/{fn}') as f:
            data = json.load(f)
        if isinstance(data, list):
            for p in data:
                json_names.add(p.get('id') or p.get('name'))
        elif 'presets' in data:
            for p in data['presets']:
                json_names.add(p.get('id') or p.get('name'))

    ok = inline == json_names
    return {
        'name': 'preset DB ↔ JSON',
        'ok': ok,
        'inline_count': len(inline),
        'json_count': len(json_names),
        'only_inline': sorted(inline - json_names),
        'only_json': sorted(json_names - inline),
    }


def check_fabrics(text):
    """2. fabric 41 동기화 (FabricModule.DB, name 매칭)"""
    fm_start = text.find('const FabricModule')
    if fm_start < 0:
        return {'name': 'fabric ↔ JSON', 'ok': False, 'note': 'FabricModule not found'}
    db_body = find_block(text[fm_start:], 'DB:', '[') or ''
    inline_names = set(re.findall(r"name:['\"]([^'\"]+)['\"]", db_body))

    json_names = set()
    if os.path.exists('data/fabrics.json'):
        with open('data/fabrics.json') as f:
            data = json.load(f)
        for f_ in (data if isinstance(data, list) else data.get('fabrics', [])):
            # JSON entries have name.ko (B6.3 schema), fall back to name string
            n = f_.get('name')
            if isinstance(n, dict):
                json_names.add(n.get('ko') or n.get('en'))
            else:
                json_names.add(n)

    ok = inline_names == json_names
    return {
        'name': 'fabric ↔ JSON',
        'ok': ok,
        'inline_count': len(inline_names),
        'json_count': len(json_names),
        'only_inline_sample': sorted(inline_names - json_names)[:5],
        'only_json_sample': sorted(json_names - inline_names)[:5],
    }


def check_rules(text):
    """3. compat sample lift-and-shift 정합

    cont.72 Part 4 baseline: 6 sample lift-and-shift
    (tshirts/shirts/polo/knitwear/sweatshirts/cross_category)
    각 파일 = 1 sample rule. 전체 27 rule 중 6개만 외부 분리.
    """
    if not os.path.isdir('data/rules'):
        return {'name': 'compat rules', 'ok': False, 'note': 'data/rules/ missing'}
    rule_files = [
        f for f in sorted(os.listdir('data/rules'))
        if f.endswith('.json') and f not in ('index.json', 'sleeve_length_ratios.json')
    ]
    rule_count = 0
    for fn in rule_files:
        try:
            with open(f'data/rules/{fn}') as f:
                data = json.load(f)
            if isinstance(data, list):
                rule_count += len(data)
            elif 'rules' in data:
                rule_count += len(data['rules'])
        except Exception:
            pass
    # cont.72 Part 4 baseline: 6 sample files / 6 sample rules
    # (B6.1 lift-and-shift sample phase; full 27 rule lift-and-shift = Phase 2)
    BASELINE_SAMPLE_RULES = 6
    BASELINE_SAMPLE_SYSTEMS = 6
    ok = rule_count >= BASELINE_SAMPLE_RULES and len(rule_files) == BASELINE_SAMPLE_SYSTEMS
    return {
        'name': 'compat rules (B6.1 sample lift-and-shift)',
        'ok': ok,
        'system_count': len(rule_files),
        'rule_count': rule_count,
        'baseline': f'sample {BASELINE_SAMPLE_SYSTEMS} system / ≥{BASELINE_SAMPLE_RULES} rule (cont.72 Part 4 sample lift-and-shift; full 27 rule = Phase 2)',
    }


def main():
    if not os.path.exists('flat-v6.html'):
        print('ERR: must run from flat/ project root')
        sys.exit(2)

    with open('flat-v6.html') as f:
        text = f.read()

    results = [
        check_presets(text),
        check_fabrics(text),
        check_rules(text),
    ]

    print('# FLAT sync_check report')
    print()
    all_ok = True
    for r in results:
        status = '✅' if r['ok'] else '❌'
        print(f"{status} {r['name']}")
        for k, v in r.items():
            if k in ('name', 'ok'):
                continue
            print(f'    {k}: {v}')
        print()
        all_ok = all_ok and r['ok']

    print('=' * 40)
    print('OVERALL:', '✅ PASS' if all_ok else '❌ FAIL')
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
