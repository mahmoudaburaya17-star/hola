"""Day 9 reels (house). Usage: python3 day09.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day09_words", title1="تعالى أوريك", title2="بيتي بالإسباني! 🏠",
         cta="اكتب في الكومنتات:<br><span class='ltr'>Mi casa tiene ___ habitaciones</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Casa", size=250, pron="كَاسا", mean="بيت", pill="<span class='ltr'>la casa</span> = البيت",
      note="الـ c قبل a = ك", say="Casa", example="Bienvenido a mi casa."),
 dict(tag="الكلمة التانية", es="Cocina", size=210, pron="كُوثِينا", mean="مطبخ", pill="الـ c قبل i = ث",
      note="في إسبانيا: ث", say="Cocina", example="La cocina está allí."),
 dict(tag="الكلمة التالتة", es="Baño", size=250, pron="بَانْيو", mean="حمام", pill="الـ ñ = «ني»",
      note="el baño (مذكر)", say="Baño", example="¿Dónde está el baño?"),
 dict(tag="الكلمة الرابعة", es="Dormitorio", size=150, pron="دُورْمِيتُورْيو", mean="أوضة نوم", pill="من <span class='ltr'>dormir</span> = ينام",
      note="الجمع: dormitorios", say="Dormitorio", example="Tiene tres dormitorios."),
 ],
 recap=[("بيت", "Casa"), ("مطبخ", "Cocina"), ("حمام", "Baño"), ("أوضة نوم", "Dormitorio")],
 q_ar="«مطبخ» بالإسباني؟", q_right="Cocina.", q_wrong="Baño.")

D = dict(file="reel_day09_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="سارة وبابلو 🏠",
         cta="وصّف بيتك<br>بالإسباني في الكومنتات",
         lines=[
 dict(name="سارة", side="l", voice="ef_dora", es="¡Bienvenido a mi casa!", ar="أهلاً بيك في بيتي!"),
 dict(name="بابلو", side="r", voice="em_alex", es="¡Qué bonita! ¿Cuántas habitaciones tiene?", ar="إيه الجمال! كام غرفة فيه؟"),
 dict(name="سارة", side="l", voice="ef_dora", es="Tiene tres dormitorios, una cocina y dos baños.", ar="فيه 3 غرف نوم ومطبخ وحمامين."),
 dict(name="بابلو", side="r", voice="em_alex", es="¿Dónde está la cocina?", ar="فين المطبخ؟"),
 dict(name="سارة", side="l", voice="ef_dora", es="Está al final del pasillo.", ar="في آخر الممر."),
 dict(name="بابلو", side="r", voice="em_alex", es="Me encanta tu casa.", ar="بيتك عجبني أوي."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
