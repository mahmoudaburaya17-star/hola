import reels
W = dict(file="reel_day01_words", title1="تحيات إسباني", title2="لازم تعرفها!", cta="تفتكر تحية تانية؟<br>اكتبها في الكومنتات",
 words=[
 dict(tag="الكلمة الأولى", es="Hola", size=230, pron="أُولا", mean="مرحبًا", pill="حرف H صامت — مبيتنطقش", note="يعني مش «هولا»", say="Hola", example="¡Hola! Me llamo Sara."),
 dict(tag="الكلمة التانية", es="Buenos días", size=150, pron="بُويْنُس دِيَاس", mean="صباح الخير", pill="بنقولها لحد الظهر", note="وبعد الظهر: <span class='ltr'>Buenas tardes</span>", say="Buenos días", example="Buenos días. ¿Cómo estás?"),
 dict(tag="الكلمة التالتة", es="¿Cómo estás?", size=128, pron="كُومو إِسْتَاس", mean="إزيك؟", pill="علامة <span class='ltr'>¿</span> بتبدأ مقلوبة", note="الرد: <span class='ltr'>Bien, gracias</span>", say="¿Cómo estás?", example="Bien, gracias. ¿Y tú?"),
 dict(tag="الكلمة الرابعة", es="Gracias", size=190, pron="غْرَاثْيَاس", mean="شكرًا", pill="حرف C قبل I = ث (في إسبانيا)", note="وفي أمريكا اللاتينية بتتنطق س", say="Gracias", example="Muchas gracias."),
 ],
 recap=[("مرحبًا","Hola"),("صباح الخير","Buenos días"),("إزيك؟","¿Cómo estás?"),("شكرًا","Gracias")],
 q_ar="«صباح الخير» بالإسباني؟", q_right="Buenos días", q_wrong="Buenas noches")
D = dict(file="reel_day01_dialogo", tag="محادثة اليوم", title1="محادثة اليوم", title2="سلّم بالإسباني!", cta="جرّب ترد بالإسباني<br>في الكومنتات",
 lines=[
 dict(name="ليلى", side="r", voice="ef_dora", es="¡Hola! Buenos días.", ar="مرحبًا! صباح الخير."),
 dict(name="كارلوس", side="l", voice="em_alex", es="¡Buenos días! ¿Cómo estás?", ar="صباح الخير! إزيك؟"),
 dict(name="ليلى", side="r", voice="ef_dora", es="Bien, gracias. ¿Y tú?", ar="كويسة، شكرًا. وإنت؟"),
 dict(name="كارلوس", side="l", voice="em_alex", es="Muy bien. Me llamo Carlos.", ar="كويس جدًا. اسمي كارلوس."),
 dict(name="ليلى", side="r", voice="ef_dora", es="Me llamo Laila. Mucho gusto.", ar="اسمي ليلى. اتشرفنا."),
 dict(name="كارلوس", side="l", voice="em_alex", es="Encantado.", ar="اتشرفت."),
 ])
if __name__=="__main__":
    import sys
    which = sys.argv[1]
    if which=="w": print(reels.word_reel(W, "out_words"))
    else: print(reels.dialog_reel(D, "out_dialog"))
