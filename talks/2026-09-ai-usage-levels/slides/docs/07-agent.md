# Slide 07 — Growth Intelligence Harness

## Status

`07-agent.html` สร้างแล้วเมื่อ 2026-09-06 ตาม visual และโครง 8 beats ที่ user
อนุมัติ อยู่ระหว่างรอ user เปิดดูและให้ feedback

## Opening scene — เขาวงกต

ใช้สไลด์เดียวเต็มเวทีเปรียบเทียบงานเดียวกันก่อนและหลังมี Harness:

- คนกับหุ่นอยู่ใกล้ทางเข้ามุมซ้ายล่าง โดยมีขนาดใหญ่พอให้อ่านท่าทางได้
- เขาวงกตกินพื้นที่เกือบเต็มจอ ใช้ช่องสี่เหลี่ยมกว้างและความซับซ้อนระดับกลาง
- กล่องสมบัติอยู่มุมขวาบน เป็น business outcome ของงาน
- ไม่มี footer; เหลือเพียง title และ caption ตัวเล็กด้านล่าง
- ครึ่งแรกหุ่นรู้เป้าหมายแต่เดินลองผิดลองถูก หยุดคิดตามทางแยก เจอทางตัน
  แล้วกลับมาถามคน
- ครึ่งหลังใช้เขาวงกตและเป้าหมายเดิม สิ่งที่เพิ่มคือ Harness
- balloon ตอนสั่งมีรูปหีบเดียวกับเป้าหมาย คนยื่นชุดภารกิจ/แผนที่ให้หุ่น
  แล้วหุ่นตอบ `🫡👌`
- Harness ต้องสื่อมากกว่าแผนที่: มีเส้นทางทีละช่วง, ป้าย Context, Tool,
  Decision, Human approval และ Verify
- เส้นทางไม่ควรเผยจนถึงสมบัติตั้งแต่ต้น ให้เปิดทีละช่วงหลังผ่าน checkpoint

ความหมายขององค์ประกอบ:

```text
เขาวงกต = งานจริงที่ซับซ้อน
หุ่น      = Model / Agent
สมบัติ    = Business outcome หรืองานที่เสร็จ
Harness   = แผนงาน + Context + Tools + Decision + Human + Verify
```

### 8 beats

หน้าเริ่มต้นแสดง `0/8`

1. คนชี้ไปที่สมบัติและสั่งหุ่น
2. หุ่นตอบรับแล้วเดินเข้าเขาวงกต
3. หุ่นหยุดคิดตามทางแยก ลองหลายทางและทิ้งรอยเดินไว้
4. หุ่นเจอทางตัน ย้อนกลับ แล้วกลับมาถามคน
5. ล้างรอยทางเดิม คนส่งชุดภารกิจพร้อม Harness ให้หุ่น
6. แผนที่กางออก และป้าย Context/Tools/Decision ตกลงตามทาง
7. หุ่นตอบ `🫡👌` แล้วเดินตาม workflow; ผ่าน `[Human]` approval ระหว่างทาง
8. ผ่าน Verify เปิดกล่อง และนำสมบัติกลับมา

caption ช่วงแรก: **มีเป้าหมาย แต่ไม่มีระบบพาไปจนจบ**

ครึ่งแรกควรรู้สึกช้าและเสียเวลา โดย Beat 3 เป็น micro-animation ที่ยาวที่สุด
ครึ่งหลังเดินได้มั่นใจขึ้น แต่ยังต้องอ่านผล ตัดสินใจ และขออนุมัติ ไม่ใช่ GPS
ที่รู้คำตอบทั้งหมดล่วงหน้า

## Implementation

- เวที 1280×720 และระบบควบคุมเหมือนสไลด์ก่อนหน้า: click/keyboard/back/reset/AUTO,
  iframe postMessage และ reduced motion
- เขาวงกตเป็น logical grid 12×6 สร้างด้วย deterministic depth-first maze จึงได้
  รูปเดิมทุกครั้ง ใช้กำแพงเส้นบางสี `--sign` และมีเส้นทางจริงจาก START ไปหีบ
- PREV คือ `06-context-files.html`; NEXT ยังว่างจนกว่าจะล็อกสไลด์ถัดไป
- ตัวละครใช้ sprite เดิมขนาด 50×64px และหีบ 52×45px เพราะช่องทางเดินกว้างขึ้น
- ครึ่งแรกคำนวณกิ่งที่ออกจากเส้นทางจริงให้หุ่นเดินไปจนตัน ทิ้งรอยสีเทา แล้วย้อน
  กลับมาถามคน
- ครึ่งหลังใช้เส้นทางสองชั้นสีทอง `--door` + `--frame` เปิดทีละช่วง และ pulse
  ระหว่างทำงาน
- ป้ายใช้ Emoji ใหญ่เหนือ label ที่จัดกึ่งกลาง: 📖 Context, 🔧 Tool,
  🔀 Decision, 👤 Human, ✅ Verify; ป้ายตกจากเหนือจอทีละใบ เด้ง/สั่นตอนลง
  เฉพาะตอนเข้า Beat 6 จากนั้นค้างตำแหน่งเดิมใน Beat 7–8 และ pulse อีกครั้งเมื่อ
  หุ่นเดินถึง นี่เป็นข้อยกเว้นเรื่อง UI emoji ตามคำขอของ user
- Beat 7 หุ่นหยุดที่ `[Human]` และส่งสัญญาณกลับมาหาคนเพื่อขออนุมัติ
- Beat 8 เดินต่อถึงกล่อง ผ่าน Verify เปิดกล่อง แล้วนำสมบัติกลับมาที่ START
- การ์ดแผนที่/Harness ใช้เส้นแผนที่จริงแทนเส้น box-shadow ที่เคยดูเหมือนถูกขีดฆ่า
  วางเหนือทางเข้าโดยไม่ทับคน หุ่น หรือ balloon แล้วจางก่อนหุ่นเริ่มเดิน
- Beat 8 หีบสั่น ฝากระเด้งเปิด ปล่อยประกายพิกเซล แล้วสมบัติลอยไปอยู่กับหุ่น
  ก่อนหุ่นนำกลับไปหา user

## Verification

- inline JavaScript syntax และ `git diff --check` ผ่าน
- เปิดด้วย Edge headless ที่ 1280×720 แล้วครบ Beat 1, 4, 6, 7 และ 8
- ทดสอบ animation จริงของ Beat 7–8 แล้ว หุ่นหยุดที่ Human gate และกลับมาถึง
  START พร้อมสมบัติ
- ไม่พบ JavaScript page error; title, maze, caption, controls และ labels อยู่ในเวที

## Big idea

ใช้ **Growth Intelligence Harness** หรือ “ระบบวิเคราะห์โอกาสการเติบโตและแนะนำ
กลยุทธ์ทางธุรกิจ” เป็น use case หลัก เพื่อแสดงว่า Harness รับโจทย์ธุรกิจ แล้วไป
ประกอบข้อมูลจาก Context และ Tools จำนวนมากเพื่อช่วยตัดสินใจ ไม่จำกัดอยู่ที่
StaffHub หรืองานพัฒนา software

Harness เดียวกันต้องเริ่มได้สองแบบ:

```text
User request ──────┐
                   ├──→ Growth Intelligence Harness
Scheduled job ─────┘
```

- On-demand เช่น “ช่วยหาโอกาสเพิ่มยอดขายไตรมาสหน้า และเสนอ Promotion ที่เหมาะ
  กับลูกค้าแต่ละกลุ่ม”
- Scheduled เช่น รันรายสัปดาห์/รายเดือน เพื่อตรวจพฤติกรรมลูกค้า Stock และกระแส
  ภายนอก แล้วแจ้งเมื่อพบโอกาสหรือความเสี่ยงที่มีนัยสำคัญ

## Node language

- `[Context]` = กฎ ความรู้ นิยาม เป้าหมาย หรือข้อจำกัดที่ใช้ตัดสินใจ
- `[Tool]` = การอ่านหรือเปลี่ยนข้อมูลในระบบ
- `[Context + Tool]` = ดึงข้อมูลจริงแล้วตีความด้วยกฎ/ความรู้ที่เกี่ยวข้อง
- `[Decision]` = จุดที่ Harness ประเมินหลักฐานและเลือกทางเดิน
- `[Human]` = จุดที่คนตรวจ ตัดสินใจ หรืออนุมัติก่อนลงมือจริง

user ชอบที่มี `[Human]` อยู่ใน flow มาก ต้องคงไว้ อย่าทำให้ Harness ดูเป็นระบบ
อัตโนมัติที่ตัดสินใจแทนคนทั้งหมด

## Base workflow

```text
รับเป้าหมายและช่วงเวลาที่ต้องการวิเคราะห์
                         [Context]
  ↓
อ่านเป้าหมายธุรกิจ กำไรขั้นต่ำ งบ Promotion
ข้อจำกัด Brand นโยบายข้อมูล และ Privacy
                         [Context]
  ↓
ดึง Customer Profile และ Segmentation
จาก Customer DB / CRM
                         [Context + Tool]
  ↓
ดึง Order History, Basket Size และ Product Affinity
จาก Order DB / Data Warehouse
                         [Context + Tool]
  ↓
วิเคราะห์พฤติกรรมการใช้งานจาก Event Logs
                         [Context + Tool]
  ↓
ดู Conversion Funnel, Retention และ Performance
จาก Datadog / New Relic / Analytics
                         [Context + Tool]
  ↓
ตรวจ Stock, Lead Time และ Supply Constraints
จาก Inventory DB / ERP
                         [Context + Tool]
  ↓
สำรวจข่าว คู่แข่ง Social Trend และ Market Data
ผ่าน Search / News / Third-party APIs
                         [Context + Tool]
  ↓
แบ่งกลุ่มลูกค้าและหาโอกาสของแต่ละกลุ่ม
                         [Decision]
  ↓
สร้างและจำลองทางเลือกเชิงกลยุทธ์หลายแบบ
                         [Context + Tool]
  ↓
ประเมิน Revenue, Cost, Risk และสิ่งที่ต้องเตรียม
                         [Decision]
  ↓
สร้าง Report + Infographic + Recommended Actions
                         [Tool]
  ↓
ส่งให้ผู้มีอำนาจตัดสินใจ
                         [Human]
  ↓
สร้าง Tickets ตามทางเลือกที่อนุมัติ
                         [Tool]
```

จงใจให้ข้อมูลและเครื่องมือหลากหลาย: DB มากกว่าหนึ่งชุด, logs, CRM, Order DB,
Data Warehouse, Inventory/ERP, Search/News/third-party APIs, Datadog/New Relic/
analytics และเครื่องมือสร้าง report, infographic และ ticket

## Expected output

ไม่สรุปเป็นคำตอบเดียว แต่เสนอหลายทิศทางพร้อมหลักฐาน ผลกระทบ trade-off และงานที่
ต้องทำต่อ ตัวอย่างทิศทาง:

1. **Promotion เฉพาะกลุ่ม** — target segment, expected uplift, discount budget,
   Stock ที่ต้องเติม, ช่องทางสื่อสาร และ experiment/control group
2. **ปรับ Product Mix** — สินค้าที่ควรเพิ่ม/ลด, product affinity, ผลต่อ margin,
   supply risk และ experiment ที่ควรรัน
3. **ออกผลิตภัณฑ์ใหม่** — กลุ่มเป้าหมาย, unmet need, feature/คุณสมบัติ,
   opportunity size, market trend/คู่แข่ง และงานวิจัยที่ต้องทำก่อนลงทุน

ปลายทางคือรายงานช่วยตัดสินใจที่มี infographic สวยและอ่านง่าย จากนั้นให้
`[Human]` เลือกหรืออนุมัติทางเลือก จึงค่อยสร้าง ticket/action items ที่เกี่ยวข้อง

## Guardrails

- Customer profile, เพศ, อายุ และพฤติกรรมเป็นข้อมูลส่วนบุคคล ต้องมี privacy,
  consent, data minimization/masking และ access control เป็น Context
- ตรวจ bias ของ segmentation และคำแนะนำ
- แยก observed evidence, inference และ forecast ให้ชัด
- คำแนะนำเชิงกลยุทธ์ต้องผ่าน `[Human]` ก่อนสร้างผลกระทบจริง เช่น เปิด Promotion,
  สั่ง Stock หรือเริ่มลงทุนพัฒนาผลิตภัณฑ์

## Reserved pre-closing slide idea

เก็บภาพเปรียบเทียบนี้ไว้เป็นสไลด์ช่วงก่อนปิด ยังไม่ต้องออกแบบจนกว่าจะคุยกับ user:

```text
Model   = สมอง
Context = ความรู้และคู่มือ
Tools   = มือและเครื่องมือ
Harness = วิธีทำงาน + ผู้ควบคุมงาน
```
