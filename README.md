# mlbs-tech-talks

เก็บ presentation ของตัวเองสำหรับงาน TechTalks (รายเดือน)

## โครงสร้าง

```
talks/YYYY-MM-<topic>/
├── slides/     # ตัว presentation
├── assets/     # รูป ไฟล์ประกอบ
├── NOTES.md    # เนื้อหา script ลิงก์อ้างอิง
└── HANDOFF.md  # working state (ทำถึงไหน / ต่อยังไง)
```

## เปิด Slide Preview

รันจาก repo root:

```powershell
python -m http.server 8777
```

แล้วเปิด `http://localhost:8777/` ใน browser

## Talks

| เดือน | หัวข้อ | โฟลเดอร์ |
| --- | --- | --- |
| 2026-09 | Level Up How You Use AI (chat → prompt → context → agent harness) | [talks/2026-09-ai-usage-levels](talks/2026-09-ai-usage-levels) |
