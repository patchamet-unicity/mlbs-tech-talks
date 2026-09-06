# สไลด์ 6 — `06-context-files.html`

**ระดับ 03 — Context ที่ประกอบจากหลายไฟล์** เริ่มจาก `context/staffhub-access.md`
ใบเดียวในสไลด์ 5 แล้วแยกรายละเอียดออกมาโดย root ยังอ่านได้ทางซ้ายตลอด

## Beats และ speaker intent

| beat | ภาพ | speaker intent |
| --- | --- | --- |
| 1 | `staffhub-access.md` ใบเต็มแบบเดียวกับสไลด์ 5 | จุดเริ่มต้นที่มี shared context ครบ |
| 2 | Highlight Log ใน root และดึง `logs.md` เต็มใบไปขวา | ดูเหตุการณ์ sign-in จาก employee ID และช่วงเวลา |
| 3 | Highlight DB และดึง `database.md`; logs ซ้อนด้านหลัง | เทียบ user, role, department และ synced_at |
| 4 | Highlight steps ด้านสิทธิ์และดึง `permissions.md` | ใช้ role, scope, terminated และ transfer rules แปลข้อมูล |
| 5 | Highlight response format และดึง `response-format.md` | สรุป finding/evidence/action โดยแยก observed จาก inference |
| 6 | เอกสารเต็มสี่ใบซ้อนเป็นกอง | Context ชุดเดียวกันแยกตามหน้าที่ได้ |
| 7 | กองเอกสารหดกลับหา root; root ขยายกลับกึ่งกลางและแทนรายละเอียดเดิมในแต่ละ section ด้วย cross-context refs | ไฟล์หลักยังหน้าตาเดิม แต่รู้ว่าแต่ละเรื่องอยู่ที่ไหน |
| 8 | root ย่อเป็น thumbnail ฝั่งซ้าย, trunk/branches กางออก, paper thumbnails 4 ใบขึ้นทีละใบ | โครงสร้าง context ชัดก่อนส่งไม้ต่อ Agent Harness |
| 9 | StaffHub tree ย่อลงเป็นช่องแรก แล้ว mini document trees รูปแบบเดียวกันค่อย ๆ ปรากฏจนครบกริด 4×3; แต่ละชุดมี label อ่านได้ด้านบน | เราเก็บ context ได้หลายชุด แต่ละชุดมีโครงสร้างลึก 2–4 ชั้นตามเรื่องนั้น |

## เอกสารตัวอย่าง

- `logs.md`: server/IP, Loki datasource, employee/time search, command และ evidence fields
- `database.md`: read-replica, schema/tables, read-only query และ sample SELECT
- `permissions.md`: roles, scope, terminated/transfer, mock sync job, ownership
- `response-format.md`: response sections และ mock Markdown output

ค่า server, IP, commands, job names และ schema เป็น **illustrative/mock** ไม่ใช่ production facts.

## พฤติกรรม

- `BEATS = 9`; normal forward rebuilds prior state then applies new state on animation frame
  เพื่อให้ paper extraction/stack/collapse transition เห็นจริง
- Back, reset, rapid input และ reduced motion ใช้ `rebuild()` เป็น deterministic state
- Beat 1: Back button และ ArrowLeft ไป `05-context.html`; NEXT คือ `07-agent.html`
- iframe ส่ง `slide:next` และ `slide:prev`

## ข้อควรระวัง

1. Root ฝั่งซ้ายต้องอ่านได้ Beats 2–5 และ highlight ต้องตรงกับเอกสารที่ดึงออกมา
2. Paper ซ้อนด้านหลังตั้งใจให้ทับกัน แต่ต้องไม่ออกนอกเวที
3. Beat 7 ยังคงหน้าตา document และ section เดิม ไม่กลายเป็น index table; refs ต้องแทนที่รายละเอียดเดิม ไม่ใช่ต่อท้าย
4. Beat 8 ใช้ root thumbnail เป็น entry point/router เชื่อมลูก 4 ใบด้วยเส้น orthogonal; child thumbnails เป็น miniature paper ไม่ใช่ generic card
5. Beat 9 ต้องใช้ mini document tree รูปแบบเดียวกับ StaffHub ทุกชุด, มี label อ่านได้เหนือ cluster และห้ามลากเส้นเชื่อมข้ามคนละเรื่อง