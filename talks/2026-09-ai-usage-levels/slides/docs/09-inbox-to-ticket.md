# Slide 09 — Inbox-to-Ticket Harness

## Status

`09-inbox-to-ticket.html` ใช้โครง 70 beats ครบตั้งแต่ Opening / `INTAKE`
ไปจนถึง `TRIAGE`, `INVESTIGATE`, `SYNTHESIZE`, `OWNERSHIP`,
`DISPATCH` และ Final Result

สไลด์นี้เป็นตัวอย่างงานจริงต่อจาก `08-agent.html`: ทุก phase ใช้ภาษาภาพเดียวกับ
`INTAKE` คือเปิด Markdown ทีละใบ คงใบก่อนหน้าเป็นกอง รวมเป็น working set
แล้วยุบเข้า checkpoint บน route พร้อม tree รายชื่อไฟล์ที่ค้างอยู่ตลอด

## Current implementation — 70 beats

- **Beats 1–10 — Opening + INTAKE**: เปิด route → แสดง Markdown 7 ใบทีละใบ →
  รวมเป็น working set → ยุบเข้า `[INTAKE]`
- **Beats 11–20 — TRIAGE**: แสดง Markdown 8 ใบทีละใบ → รวม → ยุบเข้า
  `[TRIAGE]`
- **Beats 21–33 — INVESTIGATE**: รับ `triaged-work-items.md` แล้ว fan-out เป็น
  Business / Technical; แสดงเอกสารสองฝั่งเป็นคู่ ๆ ก่อนรวมผลและยุบเข้า
  `[INVESTIGATE]`
- Technical Evidence แตกเป็นไฟล์จริงระดับ `system-structure.md`,
  `web-check.md`, `api-check.md`, `database-check.md`, `log-check.md` และ
  `code-check.md` ไม่ใช้ไฟล์ umbrella ใบเดียว
- **Beats 34–43 — SYNTHESIZE**: แสดง Markdown 8 ใบ → รวมหลักฐาน ประเมิน
  confidence และล็อก scope → ยุบเข้า `[SYNTHESIZE]`
- **Beats 44–54 — OWNERSHIP**: แสดง Markdown 9 ใบ → ระบุ owner, approver,
  dependencies จาก confirmed scope → ยุบเข้า `[OWNERSHIP]`
- **Beats 55–68 — DISPATCH**: แสดง Markdown 12 ใบ → เตรียม parent/child tickets,
  human approval และ verify ticket set → ยุบเข้า `[DISPATCH]`
- **Beats 69–70 — Final Result**: zoom out เห็น route และ tree ทั้งหก phase
  จากนั้นคนกับหุ่นเคลื่อนไปถึงเส้นชัย
- tree ใต้ phase ที่เสร็จแล้วคงอยู่ใน world เสมอ; กล้องเลื่อนไปตาม phase ปัจจุบัน
  และกองการ์ดใหม่สามารถซ้อนบัง tree เก่าได้ตามจังหวะการเล่า
- caption ทุก beat เป็นภาษาไทย; title ใน body ของทุกการ์ดมี Emoji
- `PREV = "08-agent.html"`; สไลด์ 08 เชื่อม `NEXT = "09-inbox-to-ticket.html"`;
  `NEXT` ของสไลด์ 09 ยังว่าง
- รองรับ controls, AUTO, iframe postMessage, reduced motion และ rebuild state
  สำหรับ forward/back/reset ตามสไลด์ก่อนหน้า

### Verification ล่าสุด

- inline JavaScript syntax และ `git diff --check` ผ่าน
- headless Chrome ผ่านครบ 70 beats ที่ viewport 1280×720 รวม back, reset และ
  rapid navigation
- ทุก milestone มีจำนวน persistent trees ถูกต้อง: 2 / 3 / 4 / 5 / 6
- ไม่พบ active Markdown card ล้นกรอบ และ INVESTIGATE tree มีไฟล์ structure,
  web, API, database, logs และ code ครบ

## Working name

ชื่อที่เข้าใจง่ายบนสไลด์:

**Inbox-to-Ticket Agent**

ชื่อที่อธิบายหน้าที่ได้แม่นกว่า:

**Request Investigation & Routing Agent**

เมื่อเล่าในบริบทของ talk ให้มองว่า Agent คือผู้ทำงาน ส่วน Harness คือระบบที่จัด
Context, Tools, Decision points, Human approval และการ Verify รอบ Agent

## Visual language

อย่าเรียกทุกอย่างว่า Context ปนกัน ให้แยกชนิดของ node ชัดเจน:

- `[INPUT]` = เมล เอกสาร และหลักฐานจริงที่เข้ามา
- `[CTX]` = กฎ ความรู้ และข้อจำกัดที่ Agent ใช้อ้างอิง
- `[TOOL]` = สิ่งที่ Agent ใช้อ่าน ค้นหา หรือเปลี่ยนข้อมูล
- `[DECISION]` = จุดจำแนก ประเมินหลักฐาน หรือเลือกทางเดิน
- `[HUMAN]` = จุดขอข้อมูล ตรวจทาน หรือตัดสินใจอนุมัติ
- `[OUTPUT]` = Report, Ticket หรือ Action item ที่สร้างออกมา
- `[VERIFY]` = การตรวจความครบถ้วน ความถูกต้อง และผลกระทบก่อนจบงาน

การแยกภาษาภาพนี้สำคัญ เพราะช่วยให้สไลด์ไม่กลายเป็นแค่ “เอา Context หลายไฟล์
มารวมกัน” ซึ่งจะซ้ำกับ `06-context-files.html`; สไลด์นี้ต้องแสดงว่า Harness คุม
วิธีทำงานและจุดตัดสินใจทั้งหมดด้วย

## Event tree

```text
[TRIGGER] New email / Scheduled inbox check
|
+-- 1. INTAKE — Read and normalize
|   |
|   +-- [CTX] Inbox rules
|   |   +-- Subject / prefix ที่ต้องรับ
|   |   +-- Sender / To / CC ที่เกี่ยวข้อง
|   |   +-- Attachment types ที่อ่านได้
|   |   \-- เมลแบบไหนให้ข้าม เช่น auto-reply / duplicate
|   |
|   \-- [INPUT] Request package
|       +-- เนื้อหาเมล
|       +-- ประวัติการสนทนา
|       \-- เอกสารแนบ
|
+-- 2. TRIAGE — Break into Work Items and classify
|   |
|   +-- Work Item A
|   +-- Work Item B
|   \-- Work Item C
|       |
|       \-- [DECISION] Classify each Work Item
|           +-- Issue / Incident
|           +-- Requirement / Change
|           +-- Question / Clarification
|           \-- Unknown / Low confidence -> [HUMAN] ขอข้อมูลเพิ่ม
|
+-- 3. INVESTIGATE — Confirm what is actually related
|   |
|   +-- [FAN OUT] Investigate in parallel
|   |   |
|   |   +-- [BUSINESS CONTEXT]
|   |   |   +-- Policy / current process
|   |   |   +-- Country / customer / product rules
|   |   |   +-- SLA / severity
|   |   |   \-- ขอบเขตที่ Agent ทำเองได้
|   |   |
|   |   \-- [TECHNICAL EVIDENCE]
|   |       |
|   |       +-- [CTX] System knowledge
|   |       |   +-- โครงสร้างระบบ
|   |       |   +-- ตำแหน่งข้อมูล
|   |       |   +-- วิธีตรวจสอบ
|   |       |   \-- Known issues / limitations
|   |       |
|   |       \-- [TOOLS] Inspect relevant systems
|   |           +-- Web / Admin portal
|   |           +-- API
|   |           +-- Database / schema
|   |           +-- Logs
|   |           \-- Source code
|   |
|   \-- [FAN IN] Investigation findings
|       +-- Business constraints
|       +-- Technical evidence
|       +-- Missing information
|       \-- Conflicts between sources
|
+-- 4. SYNTHESIZE — Combine and verify findings
|   |
|   +-- สิ่งที่ยืนยันได้จากหลักฐาน
|   +-- ข้อสันนิษฐาน
|   +-- Root cause หรือ expected change
|   +-- ผลกระทบและขอบเขตที่เกี่ยวข้องจริง
|   \-- [DECISION] Confidence เพียงพอหรือยัง?
|       |
|       +-- No  -> กลับไปตรวจเพิ่ม / [HUMAN] ขอข้อมูลเพิ่ม
|       \-- Yes -> ล็อก scope แล้วเดินหน้าต่อ
|
+-- 5. OWNERSHIP — Route from confirmed scope
|   |
|   +-- [CTX] System ownership
|   +-- [CTX] Team responsibilities
|   +-- [CTX] Approval matrix
|   +-- [DECISION] หนึ่งเรื่องหรือต้องแยกหลายทีม?
|   \-- [OUTPUT] Owners, approvers and dependencies
|
\-- 6. DISPATCH — Prepare, approve, create and verify
    |
    +-- Prepare Ticket plan
    |   +-- Parent request
    |   +-- Child ticket: ทีม A
    |   +-- Child ticket: ทีม B
    |   \-- Dependencies ระหว่าง Ticket
    |
    +-- [HUMAN] ตรวจข้อสรุป ผู้รับผิดชอบ และอนุมัติก่อนสร้าง
    |
    +-- [TOOL] Create parent Ticket
    |
    +-- [FAN OUT] Create child Tickets in parallel
    |   |
    |   +-- Child: Team A
    |   |   +-- Relevant summary
    |   |   +-- Evidence / attachments
    |   |   \-- Acceptance criteria
    |   |
    |   +-- Child: Team B
    |   |   +-- Relevant summary
    |   |   +-- Evidence / attachments
    |   |   \-- Acceptance criteria
    |   |
    |   \-- Child: Team C
    |       +-- Relevant summary
    |       +-- Evidence / attachments
    |       \-- Acceptance criteria
    |
    \-- [FAN IN] Verify complete Ticket set
        +-- ไม่มี Ticket ซ้ำ
        +-- Summary / evidence ครบ
        +-- Acceptance criteria ชัด
        +-- Owner / watchers / links ถูกต้อง
        \-- Dependencies เชื่อมครบ
```

## Core flow

```text
1. INTAKE
   อ่านและจัดรูปข้อมูล

2. TRIAGE
   แตก Work Items และจำแนกประเภท

3. INVESTIGATE
   ตรวจ Business Context และ Technical Evidence พร้อมกัน
   เพื่อยืนยันว่าอะไรเกี่ยวข้องกับเรื่องนี้จริง

4. SYNTHESIZE
   รวมหลักฐาน ประเมินความมั่นใจ และล็อกขอบเขต

5. OWNERSHIP
   ใช้ขอบเขตที่ยืนยันแล้วระบุ Owner, Approver และ Dependencies

6. DISPATCH
   ให้คนอนุมัติ แตก Ticket ไปแต่ละทีม และตรวจความครบถ้วน
```

## Analysis notes

- Flow นี้เป็น Agent workflow ชัดเจน เพราะ Agent ไม่ได้แค่อ่านและสรุป แต่ต้อง
  จำแนกงาน เลือก Context เรียก Tools ประเมินหลักฐาน และสร้างผลลัพธ์จริง
- อย่าหา Ownership จากข้อความในเมลเร็วเกินไป เพราะระบบหรือทีมที่ถูกกล่าวถึงอาจไม่ใช่
  เจ้าของสาเหตุจริง ต้องตรวจ Business Context และ Technical Evidence แล้วล็อก scope ก่อน
- ถ้าต้องขอสิทธิ์หรือข้อมูลจากคนระหว่าง Investigate ให้มองว่าเป็นผู้ช่วยเปิดทาง ไม่ใช่
  การระบุ Owner ของงาน ซึ่งจะเกิดใน phase 5 หลัง Synthesize
- ผลลัพธ์อาจไม่ใช่ Ticket เดียว ควรสร้าง parent request แล้วแตก child tickets
  ตามทีม พร้อม dependency เพื่อไม่ให้แต่ละทีมเห็นข้อมูลเพียงบางส่วนโดยขาดภาพรวม
- ต้องแยก observed evidence, inference และสิ่งที่ยังไม่ทราบให้ชัด โดยเฉพาะก่อน
  สร้าง Ticket หรือ route ไปหาทีมอื่น
- ขั้นตอนตรวจระบบควรเป็น read-only โดยปริยาย การเปลี่ยนข้อมูลจริงต้องเป็นอีก flow
  ที่มีสิทธิ์และ Human approval ของตัวเอง
- ต้องมี duplicate check ก่อนสร้าง Ticket เพราะเมล thread เดิมอาจถูกส่งต่อหรือ
  trigger ซ้ำได้

## Possible slide direction

Tree เต็มชุดใหญ่เกินกว่าจะเปิดพร้อมกันในหน้าเดียว ควรให้แกนหลักอยู่กลางเวทีแล้ว
ค่อยแตกกิ่งตาม beat:

1. `INTAKE` — เมลและ attachment เข้ามา
2. `TRIAGE` — แตก request เป็น Work Items และจำแนกประเภท
3. `INVESTIGATE` — แตกสองกิ่ง Business Context / Technical Evidence พร้อมกัน
4. `SYNTHESIZE` — รวมผลกลับมา ยืนยันความเกี่ยวข้องและล็อก scope
5. `OWNERSHIP` — ใช้ scope ที่ยืนยันแล้วหา Owner, Approver และ Dependencies
6. `DISPATCH` — หยุดที่ Human approval ก่อนแตก parent/child Tickets แล้ว Verify

ภาพควรทำให้เห็นว่า Context และ Tools ถูกเลือกตามประเภทงาน ไม่ได้เปิดทุกอย่าง
พร้อมกันทุกครั้ง และ `[Human]` ต้องยังเด่นเหมือนใน `08-agent.html`

## Resolved decisions

- สไลด์ 09 เป็นตัวอย่าง workflow ต่อจากแนวคิด Agent Harness ในสไลด์ 08
- จุดเริ่มบนภาพใช้ `User request` จากอีเมลและ attachment
- TRIAGE ใช้ Work Item A/B เพื่อสื่อว่าหนึ่ง request แตกได้หลายงาน โดยไม่ใส่
  รายละเอียดเคสจนแน่นเกินไป
- Human approval ตรวจ Ticket plan ทั้งก้อนหนึ่งครั้งก่อนสร้างจริง
- ใช้ 70 beats: ทุก phase อธิบายเอกสารทีละใบด้วย animation grammar เดียวกับ
  INTAKE; INVESTIGATE เพิ่ม fan-out Business / Technical ภายใน grammar เดิม
