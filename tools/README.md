# أدوات إنتاج الريلز والصور

سكربتات بتولّد ريلز (1080×1920) وصور (1080×1080) لقناة أهلاً Hola بنفس التصميم.

## التجهيز (مرة واحدة)

مجلد شغل واحد، وليكن `$HOLA_WORK`، فيه:

- `reel/` : انسخ فيه محتويات المجلد ده (`reels.py` و`images.py` و`day01.py` و`base.css`).
- `fontpkg/` : `npm install @fontsource/cairo @fontsource/tajawal` (خطوط عربية).
- `tts/` : نموذج Kokoro (`kokoro.int8.onnx` و`voices.bin`) من إصدار `model-files-v1.0` في مستودع kokoro-onnx، و`pip install kokoro-onnx soundfile`.

المطلوب كمان: Google Chrome على `/usr/bin/google-chrome`، وPlaywright لبايثون، وffmpeg، وPillow.

## الاستخدام

```
export HOLA_WORK=/path/to/work
cd $HOLA_WORK/reel
python3 day01.py w   # ريل النطق
python3 day01.py d   # ريل المحادثة
python3 images.py    # صور الكاروسيل وكلمات اليوم
```

كل يوم جديد = ملف مثل `day01.py` بمحتوى اليوم (قاموس الكلمات وسطور المحادثة).

## ملاحظات

- الصوت آلي (Kokoro) مش تسجيل بشري. يتراجع بنفسك قبل النشر.
- اسم القناة بيظهر في كل مشاهد الريل عن طريق `.wm` في `base.css`.
- مسارات `images.py` و`day01.py` تفترض مجلد `reel/` تحت `$HOLA_WORK`.
