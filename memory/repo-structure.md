# โครงสร้าง repo

```
talks/YYYY-MM-<topic>/
├── slides/     # ตัว presentation
├── assets/     # รูป ไฟล์ประกอบ
├── NOTES.md    # เนื้อหา script ลิงก์อ้างอิง (content ของ talk)
└── HANDOFF.md  # working state — ทำถึงไหน ตัดสินใจอะไรไปแล้ว next action

talks/assets/   # shared assets ใช้ข้าม talk (ไม่ผูกกับ talk ไหน)
└── characters/ # ตัวละครคน+หุ่น AI — ต้นทางคือ build-sprites.py (2026-08-25)
```

- ตั้งชื่อ folder talk เป็น `YYYY-MM-<topic-slug>` (แค่เดือนพอ ไม่ต้องระดับวัน
  เพราะเดือนละครั้ง) ตัวพิมพ์เล็กคั่น `-`
- **NOTES.md กับ HANDOFF.md แยกบทบาทชัด**: NOTES = เนื้อหาของ talk,
  HANDOFF = state ของงาน (เขียน/อัปเดตโดย `/prep-compact`)
- README หลักมีตาราง Talks เป็นสารบัญ — เพิ่ม talk ใหม่ต้องเติมแถวด้วย
- เคยมี `ideas/BACKLOG.md` แล้ว user ให้เอาออก (2026-08-24) — ยังไม่ต้องมี
- stage ของ talk ไล่ตามนี้: คิดหัวข้อ → outline → เนื้อหา → สไลด์ → ซ้อม
