"""Generate accessible standalone project pages and the browser data file.
Run: python3 tools/build_project_pages.py
Source of truth: projects.json. No build-time dependencies.
"""
from pathlib import Path
import json,html,re
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'projects.json').read_text());out=ROOT/'case-studies';out.mkdir(exist_ok=True)
def e(s):return html.escape(str(s),quote=True)
names={'ba':'Business Analyst','sa':'System Analyst','da':'Data Analyst','app':'Application','ux':'Interactive / UX'}
for p in data:
 title=e(p['title']);head=f'''<!doctype html><html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Panupong Intasan</title><meta name="description" content="{e(p['desc'])}"><link rel="canonical" href="https://intasan.github.io/portfolio/case-studies/{p['id']}.html"><link rel="icon" href="../favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;1,400&family=IBM+Plex+Sans+Thai:wght@400;500&family=Noto+Serif+Thai:wght@400&display=swap" rel="stylesheet"><link rel="stylesheet" href="../engine/base.css"><link rel="stylesheet" href="../brand.css"></head><body><a class="skip" href="#case-content">ข้ามไปเนื้อหา</a><header class="nav"><div class="w nav-row"><a class="identity" href="../index.html"><span class="monogram">P.I</span><small>PANUPONG<br>INTASAN</small></a><a class="link" href="../index.html#all-work">กลับไปผลงาน ↗</a></div></header><main id="case-content" class="w" style="padding-top:50px;padding-bottom:65px"><article class="detail"><div class="eyebrow">{e(p['kind'])}</div><h1 style="font-size:clamp(2.5rem,6vw,5rem);line-height:1.15;margin:20px 0">{title}</h1><div class="tags">'''+''.join(f'<span class="tag">{e(names[x])}</span>' for x in p['cats'])+f'''</div><p>{e(p['desc'])}</p><div class="detailgrid"><div><h2 class="label">บทบาท / สิ่งที่ทำ</h2><p>{e(p['role'])}</p><h2 class="label">ขอบเขตที่นำเสนอ</h2><ul>'''+''.join(f'<li>{e(x)}</li>' for x in p['features'])+'''</ul><h2 class="label">เครื่องมือและวิธีการ</h2><div class="tags">'''+''.join(f'<span class="tag">{e(x)}</span>' for x in p['tech'])+f'''</div><h2 class="label">ผลลัพธ์ / สิ่งที่ส่งมอบ</h2><p>{e(p['result'])}</p><h2 class="label">ขอบเขตและสถานะ</h2><p class="note">{e(p['limit'])}</p><div class="actions">'''
 if p.get('repo'):head+=f'<a class="btn primary" href="https://github.com/intasan/{p["repo"]}" target="_blank" rel="noopener noreferrer">โค้ด / เอกสารโครงการ ↗</a>'
 if p.get('repo') and p['repo']!='02739452-26-6621655321':head+=f'<a class="btn" href="https://github.com/intasan/{p["repo"]}/blob/main/docs/VERIFIED_SCOPE.md">ผลตรวจและข้อจำกัดจริง ↗</a>'
 if p.get('analysis'):head+=f'<a class="btn" href="../{e(p["analysis"]["href"])}">อ่านเอกสารวิเคราะห์ระบบ ↗</a>'
 if p['id']=='ppe':head+='<a class="btn primary" href="../ppe-case-study.html">อ่านตัวอย่างเอกสาร BA ↗</a>'
 head+='</div></div><div>'
 if p['images']:
  head+='<h2 class="label">ภาพจากโครงการ</h2>'
  for im in p['images']:head+=f'<figure style="margin:0 0 25px"><a href="{e(im["src"])}" target="_blank" rel="noopener noreferrer"><img src="{e(im["src"])}" alt="{e(im["caption"])}" loading="lazy" style="width:100%;border:1px solid var(--line)"></a><figcaption class="caption">{e(im["caption"])}</figcaption></figure>'
 if p.get('analysis'):head+=f'<h2 class="label">Data Flow และเอกสารวิเคราะห์</h2><a href="../{e(p["analysis"]["href"])}"><img src="../{e(p["analysis"]["diagram"])}" alt="Data Flow Diagram {title}" loading="lazy" style="width:100%;border:1px solid var(--line)"></a><p class="caption">เอกสารใหม่จาก source baseline พร้อม Requirement, Workflow, Data Model และ UAT ที่ระบุสถานะตามจริง</p>'
 head+='<h2 class="label">กระบวนการของโครงการ</h2><ol class="flow">'+''.join(f'<li>{e(x)}</li>' for x in p['flow'])+'</ol></div></div></article></main><footer class="footer"><div class="w"><span>© 2026 PANUPONG INTASAN</span><a href="../index.html#contact">ติดต่อ / ร่วมงาน ↗</a></div></footer></body></html>'
 (out/(p['id']+'.html')).write_text(head)
(ROOT/'projects.js').write_text('/* Generated from projects.json by tools/build_project_pages.py. */\nwindow.PORTFOLIO_PROJECTS='+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
s=(ROOT/'index.html').read_text()
# Preserve native links to real case-study pages; JS progressively enhances them into dialogs.
for p in data:
 s=s.replace(f'href="#project={p["id"]}"',f'href="case-studies/{p["id"]}.html" data-project="{p["id"]}"')
 s=s.replace(f'data-project="{p["id"]}" data-project="{p["id"]}"',f'data-project="{p["id"]}"')
(ROOT/'index.html').write_text(s)
urls=['https://intasan.github.io/portfolio/analysis/']+['https://intasan.github.io/portfolio/'+x['analysis']['href'] for x in data if x.get('analysis')]+['https://intasan.github.io/portfolio/','https://intasan.github.io/portfolio/ppe-case-study.html']+['https://intasan.github.io/portfolio/case-studies/'+x['id']+'.html' for x in data]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+x+'</loc><lastmod>2026-10-30</lastmod></url>' for x in urls)+'</urlset>')
print('Built',len(data),'standalone case studies')
