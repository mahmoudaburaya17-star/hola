"""Day 4 reels (daily-life verbs). Usage: python3 day04.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day04_words", title1="احكي يومك", title2="بالإسباني!",
         cta="اكتب في الكومنتات:<br><span class='ltr'>Yo ___ español</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Trabajo", size=190, pron="تْرَبَاخو", mean="أنا بشتغل", pill="من الفعل trabajar (يشتغل)",
      note="مع «أنا» الفعل بينتهي بحرف <span class='ltr'>o</span>", say="Trabajo", example="Trabajo en una escuela."),
 dict(tag="الكلمة التانية", es="Estudio", size=190, pron="إِسْتُودْيو", mean="أنا بذاكر", pill="من الفعل estudiar (يذاكر)",
      note="زي الأولى: حرف <span class='ltr'>o</span> في الآخر", say="Estudio", example="Estudio español."),
 dict(tag="الكلمة التالتة", es="Hablo", size=210, pron="أَبْلو", mean="أنا بتكلم", pill="الـ h صامتة زي ما اتعلمنا",
      note="إنت بتتكلم = <span class='ltr'>hablas</span>", say="Hablo", example="Hablo árabe e inglés."),
 dict(tag="الكلمة الرابعة", es="Como", size=230, pron="كُومو", mean="أنا باكل", pill="من الفعل comer (ياكل)",
      note="إحنا بناكل = <span class='ltr'>comemos</span>", say="Como", example="Como arroz todos los días."),
 ],
 recap=[("أنا بشتغل", "Trabajo"), ("أنا بذاكر", "Estudio"), ("أنا بتكلم", "Hablo"), ("أنا باكل", "Como")],
 q_ar="«أنا بتكلم إسباني» بالإسباني؟", q_right="Hablo español.", q_wrong="Hablas español.")

D = dict(file="reel_day04_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="ساكن فين؟",
         cta="جرّب ترد بالإسباني<br>في الكومنتات",
         lines=[
 dict(name="نورا", side="r", voice="ef_dora", es="¿Dónde vives?", ar="ساكن فين؟"),
 dict(name="لويس", side="l", voice="em_alex", es="Vivo en Sevilla. ¿Y tú?", ar="ساكن في إشبيلية. وإنتِ؟"),
 dict(name="نورا", side="r", voice="ef_dora", es="Vivo en El Cairo. Trabajo en una escuela.", ar="ساكنة في القاهرة. وبشتغل في مدرسة."),
 dict(name="لويس", side="l", voice="em_alex", es="¿Qué idiomas hablas?", ar="بتتكلمي لغات إيه؟"),
 dict(name="نورا", side="r", voice="ef_dora", es="Hablo árabe e inglés. Estudio español.", ar="بتكلم عربي وإنجليزي. وبذاكر إسباني."),
 dict(name="لويس", side="l", voice="em_alex", es="¡Muy bien!", ar="كويس جدًا!"),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
