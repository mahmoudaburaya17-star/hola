"""Scene specs for the three voice-track videos (family / question words / nada-traje).
Times are hand-synced to the supplied audio (rough: the tracks have continuous background music).
Usage: python3 motion_specs.py OUTDIR  -> writes easy.json, family.json, how.json, nada.json
"""
import json, os, sys

HINT_N = "الـ <b>ñ</b> = «ني»"


def pair(t0, r, t1, eng, ar, es, pron, size, icon, hint="", n=0, tot=0):
    return dict(k="pair", t0=t0, r=r, t1=t1, eng=eng, ar=ar, es=es, pron=pron, size=size, icon=icon, hint=hint, n=n, tot=tot)


def sent(t0, t1, lang, words, w0, w1, tag, ar="", ar_at=None, cta=False):
    return dict(k="sent", t0=t0, t1=t1, lang=lang, words=words, w0=w0, w1=w1, tag=tag, ar=ar, ar_at=ar_at, cta=cta)


# ---------------------------------------------------------------- Spanish is easy (35.27 s)
def times(a, b, n):
    return [round(a + (b - a) * i / n, 3) for i in range(n)]


EASY = dict(glyph="ñ", scenes=[
    dict(k="title", t0=0, t1=3.4, lines=[["Spanish", "w"], ["is easy,", "o"], ["right?", "w"]], sub="حرف واحد بيخلّي الكلام ده كله سهل"),
    dict(k="title", t0=3.4, t1=6.4, lines=[["How do you say", "w"], ["“tomorrow”", "o"], ["in Spanish?", "w"]], sub="إزاي تقول «غدًا» بالإسباني؟"),
    pair(6.4, 6.55, 7.9, "Tomorrow", "غدًا", "Mañana", "مَانْيَانا", 240, "🌅", HINT_N, 1, 9),
    pair(7.9, 8.9, 9.6, "Morning", "الصباح", "Mañana", "مَانْيَانا", 240, "☀️", "نفس الكلمة: غدًا = الصباح", 2, 9),
    pair(9.6, 10.5, 11.2, "Spider", "عنكبوت", "Araña", "أَرَانْيا", 260, "🕷️", "", 3, 9),
    pair(11.2, 12.0, 12.8, "Scratches", "يخدش", "Arañar", "أَرَانْيَار", 240, "🐾", "", 4, 9),
    pair(12.8, 13.75, 14.45, "Skill", "مهارة", "Maña", "مَانْيا", 270, "🎯", "con maña = بمهارة", 5, 9),
    pair(14.45, 15.1, 15.98, "Spiderweb", "شبكة العنكبوت", "Telaraña", "تِيلَرَانْيا", 210, "🕸️", "", 6, 9),
    pair(15.98, 16.7, 17.6, "Strange", "غريبة", "Extraña", "إِكْسْتْرَانْيا", 220, "👽", "", 7, 9),
    pair(17.6, 18.3, 19.15, "Spain", "إسبانيا", "España", "إِسْبَانْيا", 250, "🇪🇸", "الـ ñ هي سبب اسم البلد كمان!", 8, 9),
    pair(19.15, 19.9, 20.9, "Mountain", "جبل", "Montaña", "مُونْتَانْيا", 190, "⛰️", "", 9, 9),
    dict(k="title", t0=20.9, t1=22.5, lines=[["Try", "w"], ["this!", "o"]], sub="جرّب الجملة دي بصوت عالي"),
    sent(22.5, 28.58, "en", "Tomorrow morning, the strange spider from Spain skillfully scratches the spider web on the mountain.".split(),
         22.56, 28.3, "الجملة بالإنجليزي"),
    dict(sent(28.58, 35.27, "es", "Mañana por la mañana, la extraña araña de España, araña con maña la telaraña de la montaña.".split(),
              28.62, 35.0, "الجملة بالإسباني", ar="بكرة الصبح، العنكبوتة الغريبة من إسبانيا بتخدش بمهارة شبكتها في الجبل.", ar_at=30.5, cta=True),
         times=times(28.62, 30.34, 4) + times(30.5, 34.9, 13)),
])

# ---------------------------------------------------------------- family (35.35 s)
FAMILY = dict(glyph="¡", scenes=[
    dict(k="title", t0=0, t1=3.0, lines=[["Let's learn", "w"], ["family", "o"], ["basics", "w"]], sub="أساسيات العيلة بالإسباني"),
    dict(k="title", t0=3.0, t1=4.9, lines=[["Spanish", "w"], ["is easy,", "o"], ["right?", "w"]]),
    pair(4.9, 5.94, 6.85, "Dad", "أب", "Papá", "بَابَا", 240, "👨", "النبرة على الآخر: <b>papá</b>", 1, 9),
    pair(6.85, 7.75, 8.3, "Potato", "بطاطس", "Papa", "بَابا", 240, "🥔", "من غير شرطة: <b>papa</b> = بطاطس", 2, 9),
    pair(8.3, 9.1, 9.7, "The Pope", "بابا الفاتيكان", "El Papa", "إِل بَابا", 190, "⛪", "نفس الشكل: <b>el Papa</b>", 3, 9),
    pair(9.7, 10.44, 10.95, "Uncle", "عمّ / خال", "Tío", "تِيو", 270, "👴", "", 4, 9),
    pair(10.95, 11.8, 12.25, "Dude", "يا صاحبي", "Tío", "تِيو", 270, "😎", "نفس الكلمة! في إسبانيا <b>tío</b> = يا صاحبي", 5, 9),
    pair(12.25, 13.13, 13.75, "Father", "أب", "Padre", "بَادْرِي", 230, "👨‍👧", "", 6, 9),
    pair(13.75, 14.46, 15.62, "How cool!", "يا سلام!", "¡Qué padre!", "كِي بَادْرِي", 150, "🤩", "في المكسيك: <b>padre</b> = رائع", 7, 9),
    pair(15.62, 16.2, 16.55, "Mother", "أم", "Madre", "مَادْرِي", 230, "👩", "", 8, 9),
    pair(16.55, 17.32, 18.25, "Oh my god!", "يا نهار!", "¡Madre mía!", "مَادْرِي مِيا", 150, "😱", "للتعجب في إسبانيا", 9, 9),
    dict(k="title", t0=18.25, t1=19.1, lines=[["Try", "w"], ["this!", "o"]], sub="جرّب الجملة دي بصوت عالي"),
    sent(19.1, 23.4, "en", "My dad eats potato with the Pope. How cool! Oh my God, dude!".split(), 19.2, 22.4, "الجملة بالإنجليزي"),
    sent(23.4, 28.75, "es", "Mi papá come papa con el Papa. ¡Qué padre! ¡Madre mía, tío!".split(), 23.55, 28.3, "الجملة بالإسباني"),
    sent(28.75, 33.85, "es", "Mi papá come papa con el Papa. ¡Qué padre! ¡Madre mía, tío!".split(), 28.85, 33.4, "كرّرها معانا",
         ar="أبويا بياكل بطاطس مع البابا. يا سلام! يا نهار يا صاحبي!", ar_at=29.8),
    dict(k="end", t0=33.85, t1=35.35, lines=["تابعنا لكلمات جديدة كل يوم"]),
])

# ---------------------------------------------------------------- question words (10.86 s)
HOW = dict(glyph="¿", scenes=[
    pair(0.0, 0.8, 1.38, "What", "إيه؟", "¿Qué?", "كِي", 250, "❓", "", 1, 8),
    pair(1.38, 1.9, 2.68, "Why", "ليه؟", "¿Por qué?", "بُور كِي", 190, "🤔", "", 2, 8),
    pair(2.68, 3.38, 3.93, "Where", "فين؟", "¿Dónde?", "دُونْدِي", 220, "📍", "", 3, 8),
    pair(3.93, 4.76, 5.3, "Who", "مين؟", "¿Quién?", "كْيِين", 240, "🧑", "", 4, 8),
    pair(5.3, 6.11, 6.64, "How", "إزاي؟", "¿Cómo?", "كُومو", 240, "🛠️", "", 5, 8),
    pair(6.64, 7.43, 8.02, "When", "إمتى؟", "¿Cuándo?", "كُوانْدو", 210, "⏰", "", 6, 8),
    pair(8.02, 8.65, 9.36, "How much", "بكام؟", "¿Cuánto?", "كُوانْتو", 210, "💰", "", 7, 8),
    pair(9.36, 10.0, 10.86, "How many", "كام واحد؟", "¿Cuántos?", "كُوانْتوس", 190, "🔢", "", 8, 8),
])

# ---------------------------------------------------------------- nada / traje (33.71 s)
NADA = dict(glyph="ñ", scenes=[
    dict(k="title", t0=0, t1=2.45, lines=[["Spanish", "w"], ["is easy,", "o"], ["right?", "w"]]),
    dict(k="title", t0=2.45, t1=4.7, lines=[["How do you say", "w"], ["“nothing”", "o"], ["in Spanish?", "w"]], sub="إزاي تقول «ولا حاجة» بالإسباني؟"),
    pair(4.7, 5.77, 6.45, "Nothing / At all", "ولا حاجة / خالص", "Nada", "نَادَا", 270, "🚫", "", 1, 6),
    pair(6.45, 7.4, 8.05, "He swims", "هو بيعوم", "Nada", "نَادَا", 270, "🏊", "نفس الكلمة! الفعل: <b>nadar</b>", 2, 6),
    pair(8.05, 9.0, 9.6, "I swim", "أنا بعوم", "Nado", "نَادو", 270, "🏊‍♂️", "", 3, 6),
    pair(9.6, 10.64, 11.2, "Swimsuit", "مايوه", "Traje", "تْرَاخِي", 250, "🩱", "", 4, 6),
    pair(11.2, 12.26, 12.85, "I brought", "أنا جبت", "Traje", "تْرَاخِي", 250, "🎒", "نفس الكلمة! الفعل: <b>traer</b>", 5, 6),
    pair(12.85, 13.77, 14.75, "Because", "علشان", "Porque", "بُورْكِي", 230, "💡", "", 6, 6),
    dict(k="title", t0=14.75, t1=15.95, lines=[["Try", "w"], ["this!", "o"]], sub="جرّب الجملة دي بصوت عالي"),
    sent(15.95, 18.75, "en", "I don't swim at all because I didn't bring a swimsuit.".split(), 16.1, 17.8, "الجملة بالإنجليزي"),
    sent(18.75, 20.85, "en", "I didn't bring a swimsuit because I don't swim at all.".split(), 18.85, 20.4, "ونقدر نقولها بالعكس"),
    sent(20.85, 24.2, "es", "No nado nada porque no traje traje.".split(), 20.95, 23.6, "الجملة بالإسباني",
         ar="مبعومش خالص علشان معييش مايوه.", ar_at=22.0),
    sent(24.2, 29.0, "es", "No traje traje porque no nado nada.".split(), 24.3, 28.4, "بالعكس: كمان بالإسباني", ar="معييش مايوه علشان مبعومش خالص.", ar_at=25.2),
    sent(29.0, 33.71, "es", "No nado nada porque no traje traje.".split(), 29.1, 32.9, "تحدّي السرعة!",
         ar="مبعومش خالص علشان معييش مايوه.", ar_at=29.1, cta=True),
])

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    for name, spec in (("easy", EASY), ("family", FAMILY), ("how", HOW), ("nada", NADA)):
        json.dump(spec, open(f"{out}/{name}.json", "w"), ensure_ascii=False)
        print(name)
