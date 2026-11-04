# Project content audit

Baseline portfolio: 32f78f8cb728556f4fb784518cfb8cd16b132df1. Reviewed repository trees and relevant source; business results are not inferred from code. No mutation targeted intasan/02739452-26-6621655321.

| Case study | Current presentation | Evidence / acceptance boundary |
|---|---|---|
| yuyenpensuk | เว็บไซต์แสดงสินค้าและบริการของบริษัทอยู่เย็นเป็นสุข วิศวกรรม พร้อม CMS สำหรับทีมงาน ไม่รวม Checkout หรือรับชำระเงินอัตโนมัติ | เว็บไซต์บริษัทและ CMS พร้อม Source Code, แนวทาง Deployment และเอกสารวิเคราะห์ระบบ |
| agricultural | รวบรวมราคาสินค้าเกษตรจาก DIT, NABC และตลาดไท พร้อม Dashboard ที่อ่าน PostgreSQL โดยตรง | ชุดหลักฐานวันที่ 23 ตุลาคม 2569 บันทึก 398 แถวหลังตัดซ้ำจาก DIT, NABC และตลาดไท พร้อมภาพ Dashboard และผลตรวจ SQL; เป็นผลของชุดตรวจสอบดังกล่าว ไม่ใช่จำนวนข้อมูลสด |
| ppe | วิเคราะห์ระบบตรวจ PPE สี่ประเภท ณ ทางเข้าโรงงาน: Helmet, Mask, Vest และ Gloves | จัดทำข้อเสนอระบบ ครอบคลุมขอบเขต ความเสี่ยง MVP และเงื่อนไขที่ต้องยืนยันกับลูกค้า |
| motoinsight | Source Python สำหรับอ่านรายการรถจักรยานยนต์จาก CheckRaka ทำความสะอาด CSV และสรุปข้อมูล ยังไม่มี Dashboard หรือผล Dataset ที่ตรวจยืนยัน | Source สำหรับการจัดเตรียมและวิเคราะห์ข้อมูล ยังไม่มีผลการประมวลผลจาก Dataset จริงที่ยืนยันใน Portfolio นี้ |
| gold-thai | Dashboard รวบรวมราคาทองจาก API จริงและ SQLite; ยังไม่มีการประเมินโมเดลพยากรณ์ | Dashboard รวบรวมราคาทองจริงและจัดเก็บ SQLite พร้อมภาพจากชุดหลักฐานใน Repository; ขอบเขตปัจจุบันเป็นการติดตามราคา ยังไม่มีผลพยากรณ์ |
| gold-trading | แนวคิดระบบรวบรวมและวิเคราะห์ราคาทองคำ ปัจจุบันมีเอกสารและหน้าแนะนำโครงการ | เอกสารแนวคิดและหน้าแนะนำโครงการ ยังไม่มี ETL, Airflow DAG, PostgreSQL, ML หรือ Dashboard ที่รันได้ใน Repository ปัจจุบัน |
| flood | แพลตฟอร์มวิจัยสถานการณ์น้ำ แยก Public Dashboard และ Research API พร้อมแหล่งที่มาของข้อมูล | Source ของแผนที่ Dashboard และ Research API พร้อมเอกสารออกแบบระบบ เป็นงานวิจัยระหว่างพัฒนา ยังไม่มีผลประเมินความเสี่ยงรายที่ดินที่ผ่านการรับรอง |
| system-design | เอกสารวิเคราะห์ระบบและ SQL schema สำหรับระบบหาบ้านให้สัตว์ พร้อม Source ควบคุมราวตากผ้าอัตโนมัติ | Source Code, SQL schema และเอกสารวิเคราะห์ระบบสำหรับงานรายวิชา |
| booking | เว็บค้นหาห้องว่างและจองที่พัก พร้อมป้องกันจองซ้อนและประวัติการจองใน SQLite | เว็บต้นแบบการจองที่พักและเอกสารวิเคราะห์ระบบ พร้อมการจัดเก็บ SQLite; ยังไม่มีข้อมูลห้องพักจริงจากผู้ประกอบการ |
| adoption | ออกแบบระบบเชื่อมต่อข้อมูลสัตว์กับผู้สนใจรับเลี้ยง | SQL schema ของระบบรับเลี้ยงสัตว์และเอกสารวิเคราะห์ใน Repository งานรายวิชา |
| vending | เว็บสั่งเครื่องดื่ม พร้อมตะกร้า สต็อก คำสั่งซื้อ และสะสมคะแนนใน SQLite | เว็บต้นแบบสำหรับกระบวนการสั่งเครื่องดื่มและเอกสารระบบ ยังไม่มีข้อมูลธุรกิจหรือธุรกรรมจริงจากผู้ประกอบการ |
| gesture | Source สำหรับอ่านภาพ ปรับขนาด และเตรียม Label จากโฟลเดอร์ ยังไม่มีโมเดลจำแนกหรือผลประเมินที่ยืนยัน | Source ของโครงการ Machine Learning ยังไม่มีผลประเมินจาก Dataset จริงที่ตรวจยืนยันใน Portfolio นี้ |
| social | Flutter UI shell และ Service wrappers ที่สร้างใหม่สำหรับแนวคิด Social App ส่วน Feed, Profile, Post, Like และ Comment ยังเป็นขอบเขตที่ต้องเชื่อมต่อและพัฒนาต่อ | Source ของแอปต้นแบบ Flutter ที่สร้างใหม่ แสดงขอบเขตงานพัฒนา ไม่อ้างว่าติดตั้งใช้งานจริง |
| clothesline | Source Arduino อ่านค่าฝนจาก A0 และสั่งมอเตอร์หุบราวเมื่อค่าต่ำกว่า Threshold ยังไม่มีผลทดสอบกับอุปกรณ์จริง | Source ควบคุมราวตากผ้าด้วย Arduino ใน Repository งานรายวิชา ยังไม่มีหลักฐานทดสอบกับอุปกรณ์ใน Portfolio นี้ |
| open-house | ออกแบบ Visitor Flow การจัดสรรเจ้าหน้าที่ และแผนรองรับเหตุการณ์ | ชิ้นงานแนวคิดการออกแบบกิจกรรม ไม่ใช่หลักฐานผลการจัดงานจริง |
| tarot | แอปเลือกไพ่ 3 ใบ เปิดข้อความด้วย CSS 3D เปลี่ยนไพ่และเริ่มใหม่ได้ | ต้นแบบ Interactive ที่สร้างใหม่ มี Source และภาพการเลือกไพ่ใน Repository; ไม่ใช่ระบบให้บริการเชิงพาณิชย์ |
| space | นำเสนอดวงอาทิตย์ ดาวศุกร์ โลก และดาวเสาร์ในรูปแบบ 3D | Source ของต้นแบบสำรวจอวกาศแบบ Interactive ที่สร้างใหม่ ไม่อ้างว่าเป็นผลิตภัณฑ์เชิงพาณิชย์ |

## Corrections made in this review

- Yuyenpensuk: JSON file storage confirmed from database.js; Express/EJS public/admin split, upload validation, bcrypt/optional OTP and Docker mounts checked in source commit ffecf660f2fdd1a14de3561d817f2276a3c8fee4. Six real browser pages captured. Two local security-header tests passed. No authenticated CMS, production writes or restart test. No proof of deployed/source equivalence. Owner discussion and delivery are user-supplied project history, not independently signed-off records.
- Gold Trading: current tree 5a0872c07784fcc7e82ddaf7be6ef9fae41c4577 contains only introduction/concept documents. Marked Concept / In Progress. Proposed sources, ETL, schema, feature engineering, evaluation and dashboard are distinguished from implementation. No old model scores reused.
- MotoInsight: motorcycle_scraper.py and data_cleaning.py support parsing, CSV and cleaning. Removed notebook, exchange-rate API, Gradio/Plotly-dashboard claims not established by current source.
- Gesture: hand_gesture_pipeline.py reads, resizes and normalizes images and loads folder labels. It does not train or evaluate a classifier.
- Flutter Social: main.dart is a UI shell. README_CODE lists expected files that are not all in the tree; profile/feed/likes/comments/storage are not presented as completed features.
- Clothesline: source reads A0 and drives timed retraction when below threshold. No mobile-app integration or physical-device validation claimed.
- Animal Adoption: actual schema contains animals, adopters and adoption_requests with foreign keys. A new source-derived ERD documents that schema; generic example diagrams in older coursework notes are not treated as implemented evidence.
- Booking/Vending/Tarot/Space: reconstructed prototypes remain explicitly labeled. No actual business bookings, payments, stock or users are claimed.
- Flood: research work, no validated land-level risk outcome. GoldSense: price tracking, no evaluated forecast. Historical evidence remains historical.

## English review

Case-study headings use Project Overview, Business Problem, My Responsibilities, Implementation Scope, Results & Deliverables and Limitations consistently. Proposed, source-derived, reconstructed and historical are used as scope qualifiers rather than success claims. Resume English was rewritten for each target role. Thai explanatory content remains intentionally bilingual.


## Gold runtime update — 4 November 2026

Supersedes Gold runtime limitations in earlier dated sections only. Actual Docker + PostgreSQL 16.15 restart persistence and all three Airflow 2.10.5 DAG tasks passed on GitHub Actions run 41788294519. Daily 13:17 Asia/Bangkok refresh first full execution 41788601769 passed, including recorded export commit and Pages rebuild. Services are ephemeral; no hosted Airflow UI or permanent PostgreSQL deployment is claimed. Latest recorded export has 2,412 observations, 4 November 2026 06:56:26 UTC.

ML remains NOT PASSED: HGB MAE 138.14 vs naive 135.47; broader 16-configuration pre-holdout validation still selected the naive baseline. No predictive accuracy or forecast promotion is claimed. Raw source logs and reproducible comparison are in intasan/gold-trading.

Gold gallery now includes five real browser captures: overview, monthly history, model evaluation, pipeline/provenance and the successful GitHub Actions runtime integration. The *-current.jpg images show the 4 November export; the Actions capture is test-run evidence, not an Airflow UI or database GUI capture. External URLs point to the author's own Gold repository. All are Real Evidence of the displayed page, with stated scope; none is an AI screenshot.

Case-study source-derived requirements, data model and architecture links remain available. Hero, theme, navigation, Orb and all animation source were unchanged. Agricultural repository was not modified.
