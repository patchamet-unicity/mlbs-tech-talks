# Slide 10 — Level Complete

สไลด์ปิดของ talk ใช้ภาพ callback กลับไปหา `01-title.html` และ
`02-levels.html` หลังจาก Slide 09 ที่มีรายละเอียด 70 beats จบลงแล้ว

## เป้าหมาย

- ให้คนดูพักสายตาหลัง workflow ที่หนาแน่น
- ปิดวงกลับไปหาแกน `Level Up How You Use AI`
- ทิ้งคำถามให้คนดูนึกถึงงานของตัวเองแทนการสรุปเนื้อหาซ้ำ

## Beat

มี 3 beats:

1. **LEVEL COMPLETE** — กรอบแบบหน้าเปิดเลื่อนลง คนเดินและหุ่นลอยมาหยุดที่
   ธงเส้นชัย ใช้พื้นที่ว่างมากเพื่อเปลี่ยนจังหวะจาก Slide 09
2. **4 levels callback** — ธงหาย บันได `Chat`, `Prompt Engineer`,
   `Context Engineer`, `Agent Harness` กลับมาเหมือน Slide 02; คนกระโดดขึ้น
   ขั้น 04 และหุ่นลอยขึ้นข้างกัน
3. **Closing question** — บันไดลด opacity เป็นฉากหลัง กรอบเปลี่ยนเป็นชื่อ talk
   และคำถาม `งานชิ้นไหนของคุณ พร้อมขยับขึ้นอีกหนึ่งระดับ?`; `Q&A ▼`
   กะพริบแทนสัญญาณรอคลิก

## Visual rules

- เวที 1280×720 และใช้สี/ฟอนต์จาก `theme.css`
- ใช้กรอบ title แบบเดียวกับ Slide 01
- บันไดใช้ตำแหน่งและสัดส่วนเดียวกับ Slide 02
- ใช้ `--accent` เฉพาะเลข `04`
- ไม่มี recap cards หรือข้อความสรุปเพิ่มเติม
- ตัวละครใช้ sprite เดิมจาก `characters.js`; คนเดินเข้าฉากเฉพาะ Beat 1
- รองรับ back, reset, AUTO, iframe postMessage และ reduced motion

## Navigation

- `PREV = "09-inbox-to-ticket.html"`
- `NEXT = ""` เพราะเป็นสไลด์สุดท้าย
- Slide 09 เชื่อม `NEXT = "10-level-complete.html"`

## Verification

- inline JavaScript syntax และ `git diff --check` ผ่าน
- headless Chrome ผ่านครบ 3 beats ที่ viewport 1280×720
- ตรวจ back, reset, element overflow และ runtime errors แล้ว
- inspect screenshot ของ Beat 1–3 แล้ว ไม่มีการชนกันของกรอบ บันได ตัวละคร
  หรือ controls
