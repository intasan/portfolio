# ขอบเขตที่ตรวจสอบจากระบบจริง

Repository: `intasan/portfolio`
ฐาน source ที่ตรวจ: `26f6edac6ef5d3b1515e7bf1abf0c7d044814778`

**สถานะ: กำลังอัปเดตหลักฐาน**

แยกภาพธุรกรรมจาก test catalog เดิมออกจาก gallery และเชื่อมผลตรวจที่รันได้จริง

## แหล่งหลักฐาน

- [evidence/source-audit.json](../evidence/source-audit.json)

## Traceability จาก source

| ไฟล์ที่ตรวจ | ขอบเขตที่ยืนยันได้ |
|---|---|
| [index.html](../index.html) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |
| [tools/build_analysis_docs.py](../tools/build_analysis_docs.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |
| [tools/build_project_pages.py](../tools/build_project_pages.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |
| [tools/render_film.py](../tools/render_film.py) | พบ source ใน commit ข้างต้น; การมีไฟล์ไม่ใช่การทดสอบผ่าน |

## เกณฑ์ตรวจรับ BA / SA

| เกณฑ์ | หลักฐาน / สถานะ |
|---|---|
| ขอบเขตปัจจุบันตรงกับ source | กำลังอัปเดตหลักฐาน |
| End-to-end ด้วยข้อมูลจริง | แยกภาพธุรกรรมจาก test catalog เดิมออกจาก gallery และเชื่อมผลตรวจที่รันได้จริง |
| ผลการทดสอบที่ทำซ้ำได้ | อ่าน command, stdout, exit code ใน evidence; syntax check ไม่ใช่ runtime test |
| ข้อมูลจริงและ provenance | เฉพาะราคาทองใน live-verification.txt ที่มี URL/เวลา publication; ไม่ใช้ fixture เป็นข้อมูลจริง |
| UAT โดยเจ้าของงานหรือผู้ใช้งาน | ยังไม่ได้ดำเนินการในรอบนี้ |

## ข้อจำกัดการแสดงผลงาน

ผล unit tests เป็นการตรวจ logic โดยมี fixture ตาม suite เดิม ไม่ใช่หลักฐานธุรกรรมจริง การฝึกโมเดลจริง การทำงานของอุปกรณ์จริง หรือการรับรองจากผู้ใช้ ไม่สร้างข้อมูลธุรกิจทดแทนข้อมูลที่ขาด และไม่อนุมานว่าไม่มีข้อมูลเท่ากับปลอดภัย


## ผล browser รอบปัจจุบัน

เปิด Portfolio ได้ เปิด dialog ของ GoldSense ได้ และสลับ gallery จากภาพ Dashboard จริงไปภาพ log viewer ได้ รูปโหลดจาก Repository ที่อัปโหลดแล้ว ไม่ใช่ภาพ placeholder ไม่อ้างว่าทดสอบทุกหน้าหรือทุกขนาดจอในรอบนี้
