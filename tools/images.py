import os
from playwright.sync_api import sync_playwright
import os as _os
S = _os.environ.get("HOLA_WORK", "/tmp/hola-work")
CSS=open(f"{S}/reel/base.css").read().replace("__FP__",f"{S}/fontpkg/node_modules/@fontsource")
CSS+="""
html,body{height:1080px!important}
.col{padding-top:190px!important}
.wm{top:56px!important;font-size:46px!important}
.es{white-space:normal}
.big{font-family:'Poppins',sans-serif;font-weight:700;color:var(--or);direction:ltr;text-align:center;line-height:1.15}
.pair{display:flex;align-items:center;gap:30px;margin-top:34px}
.sq-title{font-size:92px;font-weight:800;text-align:center;line-height:1.35}
.sq-title .o{color:var(--or)}
.lst{display:flex;flex-direction:column;gap:14px;margin-top:0}
.num{color:var(--teal);font-weight:800;font-size:44px}
"""
def pg(inner): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='glow' style='bottom:-560px'></div><div class='wm'>أهلاً <span class='o ltr'>Hola</span></div><div class='col'>{inner}</div></body></html>"
def slide(tag, es, size, pron, mean, extra=""):
    return pg(f"<div class='tag' style='margin-bottom:40px'>{tag}</div><div class='big' style='font-size:{size}px'>{es}</div><div class='pron' style='font-size:84px;margin-top:40px'>{pron}</div><div class='mean' style='font-size:96px;margin-top:20px'>{mean}</div>{extra}")
slides={
 "carousel_1": pg("<div class='sq-title' style='margin-top:120px'>5 تحيات<br><span class='o'>لازم تعرفها</span><br>بالإسباني 🇪🇸</div><div class='small' style='margin-top:50px'>اسحب ← </div>".replace("🇪🇸","")),
 "carousel_2": slide("1","Hola",190,"أُولا","مرحبًا","<div class='pill' style='margin-top:40px'>حرف H صامت — مبيتنطقش</div>"),
 "carousel_3": slide("2","Buenos días",120,"بُويْنُس دِيَاس","صباح الخير","<div class='pill' style='margin-top:40px'>بنقولها لحد الظهر</div>"),
 "carousel_4": pg("<div class='tag' style='margin-bottom:40px'>3</div><div class='big' style='font-size:100px'>Buenas tardes</div><div class='mean' style='font-size:76px;margin-top:6px'>مساء الخير (بعد الظهر)</div><div class='big' style='font-size:100px;margin-top:70px'>Buenas noches</div><div class='mean' style='font-size:76px;margin-top:6px'>مساء الخير (بالليل)</div>"),
 "carousel_5": slide("4","¿Cómo estás?",104,"كُومو إِسْتَاس","إزيك؟","<div class='pill' style='margin-top:36px'>الرد: <span class='ltr'>Bien, gracias</span></div>"),
 "carousel_6": pg("<div class='sq-title' style='margin-top:110px'>احفظ البوست<br><span class='o'>وشاركه</span><br>مع صاحبك ✅</div>".replace("✅","")+"<div class='small' style='margin-top:40px'>إسباني بالعربي.. صح من أول كلمة</div>"),
}
rows=[("Hola","مرحبًا"),("Gracias","شكرًا"),("Por favor","لو سمحت"),("De nada","عفوًا"),("Adiós","مع السلامة")]
lst="".join(f"<div class='rowc' style='margin-top:0'><div class='chip' style='width:360px;font-size:46px;padding:12px 30px'>{b}</div><div class='arrow' style='font-size:56px'>←</div><div class='chip es2' style='width:420px;font-size:44px;padding:12px 30px'>{a}</div></div>" for a,b in rows)
slides["words"]=pg(f"<div class='tag' style='margin-bottom:34px'>كلمات اليوم</div><div class='lst'>{lst}</div>")
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox","--allow-file-access-from-files"])
    page=b.new_page(viewport={"width":1080,"height":1080})
    for n,h in slides.items():
        f=f"{S}/reel/imgs/{n}.html"; open(f,"w").write(h)
        page.goto("file://"+f); page.wait_for_timeout(400); page.screenshot(path=f"{S}/reel/imgs/{n}.png")
    b.close()
from PIL import Image
names=list(slides)
sh=Image.new("RGB",(360*4,360*2))
for i,n in enumerate(names): sh.paste(Image.open(f"{S}/reel/imgs/{n}.png").resize((360,360)),((i%4)*360,(i//4)*360))
sh.save(f"{S}/reel/imgs_sheet.png"); print(names)
