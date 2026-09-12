# เอกสารประกอบสไลด์ — 2026-09 "Level Up How You Use AI"

โฟลเดอร์นี้เก็บเอกสารอธิบายสไลด์ **ไฟล์ละหนึ่งสไลด์** เขียนไว้ให้ AI ตัวอื่น
(หรือตัวเราเองในอีกสามเดือน) อ่านแล้วเข้าใจสไลด์ได้เร็วโดยไม่ต้องไล่โค้ดทั้งไฟล์

| ไฟล์ | สไลด์ |
| --- | --- |
| [01-title.md](01-title.md) | `../01-title.html` — หน้าจอเปิดเกมสไตล์ GBC |
| [02-levels.md](02-levels.md) | `../02-levels.html` — บันได 4 ระดับ |
| [03-chat.md](03-chat.md) | `../03-chat.html` — บทสนทนา IT support 9 ข้อความ ระดับ 01 Chat |
| [04-prompt.md](04-prompt.md) | `../04-prompt.html` — ยุบ 9 ข้อความเป็นพรอมต์เดียว ระดับ 02 Prompt |
| [05-context.md](05-context.md) | `../05-context.html` — ยกของที่ซ้ำไปไว้ในไฟล์เดียว ระดับ 03 Context |
| [06-context-files.md](06-context-files.md) | `../06-context-files.html` — Context ที่ประกอบจากหลายไฟล์ |
| [07-agent.md](07-agent.md) | `../07-agent.html` — Intro เข้า Agent Harness |
| [08-agent.md](08-agent.md) | `../08-agent.html` — เขาวงกตก่อนและหลังมี Agent Harness |
| [09-inbox-to-ticket.md](09-inbox-to-ticket.md) | `../09-inbox-to-ticket.html` — Inbox-to-Ticket Harness; INTAKE prototype 10 beats |

## สิ่งที่ใช้ร่วมกันทุกสไลด์ (อ่านก่อน)

### 1. เวทีขนาดคงที่ 1280×720

ทุกสไลด์วาดบน `.stage` ขนาด **1280×720 px ตายตัว** แล้วย่อ/ขยายให้พอดีจอด้วย
`transform: scale(var(--stage-scale))` ที่ JS คำนวณจาก `min(vw/1280, vh/720)`

> **ตัวเลขทุกตัวในสไลด์เป็น px ของเวที ไม่ใช่ px ของจอจริง** ฉายจอไหนก็ได้สัดส่วนเดิม
> อย่าเปลี่ยนไปใช้ `vw`/`vh`/`%` เพราะจะพังสัดส่วนกับตัวละครที่เป็น pixel art

### 2. ระบบ beat (คุมด้วยคลิก ไม่ใช่ timeline อัตโนมัติ)

สไลด์เล่นเป็น **cutscene ทีละจังหวะ** เหมือน animation step ใน PowerPoint
คลิก / `Space` / `→` / `Enter` = เดินหน้าหนึ่ง beat, จบ beat สุดท้ายแล้วกดอีกที = ไปสไลด์ถัดไป

| การกด | ผล |
| --- | --- |
| คลิก / `Space` / `→` / `Enter` / `PageDown` | เดินหน้า 1 beat (beat สุดท้าย → สไลด์ถัดไป) |
| `←` / `PageUp` | ถอย 1 beat — **ถอยจนสุดแล้วค่อยข้ามไปสไลด์ก่อนหน้า** |
| `R` | เริ่มสไลด์นี้ใหม่ตั้งแต่ beat 1 |

**ปุ่มมุมล่างขวา** `◀ ▶ ▪▪□□ ↺ AUTO` — ไม่มีกรอบ เป็นกลิฟจาง `opacity .28`
ชัดตอน hover, pips บอกว่าอยู่ beat ไหน, `AUTO` เป็น toggle เดินหน้า beat เองตาม
`AUTO_HOLD[beat]` (ms) ตอนเปิดจะขีดเส้นใต้

`.controls` มี `stopPropagation` บน click อยู่ — กดปุ่มแล้วจะไม่ไปโดน
handler "คลิกที่ไหนก็ได้ = เดินหน้า" ซ้ำ

### 3. โหมดฝังใน iframe

ถ้าสไลด์ถูกเปิดใน iframe (`window.parent !== window`) การเปลี่ยนสไลด์จะ
**ไม่ navigate เอง** แต่ยิง `postMessage({ type: "slide:next" | "slide:prev", from: "<ชื่อสไลด์>" })`
ให้หน้ารวมสไลด์จัดการแทน — หน้ารวมยังไม่ได้ทำ แต่โค้ดฝั่งสไลด์รองรับไว้แล้ว
เปิดเดี่ยวๆ จะ `location.href = NEXT/PREV` ตามปกติ

### 4. ธีมสี

ทุกสีมาจาก [`../theme.css`](../theme.css) **ห้าม hardcode hex ในไฟล์สไลด์**
กติกาเดิมคือ `--accent` (แดง `#E8586B`) ใช้เน้นได้จุดเดียวต่อสไลด์
— ตอนนี้ผ่อนปรนแล้ว ใช้ตามหน้างานได้ แต่ยังควรจำกัดไว้จุดเดียวเพราะเป็นสีสดสีเดียวในพาเลตต์

### 5. ตัวละคร

```html
<script src="../../assets/characters/characters.js"></script>
<div data-char="human-right"></div>
```

- `characters.js` เป็น **ไฟล์ที่ generate ออกมา ห้ามแก้มือ** — แก้ที่
  `talks/assets/characters/build-sprites.py` แล้วรัน `python build-sprites.py`
- sprite ที่มี: `human` `human-right` `human-left` `human-right-walk`
  `human-left-walk` `robot` `robot-left` `robot-right`
- ขนาดคุมด้วย `--char-size` (ค่า default 180px) อัตราส่วนสไปรต์คือ **40:51**
  ดังนั้น `ความกว้าง = --char-size * 40 / 51`
- **ห้ามหันหัวมากกว่าท่า 3/4 ปัจจุบัน** — เคยลองแล้วพังสองรอบ
  (รายละเอียดใน `../../HANDOFF.md`)

### 6. `prefers-reduced-motion`

ทุกสไลด์มี media query ปิดอนิเมชัน/transition/micro loop ทั้งหมด
แล้วแสดงเป็นภาพนิ่งท่าสุดท้าย **ถ้าเพิ่มอนิเมชันใหม่ต้องไปเพิ่มในบล็อกนั้นด้วย**

### 7. เปิดดูตอนพัฒนา

ต้องเสิร์ฟผ่าน http เพราะ `characters.js` เป็น relative path — เปิดไฟล์ตรงๆ
ด้วย `file://` จะไม่มีตัวละคร

```bash
python -m http.server 8777
```

แล้วเปิด `http://localhost:8777/talks/2026-09-ai-usage-levels/slides/01-title.html`
(จาก repo root ใช้ `python -m http.server 8777`)
