#!/usr/bin/env python3
"""
FLAT 실측 검수 스크립트 — 기획탭 DOM 검증용.

Claude 기획탭 세션 내 bash_tool로 실행.
배경: cont.62 "underarm dashed 제거 완료" 보고가 실제 DOM과 불일치 (2026-04-21).
기획탭이 DOM 레벨에서 bbox/path 좌표로 직접 측정.

검증된 경로:
- ?demo URL은 Shirt state로 시작하는 버그 (사용 금지)
- 올바른 진입: 카드 피드 → Crew Tee 카드 → CardFeed.pickVariant(0)
  → setMode('panel') → state 조작 → setMode('direct')

사용법: python3 inspect_flat.py [preset] [sleeve]
  - preset: crew (기본)
  - sleeve: short | long

결과 (Claude 컴퓨터 /home/claude/):
  {preset}_{sleeve}_front.png / _back.png / _full.png / _Lsleeve.png / _Rsleeve.png
  stdout: 모든 dashed 요소 좌표

2026-04-21 기획탭 cont.64 최초 작성.
"""

import sys
import re
from playwright.sync_api import sync_playwright

CHROME_PATH = "/home/claude/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome"
FLAT_URL = "https://yunyiram.github.io/flat/flat-v6.html"


def enter_crew_tee(page):
    page.goto(FLAT_URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(2500)
    page.evaluate("document.querySelector('.card[data-card=\"0\"] .card-enter-btn').click()")
    page.wait_for_timeout(1500)
    page.evaluate("CardFeed.pickVariant(0)")
    page.wait_for_timeout(1500)
    page.evaluate("setMode('panel')")
    page.wait_for_timeout(400)


def set_state(page, **kwargs):
    parts = []
    for k, v in kwargs.items():
        if isinstance(v, str):
            parts.append(f"S.{k}={v!r}")
        else:
            parts.append(f"S.{k}={v}")
    js = ";".join(parts)
    page.evaluate(f"{js}; if(typeof showHandles!=='undefined')showHandles=false; draw();")
    page.wait_for_timeout(500)


def dump_dashed(page):
    return page.evaluate("""
    () => Array.from(document.getElementById('svgF').querySelectorAll('[stroke-dasharray]'))
        .map(p => ({
            tag: p.tagName,
            x1: p.getAttribute('x1'), y1: p.getAttribute('y1'),
            x2: p.getAttribute('x2'), y2: p.getAttribute('y2'),
            d: (p.getAttribute('d') || '').slice(0, 120),
            dash: p.getAttribute('stroke-dasharray')
        }));
    """)


def capture_zooms(page, prefix, zooms):
    page.locator('#svgF').screenshot(path=f"/home/claude/{prefix}_front.png")
    page.locator('#svgB').screenshot(path=f"/home/claude/{prefix}_back.png")

    svg_raw = page.evaluate("""
        () => document.getElementById('svgF').outerHTML
            .replace(/var\\(--gfill\\)/g, 'white')
            .replace(/var\\(--gstroke\\)/g, '#1A1A1A')
            .replace(/var\\(--stitch\\)/g, '#666')
    """)
    clean = re.sub(r'<text[^>]*>[\s\S]*?</text>', '', svg_raw)
    m = re.search(r'<svg[^>]*>(.*)</svg>', clean, re.DOTALL)
    if not m:
        return
    inner = m.group(1)
    for label, vb, suffix in zooms:
        zp = page.context.new_page()
        html = (
            '<!DOCTYPE html><html><body style="margin:0;padding:30px;background:#fafafa;font-family:sans-serif;">'
            f'<div style="font-size:14px;color:#555;margin-bottom:8px;">{label}</div>'
            f'<svg viewBox="{vb}" style="width:1500px;height:1500px;background:white;border:1px solid #ccc;" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'
            '</body></html>'
        )
        zp.set_content(html)
        zp.wait_for_timeout(300)
        zp.screenshot(path=f"/home/claude/{prefix}_{suffix}.png", full_page=False)
        zp.close()


def main():
    preset = sys.argv[1] if len(sys.argv) > 1 else "crew"
    sleeve = sys.argv[2] if len(sys.argv) > 2 else "short"

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        ctx = browser.new_context(viewport={"width": 2400, "height": 1600}, device_scale_factor=3)
        page = ctx.new_page()
        enter_crew_tee(page)
        if sleeve == "long":
            set_state(page, sleeveLen='long', sleeveLength=95, sleeveCuff='plain',
                      neckFinish='rib', closure='none', pocket='none')
        page.evaluate("""
            setMode('direct');
            document.querySelectorAll('.reset-btn,#resetBtn,#canvasHint').forEach(b => {
                if (b) b.style.display = 'none';
            });
        """)
        page.wait_for_timeout(500)
        dashed = dump_dashed(page)
        print(f"=== {preset} {sleeve} — dashed ({len(dashed)}) ===")
        for i, d in enumerate(dashed):
            if d['x1']:
                print(f"  #{i} {d['tag']} ({d['x1']},{d['y1']}) -> ({d['x2']},{d['y2']}) dash={d['dash']}")
            else:
                print(f"  #{i} {d['tag']} d={d['d']}")
        prefix = f"{preset}_{sleeve}"
        capture_zooms(page, prefix, [
            ("Full clean", "0 0 320 460", "full"),
            ("Left sleeve end", "0 98 90 100", "Lsleeve"),
            ("Right sleeve end", "230 98 90 100", "Rsleeve"),
        ])
        print(f"\n/home/claude/{prefix}_*.png")
        browser.close()


if __name__ == "__main__":
    main()
