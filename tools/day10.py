"""Day 10 reels. Usage: python3 day10.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day10_words", title1="الألوان", title2="بالإسباني! 🎨",
         cta="اكتب في الكومنتات:<br><span class='ltr'>Mi color favorito es ___</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Rojo", size=270, pron="رُوخو", mean="أحمر", pill="المؤنث: <span class='ltr'>roja</span>",
      note="الـ j = خ", say="Rojo", example="El coche es rojo."),
 dict(tag="الكلمة التانية", es="Azul", size=270, pron="أَثُول", mean="أزرق", pill="ثابتة للمذكر والمؤنث",
      note="الـ z = ث في إسبانيا", say="Azul", example="La casa es azul."),
 dict(tag="الكلمة التالتة", es="Verde", size=250, pron="بِيرْدِي", mean="أخضر", pill="ثابتة للمذكر والمؤنث",
      note="الـ v = ب", say="Verde", example="Me gusta el verde."),
 dict(tag="الكلمة الرابعة", es="Amarillo", size=190, pron="أَمَارِيّو", mean="أصفر", pill="المؤنث: <span class='ltr'>amarilla</span>",
      note="الـ ll = ي", say="Amarillo", example="Mi casa es amarilla."),
 ],
 recap=[("أحمر", "Rojo"), ("أزرق", "Azul"), ("أخضر", "Verde"), ("أصفر", "Amarillo")],
 q_ar="«أخضر» بالإسباني؟", q_right="Verde.", q_wrong="Rojo.")

D = dict(file="reel_day10_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="مارتا وكريم 🎨",
         cta="قول لون عربيتك<br>بالإسباني في الكومنتات",
         lines=[
 dict(name="مارتا", side="l", voice="ef_dora", es="¿De qué color es tu coche?", ar="إيه لون عربيتك؟"),
 dict(name="كريم", side="r", voice="em_alex", es="Es rojo. ¿Y el tuyo?", ar="أحمر. وبتاعك؟"),
 dict(name="مارتا", side="l", voice="ef_dora", es="El mío es blanco.", ar="بتاعي أبيض."),
 dict(name="كريم", side="r", voice="em_alex", es="¡Mira! Mi casa es amarilla.", ar="بص! بيتي أصفر."),
 dict(name="مارتا", side="l", voice="ef_dora", es="¡Qué bonita!", ar="جميل!"),
 dict(name="كريم", side="r", voice="em_alex", es="Mi color favorito es el verde.", ar="لوني المفضل الأخضر."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
