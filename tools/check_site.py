from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
R=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.errors=[];self.h1=0;self.title=False;self.description=False
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and d.get('name')=='description':self.description=True
  if tag=='img' and d.get('src') and not d.get('alt'):self.errors.append('image missing alt')
  for k in ['href','src']:
   if k in d:self.refs.append(d[k])
files=[f for f in R.rglob('*.html') if not any(p in f.parts for p in ['dist','.git','docs','tools'])]
parsed={}
for f in files:
 p=Page();p.feed(f.read_text());parsed[f]=p
issues=[];external=set();count=0
for f,p in parsed.items():
 for err in p.errors:issues.append([str(f.relative_to(R)),err])
 if len(p.ids)!=len(set(p.ids)):issues.append([str(f.relative_to(R)),'duplicate id'])
 if not p.title:issues.append([str(f.relative_to(R)),'missing title'])
 if not p.description:issues.append([str(f.relative_to(R)),'missing description'])
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:
   if u.scheme in ['http','https']:external.add(ref)
   continue
  target=(f.parent/u.path).resolve() if u.path else f
  if target.is_dir():target=target/'index.html'
  # Certificate filename contains literal percent escapes.
  if not target.exists():target=(f.parent/unquote(u.path)).resolve()
  count+=1
  if not target.exists():issues.append([str(f.relative_to(R)),f'missing {ref}'])
  elif u.fragment and target in parsed and unquote(u.fragment) not in parsed[target].ids:issues.append([str(f.relative_to(R)),f'missing fragment {ref}'])
home=(R/'index.html').read_text()
for word in ['REPOSITORY_AUDIT','VERIFIED_SCOPE','18 Repository','Flutter SDK','WebGL','PostGIS','projects.json']:
 if word in home:issues.append(['index.html',f'audit/runtime leak {word}'])
result={'html_pages':len(files),'local_references_checked':count,'issues':issues,'external_urls':sorted(external),'scope':'Static HTML links, fragments, alt text, duplicate IDs, metadata and homepage audit exclusion. No external HTTP or browser assertions in this check.'}
(R/'docs/internal/static-qa.json').write_text(json.dumps(result,indent=2,ensure_ascii=False));print(json.dumps({k:v for k,v in result.items() if k!='external_urls'},indent=2,ensure_ascii=False))
raise SystemExit(bool(issues))
