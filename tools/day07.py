"""Day 7 reels (Arabic loanwords). Usage: python3 day07.py w|d OUTBASE  (HOLA_WORK set)."""
import sys
import reels

W = dict(file="reel_day07_words", title1="كلمات إسبانية", title2="أصلها عربي! 🌍",
         cta="اكتب في الكومنتات:<br><span class='ltr'>¡Ojalá!</span>",
         words=[
 dict(tag="الكلمة الأولى", es="Azúcar", size=210, pron="أَثُوكار", mean="سكر", pill="من العربية: السُّكَّر",
      note="الـ z = ث في إسبانيا", say="Azúcar", example="Quiero azúcar."),
 dict(tag="الكلمة التانية", es="Aceite", size=210, pron="أَثِيْتِي", mean="زيت", pill="من العربية: الزيت",
      note="الـ c قبل e = ث", say="Aceite", example="Aceite de oliva."),
 dict(tag="الكلمة التالتة", es="Almohada", size=170, pron="أَلْمُوَادا", mean="مخدة", pill="من العربية: المِخَدّة",
      note="الـ h صامتة", say="Almohada", example="Una almohada blanda."),
 dict(tag="الكلمة الرابعة", es="Ojalá", size=230, pron="أُوخَالا", mean="إن شاء الله", pill="من العربية: إن شاء الله",
      note="الـ j = خ", say="Ojalá", example="Ojalá nos veamos mañana."),
 ],
 recap=[("سكر", "Azúcar"), ("زيت", "Aceite"), ("مخدة", "Almohada"), ("إن شاء الله", "Ojalá")],
 q_ar="«إن شاء الله» بالإسباني؟", q_right="Ojalá.", q_wrong="Adiós.")

D = dict(file="reel_day07_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="كريم ومارتا 🍵",
         cta="جرّب ترد بالإسباني<br>في الكومنتات",
         lines=[
 dict(name="كريم", side="l", voice="em_alex", es="¿Quieres té?", ar="تحبي شاي؟"),
 dict(name="مارتا", side="r", voice="ef_dora", es="Sí, por favor. Con azúcar.", ar="أيوه، لو سمحت. بسكر."),
 dict(name="كريم", side="l", voice="em_alex", es="Aquí tienes. ¿Quieres también aceitunas?", ar="اتفضلي. وتحبي زيتون كمان؟"),
 dict(name="مارتا", side="r", voice="ef_dora", es="¡Sí! Me gustan mucho.", ar="أيوه! بحبه أوي."),
 dict(name="كريم", side="l", voice="em_alex", es="Ojalá nos veamos mañana.", ar="إن شاء الله نتقابل بكرة."),
 dict(name="مارتا", side="r", voice="ef_dora", es="¡Ojalá! Hasta mañana.", ar="إن شاء الله! أشوفك بكرة."),
 ])

if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    if sys.argv[1] == "w":
        print(reels.word_reel(W, f"{out}/words"))
    else:
        print(reels.dialog_reel(D, f"{out}/dialog"))
