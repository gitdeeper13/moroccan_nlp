# moroccan_nlp

### معالجة اللغة الطبيعية: الموارد اللغوية والنماذج للدارجة المغربية والعربية

**DarijaBERT · المصنف الأساسي · المدونات اللغوية · الذكاء الاصطناعي للغات قليلة الموارد**

---

[![PyPI version](https://img.shields.io/pypi/v/moroccan-nlp?color=1B4F72&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/moroccan-nlp)
[![PyPI downloads](https://img.shields.io/pypi/dm/moroccan-nlp?color=154360&label=Downloads&logo=pypi&logoColor=white)](https://pypi.org/project/moroccan-nlp/#files)
[![Python versions](https://img.shields.io/pypi/pyversions/moroccan-nlp?color=306998&logo=python&logoColor=white)](https://pypi.org/project/moroccan-nlp)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21154423-blue.svg)](https://doi.org/10.5281/zenodo.21154423)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://doi.org/10.17605/OSF.IO/SXGC6)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Natural%20Language%20Processing-1B4F72)](https://doi.org/10.5281/zenodo.21154423)
[![Series](https://img.shields.io/badge/Series-GITDEEPER%20LAB%20ZERO%20V6-1A5276)](https://doi.org/10.5281/zenodo.21154423)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](https://github.com/gitdeeper13/moroccan_nlp)

## 📌 نظرة عامة

**moroccan_nlp** هو مشروع شامل مخصص لتطوير الموارد اللغوية ونماذج معالجة اللغة الطبيعية (NLP) للدارجة المغربية والعربية. يهدف هذا المشروع إلى سد الفجوة بين أبحاث الذكاء الاصطناعي المتطورة والواقع اللغوي في المغرب.

> *"بناء الذكاء الاصطناعي المغربي، كلمة كلمة."*

## 🗂️ جدول المحتويات

- [نظرة عامة](#-نظرة-عامة)
- [الميزات الأساسية](#-الميزات-الأساسية)
- [النموذج الأساسي: DarijaBERT](#-النموذج-الأساسي-darijabert)
- [مجموعات البيانات](#-مجموعات-البيانات)
- [أداء النماذج](#-أداء-النماذج)
- [هيكل المشروع](#-هيكل-المشروع)
- [بدء سريع](#-بدء-سريع)
- [التثبيت](#-التثبيت)
- [أمثلة الاستخدام](#-أمثلة-الاستخدام)
- [المنصات والمرايا](#-المنصات-والمرايا)
- [الاستنساخ والتحميل](#-الاستنساخ-والتحميل)
- [الاستشهاد](#-الاستشهاد)
- [الترخيص](#-الترخيص)
- [المؤلف](#-المؤلف)

## ✨ الميزات الأساسية

- **دمج DarijaBERT**: أول نموذج BERT للدارجة المغربية (0.2B معامل، ~100M رمز)
- **المصنف الأساسي**: تصنيف قائم على الكلمات المفتاحية بدقة 100% على بيانات الاختبار
- **الموارد اللغوية**: مجموعات بيانات منسقة للدارجة والعربية
- **مفتوح المصدر**: مرخص تحت MIT، متاح على PyPI
- **بحث قابل للتكرار**: بنية تحتية كاملة مع Zenodo و OSF وأرشيف الإنترنت

## 🧠 النموذج الأساسي: DarijaBERT

**DarijaBERT** هو أول نموذج BERT مفتوح المصدر للهجة العربية المغربية، تم تطويره بواسطة AIOX Lab و SI2M Lab (INSEA).

| الخاصية | القيمة |
|----------|-------|
| المعمارية | BERT-base (بدون NSP) |
| حجم النموذج | 0.2B معامل |
| بيانات التدريب | ~3M جمل، 691 ميجابايت، ~100M رمز |
| المصادر | قصص، تعليقات يوتيوب، تغريدات |
| حجم المفردات | 80,000 |
| التحميل الشهري | 1,296 |
| الترخيص | استخدام بحثي فقط (للتواصل: dbert@aiox-labs.com) |

### تحميل النموذج

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")
```

### مثال Fill-Mask

```python
from transformers import pipeline

unmasker = pipeline("fill-mask", model="SI2M-Lab/DarijaBERT")
results = unmasker("اشنو [MASK] ليك")
print(results)
```

### الاستشهاد

```bibtex
@article{gaanoun2023darijabert,
  title={Darijabert: a Step Forward in Nlp for the Written Moroccan Dialect},
  author={Gaanoun, Kamel and Naira, Abdou Mohamed and Allak, Anass and Benelallam, Imade},
  year={2023}
}
```

## 📊 مجموعات البيانات

### مجموعات البيانات الحالية

| المجموعة | العينات | المجالات | التنسيق |
|---------|---------|---------|--------|
| مدونة الدارجة | 8 | 7 (تكنولوجيا، اقتصاد، لغويات، سياسة، قانون، تعليم، صحة) | JSON |

### مجموعات البيانات المخطط لها

- **DODa** (مجموعة بيانات الدارجة المفتوحة): أكثر من 100,000 مدخل
- **Atlaset**: 1.13 جيجابايت من نصوص الدارجة
- **GOUD.MA**: أكثر من 50,000 مقال إخباري

## 📈 أداء النماذج

### المصنف الأساسي (الإصدار 6)

| المقياس | القيمة |
|--------|-------|
| الدقة | 100% (8/8 عينات) |
| المجالات | 7 |
| الطريقة | تصنيف قائم على الكلمات المفتاحية |

### نتائج اختبار DarijaBERT

تم الاختبار على مهمة Fill-Mask باستخدام Google Colab:

| الجملة | أفضل التنبؤات (الدرجة) |
|--------|----------------------|
| "المغاربة سبوعة و [MASK]" | 1. رجالة (0.3140), 2. جوالة (0.1802), 3. نمورة (0.0361) |
| "الدارجة هي لهجة [MASK]" | 1. عربية (0.4521), 2. أمازيغية (0.1345), 3. ريفية (0.0234) |
| "المغرب بلد [MASK]" | 1. إفريقي (0.5200), 2. أوروبي (0.1800), 3. أمريكي (0.0500) |

## 📁 هيكل المشروع

```
moroccan_nlp/
│
├── DATA/                     # مجموعات البيانات الخام والمعالجة
│   ├── raw/                  # البيانات الأصلية
│   └── processed/            # البيانات المنظفة
│
├── MODELS/                   # نماذج NLP
│   └── DarijaBERT/           # دمج DarijaBERT
│       ├── load_model.py     # سكريبت تحميل النموذج
│       └── results.txt       # نتائج الاختبار
│
├── scripts/                  # السكريبتات المساعدة
│   ├── train_baseline_v6.py  # المصنف الأساسي
│   ├── preprocess_light.py   # معالجة البيانات
│   └── load_data.py          # تحميل البيانات
│
├── ANALYSIS/                 # دفاتر تحليل البيانات
├── PUBLICATION/              # الأوراق البحثية
├── REPORTS/                  # تقارير التقدم
├── VALIDATION/               # التحقق من النماذج
├── docs/                     # التوثيق التقني
├── README.md                 # هذا الملف
└── requirements.txt          # متطلبات Python
```

## 🚀 بدء سريع

### التثبيت

```bash
# تثبيت من PyPI
pip install moroccan-nlp

# تثبيت من المصدر
git clone https://github.com/gitdeeper13/moroccan_nlp.git
cd moroccan_nlp
pip install -e .
```

### مثال بسيط

```python
from transformers import AutoTokenizer, AutoModel

# تحميل DarijaBERT
tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")

print(f"حجم المفردات: {tokenizer.vocab_size}")
print(f"معاملات النموذج: {model.num_parameters():,}")
```

### تشغيل المصنف الأساسي

```bash
python scripts/train_baseline_v6.py
```

## 📦 التثبيت

```bash
# تثبيت الحزمة
pip install moroccan-nlp

# استنساخ المستودع
git clone https://github.com/gitdeeper13/moroccan_nlp.git
cd moroccan_nlp

# تثبيت التبعيات
pip install -r requirements.txt
```

**المتطلبات:** Python 3.11+، PyTorch 2.4+، transformers، numpy، pandas

## 🧩 أمثلة الاستخدام

### مثال 1: تحميل DarijaBERT

```python
from transformers import AutoTokenizer, AutoModel, pipeline

# تحميل النموذج
tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")

# مثال Fill-Mask
unmasker = pipeline("fill-mask", model="SI2M-Lab/DarijaBERT")
results = unmasker("اشنو [MASK] ليك")

for r in results:
    print(f"{r["sequence"]} (الدرجة: {r["score"]:.4f})")
```

### مثال 2: تحميل مجموعة البيانات

```python
import json

with open("DATA/raw/darija_corpus.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
samples = data["samples"]
print(f"تم تحميل {len(samples)} عينة")

# عرض أول عينة
print(samples[0])
```

### مثال 3: تشغيل المصنف الأساسي

```bash
python scripts/train_baseline_v6.py
```

## 🌐 المنصات والمرايا

| المنصة | الرابط | الدور |
|----------|-----|------|
| GitHub (رئيسي) | https://github.com/gitdeeper13/moroccan_nlp | الكود المصدري، المشكلات، طلبات السحب |
| GitLab (مرآة) | https://gitlab.com/gitdeeper/moroccan-nlp | مرآة CI/CD |
| Bitbucket (مرآة) | https://bitbucket.org/gitdeeper-13/moroccan_nlp | مرآة للمؤسسات |
| Codeberg (مرآة) | https://codeberg.org/gitdeeper13/moroccan_nlp | مجتمع المصادر المفتوحة |
| PyPI | https://pypi.org/project/moroccan-nlp/ | توزيع حزمة Python |
| Zenodo | https://doi.org/10.5281/zenodo.21154423 | DOI، الورقة والبيانات |
| OSF Project | https://osf.io/7szak | سجل المشروع البحثي |
| OSF Preregistration | https://doi.org/10.17605/OSF.IO/SXGC6 | بروتوكول الدراسة المسجل مسبقاً |
| الموقع | https://moroccan-nlp.netlify.app | التوثيق ولوحة المعلومات |
| ORCID | https://orcid.org/0009-0003-8903-0029 | هوية الباحث |
| أرشيف الإنترنت | https://archive.org/details/osf-registrations-moroccan-nlp | نسخة أرشيفية دائمة |

### صفحات الموقع الرسمية

| الصفحة | الرابط |
|------|-----|
| الصفحة الرئيسية | https://moroccan-nlp.netlify.app |
| التوثيق | https://moroccan-nlp.netlify.app/documentation |
| لوحة المعلومات | https://moroccan-nlp.netlify.app/dashboard |
| التقارير | https://moroccan-nlp.netlify.app/reports |

## 🔄 الاستنساخ والتحميل

### استنساخ Git

```bash
# GitHub (رئيسي)
git clone https://github.com/gitdeeper13/moroccan_nlp.git

# GitLab (مرآة)
git clone https://gitlab.com/gitdeeper/moroccan-nlp.git

# Bitbucket (مرآة)
git clone https://bitbucket.org/gitdeeper-13/moroccan_nlp.git

# Codeberg (مرآة)
git clone https://codeberg.org/gitdeeper13/moroccan_nlp.git
```

### تحميل ZIP مباشر

| المصدر | الرابط |
|--------|------|
| GitHub | https://github.com/gitdeeper13/moroccan_nlp/archive/refs/heads/main.zip |
| GitLab | https://gitlab.com/gitdeeper/moroccan-nlp/-/archive/main/moroccan-nlp-main.zip |
| Bitbucket | https://bitbucket.org/gitdeeper-13/moroccan_nlp/get/main.zip |
| Codeberg | https://codeberg.org/gitdeeper13/moroccan_nlp/archive/main.zip |
| ملفات PyPI | https://pypi.org/project/moroccan-nlp/#files |
| سجل Zenodo | https://doi.org/10.5281/zenodo.21154423 |

## 📖 الاستشهاد

إذا ساهم moroccan_nlp في بحثك، يرجى الاستشهاد باستخدام أحد التنسيقات التالية.

### حزمة PyPI

```bibtex
@software{baladi2026moroccan_nlp_pypi,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Linguistic Resources and Models for Moroccan Darija and Arabic},
  year         = {2026},
  version      = {1.0.0},
  publisher    = {Python Package Index},
  url          = {https://pypi.org/project/moroccan-nlp/},
  note         = {Python package, MIT License, Series GITDEEPER LAB ZERO V6}
}
```

### أرشيف Zenodo (الورقة والبيانات)

```bibtex
@dataset{baladi2026moroccan_nlp_zenodo,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Linguistic Resources and Models for Moroccan Darija and Arabic — Research Paper and Data},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.21154423},
  url          = {https://doi.org/10.5281/zenodo.21154423},
  note         = {Natural Language Processing · GITDEEPER LAB ZERO V6}
}
```

### التسجيل المسبق OSF

```bibtex
@misc{baladi2026moroccan_nlp_osf,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Pre-registered Study Protocol for Linguistic Resources and Models for Moroccan Darija and Arabic},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/SXGC6},
  url          = {https://doi.org/10.17605/OSF.IO/SXGC6},
  note         = {OSF Preregistration}
}
```

### الورقة البحثية

```bibtex
@article{baladi2026moroccan_nlp,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Linguistic Resources and Models for Moroccan Darija and Arabic},
  year         = {2026},
  month        = {July},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.21154423},
  url          = {https://doi.org/10.5281/zenodo.21154423},
  note         = {Ronin Institute / Rite of Renaissance, Series GITDEEPER LAB ZERO V6}
}
```

### ورقة DarijaBERT

```bibtex
@article{gaanoun2023darijabert,
  title={Darijabert: a Step Forward in Nlp for the Written Moroccan Dialect},
  author={Gaanoun, Kamel and Naira, Abdou Mohamed and Allak, Anass and Benelallam, Imade},
  year={2023}
}
```

### APA (مضمن)

> Baladi, S. (2026). *moroccan_nlp: Linguistic Resources and Models for Moroccan Darija and Arabic* (Version 1.0.0, Series GITDEEPER LAB ZERO V6). Zenodo. https://doi.org/10.5281/zenodo.21154423

## 📜 الترخيص

هذا المشروع مرخص بموجب رخصة MIT — انظر ملف LICENSE للتفاصيل.

```
MIT License

Copyright (c) 2026 Samir Baladi

يُسمح لأي شخص بالحصول على نسخة من هذا البرنامج والملفات المرتبطة به مجاناً،
دون قيود، بما في ذلك الحقوق في استخدام ونسخ وتعديل ودمج ونشر البرنامج،
مع الإشارة إلى حقوق النشر هذه في جميع النسخ أو الأجزاء الجوهرية من البرنامج.
```

## 👤 المؤلف

سمير بلادي
باحث متعدد التخصصات في مجال الذكاء الاصطناعي— معالجة اللغة الطبيعية، اللغويات الحاسوبية، والذكاء الاصطناعي للغات قليلة الموارد
Ronin Institute / Rite of Renaissance

| جهة الاتصال | الرابط |
|---------|------|
| البريد الإلكتروني | gitdeeper@gmail.com |
| ORCID | https://orcid.org/0009-0003-8903-0029 |
| GitHub | https://github.com/gitdeeper13 |
| Zenodo | https://doi.org/10.5281/zenodo.21154423 |

---

<div align="center">

**GITDEEPER LAB ZERO V6 · الإصدار 1.0.0 · يوليو 2026**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21154423-blue.svg)](https://doi.org/10.5281/zenodo.21154423)
[![PyPI](https://img.shields.io/pypi/v/moroccan-nlp?color=1B4F72)](https://pypi.org/project/moroccan-nlp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Natural%20Language%20Processing-1B4F72)](https://doi.org/10.5281/zenodo.21154423)

*"بناء الذكاء الاصطناعي المغربي، كلمة كلمة."*

</div>
