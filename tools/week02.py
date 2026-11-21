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

if __name__ == "__main__":
    out = sys.argv[1]
    days = [int(x) for x in sys.argv[2:]] or sorted(DAYS)
    for d in days:
        render(DAYS[d], f"{out}/day-{d:02d}")
        print("day", d, len(DAYS[d]), "images")
