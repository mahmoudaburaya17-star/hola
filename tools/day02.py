"""Day 2 reels (identity / ser). Usage: python3 day02.py w|d  (run with HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day02_words", title1="عرّف بنفسك", title2="بالإسباني!",
         cta="اكتب جملتك في الكومنتات:<br><span class='ltr'>Soy de ___</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Soy", size=230, pron="سُوي", mean="أنا (أكون)", pill="من الفعل ser (يكون)",
      note="في الإسباني لازم الفعل يتكتب", say="Soy", example="Soy Omar. Soy egipcio."),
 dict(tag="الكلمة التانية", es="Eres", size=210, pron="إِرِس", mean="إنت", pill="للأصحاب (غير رسمي)",
      note="لحضرتك: <span class='ltr'>usted es</span>", say="Eres", example="¿Eres egipcia?"),
 dict(tag="الكلمة التالتة", es="Es", size=230, pron="إِس", mean="هو / هي", pill="للغايب المفرد",
      note="مثال: <span class='ltr'>Ella es médica</span>", say="Es", example="Ella es médica."),
 dict(tag="الكلمة الرابعة", es="Egipto", size=190, pron="إِخِيبْتو", mean="مصر",
      pill="مصري = <span class='ltr'>egipcio</span> · مصرية = <span class='ltr'>egipcia</span>",
      note="الجنسية بتتكتب بحرف صغير", say="Egipto", example="Soy de Egipto."),
 ],
 recap=[("أنا", "Soy"), ("إنت", "Eres"), ("هو / هي", "Es"), ("مصر", "Egipto")],
 q_ar="«هي مغربية» بالإسباني؟", q_right="Ella es marroquí.", q_wrong="Ella son marroquí.")

D = dict(file="reel_day02_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="عرّف بنفسك!",
         cta="جرّب ترد بالإسباني<br>في الكومنتات",
         lines=[
 dict(name="سارة", side="r", voice="ef_dora", es="Hola, ¿cómo te llamas?", ar="مرحبًا، اسمك إيه؟"),
 dict(name="بيدرو", side="l", voice="em_alex", es="Me llamo Pedro. ¿Y tú?", ar="اسمي بيدرو. وإنتِ؟"),
 dict(name="سارة", side="r", voice="ef_dora", es="Soy Sara. Soy egipcia, de Alejandría.", ar="أنا سارة. مصرية، من الإسكندرية."),
 dict(name="بيدرو", side="l", voice="em_alex", es="¡Qué bien! Yo soy de Madrid.", ar="حلو! أنا من مدريد."),
 dict(name="سارة", side="r", voice="ef_dora", es="¿Eres estudiante?", ar="إنت طالب؟"),
 dict(name="بيدرو", side="l", voice="em_alex", es="No, soy ingeniero. ¿Y tú?", ar="لأ، أنا مهندس. وإنتِ؟"),
 dict(name="سارة", side="r", voice="ef_dora", es="Yo soy médica.", ar="أنا دكتورة."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
