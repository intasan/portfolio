"""Update content within the existing cosmic design. Hero and visual assets remain unchanged."""
from pathlib import Path
import subprocess,json,re,html
R=Path(__file__).resolve().parent.parent
baseline='177e84cbb2068d07c45d717e6a8aee8917e3c4ca'
def original(p):return subprocess.check_output(['git','-C',str(R),'show',baseline+':'+p]).decode()
def e(s):return html.escape(s,quote=True)
D=json.loads((R/'projects.json').read_text());P={p['id']:p for p in D};C=json.loads((R/'docs/case-study-content.json').read_text())
P['yuyenpensuk'].update(title='Yuyenpensuk Website & CMS',desc='เว็บไซต์แสดงสินค้าและบริการของบริษัทอยู่เย็นเป็นสุข วิศวกรรม พร้อม CMS สำหรับทีมงาน ไม่รวม Checkout หรือรับชำระเงินอัตโนมัติ',tech=['Node.js','Express','EJS','JavaScript','JSON file storage','Docker'])
P['gold-trading'].update(kind='Concept Study · 2026',desc='แนวคิดระบบรวบรวมและวิเคราะห์ราคาทองคำ ปัจจุบันมีเอกสารและหน้าแนะนำโครงการ',role='จัดทำกรอบแนวคิดและหน้าอธิบายโครงการด้านการรวบรวมและวิเคราะห์ราคาทองคำ',features=['Project concept','Data integration scope'],tech=['HTML','Markdown'],flow=['กำหนดโจทย์ข้อมูล','วางกรอบการรวบรวม','วางแนวทางวิเคราะห์'])
P['system-design'].update(desc='เอกสารวิเคราะห์ระบบและ SQL schema สำหรับระบบหาบ้านให้สัตว์ พร้อม Source ควบคุมราวตากผ้าอัตโนมัติ',features=['System analysis document','Animal adoption SQL schema','IoT clothesline source'],tech=['SQL','Database Design','System Analysis','Arduino'],flow=['กำหนดขอบเขต','วิเคราะห์ผู้ใช้และข้อมูล','ออกแบบ schema','จัดทำเอกสาร'])
for p in D:
 text=C[p['id']]
 m=re.search(r'<section id="deliverables"><h2>.*?</h2><p>(.*?)</p>',text)
 if m:p['result']=html.unescape(re.sub('<[^>]+>','',m[1]))
 p.pop('limit',None) # preserved in docs/internal/PROJECT_METADATA_20261103.json
 # Keep design baseline wrapper, typography and existing effects stylesheet.
 old=original('case-studies/'+p['id']+'.html')
 prefix=old.split('<article class="detail">')[0]
 prefix=re.sub(r'<title>.*?</title>', '<title>'+e(p['title'])+' | Panupong Intasan</title>',prefix)
 prefix=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+e(p['desc'])+'">',prefix)
 suffix=old.split('</article>',1)[1]
 # Shared current design; source-derived sections are content only.
 text=re.sub(r'<h2>(.*?)</h2>',r'<h2 class="label">\1</h2>',text)
 text=text.replace('class="button solid"','class="btn primary"').replace('class="text-link"','class="work-link"').replace('class="fine"','class="caption"')
 text=text.replace('width="1440" height="900"','style="width:100%;height:auto"').replace('width="1100" height="540"','style="width:100%;height:auto"')
 # Use existing detail layout and classes; no new design stylesheet.
 title=f'<div class="eyebrow">{e(p["kind"])}</div><h1 style="font-size:clamp(2.5rem,6vw,5rem);line-height:1.15;margin:20px 0">{e(p["title"])}</h1><p>{e(p["desc"])}</p><div class="tags">'+''.join(f'<span class="tag">{e(t)}</span>' for t in p['tech'])+'</div>'
 (R/'case-studies'/f'{p["id"]}.html').write_text(prefix+'<article class="detail">'+title+text+'</article>'+suffix)
(R/'projects.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
(R/'projects.js').write_text('/* Content data; audit history remains in docs/internal. */\nwindow.PORTFOLIO_PROJECTS='+json.dumps(D,ensure_ascii=False,indent=2)+';\n')
s=original('index.html')
# Replace only the Featured Projects content, preserving section classes/layout.
start=s.index('<article class="featured-work');end=s.index('<div class="rule" style="padding-top:20px">',start)
features=''
for pid,label,summary in [
 ('yuyenpensuk','SOURCE-DERIVED DOCUMENTATION','โจทย์: ให้บริษัทปรับสินค้าและบริการได้ผ่าน CMS · วิเคราะห์: คุยกับเจ้าของและออกแบบ Workflow · พัฒนา: Node.js / Express, JSON และ Uploads · ส่งมอบ: เว็บไซต์และเอกสารระบบ'),
 ('gold-trading','CONCEPT STUDY','โจทย์: จัดโครงสร้างข้อมูลเพื่อศึกษาราคาทอง · วิธีการ: วางกรอบ Data Integration และแนวทางวิเคราะห์ · ชิ้นงานปัจจุบัน: เอกสารแนวคิด ยังไม่มี ETL หรือโมเดลที่รันได้ใน Repository'),
 ('agricultural','REPOSITORY SCREENSHOT','โจทย์: รวมราคาต่างแหล่งโดยรักษาหน่วยและประเภทการวัด · พัฒนา: Airflow → Validation → PostgreSQL → Streamlit · ผลลัพธ์: Dashboard และชุดหลักฐานตรวจข้อมูลจาก DIT, NABC และตลาดไท')]:
 p=P[pid]
 if pid=='yuyenpensuk':img='<img src="analysis/yuyenpensuk/diagrams/data-flow.svg" alt="Data flow ของเว็บไซต์และ CMS จัดทำจาก Source Code ไม่ใช่ภาพหน้าจอ" loading="lazy" style="object-fit:contain" width="1363" height="936">'
 elif pid=='agricultural':img=f'<img src="{e(p["images"][0]["src"])}" alt="Dashboard ราคาสินค้าเกษตรจากชุดหลักฐานใน Repository" loading="lazy" style="object-fit:contain" width="1363" height="936">'
 else:img='<div style="padding:32px;align-self:center"><div class="eyebrow">CONCEPT STUDY</div><h3>Gold Trading<br>Analytics</h3><p>เอกสารแนวคิด · ไม่ใช่ Dashboard หรือผลพยากรณ์</p></div>'
 features+=f'<article class="featured-work reveal"><a class="work-visual" href="case-studies/{pid}.html" data-project="{pid}" aria-label="ดู {e(p["title"])}">{img}<div class="visual-label"><span>{label}</span><span>{e(p["title"])}</span></div></a><div class="work-copy"><div class="eyebrow">PROJECT OVERVIEW</div><h3>{e(p["title"])}</h3><p>{e(summary)}</p><a class="work-link" href="case-studies/{pid}.html" data-project="{pid}">ดูกรณีศึกษา ↗</a></div></article>'
s=s[:start]+features+s[end:]
# Existing education/document section: enrich with actual document links only.
needle='<section class="content paper document-section" id="experience">'
a=s.index(needle);z=s.index('</section>',a)
sec=s[a:z]
sec=sec.replace('พร้อมตัวอย่างโครงงานและกรณีศึกษาที่เกี่ยวข้อง','พร้อมเอกสารวิเคราะห์จาก Source Code ที่ระบุ Baseline และสถานะ UAT อย่างชัดเจน')
sec=sec.replace('ดูผลงานและกรณีศึกษา</a>','ดูผลงานและกรณีศึกษา</a><p><a class="work-link" href="analysis/yuyenpensuk/index.html">Requirements · DFD · Logical Data Model · UAT ↗</a></p><p><a class="work-link" href="analysis/index.html">เอกสาร BA / SA ทั้งหมด ↗</a></p>')
s=s[:a]+sec+s[z:]
# Correct unsubstantiated skills in body only; hero remains byte-identical.
s=s.replace('Requirements Gathering · BRD · As-Is / To-Be · Gap Analysis · Feasibility Study · Acceptance Criteria · UAT Planning','Requirements Gathering · Functional Requirements · Business Rules · Workflow · Acceptance Criteria · UAT Planning')
s=s.replace('Use Case · UML · DFD · ERD · Database Design · Normalization · REST API · System Flow · Wireframe','DFD · Logical Data Model · SQL Schema · Database Design · REST API · System Flow')
s=s.replace('SQL · Python · Pandas · Data Cleaning · Data Validation · Visualization · PostgreSQL · Excel / Sheets · ETL / Airflow','SQL · Python · Pandas · Data Cleaning · Data Validation · Visualization · PostgreSQL · ETL / Airflow')
s=s.replace('ศึกษาสาขาเทคโนโลยีสารสนเทศ มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน อยู่ระหว่างยืนยันสถานะสำเร็จการศึกษาและเอกสารทางการ พร้อมเริ่มงานเดือนพฤศจิกายน 2569','สำเร็จการศึกษาสาขาเทคโนโลยีสารสนเทศ มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน พร้อมเริ่มงานเดือนพฤศจิกายน 2569')
s=s.replace('เครื่องมือที่ใช้: Figma, Draw.io, Postman, Git / GitHub, VS Code, PowerPoint และ Generative AI สำหรับช่วยค้นคว้าและจัดทำงาน โดยตรวจสอบผลก่อนใช้','ใช้ GitHub, Airflow, Docker และ ChatGPT Work ช่วยพัฒนาและจัดทำเอกสาร โดยตรวจ Source Code และผลลัพธ์ก่อนนำเสนอ')
# No structural edits to navigation, hero, effects or motion controls.
s=s.replace('src="projects.js"','src="projects.js?v=20261103-content"')
(R/'index.html').write_text(s)
# Preserve full assessment, repair its content link and metadata.
s=original('ppe-case-study.html').replace('index.html#project=ppe','case-studies/ppe.html')
if 'name="description"' not in s:s=s.replace('<title>','<meta name="description" content="BA assessment: PPE inspection requirements, acceptance criteria and UAT planning"><title>',1)
(R/'ppe-case-study.html').write_text(s)
print('Updated content within existing cosmic design')
