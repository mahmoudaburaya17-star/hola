"""Image builders for text posts (1080x1080). Same look as the reels.

Needs the same setup as reels.py (see README): $HOLA_WORK/reel/base.css, $HOLA_WORK/fontpkg, Chrome.
"""
import os
from playwright.sync_api import sync_playwright

S = os.environ.get("HOLA_WORK", "/tmp/hola-work")
FP = f"{S}/fontpkg/node_modules/@fontsource"

EXTRA = """
html,body{height:1080px!important}
.col{padding-top:150px!important;padding-bottom:50px;justify-content:center}
.wm{top:54px!important;font-size:46px!important}
.glow{bottom:-560px!important}
.sq-title{font-size:88px;font-weight:800;text-align:center;line-height:1.4}
.sq-title .o{color:var(--or)}
.big{font-family:'Poppins',sans-serif;font-weight:700;color:var(--or);direction:ltr;text-align:center;line-height:1.15;white-space:nowrap}
.es2l{font-family:'Poppins',sans-serif;font-weight:600;color:#fff;direction:ltr;text-align:center;line-height:1.2;white-space:nowrap}
.lst{display:flex;flex-direction:column;gap:var(--g,14px)}
.lst .chip{font-size:var(--f,60px);padding:var(--p,26px) 30px;width:360px;min-width:0}
.lst .chip.es2{font-size:calc(var(--f,60px) - 8px);width:450px}
.lst .arrow{font-size:calc(var(--f,60px) - 8px)}
.card{background:var(--card);border:2px solid #2b3d66;border-radius:34px;padding:22px 40px;width:940px;text-align:center}
.card .e{font-family:'Poppins',sans-serif;font-weight:700;color:var(--or);direction:ltr;font-size:50px;line-height:1.25}
.card .a{font-weight:700;color:#fff;font-size:42px;margin-top:6px;line-height:1.35}
.card.good{border-color:var(--teal)}
.card.bad{border-color:var(--coral);opacity:.9}
.card .badge{font-weight:800;font-size:36px;margin-top:6px}
.card.good .badge{color:var(--teal)}
.card.bad .badge{color:var(--coral)}
.notebar{color:#9fb0cf;font-size:40px;margin-top:30px;font-weight:500;text-align:center;line-height:1.5;max-width:940px}
.qo{display:flex;align-items:center;gap:28px;background:var(--card);border:3px solid #2b3d66;border-radius:36px;padding:14px 38px;width:860px;direction:ltr}
.ql{background:var(--teal);color:#0b1630;width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Poppins',sans-serif;font-weight:800;font-size:38px;flex:none}
.qo.rtl{direction:rtl}
.qt{flex:1;text-align:start;font-family:'Poppins','CairoA',sans-serif;font-weight:700;font-size:50px;color:var(--or)}
.qq{font-size:60px;font-weight:800;text-align:center;line-height:1.35;margin-bottom:26px;max-width:960px}
.qq .ltr{color:var(--or)}
"""
CSS = open(f"{S}/reel/base.css").read().replace("__FP__", FP) + EXTRA


def page(inner):
    wm = "<div class='wm'>أهلاً <span class='o ltr'>Hola</span></div>"
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
            f"<div class='glow'></div>{wm}<div class='col'>{inner}</div></body></html>")


def _size(txt, table):
    n = len(txt)
    for limit, px in table:
        if n <= limit:
            return px
    return table[-1][1]


def cover(l1, l2="", l3="", sub=""):
    t = f"{l1}<br><span class='o'>{l2}</span>" + (f"<br>{l3}" if l3 else "")
    if sub and (sub[0].isascii() or sub[0] == "¿"):
        sub = f"<span class='ltr'>{sub}</span>"
    s = f"<div class='small' style='margin-top:44px'>{sub}</div>" if sub else ""
    return page(f"<div class='sq-title'>{t}</div>{s}")


def rows(tag, pairs, note=""):
    """pairs: [(arabic, spanish)] as chips (short words)."""
    n = len(pairs)
    f, p, g = {1: (60, 26, 14), 2: (60, 26, 14), 3: (60, 26, 14), 4: (54, 18, 12), 5: (48, 12, 10), 6: (40, 9, 9)}.get(n, (35, 6, 7))
    r = "".join(
        f"<div class='rowc' style='margin-top:0'><div class='chip'>{a}</div><div class='arrow'>←</div>"
        f"<div class='chip es2'>{b}</div></div>" for a, b in pairs)
    nb = f"<div class='notebar' style='margin-top:20px;font-size:36px'>{note}</div>" if note else ""
    return page(f"<div class='tag' style='margin-bottom:30px'>{tag}</div>"
                f"<div class='lst' style='--f:{f}px;--p:{p}px;--g:{g}px'>{r}</div>{nb}")


def cards(tag, items, note=""):
    """items: [(spanish, arabic, tone)] tone in '', 'good', 'bad'; arabic may carry a badge via ('text','badge')."""
    out = ""
    for it in items:
        es, ar = it[0], it[1]
        tone = it[2] if len(it) > 2 else ""
        out += f"<div class='card {tone}'><div class='e'>{es}</div><div class='a'>{ar}</div></div>"
    n = f"<div class='notebar'>{note}</div>" if note else ""
    return page(f"<div class='tag' style='margin-bottom:28px'>{tag}</div><div class='lst'>{out}</div>{n}")


def word(tag, es, pron, mean, pill=""):
    px = _size(es, [(6, 190), (11, 130), (16, 100), (99, 74)])
    p = f"<div class='pill' style='margin-top:36px'>{pill}</div>" if pill else ""
    return page(f"<div class='tag' style='margin-bottom:34px'>{tag}</div><div class='big' style='font-size:{px}px'>{es}</div>"
                f"<div class='pron' style='font-size:80px;margin-top:34px'>{pron}</div>"
                f"<div class='mean' style='font-size:92px;margin-top:14px'>{mean}</div>{p}")


def pair(tag, es1, es2, ar):
    return page(f"<div class='tag' style='margin-bottom:40px'>{tag}</div><div class='big' style='font-size:130px'>{es1}</div>"
                f"<div class='arrow' style='font-size:84px;margin:6px 0'>↓</div>"
                f"<div class='es2l' style='font-size:{_size(es2,[(14,84),(99,66)])}px'>{es2}</div>"
                f"<div class='mean' style='font-size:66px;margin-top:36px'>{ar}</div>")


def quiz(q, opts, foot="اكتب الحرف في الكومنتات | الإجابة بكرة الصبح"):
    def _row(l, t):
        ar = any("\u0600" <= c <= "\u06ff" for c in t[:2])
        return (f"<div class='qo{' rtl' if ar else ''}'><div class='ql'>{l}</div>"
                f"<div class='qt' dir='auto'>{t}</div></div>")
    o = "".join(_row(l, t) for l, t in opts)
    return page(f"<div class='tag' style='margin-bottom:24px'>تحدّي</div><div class='qq'>{q}</div>"
                f"<div style='display:flex;flex-direction:column;gap:16px'>{o}</div>"
                f"<div class='small' style='margin-top:26px;font-size:36px'>{foot}</div>")


def render(pages, outdir):
    """pages: {name: html} -> outdir/name.png (1080x1080)."""
    os.makedirs(outdir, exist_ok=True)
    tmp = f"{outdir}/_html"
    os.makedirs(tmp, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome",
                              args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1080})
        for name, html in pages.items():
            f = f"{tmp}/{name}.html"
            open(f, "w").write(html)
            pg.goto("file://" + f)
            pg.wait_for_timeout(350)
            pg.screenshot(path=f"{outdir}/{name}.png")
        b.close()
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
