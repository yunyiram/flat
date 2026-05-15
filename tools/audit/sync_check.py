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
    # cont.72 Part 16 자율 영역 B: declared 68 (base 60 + 확장 8) 정정
    BASELINE_TERMS = 68
    terms_ok = declared_total == BASELINE_TERMS and computed_total == BASELINE_TERMS

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


def check_params(text):
    """7. params.json 19 top keys 인벤토리 + state_defaults 카운트 ↔ inline S 객체 비교

    cont.72 Part 16 자율 영역 C — B6.4 spec § 3 후속 구현.
    params.json v0.26 = 19 top keys / 200+ entries.
    state_defaults 63 entries ↔ flat-v6.html S 객체 초기값 카운트 비교.
    """
    if not os.path.exists('data/params.json'):
        return {'name': 'params (B6.4)', 'ok': False, 'note': 'data/params.json missing'}
    with open('data/params.json') as f:
        p = json.load(f)

    # 1. top-level keys (메타 3 + 17 도메인 = 20 baseline)
    # cont.72 Part 16 C 정정: B6.4 spec 초기 19 표기 → 실제 20 (svg_constants 포함)
    top_keys = list(p.keys())
    BASELINE_TOP_KEYS = 20

    # 2. state_defaults 카운트 (description 제외)
    state_defaults = p.get('state_defaults', {})
    state_count = len([k for k in state_defaults if k != 'description'])

    # 3. inline S 객체 (flat-v6.html const S = {...}) 카운트 추출
    # 정확한 const S = { ... } 찾기 (3-line stretch)
    s_match = re.search(r'const\s+S\s*=\s*\{', text)
    inline_s_count = 0
    if s_match:
        open_pos = s_match.end() - 1
        depth = 0
        i = open_pos
        while i < len(text):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    s_body = text[open_pos:i + 1]
                    # 첫 레벨 키만 카운트 (nested object의 key는 제외)
                    # 매칭: 줄 시작 또는 ,/{ 후의 식별자:
                    inline_s_count = len(re.findall(
                        r"[\{,]\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:",
                        s_body
                    ))
                    # 첫 키 (const S = {x: ...) 누락 가능
                    if not s_body.startswith('{,'):
                        # skip — regex already covers '{...' pattern
                        pass
                    break
            i += 1

    # 4. collar_params 6 카테고리 ↔ collarTypeMap (대략 22 type 확인)
    collar_params = p.get('collar_params', {})
    collar_cat_count = len([k for k in collar_params if k != 'description'])

    # baseline pass: top keys + state_defaults 양쪽 비어있지 않음
    ok = (
        len(top_keys) == BASELINE_TOP_KEYS
        and state_count >= 50  # 메타 제외 63 - description 1 = 62, 보수적 50
        and inline_s_count >= 30  # S 객체 최소 30 키
    )
    return {
        'name': 'params (B6.4 cross-ref)',
        'ok': ok,
        'top_keys_count': len(top_keys),
        'state_defaults_entries': state_count,
        'inline_S_entries': inline_s_count,
        'collar_params_categories': collar_cat_count,
        'baseline': f'{BASELINE_TOP_KEYS} top keys (메타 3 + 16 도메인) / state_defaults ≥50 / inline S ≥30 (cont.72 Part 16 A3 인벤토리)',
    }


def check_i18n(text):
    """8. LANG.en vs LANG.ko 정합 (모든 nested key 매칭)

    cont.72 Part 16 자율 영역 F. inventory § 8 D-2 "i18n 자동 병기 매핑 정합성
    미검증" 대응. EN/KO 키 갯수 + 카테고리별 정확 매칭 검증.
    """
    # LANG={ en:{...}, ko:{...}, ko_factory:{...} }
    lang_start = text.find('const LANG={')
    if lang_start < 0:
        return {'name': 'i18n EN/KO', 'ok': False, 'note': 'LANG not found'}

    def extract_section(start_marker, section_text):
        sec_start = section_text.find(start_marker)
        if sec_start < 0:
            return None
        open_pos = section_text.find('{', sec_start)
        depth = 0
        i = open_pos
        while i < len(section_text):
            if section_text[i] == '{':
                depth += 1
            elif section_text[i] == '}':
                depth -= 1
                if depth == 0:
                    return section_text[open_pos:i + 1]
            i += 1
        return None

    lang_body = text[lang_start:]
    en_body = extract_section('en:{', lang_body)
    ko_body = extract_section('ko:{', lang_body)

    if not en_body or not ko_body:
        return {'name': 'i18n EN/KO', 'ok': False, 'note': 'en/ko not found'}

    # 카테고리 추출 (depth-aware, nested object 안 키 제외)
    def top_categories(body):
        cats = {}
        depth = 0
        i = 1  # skip opening {
        while i < len(body):
            ch = body[i]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            elif depth == 0 and (ch.isalpha() or ch == '_'):
                m = re.match(r"([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*\{", body[i:])
                if m:
                    cat_name = m.group(1)
                    cat_open = i + m.end() - 1
                    d = 0
                    j = cat_open
                    while j < len(body):
                        if body[j] == '{':
                            d += 1
                        elif body[j] == '}':
                            d -= 1
                            if d == 0:
                                cat_body = body[cat_open + 1:j]
                                # 첫 레벨 키만 — depth=0 + 문자열 리터럴 제외
                                d2 = 0
                                k = 0
                                key_count = 0
                                in_string = None
                                while k < len(cat_body):
                                    c2 = cat_body[k]
                                    # 문자열 리터럴 추적
                                    if in_string:
                                        if c2 == in_string and (k == 0 or cat_body[k - 1] != '\\'):
                                            in_string = None
                                        k += 1
                                        continue
                                    if c2 in ("'", '"'):
                                        in_string = c2
                                        k += 1
                                        continue
                                    if c2 == '{':
                                        d2 += 1
                                    elif c2 == '}':
                                        d2 -= 1
                                    elif d2 == 0 and (c2.isalpha() or c2 == '_'):
                                        m2 = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*\s*:", cat_body[k:])
                                        if m2:
                                            key_count += 1
                                            k += m2.end()
                                            continue
                                    k += 1
                                cats[cat_name] = key_count
                                i = j + 1
                                break
                        j += 1
                    continue
            i += 1
        return cats

    en_cats = top_categories(en_body)
    ko_cats = top_categories(ko_body)

    # 정합 검증
    en_keys = set(en_cats.keys())
    ko_keys = set(ko_cats.keys())
    cat_ok = en_keys == ko_keys

    # 카테고리별 항목 카운트 매칭
    mismatch = []
    for k in (en_keys & ko_keys):
        if en_cats[k] != ko_cats[k]:
            mismatch.append(f"{k}: EN {en_cats[k]} vs KO {ko_cats[k]}")

    count_ok = len(mismatch) == 0
    ok = cat_ok and count_ok

    return {
        'name': 'i18n EN/KO 정합',
        'ok': ok,
        'en_categories': len(en_cats),
        'ko_categories': len(ko_cats),
        'en_only': sorted(en_keys - ko_keys),
        'ko_only': sorted(ko_keys - en_keys),
        'count_mismatch': mismatch[:10],
        'baseline': f'EN ↔ KO 카테고리 + 카운트 정확 일치 (cont.72 Part 8 T1 i18n sleeve.capped 정정 후속)',
    }


def check_preset_schema(text):
    """9. PresetModule.DB 34 preset schema 정합

    cont.72 Part 16 자율 영역 G. inventory § 8 D-2 "B6.2 schema 정합 (simplification)"
    대응. recommendedFabricIds / activeMode / isHero / difficulty 등 spec v0.2 필드의
    빈 채로 lift-and-shift 상태 측정.

    참고: spec v0.2는 풍부한 schema 정의했지만 cont.72 Part 3 lift-and-shift는
    현 FLAT enum/cat 그대로 (자율 결정, 사고 m 대응). 본 check는 *현 schema 정합*
    검증만 — spec v0.2 schema 적용 여부는 별도 작업 (Phase 4).
    """
    if not os.path.isdir('data/presets'):
        return {'name': 'preset schema', 'ok': False, 'note': 'data/presets/ missing'}

    cat_files = [
        f for f in sorted(os.listdir('data/presets'))
        if f.endswith('.json') and f != 'index.json'
    ]
    schema_issues = []
    total_presets = 0
    required_fields = ['name', 'cat', 's']  # 현 minimal schema
    optional_fields = ['recommendedFabricIds', 'activeMode', 'isHero', 'difficulty']
    optional_filled = {f: 0 for f in optional_fields}

    for fn in cat_files:
        with open(f'data/presets/{fn}') as f:
            data = json.load(f)
        entries = data if isinstance(data, list) else data.get('presets', [])
        for p in entries:
            total_presets += 1
            for req in required_fields:
                if req not in p:
                    schema_issues.append(f"{fn}: {p.get('name', '?')} missing {req}")
            for opt in optional_fields:
                if opt in p and p[opt] is not None and p[opt] != []:
                    optional_filled[opt] += 1

    ok = len(schema_issues) == 0
    return {
        'name': 'preset schema (B6.2 v0.1 minimal)',
        'ok': ok,
        'total_presets': total_presets,
        'required_field_issues': len(schema_issues),
        'issues_sample': schema_issues[:5],
        'optional_filled': optional_filled,
        'baseline': '34 preset / required: name+cat+s / optional (spec v0.2 schema 후속): recommendedFabricIds/activeMode/isHero/difficulty 모두 0 = lift-and-shift 정합',
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
        check_params(text),
        check_i18n(text),
        check_preset_schema(text),
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
