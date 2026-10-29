/* Scroll Film: local original WebP sequences, lo -> hi, native scroll (no double easing).
   Fixed-orientation asset set for the lifetime of the page; CSS handles rotations without a reload.
   48 decoded hi frames: ~169 MB landscape / ~96 MB portrait, plus low tier and canvas.
*/
(() => {
'use strict';
const canvas=document.querySelector('[data-film-canvas]');if(!canvas)return;
const ctx=canvas.getContext('2d',{alpha:false});if(!ctx)return;
const orientation=matchMedia('(max-width:760px)').matches?'portrait':'landscape';
const count=Number(canvas.dataset.frames),step=Number(canvas.dataset.loStep),root=canvas.dataset.root;
const poster=document.querySelector('.film-poster');
const stats={exact:0,near:0,lo:0,poster:0,none:0};let enabled=!matchMedia('(prefers-reduced-motion:reduce)').matches;
const pad=i=>String(i+1).padStart(4,'0');let scenes=[],shown='',scheduled=false,ready=false,lastFrame=0;
function sequence(n,url){const imgs=new Array(n),ready=new Uint8Array(n),pending=new Array(n);return {imgs,ready,count:n,load(i){if(i<0||i>=n)return Promise.resolve();if(pending[i])return pending[i];const im=new Image();im.decoding='async';im.src=url(i);imgs[i]=im;pending[i]=im.decode().then(()=>{ready[i]=1;schedule()},()=>{});return pending[i]},nearest(i){for(let d=0;d<n;d++){if(i-d>=0&&ready[i-d])return i-d;if(i+d<n&&ready[i+d])return i+d}return -1}}}
const hi=sequence(count,i=>`${root}/${orientation}/f_${pad(i)}.webp`),lo=sequence(Math.ceil(count/step),i=>`${root}/${orientation}-lo/f_${pad(i)}.webp`);
function measure(){scenes=[...document.querySelectorAll('[data-film]')].map(el=>{const [p0,p1]=el.dataset.film.split('-').map(Number);const start=el.getBoundingClientRect().top+scrollY;return {start,end:start+el.offsetHeight,f0:p0*(count-1),f1:p1*(count-1)}})}
function frameAt(y){let f=0;for(const s of scenes){if(y>=s.end){f=s.f1;continue}if(y>=s.start)f=s.f0+(s.f1-s.f0)*(y-s.start)/(s.end-s.start||1);break}return Math.max(0,Math.min(count-1,Math.round(f)))}
function pick(want){if(hi.ready[want])return {im:hi.imgs[want],key:'h'+want,kind:'exact'};let h=hi.nearest(want);if(h>=0&&Math.abs(h-want)<step)return {im:hi.imgs[h],key:'h'+h,kind:'near'};let j=lo.nearest(Math.round(want/step));if(j>=0)return {im:lo.imgs[j],key:'l'+j,kind:'lo'};if(h>=0)return {im:hi.imgs[h],key:'h'+h,kind:'near'};return null}
function draw(p){const w=canvas.width,h=canvas.height,s=Math.min(w/p.im.naturalWidth,h/p.im.naturalHeight);ctx.fillStyle='#0a0b0b';ctx.fillRect(0,0,w,h);ctx.imageSmoothingQuality='high';ctx.drawImage(p.im,(w-p.im.naturalWidth*s)/2,(h-p.im.naturalHeight*s)/2,p.im.naturalWidth*s,p.im.naturalHeight*s);shown=p.key;canvas.classList.add('ready');stats[p.kind]++;canvas.dataset.rendered=p.key;}
function tick(){scheduled=false;if(document.hidden)return;const want=enabled?frameAt(scrollY+innerHeight*.15):0;canvas.dataset.frame=String(want);if(enabled){const dir=want>=lastFrame?1:-1;hi.load(want);for(let k=1;k<=6;k++)hi.load(want+dir*k)}lastFrame=want;const p=pick(want);if(!p){if(poster?.complete&&poster.naturalWidth)stats.poster++;else stats.none++;return}if(p.key!==shown)draw(p)}
function schedule(){if(!scheduled&&!document.hidden){scheduled=true;requestAnimationFrame(tick)}}
function resize(){const dpr=Math.min(devicePixelRatio||1,1.75);canvas.width=Math.round(canvas.clientWidth*dpr);canvas.height=Math.round(canvas.clientHeight*dpr);shown='';measure();schedule()}
async function preload(seq,order,parallel=4){let k=0;await Promise.all(Array.from({length:parallel},async()=>{while(k<order.length)await seq.load(order[k++])}))}
function coarse(n){const a=[0,n-1],seen=new Set(a);for(let s=16;s>=1;s>>=1)for(let i=0;i<n;i+=s)if(!seen.has(i)){seen.add(i);a.push(i)}return a}
let loadingFull=false;async function fullLoad(){if(loadingFull)return;loadingFull=true;await preload(lo,coarse(lo.count),4);await preload(hi,coarse(count),4)}
function setMotion(v){enabled=Boolean(v);canvas.dataset.motion=enabled?'on':'off';if(enabled)fullLoad();shown='';schedule()}
new ResizeObserver(resize).observe(canvas);new ResizeObserver(()=>{measure();schedule()}).observe(document.querySelector('main'));
addEventListener('scroll',schedule,{passive:true});addEventListener('resize',resize,{passive:true});document.addEventListener('visibilitychange',()=>{scheduled=false;if(!document.hidden){shown='';schedule()}});canvas.addEventListener('contextlost',()=>{canvas.classList.remove('ready');shown=''});canvas.addEventListener('contextrestored',()=>{shown='';resize()});document.addEventListener('portfolio:motion',e=>setMotion(e.detail));
(async()=>{await Promise.all([lo.load(0),hi.load(0)]);ready=true;resize();if(enabled)fullLoad()})();
window.__film={stats,frameAt,set:orientation,frames:count,setMotion,get ready(){return ready}};
})();
