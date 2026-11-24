"""Images for week 2 text posts. Usage: python3 week02.py OUTDIR [day ...]

Writes OUTDIR/day-NN/{lesson-N,carousel-N,words,quiz}.png (1080x1080).
Day 1's lesson/carousel/words already exist in media/day-01; only its quiz is generated here.
"""
import sys
from postimg import cover, rows, cards, word, pair, quiz, render

L = "<span class='ltr'>{}</span>"
def lt(x): return L.format(x)


DAYS = {}
# ---------------- week 2 / day 8: family
DAYS[8] = {
 "lesson-1": cover("إزاي تحكي", "عن عيلتك", "بالإسباني؟", "Mi familia"),
 "lesson-2": cards("احكي عن عيلتك", [("Mi familia es grande.", "عيلتي كبيرة"), ("Tengo dos hermanos y una hermana.", "عندي أخوين وأخت")],
                   f"الفعل {lt('tengo')} = عندي"),
 "lesson-3": rows("أفراد العيلة", [("أب / أم", "padre / madre"), ("أخ / أخت", "hermano / hermana"),
                                   ("جد / جدة", "abuelo / abuela"), ("ابن / بنت", "hijo / hija")]),
 "lesson-4": cards("نصيحة", [("o = مذكر · a = مؤنث", "hermano ← hermana"),
                             ("mi / mis", "mi hermano · mis hermanos")],
                   f"{lt('mi')} للمفرد و{lt('mis')} للجمع"),
 "carousel-1": cover("أفراد العيلة", "بالإسباني", "", "اسحب ←"),
 "carousel-2": rows("1", [("أب", "padre"), ("أم", "madre")]),
 "carousel-3": rows("2", [("أخ", "hermano"), ("أخت", "hermana")]),
 "carousel-4": rows("3", [("جد", "abuelo"), ("جدة", "abuela")]),
 "carousel-5": rows("4", [("ابن", "hijo"), ("بنت", "hija")]),
 "carousel-6": cover(lt("Tengo ___"), "hermanos", "", "اكتب عددهم في الكومنتات"),
 "words": rows("كلمات اليوم", [("أب", "Padre"), ("أم", "Madre"), ("أخ", "Hermano"), ("أخت", "Hermana"),
                               ("جد", "Abuelo"), ("جدة", "Abuela"), ("عيلة", "Familia")]),
 "quiz": quiz("«أخت» بالإسباني؟", [("A", "Hermano"), ("B", "Hermana"), ("C", "Abuela")]),
}

DAYS[9] = {
 "lesson-1": cover("تعالى أوريك", "بيتي", "بالإسباني", "Mi casa"),
 "lesson-2": cards("رحّب بضيوفك", [("¡Bienvenido a mi casa!", "أهلاً بيك في بيتي!"), ("Mi casa tiene tres habitaciones.", "بيتي فيه 3 غرف")],
                   f"{lt('habitación')} = غرفة"),
 "lesson-3": rows("أجزاء البيت", [("البيت", "la casa"), ("المطبخ", "la cocina"), ("الحمام", "el baño"),
                                  ("أوضة النوم", "el dormitorio")]),
 "lesson-4": cards("hay ولا está؟", [("Hay un jardín.", "فيه جنينة"), ("La cocina está allí.", "المطبخ هناك")],
                   f"{lt('hay')} لوجود الشيء، و{lt('está')} لمكانه"),
 "carousel-1": cover("أجزاء البيت", "بالإسباني", "", "اسحب ←"),
 "carousel-2": rows("1", [("البيت", "la casa"), ("المطبخ", "la cocina")]),
 "carousel-3": rows("2", [("الحمام", "el baño"), ("أوضة النوم", "el dormitorio")]),
 "carousel-4": rows("3", [("الصالون", "el salón"), ("الجنينة", "el jardín")]),
 "carousel-5": cards("اسأل", [("¿Dónde está la cocina?", "فين المطبخ؟")], f"الرد: {lt('Está allí')} = هناك"),
 "carousel-6": cover(lt("Mi casa tiene ___"), "habitaciones", "", "اكتب عدد غرفك في الكومنتات"),
 "words": rows("كلمات اليوم", [("البيت", "Casa"), ("المطبخ", "Cocina"), ("الحمام", "Baño"), ("أوضة النوم", "Dormitorio"),
                               ("الصالون", "Salón"), ("الجنينة", "Jardín")]),
 "quiz": quiz("«مطبخ» بالإسباني؟", [("A", "Baño"), ("B", "Cocina"), ("C", "Salón")]),
}

if __name__ == "__main__":
    out = sys.argv[1]
    days = [int(x) for x in sys.argv[2:]] or sorted(DAYS)
    for d in days:
        render(DAYS[d], f"{out}/day-{d:02d}")
        print("day", d, len(DAYS[d]), "images")
