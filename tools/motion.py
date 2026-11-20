"""Motion-graphics engine for the أهلاً Hola videos (1080x1920, 30fps).

A video = list of scenes (see SCENE KINDS). The page is driven by render(t) so every frame is
a deterministic screenshot, streamed straight into ffmpeg together with the original voice track.

SCENE KINDS (all times in seconds on the audio timeline)
  title : {k,t0,t1,lines:[[text,'w'|'o'|'t'],..],sub}
  pair  : {k,t0,t1,r,eng,ar,es,pron,size,icon,hint,n,tot}      r = reveal time (absolute)
  sent  : {k,t0,t1,lang:'en'|'es',words:[..],w0,w1,tag,ar,ar_at,cta}   words spread over w0..w1 (absolute)
  end   : {k,t0,t1,lines:[..]}

Usage: HOLA_WORK=... python3 motion.py SPEC.json AUDIO OUT.mp4 [--stills t1,t2,..]
"""
import os, sys, json, subprocess, re
from playwright.sync_api import sync_playwright

S = os.environ.get("HOLA_WORK", "/tmp/hola-work")
FP = f"{S}/fontpkg/node_modules/@fontsource"
BASE = open(f"{S}/reel/base.css").read().replace("__FP__", FP)

CSS = """
html,body{width:1080px;height:1920px;overflow:hidden;background:#0c1730}
#bg{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 38%,#17305f 0%,#101d3b 55%,#0a1226 100%)}
#glyph{position:absolute;left:50%;top:50%;font-family:'Poppins',sans-serif;font-weight:800;font-size:1300px;color:#ffffff;opacity:.035;direction:ltr;white-space:nowrap;line-height:1}
.dot{position:absolute;border-radius:50%}
#wm{position:absolute;top:84px;left:0;right:0;text-align:center;font-size:58px;font-weight:800;z-index:20}
#wm .o{color:var(--or)}
#bar{position:absolute;left:0;bottom:0;height:14px;background:linear-gradient(90deg,#FFA51F,#ffd27a);z-index:20}
#bartrack{position:absolute;left:0;right:0;bottom:0;height:14px;background:#ffffff14;z-index:19}
.scene{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;padding:150px 50px 120px}
.lt{direction:ltr;unicode-bidi:isolate;font-family:'Poppins','CairoA',sans-serif}
.pill{background:var(--coral);color:#fff;font-weight:700;font-size:44px;padding:16px 46px;border-radius:60px;margin-bottom:34px}
.eng{font-family:'Poppins',sans-serif;direction:ltr;font-weight:600;font-size:74px;color:#cfd9ee;text-transform:uppercase;letter-spacing:6px;text-align:center}
.ar{font-weight:800;font-size:96px;line-height:1.3;margin-top:8px;text-align:center}
.icon{font-family:'Noto Color Emoji';font-size:210px;line-height:1.1;margin-bottom:6px}
.spw{position:relative;height:300px;display:flex;align-items:center;justify-content:center;margin-top:28px;direction:ltr}
.sp{font-family:'Poppins',sans-serif;font-weight:700;color:var(--or);white-space:nowrap;line-height:1.1;display:flex}
.sp span{display:inline-block;transform-origin:50% 70%}
.sp span.n{color:var(--teal)}
.q2{position:absolute;font-family:'Poppins',sans-serif;font-weight:800;font-size:230px;color:#3a4d7a}
.pr{color:var(--teal);font-weight:800;font-size:96px;margin-top:6px;min-height:120px;text-align:center;line-height:1.3}
.hint{background:#1a2a4c;border:3px solid var(--teal);color:#fff;font-weight:700;font-size:44px;padding:18px 46px;border-radius:70px;margin-top:34px;text-align:center;line-height:1.4;max-width:960px}
.hint b{color:var(--teal);font-family:'Poppins',sans-serif}
.dots{position:absolute;bottom:96px;left:0;right:0;display:flex;justify-content:center;gap:16px;direction:ltr}
.dots i{width:20px;height:20px;border-radius:50%;background:#2b3d66;transition:none}
.ttl{font-family:'Poppins','CairoA',sans-serif;font-weight:800;font-size:128px;line-height:1.18;text-align:center;direction:ltr;color:#fff}
.ttl .o{color:var(--or)} .ttl .t{color:var(--teal)}
.ttl div{overflow:visible}
.sub{color:#b8c6e4;font-size:56px;font-weight:700;margin-top:44px;text-align:center;line-height:1.5}
.sent{font-family:'Poppins',sans-serif;font-weight:700;font-size:80px;line-height:1.5;text-align:center;direction:ltr;max-width:960px}
.sent .w{display:inline-block;color:#46598a;transform-origin:50% 80%;margin:0 7px}
.sent .w .n{color:var(--teal)}
.sar{color:#cfd9ee;font-weight:800;font-size:54px;margin-top:50px;text-align:center;line-height:1.55;max-width:940px}
.cta{position:absolute;bottom:150px;left:0;right:0;text-align:center;font-size:52px;font-weight:800;color:#b8c6e4}
.cta b{color:var(--or)}
.ring{position:absolute;border-radius:50%;border:8px solid var(--or);left:50%;top:50%}
.spark{position:absolute;left:50%;top:50%;width:18px;height:18px;border-radius:50%}
"""

JS = r"""
const SPEC = __SPEC__;
const W=1080,H=1920,DUR=SPEC.dur;
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const P=(u,s,d)=>clamp((u-s)/d);
const E={out:x=>1-Math.pow(1-x,3),back:x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)},
  io:x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2,exp:x=>x>=1?1:1-Math.pow(2,-10*x)};
const $=(h)=>{const d=document.createElement('div');d.innerHTML=h.trim();return d.firstChild};
const stage=document.getElementById('stage');
const nz=s=>s.replace(/([ñÑ])/g,"<span class='n'>$1</span>");
// ---- background dots
const dots=[];for(let i=0;i<22;i++){const d=document.createElement('div');d.className='dot';const sz=8+((i*37)%22);
 d.style.width=d.style.height=sz+'px';d.style.background=i%3==0?'#2EC4B6':'#FFA51F';d.dataset.sz=sz;d.dataset.x=(i*191)%W;d.dataset.sp=20+((i*13)%34);d.dataset.ph=i*0.7;
 d.style.opacity=.10+((i*7)%10)/100;document.getElementById('bg').appendChild(d);dots.push(d)}
const glyph=document.getElementById('glyph');glyph.textContent=SPEC.glyph||'ñ';
// ---- scenes
const scenes=[];
function mk(sc){
 const root=document.createElement('div');root.className='scene';stage.appendChild(root);const o={sc,root,u:0};
 if(sc.k=='title'){
  const rows=sc.lines.map((l,i)=>`<div class='ttl' data-i='${i}'><span class='${l[1]=='o'?'o':(l[1]=='t'?'t':'')}'>${l[0]}</span></div>`).join('');
  root.innerHTML=rows+(sc.sub?`<div class='sub'>${sc.sub}</div>`:'')+`<div class='ul' style='width:380px;height:12px;border-radius:8px;background:linear-gradient(90deg,#FFA51F,#2EC4B6);margin-top:46px;transform-origin:left'></div>`;
  const rs=[...root.querySelectorAll('.ttl')],sub=root.querySelector('.sub'),ul=root.querySelector('.ul');
  o.upd=(u)=>{rs.forEach((r,i)=>{const p=E.out(P(u,0.05+i*0.14,0.45));r.style.opacity=p;r.style.transform=`translateY(${(1-p)*70}px) scale(${.92+.08*p})`});
   if(sub){const p=E.out(P(u,0.05+rs.length*0.14+0.1,0.4));sub.style.opacity=p;sub.style.transform=`translateY(${(1-p)*40}px)`}
   ul.style.transform=`scaleX(${E.out(P(u,0.4,0.7))})`;};
 } else if(sc.k=='pair'){
  const dots=sc.tot?`<div class='dots'>${Array.from({length:sc.tot},(_,i)=>`<i></i>`).join('')}</div>`:'';
  root.innerHTML=`<div class='icon'>${sc.icon||''}</div><div class='eng'>${sc.eng}</div><div class='ar'>${sc.ar}</div>
   <div class='spw'><div class='q2'>?</div><div class='sp lt' style='font-size:${sc.size}px'>${[...sc.es].map(c=>`<span class='${/[ñÑ]/.test(c)?'n':''}'>${c==' '?'&nbsp;':c}</span>`).join('')}</div></div>
   <div class='pr'>${sc.pron}</div>${sc.hint?`<div class='hint'>${sc.hint}</div>`:`<div class='hint' style='visibility:hidden'>.</div>`}${dots}`;
  const ic=root.querySelector('.icon'),eng=root.querySelector('.eng'),ar=root.querySelector('.ar'),q=root.querySelector('.q2'),
   letters=[...root.querySelectorAll('.sp span')],pr=root.querySelector('.pr'),hint=root.querySelector('.hint'),dd=[...root.querySelectorAll('.dots i')];
  const spw=root.querySelector('.spw');
  const ring=$("<div class='ring'></div>");spw.appendChild(ring);
  const sparks=Array.from({length:14},(_,i)=>{const s=$("<div class='spark'></div>");s.style.background=i%2?'#2EC4B6':'#FFA51F';spw.appendChild(s);return s});
  const rr=sc.r-sc.t0, fast=(sc.t1-sc.t0)<1.6, k=fast?0.6:1;
  o.upd=(u)=>{
   const pi=E.back(P(u,0,0.38*k));ic.style.opacity=clamp(pi*2);ic.style.transform=`translateY(${(1-pi)*-90+Math.sin(u*3.2)*8}px) scale(${.4+.6*pi}) rotate(${(1-pi)*-18}deg)`;
   const pe=E.out(P(u,0.06*k,0.3*k));eng.style.opacity=pe;eng.style.transform=`translateX(${(1-pe)*-120}px)`;eng.style.letterSpacing=(6+(1-pe)*18)+'px';
   const pa=E.back(P(u,0.2*k,0.35*k));ar.style.opacity=clamp(pa*1.5);ar.style.transform=`scale(${.5+.5*pa})`;
   const qv=u<rr?1:0, qp=clamp(1-P(u,rr-0.02,0.12));q.style.opacity=qp*(.55+.25*Math.sin(u*7));q.style.transform=`scale(${1+.08*Math.sin(u*7)})`;
   letters.forEach((l,i)=>{const pr0=P(u,rr+i*0.045*k,0.34*k),p=E.back(pr0);l.style.opacity=pr0>0?1:0;
     const bump=(l.classList.contains('n')&&u>rr+0.6)?(1+.1*Math.max(0,Math.sin((u-rr)*4))):1;
     l.style.transform=`translateY(${(1-p)*90}px) scale(${(.2+.8*p)*bump})`});
   const rp=P(u,rr,0.6*k);ring.style.opacity=rp>0&&rp<1?(1-rp)*.9:0;const rs=60+rp*520;ring.style.width=ring.style.height=rs+'px';ring.style.marginLeft=ring.style.marginTop=(-rs/2)+'px';
   sparks.forEach((s,i)=>{const a=i/14*Math.PI*2+.3,d=E.out(P(u,rr,0.55*k))*(240+(i%3)*70);const op=rp>0&&rp<1?1-rp:0;
     s.style.opacity=op;s.style.transform=`translate(${Math.cos(a)*d-9}px,${Math.sin(a)*d*0.7-9}px) scale(${1-rp*.6})`});
   const pp=E.out(P(u,rr+0.3*k,0.35*k));pr.style.opacity=pp;pr.style.transform=`translateY(${(1-pp)*50}px)`;
   const ph=E.back(P(u,rr+0.5*k,0.4*k));hint.style.opacity=clamp(ph*1.5);hint.style.transform=`scale(${.7+.3*ph})`;
   dd.forEach((d,i)=>{d.style.background=i<sc.n?'#FFA51F':'#2b3d66';d.style.transform=(i==sc.n-1)?`scale(${1+.5*Math.max(0,1-u*3)})`:'scale(1)'});
  };
 } else if(sc.k=='sent'){
  const words=sc.words.map(w=>`<span class='w'>${sc.lang=='es'?nz(w):w}</span>`).join(' ');
  root.innerHTML=`<div class='pill'>${sc.tag}</div><div class='sent'>${words}</div>${sc.ar?`<div class='sar'>${sc.ar}</div>`:''}${sc.cta?`<div class='cta'>تابع <b>أهلاً Hola</b> لكلمات جديدة كل يوم</div>`:''}`;
  const pill=root.querySelector('.pill'),ws=[...root.querySelectorAll('.w')],sar=root.querySelector('.sar'),cta=root.querySelector('.cta');
  const n=ws.length,tw=ws.map((_,i)=>(sc.times?sc.times[i]:(sc.w0+(sc.w1-sc.w0)*i/n))-sc.t0);
  const lit=sc.lang=='es'?'#FFA51F':'#ffffff';
  o.upd=(u)=>{
   const pp=E.back(P(u,0,0.35));pill.style.opacity=clamp(pp*1.5);pill.style.transform=`translateY(${(1-pp)*-60}px) scale(${.7+.3*pp})`;
   ws.forEach((w,i)=>{const d=u-tw[i];if(d<0){w.style.color='#46598a';w.style.transform='none';w.style.textShadow='none';return}
     const p=E.back(clamp(d/0.28));const act=d<0.38?1-d/0.38:0;
     w.style.color=d<0.5?'#ffffff':lit;w.style.transform=`translateY(${(1-p)*-26}px) scale(${1+.16*act})`;
     w.style.textShadow=act>0?`0 0 ${40*act}px rgba(255,165,31,${.85*act})`:'none'});
   if(sar){const p=E.out(P(u,(sc.ar_at!=null?sc.ar_at-sc.t0:0.6),0.5));sar.style.opacity=p;sar.style.transform=`translateY(${(1-p)*40}px)`}
   if(cta){const p=E.out(P(u,(sc.t1-sc.t0)-1.4,0.4));cta.style.opacity=p;cta.style.transform=`translateY(${(1-p)*30}px)`}
  };
 } else if(sc.k=='end'){
  root.innerHTML=`<div class='ttl' style='font-size:150px'><span class='o'>أهلاً</span> <span class='lt'>Hola</span></div><div class='sub' style='font-size:64px'>${sc.lines.join('<br>')}</div><div class='ul' style='width:420px;height:12px;border-radius:8px;background:linear-gradient(90deg,#FFA51F,#2EC4B6);margin-top:46px'></div>`;
  const t=root.querySelector('.ttl'),s=root.querySelector('.sub');
  o.upd=(u)=>{const p=E.back(P(u,0,0.5));t.style.opacity=clamp(p*1.5);t.style.transform=`scale(${.6+.4*p})`;const q=E.out(P(u,0.3,0.4));s.style.opacity=q;s.style.transform=`translateY(${(1-q)*40}px)`}
 }
 scenes.push(o);
}
SPEC.scenes.forEach(mk);
function render(t){
 // background
 dots.forEach((d,i)=>{const sp=+d.dataset.sp,ph=+d.dataset.ph;const y=((H+100)-((t*sp*3+i*97)%(H+200)));
   d.style.transform=`translate(${(+d.dataset.x)+Math.sin(t*.6+ph)*30}px,${y}px)`});
 glyph.style.transform=`translate(-50%,-50%) rotate(${Math.sin(t*.25)*6}deg) scale(${1+.04*Math.sin(t*.5)})`;
 document.getElementById('bar').style.width=(t/DUR*W)+'px';
 const EXIT=0.18;
 scenes.forEach(o=>{const sc=o.sc,u=t-sc.t0;
   if(t<sc.t0||t>=sc.t1+EXIT){o.root.style.display='none';return}
   o.root.style.display='flex';o.upd(u);
   const out=t>sc.t1?P(t,sc.t1,EXIT):0;
   o.root.style.opacity=1-out;o.root.style.transform=`translateY(${-60*E.out(out)}px) scale(${1-.04*out})`;
 });
}
render(0);
"""

HTML = """<html><head><meta charset='utf-8'><style>{base}{css}</style></head><body>
<div id='bg'></div><div id='glyph'></div><div id='wm'>أهلاً <span class='o lt'>Hola</span></div>
<div id='stage'></div><div id='bartrack'></div><div id='bar'></div>
<script>{js}</script></body></html>"""


def build_page(spec, path):
    html = HTML.format(base=BASE, css=CSS, js=JS.replace("__SPEC__", json.dumps(spec, ensure_ascii=False)))
    open(path, "w").write(html)


def main():
    spec_path, audio, out = sys.argv[1:4]
    stills = None
    if "--stills" in sys.argv:
        stills = [float(x) for x in sys.argv[sys.argv.index("--stills") + 1].split(",")]
    spec = json.load(open(spec_path))
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio]))
    spec["dur"] = dur
    page_path = os.path.abspath(out) + ".html"
    build_page(spec, page_path)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + page_path)
        pg.wait_for_timeout(600)
        if stills:
            for t in stills:
                pg.evaluate(f"render({t})")
                pg.screenshot(path=f"{os.path.abspath(out)}_t{t}.png")
            b.close()
            return
        fps = 30
        n = int(dur * fps)
        tmp = out + ".tmp.mp4"
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps), "-c:v", "mjpeg", "-i", "-",
                               "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "19", "-preset", "veryfast",
                               "-pix_fmt", "yuv420p", "-r", str(fps), "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", tmp],
                              stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f"render({i / fps})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
            if i % 150 == 0:
                print(f"frame {i}/{n}", flush=True)
        ff.stdin.close()
        ff.wait()
        b.close()
    os.rename(tmp, out)
    print("done", out, dur)


if __name__ == "__main__":
    main()
