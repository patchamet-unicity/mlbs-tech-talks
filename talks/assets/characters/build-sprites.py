# -*- coding: utf-8 -*-
"""
build-sprites.py -- ต้นทางของตัวละครพิกเซลใน talk นี้

ตัวละครวาดเป็น "กริดครึ่งซ้าย" (20 คอลัมน์) แล้ว mirror ให้เป็น 40 คอลัมน์
เสร็จแล้วเติมเส้นขอบอัตโนมัติ (ช่องว่างที่ติดกับตัวละครจะกลายเป็นสีเส้นขอบ)
เพราะงั้นแก้ทรงตัวละครให้แก้ที่ sp(...) ข้างล่าง ห้ามไปแก้ characters.js ตรงๆ

รัน:  python build-sprites.py
ได้:  ../characters.js  และ  preview.html
"""
import io
import os

HW, H = 20, 51

PAL = {
    'k': '#2B322D', 'H': '#6E7869', 'h': '#4A524A', 'j': '#363D37',
    's': '#F0B394', 'l': '#F8C9AC', 'S': '#D4906F', 'w': '#FFF6E2',
    'e': '#252B26', 'm': '#B87A52', 'p': '#E39AA0',
    't': '#3A423C', 'T': '#4C564D', 'D': '#2A312C',
    'n': '#8794A6', 'N': '#6E7B8C', 'L': '#9BA7B6',
    'o': '#2E352F', 'O': '#464E47',
    'A': '#ABB0AB', 'd': '#D9DCD7', 'E': '#ECEEEA', 'a': '#9AA199',
    'b': '#333B35', 'B': '#414A42', 'f': '#F2DC9A', 'F': '#FBEDBE',
    'r': '#E8586B', 'R': '#C4485A',
}


def blank():
    return [['.'] * HW for _ in range(H)]


def sp(g, y0, y1, x0, x1, c):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if 0 <= y < H and 0 <= x < HW:
                g[y][x] = c


# ============================== คน ==============================
h = blank()
# ผม -- ทรงปกหน้าผาก เทาดำ 3 เฉด
# ยอดหัวไล่ทีละขั้น 4 ขั้น ให้กะโหลกโค้ง ไม่เป็นกล่องเหลี่ยม
sp(h, 3, 3, 15, 19, 'h'); sp(h, 4, 4, 13, 19, 'h'); sp(h, 5, 5, 11, 19, 'h')
sp(h, 6, 6, 10, 19, 'h'); sp(h, 7, 11, 9, 19, 'h')
sp(h, 3, 3, 15, 19, 'H'); sp(h, 4, 6, 13, 19, 'H')
sp(h, 10, 11, 9, 19, 'j')
# หน้า
sp(h, 12, 27, 9, 19, 's')
sp(h, 12, 15, 17, 19, 'l')
# จอนสองข้าง
sp(h, 12, 19, 9, 11, 'h'); sp(h, 12, 17, 9, 10, 'j'); sp(h, 18, 19, 11, 11, 'j')
# ปอยผมหน้าผาก
sp(h, 12, 13, 13, 16, 'h'); sp(h, 12, 12, 17, 19, 'j')
# หู
sp(h, 17, 22, 7, 8, 's'); sp(h, 18, 21, 7, 7, 'S')
# ตา + คิ้ว -- 8x5 -> 5x4 -> 3x3 -> 4x4 (ทรงจัตุรัสเท่าเดิม แค่ขยับใหญ่ขึ้นขั้นนึง)
sp(h, 18, 21, 14, 17, 'e')
sp(h, 18, 18, 14, 14, 'w')
sp(h, 16, 16, 14, 17, 'j')
# แก้ม ปาก คาง
sp(h, 22, 23, 9, 11, 'p')
sp(h, 25, 26, 18, 19, 'm')
sp(h, 27, 27, 11, 19, 'S')
# ลบมุมกรามทิ้ง ให้คางมนรับกับกะโหลก
sp(h, 26, 27, 9, 9, '.'); sp(h, 27, 27, 10, 10, '.')
# เสื้อยืดดำ + คอ
sp(h, 28, 39, 12, 19, 't'); sp(h, 28, 29, 12, 15, 'T'); sp(h, 30, 31, 12, 19, 'T')
sp(h, 38, 39, 12, 19, 'D')
sp(h, 28, 31, 16, 19, 'D')
sp(h, 28, 29, 16, 19, 'S')
# แขน + มือ
sp(h, 30, 37, 8, 11, 't'); sp(h, 30, 31, 8, 11, 'T'); sp(h, 36, 37, 8, 11, 'D')
sp(h, 38, 41, 8, 11, 's'); sp(h, 40, 41, 8, 11, 'S')
# ยีนส์
sp(h, 40, 43, 12, 19, 'n'); sp(h, 40, 41, 12, 15, 'L')
sp(h, 40, 43, 18, 19, 'N')
sp(h, 44, 45, 13, 17, 'n'); sp(h, 45, 45, 13, 17, 'N')
# รองเท้า
sp(h, 46, 49, 11, 17, 'o'); sp(h, 46, 46, 11, 17, 'O'); sp(h, 49, 49, 11, 17, 'a')

# ============================== หุ่น ==============================
b = blank()
# เสาอากาศ
sp(b, 0, 2, 16, 19, 'r'); sp(b, 0, 0, 16, 19, 'R'); sp(b, 1, 1, 16, 17, 'R')
sp(b, 3, 8, 18, 19, 'A'); sp(b, 3, 8, 18, 18, 'a')
# เคส
sp(b, 9, 10, 12, 19, 'A')
sp(b, 11, 36, 8, 19, 'd')
sp(b, 11, 13, 8, 19, 'E'); sp(b, 11, 36, 8, 9, 'E')
sp(b, 35, 36, 8, 19, 'A')
# ครีบข้าง
sp(b, 19, 26, 4, 7, 'A'); sp(b, 19, 20, 4, 7, 'd'); sp(b, 25, 26, 4, 7, 'a')
# จอ
sp(b, 15, 30, 10, 19, 'b')
sp(b, 15, 16, 10, 19, 'B'); sp(b, 21, 21, 10, 19, 'B')
# ตา -- ถอยออกจากกลางจอ ให้ระยะห่างระหว่างลูกตากว้างขึ้นจาก 2 เป็น 6 ช่อง
sp(b, 19, 26, 12, 16, 'f'); sp(b, 19, 20, 12, 15, 'F'); sp(b, 19, 26, 12, 12, 'F')
# แถบปาก + ฐาน
sp(b, 33, 34, 14, 19, 'A')
sp(b, 38, 40, 12, 19, 'A'); sp(b, 38, 38, 12, 19, 'd')


# ============================== ประกอบ ==============================
def mirror(g):
    return [r + r[::-1] for r in g]


def outline(f):
    W = len(f[0])
    o = [r[:] for r in f]
    for y in range(H):
        for x in range(W):
            if f[y][x] != '.':
                continue
            if any(0 <= y + dy < H and 0 <= x + dx < W and f[y + dy][x + dx] != '.'
                   for dy in (-1, 0, 1) for dx in (-1, 0, 1)):
                o[y][x] = 'k'
    return o


def rects(f, y0, y1):
    W = len(f[0])
    out = []
    for y in range(y0, y1 + 1):
        row = f[y]
        x = 0
        while x < W:
            c = row[x]
            if c == '.':
                x += 1
                continue
            n = x
            while n < W and row[n] == c:
                n += 1
            out.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>'
                       % (x, y, n - x, PAL[c]))
            x = n
    return ''.join(out)


HUMAN = outline(mirror(h))
ROBOT = outline(mirror(b))

# คน: หัวขยับแยกจากลำตัวเวลาหายใจ / หุ่น: ลอยทั้งตัว
HEAD_SPLIT = 28
SPRITES = [
    ('human', dict(w=40, hgt=51, shadow=(20, 49.6, 11, 1.4),
                   parts=[('char-head', rects(HUMAN, 0, HEAD_SPLIT - 1)),
                          ('char-torso', rects(HUMAN, HEAD_SPLIT, H - 1))])),
    ('robot', dict(w=40, hgt=51, shadow=(20, 49.2, 8.5, 1.3),
                   parts=[('char-float', rects(ROBOT, 0, H - 1))])),
]

LABEL = {'human': 'ตัวละครคน', 'robot': 'ตัวละคร AI'}


def svg(name, s):
    cx, cy, rx, ry = s['shadow']
    body = ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#38403A" opacity="0.13"/>'
            % (cx, cy, rx, ry))
    for cls, r in s['parts']:
        body += '<g class="%s">%s</g>' % (cls, r)
    return ('<svg viewBox="0 0 %d %d" class="char char-%s" shape-rendering="crispEdges" '
            'role="img" aria-label="%s">%s</svg>' % (s['w'], s['hgt'], name, LABEL[name], body))


CSS = (
    "@keyframes charBob{0%,100%{transform:translateY(0)}50%{transform:translateY(0.5px)}}"
    "@keyframes charSquash{0%,100%{transform:scaleY(1)}50%{transform:scaleY(0.982)}}"
    "@keyframes charFloat{0%,100%{transform:translateY(-1.1px)}50%{transform:translateY(1.1px)}}"
    ".char{height:var(--char-size,180px);width:auto;display:block}"
    ".char-head{animation:charBob 2.6s ease-in-out infinite}"
    ".char-torso{animation:charSquash 2.6s ease-in-out infinite;"
    "transform-origin:50% 100%;transform-box:fill-box}"
    ".char-float{animation:charFloat 3.1s ease-in-out infinite}"
    "@media(prefers-reduced-motion:reduce){"
    ".char-head,.char-torso,.char-float{animation:none}}"
)

HERE = os.path.dirname(os.path.abspath(__file__))

js = [
    '// สร้างจาก sprites/build-sprites.py -- อย่าแก้ไฟล์นี้ตรงๆ',
    '// ใช้งาน: <script src="characters.js"></script> แล้ววาง <div data-char="human"></div>',
    '// ปรับขนาดด้วย CSS custom property --char-size (ค่าเริ่มต้น 180px)',
    '(function () {',
    '  var CSS = ' + repr(CSS) + ';',
    '  var SVG = {',
]
for name, s in SPRITES:
    js.append('    %s: %s,' % (name, repr(svg(name, s))))
js += [
    '  };',
    '  var st = document.createElement("style");',
    '  st.textContent = CSS;',
    '  document.head.appendChild(st);',
    '  function hydrate(root) {',
    '    (root || document).querySelectorAll("[data-char]").forEach(function (el) {',
    '      var s = SVG[el.getAttribute("data-char")];',
    '      if (s) el.innerHTML = s;',
    '    });',
    '  }',
    '  window.Characters = { svg: SVG, hydrate: hydrate };',
    '  if (document.readyState === "loading") {',
    '    document.addEventListener("DOMContentLoaded", function () { hydrate(); });',
    '  } else {',
    '    hydrate();',
    '  }',
    '})();',
    '',
]
io.open(os.path.join(HERE, 'characters.js'), 'w', encoding='utf-8').write('\n'.join(js))

PREVIEW = u"""<!doctype html>
<html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ตัวละคร -- Level Up How You Use AI</title>
<style>
%s
:root{--ground:#E4EBD9;--sign:#ABB0AB;--ink:#38403A;--ink-soft:#6B7568;--ash:#A9B2A8}
body{margin:0;background:var(--ground);color:var(--ink);
font-family:"Kanit","Segoe UI",system-ui,sans-serif}
.bar{background:var(--sign);border-bottom:2px solid var(--ink);padding:14px 28px;font-size:20px}
.stage{display:flex;align-items:flex-end;justify-content:center;gap:110px;padding:56px 0}
.small{gap:52px;padding:26px 0}
.small .char{--char-size:96px}
.cap{padding:12px 28px;font-size:14px;color:var(--ink-soft);border-top:1px solid var(--ash)}
</style></head><body>
<div class="bar">ระดับ 1 — chat</div>
<div class="stage">%s%s</div>
<div class="cap">ขนาดจริงบนสไลด์</div>
<div class="stage small">%s%s</div>
</body></html>
"""
hs = svg('human', SPRITES[0][1])
rs = svg('robot', SPRITES[1][1])
io.open(os.path.join(HERE, 'preview.html'), 'w', encoding='utf-8').write(
    PREVIEW % (CSS, hs, rs, hs, rs))

print('ok -- characters.js + preview.html')
