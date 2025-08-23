#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
النظام الذكي لإنشاء الصفحات الاحترافية
يستخدم Perplexity AI لإنشاء صفحات ويب احترافية تلقائياً
'''

import os
import json
import time
import requests
from datetime import datetime

class SmartPageCreator:
    def __init__(self):
        self.perplexity_api_key = os.getenv('PERPLEXITY_API_KEY', '')
        self.setup_directories()
        print("🤖 النظام الذكي لإنشاء الصفحات الاحترافية")
        print("=" * 60)

    def setup_directories(self):
        dirs = [
            './smart_pages/pages',
            './smart_pages/assets/css', 
            './smart_pages/assets/js',
            './smart_pages/data'
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)

    def ask_perplexity(self, question):
        if not self.perplexity_api_key:
            return self.get_sample_content(question)

        try:
            headers = {
                'Authorization': f'Bearer {self.perplexity_api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'llama-3.1-sonar-small-128k-online',
                'messages': [{'role': 'user', 'content': question}],
                'max_tokens': 1500
            }

            response = requests.post(
                'https://api.perplexity.ai/chat/completions',
                headers=headers, json=data, timeout=30
            )

            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                return self.get_sample_content(question)

        except Exception:
            return self.get_sample_content(question)

    def get_sample_content(self, question):
        if 'عنوان' in question or 'title' in question:
            return 'الصفحة الاحترافية الذكية'
        elif 'وصف' in question or 'description' in question:
            return 'صفحة ويب احترافية تم إنشاؤها بالذكاء الاصطناعي'
        elif 'محتوى' in question or 'content' in question:
            return '''
<h2>مرحباً بك في عالم التقنية</h2>
<p>هذه صفحة تم إنشاؤها تلقائياً باستخدام الذكاء الاصطناعي.</p>
<h3>المميزات الرئيسية</h3>
<ul>
    <li>تصميم احترافي ومتجاوب</li>
    <li>محتوى ذكي ومخصص</li>
    <li>تفاعلية متقدمة</li>
</ul>
'''
        else:
            return 'ذكاء اصطناعي، تقنية، برمجة'

    def create_css(self):
        css = '''
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f4f4f4;
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

.header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white; padding: 3rem 0; text-align: center;
}

.header h1 { font-size: 3rem; margin-bottom: 1rem; }
.header p { font-size: 1.2rem; }

.nav {
    background: white; padding: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.nav ul { list-style: none; display: flex; justify-content: center; gap: 2rem; }

.nav a {
    text-decoration: none; color: #333; font-weight: 600;
    padding: 0.5rem 1rem; border-radius: 5px;
    transition: all 0.3s ease;
}

.nav a:hover { background: #667eea; color: white; }

.main { padding: 3rem 0; }

.section {
    background: white; margin: 2rem 0; padding: 2rem;
    border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.section h2 { color: #667eea; margin-bottom: 1rem; }

.btn {
    display: inline-block; padding: 1rem 2rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white; text-decoration: none; border-radius: 5px;
    transition: transform 0.3s ease;
}

.btn:hover { transform: translateY(-2px); }

.footer {
    background: #333; color: white; padding: 2rem 0; text-align: center;
}

@media (max-width: 768px) {
    .header h1 { font-size: 2rem; }
    .container { padding: 0 15px; }
    .nav ul { flex-direction: column; gap: 1rem; }
}
'''

        with open('./smart_pages/assets/css/style.css', 'w') as f:
            f.write(css)
        return './smart_pages/assets/css/style.css'

    def create_js(self):
        js = '''
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎉 الصفحة الذكية جاهزة!');

    // تأثيرات سلسة
    const sections = document.querySelectorAll('.section');
    sections.forEach((section, index) => {
        section.style.animationDelay = (index * 0.2) + 's';
        section.style.animation = 'fadeInUp 0.6s ease forwards';
    });

    // تأثير الأزرار
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            console.log('تم النقر على الزر!');
        });
    });
});

// إضافة CSS للحركات
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);
'''

        with open('./smart_pages/assets/js/main.js', 'w') as f:
            f.write(js)
        return './smart_pages/assets/js/main.js'

    def create_page(self, topic):
        print(f"🏗️ إنشاء صفحة عن: {topic}")

        # إنشاء المحتوى بالذكاء الاصطناعي
        title = self.ask_perplexity(f"اكتب عنوان جذاب عن {topic}")
        description = self.ask_perplexity(f"اكتب وصف قصير عن {topic}")
        content = self.ask_perplexity(f"اكتب محتوى HTML عن {topic}")
        keywords = self.ask_perplexity(f"كلمات مفتاحية عن {topic}")

        # إنشاء الملفات
        css_path = self.create_css()
        js_path = self.create_js()

        # إنشاء HTML
        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>{title}</h1>
            <p>{description}</p>
        </div>
    </header>

    <nav class="nav">
        <div class="container">
            <ul>
                <li><a href="#home">الرئيسية</a></li>
                <li><a href="#about">حول</a></li>
                <li><a href="#contact">تواصل</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="container">
            <section class="section">
                <div style="position: relative;">
                    <div style="position: absolute; top: 10px; right: 10px; background: #667eea; color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px;">
                        🤖 محتوى ذكي
                    </div>
                    {content}
                </div>
            </section>

            <section class="section" style="text-align: center;">
                <h2>تم الإنشاء بالذكاء الاصطناعي</h2>
                <p>هذه الصفحة تم إنشاؤها تلقائياً باستخدام تقنيات متطورة</p>
                <a href="#" class="btn">اكتشف المزيد</a>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>© {datetime.now().year} النظام الذكي - تم الإنشاء: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>'''

        # حفظ الصفحة
        filename = f"{topic.replace(' ', '_').lower()}.html"
        filepath = f"./smart_pages/pages/{filename}"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✅ تم إنشاء: {filepath}")
        return filepath

    def create_index(self, pages):
        topics = [p.split('/')[-1].replace('.html', '').replace('_', ' ').title() for p in pages]

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>النظام الذكي - الفهرس</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>🤖 النظام الذكي لإنشاء الصفحات</h1>
            <p>تم إنشاء {len(pages)} صفحة احترافية</p>
        </div>
    </header>

    <main class="main">
        <div class="container">
            <section class="section">
                <h2>📋 فهرس الصفحات</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    {"".join([f'''
                    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <h3 style="color: #667eea; margin-bottom: 1rem;">{topic}</h3>
                        <p>صفحة احترافية تم إنشاؤها بالذكاء الاصطناعي</p>
                        <a href="pages/{os.path.basename(page)}" class="btn" style="margin-top: 1rem;">عرض الصفحة</a>
                    </div>
                    ''' for page, topic in zip(pages, topics)])}
                </div>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>© {datetime.now().year} النظام الذكي</p>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>'''

        with open('./smart_pages/index.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print("📋 تم إنشاء صفحة الفهرس: ./smart_pages/index.html")

def main():
    creator = SmartPageCreator()

    topics = ["الذكاء الاصطناعي", "البرمجة الحديثة", "التسويق الرقمي", "ريادة الأعمال"]

    pages = []
    for topic in topics:
        page_path = creator.create_page(topic)
        pages.append(page_path)
        time.sleep(1)  # راحة بين الصفحات

    creator.create_index(pages)

    print(f"\n🎉 تم إنشاء {len(pages)} صفحة احترافية!")
    print("🌐 افتح: ./smart_pages/index.html")

if __name__ == "__main__":
    main()
