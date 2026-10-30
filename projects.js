/* Generated from projects.json by tools/build_project_pages.py. */
window.PORTFOLIO_PROJECTS=[
  {
    "id": "yuyenpensuk",
    "title": "อยู่เย็นเป็นสุข วิศวกรรม",
    "cats": [
      "ba",
      "sa"
    ],
    "kind": "โครงการเว็บไซต์สำหรับบริษัท · 2026",
    "desc": "เว็บไซต์บริษัทและระบบ CMS สำหรับจัดการสินค้า บริการ ข่าว และผลงาน",
    "role": "ประสานงานกับเจ้าของบริษัท รวบรวมความต้องการ ออกแบบ Flow และพัฒนาเว็บไซต์พร้อมระบบจัดการเนื้อหา",
    "features": [
      "Admin Login",
      "สินค้าและบริการ",
      "ข่าวและผลงาน",
      "อัปโหลดรูปภาพ",
      "จัดเก็บข้อมูล CMS"
    ],
    "flow": [
      "ความต้องการเจ้าของบริษัท",
      "ออกแบบเว็บและ CMS",
      "พัฒนา",
      "ทดสอบและส่งมอบ"
    ],
    "tech": [
      "Node.js",
      "Express",
      "JavaScript",
      "Docker",
      "Ubuntu"
    ],
    "result": "ทดสอบ security policy ผ่าน; CMS ยังไม่ตรวจรับ",
    "limit": "2 automated tests ผ่าน แต่ startup แบบ REQUIRE_EXISTING_DATA=1 หยุดเพราะไม่มีฐานข้อมูล CMS จริง; ไม่มี product JPG uploads จริงครบ และยังไม่ได้ทดสอบ admin flow",
    "repo": "yuyenpensuk-website",
    "images": [],
    "analysis": {
      "href": "analysis/yuyenpensuk/index.html",
      "diagram": "analysis/yuyenpensuk/diagrams/data-flow.svg",
      "label": "Requirement · DFD · Data Model · Workflow · UAT"
    }
  },
  {
    "id": "agricultural",
    "title": "Agricultural Prices Analytics",
    "cats": [
      "da",
      "sa"
    ],
    "kind": "โครงงานรายวิชา · 2026",
    "desc": "รวบรวมราคาสินค้าเกษตรจาก DIT, NABC และตลาดไท พร้อม Dashboard ที่อ่าน PostgreSQL โดยตรง",
    "role": "ออกแบบการรวบรวมและตรวจสอบข้อมูล ปรับ Pipeline และ Dashboard ให้เปรียบเทียบราคาอย่างมีเงื่อนไข",
    "features": [
      "3 แหล่งข้อมูลจริง",
      "Common Schema",
      "UPSERT",
      "แนวโน้มราคา",
      "Pipeline Status"
    ],
    "flow": [
      "DIT / NABC / ตลาดไท",
      "ตรวจหน่วยและวันที่",
      "ตัดซ้ำและ UPSERT",
      "PostgreSQL",
      "Streamlit Dashboard"
    ],
    "tech": [
      "Python",
      "Pandas",
      "Airflow",
      "PostgreSQL",
      "Streamlit"
    ],
    "result": "README รุ่นวันที่ 23 ตุลาคม 2569 ระบุ 398 รายการหลังตัดซ้ำ และรักษาข้อมูลเดิม 354 รายการ",
    "limit": "398 เป็นจำนวนในชุดตรวจสอบรุ่นดังกล่าว ไม่ใช่จำนวนสด; เปรียบเทียบเฉพาะหน่วย ประเภทการวัด และช่วงเวลาที่สอดคล้องกัน",
    "repo": "02739452-26-6621655321",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/02739452-26-6621655321/main/evidence/third_source/screenshots/dashboard.png",
        "caption": "ภาพ Dashboard จากหลักฐานการทดสอบใน Repository"
      },
      {
        "src": "https://raw.githubusercontent.com/intasan/02739452-26-6621655321/main/evidence/third_source/screenshots/dashboard-table.png",
        "caption": "ภาพตารางข้อมูลจากหลักฐานการทดสอบ"
      },
      {
        "src": "https://raw.githubusercontent.com/intasan/02739452-26-6621655321/main/evidence/third_source/screenshots/graph.png",
        "caption": "ภาพกราฟจากหลักฐานการทดสอบ"
      }
    ]
  },
  {
    "id": "ppe",
    "title": "AI PPE Inspection — BA Case Study",
    "cats": [
      "ba",
      "sa"
    ],
    "kind": "แบบทดสอบสมัครงาน · 2026",
    "desc": "วิเคราะห์ระบบตรวจ PPE สี่ประเภท ณ ทางเข้าโรงงาน: Helmet, Mask, Vest และ Gloves",
    "role": "วิเคราะห์โจทย์ กำหนดขอบเขต จัดคำถามเก็บความต้องการ ร่าง FR / NFR และ Acceptance Criteria",
    "features": [
      "24 คำถาม",
      "Functional Requirements",
      "Non-functional Requirements",
      "Uncertain / Manual Review",
      "UAT Scenarios"
    ],
    "flow": [
      "เข้าเขตตรวจ",
      "ประเมิน PPE",
      "ครบ / ไม่ครบ / ไม่มั่นใจ",
      "เจ้าหน้าที่ตรวจทาน",
      "แจ้งเตือนและบันทึก"
    ],
    "tech": [
      "Requirement Analysis",
      "Process Flow",
      "Acceptance Criteria",
      "UAT Planning"
    ],
    "result": "จัดทำข้อเสนอระบบ ครอบคลุมขอบเขต ความเสี่ยง MVP และเงื่อนไขที่ต้องยืนยันกับลูกค้า",
    "limit": "เป็น Proposed Solution สำหรับแบบทดสอบ ยังไม่ใช่ระบบ AI ที่พัฒนาและติดตั้งใช้งานจริง",
    "repo": null,
    "images": []
  },
  {
    "id": "motoinsight",
    "title": "MotoInsight — Data Analysis & ETL",
    "cats": [
      "da"
    ],
    "kind": "โครงงานรายวิชา",
    "desc": "Notebook รวบรวมข้อมูลรถจักรยานยนต์จาก CheckRaka และอัตราแลกเปลี่ยนผ่าน REST API",
    "role": "จัดเตรียมข้อมูลด้วย Web Scraping / API ทำความสะอาด แปลงข้อมูล และนำเสนอผ่านกราฟกับ Dashboard",
    "features": [
      "Web Scraping",
      "REST API",
      "Data Cleaning",
      "CSV / XLSX Export",
      "Gradio Dashboard"
    ],
    "flow": [
      "Web / API",
      "Transform",
      "Export",
      "Analysis",
      "Gradio"
    ],
    "tech": [
      "Python",
      "Pandas",
      "NumPy",
      "BeautifulSoup",
      "Matplotlib",
      "Plotly",
      "Gradio"
    ],
    "result": "ยังประมวลผลไม่ได้",
    "limit": "รัน data_cleaning.py แล้วไม่พบ data/input.csv; gesture pipeline ขาด cv2 และไม่มี dataset ที่แนบใน Repository",
    "repo": "machine-learning-project",
    "images": []
  },
  {
    "id": "gold-thai",
    "title": "GoldSense — Thai Gold 96.5%",
    "cats": [
      "da",
      "sa"
    ],
    "kind": "โครงงานรายวิชา · 2026",
    "desc": "Dashboard รวบรวมราคาทองจาก API จริงและ SQLite; ยังไม่มีการประเมินโมเดลพยากรณ์",
    "role": "ออกแบบการดึงข้อมูล การจัดเก็บ และการแสดงกราฟสำหรับติดตามราคา",
    "features": [
      "ดึงข้อมูลราคาจริง",
      "SQLite ไม่เพิ่ม publication ซ้ำ",
      "สถานะข้อมูลเก่า/ไม่มีข้อมูล",
      "ยังไม่แสดงผลพยากรณ์"
    ],
    "flow": [
      "Thai Gold API",
      "ตรวจราคาและเวลาเผยแพร่",
      "SQLite",
      "Dashboard"
    ],
    "tech": [
      "Node.js 24",
      "SQLite",
      "JavaScript"
    ],
    "result": "รันรวบรวมข้อมูลจริงได้; ยังไม่มี forecast",
    "limit": "รัน HTTP API, query SQLite และจับภาพ Dashboard จริงได้; มีราคาจริง 1 publication; ไม่แสดง forecast/MAE/RMSE เพราะยังไม่มี chronological holdout",
    "repo": "thai-gold-price-forecast",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/thai-gold-price-forecast/main/evidence/dashboard-actual.jpg",
        "caption": "Dashboard กับราคาจริง 1 publication; ยังไม่มี forecast"
      },
      {
        "src": "https://raw.githubusercontent.com/intasan/thai-gold-price-forecast/main/evidence/database-api-log-view.jpg",
        "caption": "ภาพ viewer ของ log HTTP และ SQL ที่รันจริง ไม่ใช่หน้าจอโปรแกรมจัดการ DB"
      }
    ]
  },
  {
    "id": "gold-trading",
    "title": "Gold Trading Analytics",
    "cats": [
      "da",
      "sa"
    ],
    "kind": "โครงการทดลองด้านข้อมูล · 2026",
    "desc": "เอกสารแนวคิดระบบวิเคราะห์ทองคำ ยังไม่มี ETL / API / โมเดลที่รันได้ใน Repository",
    "role": "ออกแบบแนวทาง Data Pipeline, Feature Engineering และการนำเสนอผลการทดลอง",
    "features": [
      "เอกสารแนวคิดและหน้าแนะนำเท่านั้น"
    ],
    "flow": [
      "เอกสารแนวคิด",
      "รอ source และข้อมูลจริง"
    ],
    "tech": [
      "HTML",
      "Markdown"
    ],
    "result": "ยังไม่มีระบบที่รันได้",
    "limit": "Repository มีเพียง README และ index.html; ไม่มี Airflow DAG, API, Compose, model หรือข้อมูลจริงสำหรับยืนยันตัวเลขเดิม",
    "repo": "gold-trading",
    "images": []
  },
  {
    "id": "flood",
    "title": "Thailand Flood Intelligence",
    "cats": [
      "da",
      "sa"
    ],
    "kind": "โครงการระหว่างพัฒนา · 2026",
    "desc": "แพลตฟอร์มวิจัยสถานการณ์น้ำ แยก Public Dashboard และ Research API พร้อมแหล่งที่มาของข้อมูล",
    "role": "ออกแบบขอบเขตข้อมูล การแสดงผลบนแผนที่ และเงื่อนไขตรวจสอบข้อมูลก่อนนำเสนอ",
    "features": [
      "Map / GeoJSON",
      "Historical Water Levels",
      "Data Provenance",
      "Research API",
      "Readiness Status"
    ],
    "flow": [
      "ข้อมูลที่มีสิทธิ์ใช้",
      "ตรวจคุณภาพ",
      "PostGIS",
      "API",
      "แผนที่ / Dashboard"
    ],
    "tech": [
      "Next.js",
      "TypeScript",
      "MapLibre",
      "FastAPI",
      "PostGIS"
    ],
    "result": "โค้ดทดสอบผ่าน; ข้อมูลและแบบจำลองยังไม่พร้อม",
    "limit": "Backend 259 passed, 5 skipped; Frontend 20 passed และ build/typecheck ผ่าน; actual API ให้ readiness 503 เพราะ PostGIS ไม่พร้อม; ไม่มีผลเสี่ยงรายที่ดินที่ผ่าน validation; UI readiness แสดงตรวจสอบไม่ได้ เพราะ preview Python ไม่มี uvicorn",
    "repo": "Thailand-Flood-Intelligence",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/Thailand-Flood-Intelligence/main/evidence/readiness-actual.jpg",
        "caption": "หน้า readiness จริง: ตรวจสอบสถานะไม่ได้"
      },
      {
        "src": "https://raw.githubusercontent.com/intasan/Thailand-Flood-Intelligence/main/evidence/test-log-view.jpg",
        "caption": "ภาพ viewer ของ stdout pytest ที่รันจริง; ไม่ใช่หลักฐานแบบจำลองพร้อมใช้"
      }
    ],
    "analysis": {
      "href": "analysis/flood/index.html",
      "diagram": "analysis/flood/diagrams/data-flow.svg",
      "label": "Requirement · DFD · Data Model · Workflow · UAT"
    }
  },
  {
    "id": "system-design",
    "title": "System Analysis & Design Coursework",
    "cats": [
      "ba",
      "sa"
    ],
    "kind": "งานวิเคราะห์ระบบในรายวิชา · 2025",
    "desc": "รวมการวิเคราะห์และออกแบบระบบผ่าน UML, DFD, ERD และแบบจำลองฐานข้อมูล",
    "role": "แปลงโจทย์เป็นผู้ใช้งาน Use Case กระบวนการ และแบบจำลองข้อมูล",
    "features": [
      "Banking / Hospital UML",
      "ATM / Toy Car UML",
      "Use Case",
      "DFD / ERD",
      "Normalization 1NF–3NF"
    ],
    "flow": [
      "โจทย์และผู้ใช้งาน",
      "Requirements",
      "Use Case / UML",
      "Data Model",
      "Documentation"
    ],
    "tech": [
      "UML",
      "DFD",
      "ERD",
      "Database Design"
    ],
    "result": "ตรวจได้เฉพาะ source และ schema",
    "limit": "มี schema.sql, clothesline.ino และ docs/system-analysis.md; ไม่มี MySQL, Arduino toolchain หรืออุปกรณ์จริงในสภาพแวดล้อมนี้",
    "repo": "system-analysis-projects",
    "images": []
  },
  {
    "id": "booking",
    "title": "STILL — Lodging Booking",
    "cats": [
      "ba",
      "sa"
    ],
    "kind": "เว็บต้นแบบ Node.js + SQLite · ยังไม่มีข้อมูลธุรกิจจริง",
    "desc": "เว็บค้นหาห้องว่างและจองที่พัก พร้อมป้องกันจองซ้อนและประวัติการจองใน SQLite",
    "role": "กำหนด Booking Flow และกติกาวันเข้าพัก พร้อมพัฒนาโดยใช้ AI assistance ใน ChatGPT Work และตรวจการจอง/ยกเลิกจริง",
    "features": [
      "Date / Guest Search",
      "Room Type Filter",
      "Atomic Overlap Protection",
      "Booking History",
      "Cancellation"
    ],
    "flow": [
      "เลือกวันและจำนวนคน",
      "ตรวจห้องว่างจาก SQLite",
      "ตรวจราคา",
      "ยืนยันการจอง",
      "ประวัติ / ยกเลิก"
    ],
    "tech": [
      "Node.js 24",
      "SQLite",
      "JavaScript",
      "HTML / CSS"
    ],
    "result": "ทดสอบ logic ผ่าน; ข้อมูลธุรกิจยังไม่มี",
    "limit": "4 unit tests ผ่านด้วย fixture ในหน่วยความจำเท่านั้น; runtime ใหม่ไม่สร้าง sample rooms; ไม่มีข้อมูลห้องจริงหรือการเชื่อมผู้ประกอบการ",
    "repo": "lodging-booking-system",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/lodging-booking-system/main/evidence/empty-real-data-actual.jpg",
        "caption": "Runtime จริงไม่เติม sample rooms; ยังไม่มีข้อมูลห้องจริง"
      }
    ]
  },
  {
    "id": "adoption",
    "title": "ระบบหาบ้านให้สัตว์",
    "cats": [
      "ba",
      "sa"
    ],
    "kind": "กรณีศึกษาออกแบบระบบ",
    "desc": "ออกแบบระบบเชื่อมต่อข้อมูลสัตว์กับผู้สนใจรับเลี้ยง",
    "role": "วิเคราะห์ผู้ใช้และกระบวนการยื่นคำขอรับเลี้ยง",
    "features": [
      "Visitor",
      "Adopter",
      "Shelter",
      "Admin"
    ],
    "flow": [
      "ค้นหาสัตว์",
      "ดูรายละเอียด",
      "ยื่นคำขอ",
      "ตรวจสอบ",
      "อนุมัติ"
    ],
    "tech": [
      "Requirements",
      "Use Case",
      "System Design"
    ],
    "result": "ตรวจได้เฉพาะ source และ schema",
    "limit": "มี schema.sql, clothesline.ino และ docs/system-analysis.md; ไม่มี MySQL, Arduino toolchain หรืออุปกรณ์จริงในสภาพแวดล้อมนี้",
    "repo": "system-analysis-projects",
    "images": []
  },
  {
    "id": "vending",
    "title": "VOLT — Drink Station",
    "cats": [
      "ba",
      "sa"
    ],
    "kind": "เว็บต้นแบบ Node.js + SQLite · ยังไม่มีข้อมูลธุรกิจจริง",
    "desc": "เว็บสั่งเครื่องดื่ม พร้อมตะกร้า สต็อก คำสั่งซื้อ และสะสมคะแนนใน SQLite",
    "role": "กำหนดขอบเขตและ Business Rules พร้อมพัฒนาโดยใช้ AI assistance ใน ChatGPT Work และตรวจผลการทำงานจริง",
    "features": [
      "SQLite Persistence",
      "Server-side Totals",
      "Stock Reservation / Cancellation",
      "Test Payment",
      "10 Purchases → 1 Reward"
    ],
    "flow": [
      "เลือกสินค้า",
      "ตรวจยอดจากเซิร์ฟเวอร์",
      "กันสต็อก",
      "ยืนยันชำระทดลอง",
      "บันทึกคะแนน / ประวัติ"
    ],
    "tech": [
      "Node.js 24",
      "SQLite",
      "JavaScript",
      "HTML / CSS"
    ],
    "result": "ทดสอบ logic ผ่าน; ข้อมูลธุรกิจยังไม่มี",
    "limit": "4 unit tests ผ่านด้วย fixture ในหน่วยความจำเท่านั้น; runtime ใหม่ไม่สร้าง sample catalog; ไม่มี integration ชำระเงินจริง/เครื่องจ่ายจริง",
    "repo": "energy-drink-vending-machine",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/energy-drink-vending-machine/main/evidence/empty-real-data-actual.jpg",
        "caption": "Runtime จริงไม่เติม sample catalog; ยังไม่มีข้อมูลสินค้าจริง"
      }
    ]
  },
  {
    "id": "gesture",
    "title": "Hand Gesture Recognition",
    "cats": [
      "da"
    ],
    "kind": "โครงงาน Machine Learning · 2024",
    "desc": "ทดลองจำแนกท่าทางมือจากภาพและกระบวนการประมวลผลภาพ",
    "role": "ออกแบบ Workflow การเก็บภาพ ตรวจจับมือ และจำแนกท่าทาง",
    "features": [
      "Hand Detection",
      "Landmarks",
      "Classification",
      "Image Processing"
    ],
    "flow": [
      "ภาพ / กล้อง",
      "ประมวลผลภาพ",
      "ตรวจจับมือ",
      "Features",
      "จำแนกท่าทาง"
    ],
    "tech": [
      "Python",
      "OpenCV",
      "NumPy",
      "Machine Learning"
    ],
    "result": "ยังประมวลผลไม่ได้",
    "limit": "รัน data_cleaning.py แล้วไม่พบ data/input.csv; gesture pipeline ขาด cv2 และไม่มี dataset ที่แนบใน Repository",
    "repo": "machine-learning-project",
    "images": []
  },
  {
    "id": "social",
    "title": "Flutter Social Media App",
    "cats": [
      "app"
    ],
    "kind": "โครงงานแอปพลิเคชัน / โค้ดสร้างใหม่",
    "desc": "แอป Social Media แบบ X-style มี Feed, Profile, Post, Like และ Comment",
    "role": "พัฒนา Flow การใช้งานและเชื่อมข้อมูลกับ Firebase",
    "features": [
      "Authentication",
      "Public Feed",
      "Profile",
      "Post / Like / Comment",
      "Audio"
    ],
    "flow": [
      "Login",
      "Feed",
      "Post",
      "Interaction",
      "Profile"
    ],
    "tech": [
      "Flutter",
      "Dart",
      "Firebase Auth",
      "Firestore",
      "Firebase Storage"
    ],
    "result": "ยังรันไม่ได้",
    "limit": "ไม่มี Flutter SDK; ไม่มี pubspec.yaml และหน้า pages ที่ service อ้างอิง รวมทั้งยังไม่มี Firebase configuration",
    "repo": "flutter-social-app",
    "images": []
  },
  {
    "id": "clothesline",
    "title": "ราวตากผ้าอัตโนมัติ",
    "cats": [
      "app",
      "sa"
    ],
    "kind": "โครงงาน IoT · 2024",
    "desc": "เชื่อมเซนเซอร์ความชื้น/ฝนกับไมโครคอนโทรลเลอร์และแอปติดตาม",
    "role": "ออกแบบลำดับการอ่านเซนเซอร์ สั่งมอเตอร์ และควบคุมผ่านแอป",
    "features": [
      "Rain / Moisture Sensor",
      "Microcontroller",
      "Motor",
      "Mobile Control"
    ],
    "flow": [
      "Sensor",
      "Detection",
      "Controller",
      "Decision",
      "Motor"
    ],
    "tech": [
      "IoT",
      "Microcontroller",
      "Mobile Application"
    ],
    "result": "ตรวจได้เฉพาะ source และ schema",
    "limit": "มี schema.sql, clothesline.ino และ docs/system-analysis.md; ไม่มี MySQL, Arduino toolchain หรืออุปกรณ์จริงในสภาพแวดล้อมนี้",
    "repo": "system-analysis-projects",
    "images": []
  },
  {
    "id": "open-house",
    "title": "Open House: Sun of Prosperity",
    "cats": [
      "ba",
      "ux"
    ],
    "kind": "งานออกแบบแผนกิจกรรม",
    "desc": "ออกแบบ Visitor Flow การจัดสรรเจ้าหน้าที่ และแผนรองรับเหตุการณ์",
    "role": "วาง Theme กระบวนการเข้าชม และ Scenario ฝนตก / No-show",
    "features": [
      "10 Houses ในแผน",
      "20 Staff ในแผน",
      "Floors 12 / 14",
      "Elevator Flow",
      "Scenario Planning"
    ],
    "flow": [
      "Visitor Journey",
      "Houses",
      "Staff Allocation",
      "Floor / Elevator",
      "Scenarios"
    ],
    "tech": [
      "Process Design",
      "Resource Planning",
      "Scenario Planning"
    ],
    "result": "ตรวจได้เฉพาะเอกสาร",
    "limit": "มี planning.md; ไม่มีหลักฐานการจัดงานจริงหรือแบบแปลนและการอนุมัติจริง",
    "repo": "sun-of-prosperity-open-house",
    "images": []
  },
  {
    "id": "tarot",
    "title": "Interactive 3D Tarot",
    "cats": [
      "ux"
    ],
    "kind": "โครงงานต้นแบบ Interactive (reconstructed)",
    "desc": "แอปเลือกไพ่ 3 ใบ เปิดข้อความด้วย CSS 3D เปลี่ยนไพ่และเริ่มใหม่ได้",
    "role": "ออกแบบ Page Flow และ Interaction ของเว็บ",
    "features": [
      "เลือกไพ่",
      "CSS 3D flip",
      "ข้อความสะท้อนความคิด",
      "เริ่มใหม่"
    ],
    "flow": [
      "เลือกไพ่",
      "เปิดข้อความ",
      "เปลี่ยนไพ่หรือเริ่มใหม่"
    ],
    "tech": [
      "HTML",
      "CSS 3D",
      "JavaScript"
    ],
    "result": "ผ่าน browser checks ที่รันจริง",
    "limit": "เลือกไพ่ 2, reset และเลือกไพ่ 3 ได้จริง; ใช้ CSS 3D และข้อความสะท้อนความคิดที่เขียนขึ้น ยังไม่ได้ตรวจมือถือจริง",
    "repo": "tarot-3d-interactive",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/tarot-3d-interactive/main/evidence/card-selected-actual.jpg",
        "caption": "เลือกไพ่ใบ 3 จากแอปที่รันจริง; ข้อความสะท้อนความคิด ไม่ใช่การพยากรณ์"
      }
    ]
  },
  {
    "id": "space",
    "title": "Space Explorer 3D",
    "cats": [
      "ux"
    ],
    "kind": "โครงงานต้นแบบ Interactive (reconstructed)",
    "desc": "นำเสนอดวงอาทิตย์ ดาวศุกร์ โลก และดาวเสาร์ในรูปแบบ 3D",
    "role": "แปลงข้อกำหนดด้านภาพและการหมุนของวัตถุเป็น Interactive Presentation",
    "features": [
      "3D Objects",
      "Self Rotation",
      "Interactive Presentation"
    ],
    "flow": [
      "เลือกมุมมอง",
      "ดูโมเดล 3D",
      "สังเกตการหมุนของวัตถุ"
    ],
    "tech": [
      "Three.js",
      "JavaScript"
    ],
    "result": "ยังไม่ผ่าน WebGL runtime",
    "limit": "เพิ่ม source ส่วนควบคุมแล้ว แต่ browser สร้าง WebGL context ไม่สำเร็จ จึงยังไม่ยืนยันฉากสามมิติ",
    "repo": "space-explorer-3d",
    "images": [
      {
        "src": "https://raw.githubusercontent.com/intasan/space-explorer-3d/main/evidence/webgl-unavailable-actual.jpg",
        "caption": "สถานะจริง: สร้าง WebGL context ไม่ได้ ยังไม่ผ่านฉากสามมิติ"
      }
    ]
  }
];
