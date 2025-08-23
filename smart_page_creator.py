#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
النظام الذكي لإنشاء الصفحات الاحترافية - النسخة المُصححة
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

        except Exception as e:
            print(f"⚠️ خطأ في Perplexity API: {e}")
            return self.get_sample_content(question)

    def get_sample_content(self, question):
        if 'عنوان' in question or 'title' in question:
            return 'الصفحة الاحترافية الذكية'
        elif 'وصف' in question or 'description' in question:
            return 'صفحة ويب احترافية تم إنشاؤها بالذكاء الاصطناعي'
        elif 'محتوى' in question or 'content' in question:
            return '''<h2>مرحباً بك في عالم التقنية</h2>
<p>هذه صفحة تم إنشاؤها تلقائياً باستخدام الذكاء الاصطناعي.</p>
<h3>المميزات الرئيسية</h3>
<ul>
    <li>تصميم احترافي ومتجاوب</li>
    <li>محتوى ذكي ومخصص</li>
    <li>تفاعلية متقدمة</li>
    <li>تحسين لمحركات البحث</li>
</ul>
<p>النظام يستخدم أحدث تقنيات الويب لضمان أفضل تجربة للمستخدمين.</p>'''
        else:
            return 'ذكاء اصطناعي، تقنية، برمجة، تطوير ويب'

    def create_css(self):
        css_content = '''
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    min-height: 100vh;
}

.container { 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 0 20px; 
}

.header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white; 
    padding: 4rem 0; 
    text-align: center;
    position: relative;
    overflow: hidden;
}

.header h1 { 
    font-size: 3.5rem; 
    margin-bottom: 1rem; 
    font-weight: 700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.header p { 
    font-size: 1.3rem; 
    opacity: 0.95;
}

.nav {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    padding: 1rem 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.nav ul { 
    list-style: none; 
    display: flex; 
    justify-content: center; 
    gap: 2rem; 
    flex-wrap: wrap;
}

.nav a {
    text-decoration: none; 
    color: #333; 
    font-weight: 600;
    padding: 0.8rem 1.5rem; 
    border-radius: 25px;
    transition: all 0.3s ease;
}

.nav a:hover { 
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    transform: translateY(-2px);
}

.main { padding: 4rem 0; }

.section {
    background: white; 
    margin: 2rem 0; 
    padding: 3rem;
    border-radius: 20px; 
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    position: relative;
}

.section h2 { 
    color: #667eea; 
    margin-bottom: 1.5rem; 
    font-size: 2.5rem;
    font-weight: 700;
}

.section h3 {
    color: #764ba2;
    margin: 2rem 0 1rem 0;
    font-size: 1.8rem;
}

.section p {
    font-size: 1.1rem;
    line-height: 1.8;
    margin-bottom: 1.5rem;
    color: #555;
}

.section ul {
    margin-left: 2rem;
    margin-bottom: 1.5rem;
}

.section li {
    margin-bottom: 0.8rem;
    font-size: 1.1rem;
    line-height: 1.6;
}

.btn {
    display: inline-block; 
    padding: 1.2rem 2.5rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white; 
    text-decoration: none; 
    border-radius: 30px;
    transition: all 0.3s ease;
    font-weight: 600;
    font-size: 1.1rem;
}

.btn:hover { 
    transform: translateY(-3px); 
    box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
}

.footer {
    background: linear-gradient(135deg, #2d3748, #4a5568);
    color: white; 
    padding: 3rem 0; 
    text-align: center;
    margin-top: 4rem;
}

.footer p {
    font-size: 1.1rem;
    opacity: 0.9;
}

.ai-badge {
    position: absolute;
    top: 20px;
    right: 20px;
    background: linear-gradient(45deg, #667eea, #764ba2);
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    z-index: 10;
}

.text-center { text-align: center; }

.gradient-text {
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

@media (max-width: 768px) {
    .header h1 { font-size: 2.5rem; }
    .container { padding: 0 15px; }
    .section { padding: 2rem 1.5rem; }
    .nav ul { flex-direction: column; gap: 1rem; text-align: center; }
    .btn { padding: 1rem 2rem; font-size: 1rem; }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in { animation: fadeInUp 0.6s ease-out; }
'''

        with open('./smart_pages/assets/css/style.css', 'w', encoding='utf-8') as f:
            f.write(css_content)
        return './smart_pages/assets/css/style.css'

    def create_js(self):
        js_content = '''
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎉 الصفحة الذكية جاهزة!');

    // Add fade-in animation to sections
    const sections = document.querySelectorAll('.section');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    sections.forEach((section) => {
        observer.observe(section);
    });

    // Button hover effects
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.05)';
        });

        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Add visitor counter
    let visitors = localStorage.getItem('page_visitors') || 0;
    visitors = parseInt(visitors) + 1;
    localStorage.setItem('page_visitors', visitors);
});

// Welcome message
setTimeout(() => {
    console.log('%c🚀 مرحباً بك في النظام الذكي!', 'color: #667eea; font-size: 16px; font-weight: bold;');
}, 1000);
'''

        with open('./smart_pages/assets/js/main.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        return './smart_pages/assets/js/main.js'

    def create_page(self, topic):
        print(f"🏗️ إنشاء صفحة عن: {topic}")

        # Get content
        title = self.ask_perplexity(f"اكتب عنوان جذاب عن {topic}")
        description = self.ask_perplexity(f"اكتب وصف قصير عن {topic}")
        content = self.ask_perplexity(f"اكتب محتوى HTML عن {topic}")
        keywords = self.ask_perplexity(f"كلمات مفتاحية عن {topic}")

        # Create files
        self.create_css()
        self.create_js()

        # Create HTML
        current_time = datetime.now()
        html_template = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {{ font-family: 'Tajawal', sans-serif; }}
    </style>
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
                <li><a href="#home"><i class="fas fa-home"></i> الرئيسية</a></li>
                <li><a href="#about"><i class="fas fa-info-circle"></i> حول</a></li>
                <li><a href="#contact"><i class="fas fa-envelope"></i> تواصل</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="container">
            <section class="section">
                <div class="ai-badge">
                    <i class="fas fa-robot"></i> محتوى ذكي
                </div>
                {content}
            </section>

            <section class="section text-center">
                <h2 class="gradient-text">تم الإنشاء بالذكاء الاصطناعي</h2>
                <p>هذه الصفحة تم إنشاؤها تلقائياً باستخدام تقنيات الذكاء الاصطناعي المتطورة</p>
                <div style="margin-top: 2rem;">
                    <a href="#" class="btn">
                        <i class="fas fa-magic"></i> اكتشف المزيد
                    </a>
                </div>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p><i class="fas fa-magic"></i> تم إنشاء هذه الصفحة بالذكاء الاصطناعي</p>
            <p style="margin-top: 1rem; opacity: 0.8;">
                © {year} النظام الذكي • تم الإنشاء: {timestamp}
            </p>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>'''

        html_content = html_template.format(
            title=title,
            description=description,
            keywords=keywords,
            content=content,
            year=current_time.year,
            timestamp=current_time.strftime("%Y-%m-%d %H:%M")
        )

        # Save page
        filename = f"{topic.replace(' ', '_').lower()}.html"
        filepath = f"./smart_pages/pages/{filename}"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Save data
        page_data = {
            'title': title,
            'description': description,
            'keywords': keywords,
            'topic': topic,
            'filename': filename,
            'created_at': current_time.isoformat()
        }

        data_file = f"./smart_pages/data/{filename.replace('.html', '.json')}"
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, indent=2, ensure_ascii=False)

        print(f"✅ تم إنشاء: {filepath}")
        return filepath, page_data

    def create_index(self, pages_data):
        # Create cards HTML
        cards_html_parts = []
        for page_path, page_data in pages_data:
            card_html = f'''
                    <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); transition: all 0.3s ease;">
                        <h3 style="color: #667eea; margin-bottom: 1rem; font-size: 1.5rem;">
                            <i class="fas fa-file-alt"></i> {page_data['topic']}
                        </h3>
                        <p style="color: #666; margin-bottom: 1.5rem; line-height: 1.6;">
                            {page_data['description'][:100]}...
                        </p>
                        <a href="pages/{page_data['filename']}" class="btn" style="font-size: 0.9rem;">
                            <i class="fas fa-eye"></i> عرض الصفحة
                        </a>
                        <div style="margin-top: 1rem; font-size: 0.8rem; color: #999;">
                            <i class="fas fa-clock"></i> {page_data['created_at'][:19]}
                        </div>
                    </div>'''
            cards_html_parts.append(card_html)

        cards_html = ''.join(cards_html_parts)
        current_time = datetime.now()

        index_template = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>النظام الذكي - الفهرس</title>
    <meta name="description" content="فهرس الصفحات التي تم إنشاؤها بالذكاء الاصطناعي">
    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {{ font-family: 'Tajawal', sans-serif; }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1><i class="fas fa-magic"></i> النظام الذكي لإنشاء الصفحات</h1>
            <p>تم إنشاء {pages_count} صفحة احترافية بالذكاء الاصطناعي</p>
        </div>
    </header>

    <main class="main">
        <div class="container">
            <section class="section">
                <h2><i class="fas fa-list"></i> فهرس الصفحات المُنشأة</h2>
                <p style="font-size: 1.2rem; color: #666; margin-bottom: 2rem;">
                    تم إنشاء هذه الصفحات تلقائياً باستخدام الذكاء الاصطناعي. كل صفحة تحتوي على محتوى فريد ومخصص.
                </p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem;">
                    {cards_html}
                </div>
            </section>

            <section class="section text-center">
                <h2 class="gradient-text">مميزات النظام الذكي</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">
                    <div style="padding: 2rem; text-align: center;">
                        <i class="fas fa-brain" style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;"></i>
                        <h3>ذكاء اصطناعي</h3>
                        <p>محتوى مُولد بالذكاء الاصطناعي</p>
                    </div>
                    <div style="padding: 2rem; text-align: center;">
                        <i class="fas fa-mobile-alt" style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;"></i>
                        <h3>تصميم متجاوب</h3>
                        <p>يعمل على جميع الأجهزة</p>
                    </div>
                    <div style="padding: 2rem; text-align: center;">
                        <i class="fas fa-rocket" style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;"></i>
                        <h3>أداء عالي</h3>
                        <p>سرعة تحميل ممتازة</p>
                    </div>
                    <div style="padding: 2rem; text-align: center;">
                        <i class="fas fa-palette" style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;"></i>
                        <h3>تصميم عصري</h3>
                        <p>واجهة جذابة ومتطورة</p>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p><i class="fas fa-magic"></i> النظام الذكي لإنشاء الصفحات الاحترافية</p>
            <p style="margin-top: 1rem;">
                تم إنشاء {pages_count} صفحة في {timestamp}
            </p>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>'''

        html_content = index_template.format(
            pages_count=len(pages_data),
            cards_html=cards_html,
            timestamp=current_time.strftime("%Y-%m-%d %H:%M")
        )

        with open('./smart_pages/index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)

        print("📋 تم إنشاء صفحة الفهرس: ./smart_pages/index.html")

def main():
    try:
        creator = SmartPageCreator()

        # Get topics from environment or use defaults
        topics_str = os.getenv('TOPICS', 'الذكاء الاصطناعي,البرمجة الحديثة,التسويق الرقمي,ريادة الأعمال')
        topics = [topic.strip() for topic in topics_str.split(',')]

        max_pages = int(os.getenv('MAX_PAGES_PER_RUN', '4'))
        topics = topics[:max_pages]

        print(f"🚀 بدء إنشاء {len(topics)} صفحة...")

        pages_data = []
        for i, topic in enumerate(topics):
            print(f"\n[{i+1}/{len(topics)}] معالجة: {topic}")
            try:
                page_path, page_data = creator.create_page(topic)
                pages_data.append((page_path, page_data))
                time.sleep(1)
            except Exception as e:
                print(f"❌ خطأ في إنشاء صفحة {topic}: {e}")

        # Create index
        if pages_data:
            creator.create_index(pages_data)

        print(f"\n🎉 تم إنشاء {len(pages_data)} صفحة بنجاح!")
        print("🌐 افتح: ./smart_pages/index.html")

        return True

    except Exception as e:
        print(f"❌ خطأ عام: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
