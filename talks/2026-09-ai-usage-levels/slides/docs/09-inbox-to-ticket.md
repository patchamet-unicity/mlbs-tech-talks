# Slide 09 Draft — Inbox-to-Ticket Harness

## Status

`09-inbox-to-ticket.html` ทำท่อนเปิดและ `INTAKE` prototype ครบ 10 beats แล้วเมื่อ
2026-09-12; user ตอบ “เยี่ยมเลย” หลังรอบแก้ caption เป็นภาษาไทยและเติม Emoji
หน้า title ของเอกสารทั้งเจ็ดใบ ส่วน `TRIAGE` ถึง `DISPATCH` ยังไม่ได้ implement

สไลด์นี้เป็นตัวอย่างงานจริงต่อจาก `08-agent.html`: Harness รับเมลและเอกสารแนบ
แตกประเด็น ตรวจ business rules ไปสำรวจระบบที่เกี่ยวข้อง แล้วเตรียม Ticket ให้ทีมที่
รับผิดชอบ โดยมี Human approval ก่อนสร้างผลกระทบจริง

## Current implementation — Opening + INTAKE

- **10 beats**: เปิด route → แสดง Markdown 7 ใบทีละใบ → รวมเป็น working set →
  ยุบเข้า `[INTAKE]`
- Beat 1 แสดง `User request → ? → Final Result`; คนและหุ่นยืนฝั่งซ้ายมองไปทาง
  เส้นชัย ก่อนหายจากฉากเมื่อเริ่มอธิบายเอกสาร
- Beats 2–8 แสดงเอกสารกลางจอทีละใบ โดยใบปัจจุบันอ่านได้เต็ม ส่วนใบก่อนหน้าค้าง
  เป็นกองทางซ้าย ใช้ภาษาภาพจาก `06-context-files.html` แต่จัดกลางเวที
- เอกสารทั้งเจ็ดใบคือ `email-request.md` `[INPUT]`, `inbox-rules.md` `[CTX]`,
  `email-reader.md` `[TOOL]`, `intake-decision.md` `[DECISION]`,
  `request-clarification.md` `[HUMAN]`, `request-package.md` `[OUTPUT]` และ
  `intake-checks.md` `[VERIFY]`
- Beat 9 รวมเอกสารทั้งเจ็ดเป็นกองเดียวพร้อมข้อความว่าเป็น INTAKE working set
- Beat 10 ยุบกองเข้า route เป็น
  `User request → [INTAKE] → ? → Final Result`; ใต้ `[INTAKE]` แสดงรายการเรียบ
  `Emoji + filename.md` ทั้งเจ็ดใบ **ไม่ใช้ boxed tree**
- caption ใต้สไลด์ของ Beats 1–10 เป็นภาษาไทยทั้งหมด; body title ของการ์ดใช้ Emoji
  ชุดเดียวกับรายการสุดท้ายตามที่ user อนุมัติ
- `PREV = "08-agent.html"`; `NEXT` ยังว่างระหว่างทำสไลด์นี้ต่อ
- รองรับ controls, AUTO, iframe postMessage, reduced motion และ rebuild state
  สำหรับ forward/back/reset ตามสไลด์ก่อนหน้า

### Verification ล่าสุด

- inline JavaScript syntax และ `git diff --check` ผ่าน
- headless browser 1280×720 ผ่านครบ Beats 1–10, back, reset และ rapid navigation
- เอกสารทั้งเจ็ดใบขึ้นเป็น active readable card ครบ; caption ไทยและ Emoji title
  ไม่ล้นหรือถูกตัด
- route Beat 10 ไม่ชน `Final Result`; ไม่พบ viewport overflow หรือ runtime error
  (มีเพียง `/favicon.ico` 404 ของ local server)

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

## Open decisions

- Use case นี้จะมาแทน Growth Intelligence Harness ใน `08-agent.md` หรือเป็น
  ตัวอย่าง workflow อีกชุดหนึ่ง
- Trigger หลักจะเป็นเมลเข้าอย่างเดียว หรือคง Scheduled inbox check ไว้ด้วย
- หนึ่งเมลตัวอย่างควรมีหนึ่งประเด็นเพื่อเล่าง่าย หรือมีสองประเด็นเพื่อโชว์การแตก
  parent/child tickets
- Human approval จะตรวจ Ticket plan ทั้งก้อนครั้งเดียว หรืออนุมัติแยกตามทีม
- จำนวน beats และระดับข้อความที่อ่านได้จริงบนสไลด์
