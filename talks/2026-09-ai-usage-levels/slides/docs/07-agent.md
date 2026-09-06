# Slide 07 — Agent Harness intro

## Purpose

สไลด์คั่นก่อนเข้าเขาวงกต ใช้ Harness เป็นก้อนพลังที่รวบ Context, Tool,
Decision, Human และ Verify เข้ามาเป็นระบบเดียวรอบหุ่น

บนสไลด์มีข้อความเพียง title `AGENT HARNESS` และ label ขององค์ประกอบ 5 อย่าง:
📖 Context, 🔧 Tool, 🔀 Decision, 👤 Human และ ✅ Verify

## Composition

- พื้นหลัง, กรอบ title, เส้นพื้น, pips, exit blink และจังหวะ pixel animation
  ยึดภาษาภาพจาก `01-title.html`
- title อยู่ในกรอบพิกเซลกึ่งกลางด้านบน ไม่มี level, subtitle, caption หรือ footer
- คนและหุ่นใช้ sprite และขนาดเดียวกับหน้า 01
- Harness เป็นก้อนพลังที่มี glow เบลอ, core และ pixel sparks
- ตอนเริ่ม Emoji แต่ละใบมีกรอบและ label เพื่อแนะนำความหมาย
- ตอนหุ่นสูบเข้ามา กรอบและ label สลาย ส่วน Emoji ย่อเล็กลง
- ช่วงสูบสร้างหางแสงจากตำแหน่งย้อนหลังของ Emoji จริง ปลายแสงจึงติดกับ Emoji
  ทุกเฟรม ไม่มีเส้นทางวาดรออยู่ข้างหน้า
- ภาพสุดท้ายเหลือ Emoji อย่างละหนึ่งชิ้น ไม่มีกรอบหรือ label หมุนตามสมการวงรี
  จริงรอบหุ่น ไม่มีเส้นขอบวงรีแข็ง มีเพียง halo เบลอจาง ๆ และหางแสงตาม Emoji

## 5 beats

1. คนกับหุ่นยืนห่างกัน ขณะที่ Context, Tool, Decision, Human และ Verify
   ลอยกระจายทั่วสไลด์
2. คนเดินเข้าหาหุ่นและส่งก้อนพลัง Harness ที่อยู่ระหว่างทั้งคู่
3. หุ่นรับพลัง ย้ายมากลางฉาก และเริ่มชาร์จด้วยวงแสงกับ pixel sparks
4. หุ่นสูบองค์ประกอบทั้งห้าเข้ามา กรอบและ label สลายระหว่างทาง
5. Emoji ขนาดเล็กโผล่จากศูนย์กลาง แล้วหมุนเป็นวงรีรอบหุ่นพร้อมหางแสงเบลอ

## Navigation and controls

- PREV คือ `06-context-files.html`
- NEXT คือ `08-agent.html`
- ใช้ระบบควบคุมร่วมของ deck: click/keyboard/back/reset/AUTO, iframe
  postMessage และ reduced motion
- `from` สำหรับ iframe คือ `07-agent`

## Decisions

- ไม่ใช้ภาพคนจูงหุ่นหรือชุดที่สวมทับตัวหุ่น เพราะอาจสื่อว่าคนควบคุมทุกก้าว
- ให้คนเป็นผู้ส่งก้อนพลัง แล้วถอยออก เพื่อสื่อว่าคนกำหนดวิธีทำงานก่อนปล่อย Agent
  ทำงานเองภายใต้ Context, Tools, Decision points, Human gates และ Verify
- Emoji บนสไลด์นี้เป็นข้อยกเว้นเรื่อง UI emoji ตามคำขอของ user และใช้ชุดเดียว
  กับป้ายในสไลด์เขาวงกตถัดไป
