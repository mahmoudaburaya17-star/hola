"""Day 8 reels (family). Usage: python3 day08.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day08_words", title1="احكي عن عيلتك", title2="بالإسباني! 👨‍👩‍👧‍👦",
         cta="اكتب في الكومنتات:<br><span class='ltr'>Tengo ___ hermanos</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Hermano", size=190, pron="إِرْمَانو", mean="أخ", pill="المؤنث: <span class='ltr'>hermana</span> = أخت",
      note="الـ h صامتة", say="Hermano", example="Tengo un hermano."),
 dict(tag="الكلمة التانية", es="Hermana", size=190, pron="إِرْمَانا", mean="أخت", pill="o = مذكر · a = مؤنث",
      note="الـ h صامتة", say="Hermana", example="Tengo una hermana."),
 dict(tag="الكلمة التالتة", es="Abuelo", size=210, pron="أَبُوِيلو", mean="جد", pill="المؤنث: <span class='ltr'>abuela</span> = جدة",
      note="الـ b بتتنطق ب", say="Abuelo", example="Mi abuelo es simpático."),
 dict(tag="الكلمة الرابعة", es="Abuela", size=210, pron="أَبُوِيلا", mean="جدة", pill="الجمع: <span class='ltr'>abuelos</span> = الأجداد",
      note="الـ ue = «ويـ»", say="Abuela", example="Mi abuela cocina muy bien."),
 ],
 recap=[("أخ", "Hermano"), ("أخت", "Hermana"), ("جد", "Abuelo"), ("جدة", "Abuela")],
 q_ar="«جدة» بالإسباني؟", q_right="Abuela.", q_wrong="Hermana.")

D = dict(file="reel_day08_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="لوسيا وعمر 👪",
         cta="احكي عن عيلتك<br>بالإسباني في الكومنتات",
         lines=[
 dict(name="لوسيا", side="l", voice="ef_dora", es="¿Tienes hermanos?", ar="عندك إخوات؟"),
 dict(name="عمر", side="r", voice="em_alex", es="Sí, tengo un hermano y dos hermanas.", ar="أيوه، عندي أخ وأختين."),
 dict(name="لوسيا", side="l", voice="ef_dora", es="¿Y tus abuelos?", ar="وأجدادك؟"),
 dict(name="عمر", side="r", voice="em_alex", es="Mi abuela vive con nosotros.", ar="جدتي عايشة معانا."),
 dict(name="لوسيا", side="l", voice="ef_dora", es="¡Qué bonito!", ar="جميل!"),
 dict(name="عمر", side="r", voice="em_alex", es="Sí, mi familia es muy unida.", ar="أيوه، عيلتي مترابطة جدًا."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
