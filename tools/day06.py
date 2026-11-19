"""Day 6 reels (directions). Usage: python3 day06.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day06_words", title1="تايه في إسبانيا؟", title2="قول كده!",
         cta="اكتب في الكومنتات:<br><span class='ltr'>¿Dónde está el baño?</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Derecha", size=200, pron="دِيرِيتْشا", mean="يمين", pill="لف يمين: <span class='ltr'>Gire a la derecha</span>",
      note="الـ ch بتتنطق «تش»", say="Derecha", example="Gire a la derecha."),
 dict(tag="الكلمة التانية", es="Izquierda", size=170, pron="إِثْكْيِيرْدا", mean="شمال", pill="الـ z بتتنطق ث (في إسبانيا)",
      note="الـ u صامتة بعد q", say="Izquierda", example="Gire a la izquierda."),
 dict(tag="الكلمة التالتة", es="Todo recto", size=150, pron="تُودو ريكْتو", mean="على طول", pill="امشي على طول",
      note="الرد الأشهر لما تسأل عن الطريق", say="Todo recto", example="Siga todo recto."),
 dict(tag="الكلمة الرابعة", es="Cerca", size=220, pron="ثِيرْكا", mean="قريب", pill="عكسها: <span class='ltr'>lejos</span> = بعيد",
      note="الـ c قبل e = ث", say="Cerca", example="Está cerca."),
 ],
 recap=[("يمين", "Derecha"), ("شمال", "Izquierda"), ("على طول", "Todo recto"), ("قريب", "Cerca")],
 q_ar="«لف يمين» بالإسباني؟", q_right="Gire a la derecha.", q_wrong="Gire a la izquierda.")

D = dict(file="reel_day06_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="فين الصيدلية؟",
         cta="جرّب تسأل عن الطريق<br>بالإسباني في الكومنتات",
         lines=[
 dict(name="السائح", side="l", voice="em_alex", es="Perdone, ¿dónde está la farmacia?", ar="عن إذنك، فين الصيدلية؟"),
 dict(name="السيدة", side="r", voice="ef_dora", es="Está cerca. Siga todo recto y luego gire a la derecha.", ar="قريبة. امشي على طول وبعدين لف يمين."),
 dict(name="السائح", side="l", voice="em_alex", es="¿Está lejos?", ar="بعيدة؟"),
 dict(name="السيدة", side="r", voice="ef_dora", es="No, está a cinco minutos andando.", ar="لأ، على بعد 5 دقايق مشي."),
 dict(name="السائح", side="l", voice="em_alex", es="Muchas gracias.", ar="شكرًا جزيلًا."),
 dict(name="السيدة", side="r", voice="ef_dora", es="De nada.", ar="عفوًا."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
