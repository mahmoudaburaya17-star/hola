"""Edu video for the 'Spanish is easy' (n-tilde words) voice track. 1080x1920, synced by hand to the audio.
Usage: HOLA_WORK=... python3 spanish_is_easy.py AUDIO OUT_MP4
"""
import os, sys, re, shutil, subprocess
from playwright.sync_api import sync_playwright

S = os.environ.get("HOLA_WORK", "/tmp/hola-work")
FP = f"{S}/fontpkg/node_modules/@fontsource"
BASE = open(f"{S}/reel/base.css").read().replace("__FP__", FP)
EXTRA = """
.wm{position:absolute;top:92px;left:0;right:0;text-align:center;font-size:58px;font-weight:800;z-index:5}
.wm .o{color:var(--or)}
.col{padding-top:250px;justify-content:flex-start}
.col.mid{justify-content:center;padding-top:60px;padding-bottom:120px}
.eng{font-family:'Poppins',sans-serif;direction:ltr;font-weight:600;font-size:76px;color:#cfd9ee;letter-spacing:6px;text-transform:uppercase}
.ar{font-weight:800;font-size:92px;margin-top:14px;line-height:1.3}
.sp{font-family:'Poppins',sans-serif;font-weight:700;color:var(--or);direction:ltr;text-align:center;white-space:nowrap;line-height:1.1}
.sp .n,.kw .n{color:var(--teal)}
.spbox{height:330px;display:flex;align-items:center;justify-content:center;margin-top:60px}
.q2{color:#35466d;font-family:'Poppins',sans-serif;font-weight:700;font-size:240px}
.pr{color:var(--teal);font-weight:800;font-size:100px;margin-top:10px;line-height:1.3;min-height:130px}
.hint{background:var(--card);border:3px solid var(--teal);color:#fff;font-weight:700;font-size:46px;padding:20px 54px;border-radius:70px;margin-top:56px}
.hint b{color:var(--teal);font-family:'Poppins',sans-serif}
.dots{position:absolute;bottom:150px;left:0;right:0;display:flex;justify-content:center;gap:18px;direction:ltr}
.dots i{width:22px;height:22px;border-radius:50%;background:#2b3d66}
.dots i.on{background:var(--or)}
.bigq{font-family:'Poppins',sans-serif;font-weight:800;font-size:112px;line-height:1.25;text-align:center;direction:ltr}
.bigq .o{color:var(--or)}
.sent{font-family:'Poppins',sans-serif;font-weight:700;font-size:78px;line-height:1.5;text-align:center;direction:ltr;max-width:960px}
.sent span{color:#4a5c86}
.sent span.on{color:#fff}
.sent span.cur{color:var(--or)}
.sent.esx span.on{color:var(--or)}
.sent.esx span.cur{color:#fff;text-shadow:0 0 30px rgba(255,165,31,.8)}
.cta{position:absolute;bottom:130px;left:0;right:0;text-align:center;font-size:50px;font-weight:700;color:#9fb0cf}
.cta b{color:var(--or)}
.sub{color:#9fb0cf;font-size:52px;font-weight:500;margin-top:40px;text-align:center;line-height:1.5}
"""
CSS = BASE + EXTRA

def n(w):  # highlight the n-tilde
    return re.sub("([ñÑ])", r"<span class='n'>\1</span>", w)

def page(inner, dots=None, extra="", mid=False):
    d = ""
    if dots is not None:
        d = "<div class='dots'>" + "".join(f"<i class='{'on' if i <= dots else ''}'></i>" for i in range(9)) + "</div>"
    wm = "<div class='wm'>أهلاً <span class='o ltr'>Hola</span></div>"
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='glow'></div>{wm}"
            f"<div class='col{' mid' if mid else ''}'>{inner}</div>{d}{extra}</body></html>")

def pair(k, eng, ar, es, pron, size, reveal, hint=""):
    sp = f"<div class='sp' style='font-size:{size}px'>{n(es)}</div>" if reveal else "<div class='q2'>?</div>"
    pr = f"<div class='pr'>{pron}</div>" if reveal else "<div class='pr'></div>"
    h = f"<div class='hint'>{hint}</div>" if (reveal and hint) else "<div class='hint' style='visibility:hidden'>.</div>"
    return page(f"<div class='tag' style='margin-bottom:56px'>كلمة {k} من 9</div><div class='eng'>{eng}</div>"
                f"<div class='ar'>{ar}</div><div class='spbox'>{sp}</div>{pr}{h}", dots=k)

def sentence(words, i, es=False, cta=False):
    sp = "".join(f"<span class='{'cur' if j == i else ('on' if j < i else '')}'>{n(w) if es else w}</span> " for j, w in enumerate(words))
    tag = "الجملة بالإسباني" if es else "الجملة بالإنجليزي"
    c = "<div class='cta'>تابع <b>أهلاً Hola</b> لكلمات جديدة كل يوم</div>" if cta else ""
    return page(f"<div class='tag' style='margin-bottom:80px'>{tag}</div><div class='sent{' esx' if es else ''}'>{sp}</div>", extra=c, mid=True)

EN = "Tomorrow morning, the strange spider from Spain skillfully scratches the spider web on the mountain.".split()
ES = "Mañana por la mañana, la extraña araña de España araña con maña la telaraña de la montaña.".split()
HINT = "حرف <b>ñ</b> = «ني» ← زي «ماني» في العربي"

def timeline():
    T = []  # (start, html)
    T.append((0.0, page("<div class='bigq'>Spanish<br>is <span class='o'>easy</span>,<br>right?</div>"
                        "<div class='sub'>حرف واحد بيخلّي الكلام ده كله سهل<br><span class='ltr' style='color:#2EC4B6;font-size:90px'>ñ</span></div>", mid=True)))
    T.append((3.3, page("<div class='bigq' style='font-size:92px'>How do you say<br><span class='o'>“tomorrow”</span><br>in Spanish?</div>"
                        "<div class='sub'>إزاي تقول «غدًا» بالإسباني؟</div>", mid=True)))
    T.append((6.1, pair(1, "Tomorrow", "غدًا", "Mañana", "مَانْيَانا", 240, False)))
    T.append((6.25, pair(1, "Tomorrow", "غدًا", "Mañana", "مَانْيَانا", 240, True, HINT)))
    T.append((7.0, pair(2, "Morning", "الصباح", "Mañana", "مَانْيَانا", 240, False)))
    T.append((8.8, pair(2, "Morning", "الصباح", "Mañana", "مَانْيَانا", 240, True, "نفس الكلمة: غدًا = الصباح")))
    T.append((9.8, pair(3, "Spider", "عنكبوت", "Araña", "أَرَانْيا", 260, False)))
    T.append((10.4, pair(3, "Spider", "عنكبوت", "Araña", "أَرَانْيا", 260, True)))
    T.append((11.0, pair(4, "Scratches", "يخدش", "Arañar", "أَرَانْيَار", 240, False)))
    T.append((12.0, pair(4, "Scratches", "يخدش", "Arañar", "أَرَانْيَار", 240, True)))
    T.append((13.2, pair(5, "Skill", "مهارة", "Maña", "مَانْيا", 270, False)))
    T.append((13.7, pair(5, "Skill", "مهارة", "Maña", "مَانْيا", 270, True, "con maña = بمهارة")))
    T.append((14.2, pair(6, "Spiderweb", "شبكة العنكبوت", "Telaraña", "تِيلَرَانْيا", 210, False)))
    T.append((14.95, pair(6, "Spiderweb", "شبكة العنكبوت", "Telaraña", "تِيلَرَانْيا", 210, True)))
    T.append((15.9, pair(7, "Strange", "غريبة", "Extraña", "إِكْسْتْرَانْيا", 220, False)))
    T.append((16.4, pair(7, "Strange", "غريبة", "Extraña", "إِكْسْتْرَانْيا", 220, True)))
    T.append((17.2, pair(8, "Spain", "إسبانيا", "España", "إِسْبَانْيا", 250, False)))
    T.append((17.9, pair(8, "Spain", "إسبانيا", "España", "إِسْبَانْيا", 250, True, "الـ ñ هي سبب اسم البلد كمان!")))
    T.append((18.64, pair(9, "Mountain", "جبل", "Montaña", "مُونْتَانْيا", 190, False)))
    T.append((19.3, pair(9, "Mountain", "جبل", "Montaña", "مُونْتَانْيا", 190, True)))
    T.append((20.7, page("<div class='bigq'>Try<br><span class='o'>this!</span></div><div class='sub'>جرّب الجملة دي بصوت عالي</div>", mid=True)))
    # English sentence karaoke 22.27 -> 28.4
    t0, t1 = 22.27, 28.4
    for i in range(len(EN)):
        T.append((t0 + (t1 - t0) * i / len(EN), sentence(EN, i)))
    # Spanish sentence karaoke 28.45 -> 34.4
    s0, s1 = 28.45, 34.4
    for i in range(len(ES)):
        T.append((s0 + (s1 - s0) * i / len(ES), sentence(ES, i, es=True, cta=(i >= len(ES) - 3))))
    return T

def main(audio, out):
    work = os.path.abspath(out) + "_work"
    shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio]))
    T = timeline()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for i, (t, html) in enumerate(T):
            f = f"{work}/s{i:03d}.html"
            open(f, "w").write(html)
            pg.goto("file://" + f); pg.wait_for_timeout(250)
            pg.screenshot(path=f"{work}/s{i:03d}.jpg", type="jpeg", quality=92)
        b.close()
    clips = []
    for i, (t, _) in enumerate(T):
        end = T[i + 1][0] if i + 1 < len(T) else dur
        d = round(end - t, 3)
        c = f"{work}/c{i:03d}.mp4"
        tmp = f"{work}/c{i:03d}.tmp.mp4"
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", f"{work}/s{i:03d}.jpg",
            "-vf", f"format=yuv420p,loop=-1:1,trim=duration={d},setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.08",
            "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30", tmp])
        os.rename(tmp, c); clips.append(c)
    open(f"{work}/list.txt", "w").write("".join(f"file '{c}'\n" for c in clips))
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt", "-c", "copy", f"{work}/v.mp4"])
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{work}/v.mp4", "-i", audio,
        "-f", "lavfi", "-i", f"color=c=0xFFA51F:s=1080x12:d={dur}",
        "-filter_complex", f"[0:v][2:v]overlay=x='-1080+1080*t/{dur}':y=1908[v]",
        "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out])
    print(out, dur)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
