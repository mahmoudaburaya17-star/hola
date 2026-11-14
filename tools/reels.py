import json, os, subprocess, sys, shutil
import numpy as np, soundfile as sf
from playwright.sync_api import sync_playwright
import os as _os
S = _os.environ.get("HOLA_WORK", "/tmp/hola-work")
FP = f"{S}/fontpkg/node_modules/@fontsource"
SR = 24000
FR = 30
def q(d): return round(d*FR)/FR

CSS = open(f"{S}/reel/base.css").read().replace("__FP__", FP)
LOGO = """<svg class="logo" viewBox="0 0 150 170"><path d="M20 160 V75 a55 55 0 0 1 110 0 V160" fill="none" stroke="#FFA51F" stroke-width="12" stroke-linecap="round"/><circle cx="68" cy="82" r="22" fill="#FFA51F"/><circle cx="92" cy="98" r="15" fill="#E8604C"/></svg>"""
BRAND = "<div class='brandname'>أهلاً <span class='o ltr'>Hola</span></div>"
def page(inner):
    wm = "" if 'class="logo"' in inner else "<div class='wm'>أهلاً <span class='o ltr'>Hola</span></div>"
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='glow'></div>{wm}<div class='col'>{inner}</div></body></html>"
def hide(c): return "" if c else " hide"

# ---------- sound effects (modelled on the reference video's pops / ticks / dings)
def env(n, decay): return np.exp(-np.arange(n)/SR*decay).astype(np.float32)
def tone(f, d, decay, amp=1.0):
    n=int(d*SR); t=np.arange(n)/SR; return (np.sin(2*np.pi*f*t)*env(n,decay)*amp).astype(np.float32)
def sfx_pop():
    a=np.zeros(int(.22*SR),dtype=np.float32); x=tone(650,.07,45,.55); y=tone(1000,.09,40,.55)
    a[:len(x)]+=x; i=int(.05*SR); a[i:i+len(y)]+=y; return a
def sfx_tick():
    rng=np.random.default_rng(3); n=int(.12*SR); a=np.zeros(n,dtype=np.float32)
    a[:int(.008*SR)]=rng.uniform(-1,1,int(.008*SR)).astype(np.float32)*.5
    t=tone(520,.1,38,.6); a[:len(t)]+=t; return a
def sfx_ding():
    a=tone(880,.5,9,.45)+tone(1320,.5,11,.35)
    return a.astype(np.float32)
def put(buf, clip, at):
    i=int(at*SR); 
    if i+len(clip)>len(buf): buf.resize(i+len(clip)+SR, refcheck=False)
    buf[i:i+len(clip)] += clip

# ---------- TTS
_k = None
def tts(text, voice, speed, path):
    global _k
    if _k is None:
        from kokoro_onnx import Kokoro
        _k = Kokoro(f"{S}/tts/kokoro.int8.onnx", f"{S}/tts/voices.bin")
    a, sr = _k.create(text, voice=voice, speed=speed, lang="es")
    sf.write(path, a, sr); return len(a)/sr

# ---------- render pipeline
def render(name, stages, audio_events, outdir):
    """stages: [(id, dur, html)], audio_events: [(kind, time, payload)]"""
    os.makedirs(f"{outdir}/png", exist_ok=True); os.makedirs(f"{outdir}/clips", exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox","--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width":1080,"height":1920})
        for sid, dur, html in stages:
            f=f"{outdir}/png/{sid}.html"; open(f,"w").write(html)
            pg.goto("file://"+f); pg.wait_for_timeout(350); pg.screenshot(path=f"{outdir}/png/{sid}.png")
        b.close()
    lst=[]
    for sid, dur, _ in stages:
        tmp=f"{outdir}/clips/{sid}.tmp.mp4"; fin=f"{outdir}/clips/{sid}.mp4"
        r=subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(FR),"-i",f"{outdir}/png/{sid}.png","-vf",f"format=yuv420p,loop=-1:1,trim=duration={dur}","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FR),tmp])
        assert r.returncode==0; os.rename(tmp,fin); lst.append(f"file '{fin}'")
    open(f"{outdir}/list.txt","w").write("\n".join(lst))
    total=sum(d for _,d,_ in stages)
    r=subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{outdir}/list.txt","-c","copy",f"{outdir}/v.tmp.mp4"]); assert r.returncode==0
    os.rename(f"{outdir}/v.tmp.mp4", f"{outdir}/v.mp4")
    buf=np.zeros(int((total+.3)*SR),dtype=np.float32)
    for kind,t,pay in audio_events:
        if kind=="pop": put(buf,sfx_pop(),t)
        elif kind=="tick": put(buf,sfx_tick(),t)
        elif kind=="ding": put(buf,sfx_ding(),t)
        elif kind=="voice":
            a,_=sf.read(pay,dtype="float32"); put(buf,a*0.95,t)
    buf=np.clip(buf[:int(total*SR)],-1,1); sf.write(f"{outdir}/audio.wav",buf,SR)
    out=f"{outdir}/{name}.mp4"; tmp=f"{outdir}/{name}.tmp.mp4"
    r=subprocess.run(["ffmpeg","-v","error","-y","-i",f"{outdir}/v.mp4","-i",f"{outdir}/audio.wav","-f","lavfi","-i",f"color=c=0xFFA51F:s=1080x10:r={FR}:d={total}",
      "-filter_complex",f"[0:v][2:v]overlay=x='-w+w*t/{total}':y=H-h:shortest=1,format=yuv420p[v]","-map","[v]","-map","1:a","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-t",str(total),tmp])
    assert r.returncode==0; os.rename(tmp,out); return out, total

# ---------- WORD (pronunciation) reel
def word_reel(cfg, outdir):
    outdir=os.path.abspath(outdir)
    os.makedirs(outdir,exist_ok=True)
    st=[]; ev=[]; t=0.0
    def add(sid,d,html): 
        nonlocal t; st.append((sid,d,html)); t+=d; return t-d
    def wstage(w,s):
        return page(f"""<div class='tag'>{w['tag']}</div><div class='es' style='font-size:{w['size']}px'>{w['es']}</div>
<div class='pron{hide(s>=2)}'>{w['pron']}</div><div class='mean{hide(s>=2)}'>{w['mean']}</div>
<div class='pill{hide(s>=3)}'>{w['pill']}</div><div class='note{hide(s>=3)}'>{w['note']}</div>""")
    t0=add("title",2.5,page(f"<div style='margin-top:230px'>{LOGO}</div>{BRAND}<div class='title1' style='margin-top:50px'>{cfg['title1']}<br><span class='o'>{cfg['title2']}</span></div>"))
    ev.append(("pop",t0+.1,None))
    for i,w in enumerate(cfg["words"],1):
        a=add(f"w{i}A",1.2,wstage(w,1)); add(f"w{i}B",1.0,wstage(w,2)); add(f"w{i}C",2.8,wstage(w,3))
        ev.append(("pop",a+.05,None))
        d1=tts(w["say"],"ef_dora",0.8,f"{outdir}/w{i}.wav"); d2=tts(w["example"],"ef_dora",0.9,f"{outdir}/e{i}.wav")
        ev.append(("voice",a+.45,f"{outdir}/w{i}.wav")); ev.append(("voice",a+2.6,f"{outdir}/e{i}.wav"))
    rows="".join(f"<div class='rowc'><div class='chip'>{a}</div><div class='arrow'>←</div><div class='chip es2'>{b}</div></div>" for a,b in cfg["recap"])
    a=add("summary",3.5,page(f"<div class='h2' style='margin-top:260px'>الخلاصة</div>{rows}")); ev.append(("pop",a+.05,None))
    def chal(count=None,rev=False):
        o1="opt ok" if rev else "opt"; o2="opt dim" if rev else "opt"
        cnt=f"<div class='count'>{count}</div>" if count else ""
        ans="<div class='small' style='color:#2EC4B6;font-size:56px;font-weight:700'>صح! ✓</div>" if rev else ""
        return page(f"""<div class='tag'>تحدّي</div><div class='q'>{cfg['q_ar']}</div>
<div style='display:flex;flex-direction:column;gap:36px'><div class='{o1}'>{cfg['q_right']}</div><div class='{o2}'>{cfg['q_wrong']}</div></div>{cnt}{ans}""")
    a=add("chalQ",1.2,chal()); ev.append(("pop",a+.05,None))
    for c in (3,2,1):
        a=add(f"chal{c}",1.0,chal(count=c)); ev.append(("tick",a+.02,None))
    a=add("chalR",2.2,chal(rev=True)); ev.append(("ding",a+.02,None))
    tts(cfg["q_right"],"ef_dora",0.85,f"{outdir}/q.wav"); ev.append(("voice",a+.5,f"{outdir}/q.wav"))
    a=add("outro",3.5,page(f"""<div style='margin-top:190px'>{LOGO}</div>
<div class='title1' style='font-size:76px;margin-top:70px'>{cfg['cta']}</div>
<svg width='90' height='90' viewBox='0 0 90 90' style='margin-top:40px'><path d='M45 10 V70 M20 46 L45 72 L70 46' fill='none' stroke='#FFA51F' stroke-width='10' stroke-linecap='round' stroke-linejoin='round'/></svg>
<div class='title1' style='font-size:110px;margin-top:60px'><span class='o'>Hola</span> أهلاً</div><div class='small'>إسباني بالعربي.. صح من أول كلمة</div>"""))
    ev.append(("ding",a+.05,None))
    return render(cfg["file"],st,ev,outdir)

# ---------- DIALOGUE reel
def dialog_reel(cfg, outdir):
    outdir=os.path.abspath(outdir)
    os.makedirs(outdir,exist_ok=True)
    lines=cfg["lines"]; st=[]; ev=[]; t=0.0
    def add(sid,d,html):
        nonlocal t; st.append((sid,d,html)); t+=d; return t-d
    durs=[]
    for i,l in enumerate(lines):
        durs.append(tts(l["es"],l["voice"],0.9,f"{outdir}/L{i}.wav"))
    def bubble(i,l,state):  # state: 'active','shown','dim'
        side="r" if l["side"]=="r" else "l"
        trans_vis = "" if state in ("shown","dim") else " hide"
        cls="b "+side+(" dim" if state=="dim" else "")
        return f"""<div class='{cls}'><div class='spk {side}c'>{l['name']}</div>
<div class='bes'>{l['es']}</div><div class='bar{trans_vis}'>{l['ar']}</div></div>"""
    def lstage(i, translated):
        lo=max(0,i-1); parts=[]
        for j in range(lo,i+1):
            if j<i: state="dim"
            else: state="shown" if translated else "active"
            parts.append(bubble(j,lines[j],state))
        return page(f"<div class='tag' style='margin-bottom:50px'>{cfg['tag']}</div><div class='chat'>{''.join(parts)}</div>")
    a=add("title",2.5,page(f"<div style='margin-top:230px'>{LOGO}</div>{BRAND}<div class='title1' style='margin-top:50px'>{cfg['title1']}<br><span class='o'>{cfg['title2']}</span></div>"))
    ev.append(("pop",a+.1,None))
    for i,l in enumerate(lines):
        dA=q(.4+durs[i]+.35); a=add(f"l{i}A",dA,lstage(i,False)); add(f"l{i}B",1.3,lstage(i,True))
        ev.append(("pop",a+.02,None)); ev.append(("voice",a+.4,f"{outdir}/L{i}.wav"))
    a=add("outro",3.5,page(f"""<div style='margin-top:190px'>{LOGO}</div>
<div class='title1' style='font-size:76px;margin-top:70px'>{cfg['cta']}</div>
<svg width='90' height='90' viewBox='0 0 90 90' style='margin-top:40px'><path d='M45 10 V70 M20 46 L45 72 L70 46' fill='none' stroke='#FFA51F' stroke-width='10' stroke-linecap='round' stroke-linejoin='round'/></svg>
<div class='title1' style='font-size:110px;margin-top:60px'><span class='o'>Hola</span> أهلاً</div><div class='small'>إسباني بالعربي.. صح من أول كلمة</div>"""))
    ev.append(("ding",a+.05,None))
    return render(cfg["file"],st,ev,outdir)
