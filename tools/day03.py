"""Day 3 reels (numbers / tener). Usage: python3 day03.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day03_words", title1="عُدّ بالإسباني", title2="في 30 ثانية!",
         cta="اكتب عمرك في الكومنتات:<br><span class='ltr'>Tengo ___ años</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Cinco", size=210, pron="ثِينْكو", mean="خمسة (5)", pill="حرف C قبل I = ث (في إسبانيا)",
      note="وفي أمريكا اللاتينية بتتنطق س", say="Cinco", example="Tengo cinco libros."),
 dict(tag="الكلمة التانية", es="Diez", size=230, pron="دْيِث", mean="عشرة (10)", pill="الـ z بتتنطق ث",
      note="بعدها: <span class='ltr'>once, doce, trece</span>", say="Diez", example="Diez, nueve, ocho."),
 dict(tag="الكلمة التالتة", es="Veinte", size=200, pron="بِينْتِي", mean="عشرين (20)", pill="الـ v بتتنطق قريبة من ب",
      note="30 = <span class='ltr'>treinta</span> · 40 = <span class='ltr'>cuarenta</span>", say="Veinte", example="Veinte euros."),
 dict(tag="الكلمة الرابعة", es="Tengo", size=210, pron="تِينْغو", mean="عندي", pill="عمرك: <span class='ltr'>Tengo 25 años</span>",
      note="مش «أنا 25»! بنقول «عندي 25 سنة»", say="Tengo", example="Tengo veinticinco años."),
 ],
 recap=[("5", "Cinco"), ("10", "Diez"), ("20", "Veinte"), ("عندي", "Tengo")],
 q_ar="«عندي 20 سنة» بالإسباني؟", q_right="Tengo veinte años.", q_wrong="Soy veinte años.")

D = dict(file="reel_day03_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="عمرك كام؟",
         cta="جرّب ترد بالإسباني<br>في الكومنتات",
         lines=[
 dict(name="أحمد", side="l", voice="em_alex", es="¿Cuántos años tienes?", ar="عندك كام سنة؟"),
 dict(name="خوليا", side="r", voice="ef_dora", es="Tengo veintiocho años. ¿Y tú?", ar="عندي 28 سنة. وإنت؟"),
 dict(name="أحمد", side="l", voice="em_alex", es="Tengo treinta y dos.", ar="عندي 32."),
 dict(name="خوليا", side="r", voice="ef_dora", es="¿Tienes hermanos?", ar="عندك إخوات؟"),
 dict(name="أحمد", side="l", voice="em_alex", es="Sí, tengo un hermano y dos hermanas.", ar="أيوه، عندي أخ واحد وأختين."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
