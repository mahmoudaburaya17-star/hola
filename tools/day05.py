"""Day 5 reels (restaurant). Usage: python3 day05.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day05_words", title1="اطلب أكلك", title2="بالإسباني!",
         cta="اكتب طلبك في الكومنتات:<br><span class='ltr'>Quisiera ___, por favor</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Quisiera", size=170, pron="كِيسْيِيرا", mean="كنت أود", pill="أدب أكتر من <span class='ltr'>Quiero</span>",
      note="بنقولها قبل أي طلب", say="Quisiera", example="Quisiera una ensalada, por favor."),
 dict(tag="الكلمة التانية", es="Agua", size=230, pron="أَغْوا", mean="ماء", pill="<span class='ltr'>el agua</span> — مذكر في الجمل",
      note="بدون غاز: <span class='ltr'>sin gas</span>", say="Agua", example="Agua sin gas, por favor."),
 dict(tag="الكلمة التالتة", es="Pollo", size=220, pron="بُويو", mean="فراخ", pill="الـ ll بتتنطق قريبة من «يـ»",
      note="للحلال اسأل: <span class='ltr'>¿Lleva cerdo?</span>", say="Pollo", example="Quisiera pollo, por favor."),
 dict(tag="الكلمة الرابعة", es="La cuenta", size=150, pron="لا كُوِينْتا", mean="الحساب", pill="في آخر الأكل",
      note="ومعاها دايمًا <span class='ltr'>por favor</span>", say="La cuenta", example="La cuenta, por favor."),
 ],
 recap=[("كنت أود", "Quisiera"), ("ماء", "Agua"), ("فراخ", "Pollo"), ("الحساب", "La cuenta")],
 q_ar="«الحساب لو سمحت» بالإسباني؟", q_right="La cuenta, por favor.", q_wrong="La cuento, por favor.")

D = dict(file="reel_day05_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="في المطعم!",
         cta="جرّب تطلب أكلك<br>بالإسباني في الكومنتات",
         lines=[
 dict(name="الجرسون", side="l", voice="em_alex", es="Buenas tardes. ¿Qué quieren tomar?", ar="مساء الخير. تحبوا تطلبوا إيه؟"),
 dict(name="سلمى", side="r", voice="ef_dora", es="Quisiera una ensalada y pollo, por favor.", ar="كنت أود سلطة وفراخ، لو سمحت."),
 dict(name="الجرسون", side="l", voice="em_alex", es="¿Y para beber?", ar="وللشرب؟"),
 dict(name="سلمى", side="r", voice="ef_dora", es="Agua sin gas, por favor. ¿Lleva cerdo la ensalada?", ar="ماء بدون غاز. السلطة فيها خنزير؟"),
 dict(name="الجرسون", side="l", voice="em_alex", es="No, no lleva cerdo.", ar="لأ، مفيهاش خنزير."),
 dict(name="سلمى", side="r", voice="ef_dora", es="Perfecto. La cuenta, por favor.", ar="تمام. الحساب لو سمحت."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
