# Conventions การทำงานใน repo นี้

## Git

- ทำงานบน `main` ตรงๆ ไม่แตก branch
- commit message เป็น**ภาษาอังกฤษ** conventional-commit style:
  - `talks/<talk>/**` → `feat(<talk-slug>)` (เนื้อหาใหม่) / `docs(<talk-slug>)` (โน้ต, handoff)
    — slug ตัดสั้นได้ เช่น `feat(2026-09-ai-usage): ...`
  - `.claude/skills/**` → `feat(skills)` / `chore(skills)`
  - `README.md`, root config → `docs(repo)` / `chore(repo)`
- **ห้าม `git add -A` / `git add .`** — stage ด้วย explicit path เท่านั้น
  (discipline อยู่ใน `.claude/skills/push-session/`)

## Skills

- `/push-session` — commit + push เฉพาะไฟล์ที่ session นี้แตะ (`-y` = ข้าม confirm)
- `/prep-compact` — อัปเดต `HANDOFF.md` ของ talk ที่ทำอยู่ แล้ว push ก่อน user จะ `/compact`
- ทั้งคู่ port มาจาก portal-workspace (`D:\Projects\Workground\portal-workspace`)
  แบบปรับ scope แล้ว — เคยมี `plan-sessions` ด้วยแต่ user ให้เอาออก (2026-08-24)

## ภาษา

- คุยกับ user เป็นภาษาไทย
- commit message และชื่อไฟล์เป็นภาษาอังกฤษ / เนื้อหาใน docs ปนไทยได้
