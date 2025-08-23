#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import time
import requests
from datetime import datetime

class SimplePageCreator:
    def __init__(self):
        self.api_key = os.getenv('PERPLEXITY_API_KEY', '')
        self.setup_dirs()
        print("النظام البسيط الآمن جاهز!")

    def setup_dirs(self):
        dirs = ['./simple_pages', './simple_pages/assets', './simple_pages/data']
        for d in dirs:
            os.makedirs(d, exist_ok=True)

    def get_content(self, prompt):
        if not self.api_key:
            return self.get_default_content()

        try:
            headers = {
                'Authorization': 'Bearer ' + self.api_key,
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'llama-3.1-sonar-small-128k-online',
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': 1000
            }

            response = requests.post(
                'https://api.perplexity.ai/chat/completions',
                headers=headers, 
                json=data, 
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                return self.get_default_content()

        except Exception as e:
            print("خطأ في API:", e)
            return self.get_default_content()

    def get_default_content(self):
        return "محتوى افتراضي عالي الجودة تم إنشاؤه بالنظام الذكي البسيط"

    def create_css(self):
        css = """
body { 
    font-family: Arial, sans-serif; 
    margin: 0; 
    padding: 20px; 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #333;
}

.container { 
    max-width: 800px; 
    margin: 0 auto; 
    background: white; 
    padding: 30px; 
    border-radius: 10px; 
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

h1 { 
    color: #667eea; 
    text-align: center; 
    font-size: 2.5rem; 
    margin-bottom: 20px;
}

h2 { 
    color: #764ba2; 
    font-size: 1.8rem; 
    margin: 30px 0 15px 0;
}

p { 
    line-height: 1.6; 
    margin-bottom: 15px; 
    font-size: 1.1rem;
}

.badge { 
    background: #28a745; 
    color: white; 
    padding: 10px 20px; 
    border-radius: 20px; 
    display: inline-block; 
    margin: 10px 0;
    font-weight: bold;
}

.btn { 
    background: linear-gradient(45deg, #667eea, #764ba2); 
    color: white; 
    padding: 15px 30px; 
    text-decoration: none; 
    border-radius: 25px; 
    display: inline-block; 
    margin: 20px 0;
    font-weight: bold;
    transition: transform 0.3s;
}

.btn:hover { 
    transform: translateY(-2px); 
}

.footer { 
    text-align: center; 
    margin-top: 50px; 
    padding: 20px; 
    border-top: 2px solid #eee;
    color: #666;
}
"""

        with open('./simple_pages/style.css', 'w', encoding='utf-8') as f:
            f.write(css)

    def create_page(self, topic):
        print("إنشاء صفحة عن:", topic)

        # الحصول على المحتوى
        title = self.get_content("اكتب عنوان جذاب عن " + topic)
        content = self.get_content("اكتب محتوى مفصل عن " + topic)

        if len(title) > 100:
            title = "صفحة احترافية عن " + topic

        # إنشاء HTML
        html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>""" + title + """</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="container">
        <h1>""" + title + """</h1>

        <div class="badge">مُولد بالذكاء الاصطناعي</div>

        <h2>المحتوى الرئيسي</h2>
        <p>""" + content + """</p>

        <h2>مميزات هذه الصفحة</h2>
        <p>✅ تم إنشاؤها تلقائياً بالذكاء الاصطناعي</p>
        <p>✅ تصميم بسيط وأنيق</p>
        <p>✅ محتوى عالي الجودة</p>
        <p>✅ متوافقة مع جميع الأجهزة</p>

        <a href="../index.html" class="btn">العودة للرئيسية</a>

        <div class="footer">
            <p>تم الإنشاء: """ + datetime.now().strftime("%Y-%m-%d %H:%M") + """</p>
            <p>الموضوع: """ + topic + """</p>
        </div>
    </div>
</body>
</html>"""

        # حفظ الصفحة
        filename = topic.replace(' ', '_').lower() + '.html'
        filepath = './simple_pages/' + filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

        # حفظ البيانات
        data = {
            'title': title,
            'content': content[:200] + '...',
            'topic': topic,
            'filename': filename,
            'created': datetime.now().isoformat()
        }

        with open('./simple_pages/data/' + filename.replace('.html', '.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("تم إنشاء:", filepath)
        return filepath, data

    def create_index(self, pages_data):
        cards = []
        for filepath, data in pages_data:
            card = """
        <div style="border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background: #f9f9f9;">
            <h3 style="color: #667eea; margin-bottom: 10px;">""" + data['topic'] + """</h3>
            <p style="color: #666; margin-bottom: 15px;">""" + data['content'] + """</p>
            <a href=".""" + data['filename'] + """" style="background: #667eea; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">عرض الصفحة</a>
            <small style="display: block; margin-top: 10px; color: #888;">تم الإنشاء: """ + data['created'][:10] + """</small>
        </div>"""
            cards.append(card)

        html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>النظام البسيط الذكي</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>النظام البسيط الذكي 🤖</h1>

        <div class="badge">تم إنشاء """ + str(len(pages_data)) + """ صفحة بنجاح!</div>

        <h2>الصفحات المُنشأة</h2>
        <p>تم إنشاء هذه الصفحات تلقائياً باستخدام الذكاء الاصطناعي البسيط والفعال.</p>

        """ + ''.join(cards) + """

        <div class="footer">
            <p>🎉 النظام البسيط الآمن - يعمل دائماً!</p>
            <p>تم التشغيل: """ + datetime.now().strftime("%Y-%m-%d %H:%M") + """</p>
        </div>
    </div>
</body>
</html>"""

        with open('./simple_pages/index.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print("تم إنشاء الفهرس: ./simple_pages/index.html")

    def run(self):
        try:
            print("🚀 بدء النظام البسيط الآمن...")

            # الحصول على المواضيع
            topics_env = os.getenv('TOPICS', 'الذكاء الاصطناعي,البرمجة الحديثة,التسويق الرقمي,ريادة الأعمال')
            topics = [t.strip() for t in topics_env.split(',')][:4]

            print("المواضيع:", topics)

            # إنشاء CSS
            self.create_css()

            # إنشاء الصفحات
            pages_data = []
            for i, topic in enumerate(topics):
                print("[{}/{}] معالجة: {}".format(i+1, len(topics), topic))
                try:
                    filepath, data = self.create_page(topic)
                    pages_data.append((filepath, data))
                    time.sleep(2)  # راحة
                except Exception as e:
                    print("خطأ في", topic, ":", e)
                    continue

            # إنشاء الفهرس
            if pages_data:
                self.create_index(pages_data)

            print("")
            print("🎉 تم إنشاء {} صفحة بنجاح!".format(len(pages_data)))
            print("🌐 افتح: ./simple_pages/index.html")
            print("")

            return True

        except Exception as e:
            print("خطأ عام:", e)
            return False

def main():
    creator = SimplePageCreator()
    return creator.run()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
