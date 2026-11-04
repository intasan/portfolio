"""Add only verified Yuyenpensuk content/evidence; preserve existing visual wrappers."""
from pathlib import Path
import json,re,html,hashlib
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'projects.json').read_text());p=next(x for x in D if x['id']=='yuyenpensuk');C=json.loads((R/'docs/case-study-content.json').read_text())
source='https://raw.githubusercontent.com/intasan/yuyenpensuk-website/d690c5d215d7e159200b83fc686c1f91e8ced35e/evidence/acceptance-20261104/'
admin=[{'src':source+file,'caption':caption} for file,caption in [
 ('admin-dashboard.jpg','ภาพ Production หลัง Login จริง 4 พ.ย. 2569: Admin Dashboard · ตรวจการแสดงผล ไม่ใช่ผลผ่าน CRUD/UAT'),
 ('admin-products.jpg','ภาพจริง 4 พ.ย. 2569: Product Management · รายการสินค้าและตัวกรอง'),
 ('admin-product-images.jpg','ภาพจริง 4 พ.ย. 2569: ส่วนรูปภาพใน Product Editor · ยังไม่ได้ทดสอบอัปโหลดหรือกดบันทึก'),
 ('admin-company-cms.jpg','ภาพจริง 4 พ.ย. 2569: Company Homepage CMS · เปิดดูแบบอ่านอย่างเดียว'),
 ('admin-services.jpg','ภาพจริง 4 พ.ย. 2569: Service Management · ไม่ยืนยันการบันทึกแก้ไข'),
 ('admin-news.jpg','ภาพจริง 4 พ.ย. 2569: News Management · ข้อมูลในภาพเป็นเนื้อหาที่มีอยู่ใน CMS')]]
old=[{'src':f'evidence/acceptance/yuyenpensuk/{k}.jpg','caption':f'ภาพ Browser จริง 3 พ.ย. 2569: {label} · ภาพการแสดงผลหน้าที่เปิดตรวจ'} for k,label in [('home','Public homepage'),('products','Product catalog'),('product-detail','Product detail'),('services','Services'),('projects','Company projects'),('admin-login','Admin login')]]
# Six existing gallery slots retain the presentation; all twelve captures remain in the case study.
p['images']=[old[0],admin[0],admin[1],admin[3],admin[2],old[1]]
def section(id,title,body):
 global C
 text='<section id="'+id+'"><h2>'+title+'</h2>'+body+'</section>';pat=r'<section id="'+id+r'">.*?</section>'
 C['yuyenpensuk']=re.sub(pat,lambda m:text,C['yuyenpensuk'],flags=re.S) if re.search(pat,C['yuyenpensuk']) else C['yuyenpensuk']+text
section('testing','Testing & validation','<p>4 November 2026: authenticated read-only inspection opened all 12 primary admin menu pages, product brands and an existing product editor. DAIKIN filtering returned 5 visible rows; searching FTKF returned 1; a no-match search returned 0.</p><p>Thirteen public HTTP GET checks returned 200 and fourteen anonymous admin GET checks redirected to login. Two security-header unit tests passed for header logic. These observations do not establish CRUD, upload, editor-role enforcement, restart persistence or owner UAT acceptance.</p>')
section('acceptance-docs','Requirements & acceptance traceability','<p>Source-derived requirements map the public website and CMS workflow to implementation files and acceptance criteria. They are implementation-analysis documents, not signed stakeholder approval.</p><p><a href="../analysis/yuyenpensuk/acceptance.html">Read requirements, API and sequence documentation ↗</a></p><p><a href="https://github.com/intasan/yuyenpensuk-website/blob/main/docs/acceptance/REQUIREMENT_TRACEABILITY.md">Read updated requirement-to-acceptance traceability ↗</a></p>')
section('evidence','Real public and authenticated CMS captures','<p>Public captures are dated 3 November 2026; authenticated admin captures are dated 4 November 2026. They show the actual running website, with no generated UI or added business records. Company news, promotions and installation records shown are CMS content, not claims of work personally performed by the developer.</p>'+''.join('<figure><a href="'+(im['src'] if im['src'].startswith('https:') else '../'+im['src'])+'"><img src="'+(im['src'] if im['src'].startswith('https:') else '../'+im['src'])+'" alt="'+html.escape(im['caption'])+'" loading="lazy" style="width:100%;height:auto"></a><figcaption>'+html.escape(im['caption'])+'</figcaption></figure>' for im in old+admin))
section('limitations','Verification scope','<p>Authenticated navigation, search and existing forms are verified. Actual changes to production data, uploads, backup/restore, editor permissions, restart persistence and TOTP login/recovery remain pending. Screenshots of editor controls are not proof of a successful save or upload. No Production Ready or completed owner UAT claim is made.</p>')
(R/'projects.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');(R/'projects.js').write_text('window.PORTFOLIO_PROJECTS='+json.dumps(D,ensure_ascii=False,indent=2)+';\n');(R/'docs/case-study-content.json').write_text(json.dumps(C,ensure_ascii=False,indent=2))
f=R/'case-studies/yuyenpensuk.html';s=f.read_text();prefix=s.split('<article class="detail">')[0];suffix=s.split('</article>',1)[1];oldarticle=s.split('<article class="detail">',1)[1].split('</article>',1)[0];title=oldarticle.split('<section ',1)[0]
body=re.sub(r'<h2>(.*?)</h2>',r'<h2 class="label">\1</h2>',C['yuyenpensuk']).replace('class="button solid"','class="btn primary"').replace('class="fine"','class="caption"');f.write_text(prefix+'<article class="detail">'+title+body+'</article>'+suffix)
f=R/'index.html';s=f.read_text();s=re.sub(r'projects\.js\?v=[^"\s]+','projects.js?v='+hashlib.sha256((R/'projects.js').read_bytes()).hexdigest()[:12],s);f.write_text(s)
print('Yuyenpensuk real evidence updated; theme, hero, layout and effects preserved')
