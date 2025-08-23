# 🤖 النظام الذكي لإنشاء الصفحات الاحترافية

> نظام متطور يستخدم الذكاء الاصطناعي لإنشاء صفحات ويب احترافية تلقائياً

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://github.com/YOUR_USERNAME/smart-page-creator/workflows/Smart%20Page%20Creator/badge.svg)](https://github.com/YOUR_USERNAME/smart-page-creator/actions)

## ✨ المميزات الرئيسية

🧠 **ذكاء اصطناعي متطور** - يستخدم Perplexity AI لإنشاء محتوى عالي الجودة  
🎨 **تصميم احترافي** - قوالب CSS عصرية ومتجاوبة  
⚡ **أتمتة كاملة** - تشغيل تلقائي مع GitHub Actions  
🌐 **نشر مباشر** - رفع تلقائي على GitHub Pages  
📱 **تصميم متجاوب** - يعمل على جميع الأجهزة والشاشات  
🔧 **قابل للتخصيص** - إعدادات مرنة وقوالب متعددة  

## 🚀 التشغيل السريع

### المتطلبات الأساسية
- Python 3.9 أو أحدث
- حساب GitHub
- مفتاح Perplexity AI (اختياري لكنه مُوصى به)

### التثبيت والتشغيل

```bash
# 1. استنساخ المشروع
git clone https://github.com/YOUR_USERNAME/smart-page-creator.git
cd smart-page-creator

# 2. إنشاء البيئة الافتراضية
python -m venv venv
source venv/bin/activate  # على Linux/Mac
# أو
venv\Scripts\activate  # على Windows

# 3. تثبيت المتطلبات
pip install -r requirements.txt

# 4. إعداد متغيرات البيئة
cp .env.example .env
# حرر ملف .env وأضف مفتاح Perplexity API

# 5. تشغيل النظام
python smart_page_creator.py
```

## 🔑 الحصول على Perplexity API

1. اذهب إلى [perplexity.ai](https://www.perplexity.ai/)
2. أنشئ حساباً جديداً أو سجل دخولك
3. اذهب إلى [إعدادات API](https://www.perplexity.ai/settings/api)
4. أنشئ مفتاح API جديد
5. انسخ المفتاح وأضفه في ملف `.env`

## 🛠️ الإعدادات والتخصيص

### متغيرات البيئة الرئيسية

```env
# API Keys
PERPLEXITY_API_KEY=your_api_key_here

# إعدادات أساسية
MAX_PAGES_PER_RUN=5
DEFAULT_TOPICS=الذكاء الاصطناعي,البرمجة,التسويق
CSS_THEME=default  # default, dark, modern, professional

# ميزات متقدمة
ENABLE_SEO_OPTIMIZATION=true
GENERATE_SITEMAP=true
ENABLE_ANALYTICS=true
```

### المواضيع المدعومة

يمكن للنظام إنشاء صفحات عن أي موضوع، مع التركيز على:
- التقنية والبرمجة
- التسويق الرقمي
- ريادة الأعمال
- التعليم والتطوير
- الذكاء الاصطناعي

## 🤖 أتمتة GitHub Actions

النظام يشمل workflow متطور للتشغيل التلقائي:

- **تشغيل يومي**: كل يوم الساعة 9 صباحاً
- **تشغيل يدوي**: مع إمكانية تخصيص المواضيع
- **نشر تلقائي**: على GitHub Pages
- **تنظيف تلقائي**: للنتائج القديمة

### تفعيل الأتمتة:

1. ارفع المشروع على GitHub
2. اذهب إلى Settings → Secrets → Actions
3. أضف `PERPLEXITY_API_KEY` 
4. فعل GitHub Pages من Settings → Pages
5. الآن سيعمل النظام تلقائياً!

## 📁 هيكل المشروع

```
smart-page-creator/
├── 🤖 smart_page_creator.py       # النظام الرئيسي
├── 📋 requirements.txt            # المتطلبات
├── 🔑 .env.example               # مثال متغيرات البيئة
├── 📖 README.md                  # هذا الملف
├── 🚫 .gitignore                 # ملفات مستثناة
├── 📚 github_beginners_guide.md  # دليل المبتدئين
├── 🤖 .github/workflows/         # أتمتة GitHub
│   └── smart-creator.yml
└── 🌐 smart_pages/               # الصفحات المُنتجة
    ├── index.html
    ├── pages/
    ├── assets/
    │   ├── css/
    │   └── js/
    └── data/
```

## 🎨 القوالب والثيمات

### الثيمات المتاحة:
- **Default** - تصميم أزرق أنيق
- **Dark** - وضع داكن عصري  
- **Modern** - تصميم حديث وبسيط
- **Professional** - مناسب للأعمال

### تخصيص التصميم:
```python
# في smart_page_creator.py
creator = SmartPageCreator()
creator.set_theme('modern')  # تغيير الثيم
creator.customize_colors({
    'primary': '#your-color',
    'secondary': '#your-color'
})
```

## 📊 الإحصائيات والتحليلات

النظام يوفر:
- ✅ عدد الصفحات المُنشأة
- ✅ أداء AI والاستجابة
- ✅ إحصائيات الاستخدام
- ✅ تقارير يومية/أسبوعية

## 🔧 استكشاف الأخطاء

### مشاكل شائعة وحلولها:

**❌ "API key invalid"**
```bash
# تأكد من صحة المفتاح في ملف .env
export PERPLEXITY_API_KEY="your-key-here"
python -c "import os; print(os.getenv('PERPLEXITY_API_KEY'))"
```

**❌ "Module not found"**
```bash
# إعادة تثبيت المتطلبات
pip install -r requirements.txt --force-reinstall
```

**❌ "GitHub Actions failed"**
- تأكد من إضافة PERPLEXITY_API_KEY في Secrets
- راجع logs في تبويب Actions

## 🤝 المساهمة والتطوير

نرحب بجميع المساهمات! يمكنك:

1. **Fork** المشروع
2. إنشاء **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** التغييرات (`git commit -m 'Add amazing feature'`)
4. **Push** إلى branch (`git push origin feature/amazing-feature`)
5. إنشاء **Pull Request**

## 📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

## 🌟 دعم المشروع

إذا أعجبك المشروع:
- ⭐ أعط نجمة على GitHub
- 🐛 بلغ عن الأخطاء
- 💡 اقترح ميزات جديدة
- 📢 شارك المشروع

## 📞 التواصل والدعم

- 🐛 **بلاغ الأخطاء**: [GitHub Issues](https://github.com/YOUR_USERNAME/smart-page-creator/issues)
- 💬 **الأسئلة**: [GitHub Discussions](https://github.com/YOUR_USERNAME/smart-page-creator/discussions)
- 📧 **البريد الإلكتروني**: your-email@example.com

---

<div align="center">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/smart-page-creator?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/YOUR_USERNAME/smart-page-creator?style=social" alt="Forks">
  <img src="https://img.shields.io/github/issues/YOUR_USERNAME/smart-page-creator" alt="Issues">
</div>

<div align="center">
  <h3>🚀 صُنع بـ ❤️ للمجتمع العربي</h3>
  <p>نظام ذكي • مفتوح المصدر • مجاني تماماً</p>
</div>
