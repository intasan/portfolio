from pathlib import Path
import json,concurrent.futures,urllib.request,time
R=Path(__file__).resolve().parent.parent
urls=json.loads((R/'docs/internal/static-qa.json').read_text())['external_urls']
def check(url):
 try:
  t=time.monotonic();r=urllib.request.urlopen(url,timeout=18);row={'url':url,'status':r.status,'seconds':round(time.monotonic()-t,2),'final_url':r.geturl()};r.close();return row
 except Exception as e:return {'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool: rows=list(pool.map(check,urls))
(R/'docs/internal/external-link-qa.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print(json.dumps({'checked':len(rows),'issues':[r for r in rows if r.get('status',999)>=400]},indent=2))
