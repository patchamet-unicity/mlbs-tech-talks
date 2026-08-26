# -*- coding: utf-8 -*-
"""
build-sprites.py -- ต้นทางของตัวละครพิกเซลใน talk นี้

ตัวละครวาดเป็น "กริดครึ่งซ้าย" (20 คอลัมน์) แล้ว mirror ให้เป็น 40 คอลัมน์
เสร็จแล้วเติมเส้นขอบอัตโนมัติ (ช่องว่างที่ติดกับตัวละครจะกลายเป็นสีเส้นขอบ)
เพราะงั้นแก้ทรงตัวละครให้แก้ที่ sp(...) ข้างล่าง ห้ามไปแก้ characters.js ตรงๆ

เวอร์ชันนี้วาดใหม่ทั้งชุด (2026-08-27) เทียบกับภาพอ้างอิง
talks/assets/_raw/image.png -- เป้าคือคล้าย ~80% ปรับให้เหมาะกับสไลด์

รัน:  python build-sprites.py
ได้:  characters.js  และ  preview.html
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
            if 0 <= y < H and 0 <= x < len(g[0]):
                g[y][x] = c


# ============================== คน ==============================
# หัวกลมโต ผมโดมมีช่องหน้าผาก ตาวงรีตั้ง เสื้อยืดดำแขนยาว ยีนส์
h = blank()
# ผม -- โดมกลม คลุมลงมาถึง row 13
sp(h, 2, 2, 16, 19, 'h'); sp(h, 3, 3, 13, 19, 'h'); sp(h, 4, 4, 11, 19, 'h')
sp(h, 5, 5, 10, 19, 'h'); sp(h, 6, 6, 9, 19, 'h'); sp(h, 7, 13, 8, 19, 'h')
sp(h, 2, 2, 16, 19, 'H'); sp(h, 3, 5, 13, 19, 'H')
sp(h, 12, 13, 8, 19, 'j')
# หน้า
sp(h, 14, 27, 9, 19, 's')
# ช่องหน้าผาก -- mirror แล้วได้ปลายผมแหลมกลางหน้าผากแบบภาพอ้างอิง
sp(h, 12, 13, 16, 18, 's')
sp(h, 14, 14, 16, 19, 'l')
# ล็อคผมข้างแก้ม
sp(h, 14, 19, 8, 9, 'h'); sp(h, 14, 18, 8, 8, 'j')
# หู
sp(h, 17, 21, 6, 8, 's'); sp(h, 18, 20, 6, 7, 'S')
# คิ้ว + ตาวงรีตั้ง 3x5 + ประกายตา
sp(h, 15, 15, 13, 16, 'j')
sp(h, 17, 21, 14, 16, 'e'); sp(h, 17, 17, 14, 14, 'w')
# แก้ม + ปากเล็กกลางหน้า
sp(h, 22, 23, 10, 12, 'p')
sp(h, 24, 24, 18, 19, 'm')
# คาง + ลบมุมกรามให้มน
sp(h, 27, 27, 11, 19, 'S')
sp(h, 26, 27, 9, 9, '.'); sp(h, 27, 27, 10, 10, '.')
# เสื้อยืดดำ + คอ
sp(h, 28, 38, 10, 19, 't'); sp(h, 28, 30, 10, 19, 'T'); sp(h, 37, 38, 10, 19, 'D')
sp(h, 28, 28, 16, 19, 'S')
# แขนแนบลำตัว + มือ
sp(h, 30, 36, 8, 9, 't'); sp(h, 30, 36, 8, 8, 'D')
sp(h, 37, 39, 8, 9, 's'); sp(h, 39, 39, 8, 9, 'S')
# ยีนส์ -- สะโพกแล้วแยกสองขา
sp(h, 39, 42, 10, 19, 'n'); sp(h, 39, 40, 10, 19, 'L')
sp(h, 43, 45, 11, 16, 'n'); sp(h, 45, 45, 11, 16, 'N')
# รองเท้า
sp(h, 46, 49, 10, 16, 'o'); sp(h, 46, 46, 10, 16, 'O'); sp(h, 49, 49, 10, 16, 'a')

# ============================== หุ่น ==============================
# กล่องขาวมุมมน เสาอากาศหมวกแดงกว้าง จอดำ ตาทองแท่งตั้ง ครีบข้าง ฐานจุก
b = blank()
# เสาอากาศ -- หมวกแดงทรง T กว้าง + ก้านเทา
sp(b, 0, 2, 15, 19, 'r'); sp(b, 0, 0, 15, 15, 'R'); sp(b, 2, 2, 15, 19, 'R')
sp(b, 3, 8, 18, 19, 'A'); sp(b, 3, 8, 18, 18, 'a')
# เคสมุมมน
sp(b, 9, 36, 8, 19, 'd')
sp(b, 9, 11, 10, 19, 'E'); sp(b, 12, 30, 8, 9, 'E')
sp(b, 34, 36, 8, 19, 'A')
sp(b, 9, 9, 8, 9, '.'); sp(b, 10, 10, 8, 8, '.')
sp(b, 36, 36, 8, 9, '.'); sp(b, 35, 35, 8, 8, '.')
# ครีบข้าง
sp(b, 16, 23, 5, 7, 'A'); sp(b, 16, 17, 5, 7, 'd'); sp(b, 22, 23, 5, 7, 'a')
# จอดำมุมมน (ขอบห่างเคสข้างละ 3)
sp(b, 14, 29, 11, 19, 'b'); sp(b, 14, 15, 11, 19, 'B')
sp(b, 14, 14, 11, 11, 'd'); sp(b, 29, 29, 11, 11, 'd')
# ตาทองแท่งตั้ง
sp(b, 18, 26, 14, 17, 'f'); sp(b, 18, 19, 14, 16, 'F'); sp(b, 18, 26, 14, 14, 'F')
# ฐานจุกใต้เคส
sp(b, 37, 40, 15, 19, 'A'); sp(b, 37, 37, 15, 19, 'd'); sp(b, 40, 40, 15, 19, 'a')


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


HUMAN_F = mirror(h)
ROBOT_F = mirror(b)


def copy(g):
    return [r[:] for r in g]


def flip(g):
    return [r[::-1] for r in g]


def shift_up(g):
    return [r[:] for r in g[1:]] + [['.'] * len(g[0])]


# ==================== ท่าหัน 3/4 (ตามแถวล่างของภาพอ้างอิง) ====================
# หัวหันแค่พอเห็นตาสองข้าง: เลื่อนตา/คิ้ว/ปาก/แก้มไปข้างที่หัน 2 ช่อง
# ตัวยังใช้ลำตัวหน้าตรง (มุมนี้ลำตัวต่างจากหน้าตรงน้อยมาก)
# วาดข้างเดียวพอ อีกข้างได้จาก flip

# landmark หลัง mirror (กว้าง 40): คิ้ว row15 cols13-16/23-26,
# ตา rows17-21 cols14-16/23-25, ปาก row24 cols18-21,
# แก้ม rows22-23 cols10-12/27-29, หู cols6-8/31-33


def human_34_right():
    g = copy(HUMAN_F)
    # ลบคิ้ว+ตาเดิม แล้ววาดใหม่เลื่อนขวา 2
    sp(g, 15, 21, 13, 26, 's')
    sp(g, 15, 15, 15, 18, 'j'); sp(g, 17, 21, 16, 18, 'e'); sp(g, 17, 17, 16, 16, 'w')
    sp(g, 15, 15, 25, 28, 'j'); sp(g, 17, 21, 25, 27, 'e'); sp(g, 17, 17, 25, 25, 'w')
    # ปากเลื่อนขวา 2
    sp(g, 24, 24, 18, 21, 's'); sp(g, 24, 24, 20, 23, 'm')
    # แก้มเลื่อนขวา 2
    sp(g, 22, 23, 10, 12, 's'); sp(g, 22, 23, 12, 14, 'p')
    sp(g, 22, 23, 27, 29, 's'); sp(g, 22, 23, 29, 30, 'p')
    # หูฝั่งหน้า (ขวา) หายเพราะหน้าหมุนไป -- เหลือหูฝั่งไกล
    sp(g, 17, 21, 31, 33, '.')
    return g


def human_34_stride():
    # เฟรมก้าวแบบแถวล่างภาพอ้างอิง: ขาหน้าก้าวไป ขาหลังถอยส้นยก
    g = human_34_right()
    sp(g, 43, 49, 6, 33, '.')  # ลบขา+รองเท้าท่ายืน (สะโพก rows39-42 คงไว้)
    sp(g, 43, 45, 24, 28, 'n'); sp(g, 45, 45, 24, 28, 'N')
    sp(g, 46, 49, 25, 31, 'o'); sp(g, 46, 46, 25, 31, 'O'); sp(g, 49, 49, 25, 31, 'a')
    sp(g, 43, 45, 10, 14, 'n'); sp(g, 43, 45, 10, 11, 'N')
    sp(g, 45, 48, 7, 14, 'o'); sp(g, 45, 45, 7, 14, 'O'); sp(g, 48, 48, 7, 14, 'a')
    return g


def robot_34_left():
    g = copy(ROBOT_F)
    # จอเลื่อนซ้าย 2 (งอกซ้าย ตัดขวา)
    sp(g, 14, 29, 9, 10, 'b'); sp(g, 14, 15, 9, 10, 'B'); sp(g, 14, 14, 9, 9, 'd')
    sp(g, 14, 29, 27, 28, 'd')
    # ตาเลื่อนซ้าย 2
    sp(g, 18, 26, 12, 25, 'b')
    sp(g, 18, 26, 12, 15, 'f'); sp(g, 18, 19, 12, 14, 'F'); sp(g, 18, 26, 12, 12, 'F')
    sp(g, 18, 26, 20, 23, 'f'); sp(g, 18, 19, 20, 22, 'F'); sp(g, 18, 26, 20, 20, 'F')
    return g


H34 = human_34_right()
H34_STRIDE = human_34_stride()
R34 = robot_34_left()

GRIDS = [
    ('human', HUMAN_F), ('human-right', H34), ('human-left', flip(H34)),
    ('robot', ROBOT_F), ('robot-left', R34), ('robot-right', flip(R34)),
]

# คน: หัวขยับแยกจากลำตัวเวลาหายใจ / หุ่น: ลอยทั้งตัว
HEAD_SPLIT = 28


def build(grid, kind):
    f = outline(grid)
    if kind == 'human':
        return dict(w=40, hgt=51, shadow=(20, 49.6, 11, 1.4),
                    parts=[('char-head', rects(f, 0, HEAD_SPLIT - 1)),
                           ('char-torso', rects(f, HEAD_SPLIT, H - 1))])
    return dict(w=40, hgt=51, shadow=(20, 49.2, 8.5, 1.3),
                parts=[('char-float', rects(f, 0, H - 1))])


def build_walk(fa, fb):
    # เดิน 2 เฟรมแบบ GB: ก้าว (stride) สลับกับผ่านตัว (ยืนยกตัวขึ้น 1px)
    return dict(w=40, hgt=51, shadow=(20, 49.6, 11, 1.4),
                parts=[('walk-a', rects(outline(fa), 0, H - 1)),
                       ('walk-b', rects(outline(fb), 0, H - 1))])


SPRITES = [(name, build(g, name.split('-')[0])) for name, g in GRIDS]
SPRITES += [
    ('human-right-walk', build_walk(H34_STRIDE, shift_up(H34))),
    ('human-left-walk', build_walk(flip(H34_STRIDE), flip(shift_up(H34)))),
]

LABEL = {
    'human': 'ตัวละครคน', 'human-right': 'ตัวละครคน หันขวา',
    'human-left': 'ตัวละครคน หันซ้าย',
    'human-right-walk': 'ตัวละครคน เดินไปทางขวา',
    'human-left-walk': 'ตัวละครคน เดินไปทางซ้าย',
    'robot': 'ตัวละคร AI', 'robot-left': 'ตัวละคร AI หันซ้าย',
    'robot-right': 'ตัวละคร AI หันขวา',
}


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
    "@keyframes walkStep{0%,49%{opacity:1}50%,100%{opacity:0}}"
    ".walk-a{animation:walkStep .38s linear infinite}"
    ".walk-b{animation:walkStep .38s linear infinite reverse}"
    "@media(prefers-reduced-motion:reduce){"
    ".char-head,.char-torso,.char-float{animation:none}"
    ".walk-a{animation:none;opacity:0}.walk-b{animation:none;opacity:1}}"
)

HERE = os.path.dirname(os.path.abspath(__file__))

js = [
    '// สร้างจาก build-sprites.py -- อย่าแก้ไฟล์นี้ตรงๆ',
    '// ใช้งาน: <script src="characters.js"></script> แล้ววาง <div data-char="human"></div>',
    '// ปรับขนาดด้วย CSS custom property --char-size (ค่าเริ่มต้น 180px)',
    '(function () {',
    '  var CSS = ' + repr(CSS) + ';',
    '  var SVG = {',
]
for name, s in SPRITES:
    js.append('    %s: %s,' % (repr(name), repr(svg(name, s))))
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
<div class="bar">หน้าตรง</div>
<div class="stage">%s%s</div>
<div class="bar">หันหน้าเข้าหากัน (human-right + robot-left)</div>
<div class="stage">%s%s</div>
<div class="bar">หันออก (human-left + robot-right)</div>
<div class="stage">%s%s</div>
<div class="bar">เดิน (human-right-walk + human-left-walk)</div>
<div class="stage">%s%s</div>
<div class="cap">ขนาดจริงบนสไลด์</div>
<div class="stage small">%s%s</div>
</body></html>
"""
SV = dict(SPRITES)


def _s(name):
    return svg(name, SV[name])


io.open(os.path.join(HERE, 'preview.html'), 'w', encoding='utf-8').write(
    PREVIEW % (CSS, _s('human'), _s('robot'),
               _s('human-right'), _s('robot-left'),
               _s('human-left'), _s('robot-right'),
               _s('human-right-walk'), _s('human-left-walk'),
               _s('human'), _s('robot')))

print('ok -- characters.js + preview.html')
