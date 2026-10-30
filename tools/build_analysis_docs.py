"""Reproduce BA/SA documentation and SVG diagrams for five repositories.
No runtime records, credentials or client data are read by this builder.
"""
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[2]
DATE='30 October 2026'
P=[]
def project(repo,slug,title,head,purpose,actors,scope,out,req,rules,questions,stores,links,flow,sources,uat,risks):
 P.append(dict(repo=repo,slug=slug,title=title,head=head,purpose=purpose,actors=actors,scope=scope,out=out,req=req,rules=rules,questions=questions,stores=stores,links=links,flow=flow,sources=sources,uat=uat,risks=risks))
project('energy-drink-vending-machine','vending','VOLT Drink Station','5c5e3493facc401d21b52cf6cb7a78693f58810d',
'ให้ผู้ใช้เลือกเครื่องดื่ม ตรวจยอด สร้างคำสั่งซื้อ และติดตามคะแนนได้ในเบราว์เซอร์ โดยตรวจสต็อกและคำนวณยอดจากเซิร์ฟเวอร์ ระบบนี้เป็นแอปทดลองที่บันทึกรายการจริงใน SQLite ไม่เชื่อมเครื่องจำหน่ายหรือธนาคาร',
[('ผู้ซื้อในเบราว์เซอร์','เลือกสินค้า ตรวจยอด ยืนยันชำระทดลอง ยกเลิก และดูประวัติ'),('ผู้ดูแลโครงการ','ติดตั้งระบบ ดูแลไฟล์ฐานข้อมูลและเรียกใช้ชุดทดสอบ ไม่มีหน้า Admin ในรุ่นนี้')],
'Catalog, Cart, Order, Test payment, Stock reservation, Loyalty และประวัติตาม anonymous session',
'PromptPay จริง การตัดเงิน การจ่ายสินค้าจากฮาร์ดแวร์ บัญชีสมาชิกข้ามอุปกรณ์ และระบบจัดการสินค้า',
[
('V-FR01','อ่านรายการสินค้าและสต็อกจาก SQLite','GET /api/products คืนชื่อ ราคา และ stock ตามฐานข้อมูล','server.js','API / browser เดิม'),
('V-FR02','เพิ่ม ลด และนำสินค้าออกจากตะกร้า','จำนวนใน UI และยอดรวมเปลี่ยนตามรายการที่เลือก','public/app.js','browser เดิม เฉพาะเพิ่มสินค้า'),
('V-FR03','สร้างคำสั่งซื้อด้วยราคาฝั่งเซิร์ฟเวอร์','ไม่ใช้ราคาที่ client ส่งมา และสร้างสถานะ pending เมื่อข้อมูลผ่าน','server.js','tests/orders.test.js'),
('V-FR04','ป้องกันจำนวนไม่ถูกต้องและสินค้าซ้ำ','จำนวนเป็นจำนวนเต็ม 1–10 ต่อสินค้า ไม่เกินสต็อก รายการ 1–3 ชนิดและ id ไม่ซ้ำ','server.js','tests/orders.test.js'),
('V-FR05','กันสต็อกพร้อมคำสั่งซื้อแบบ transaction','สร้าง order และลด stock สำเร็จพร้อมกัน หรือ rollback ทั้งชุด','server.js','tests/orders.test.js'),
('V-FR06','แทนที่ pending order ของ session เดิม','คืนสต็อกเดิมแล้วสร้างใหม่ใน transaction เดียว ความล้มเหลวต้องคง pending เดิม','server.js','tests/orders.test.js'),
('V-FR07','ชำระทดลองได้ครั้งเดียว','pending → paid เท่านั้น การชำระซ้ำตอบ 409 และไม่เพิ่มคะแนนซ้ำ','server.js','tests/orders.test.js / browser เดิม'),
('V-FR08','ยกเลิก pending order และคืนสต็อก','เจ้าของรายการยกเลิกได้ และสถานะเปลี่ยนเป็น cancelled','server.js','tests/orders.test.js'),
('V-FR09','สะสมและแลกเครื่องดื่มฟรี','ทุก 10 paid orders ได้ 1 reward ใช้ลดราคาหน่วยที่ถูกที่สุดในตะกร้า','server.js','tests/orders.test.js'),
('V-FR10','ดูเฉพาะประวัติของ session ปัจจุบัน','GET /api/me คืนประวัติและคะแนนของ customer ที่ผูก cookie การเปลี่ยนรายการผู้อื่นถูกปฏิเสธ','server.js','tests/orders.test.js')],
['หนึ่งคำสั่งซื้อ paid ได้ 1 stamp ไม่ใช่ 1 stamp ต่อกระป๋อง','visits เก็บเศษรอบ 0–9; rewards เก็บจำนวนสิทธิ์คงเหลือ','ยอดรวม = Σ(price × quantity) − ราคาหน่วยต่ำสุด เมื่อเลือกใช้สิทธิ์และมีสิทธิ์เพียงพอ','สิทธิ์ถูกใช้เมื่อชำระสำเร็จ ไม่ถูกหักเพียงเพราะเปิดหน้าตรวจยอด','pending order ไม่มีเวลาหมดอายุอัตโนมัติในรุ่นปัจจุบัน การกันสต็อกจึงค้างจนยกเลิกหรือแทนที่'],
['จะให้ pending order หมดอายุภายในกี่นาที และคืนสต็อกโดยกระบวนการใด','สิทธิ์ฟรีควรนับจากจำนวนครั้งหรือจำนวนหน่วย และยอดศูนย์ยังได้ stamp หรือไม่','ต้องมีบัญชีสมาชิกเพื่อกู้คืนคะแนนเมื่อ cookie หายหรือไม่','จะเพิ่ม Admin และบันทึกประวัติปรับสต็อกอย่างไร','หากเชื่อมธนาคารภายหลัง ต้องตรวจ webhook และ idempotency อย่างไร'],
[('CUSTOMERS',['id PK','visits INTEGER','rewards INTEGER']),('SESSIONS',['token PK','customer FK']),('ORDERS',['id PK','customer FK','items JSON text','total INTEGER THB','status / redeemed','created_at ISO text']),('PRODUCTS',['id PK','name / flavour','price INTEGER THB','stock INTEGER >= 0','color'])],
[('CUSTOMERS','SESSIONS','1 to many'),('CUSTOMERS','ORDERS','1 to many')],
['เลือกสินค้าและจำนวน','สร้าง pending และกันสต็อก','ตรวจคำสั่งซื้อ','ชำระทดลอง หรือยกเลิก','บันทึกสถานะและคะแนน หรือคืนสต็อก'],
['server.js','public/app.js','tests/orders.test.js','ACCEPTANCE.md','evidence/api-tests.txt'],
[('V-UAT01','V-FR03 V-FR05','Citrus 2 หน่วย ราคา 25','ยอด 50 และ stock ลด 2','ผ่าน API เดิม'),('V-UAT02','V-FR04','ส่งจำนวน 0 เศษส่วน สินค้าซ้ำ หรือเกิน 10','ปฏิเสธโดยไม่เปลี่ยนสต็อก','ผ่าน API เดิม'),('V-UAT03','V-FR07','กดยืนยัน pay ซ้ำ','409 และ stamp ไม่เพิ่มซ้ำ','ผ่าน API เดิม'),('V-UAT04','V-FR08','ยกเลิก pending','stock คืนตามจำนวนที่กัน','ผ่าน API เดิม'),('V-UAT05','V-FR09','ซื้อและจ่าย 10 คำสั่ง แล้วแลก 1 สิทธิ์','ได้ 1 reward และใช้สิทธิ์ได้ครั้งเดียว','ผ่าน API เดิม'),('V-UAT06','V-FR10','อีก session พยายามจ่ายคำสั่งซื้อเดิม','404 ไม่มีการเปลี่ยนรายการ','ผ่าน API เดิม')],
['ไม่มี expiry, rate limiting หรือการกู้คืนบัญชี จึงยังไม่พร้อมเปิด commerce สาธารณะ','ต้องทดสอบบนมือถือและทดสอบปิดโปรเซสแล้วเปิดใหม่ก่อนรับรองการใช้งานระยะยาว'])
project('lodging-booking-system','booking','STILL Lodging Booking','3f169eece63f9a70260132736e87aa0a04db773e',
'ให้ผู้ใช้ค้นหาห้องตามวันและจำนวนคน ตรวจยอดรวม และจองโดยไม่เกิดช่วงวันที่ทับซ้อน ฐานข้อมูลเก็บรายการและประวัติยกเลิกจริง แต่ห้องและราคาเป็นข้อมูลทดสอบ ไม่ได้จองโรงแรมภายนอก',
[('ผู้จองในเบราว์เซอร์','ค้นหา ตรวจสอบ ยืนยัน ดูประวัติและยกเลิกการจองของตน'),('ผู้ดูแลโครงการ','เตรียมห้องในฐานข้อมูล รันระบบและชุดทดสอบ ไม่มีหน้า Hotel Admin')],
'ค้นหาห้อง ตรวจ capacity ตรวจช่วงวันที่ คำนวณราคา จองและยกเลิกตาม session',
'รับชำระเงิน โรงแรมจริง อีเมลยืนยัน บัญชีสมาชิก การแก้วันจอง และระบบจัดการหลายสาขา',
[
('B-FR01','ค้นหาตามวันและจำนวนคน','GET /api/rooms กรอง capacity และคืน available ของแต่ละห้อง','server.js','tests/booking.test.js / browser เดิม'),
('B-FR02','กรองประเภทห้อง','คืนเฉพาะ studio suite หรือ family ตาม kind ที่เลือก','server.js','พบในโค้ด ยังไม่มีผลทดสอบเฉพาะ'),
('B-FR03','ตรวจวันเข้าพักและวันออก','วันที่ปฏิทินถูกต้อง วันเข้าไม่เป็นอดีตตาม Asia/Bangkok วันออกหลังวันเข้า ไม่เกิน 30 คืน','server.js','tests/booking.test.js'),
('B-FR04','ตรวจความจุห้อง','guests เป็นจำนวนเต็มบวกและไม่เกิน capacity ของห้อง','server.js','tests/booking.test.js'),
('B-FR05','คำนวณราคาที่เซิร์ฟเวอร์','total = room.price × nights ไม่ใช้ total จาก client','server.js','tests/booking.test.js'),
('B-FR06','กันจองซ้อนแบบ atomic','ตรวจ overlap และ INSERT ภายใน BEGIN IMMEDIATE เดียวกัน','server.js','tests/booking.test.js'),
('B-FR07','ยืนยันจองและสร้างรหัส','สร้าง UUID สถานะ confirmed พร้อมเวลา created_at','server.js','browser เดิม'),
('B-FR08','คืนประวัติของ session เท่านั้น','GET /api/bookings JOIN ชื่อห้อง และไม่ส่ง token session กลับ','server.js','tests/booking.test.js'),
('B-FR09','ยกเลิกเฉพาะรายการของตน','confirmed → cancelled เท่านั้น ห้องกลับมาว่างตามช่วงวันเดิม','server.js','tests/booking.test.js / browser เดิม'),
('B-FR10','แสดงข้อความเมื่อเกิด conflict','หากห้องถูกจองแล้วให้ API ตอบ 409 และ UI แสดงเหตุผล','server.js','tests/booking.test.js เฉพาะ API')],
['ช่วงเข้าพักใช้ [checkin, checkout) จึงให้ลูกค้ารายใหม่เข้าวันที่อีกรายออกได้','เงื่อนไขซ้อน: existing.checkin < requested.checkout AND existing.checkout > requested.checkin เฉพาะ status confirmed','หนึ่ง room record หมายถึงห้องที่จองได้หนึ่งหน่วย ไม่ใช่ room type ที่มีหลายห้องให้กระจาย','created_at เป็น timestamp แต่ checkin และ checkout เป็นวันที่ ไม่ใช่เวลาเช็คอินตามนาฬิกา','รุ่นนี้ยังอนุญาต cancellation โดยไม่มีกฎค่าปรับหรือวันตัดสิทธิ์'],
['ผู้ใช้ยกเลิกได้ถึงเวลาใด และต้องคิดค่าปรับหรือไม่','จะรองรับหลายห้องใน room type เดียวกันอย่างไร','ต้องล็อกห้องระหว่างชำระเงินหรือยืนยันได้ทันทีเหมือนรุ่นปัจจุบัน','ต้องมีช่องทางกู้คืนการจองข้ามอุปกรณ์หรือไม่','ราคาเปลี่ยนตามฤดูกาล ภาษี และเตียงเสริมคิดอย่างไร'],
[('ROOMS',['id PK','name / kind','price INTEGER THB per night','capacity INTEGER','description']),('SESSIONS',['token PK']),('BOOKINGS',['id PK','room FK','session FK','checkin / checkout DATE text','guests / total','status / created_at'])],
[('ROOMS','BOOKINGS','1 to many'),('SESSIONS','BOOKINGS','1 to many')],
['ระบุวันและจำนวนคน','ค้นหาห้องว่าง','ตรวจห้องและยอดรวม','ยืนยันแบบ atomic หรือปฏิเสธ conflict','ดูประวัติ หรือยกเลิกคืนห้องว่าง'],
['server.js','public/app.js','tests/booking.test.js','ACCEPTANCE.md','evidence/api-tests.txt'],
[('B-UAT01','B-FR05','Garden 2 คืนพร้อม client total ปลอม','ใช้ราคา server รวม 2400','ผ่าน API เดิม'),('B-UAT02','B-FR06','จองช่วงวันตรงกันหรือทับบางส่วน','409 และไม่เพิ่มรายการ','ผ่าน API เดิม'),('B-UAT03','B-FR06','วันเข้าตรงกับวันออกของรายการเดิม','จองได้','ผ่าน API เดิม'),('B-UAT04','B-FR03 B-FR04','วันผิด อดีต เกิน 30 คืน หรือคนเกิน','400 และไม่มีรายการใหม่','ผ่าน API เดิม'),('B-UAT05','B-FR08 B-FR09','session อื่นยกเลิก booking','404 รายการเดิมไม่เปลี่ยน','ผ่าน API เดิม'),('B-UAT06','B-FR09','ยกเลิกของตน แล้วค้นช่วงเดิม','แสดง cancelled และห้องกลับว่าง','ผ่าน API และ browser เดิม')],
['ยังไม่มีบัญชีสมาชิก expiry, rate limiting และกฎธุรกิจยกเลิกสำหรับโรงแรมจริง','ต้องทดสอบคำขอพร้อมกันหลายโปรเซสและความทนทานเมื่อฐานข้อมูลล็อกก่อนเปิดใช้งานจริง'])
project('yuyenpensuk-website','yuyenpensuk','Yuyenpensuk Website and CMS','f3d52d949649cb190f92496092bc6b0dc6739541',
'ให้ผู้สนใจเปิดดูข้อมูลบริษัท สินค้าและบริการ และให้ทีมงานปรับเนื้อหาผ่าน CMS โดยไม่ต้องแก้หน้าเว็บด้วยตนเอง โครงสร้างปัจจุบันเป็นเว็บบริษัทและระบบจัดการเนื้อหา ไม่ใช่ระบบ checkout หรือบริหารงานติดตั้งครบวงจร',
[('ผู้เข้าชม','ค้นหาสินค้า อ่านบริการ ผลงาน ราคาและช่องทางติดต่อ'),('Editor','เข้าสู่ระบบและจัดการเนื้อหาตาม route ที่อนุญาต'),('Super Admin','จัดการเนื้อหาและบัญชีผู้ดูแล'),('ผู้ดูแลเซิร์ฟเวอร์','ติดตั้ง สำรอง db.json และ uploads ดูแล hostname และ HTTPS')],
'Public website, CMS สำหรับบริษัท สินค้า บริการ ข่าว ผลงาน banner ราคา payment instructions และบัญชีผู้ดูแล',
'ตะกร้าสินค้า รับชำระอัตโนมัติ Stock ledger ใบเสนอราคา CRM นัดช่าง และหลักฐานรับรองว่างานติดตั้งตัวอย่างเกิดขึ้นจริง',
[
('Y-FR01','แสดงเว็บสาธารณะจากข้อมูล CMS','อ่านข้อมูลปัจจุบันก่อน render และแสดงหน้า public โดยไม่ต้อง login','server.js','พบในโค้ด'),
('Y-FR02','ค้นสินค้าและกรองยี่ห้อ','กรอง q หรือ brand และเปิดรายละเอียด id ที่มีอยู่','routes/site.js','พบในโค้ด'),
('Y-FR03','อ่านแกลเลอรีจากไฟล์ local','ส่งเฉพาะรูปที่หาได้จริงใน uploads และคืน 404 เมื่อไม่มี binary','utils/product-images.js','ต้องทดสอบกับ uploads จริง'),
('Y-FR04','ยืนยันตัวตนผู้ดูแล','ตรวจรหัสผ่านที่ hash และ OTP หากบัญชีเปิด 2FA','routes/admin.js','พบในโค้ด ยังไม่ทดสอบ end to end ในรอบนี้'),
('Y-FR05','จำกัดหน้าจัดการบัญชี','requireSuperAdmin ปฏิเสธ Editor ด้วย 403','middleware/auth.js','พบในโค้ด'),
('Y-FR06','เพิ่มแก้ลบเนื้อหา CMS','รับข้อมูลผ่าน authenticated CRUD และบันทึก db.json','routes/admin.js','ต้องทดสอบ CRUD ในข้อมูลแยก'),
('Y-FR07','ตรวจไฟล์อัปโหลดและ CSRF','ตรวจขนาด ชนิดและ magic bytes; ปฏิเสธ token ที่ไม่ตรง session','routes/admin.js','พบในโค้ด ต้องทดสอบไฟล์ผิดชนิด'),
('Y-FR08','คงข้อมูลหลัง deploy ใหม่','ใช้ DATA_DIR และ UPLOAD_DIR ภายนอก container; โหลด db เดิมโดยไม่ seed ทับ','database.js','ต้องทดสอบ restart บน volume แยก'),
('Y-FR09','แยก public และ admin ด้วย hostname','deploy-server.js เลือก app ตาม host ที่กำหนด','deploy-server.js','ต้องทดสอบ routing / proxy'),
('Y-FR10','ป้องกันลบรูปก่อนบันทึกข้อมูลสำเร็จ','persist ก่อน cleanup และ rollback object หาก save ล้มเหลว','routes/admin.js','พบในโค้ด ต้องทดสอบ fault injection')],
['seed ใช้เฉพาะเมื่อไม่มี db.json เดิม รายการ CMS ที่มีอยู่เป็นข้อมูลหลัก','รูปและฐานข้อมูลอยู่คนละที่ ต้องสำรองเป็นชุดที่สอดคล้องกัน','Editor ไม่ได้มีสิทธิ์จัดการบัญชีผู้ดูแล; Super Admin ต้องผ่าน requireAuth ด้วย','ข้อมูล projects และข้อความการตลาดที่ seed มาไม่ใช่หลักฐานยืนยันลูกค้าหรือสถิติการส่งมอบ','Production บังคับ SESSION_SECRET และรหัสเริ่มต้นที่ตรงเงื่อนไข พร้อม HTTPS; dev preview ไม่เปิด app admin'],
['ใครอนุมัติเนื้อหาและราคาแต่ละประเภทก่อนเผยแพร่','ต้องมี draft และ approval workflow หรือ publish ทันทีแบบปัจจุบัน','รูปสินค้าใดมีสิทธิ์เผยแพร่ และใครดูแลข้อมูลรุ่น/ราคา','ต้องเก็บ audit trail ของผู้แก้ไขเนื้อหาและระยะเวลาย้อนคืนเท่าไร','ต้องสำรองทุกกี่ชั่วโมง และยอมรับการสูญหายข้อมูล/เวลาหยุดระบบได้เท่าไร'],
[('CMS_DOCUMENT',['db.json physical file','company object','products / services arrays','projects / news / banners arrays','admins / pricing / payment']),('CONTENT_RECORD',['id within collection','title or name','image / gallery file paths','other fields by collection']),('ADMIN_RECORD',['id / username','password_hash','role','2FA configuration']),('UPLOAD_FILE',['relative path','validated image or catalog bytes','stored outside app container'])],
[('CMS_DOCUMENT','CONTENT_RECORD','contains'),('CMS_DOCUMENT','ADMIN_RECORD','contains'),('CONTENT_RECORD','UPLOAD_FILE','path references')],
['ผู้ดูแลเข้าสู่ระบบและ OTP หากเปิดใช้','เลือกประเภทเนื้อหาและกรอกข้อมูล','ตรวจสิทธิ์ CSRF และไฟล์','บันทึก db.json แล้วจัดการรูปที่ไม่อ้างอิง','ผู้เข้าชมเปิดข้อมูลที่อัปเดต'],
['database.js','routes/site.js','routes/admin.js','middleware/auth.js','deploy-server.js','tests/security-headers.test.js'],
[('Y-UAT01','Y-FR02','ค้น model หรือเลือก brand','รายการตรงเงื่อนไข รายการว่างต้องไม่ error','รอตรวจรับ'),('Y-UAT02','Y-FR04 Y-FR05','Editor เปิดหน้าจัดการ admins','403 และไม่แก้บัญชี','รอตรวจรับ'),('Y-UAT03','Y-FR07','อัปโหลดไฟล์นามสกุลภาพแต่ bytes ไม่ใช่ภาพ','ปฏิเสธและไม่ทิ้งไฟล์กำพร้า','รอตรวจรับ'),('Y-UAT04','Y-FR06 Y-FR08','แก้สินค้า restart แล้วเปิดใหม่','คงค่าที่บันทึกและรูปเปิดได้','รอตรวจรับ'),('Y-UAT05','Y-FR10','ทำให้ save ล้มเหลวในข้อมูลทดสอบ','ค่าก่อนหน้าและรูปอ้างอิงยังอยู่','รอตรวจรับ'),('Y-UAT06','Y-FR09','เปิด host public / admin / host ไม่อนุญาต','แยก app ถูกต้องและปฏิเสธ host อื่น','รอตรวจรับ')],
['แบบจำลองข้อมูลในเอกสารนี้เป็น logical model ของ JSON ไม่ใช่ SQL ERD และไม่มี foreign key constraint','browser รอบก่อนพบปัญหา CSS จาก CSP ใน HTTP dev; แก้แล้วและ header tests ผ่าน 2 กรณี แต่ยังไม่มีภาพหลังแก้ที่ตรวจรับแล้ว','ยังไม่มีรูป uploads ของเครื่องใช้งานจริงใน checkout; ไม่ควรรับรองแกลเลอรีจากโค้ดเพียงอย่างเดียว'])
project('thai-gold-price-forecast','gold-thai','GoldSense Thai Gold Analytics','ba3ecf504e24fc2cd7a2983aa0bfca4c36527d7f',
'รวบรวม snapshot ราคาทองคำจาก API เก็บ SQLite และแสดงราคาล่าสุด/ข้อมูลย้อนหลัง พร้อม linear regression ตัวอย่างเพื่อการศึกษา การประเมินปัจจุบันยังใช้ข้อมูลชุดเดียวกับการ fit จึงไม่ใช่หลักฐานความแม่นยำกับข้อมูลอนาคต',
[('ผู้ดูข้อมูล','เปิดราคาล่าสุด เลือกช่วงย้อนหลัง และอ่านสถานะข้อมูล'),('Thai Gold API','ส่ง JSON ราคาล่าสุด เป็น wrapper ที่โค้ดระบุว่าอ้างอิงสมาคมค้าทองคำ'),('ผู้ดูแลระบบ','กำหนด endpoint และ DB_FILE ดูแลไฟล์ฐานข้อมูลและการเชื่อมต่อ')],
'Fetch ล่าสุดทุก 60 วินาทีและเมื่อเรียก latest; เก็บ snapshots, history endpoint และสถิติ regression',
'ระบบซื้อขาย การแนะนำลงทุน ข้อมูลย้อนหลัง 1 ปีที่เติมอัตโนมัติ และโมเดลที่ผ่านการทดสอบนอกชุดฝึก',
[
('G-FR01','ดึงราคาจาก endpoint ที่กำหนด','ใช้ THAI_GOLD_API_URL หรือค่าเริ่มต้น และตรวจ HTTP status','server.js','พบในโค้ด ยังไม่ยืนยัน feed รอบนี้'),
('G-FR02','แปลงค่าราคาเป็นตัวเลข','อ่านราคาซื้อขายทองแท่ง/รูปพรรณและ metadata จาก JSON','server.js','ต้องทดสอบ payload จริงและผิดรูป'),
('G-FR03','บันทึก snapshot ใน SQLite','เก็บ source, observed_at, update_date/time และค่าราคา','server.js','พบใน DDL และ save()'),
('G-FR04','ซิงก์อัตโนมัติ','sync ตอน startup และทุก 60000 ms','server.js','พบในโค้ด'),
('G-FR05','คืนราคาที่ดึงใหม่หรือข้อมูลเก่า','/api/latest มี ok, live และ last; การดึงล้มเหลวไม่ควรสร้างราคาปลอม','server.js','พบในโค้ด ต้องทดสอบ failover'),
('G-FR06','อ่านประวัติเรียงตามเวลาที่สังเกต','/api/history กรอง observed_at ตาม days','server.js','พบในโค้ด ต้องทดสอบ input validation'),
('G-FR07','คำนวณ baseline จากลำดับแถว','/api/stats fit เส้นตรงบน goldbar_sell ที่ไม่ null และคาดค่าลำดับถัดไป','server.js','พบในโค้ด ยังไม่ใช่ next-day forecast'),
('G-FR08','ไม่แสดงตัวเลขสถิติเมื่อมีน้อยกว่า 2 แถว','คืน mae rmse forecast เป็น null','server.js','พบในโค้ด'),
('G-FR09','แสดง Dashboard และเลือกช่วงย้อนหลัง','หน้าเว็บเรียก latest/history/stats และ Chart.js','public/index.html','ยังไม่รันสำเร็จในสภาพแวดล้อมนี้'),
('G-FR10','ตรวจ process health','GET /api/health คืน ok และเวลา process','server.js','พบในโค้ด ไม่ตรวจ upstream/DB แบบ readiness')],
['observed_at เป็นเวลาที่ระบบดึง ไม่ใช่เวลาประกาศจาก upstream','UNIQUE(source, observed_at) ไม่ป้องกันการเก็บราคาประกาศเดียวซ้ำในรอบ sync ใหม่','regression ใช้ index แถวเป็นแกน x ไม่ใช่จำนวนวัน; forecast คือ snapshot index ถัดไป','MAE/RMSE ปัจจุบันเป็น in-sample fit errors; ห้ามนำไปอ้างว่าเป็นผล held-out test','หากมีข้อมูลเก่า last ต้องแสดงเวลาประกอบ ไม่ควรตีความว่าเป็นข้อมูลสด'],
['ต้องการหนึ่ง snapshot ต่อการดึง หรือหนึ่งแถวต่อประกาศราคาที่ไม่ซ้ำ','ต้องการพยากรณ์ล่วงหน้ากี่ชั่วโมงหรือกี่วัน และใช้ timestamp ใดเป็นแกนเวลา','จะจัดแบ่ง train/test ตามลำดับเวลาและเทียบ naive baseline อย่างไร','เกณฑ์ stale data และเวลารอ upstream ที่ยอมรับได้คือเท่าไร','สิทธิ์ใช้ API และเผยแพร่ประวัติราคากำหนดไว้อย่างไร'],
[('GOLD_PRICES',['id INTEGER PK','source TEXT NOT NULL','observed_at TEXT NOT NULL','update_date / update_time','goldbar_buy / goldbar_sell REAL','ornament_buy / ornament_sell REAL','spot / thb / change REAL','UNIQUE source + observed_at'])],[],
['รับ trigger ตามรอบหรือคำขอ latest','เรียก API และแปลง JSON','บันทึก snapshot หรือใช้ last หากล้มเหลว','อ่าน history และคำนวณ regression','แสดงราคา เวลา และข้อจำกัด'],
['server.js','public/index.html','package.json','README.md'],
[('G-UAT01','G-FR01 G-FR03','upstream ตอบ payload ที่ตรวจแล้ว','บันทึกราคา/หน่วย/เวลาตาม payload','รอตรวจรับ'),('G-UAT02','G-FR05','upstream ตอบ 500 โดยมีข้อมูลเดิม','live null และ last เป็นแถวเดิม ไม่สร้างข้อมูลใหม่','รอตรวจรับ'),('G-UAT03','G-FR08','มีข้อมูล 0 หรือ 1 แถว','สถิติเป็น null','รอตรวจรับ'),('G-UAT04','G-FR07','ชุดราคาคงที่ที่ใช้เฉพาะ unit test','ค่าความชันและ errors ตรงสูตร ไม่เผยเป็นข้อมูลตลาด','รอตรวจรับ'),('G-UAT05','G-FR06','days เป็นข้อความหรือไม่ใช่ค่าจำกัด','ต้องปฏิเสธอย่างชัดเจน เป็นข้อเสนอที่ยังต้องแก้','ยังไม่มี validation ครบ'),('G-UAT06','G-FR09','ตัดเครือข่ายแล้วเปิด UI','แจ้ง unavailable หรือเวลา last ตามจริง','รอตรวจรับ')],
['better-sqlite3 รุ่นเดิมติดตั้งไม่สำเร็จบน Node.js 24 ในรอบก่อน จึงยังไม่อ้างว่าได้รันระบบนี้สำเร็จ','ยังไม่มี timeout และ payload validation ที่ครบถ้วน รวมถึงอาจเกิดการอ่าน history ก่อน latest บันทึกเสร็จเพราะ UI เรียกแบบขนาน','ต้องแยก holdout test และ time horizon ก่อนใช้คำว่า forecast accuracy'])
project('Thailand-Flood-Intelligence','flood','Thailand Flood Intelligence','6c1ca635e649e3fd83bbe4890d99fdf38c0eb941',
'ให้ประชาชนและนักวิจัยดูข้อมูลตำแหน่ง ความสูงพื้นผิว และข้อมูลสถานีที่มี provenance พร้อมแสดงความพร้อมและข้อจำกัด ระบบยังไม่เปิดความเสี่ยงน้ำท่วมรายที่ดิน ไม่มี live gauge feed และไม่มี hydraulic pilot ที่รับรองแล้ว',
[('ผู้ใช้ Dashboard','ค้นตำแหน่ง วาด/นำเข้าแปลง และอ่านข้อมูลย้อนหลังที่มี'),('นักวิจัย','เรียก API ตรวจ source เวลา หน่วย datum และผลตรวจแพ็กเกจ'),('ผู้ดูแลข้อมูล','นำเข้าข้อมูลที่มีสิทธิ์ใช้และตรวจ quarantine / ingest log'),('ผู้ตรวจแบบจำลอง','เตรียม review evidence และลงนามตามกระบวนการภายนอก ไม่ใช่ Admin UI')],
'Map/parcel tools, approved historical observations, data provenance, research API, offline audit/export และ readiness reporting',
'ผลน้ำท่วมรายบ้านที่รับรองแล้ว การจำลอง hydraulic จริง live gauge feed การรังวัดระดับที่ดิน และระบบเตือนภัย Production',
[
('F-FR01','รับพิกัดและ Polygon ที่ถูกต้อง','/v1/assess ตรวจ lat/lon และ /parcels/assess รับ 2D WGS84 Polygon ที่ valid ไม่เกิน 1000 vertices','backend/app/main.py','มี tests/test_api.py ใน repo'),
('F-FR02','คืน unknown เมื่อยังไม่มีผลที่รับรอง','assessment ส่ง status unsupported, risk unknown และค่าความลึก/ระยะเวลา null','backend/app/main.py','มี tests/test_api.py ใน repo'),
('F-FR03','คำนวณพื้นที่แปลงและรูในแปลง','พื้นที่แบบ WGS84 ellipsoidal; จุดตัวแทนใช้แสดงผล ไม่ใช่วิเคราะห์ทั้งแปลง','backend/app/main.py','มี tests/test_api.py ใน repo'),
('F-FR04','ค้นตำแหน่งและความสูงจาก provider','ตรวจและ cache payload ตาม providers.py; upstream ใช้ไม่ได้ให้ตอบข้อผิดพลาด','backend/app/providers.py','มี tests/test_providers.py ใน repo'),
('F-FR05','เปิดข้อมูลสถานีเฉพาะ source อนุมัติ','query ต้องมี approval_status approved และ license_evidence ไม่ว่าง','backend/app/repository.py','มี tests/test_postgis.py ใน repo'),
('F-FR06','คืน series โดยไม่เติมค่าที่หาย','/observations ส่งแถวจริงและ gaps ไม่ interpolation; ช่วงเวลาไม่เกิน 31 วันและไม่เกิน 10000 แถว','backend/app/repository.py','มี tests/test_postgis.py ใน repo'),
('F-FR07','นำเข้าแบบ atomic และเก็บ provenance','validate ข้อมูล source เวลา หน่วยและ hash ก่อนบันทึก/กักกันตามตัวนำเข้า','backend/app/ingest.py','มี tests/test_ingest.py ใน repo'),
('F-FR08','รายงาน readiness ตามข้อมูลจริง','แยก archive, live, survey, model และ risk; DB ใช้ไม่ได้ต้องไม่แสดงเป็น 0 ที่ดูเหมือนมีข้อมูลครบ','backend/app/main.py','มี tests/test_api.py ใน repo'),
('F-FR09','ตรวจแพ็กเกจโมเดลก่อน Research API อ่าน','ตรวจหลักฐานและลายเซ็น/ไฟล์ตาม model gates; ไม่เท่ากับรับรองฟิสิกส์ของแบบจำลอง','backend/app/models.py','มี tests/test_models.py ใน repo'),
('F-FR10','ส่งออก observation ด้วยคำขอที่ระบุขอบเขต','manual Airflow export ระบุสถานี ช่วงเวลา request ID และสิทธิ์ใช้ ไม่สร้าง simulated series','pipelines/dags/hii_observation_export.py','มี tests/test_export_job.py และ VERIFICATION.md')],
['sources ที่ไม่ approved หรือไม่มี license evidence ไม่ถูกนำมาแสดงใน public queries','ระดับสถานีไม่ใช่ระดับน้ำของที่ดิน; datum ของสองแหล่งต่างกันห้ามลบกันเพื่ออ้างความลึกท่วม','ค่า 0 และค่าติดลบที่มีคุณภาพผ่านเป็นค่าจริงได้ ห้ามแทน missing ด้วย 0','freshness ของสถานีใช้เกณฑ์ 3600 วินาทีใน repository.py; gaps มากกว่า 900 วินาทีเป็นตัวบอกช่องว่างของระบบ ไม่ใช่ rating ทางการ','model_runs เป็นตารางใน schema แต่ research model gate อ่านแพ็กเกจไฟล์; ห้ามตีความว่าตารางนี้แปลว่ามี solver หรือ model ที่อนุมัติแล้ว'],
['พื้นที่นำร่องและเหตุการณ์ใดจะใช้ calibration/validation แยกกัน','ใครเป็นผู้ตรวจที่รับรองได้และมีอำนาจอนุมัติการเผยแพร่ผล','แหล่ง live feed ที่มีสิทธิ์ใช้มีไหนบ้างและมี SLA อย่างไร','ต้องแปลง vertical datum ด้วยข้อมูลสำรวจชุดใดและใครตรวจความถูกต้อง','ผลสาธารณะควรใช้ระดับความไม่แน่นอนและคำเตือนแบบใดเมื่อข้อมูลบางส่วนหาย'],
[('SOURCES',['id TEXT PK','title / url','license_evidence','approval_status']),('STATIONS',['id TEXT PK','source_id FK','location Point 4326','vertical_datum','metadata JSONB']),('OBSERVATIONS',['station_id FK + PK','observed_at PK timestamptz','value / unit','ingested_at / raw_sha256','metadata JSONB']),('INGEST_LOG',['id bigserial PK','source_id FK','started_at / status','raw_sha256 / detail'])],
[('SOURCES','STATIONS','1 to many'),('STATIONS','OBSERVATIONS','1 to many'),('SOURCES','INGEST_LOG','1 to many')],
['เลือกตำแหน่งหรือแปลง','ตรวจรูปทรงและอ่าน source ที่อนุญาต','แสดงสถานี เวลา หน่วย datum และ gaps','ตรวจ availability และหลักฐานโมเดล','คืนข้อมูลที่มี หรือ unknown พร้อมเหตุผล'],
['backend/app/main.py','backend/app/repository.py','backend/app/ingest.py','backend/app/models.py','db/001_init.sql','db/002_provenance.sql','docs/VERIFICATION.md'],
[('F-UAT01','F-FR02','ถาม risk ณ พิกัดที่ยังไม่รองรับ','unknown / unsupported ไม่แสดงว่าปลอดภัย','มี automated evidence เดิม ไม่รันใหม่รอบเอกสาร'),('F-UAT02','F-FR01 F-FR03','Polygon มีรูและรูปร่างเว้า','พื้นที่หักรูและจุดแทนอยู่ในแปลง','มี automated evidence เดิม'),('F-UAT03','F-FR05','withdraw source หลังนำเข้า','public query ไม่แสดงข้อมูล source นั้น','มี automated evidence เดิม'),('F-UAT04','F-FR06','series มีช่วงข้อมูลขาด','ส่ง gaps และไม่เติมค่าระหว่างจุด','มี automated evidence เดิม'),('F-UAT05','F-FR08','หยุดฐานข้อมูล','readiness ระบุ unavailable ไม่ใช่ข้อมูลครบ','มี tests ใน repo'),('F-UAT06','F-FR09','package ขาด signature หรือไฟล์ checksum ไม่ตรง','ไม่อนุญาตอ่านผลโมเดล','มี tests ใน repo')],
['ERD แสดงเฉพาะ core observation path; ยังมี river_reaches และ model_runs ใน DDL ซึ่งไม่ใช่ solver ที่ใช้งานแล้ว','เอกสาร VERIFICATION.md เก็บหลักฐาน CI เดิม แต่การจัดทำเอกสารรอบนี้ไม่ได้รัน pipeline หรือรับรองโมเดลซ้ำ','ต้องมี visual/WebGL/GPS QA และการตรวจทางอุทกวิทยาก่อนเปิดผลสาธารณะ'])

E=html.escape
# Shared SVG layout uses explicit cells and routed connectors; diagrams are editable source assets.
def svg(nodes,edges,title,subtitle):
 w=1120;h=max(y+height for _,x,y,width,height,label,kind in nodes)+85
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{E(title)}</title><desc id="desc">{E(subtitle)}</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#536171"/></marker></defs><rect width="100%" height="100%" fill="#fbfcfe"/><text x="35" y="39" font-family="Arial,sans-serif" font-size="23" fill="#182b3d" font-weight="bold">{E(title)}</text><text x="35" y="65" font-family="Arial,sans-serif" font-size="13" fill="#566677">{E(subtitle)}</text>']
 d={n[0]:n for n in nodes}
 for a,b,label,route in edges:
  _,x,y,bw,bh,_,_=d[a];_,xx,yy,ww,hh,_,_=d[b]
  if route=='down':pts=[(x+bw/2,y+bh),(xx+ww/2,yy)];lx=(pts[0][0]+pts[1][0])/2+8;ly=(pts[0][1]+pts[1][1])/2
  elif route=='left':pts=[(x,y+bh/2),(xx+ww,yy+hh/2)];lx=(pts[0][0]+pts[1][0])/2;ly=pts[0][1]-10
  elif route=='return':pts=[(x+bw,y+bh*.75),(1065,y+bh*.75),(1065,yy+hh*.7),(xx+ww,yy+hh*.7)];lx=870;ly=(y+bh*.75+yy+hh*.7)/2
  else:pts=[(x+bw,y+bh/2),(xx,yy+hh/2)];lx=(pts[0][0]+pts[1][0])/2;ly=(pts[0][1]+pts[1][1])/2-10
  out.append('<polyline points="'+' '.join(f'{a},{b}' for a,b in pts)+'" fill="none" stroke="#536171" stroke-width="1.8" marker-end="url(#arrow)"/>')
  if label:
   lines=label.split('\n');mw=max(map(len,lines))*7+12
   out.append(f'<rect x="{lx-mw/2}" y="{ly-14}" width="{mw}" height="{18*len(lines)+4}" fill="#fbfcfe"/>')
   for i,t in enumerate(lines):out.append(f'<text x="{lx}" y="{ly+i*18}" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#455569">{E(t)}</text>')
 for ident,x,y,bw,bh,label,kind in nodes:
  color={'actor':'#f2eee4','store':'#e8f1ed','process':'#eaf0f8','entity':'#edf1f6'}.get(kind,'#fff')
  radius=22 if kind=='process' else 3
  out.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="{radius}" fill="{color}" stroke="#7890a3" stroke-width="1.3"/>')
  lines=label.split('\n')
  for i,t in enumerate(lines):out.append(f'<text x="{x+bw/2}" y="{y+28+i*21}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{14 if i else 16}" font-weight="{"normal" if i else "bold"}" fill="#21394c">{E(t)}</text>')
 out.append(f'<text x="35" y="{h-20}" font-family="Arial,sans-serif" font-size="11" fill="#697b8c">Analysis artifact | 30 October 2026 | Read scope and implementation status in the accompanying document</text></svg>')
 return ''.join(out)

def diagrams(p):
 slug=p['slug']; repo=p['repo'];title=p['title']
 ctxactors={'vending':['Browser customer','Application operator'],'booking':['Browser guest','Application operator'],'yuyenpensuk':['Public visitor','Editor or Super Admin'],'gold-thai':['Dashboard reader','Thai Gold API'],'flood':['Dashboard / researcher','Data operator / provider']}[slug]
 c=[('user',45,125,225,90,ctxactors[0],'actor'),('system',430,125,260,110,'0 '+title+'\nApplication boundary','process'),('other',845,125,225,110,ctxactors[1],'actor')]
 ce=[('user','system','Requests / inputs','right'),('system','other','Configuration / source\ninteraction shown logically','right')]
 # context return flows explicitly in source and labels below SVG
 ctx=svg(c,ce,title+' Context','Bidirectional interface summary. Detailed input and output contracts are listed in the document.')
 actor='Browser / user'
 stores={'vending':['D1 Products','D2 Orders + customers'],'booking':['D1 Rooms','D2 Bookings + sessions'],'yuyenpensuk':['D1 CMS db.json','D2 Upload files'],'gold-thai':['D1 gold_prices','D1 gold_prices'],'flood':['D1 Approved sources + stations','D2 Observations + provenance']}[slug]
 process={'vending':['1.0 Read catalog','2.0 Reserve / pay / cancel'],'booking':['1.0 Search availability','2.0 Book / cancel atomically'],'yuyenpensuk':['1.0 Read public content','2.0 Authenticate / edit CMS'],'gold-thai':['1.0 Collect API snapshot','2.0 Query history / calculate'],'flood':['1.0 Validate / ingest','2.0 Query / explain readiness']}[slug]
 dn=[('e',35,145,210,90,actor if slug not in ['flood','gold-thai'] else 'Source / data operator','actor'),('p1',430,120,270,100,process[0],'process'),('d1',875,120,210,100,stores[0],'store'),('e2',35,370,210,100,'Browser / authorized actor','actor'),('p2',430,355,270,120,process[1],'process'),('d2',875,365,210,110,stores[1],'store')]
 de=[('e','p1','Input / query','right'),('p1','d1','Read or write\nper process contract','right'),('e2','p2','Action / request','right'),('p2','d2','Read and update\nper process contract','right')]
 dfd=svg(dn,de,title+' Data Flow','Level 1 process overview. Arrow direction details and return/error data are specified in the flow register.')
 fn=[];fe=[]
 for i,label in enumerate(p['flow']):
  # concise English captions in portable images; Thai detail in document
  eng={'vending':['Select items','Validate and reserve stock','Review pending order','Choose test payment or cancel','Commit status and loyalty / stock'], 'booking':['Enter dates and guests','Search available rooms','Review room and total','Confirm atomically or reject conflict','Read history or cancel booking'], 'yuyenpensuk':['Authenticate and optional OTP','Select content and edit fields','Check permission, CSRF and file bytes','Persist CMS then clean unused files','Render updated public content'], 'gold-thai':['Timer or latest-price request','Fetch upstream JSON','Save snapshot or keep last data','Query history and regression','Display time, status and limits'], 'flood':['Choose point or polygon','Validate geometry and source access','Read observations and metadata','Check readiness and model evidence','Return available data or unknown']}[slug][i]
  fn.append((str(i),340,105+i*110,440,70,eng,'process'))
  if i:fe.append((str(i-1),str(i),'','down'))
 workflow=svg(fn,fe,title+' Workflow','Primary flow with alternative outcomes summarized in each step. See business rules and UAT cases.')
 en=[];ee=[]
 for i,(name,fields) in enumerate(p['stores']):
  col=i%2;row=i//2;en.append((name,45+col*560,110+row*290,450,245,name+'\n'+'\n'.join(fields),'entity'))
 for a,b,l in p['links']:
  aa=next(n for n in en if n[0]==a);bb=next(n for n in en if n[0]==b)
  # ERD lines use simple top-down logical relationship; source cardinality lists remain authoritative
  ee.append((a,b,l,'right' if aa[2]==bb[2] and aa[1]<bb[1] else 'down'))
 model=svg(en,ee,title+' Data Model','Logical JSON document model; no SQL foreign keys.' if slug=='yuyenpensuk' else 'Core stored entities. PK and FK labels follow the source schema; fields are selected, not exhaustive.')
 return {'context':ctx,'data-flow':dfd,'workflow':workflow,'data-model':model}

# Override compact images with explicit paired data arrows. DFD stores may be
# repeated across panels; labels identify the same physical stores.
def interface_svg(title, subtitle, panels):
    height=120+len(panels)*260
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="t d"><title id="t">{E(title)}</title><desc id="d">{E(subtitle)}</desc><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#536171"/></marker></defs><rect width="100%" height="100%" fill="#fbfcfe"/><text x="30" y="38" font-family="Arial,sans-serif" font-size="23" font-weight="bold" fill="#182b3d">{E(title)}</text><text x="30" y="65" font-family="Arial,sans-serif" font-size="12" fill="#536171">{E(subtitle)}</text>']
    def text(x,y,label,size=13):
        for j,line in enumerate(label.split('\n')):out.append(f'<text x="{x}" y="{y+j*19}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="#21394c">{E(line)}</text>')
    for i,(left,process,right,lreq,lres,rreq,rres) in enumerate(panels):
        y=120+i*260
        out.append(f'<rect x="15" y="{y-20}" width="1090" height="220" rx="8" fill="none" stroke="#d8e0e6"/>')
        for x,w,label,kind in [(30,200,left,'actor'),(400,300,process,'process'),(870,220,right,'store')]:
            fill={'actor':'#f2eee4','process':'#eaf0f8','store':'#e8f1ed'}[kind]
            out.append(f'<rect x="{x}" y="{y+35}" width="{w}" height="120" rx="{20 if kind=="process" else 2}" fill="{fill}" stroke="#7890a3" stroke-width="1.4"/>')
            if kind=='store':out.append(f'<path d="M{x+12} {y+35}V{y+155}" fill="none" stroke="#7890a3"/>')
            text(x+w/2,y+65,label,14)
        for x1,x2,mid,request,response in [(230,400,315,lreq,lres),(700,870,785,rreq,rres)]:
            out.append(f'<path d="M{x1} {y+65}H{x2}" stroke="#536171" fill="none" stroke-width="1.6" marker-end="url(#a)"/><path d="M{x2} {y+125}H{x1}" stroke="#536171" fill="none" stroke-width="1.6" marker-end="url(#a)"/>')
            text(mid,y+13,request,11);text(mid,y+172,response,11)
    out.append(f'<text x="30" y="{height-18}" font-family="Arial,sans-serif" font-size="11" fill="#66798a">Request and response arrows are explicit. Repeated store labels refer to the same stored data.</text></svg>')
    return ''.join(out)
_original_diagrams=diagrams
def diagrams(p):
    result=_original_diagrams(p);slug=p['slug'];title=p['title']
    contexts={
      'vending':[('Browser customer','0 VOLT\nDrink Station','Application operator\nCLI / file operations','Catalog / cart action\nOrder id + session','Products / order\nStatus / rewards','No admin API\nRun / backup via CLI','Operational output\nOutside purchase API')],
      'booking':[('Browser guest','0 STILL\nLodging Booking','Application operator\nCLI / file operations','Dates / guests\nBook or cancel','Availability / price\nBooking or error','No hotel admin API\nRun / backup via CLI','Operational output\nOutside booking API')],
      'yuyenpensuk':[('Public visitor','0 Public website\nand CMS','Editor / Super Admin','Search / page id','HTML / image\nor not found','Edit response\nSession status','Credentials / OTP\nContent / files')],
      'gold-thai':[('Dashboard reader','0 GoldSense\nAnalytics','Thai Gold API','Latest / history\nStats query','Prices / timestamps\nFit statistics','HTTP latest request','Price JSON\nor HTTP error')],
      'flood':[('Dashboard reader\nResearcher','0 Flood Intelligence\nResearch platform','Operator / provider','Point / polygon\nStation / time query','Observations / metadata\nor unknown','Receipt / provider query\nQuality outcome','Raw data / evidence\nProvider response')]
    }
    panels={
      'vending': [('Browser customer','1.0 Read catalog','D1 Products','Catalog request','Products and stock','SELECT products','Names prices stock'),('Browser customer','2.0 Order and loyalty','D1 Products\nD2 Orders / Customers\nD3 Sessions','Items / pay / cancel\nSession cookie','Order / status\nRewards / error','Read + atomic write','Prices stock order\nOwner and reward data')],
      'booking':[('Browser guest','1.0 Search availability','D1 Rooms\nD2 Bookings','Dates guests kind','Availability and totals','SELECT capacity\nCheck overlap','Rooms + confirmed\nBookings'),('Browser guest','2.0 Book or cancel','D1 Rooms\nD2 Bookings\nD3 Sessions','Room dates guests\nCancel + session','Confirmation history\nor conflict','Read + atomic write','Rate / capacity\nBooking ownership')],
      'yuyenpensuk':[('Public visitor','1.0 Read public content','D1 CMS db.json\nD2 Upload files','Search / page id','HTML / image / 404','Read content\nRead file bytes','Current records\nAvailable files'),('Authorized admin','2.0 Authenticate and edit','D1 CMS db.json\nD2 Upload files','Credentials or content\nCSRF token + files','Session / saved\nor rejected','Read role + save\nValidate uploads','Role / stored content\nValidated file paths')],
      'gold-thai':[('Thai Gold API','1.0 Collect snapshot','D1 gold_prices','Price JSON\nor HTTP error','HTTP latest request','INSERT snapshot','Save result'),('Dashboard reader','2.0 Query and regression','D1 gold_prices','Latest / history / stats','Rows / fit errors\nor unavailable','SELECT snapshots','Latest row\nChronological series')],
      'flood':[('Data operator\nApproved source','1.0 Validate and ingest','D1 Sources / Stations\nD2 Observations\nD3 Ingest log','Raw data + metadata\nRights / hashes','Receipt / quarantine\nor error','Validate source\nAtomic insert / log','Approval metadata\nStored receipt'),('Dashboard reader\nResearcher','2.0 Query and readiness','D1 Sources / Stations\nD2 Observations\nModel package files','Point / polygon\nStation + time window','Approved observations\nor unknown / rejected','Approved-source query\nPackage evidence check','Rows + provenance\nModel gate outcome')]
    }
    result['context']=interface_svg(title+' Context Diagram','System boundary and external interfaces. Operator CLI access is not an implemented admin web screen.',contexts[slug])
    result['data-flow']=interface_svg(title+' Data Flow Diagram','Level 1 summary. External entities at left, processes in the centre, logical data stores at right.',panels[slug])
    # Unambiguous attribute cards avoid crossed relationship lines. Cardinalities are
    # stated beside the diagram and encoded in the detailed Mermaid source.
    layouts={
      'vending':[(335,110),(45,410),(625,410),(335,750)],
      'booking':[(45,110),(625,110),(335,430)],
      'yuyenpensuk':[(335,110),(45,430),(625,430),(45,750)],
      'gold-thai':[(335,110)],
      'flood':[(335,110),(45,430),(45,750),(625,430)]
    }
    nodes=[]
    for (name,fields),(x,y) in zip(p['stores'],layouts[slug]):
        height=max(150,55+len(fields)*21)
        nodes.append((name,x,y,450,height,name+'\n'+'\n'.join(fields),'entity'))
    edges=[(a,b,l,'down') for a,b,l in p['links']]
    result['data-model']=svg(nodes,edges,title+' Data Model','Logical JSON model; contains and path references are not SQL foreign keys.' if slug=='yuyenpensuk' else 'Core schema relationships. FK nullability and other DDL constraints are discussed in the document.')
    return result

def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(str(x).replace('|',' / ').replace('\n',' ') for x in row)+' |\n' for row in rows)

def source(p,path):return f'https://github.com/intasan/{p["repo"]}/blob/{p["head"]}/{path}'
for p in P:
 out=ROOT/p['repo']/'docs'/'analysis';(out/'diagrams').mkdir(parents=True,exist_ok=True)
 figs=diagrams(p)
 for n,s in figs.items():(out/'diagrams'/f'{n}.svg').write_text(s)
 # Mermaid sources are source-of-truth detail diagrams, not user evidence screenshots.
 model='erDiagram\n'
 if p['slug']=='yuyenpensuk':
  model='flowchart TD\n  CMS["db.json document"] --> CONTENT["Content collections"]\n  CMS --> ADMIN["Admin records"]\n  CONTENT -->|"path references"| FILES["External upload files"]\n'
 else:
  for a,b,l in p['links']:model+=f'  {a} ||--o{{ {b} : references\n'
  for name,fields in p['stores']:
   model+=f'  {name} {{\n'
   for i,f in enumerate(fields):model+=f'    string field_{i+1} "{f}"\n'
   model+='  }\n'
 (out/'diagrams'/'data-model.mmd').write_text(model)
 wf='flowchart TD\n'+''.join(f'  N{i}["{t}"]\n' for i,t in enumerate(p['flow']))+''.join(f'  N{i} --> N{i+1}\n' for i in range(len(p['flow'])-1))
 (out/'diagrams'/'workflow.mmd').write_text(wf)
 actors=p['actors'];ctx='flowchart LR\n  U["'+actors[0][0]+'"]\n  S(["0 '+p['title']+'"])\n  U -->|"คำขอและข้อมูลนำเข้า"| S\n  S -->|"ผลลัพธ์ สถานะ หรือข้อผิดพลาด"| U\n'
 if p['slug']=='gold-thai':ctx+='  A["Thai Gold API"]\n  S -->|"คำขอราคาล่าสุด"| A\n  A -->|"JSON หรือ HTTP error"| S\n'
 elif p['slug']=='flood':ctx+='  A["ผู้ดูแลข้อมูลและ provider"]\n  A -->|"ข้อมูลและหลักฐานสิทธิ์ใช้"| S\n  S -->|"ผลนำเข้าและการตรวจคุณภาพ"| A\n'
 elif p['slug']=='yuyenpensuk':ctx+='  A["Editor และ Super Admin"]\n  A -->|"ข้อมูลเนื้อหา ไฟล์ และคำขอแก้ไข"| S\n  S -->|"ผลบันทึกและข้อผิดพลาด"| A\n'
 (out/'diagrams'/'context.mmd').write_text(ctx)
 # Register gives direction and return data that are condensed in exported diagrams.
 flows={
 'vending': [('D01','ผู้ซื้อ','1.0 Catalog','คำขอสินค้า','รายการสินค้าและ stock'),('D02','ผู้ซื้อ','2.0 Order','id และ quantity / redeem','pending order หรือ validation error'),('D03','2.0 Order','D1 Products','อ่านราคาจริงและ stock; ลด/คืน stock','ราคากับ stock ปัจจุบัน'),('D04','2.0 Order','D2 Orders Customers Sessions','สร้าง/อ่าน order; ปรับสถานะ stamp/reward','order และสิทธิ์ของ session'),('D05','ผู้ซื้อ','2.0 Order','pay/cancel พร้อม cookie','paid/cancelled หรือ 404/409')],
 'booking':[('D01','ผู้จอง','1.0 Search','checkin checkout guests kind','รายการห้อง available nights total'),('D02','1.0 Search','D1 Rooms + D2 Bookings','อ่าน capacity ราคา และ confirmed overlaps','ห้องและรายการที่ทับช่วงวัน'),('D03','ผู้จอง','2.0 Booking','room id วันที่และจำนวนคน','booking confirmed หรือ 400/409'),('D04','2.0 Booking','D2 Bookings Sessions','ตรวจเจ้าของและเขียน/ยกเลิก','id status และประวัติ'),('D05','ผู้จอง','2.0 Booking','คำขอประวัติหรือยกเลิกพร้อม cookie','ประวัติตนเอง หรือผลยกเลิก')],
 'yuyenpensuk':[('D01','Visitor','1.0 Public content','ค้นหา brand/id/หน้าเนื้อหา','HTML หรือ 404'),('D02','1.0 Public content','D1 CMS / D2 Uploads','อ่านข้อมูลและไฟล์ที่อ้างอิง','เนื้อหาและ bytes ที่มีอยู่จริง'),('D03','Admin','2.0 CMS','credentials/OTP หรือ content + CSRF + uploads','session ผลบันทึก redirect หรือ error'),('D04','2.0 CMS','D1 CMS','อ่านสิทธิ์และบันทึกเนื้อหา','ข้อมูลปัจจุบันหรือ save error'),('D05','2.0 CMS','D2 Uploads','ตรวจและเขียนไฟล์; cleanup หลัง persist','validated paths หรือ file error')],
 'gold-thai':[('D01','Timer / latest request','1.0 Collect','trigger','sync result หรือ null'),('D02','1.0 Collect','Thai Gold API','HTTP latest request','JSON หรือ HTTP error'),('D03','1.0 Collect','D1 gold_prices','INSERT snapshot','persist result'),('D04','Dashboard','2.0 Query / regression','latest/history/stats request','ราคา history stats หรือ error'),('D05','2.0 Query / regression','D1 gold_prices','อ่าน latest และ non-null sell series','rows ที่เรียง observed_at')],
 'flood':[('D01','Operator / provider','1.0 Validate / ingest','raw source + rights/provenance metadata','receipt / quarantine / validation error'),('D02','1.0 Validate / ingest','D1 Sources Stations + D2 Observations','ตรวจ source และเขียนข้อมูลที่ผ่าน','transaction status / ingest log'),('D03','Dashboard / researcher','2.0 Query / readiness','coordinates Polygon station/time query','geometry metadata observations หรือ unknown'),('D04','2.0 Query / readiness','D1 Sources Stations + D2 Observations','อ่านเฉพาะ source approved และ licensed','series source datum freshness และ gaps'),('D05','2.0 Query / readiness','Model package files / providers','ตรวจแพ็กเกจหรือเรียก provider ตาม endpoint','ผลที่ผ่าน gate หรือ unavailable/rejected')]}
 f=flows[p['slug']]
 dfd='flowchart TD\n'
 # Exact flows mirrored in editable source, with stores separate from processes.
 nodemap={};idx=0
 for row in f:
  for label in row[1:3]:
   if label not in nodemap:nodemap[label]=f'N{idx}';idx+=1
 for label,n in nodemap.items():dfd+=f'  {n}["{label}"]\n'
 for ident,a,b,request,response in f:
  dfd+=f'  {nodemap[a]} -->|"{ident} {request}"| {nodemap[b]}\n  {nodemap[b]} -->|"{response}"| {nodemap[a]}\n'
 (out/'diagrams'/'data-flow.mmd').write_text(dfd)
 md=f'''# {p['title']} เอกสารวิเคราะห์ความต้องการและออกแบบระบบ

รุ่นเอกสาร 1.0 · วันที่ {DATE} · ผู้จัดทำ Panupong Intasan โดยใช้ AI assistance ใน ChatGPT Work

{p['purpose']}

**สถานะเอกสาร:** จัดทำใหม่จากการอ่านโค้ด ณ commit `{p['head']}` เพื่ออธิบายระบบและใช้ตรวจรับ ไม่ใช่บันทึกการสัมภาษณ์หรือหลักฐานว่าผู้มีส่วนได้ส่วนเสียอนุมัติ Requirement แล้ว รายการที่ยังต้องตัดสินใจอยู่ในหัวข้อคำถามยืนยัน

[อ่านฉบับเว็บบน Portfolio](https://intasan.github.io/portfolio/analysis/{p['slug']}/index.html) · [ไฟล์ HTML](analysis.html) · [Diagram source](diagrams/)

## 1 เป้าหมาย ผู้ใช้งาน และขอบเขต

{table(['ผู้เกี่ยวข้อง','หน้าที่'],p['actors'])}

**อยู่ในขอบเขต:** {p['scope']}

**อยู่นอกขอบเขต:** {p['out']}

## 2 วิธีเก็บและยืนยันความต้องการ

เอกสารรอบนี้ใช้ source review, schema review และผลทดสอบที่มีอยู่เป็น input ข้อกำหนดแบบ As implemented ใช้อธิบายพฤติกรรมที่พบในโค้ด ส่วน To be เป็นข้อเสนอหรือคำถามที่ยังไม่ได้อนุมัติ ไม่มีการสร้างชื่อผู้ให้สัมภาษณ์ วันประชุม หรือผลลงนามย้อนหลัง

กระบวนการยืนยันที่เสนอคือให้ผู้ใช้งานหลักทบทวน scope และ Business Rules จากนั้นเดินผ่าน scenario ปกติและข้อผิดพลาด บันทึกคำตอบพร้อมผู้ตัดสินใจ แล้วปรับ version ของ Requirement และ UAT ก่อนรับรองการใช้งานจริง

## 3 Functional Requirements และเกณฑ์ยอมรับ

ทุกแถวต่อไปนี้เป็น **As implemented จากโค้ด** คอลัมน์หลักฐานแยกสิ่งที่มีการทดสอบเดิมกับสิ่งที่เพียงพบใน source การจัดทำเอกสารไม่ได้ทำให้ผลทดสอบที่ยังรออยู่กลายเป็นผ่าน

{table(['รหัส','ความต้องการ','เกณฑ์ยอมรับ','Source','หลักฐานหรือสถานะ'],p['req'])}

## 4 Business Rules

'''+''.join(f'{i+1}. {r}\n' for i,r in enumerate(p['rules']))+f'''
## 5 Non Functional Requirements

{table(['รหัส','ประเด็น','เกณฑ์และสถานะ'],[(p['slug']+'-NFR01','Data integrity','ใช้การตรวจสอบ input และการบันทึกที่สอดคล้องกับ business rules; ดูข้อจำกัดรายโครงการด้านล่าง'),(p['slug']+'-NFR02','Access control','ตรวจสิทธิ์ที่ server ตาม actor และ endpoint; ไม่อ้างสิทธิ์ที่ระบบยังไม่มี'),(p['slug']+'-NFR03','Observability','ต้องอธิบาย error / unavailable และ provenance ที่มีอยู่; audit trail แบบสมบูรณ์ยังไม่ถือว่ามี'),(p['slug']+'-NFR04','Usability','เสนอให้ทดสอบ desktop และ mobile ตั้งแต่ 360 px พร้อม keyboard; ยังไม่มีผลตรวจครบทุกขนาด'),(p['slug']+'-NFR05','Performance','ยังไม่มี SLA ที่ผู้เกี่ยวข้องอนุมัติ ต้องกำหนดจำนวนผู้ใช้และเกณฑ์ response time ก่อน load test'),(p['slug']+'-NFR06','Recovery','เสนอให้ทดสอบสำรองและกู้คืนข้อมูลพร้อมไฟล์ที่สัมพันธ์กัน; RPO/RTO ยังต้องตกลง ไม่กำหนดตัวเลขแทนผู้ใช้')])}

## 6 Context Diagram

![Context Diagram](diagrams/context.svg)

อ่านร่วมกับ [Mermaid context source](diagrams/context.mmd) ซึ่งแสดงข้อมูลขาเข้าและขาออกแยกทิศทาง Context Diagram กำหนดขอบเขตระบบทั้งก้อน ไม่แสดง data store ภายใน

## 7 Data Flow Diagram และทะเบียนข้อมูล

![Data flow process overview](diagrams/data-flow.svg)

ภาพ SVG เป็น process overview แบบย่อ ส่วน [DFD Mermaid source](diagrams/data-flow.mmd) และทะเบียนด้านล่างแสดงทิศทาง request/response และ data store อย่างละเอียด ห้ามตีความลูกศรเป็นลำดับเวลาดำเนินงานอย่างเดียว

{table(['Flow','ต้นทาง','ปลายทาง','ข้อมูลที่ส่งไป','ข้อมูลตอบกลับ'],f)}

## 8 Workflow

![Workflow](diagrams/workflow.svg)

'''+''.join(f'{i+1}. {r}\n' for i,r in enumerate(p['flow']))+f'''
ข้อผิดพลาดต้องส่งผลตาม Requirement ที่เกี่ยวข้องและไม่ข้ามการตรวจสิทธิ์หรือความถูกต้องของข้อมูล [แก้ไข Mermaid workflow](diagrams/workflow.mmd)

## 9 Data Model และ Data Dictionary

![Data model](diagrams/data-model.svg)

{('นี่เป็นแบบจำลองเชิงตรรกะของข้อมูล JSON และไฟล์ ไม่มี SQL table หรือ FK บังคับความสัมพันธ์' if p['slug']=='yuyenpensuk' else 'แบบจำลองแสดง core entities ตาม schema ที่ตรวจอ่าน ความสัมพันธ์ที่แอปคาดหวังอาจเข้มกว่าข้อจำกัด nullable ของฐานข้อมูล จึงต้องอ่าน DDL และ validation ประกอบ')}

{table(['Entity หรือ data store','ข้อมูลหลัก'],[(a,'; '.join(b)) for a,b in p['stores']])}

'''
 if p['slug']=='vending':md+='`orders.items` เก็บ JSON text ของรายการ id/name/price/quantity ซึ่งเป็น snapshot ณ เวลาสั่ง ไม่มีตาราง order_items และไม่มี FK ระหว่าง JSON กับ products แม้แอปจะตรวจ id ก่อนบันทึก\n\n'
 if p['slug']=='flood':md+='ERD นี้เลือกแสดง observation path เท่านั้น ตาราง `river_reaches` มี downstream self reference และ `model_runs` เก็บ metadata ตาม DDL ไม่ได้หมายความว่า pipeline hydraulic model ทำงานแล้ว ส่วน model gate ใช้แพ็กเกจไฟล์แยกจากตารางดังกล่าว\n\n'
 if p['slug']=='gold-thai':md+='มีตารางหลักเดียว ไม่มีความสัมพันธ์ระหว่างตาราง; UNIQUE ใช้ source กับ observed_at ไม่ใช่ upstream announcement ID\n\n'
 md+=f'''{table(['Parent','Child','Relationship'],p['links']) if p['links'] else 'Single table model ไม่มีความสัมพันธ์ระหว่างตาราง'}

[Mermaid data model source](diagrams/data-model.mmd)

## 10 UAT และ Requirement Traceability

ตารางนี้เป็น test design และ mapping กับหลักฐานที่มี การผ่าน unit/API test ไม่เท่ากับผู้ใช้ปลายทางลงนาม UAT

{table(['Test ID','Requirement','ขั้นตอนหรือ input','ผลคาดหวัง','สถานะหลักฐาน'],p['uat'])}

**ผู้ตรวจรับ:** ยังไม่กำหนด · **วันที่ตรวจรับกับผู้ใช้:** ยังไม่ดำเนินการในรอบเอกสารนี้ · **ผลลงนาม:** ยังไม่มี

## 11 ข้อจำกัดและความเสี่ยง

'''+''.join(f'- {r}\n' for r in p['risks'])+'''\n## 12 คำถามที่ต้องยืนยันก่อนขยายระบบ

'''+''.join(f'{i+1}. {r}\n' for i,r in enumerate(p['questions']))+'''\n## 13 Source Baseline และประวัติเอกสาร

'''+''.join(f'- [{s}]({source(p,s)})\n' for s in p['sources'])+f'''
| Version | วันที่ | รายการเปลี่ยนแปลง |
| --- | --- | --- |
| 1.0 | {DATE} | จัดทำ requirement catalogue, data flow register, diagrams, data dictionary และ UAT traceability จาก source baseline |

เอกสารวิเคราะห์และไดอะแกรมเป็น deliverable ใหม่ ไม่ใช่ภาพหน้าจอหรือหลักฐานผลการทำงานที่ยังไม่ได้ทดสอบ ไม่มีการอ่านหรือแก้ repository ที่ผู้ใช้ระบุให้ยกเว้น
'''
 (out/'README.md').write_text(md)
 (out/'manifest.json').write_text(json.dumps({k:p[k] for k in ['title','repo','slug','head']}|{'document_version':'1.0','date':'2026-10-30','requirements':len(p['req']),'diagrams':list(figs)},ensure_ascii=False,indent=2)+'\n')
print('Generated',len(P),'analysis packs;',sum(len(p['req']) for p in P),'requirements;',len(P)*4,'SVG diagrams')

# Typed editable ERDs use actual column names, avoiding invented normalized tables.
SCHEMAS={
 'vending': {'CUSTOMERS':[('TEXT','id','PK'),('INTEGER','visits',''),('INTEGER','rewards','')], 'SESSIONS':[('TEXT','token','PK'),('TEXT','customer','FK')], 'ORDERS':[('TEXT','id','PK'),('TEXT','customer','FK'),('TEXT','items',''),('INTEGER','total',''),('TEXT','status',''),('INTEGER','redeemed',''),('TEXT','created_at','')], 'PRODUCTS':[('TEXT','id','PK'),('TEXT','name',''),('TEXT','flavour',''),('INTEGER','price',''),('INTEGER','stock',''),('TEXT','color','')]},
 'booking': {'ROOMS':[('TEXT','id','PK'),('TEXT','name',''),('TEXT','kind',''),('INTEGER','price',''),('INTEGER','capacity',''),('TEXT','description','')], 'SESSIONS':[('TEXT','token','PK')], 'BOOKINGS':[('TEXT','id','PK'),('TEXT','session','FK'),('TEXT','room','FK'),('TEXT','checkin',''),('TEXT','checkout',''),('INTEGER','guests',''),('INTEGER','total',''),('TEXT','status',''),('TEXT','created_at','')]},
 'gold-thai': {'GOLD_PRICES':[('INTEGER','id','PK'),('TEXT','source',''),('TEXT','observed_at',''),('TEXT','update_date',''),('TEXT','update_time',''),('REAL','goldbar_buy',''),('REAL','goldbar_sell',''),('REAL','ornament_buy',''),('REAL','ornament_sell',''),('REAL','spot',''),('REAL','thb',''),('REAL','change','')]},
 'flood': {'SOURCES':[('text','id','PK'),('text','title',''),('text','url',''),('text','license_evidence',''),('text','approval_status','')], 'STATIONS':[('text','id','PK'),('text','source_id','FK'),('geometry','location',''),('text','vertical_datum',''),('jsonb','metadata','')], 'OBSERVATIONS':[('text','station_id','PK, FK'),('timestamptz','observed_at','PK'),('timestamptz','ingested_at',''),('double','value',''),('text','unit',''),('text','raw_sha256',''),('jsonb','metadata','')], 'INGEST_LOG':[('bigserial','id','PK'),('text','source_id','FK'),('timestamptz','started_at',''),('text','status',''),('text','raw_sha256',''),('text','detail','')]}
}
for p in P:
 if p['slug'] not in SCHEMAS:continue
 m='erDiagram\n'
 for parent,child,label in p['links']:
  cardinality='||' if child=='OBSERVATIONS' else '|o'
  m+=f'  {parent} {cardinality}--o{{ {child} : references\n'
 for name,fields in SCHEMAS[p['slug']].items():
  m+=f'  {name} {{\n'
  for typ,name_,key in fields:m+=f'    {typ} {name_} {key}\n'
  m+='  }\n'
 (ROOT/p['repo']/'docs/analysis/diagrams/data-model.mmd').write_text(m)
