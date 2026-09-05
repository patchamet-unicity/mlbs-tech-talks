# Conventions การทำงานใน repo นี้

## Git

- ทำงานบน `main` ตรงๆ ไม่แตก branch
- commit message เป็น**ภาษาอังกฤษ** conventional-commit style:
  - `talks/<talk>/**` → `feat(<talk-slug>)` (เนื้อหาใหม่) / `docs(<talk-slug>)` (โน้ต, handoff)
    — slug ตัดสั้นได้ เช่น `feat(2026-09-ai-usage): ...`
  - `README.md`, root config → `docs(repo)` / `chore(repo)`
- **ห้าม `git add -A` / `git add .`** — stage ด้วย explicit path เท่านั้น

## ภาษา

- คุยกับ user เป็นภาษาไทย
- commit message และชื่อไฟล์เป็นภาษาอังกฤษ / เนื้อหาใน docs ปนไทยได้
