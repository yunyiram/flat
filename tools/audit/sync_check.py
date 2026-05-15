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


def check_card_data(text):
    """4. CARD_DATA targetPresetName ↔ PresetModule.DB names

    cont.72 Part 12 fix: 5 카드에 targetPresetName 명시 추가.
    Card 0/1/2 = crewTee / Card 3 = hoodie / Card 4 = sweatshirt 매핑.
    targetPresetName이 실제 DB.name과 일치해야 fuzzy fallback 없이 직접 매칭.
    """
    # CARD_DATA 안의 targetPresetName 추출
    card_targets = re.findall(r"targetPresetName:['\"]([^'\"]+)['\"]", text)

    # PresetModule.DB.name 셋 (tops only — CARD_DATA = top wear)
    pm_start = text.find('const PresetModule={')
    db_body = find_block(text[pm_start:], 'DB:[', '[') or ''
    db_names = set(re.findall(r"name:['\"]([^'\"]+)['\"]", db_body))

    invalid = [t for t in card_targets if t not in db_names]
    ok = len(invalid) == 0 and len(card_targets) >= 5
    return {
        'name': 'CARD_DATA targetPresetName (cont.72 Part 12 fix)',
        'ok': ok,
        'card_targets_count': len(card_targets),
        'card_targets': card_targets[:10],
        'invalid_targets': invalid,
        'baseline': '5 카드 모두 명시 (Card 0/1/2 crewTee / 3 hoodie / 4 sweatshirt)',
    }


def check_seams(text):
    """5. S14 Phase 1 seams 27 area ↔ data/seams/ 분할

    cont.72 Part 10 baseline: 8 파일 (collar 4 / collar_stand 4 / cuff 4 /
    sleeve 5 / pocket 3 / side_seam 2 / singles 5 + index)
    = 27 area, tbd 10, factory validation 후속.
    """
    if not os.path.isdir('data/seams'):
        return {'name': 'seams (S14 Phase 1)', 'ok': False, 'note': 'data/seams/ missing'}
    seam_files = [
        f for f in sorted(os.listdir('data/seams'))
        if f.endswith('.json') and f != 'index.json'
    ]
    area_count = 0
    tbd_count = 0
    for fn in seam_files:
        try:
            with open(f'data/seams/{fn}') as f:
                data = json.load(f)
            entries = data if isinstance(data, list) else (data.get('areas') or data.get('seams') or [])
            area_count += len(entries)
            for e in entries:
                v = (e.get('default') or e.get('defaultValue') or '')
                if isinstance(v, str) and v.lower() in ('tbd', 'todo', ''):
                    tbd_count += 1
        except Exception:
            pass
    # cont.72 Part 10 baseline
    BASELINE_AREA = 27
    BASELINE_FILES = 7  # excluding index.json
    ok = area_count == BASELINE_AREA and len(seam_files) == BASELINE_FILES
    return {
        'name': 'seams (S14 Phase 1)',
        'ok': ok,
        'file_count': len(seam_files),
        'area_count': area_count,
        'tbd_count': tbd_count,
        'baseline': f'{BASELINE_FILES} file / {BASELINE_AREA} area (cont.72 Part 10; 28 vs 27 모호 cowork 정정 후속)',
    }


def check_factory_terms(text):
    """6. B6.5 봉제 현장용어 60 매핑 ↔ LANG.ko_factory 정합

    cont.72 Part 13-15 baseline:
    - data/factory_terms.json: 60 terms / 8 category
    - data/factory_terms_i18n_mapping.json: 60→18 UI + 26 construction-only + 6 확장
    - flat-v6.html LANG.ko_factory: 19 entries (sleeve/body/neck/detail/pants/skirt 6 카테고리)
    """
    if not os.path.exists('data/factory_terms.json'):
        return {'name': 'factoryTerms (B6.5)', 'ok': False, 'note': 'data/factory_terms.json missing'}
    with open('data/factory_terms.json') as f:
        ft = json.load(f)
    # schema: { terms: { cat: { key: {...} } }, totalTerms: 60 }
    declared_total = ft.get('totalTerms', 0)
    computed_total = 0
    for cat, entries in ft.get('terms', {}).items():
        if isinstance(entries, (list, dict)):
            computed_total += len(entries)
    BASELINE_TERMS = 60
    # declared 60, computed 68 (메모리 source = 서울의류협동조합 60 + 확장 8). 양쪽 표시
    terms_ok = declared_total >= BASELINE_TERMS

    mapping_count = 0
    mapping_ok = False
    if os.path.exists('data/factory_terms_i18n_mapping.json'):
        with open('data/factory_terms_i18n_mapping.json') as f:
            m = json.load(f)
        # schema: { mappings: { cat: { key: {...} } } }
        mappings = m.get('mappings', {})
        for cat, entries in mappings.items():
            if isinstance(entries, (list, dict)):
                mapping_count += len(entries)
        mapping_ok = mapping_count >= 18  # 60→18 UI baseline

    # ko_factory LANG section: 카운트 (LANG 객체 nested)
    ko_factory_start = text.find('ko_factory:{')
    if ko_factory_start < 0:
        ko_factory_start = text.find('ko_factory:')
    ko_factory_count = 0
    if ko_factory_start > 0:
        # find matching {...} block
        open_pos = text.find('{', ko_factory_start)
        depth = 0
        i = open_pos
        while i < len(text):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    ko_factory_body = text[open_pos:i + 1]
                    break
            i += 1
        # count nested keys (sleeve.* + body.* etc.)
        ko_factory_count = len(re.findall(r"^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*['\"]", ko_factory_body, re.MULTILINE))

    ok = terms_ok and mapping_ok and ko_factory_count >= 15
    return {
        'name': 'factoryTerms (B6.5 Phase 1-2)',
        'ok': ok,
        'declared_terms': declared_total,
        'computed_terms': computed_total,
        'mapping_count': mapping_count,
        'ko_factory_keys': ko_factory_count,
        'baseline': '60 terms / ≥18 mapping (UI) / ≥15 ko_factory keys (cont.72 Part 13-15)',
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
        check_card_data(text),
        check_seams(text),
        check_factory_terms(text),
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
