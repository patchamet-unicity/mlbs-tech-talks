# mlbs-tech-talks

Repo เก็บและทำ presentation ของ user สำหรับงาน TechTalks รายเดือน

ไฟล์นี้เป็น **index เท่านั้น** — เนื้อหาอยู่ใน `memory/` ให้อ่านเฉพาะไฟล์ที่เกี่ยวกับงานที่กำลังทำ:

- [memory/techtalks-event.md](memory/techtalks-event.md) — งาน TechTalks คืออะไร, Slack channel, รอบถัดไปของ user
- [memory/repo-structure.md](memory/repo-structure.md) — โครง `talks/`, บทบาท NOTES.md vs HANDOFF.md, stage ของ talk
- [memory/conventions.md](memory/conventions.md) — git/commit style และภาษา

State ของ talk ที่กำลังทำอยู่ **ไม่อยู่ใน memory** — อ่านจาก `talks/<talk>/HANDOFF.md` ของ talk นั้น

## Slide preview

เปิด local server จาก repo root ด้วย:

```powershell
python -m http.server 8777
```

จากนั้นเปิด slide ที่ต้องการผ่าน `http://localhost:8777/`
