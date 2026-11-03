from pathlib import Path
import re,html,json
R=Path(__file__).resolve().parents[1]
def write(p,s):f=R/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s)
def svg(title,boxes,edges,w=1120,h=600):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#566677"/></marker></defs><rect width="100%" height="100%" fill="#fbfcfe"/><g font-family="Arial,sans-serif" fill="#182b3d"><text x="30" y="40" font-size="23">{title}</text><text x="30" y="65" font-size="13">Source-derived analysis · 3 November 2026 · Not a runtime screenshot</text>'
 for x1,y1,x2,y2,label in edges:s+=f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#566677" fill="none" marker-end="url(#a)"/><text x="{(x1+x2)/2}" y="{(y1+y2)/2-10}" text-anchor="middle" font-size="13">{html.escape(label)}</text>'
 for x,y,bw,bh,lines in boxes:
  s+=f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="5" fill="#edf1f6" stroke="#7890a3"/>'
  for i,line in enumerate(lines):s+=f'<text x="{x+15}" y="{y+29+i*25}" font-size="15">{html.escape(line)}</text>'
 return s+'</g></svg>'
write('analysis/adoption/erd.svg',svg('Animal Adoption — SQL ERD',[(30,130,300,180,['animals','PK id','name, species, status','description']),(410,350,310,210,['adoption_requests','PK id','FK animal_id → animals.id','FK adopter_id → adopters.id','status, created_at']),(790,130,300,180,['adopters','PK id','name','UNIQUE email'])],[(180,310,410,390,'one animal : many requests'),(940,310,720,390,'one adopter : many requests')]))
write('analysis/adoption/erd.mmd','''erDiagram
 animals ||--o{ adoption_requests : receives
 adopters ||--o{ adoption_requests : submits
 animals { int id PK\n varchar name\n varchar species\n varchar status\n text description }
 adopters { int id PK\n varchar name\n varchar email UK }
 adoption_requests { int id PK\n int animal_id FK\n int adopter_id FK\n varchar status\n timestamp created_at }
''')
write('analysis/yuyenpensuk/diagrams/use-cases.svg',svg('Yuyenpensuk — Implemented Use Cases',[(30,150,200,120,['Visitor','Public browsing']),(30,370,200,120,['Authenticated admin','Role checked server-side']),(400,110,320,180,['Public website','Browse/search products','View details/services/projects','Read contact information']),(400,360,320,170,['CMS','Manage content & company','Upload validated files','Manage own profile']),(820,360,270,170,['Super Admin only','Manage admin accounts','After authentication'])],[(230,200,400,200,'requests'),(230,420,400,420,'authorized actions'),(720,430,820,430,'role restriction')]))
# Sequence uses explicit lifelines and time order, not claimed as a trace capture.
s=svg('Yuyenpensuk — Content Save Sequence',[(30,110,220,65,['Admin browser']),(310,110,220,65,['Express / admin route']),(590,110,220,65,['database.js']),(870,110,220,65,['db.json / uploads'])],[],h=650)
s=s.replace('</g></svg>','')
for x in [140,420,700,980]:s+=f'<line x1="{x}" y1="175" x2="{x}" y2="610" stroke="#7890a3" stroke-dasharray="5 5"/>'
for y,a,b,label in [(230,140,420,'POST content + CSRF + optional files'),(310,420,700,'Validate auth, CSRF and bytes; save()'),(390,700,980,'Write temporary JSON; rename'),(470,980,420,'Persist success; then clean unused uploads'),(550,420,140,'Redirect to CMS result')]:
 s+=f'<path d="M{a} {y} L{b} {y}" fill="none" stroke="#566677" marker-end="url(#a)"/><text x="{min(a,b)+10}" y="{y-12}" font-family="Arial" font-size="13" fill="#182b3d">{html.escape(label)}</text>'
write('analysis/yuyenpensuk/diagrams/content-sequence.svg',s+'</g></svg>')
write('analysis/yuyenpensuk/diagrams/content-sequence.mmd','''sequenceDiagram
 actor Admin
 participant Route as Express admin route
 participant DB as database.js
 participant Files as JSON and uploads
 Admin->>Route: Content, CSRF, optional files
 Route->>Route: Check session, CSRF and file bytes
 Route->>DB: save()
 DB->>Files: Write temporary JSON and rename
 Files-->>DB: Persisted or error
 DB-->>Route: Result
 alt Success
 Route->>Files: Clean unused uploads
 Route-->>Admin: Redirect
 else Failure
 Route-->>Admin: Error and rollback handling
 end
''')
old=(R/'analysis/yuyenpensuk/index.html').read_text();head=old.split('<body')[0]+'<body class="fx-subpage">';head=re.sub('<title>.*?</title>','<title>Yuyenpensuk Source-derived Specification | Panupong Intasan</title>',head)
body='''<header><b>Panupong Intasan · Source-derived specification</b><a href="index.html">Full analysis</a><a href="../../index.html">Portfolio</a></header><main><h1>Yuyenpensuk — Requirements & Design Review</h1><p class="meta">3 November 2026 · Source commit ffecf660f2fdd1a14de3561d817f2276a3c8fee4</p><p>This document was prepared from repository source and read-only browser observations. It is not a retrospective interview transcript, stakeholder approval or signed UAT result.</p><h2>Business requirements and scope</h2><p>Provide a public product/service catalogue and a CMS so authorized staff can maintain company content. The owner discussion and delivery history are supplied by the portfolio owner. No meeting minutes or signed requirements were available for independent verification.</p><p>Public browsing, content management and file uploads are in scope. Checkout, payment processing, inventory ledgers and installation scheduling are outside the implemented scope reviewed here.</p><h2>Software requirements and traceability</h2><div class="table-wrap"><table><tr><th>ID</th><th>Requirement / acceptance condition</th><th>Source</th><th>Verification</th></tr>'''
rows=[('FR01','Visitors can browse catalogue and product details without an admin session.','routes/site.js, views/site/','Read-only production pages observed'),('FR02','Content management requires an authenticated admin session.','middleware/auth.js, routes/admin.js','Source inspected; authenticated runtime NOT TESTED'),('FR03','Admin-account management requires the superadmin role.','middleware/auth.js, routes/admin.js','Source inspected; role enforcement runtime NOT TESTED'),('FR04','Multipart saves validate CSRF, allowed extension, size and file signatures.','routes/admin.js','Source inspected; uploads NOT TESTED'),('FR05','CMS content is persisted to JSON with temporary-file write and rename.','database.js','Source inspected; restart/persistence NOT TESTED'),('FR06','When enabled for an account, OTP is required before the session becomes authenticated.','routes/admin.js','Source inspected; 2FA NOT TESTED'),('FR07','Public and admin hosts route to separate Express apps with shared storage.','deploy-server.js','Source inspected; live source/deployed build equivalence NOT VERIFIED')]
for row in rows:body+='<tr>'+''.join('<td>'+html.escape(x)+'</td>' for x in row)+'</tr>'
body+='''</table></div><h2>Solution design</h2><p>Express renders EJS templates. deploy-server.js dispatches by hostname. database.js reads db.json from DATA_DIR, while UPLOAD_DIR stores files. Password verification uses bcrypt; account-enabled OTP uses otplib. These are code observations, not a security certification.</p><img src="diagrams/use-cases.svg" alt="Source-derived implemented use cases"><h2>Business workflow / activity overview</h2><img src="diagrams/workflow.svg" alt="Existing content-management workflow"><p>Normal flow: authenticate → select content → submit fields and files → validate → persist → display updated public content. Validation or storage failure must not be reported as a successful save.</p><h2>Sequence design</h2><img src="diagrams/content-sequence.svg" alt="Source-derived content-save sequence"><a href="diagrams/content-sequence.mmd">Mermaid source</a><h2>Data model</h2><img src="diagrams/data-model.svg" alt="Logical JSON data model"><p>This is a logical JSON model, not a relational SQL ERD. Company and content collections, admin records and file-path references are stored without SQL foreign-key constraints.</p><h2>User stories and acceptance criteria</h2><ul><li>As a visitor, I want to open a product by ID so I can inspect its details. Acceptance: existing ID returns its details; an unknown ID returns the implemented not-found response.</li><li>As an authorized editor, I want to update company content without editing EJS. Acceptance: a valid authenticated request with valid CSRF and permitted files persists the submitted fields; invalid requests must not report success.</li><li>As a superadmin, I want account management restricted by role. Acceptance: an authenticated non-superadmin receives HTTP 403 and no account mutation occurs.</li></ul><h2>API / endpoint catalogue</h2><p>These are HTML form routes and internal image endpoints, not a versioned public REST API contract.</p><div class="table-wrap"><table><tr><th>Method / path</th><th>Purpose</th><th>Access</th></tr>'''
for a,b,c in [('GET /products; /products/:id','Catalogue / detail','Public'),('GET /services; /projects','Service / project pages','Public'),('GET, POST /admin/login','Render login / verify password','Unauthenticated'),('GET, POST /admin/otp','Account-enabled OTP','Pending sign-in'),('GET /admin','Dashboard','Authenticated'),('GET, POST /admin/company','Company page / save','Authenticated + CSRF on write'),('POST /admin/products/save','Create / update product','Authenticated + multipart validation'),('POST /admin/products/delete/:id','Delete product','Authenticated + CSRF'),('GET /admin/api/product-gallery/:id','Image metadata','Authenticated'),('GET /admin/api/product-image/:id/:index','Image bytes','Authenticated'),('GET /admin/admins; POST /admin/admins/save','Account management','Superadmin')]:body+='<tr><td>'+a+'</td><td>'+b+'</td><td>'+c+'</td></tr>'
body+='''</table></div><h2>UAT test design — NOT EXECUTED</h2><p>Proposed cases: product search and unknown ID; editor denied admin-account management; invalid file signature rejected; invalid CSRF rejected; saved content visible after restart; OTP required when enabled; failed storage does not remove referenced images. These are acceptance scenarios, not passed results or user sign-off.</p><h2>Observed validation and limitations</h2><p>Six real browser captures are available: homepage, catalogue, product detail, services, projects and admin login. Two security-header unit tests passed in this review. No production data was changed. Dashboard, content-management screens, uploads, permission checks, OTP and restart persistence remain untested because no authenticated session was available.</p><p>Production catalogue/projects contain Test/test entries. Existing seeded stock content in source and claims inside a page capture do not establish customer delivery history, sales or installation statistics.</p><h2>Source references</h2><ul>'''
for p in ['database.js','routes/site.js','routes/admin.js','middleware/auth.js','deploy-server.js','docker-compose.yml','tests/security-headers.test.js']:body+=f'<li><a href="https://github.com/intasan/yuyenpensuk-website/blob/ffecf660f2fdd1a14de3561d817f2276a3c8fee4/{p}">{p}</a></li>'
write('analysis/yuyenpensuk/acceptance.html',head+body+'</ul></main></body></html>')
# Repair previously hidden evidence gallery scope and use current supplied fields consistently.
C=json.loads((R/'docs/case-study-content.json').read_text());D=json.loads((R/'projects.json').read_text())
for p in D:
 if p['id'] in ['gold-thai','flood']:
  gallery='<section id="evidence"><h2>Repository-recorded evidence</h2>'+''.join(f'<figure><img src="{im["src"]}" alt="{html.escape(im["caption"])}" style="width:100%;height:auto" loading="lazy"><figcaption>{html.escape(im["caption"])} · Historical capture; not rerun in this review.</figcaption></figure>' for im in p['images'])+'</section>'
  C[p['id']]=re.sub(r'<section id="evidence">.*?</section>','',C[p['id']],flags=re.S)+gallery
write('docs/case-study-content.json',json.dumps(C,ensure_ascii=False,indent=2))
