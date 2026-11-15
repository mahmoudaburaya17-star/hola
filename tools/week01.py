"""Images for week 1 text posts. Usage: python3 week01.py OUTDIR [day ...]

Writes OUTDIR/day-NN/{lesson-N,carousel-N,words,quiz}.png (1080x1080).
Day 1's lesson/carousel/words already exist in media/day-01; only its quiz is generated here.
"""
import sys
from postimg import cover, rows, cards, word, pair, quiz, render

L = "<span class='ltr'>{}</span>"
def lt(x): return L.format(x)

DAYS = {}

# ---------------- day 1
DAYS[1] = {"quiz": quiz(f"إزاي تقول «صباح الخير» بالإسباني؟",
                        [("A", "Buenas noches"), ("B", "Buenos días"), ("C", "Adiós")])}

# ---------------- day 2
DAYS[2] = {
 "lesson-1": cover("إزاي تقول", "أنا مصري", "بالإسباني؟", "Soy egipcio"),
 "lesson-2": cards("لو راجل ولا ست", [("Soy egipcio.", "أنا مصري (راجل)"), ("Soy egipcia.", "أنا مصرية (ست)")],
                   f"الفعل {lt('soy')} من {lt('ser')} (يكون). في العربي بنحذفه، لكن في الإسباني لازم يتكتب"),
 "lesson-3": rows("الفعل ser", [("أنا", "yo soy"), ("إنت", "tú eres"), ("هو / هي", "él / ella es"),
                                ("إحنا", "nosotros somos"), ("هم", "ellos son")]),
 "lesson-4": cards("أمثلة", [("Soy estudiante.", "أنا طالب"), ("Ella es médica.", "هي دكتورة"),
                             ("Somos amigos.", "إحنا أصحاب")],
                   f"الجنسية بحرف صغير: {lt('egipcio')} مش {lt('Egipcio')}<br>اكتب: {lt('Soy de ___')}"),
 "carousel-1": cover("جنسيات", "عربية", "بالإسباني", "اسحب ←"),
 "carousel-2": pair("مصر", "Egipto", "egipcio / egipcia", "مصري / مصرية"),
 "carousel-3": pair("المغرب", "Marruecos", "marroquí", "مغربي / مغربية"),
 "carousel-4": pair("لبنان", "Líbano", "libanés / libanesa", "لبناني / لبنانية"),
 "carousel-5": pair("الأردن", "Jordania", "jordano / jordana", "أردني / أردنية"),
 "carousel-6": cover("قول جنسيتك", "في الكومنتات", "", "Soy ___"),
 "words": rows("كلمات اليوم", [("أنا (أكون)", "Soy"), ("إنت", "Eres"), ("هو / هي", "Es"),
                               ("مصر", "Egipto"), ("طالب / ة", "Estudiante"), ("طبيب / ة", "Médico/a")]),
 "quiz": quiz(f"أكمل: {lt('Ella ___ marroquí.')}", [("A", "soy"), ("B", "es"), ("C", "son")]),
}

# ---------------- day 3
DAYS[3] = {
 "lesson-1": cover("عُدّ من 1", "لـ 10", "بالإسباني", "Los números"),
 "lesson-2": rows("من 1 لـ 5", [("1", "uno"), ("2", "dos"), ("3", "tres"), ("4", "cuatro"), ("5", "cinco")]),
 "lesson-3": rows("من 6 لـ 10", [("6", "seis"), ("7", "siete"), ("8", "ocho"), ("9", "nueve"), ("10", "diez")]),
 "lesson-4": cards("العمر والأرقام", [("treinta y ocho", "38 = ثلاثين وثمانية (مش ثمانية وثلاثين)"),
                                      ("Tengo 25 años.", "عندي 25 سنة (مش «أنا 25»)"),
                                      ("¿Cuántos años tienes?", "عندك كام سنة؟")]),
 "carousel-1": cover("الأرقام", "من 1 لـ 10", "", "اسحب ←"),
 "carousel-2": rows("1 إلى 3", [("1", "uno"), ("2", "dos"), ("3", "tres")]),
 "carousel-3": rows("4 إلى 6", [("4", "cuatro"), ("5", "cinco"), ("6", "seis")]),
 "carousel-4": rows("7 إلى 10", [("7", "siete"), ("8", "ocho"), ("9", "nueve"), ("10", "diez")]),
 "carousel-5": rows("العشرات", [("20", "veinte"), ("30", "treinta"), ("40", "cuarenta")]),
 "carousel-6": cover("قول عمرك", "في الكومنتات", "", "Tengo ___ años"),
 "words": rows("كلمات اليوم", [("صفر", "Cero"), ("10", "Diez"), ("20", "Veinte"), ("50", "Cincuenta"),
                               ("100", "Cien"), ("عندي", "Tengo"), ("سنين", "Años")]),
 "quiz": quiz("إزاي تقول 45؟", [("A", "cuarenta y cinco"), ("B", "cincuenta y cuatro"), ("C", "cuatro y cincuenta")]),
}

# ---------------- day 4
DAYS[4] = {
 "lesson-1": cover("الأفعال في الإسباني", "زي العربي", "بالظبط!", "-ar · -er · -ir"),
 "lesson-2": rows("hablar = يتكلم", [("أنا بتكلم", "yo hablo"), ("إنت بتتكلم", "tú hablas"), ("هو بيتكلم", "él habla"),
                                      ("إحنا بنتكلم", "nosotros hablamos"), ("هم بيتكلموا", "ellos hablan")]),
 "lesson-3": cards("الأفعال التلاتة", [("hablar → hablo", f"يتكلم {lt('(-ar)')}"), ("comer → como", f"يأكل {lt('(-er)')}"),
                                       ("vivir → vivo", f"يعيش {lt('(-ir)')}")],
                   f"شيل النهاية {lt('-ar / -er / -ir')} وحط نهاية الضمير"),
 "lesson-4": cards("أمثلة", [("Trabajo en una escuela.", "أنا بشتغل في مدرسة"), ("Vivo en El Cairo.", "أنا ساكن في القاهرة"),
                             ("No hablo francés.", "أنا مبتكلمش فرنساوي")],
                   "الضمير ممكن يتحذف لأن الفعل بيدل عليه"),
 "carousel-1": cover("5 أفعال", "لازم تعرفها", "", "اسحب ←"),
 "carousel-2": pair("فعل 1", "trabajar", "trabajo", "يشتغل"),
 "carousel-3": pair("فعل 2", "estudiar", "estudio", "يذاكر"),
 "carousel-4": pair("فعل 3", "hablar", "hablo", "يتكلم"),
 "carousel-5": rows("فعلين", [("يأكل", "comer"), ("يشرب", "beber")]),
 "carousel-6": cover("جرّب", "في الكومنتات", "", "Yo ___ español"),
 "words": rows("كلمات اليوم", [("يشتغل", "Trabajar"), ("يذاكر", "Estudiar"), ("يعيش", "Vivir"), ("يقرأ", "Leer"),
                               ("يكتب", "Escribir"), ("كل يوم", "Todos los días")]),
 "quiz": quiz(f"أكمل: {lt('Nosotros (comer) ___ arroz.')}", [("A", "como"), ("B", "comemos"), ("C", "comen")]),
}

# ---------------- day 5
DAYS[5] = {
 "lesson-1": cover("اطلب أكلك", "بأدب", "في المطعم", "En el restaurante"),
 "lesson-2": cards("إزاي تطلب؟", [("Quiero un café.", "عايز قهوة (مباشرة شوية)", "bad"),
                                  ("Quisiera un café, por favor.", "لو سمحت، كنت أود قهوة (بأدب)", "good")]),
 "lesson-3": cards("gustar", [("Me gusta el té.", "الشاي بيعجبني"), ("Me gustan las frutas.", "الفواكه بتعجبني")],
                   f"الشيء هو الفاعل: مفرد {lt('gusta')} / جمع {lt('gustan')}"),
 "lesson-4": cards("لو بتاكل حلال", [("¿Lleva cerdo o alcohol?", "فيه لحم خنزير أو كحول؟"),
                                     ("No como cerdo.", "أنا مبآكلش لحم خنزير")],
                   "اسأل دايمًا، الحلال مش متوفر في كل مطعم"),
 "carousel-1": cover("مفردات", "المطعم", "", "اسحب ←"),
 "carousel-2": rows("أكل 1", [("ماء", "el agua"), ("عيش", "el pan"), ("أرز", "el arroz")]),
 "carousel-3": rows("أكل 2", [("فراخ", "el pollo"), ("لحمة", "la carne"), ("سمك", "el pescado")]),
 "carousel-4": rows("شرب", [("شاي", "el té"), ("قهوة", "el café"), ("لبن", "la leche")]),
 "carousel-5": rows("أكل 3", [("سلطة", "la ensalada"), ("شوربة", "la sopa"), ("جبنة", "el queso")]),
 "carousel-6": cover("اطلب أكلك", "في الكومنتات", "", "Quisiera ___, por favor"),
 "words": rows("كلمات اليوم", [("ماء", "Agua"), ("عيش", "Pan"), ("أرز", "Arroz"), ("فراخ", "Pollo"),
                               ("شاي", "Té"), ("قهوة", "Café"), ("الحساب", "La cuenta")]),
 "quiz": quiz(f"أكمل: {lt('Me ___ las naranjas.')}", [("A", "gusta"), ("B", "gustan"), ("C", "gusto")]),
}

# ---------------- day 6
DAYS[6] = {
 "lesson-1": cover("تايه؟", "اسأل", "عن الطريق", "Direcciones"),
 "lesson-2": cards("اسأل وافهم الرد", [("Perdone, ¿dónde está la farmacia?", "عن إذنك، فين الصيدلية؟"),
                                       ("Está cerca. Siga todo recto y gire a la derecha.", "قريبة. امشي على طول ولف يمين")]),
 "lesson-3": rows("اتجاهات", [("يمين", "a la derecha"), ("شمال", "a la izquierda"), ("على طول", "todo recto"),
                              ("قريب", "cerca"), ("بعيد", "lejos")]),
 "lesson-4": cards("está ولا hay؟", [("El hotel está aquí.", "الفندق هنا (محدد ← está)"),
                                     ("Hay una farmacia cerca.", "فيه صيدلية قريبة (غير محدد ← hay)")]),
 "carousel-1": cover("أماكن", "لازم تسأل عنها", "", "اسحب ←"),
 "carousel-2": rows("أماكن 1", [("المطار", "el aeropuerto"), ("المحطة", "la estación")]),
 "carousel-3": rows("أماكن 2", [("الفندق", "el hotel"), ("البنك", "el banco")]),
 "carousel-4": rows("أماكن 3", [("الصيدلية", "la farmacia"), ("المستشفى", "el hospital")]),
 "carousel-5": rows("أماكن 4", [("المسجد", "la mezquita"), ("الحمام", "el baño")]),
 "carousel-6": cover("اسأل", "في الكومنتات", "", "¿Dónde está ___?"),
 "words": rows("كلمات اليوم", [("يمين", "Derecha"), ("شمال", "Izquierda"), ("على طول", "Todo recto"),
                               ("قريب", "Cerca"), ("بعيد", "Lejos"), ("فين…؟", "¿Dónde está…?")]),
 "quiz": quiz(f"أكمل: {lt('___ una farmacia cerca.')}", [("A", "Está"), ("B", "Hay"), ("C", "Es")]),
}

# ---------------- day 7
DAYS[7] = {
 "lesson-1": cover("كلمات إسباني", "أصلها عربي", "", "بسبب الأندلس"),
 "lesson-2": rows("من العربي للإسباني", [("السُّكَّر", "azúcar"), ("الزيت", "aceite"), ("الزيتونة", "aceituna"),
                                         ("الرُّز", "arroz")]),
 "lesson-3": rows("كمان", [("المِخَدّة", "almohada"), ("القطن", "algodón"), ("ياسمين", "jazmín")]),
 "lesson-4": cards("نصيحة", [("al- = ال", "almohada · algodón · almacén · alcázar"),
                             ("Ojalá", "إن شاء الله / يا ريت")],
                   f"للتأكد من أصل أي كلمة ابحث عنها في DLE على {lt('rae.es')}"),
 "carousel-1": cover("كلمات إسبانية", "أصلها عربي", "", "اسحب ←"),
 "carousel-2": pair("1", "azúcar", "السُّكَّر", "سكر"),
 "carousel-3": rows("2", [("زيت", "aceite"), ("زيتونة", "aceituna")]),
 "carousel-4": pair("3", "almohada", "المِخَدّة", "مخدة"),
 "carousel-5": pair("4", "algodón", "القطن", "قطن"),
 "carousel-6": cover("ojalá", "= إن شاء الله", "", "احفظها!"),
 "words": rows("مراجعة الأسبوع", [("مرحبًا", "Hola"), ("أنا", "Soy"), ("عندي", "Tengo"), ("بشتغل", "Trabajo"),
                                  ("كنت أود", "Quisiera"), ("فين…؟", "¿Dónde está…?"), ("إن شاء الله", "Ojalá")]),
 "quiz": quiz(f"كلمة {lt('ojalá')} معناها إيه؟", [("A", "شكرًا"), ("B", "إن شاء الله / يا ريت"), ("C", "مع السلامة")],
              "اكتب الحرف في الكومنتات | الإجابة بكرة الصبح"),
}

if __name__ == "__main__":
    out = sys.argv[1]
    days = [int(x) for x in sys.argv[2:]] or sorted(DAYS)
    for d in days:
        render(DAYS[d], f"{out}/day-{d:02d}")
        print("day", d, len(DAYS[d]), "images")
