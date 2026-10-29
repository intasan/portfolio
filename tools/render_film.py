"""Original procedural 3D artwork. No third-party model or stock footage.
Render torus meshes with depth-sorted faces, metallic shading and an orbiting camera.
Generate independent landscape/portrait compositions plus tiered WebP frames.
"""
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFilter
import math,json
ROOT=Path(__file__).resolve().parents[1]/'assets'/'film-v1';N=48;STEP=3

def rx(a):return np.array([[1,0,0],[0,np.cos(a),-np.sin(a)],[0,np.sin(a),np.cos(a)]])
def ry(a):return np.array([[np.cos(a),0,np.sin(a)],[0,1,0],[-np.sin(a),0,np.cos(a)]])
def rz(a):return np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])

def ring(R,r,mat):
 u=np.linspace(0,2*np.pi,161);v=np.linspace(0,2*np.pi,49);u,v=np.meshgrid(u,v,indexing='ij')
 xyz=np.stack([(R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v)],axis=-1)
 xyz=xyz@mat.T
 faces=np.stack([xyz[:-1,:-1],xyz[1:,:-1],xyz[1:,1:],xyz[:-1,1:]],axis=2).reshape(-1,4,3)
 return faces
base=np.concatenate([ring(1.55,.14,rx(.18)),ring(1.32,.13,rx(1.15)@ry(.40)),ring(1.08,.12,ry(1.28)@rz(.4))])
colors=np.concatenate([np.tile([194,157,91],(160*48,1)),np.tile([191,192,183],(160*48,1)),np.tile([110,132,120],(160*48,1))])
light=np.array([-.4,.75,1.]);light/=np.linalg.norm(light);view=np.array([0,0,1.])
for name,w,h,scale in [('landscape',1100,800,208),('portrait',640,780,150)]:
 (ROOT/name).mkdir(parents=True,exist_ok=True);(ROOT/(name+'-lo')).mkdir(exist_ok=True)
 yy,xx=np.mgrid[:h,:w];glow=np.exp(-(((xx-w*.52)/(w*.38))**2+((yy-h*.5)/(h*.4))**2)*2)
 bg=np.empty((h,w,3),dtype=np.uint8)
 for c,b in enumerate([10,11,11]):bg[:,:,c]=np.clip(b+glow*[15,16,13][c],0,255)
 background=Image.fromarray(bg)
 for i in range(N):
  t=i/(N-1);mat=rx(.4+.15*np.sin(t*np.pi))@ry(-.7+t*2.05)@rz(-.25+t*.4)
  faces=base@mat.T;cent=faces.mean(axis=1);norm=np.cross(faces[:,1]-faces[:,0],faces[:,2]-faces[:,0]);norm/=np.linalg.norm(norm,axis=1)[:,None]
  diff=np.clip(norm@light,0,1);reflect=2*(norm@light)[:,None]*norm-light;spec=np.clip(reflect@view,0,1)**32
  shade=.20+.66*diff;rgb=np.clip(colors*shade[:,None]+spec[:,None]*160,0,255).astype(int)
  im=background.copy();shadow=Image.new('RGBA',(w,h));sd=ImageDraw.Draw(shadow);sd.ellipse((w*.24,h*.78,w*.78,h*.86),fill=(0,0,0,160));shadow=shadow.filter(ImageFilter.GaussianBlur(28));im=Image.alpha_composite(im.convert('RGBA'),shadow).convert('RGB');d=ImageDraw.Draw(im)
  # small central sphere with a metallic gradient
  z=faces[:,:,2];fac=5.8/(5.8-z);pts=faces[:,:,:2]*fac[:,:,None]*scale;pts[:,:,0]+=w*.5;pts[:,:,1]=h*.48-pts[:,:,1]
  # far to near surface order, including backfaces for complete solid geometry
  for k in np.argsort(cent[:,2]):d.polygon([tuple(q) for q in pts[k]],fill=tuple(rgb[k]))
  im.save(ROOT/name/f'f_{i+1:04}.webp','WEBP',quality=83,method=4)
  if i%STEP==0:im.resize((330,240) if name=='landscape' else (240,292),Image.Resampling.LANCZOS).save(ROOT/(name+'-lo')/f'f_{i//STEP+1:04}.webp','WEBP',quality=52,method=4)
  if i==0:im.save(ROOT/(name+'-poster.webp'),'WEBP',quality=88)
 print(name,'done',flush=True)
(ROOT/'manifest.json').write_text(json.dumps({'frames':N,'step':STEP,'authorship':'Original procedural 3D artwork','sets':{'landscape':[1100,800],'portrait':[640,780]}},indent=2))
print('Total bytes',sum(x.stat().st_size for x in ROOT.rglob('*') if x.is_file()))
