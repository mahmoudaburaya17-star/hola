"""Day 11 reels. Usage: python3 day11.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day11_words", title1="وصّف أي حاجة", title2="بالإسباني! ✨",
         cta="اكتب في الكومنتات:<br><span class='ltr'>Mi casa es ___</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Grande", size=230, pron="غْرَانْدي", mean="كبير", pill="ثابتة للمذكر والمؤنث",
      note="الـ g قبل r = غ", say="Grande", example="La casa es grande."),
 dict(tag="الكلمة التانية", es="Pequeño", size=200, pron="بِكِينْيو", mean="صغير", pill="المؤنث: <span class='ltr'>pequeña</span>",
      note="الـ ñ = «ني»", say="Pequeño", example="El jardín es pequeño."),
 dict(tag="الكلمة التالتة", es="Bonito", size=230, pron="بُونِيتو", mean="جميل", pill="المؤنث: <span class='ltr'>bonita</span>",
      note="الـ b = ب", say="Bonito", example="Es muy bonito."),
 dict(tag="الكلمة الرابعة", es="Nuevo", size=250, pron="نُوِيبو", mean="جديد", pill="المؤنث: <span class='ltr'>nueva</span>",
      note="الـ ue = «وي»", say="Nuevo", example="Tengo una casa nueva."),
 ],
 recap=[("كبير", "Grande"), ("صغير", "Pequeño"), ("جميل", "Bonito"), ("جديد", "Nuevo")],
 q_ar="«صغير» بالإسباني؟", q_right="Pequeño.", q_wrong="Grande.")

D = dict(file="reel_day11_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="لوسيا وعمر ✨",
         cta="وصّف بيتك<br>بالإسباني في الكومنتات",
         lines=[
 dict(name="لوسيا", side="l", voice="ef_dora", es="¿Cómo es tu casa nueva?", ar="إيه شكل بيتك الجديد؟"),
 dict(name="عمر", side="r", voice="em_alex", es="Es pequeña, pero muy bonita.", ar="صغير بس حلو أوي."),
 dict(name="لوسيا", side="l", voice="ef_dora", es="¿Tiene un jardín grande?", ar="فيه جنينة كبيرة؟"),
 dict(name="عمر", side="r", voice="em_alex", es="No, el jardín es pequeño.", ar="لأ، الجنينة صغيرة."),
 dict(name="لوسيا", side="l", voice="ef_dora", es="No importa. ¡Es perfecta!", ar="مش مهم. دي مثالية!"),
 dict(name="عمر", side="r", voice="em_alex", es="Gracias. Ven a verla.", ar="شكرًا. تعالي شوفيه."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
