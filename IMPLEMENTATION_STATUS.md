# สถานะการตรวจ

ยังไม่เสร็จครบทุกโปรเจกต์ รายละเอียดตามหลักฐานจริง [verification](verification.html)

- **app: ยังรันไม่ได้** — ไม่มี Flutter SDK ในสภาพแวดล้อมนี้; การพิสูจน์ MQTT และ LED ต้องมีอุปกรณ์และ broker จริง
- **flutter-social-app: ยังรันไม่ได้** — ไม่มี Flutter SDK; ไม่มี pubspec.yaml และหน้า pages ที่ service อ้างอิง รวมทั้งยังไม่มี Firebase configuration
- **gold-trading: ยังไม่มีระบบที่รันได้** — Repository มีเพียง README และ index.html; ไม่มี Airflow DAG, API, Compose, model หรือข้อมูลจริงสำหรับยืนยันตัวเลขเดิม
- **machine-learning-project: ยังประมวลผลไม่ได้** — รัน data_cleaning.py แล้วไม่พบ data/input.csv; gesture pipeline ขาด cv2 และไม่มี dataset ที่แนบใน Repository
- **yolo11-object-detection: ยังฝึกหรือประเมินไม่ได้** — รัน train.py แล้วขาด ultralytics; ไม่มีภาพและ labels ของ dataset และไม่มี weights/ผลประเมินที่ตรวจสอบได้
- **consumer-detective: ตรวจได้เฉพาะเอกสาร** — มี analysis.md; ไม่มีระบบให้รันหรือไฟล์งานนำเสนอฉบับสมบูรณ์
- **light-pollution-analysis: ตรวจได้เฉพาะเอกสาร** — มี report.md; ไม่มีชุดข้อมูลดิบหรือไฟล์คำนวณสำหรับตรวจซ้ำผลวิเคราะห์
- **sun-of-prosperity-open-house: ตรวจได้เฉพาะเอกสาร** — มี planning.md; ไม่มีหลักฐานการจัดงานจริงหรือแบบแปลนและการอนุมัติจริง
- **system-analysis-projects: ตรวจได้เฉพาะ source และ schema** — มี schema.sql, clothesline.ino และ docs/system-analysis.md; ไม่มี MySQL, Arduino toolchain หรืออุปกรณ์จริงในสภาพแวดล้อมนี้
- **tarot-3d-interactive: ผ่าน browser checks ที่รันจริง** — เลือกไพ่ 2, reset และเลือกไพ่ 3 ได้จริง; ใช้ CSS 3D และข้อความสะท้อนความคิดที่เขียนขึ้น ยังไม่ได้ตรวจมือถือจริง
- **space-explorer-3d: ยังไม่ผ่าน WebGL runtime** — เพิ่ม source ส่วนควบคุมแล้ว แต่ browser สร้าง WebGL context ไม่สำเร็จ จึงยังไม่ยืนยันฉากสามมิติ
- **intasan: ตรวจ source โปรไฟล์** — README เป็น landing page; ใช้สถานะจาก evidence ของแต่ละ Repository เท่านั้น
- **portfolio: อัปเดตหลักฐานและข้อจำกัดแล้ว** — ใช้ภาพจาก browser จริง แยก empty/error state ออกจากระบบที่พร้อมใช้ ไม่แสดงธุรกรรม fixture เดิมใน gallery
- **yuyenpensuk-website: ทดสอบ security policy ผ่าน; CMS ยังไม่ตรวจรับ** — 2 automated tests ผ่าน แต่ startup แบบ REQUIRE_EXISTING_DATA=1 หยุดเพราะไม่มีฐานข้อมูล CMS จริง; ไม่มี product JPG uploads จริงครบ และยังไม่ได้ทดสอบ admin flow
- **energy-drink-vending-machine: ทดสอบ logic ผ่าน; ข้อมูลธุรกิจยังไม่มี** — 4 unit tests ผ่านด้วย fixture ในหน่วยความจำเท่านั้น; runtime ใหม่ไม่สร้าง sample catalog; ไม่มี integration ชำระเงินจริง/เครื่องจ่ายจริง
- **lodging-booking-system: ทดสอบ logic ผ่าน; ข้อมูลธุรกิจยังไม่มี** — 4 unit tests ผ่านด้วย fixture ในหน่วยความจำเท่านั้น; runtime ใหม่ไม่สร้าง sample rooms; ไม่มีข้อมูลห้องจริงหรือการเชื่อมผู้ประกอบการ
- **Thailand-Flood-Intelligence: โค้ดทดสอบผ่าน; ข้อมูลและแบบจำลองยังไม่พร้อม** — Backend 259 passed, 5 skipped; Frontend 20 passed และ build/typecheck ผ่าน; actual API ให้ readiness 503 เพราะ PostGIS ไม่พร้อม; ไม่มีผลเสี่ยงรายที่ดินที่ผ่าน validation; UI readiness แสดงตรวจสอบไม่ได้ เพราะ preview Python ไม่มี uvicorn
- **thai-gold-price-forecast: รันรวบรวมข้อมูลจริงได้; ยังไม่มี forecast** — รัน HTTP API, query SQLite และจับภาพ Dashboard จริงได้; มีราคาจริง 1 publication; ไม่แสดง forecast/MAE/RMSE เพราะยังไม่มี chronological holdout

ไม่เปิดหรือเปลี่ยน Repository ที่ผู้ใช้ยกเว้น
