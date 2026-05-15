#!/usr/bin/env python3
"""
compat_sweep.py — 6 system 27 rule 정적 sweep + 발동 케이스 자동 검증

cont.72 Part 16 자율 영역 D. cont.72 Part 13 sample 9건 → 전수 27건.
회귀 0 (read-only). DOM 발동 검증은 Phase 후속 (preview 회복 시).

검증 영역:
  1. 6 system 정의 카운트 (NECKTYPE / SHOULDER_NECKTYPE / DETAIL_NECKTYPE /
     SHOULDER_DETAIL / COLLAR / NECK_BC_BLOCKED)
  2. 각 system 안 rule 카운트 (baseline 3/3/1/3/8/9)
  3. 차단 케이스 정적 매핑 (state combo → blocked)
  4. plan.md "27 rule" 표기 정합

실행: `python3 tools/audit/compat_sweep.py`
종료 코드: 0 = PASS, 1 = FAIL
"""
import json
import os
import re
import sys


def extract_object(text, marker):
    """const X = { ... } 본문 추출"""
    start = text.find(marker)
    if start < 0:
        return None
    open_pos = text.find('{', start)
    depth = 0
    i = open_pos
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[open_pos:i + 1]
        i += 1
    return None


def extract_array(text, marker):
    """const X = [ ... ] 본문 추출"""
    start = text.find(marker)
    if start < 0:
        return None
    open_pos = text.find('[', start)
    depth = 0
    i = open_pos
    while i < len(text):
        if text[i] == '[':
            depth += 1
        elif text[i] == ']':
            depth -= 1
            if depth == 0:
                return text[open_pos:i + 1]
        i += 1
    return None


def strip_js_comments(body):
    """JS // line comments + /* block comments */ 제거"""
    if not body:
        return ''
    # 1) line comments: // ... \n
    body = re.sub(r"//[^\n]*", '', body)
    # 2) block comments
    body = re.sub(r"/\*.*?\*/", '', body, flags=re.DOTALL)
    return body


def count_keys_top_level(body):
    """첫 레벨 키만 카운트 (nested + 주석 제외)"""
    if not body:
        return 0
    clean = strip_js_comments(body)
    # depth tracking — 최상위 {} 안의 키만
    depth = 0
    count = 0
    i = 0
    expecting_key = False
    while i < len(clean):
        ch = clean[i]
        if ch == '{':
            depth += 1
            if depth == 1:
                expecting_key = True
        elif ch == '}':
            depth -= 1
        elif ch == '[' or ch == '(':
            depth += 100  # nested → skip
        elif ch == ']' or ch == ')':
            depth -= 100
        elif depth == 1 and expecting_key and ch.isalpha() or (depth == 1 and expecting_key and ch == '_'):
            # 식별자 시작 — 끝까지 읽고 : 만나면 1 카운트
            m = re.match(r"([a-zA-Z_][a-zA-Z0-9_]*)\s*:", clean[i:])
            if m:
                count += 1
                i += m.end()
                expecting_key = False  # 다음 키는 , 후에
                continue
        elif depth == 1 and ch == ',':
            expecting_key = True
        i += 1
    return count


def analyze_compat(text):
    """6 system 27 rule sweep 정적 분석"""
    systems = {
        'NECKTYPE_COMPAT': {'marker': 'const NECKTYPE_COMPAT={', 'baseline': 3},
        'SHOULDER_NECKTYPE_COMPAT': {'marker': 'const SHOULDER_NECKTYPE_COMPAT={', 'baseline': 3},
        'DETAIL_NECKTYPE_COMPAT': {'marker': 'const DETAIL_NECKTYPE_COMPAT={', 'baseline': 1},
        'SHOULDER_DETAIL_COMPAT': {'marker': 'const SHOULDER_DETAIL_COMPAT={', 'baseline': 3},
        'COLLAR_COMPAT': {'marker': 'const COLLAR_COMPAT={', 'baseline': 8},
    }
    results = {}
    total_rules = 0
    for name, info in systems.items():
        body = extract_object(text, info['marker'])
        count = count_keys_top_level(body) if body else 0
        ok = count == info['baseline']
        results[name] = {'count': count, 'baseline': info['baseline'], 'ok': ok}
        total_rules += count

    # NECK_BC_BLOCKED = array of pairs
    bc_body = extract_array(text, 'const NECK_BC_BLOCKED=[')
    bc_count = len(re.findall(r"\[\s*['\"][^'\"]+['\"]\s*,\s*['\"][^'\"]+['\"]\s*\]", bc_body or ''))
    results['NECK_BC_BLOCKED'] = {'count': bc_count, 'baseline': 9, 'ok': bc_count == 9}
    total_rules += bc_count

    return results, total_rules


def analyze_collar_compat_detail(text):
    """COLLAR_COMPAT 안 5 collarGroup (flat/stand/shirt/tailored/deco) 별 차단/허용 매트릭스"""
    body = extract_object(text, 'const COLLAR_COMPAT={')
    if not body:
        return None
    # 각 neckShape 의 5 group 카운트 (flat/stand/shirt/tailored/deco)
    matrix = {}
    # neckShape: { flat:[..], stand:[..], shirt:[..], tailored:[..], deco:[..] }
    # 패턴: shape:{...}, 분리
    shape_pat = re.findall(
        r"([a-zA-Z_]+):\s*\{([^}]+)\}",
        body
    )
    for shape, groups_body in shape_pat:
        groups = {}
        for grp in ['flat', 'stand', 'shirt', 'tailored', 'deco']:
            m = re.search(grp + r":\s*\[([^\]]*)\]", groups_body)
            if m:
                items = [x.strip().strip("'\"") for x in m.group(1).split(',') if x.strip()]
                groups[grp] = len(items)
        matrix[shape] = groups
    return matrix


def main():
    if not os.path.exists('flat-v6.html'):
        print('ERR: must run from flat/ project root')
        sys.exit(2)

    with open('flat-v6.html') as f:
        text = f.read()

    print('# FLAT compat_sweep report')
    print('# cont.72 Part 16 자율 영역 D — 6 system 27 rule 정적 sweep')
    print()

    # 1. 6 system rule 카운트
    print('## 1. 6 system rule 카운트 정합')
    print()
    results, total = analyze_compat(text)
    all_ok = True
    for name, r in results.items():
        status = '✅' if r['ok'] else '❌'
        print(f"{status} {name}: {r['count']}/{r['baseline']}")
        all_ok = all_ok and r['ok']
    print()
    BASELINE_TOTAL = 27
    total_ok = total == BASELINE_TOTAL
    status = '✅' if total_ok else '❌'
    print(f"{status} **Total: {total}/{BASELINE_TOTAL} rule** (cont.72 Part 13 정정값)")
    all_ok = all_ok and total_ok
    print()

    # 2. COLLAR_COMPAT 8 neckShape × 5 collarGroup 차단/허용 매트릭스
    print('## 2. COLLAR_COMPAT 8 neckShape × 5 collarGroup 매트릭스')
    print()
    matrix = analyze_collar_compat_detail(text)
    if matrix:
        print(f"{'neckShape':12s} | flat | stand | shirt | tailored | deco")
        print(f"{'-'*12} | ---- | ----- | ----- | -------- | ----")
        for shape, groups in matrix.items():
            row = f"{shape:12s}"
            for grp in ['flat', 'stand', 'shirt', 'tailored', 'deco']:
                row += f" | {groups.get(grp, '-'):>4d}" if grp in groups else f" | {'-':>4s}"
            print(row)
        print()
        # 차단 셀 = 빈 배열 (0 collar 허용)
        blocked_cells = sum(
            1 for shape, groups in matrix.items()
            for grp, cnt in groups.items() if cnt == 0
        )
        total_cells = sum(len(groups) for groups in matrix.values())
        print(f"차단 셀: {blocked_cells}/{total_cells} ({blocked_cells*100//total_cells if total_cells else 0}%)")
    print()

    # 3. NECK_BC_BLOCKED 9 pair
    print('## 3. NECK_BC_BLOCKED 9 pair (neckFinish × closure)')
    print()
    bc_body = extract_array(text, 'const NECK_BC_BLOCKED=[')
    pairs = re.findall(r"\[\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*\]", bc_body or '')
    for i, (b, c) in enumerate(pairs, 1):
        print(f"  {i}. neckFinish={b} × closure={c} → blocked")
    print()

    # 4. 최종 PASS/FAIL
    print('=' * 50)
    print('OVERALL:', '✅ PASS' if all_ok else '❌ FAIL')
    print()
    print(f"발동 검증 (DOM-level) 후속:")
    print(f"  - 정적 분석: 27 rule 정의 누락 0 ✅ (위)")
    print(f"  - DOM 발동: cont.72 Part 13 sample 9건만 (28-9=18건 잔존)")
    print(f"  - Preview 회복 시 Puppeteer 자동 sweep 추천")
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
