"""Scene specs for the three voice-track videos (family / question words / nada-traje).
Times are hand-synced to the supplied audio (rough: the tracks have continuous background music).
Usage: python3 motion_specs.py OUTDIR  -> writes family.json, how.json, nada.json
"""
import json, os, sys

HINT_N = "الـ <b>ñ</b> = «ني»"


def pair(t0, r, t1, eng, ar, es, pron, size, icon, hint="", n=0, tot=0):
    return dict(k="pair", t0=t0, r=r, t1=t1, eng=eng, ar=ar, es=es, pron=pron, size=size, icon=icon, hint=hint, n=n, tot=tot)


def sent(t0, t1, lang, words, w0, w1, tag, ar="", ar_at=None, cta=False):
    return dict(k="sent", t0=t0, t1=t1, lang=lang, words=words, w0=w0, w1=w1, tag=tag, ar=ar, ar_at=ar_at, cta=cta)


# ---------------------------------------------------------------- family (35.35 s)
FAMILY = dict(glyph="¡", scenes=[
    dict(k="title", t0=0, t1=2.95, lines=[["Let's learn", "w"], ["family", "o"], ["basics", "w"]], sub="أساسيات العيلة بالإسباني"),
    dict(k="title", t0=2.95, t1=4.3, lines=[["Spanish", "w"], ["is easy,", "o"], ["right?", "w"]]),
    pair(4.3, 5.5, 7.0, "Dad", "أب", "Papá", "بَابَا", 240, "👨", "النبرة على الآخر: <b>papá</b>", 1, 8),
    pair(7.0, 7.9, 8.7, "Potato", "بطاطس", "Papa", "بَابا", 240, "🥔", "من غير شرطة: <b>papa</b> = بطاطس", 2, 8),
    pair(8.7, 9.5, 10.3, "The Pope", "بابا الفاتيكان", "El Papa", "إِل بَابا", 190, "⛪", "نفس الشكل: <b>el Papa</b>", 3, 8),
    pair(10.3, 10.9, 11.6, "Dude", "يا عم", "Tío", "تِيو", 270, "😎", "في إسبانيا: <b>tío</b> = يا صاحبي", 4, 8),
    pair(11.6, 12.3, 13.05, "Father", "أب", "Padre", "بَادْرِي", 230, "👨‍👧", "", 5, 8),
    pair(13.05, 13.8, 14.5, "How cool!", "يا سلام!", "¡Qué padre!", "كِي بَادْرِي", 150, "🤩", "في المكسيك: <b>padre</b> = رائع", 6, 8),
    pair(14.5, 15.0, 15.65, "Mother", "أم", "Madre", "مَادْرِي", 230, "👩", "", 7, 8),
    pair(15.65, 16.4, 17.3, "Oh my god!", "يا نهار!", "¡Madre mía!", "مَادْرِي مِيا", 150, "😱", "للتعجب في إسبانيا", 8, 8),
    dict(k="title", t0=17.3, t1=19.0, lines=[["Try", "w"], ["this!", "o"]], sub="جرّب الجملة دي بصوت عالي"),
    sent(19.0, 22.3, "en", "My dad eats potato with the Pope. How cool! Oh my God, dude!".split(), 19.1, 22.0, "الجملة بالإنجليزي"),
    sent(22.3, 28.0, "es", "Mi papá come papa con el Papa. ¡Qué padre! ¡Madre mía, tío!".split(), 22.4, 27.0, "الجملة بالإسباني"),
    sent(28.0, 33.8, "es", "Mi papá come papa con el Papa. ¡Qué padre! ¡Madre mía, tío!".split(), 28.1, 32.5, "كرّرها معانا",
         ar="أبويا بياكل بطاطس مع البابا. يا سلام! يا نهار يا صاحبي!", ar_at=29.0),
    dict(k="end", t0=33.8, t1=35.35, lines=["تابعنا لكلمات جديدة كل يوم"]),
])

# ---------------------------------------------------------------- question words (10.86 s)
HOW = dict(glyph="¿", scenes=[
    pair(0.0, 0.65, 1.3, "What", "إيه؟", "¿Qué?", "كِي", 250, "❓", "", 1, 8),
    pair(1.3, 1.95, 2.8, "Why", "ليه؟", "¿Por qué?", "بُور كِي", 190, "🤔", "", 2, 8),
    pair(2.8, 3.4, 4.0, "Where", "فين؟", "¿Dónde?", "دُونْدِي", 220, "📍", "", 3, 8),
    pair(4.0, 4.6, 5.2, "Who", "مين؟", "¿Quién?", "كْيِين", 240, "🧑", "", 4, 8),
    pair(5.2, 5.85, 6.6, "How", "إزاي؟", "¿Cómo?", "كُومو", 240, "🛠️", "", 5, 8),
    pair(6.6, 7.2, 8.0, "When", "إمتى؟", "¿Cuándo?", "كُوانْدو", 210, "⏰", "", 6, 8),
    pair(8.0, 8.65, 9.4, "How much", "بكام؟", "¿Cuánto?", "كُوانْتو", 210, "💰", "", 7, 8),
    pair(9.4, 10.0, 10.86, "How many", "كام واحد؟", "¿Cuántos?", "كُوانْتوس", 190, "🔢", "", 8, 8),
])

# ---------------------------------------------------------------- nada / traje (33.74 s)
NADA = dict(glyph="ñ", scenes=[
    dict(k="title", t0=0, t1=2.1, lines=[["Spanish", "w"], ["is easy,", "o"], ["right?", "w"]]),
    pair(2.1, 3.9, 5.6, "Nothing / At all", "ولا حاجة / خالص", "Nada", "نَادَا", 270, "🚫", "", 1, 6),
    pair(5.6, 6.4, 7.3, "He swims", "هو بيعوم", "Nada", "نَادَا", 270, "🏊", "نفس الكلمة! الفعل: <b>nadar</b>", 2, 6),
    pair(7.3, 7.9, 8.9, "I swim", "أنا بعوم", "Nado", "نَادو", 270, "🏊‍♂️", "", 3, 6),
    pair(8.9, 9.4, 10.4, "Swimsuit", "مايوه", "Traje", "تْرَاخِي", 250, "🩱", "", 4, 6),
    pair(10.4, 11.0, 12.1, "I brought", "أنا جبت", "Traje", "تْرَاخِي", 250, "🎒", "نفس الكلمة! الفعل: <b>traer</b>", 5, 6),
    pair(12.1, 12.7, 15.3, "Because", "علشان", "Porque", "بُورْكِي", 230, "💡", "", 6, 6),
    sent(15.3, 19.6, "en", "I don't swim at all because I didn't bring a swimsuit.".split(), 15.4, 19.2, "الجملة بالإنجليزي"),
    sent(19.6, 24.3, "es", "No nado nada porque no traje traje.".split(), 19.7, 23.4, "الجملة بالإسباني"),
    sent(24.3, 29.0, "es", "No nado nada porque no traje traje.".split(), 24.4, 28.1, "كرّرها بسرعة",
         ar="مبعومش خالص علشان معييش مايوه.", ar_at=25.2),
    sent(29.0, 33.74, "es", "No nado nada porque no traje traje.".split(), 29.1, 32.8, "تحدّي السرعة!",
         ar="مبعومش خالص علشان معييش مايوه.", ar_at=29.1, cta=True),
])

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    for name, spec in (("family", FAMILY), ("how", HOW), ("nada", NADA)):
        json.dump(spec, open(f"{out}/{name}.json", "w"), ensure_ascii=False)
        print(name)
