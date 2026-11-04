"""Content-only final acceptance updates; preserve the existing cosmic presentation."""
from pathlib import Path
import json,re,html,runpy,hashlib
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'projects.json').read_text());P={p['id']:p for p in D};C=json.loads((R/'docs/case-study-content.json').read_text())
def sec(id,title,body):return f'<section id="{id}"><h2>{title}</h2>{body}</section>'
def replace_section(pid,id,title,body):
 block=sec(id,title,body);pattern=rf'<section id="{id}">.*?</section>'
 C[pid]=re.sub(pattern,lambda m:block,C[pid],flags=re.S) if re.search(pattern,C[pid]) else C[pid]+block
shots=[('home','หน้าแรก / Public homepage'),('products','หน้ารวมสินค้า / Product catalog'),('product-detail','รายละเอียดสินค้า / Product detail'),('services','หน้าบริการ / Services'),('projects','หน้าผลงาน / Company projects'),('admin-login','หน้าเข้าสู่ระบบ / Admin login')]
P['yuyenpensuk']['images']=[{'src':f'evidence/acceptance/yuyenpensuk/{k}.jpg','caption':f'ภาพ Browser จริง 3 พ.ย. 2569: {label} · ยืนยันการแสดงผลหน้าเว็บ ไม่รับรองข้อมูลธุรกิจในภาพ'} for k,label in shots]
P['gold-trading']['kind']='Concept / In Progress · 2026'
fix={
'motoinsight':dict(title='MotoInsight — Scraping & Data Preparation',desc='Source Python สำหรับอ่านรายการรถจักรยานยนต์จาก CheckRaka ทำความสะอาด CSV และสรุปข้อมูล ยังไม่มี Dashboard หรือผล Dataset ที่ตรวจยืนยัน',features=['CheckRaka HTML parser','CSV export','Duplicate removal','Missing-value handling','Descriptive summary'],tech=['Python','Pandas','Requests','BeautifulSoup'],role='ศึกษาการแยกข้อมูลจาก HTML และจัดเตรียม CSV เพื่อใช้วิเคราะห์ต่อ',flow=['อ่าน HTML','แยกข้อมูลและลิงก์','ส่งออก CSV','ทำความสะอาด','สรุปข้อมูล']),
'gesture':dict(desc='Source สำหรับอ่านภาพ ปรับขนาด และเตรียม Label จากโฟลเดอร์ ยังไม่มีโมเดลจำแนกหรือผลประเมินที่ยืนยัน',features=['Read images with OpenCV','Resize to 224 × 224','Normalize pixels','Load folder labels'],tech=['Python','OpenCV','NumPy'],role='ศึกษาการเตรียมภาพและ Label สำหรับงานจำแนกท่าทางมือ',flow=['อ่านโฟลเดอร์ภาพ','ปรับขนาด','Normalize','เตรียมภาพและ Label']),
'social':dict(desc='Flutter UI shell และ Service wrappers ที่สร้างใหม่สำหรับแนวคิด Social App ส่วน Feed, Profile, Post, Like และ Comment ยังเป็นขอบเขตที่ต้องเชื่อมต่อและพัฒนาต่อ',features=['Flutter Material UI shell','Authentication service wrapper','Firestore service wrapper'],tech=['Dart','Flutter','Firebase service interfaces'],role='จัดโครงสร้าง UI shell และแนวทางเชื่อม Service สำหรับต้นแบบที่สร้างใหม่',flow=['เปิด UI shell','วาง Service interfaces','เชื่อมต่อ Backend ในขั้นต่อไป']),
'clothesline':dict(desc='Source Arduino อ่านค่าฝนจาก A0 และสั่งมอเตอร์หุบราวเมื่อค่าต่ำกว่า Threshold ยังไม่มีผลทดสอบกับอุปกรณ์จริง',features=['Analog rain-sensor input','Threshold-based retraction','Timed motor control','Serial logging'],tech=['Arduino','C++','Analog sensor','Motor control'],role='ออกแบบเงื่อนไขอ่านเซนเซอร์และควบคุมมอเตอร์ใน Source งานรายวิชา',flow=['อ่าน A0','เทียบ Threshold','ฝนตก: หุบราว','หยุดมอเตอร์']),
'system-design':dict(role='จัดทำและรวบรวม Source งานรายวิชา: SQL schema การรับเลี้ยงสัตว์ เอกสารกระบวนการ และโค้ดควบคุมอุปกรณ์'),
}
for pid,fields in fix.items():
 P[pid].update(fields)
 for id,title,body in [('overview','Project overview','<p>'+html.escape(P[pid]['desc'])+'</p>'),('responsibilities','My responsibilities','<p>'+html.escape(P[pid]['role'])+'</p>'),('implementation','Implementation scope','<ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in P[pid]['features'])+'</ul>'),('workflow','System workflow','<ol class="flow">'+''.join('<li>'+html.escape(x)+'</li>' for x in P[pid]['flow'])+'</ol>')]:replace_section(pid,id,title,body)
replace_section('yuyenpensuk','testing','Testing & validation','<p>รอบ Final Review เปิดหน้าบ้านและ Admin Login จริงแบบอ่านอย่างเดียว และรัน Unit Tests ของ Security Headers ผ่าน 2 กรณีบน Source ที่ตรวจ ส่วน CRUD, Upload, การบังคับสิทธิ์, 2FA และ Persistence บน Production ยังไม่ได้ทดสอบในรอบนี้</p><p>Source ที่อ่านไม่ใช่หลักฐานว่า Binary บน VPS ตรงกับ Commit นี้ จึงไม่รับรอง Production Ready จากการตรวจหน้าจอ</p>')
replace_section('yuyenpensuk','acceptance-docs','Source-derived requirements & API documentation','<p>เอกสารเสริมรอบตรวจรับระบุ Source Commit, Requirement Traceability, User Stories, Acceptance Criteria, Endpoint Catalogue และ Sequence Diagram แยกจากบันทึกเก็บ Requirement กับเจ้าของบริษัท</p><a href="../analysis/yuyenpensuk/acceptance.html">Read source-derived specification ↗</a>')
replace_section('yuyenpensuk','evidence','Real browser captures','<p>ภาพต่อไปนี้จับจากเว็บไซต์จริงเมื่อ 3 พฤศจิกายน 2569 ไม่ได้สร้างข้อมูลเพิ่ม รายการ Test/test ที่พบใน Production และข้อความการตลาดภายในภาพไม่ได้ถูกนำมาอ้างเป็นผลงานติดตั้งหรือผลลัพธ์ของผู้พัฒนา</p>'+''.join(f'<figure><a href="../{im["src"]}"><img src="../{im["src"]}" alt="{html.escape(im["caption"])}" loading="lazy" style="width:100%;height:auto"></a><figcaption>{html.escape(im["caption"])}</figcaption></figure>' for im in P['yuyenpensuk']['images']))
C['yuyenpensuk']=re.sub(r'<p class="fine">แสดงเอกสารแทนภาพหน้าจอ.*?</p>','',C['yuyenpensuk'])
replace_section('yuyenpensuk','limitations','Limitations','<p>Admin Dashboard, Product Management, Content Management และ Company Management ยังไม่มีภาพจาก Session ที่ยืนยันตัวตนในรอบนี้ หน้า Login เปิดได้ แต่ Browser ไม่มี Session ที่เข้าสู่ระบบ จึงไม่กล่าวอ้างว่าทดสอบหลังบ้านแล้ว</p>')
replace_section('gold-trading','scope','Concept / In Progress','<p>สิ่งที่มีจริงใน Repository: README และหน้า HTML แนะนำแนวคิด พร้อมเอกสารขอบเขต ยังไม่มี Source ETL, Airflow DAG, Database schema, Feature Engineering, ML training หรือ Dashboard ที่เชื่อมข้อมูลจริง</p><p>หน้าแนะนำเดิมใน Repository ไม่ใช่หลักฐานการรัน Pipeline หรือผลประเมินโมเดล ตัวเลขเก่าไม่ถูกนำมาใช้ใน Portfolio</p>')
replace_section('gold-trading','proposal','Proposed technical scope','<p>Objective: explore a traceable gold-price dataset for analysis. Proposed flow: approved market sources → raw observations → validation and normalization → analytical storage → features → chronological evaluation → dashboard.</p><ul><li>Data sources: candidate sources require access, licensing, timestamp and unit checks; no integrated source is verified.</li><li>Architecture / ETL / database: design direction only; no executable implementation or schema is supplied.</li><li>Feature engineering: proposed indicators and market covariates require reproducible input series; no generated feature dataset is verified.</li><li>ML: no trained model or forecast output is verified. No model family is claimed as implemented.</li><li>Evaluation methodology: proposed chronological holdout or walk-forward validation, leakage checks, and a simple baseline before reporting MAE/RMSE. No score is available.</li><li>Dashboard: concept presentation only; no live analytical dashboard is verified.</li></ul>')
# Add an actual SQL-based ERD instead of claiming generic coursework examples as implementation.
replace_section('adoption','data-model','Source-derived relational model','<p>อ้างอิง animal-adoption/schema.sql: animals และ adopters มี Primary Key ของตนเอง ส่วน adoption_requests อ้าง animal_id และ adopter_id ด้วย Foreign Key เป็นการออกแบบ Schema ไม่ใช่หลักฐานว่า Backend หรือฐานข้อมูล Production เปิดใช้งานแล้ว</p><a href="../analysis/adoption/erd.svg"><img src="../analysis/adoption/erd.svg" alt="ERD จาก SQL schema ระบบรับเลี้ยงสัตว์" style="width:100%;height:auto" loading="lazy"></a>')
for pid in ['space','booking','vending']:
 # Keep these captures as historical evidence in Git, not public showcase imagery.
 P[pid]['images']=[]
 C[pid]=re.sub(r'<section id="evidence">.*?</section>','',C[pid],flags=re.S)
for p in D:
 p['images']=[im for im in p.get('images',[]) if 'test-log-view' not in im['src'] and 'database-api-log-view' not in im['src']]
 C[p['id']]=re.sub(r'<figure>.*?(?:test-log-view|database-api-log-view).*?</figure>','',C[p['id']],flags=re.S) if p['id'] in ['flood','gold-thai'] else C[p['id']]
(R/'projects.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');(R/'docs/case-study-content.json').write_text(json.dumps(C,ensure_ascii=False,indent=2))
# Generate within baseline wrappers; no visual source changes.
runpy.run_path(str(R/'tools/update_content.py'),run_name='__main__')
# Metadata overwritten by the baseline updater must reflect acceptance status.
D=json.loads((R/'projects.json').read_text());next(p for p in D if p['id']=='gold-trading')['kind']='Concept / In Progress · 2026'
(R/'projects.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');(R/'projects.js').write_text('window.PORTFOLIO_PROJECTS='+json.dumps(D,ensure_ascii=False,indent=2)+';\n')
s=(R/'index.html').read_text();s=s.replace('src="analysis/yuyenpensuk/diagrams/data-flow.svg" alt="Data flow ของเว็บไซต์และ CMS จัดทำจาก Source Code ไม่ใช่ภาพหน้าจอ"','src="evidence/acceptance/yuyenpensuk/home.jpg" alt="ภาพหน้าแรกเว็บไซต์ Yuyenpensuk จับจาก Browser จริง 3 พฤศจิกายน 2569"',1).replace('SOURCE-DERIVED DOCUMENTATION</span><span>Yuyenpensuk','REAL BROWSER CAPTURE</span><span>Yuyenpensuk',1).replace('projects.js?v=20261103-content','projects.js?v=20261103-acceptance')
# Preserve Hero completely. Resume downloads live on the existing CV page.
for item in D:
 pattern=r'(<a class="project"[^>]*href="case-studies/'+item['id']+r'\.html"[^>]*>)(.*?)(</a>)'
 def fallback(m):
  text=re.sub(r'<strong>.*?</strong>','<strong>'+html.escape(item['title'])+'</strong>',m[2])
  text=re.sub(r'<small>.*?</small>','<small>'+html.escape(item['kind'])+'</small>',text)
  return m[1]+text+m[3]
 s=re.sub(pattern,fallback,s)
(R/'index.html').write_text(s)
print('Final acceptance content prepared')

# Apply the verified Gold implementation after historical acceptance transforms.
import runpy
runpy.run_path(str(R/'tools/update_gold_implementation.py'),run_name='__main__')
