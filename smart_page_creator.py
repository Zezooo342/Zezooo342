#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام النشر الذكي الهجين - الحل الأمثل للنشر على جميع المنصات
================================================================
يولد المحتوى جاهز للنسخ والنشر + أدوات مساعدة ذكية
"""

import os
import json
import requests
from datetime import datetime, timedelta
import time

class SmartSocialPublisher:
    """ناشر المحتوى الذكي - يجهز المحتوى للنشر اليدوي الأمثل"""

    def __init__(self):
        self.api_key = os.getenv('PERPLEXITY_API_KEY', '')
        self.setup_directories()
        print("🚀 نظام النشر الذكي جاهز!")
        print("📱 يولد محتوى جاهز لفيسبوك وإنستغرام وتيك توك ويوتيوب")

    def setup_directories(self):
        """إنشاء مجلدات النظام"""
        dirs = [
            './smart_publisher',
            './smart_publisher/ready_posts',
            './smart_publisher/templates',
            './smart_publisher/schedule',
            './smart_publisher/analytics'
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

    def call_perplexity_api(self, prompt, system_prompt=""):
        """استدعاء Perplexity Pro API"""
        if not self.api_key:
            print("💡 نشتغل بمحتوى عالي الجودة (أضف Perplexity Pro للقوة الكاملة)")
            return self.get_premium_content(prompt)

        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }

            messages = []
            if system_prompt:
                messages.append({'role': 'system', 'content': system_prompt})
            messages.append({'role': 'user', 'content': prompt})

            data = {
                'model': 'llama-3.1-sonar-large-128k-online',
                'messages': messages,
                'max_tokens': 2000,
                'temperature': 0.8
            }

            response = requests.post(
                'https://api.perplexity.ai/chat/completions',
                headers=headers, 
                json=data, 
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()
                print(f"✅ Perplexity Pro: محتوى حديث ({len(content)} حرف)")
                return content
            else:
                print(f"⚠️ API العادي - محتوى احتياطي عالي الجودة")
                return self.get_premium_content(prompt)

        except Exception as e:
            print(f"💡 محتوى احتياطي عالي الجودة")
            return self.get_premium_content(prompt)

    def get_premium_content(self, prompt):
        """محتوى احتياطي احترافي حسب المنصة"""

        premium_templates = {
            'facebook_educational': """🎯 5 خطوات لتحسين حياتك المهنية في 2025:

1️⃣ **طور مهاراتك الرقمية**: الذكاء الاصطناعي والتسويق الرقمي أولوية
2️⃣ **ابني شبكة علاقات قوية**: 3 اتصالات جديدة أسبوعياً في LinkedIn
3️⃣ **استثمر في تعلم اللغات**: الإنجليزية + لغة تقنية (Python مثلاً)
4️⃣ **طور العلامة الشخصية**: حضور قوي في التواصل الاجتماعي
5️⃣ **خطط للمستقبل**: أهداف واضحة لكل 3 أشهر

💡 أي من هذه النصائح ستبدأ بها اليوم؟ شاركنا في التعليقات!

#تطوير_المهنة #النجاح2025 #المستقبل_الرقمي #تطوير_الذات""",

            'instagram_lifestyle': """✨ الصباح المثالي لرائد أعمال ناجح:

6:00 🌅 استيقظ مع شروق الشمس
6:15 🧘‍♀️ تأمل وامتنان (10 دقائق)
6:30 💪 تمارين رياضية (30 دقيقة)
7:00 📚 قراءة كتاب ملهم
7:30 ☕ إفطار صحي + مراجعة الأهداف
8:00 🎯 أهم 3 مهام لليوم

البداية الصحيحة = يوم ناجح 💫

إيه روتين الصباح بتاعك؟ 👇

#روتين_الصباح #ريادة_الأعمال #النجاح #حياة_صحية #تطوير_الذات #صباح_الخير""",

            'tiktok_trending': """🔥 سر النجاح في 60 ثانية:

قانون الـ 1%:
📈 تحسن 1% كل يوم
✨ بعد سنة = تحسن 37 مرة!

المعادلة:
❌ الكمال المستحيل 
✅ التحسن الصغير المستمر

مثال:
📚 اقرأ صفحة واحدة يومياً
💪 10 تمارين يومياً  
💰 وفر جنيه واحد يومياً

النتيجة بعد سنة؟ 
شخص جديد تماماً! 🚀

#قانون_النجاح #تحسن_مستمر #تحفيز #نصائح""",

            'youtube_educational': """🎥 كيف تبدأ مشروعك الأول بـ 500 جنيه فقط

في الفيديو ده هنتكلم عن:

🎯 أفضل 5 مشاريع للمبتدئين بميزانية صغيرة
💡 كيف تختار المشروع المناسب ليك
📊 دراسة جدوى سريعة في 10 دقائق
💰 مصادر التمويل البديلة
⚡ أول خطوة عملية تخطوها بعد الفيديو

هدفي إني أساعدك تبدأ صح من أول يوم!

إيه المشروع اللي حابب تعرف عنه أكتر؟ 👇

#ريادة_الأعمال #مشاريع_صغيرة #البداية #استثمار"""
        }

        # اختيار المحتوى حسب نوع الطلب
        if 'facebook' in prompt.lower() and 'educational' in prompt.lower():
            return premium_templates['facebook_educational']
        elif 'instagram' in prompt.lower():
            return premium_templates['instagram_lifestyle']  
        elif 'tiktok' in prompt.lower():
            return premium_templates['tiktok_trending']
        elif 'youtube' in prompt.lower():
            return premium_templates['youtube_educational']
        else:
            return premium_templates['facebook_educational']  # افتراضي

    def generate_platform_ready_post(self, platform, content_type, topic, user_niche="عام"):
        """توليد منشور جاهز للنشر حسب المنصة"""

        platform_specs = {
            'facebook': {
                'max_length': 2000,
                'hashtag_limit': 5,
                'best_times': ['20:00', '21:00', '14:00'],
                'engagement_tips': [
                    'اطرح سؤال في النهاية',
                    'استخدم إيموجي لجذب الانتباه',
                    'أضف دعوة واضحة للعمل'
                ]
            },
            'instagram': {
                'max_length': 500,
                'hashtag_limit': 30,
                'best_times': ['17:00', '18:00', '19:00'],
                'engagement_tips': [
                    'احكي قصة شخصية',
                    'استخدم هاشتاجات متنوعة',
                    'أضف موقعك الجغرافي'
                ]
            },
            'tiktok': {
                'max_length': 150,
                'hashtag_limit': 10,
                'best_times': ['18:00', '19:00', '20:00'],
                'engagement_tips': [
                    'ابدأ بخطاف قوي',
                    'استخدم الترندات الحالية',
                    'اطلب التفاعل مبكراً'
                ]
            },
            'youtube': {
                'max_length': 1000,
                'hashtag_limit': 15,
                'best_times': ['14:00', '15:00', '20:00'],
                'engagement_tips': [
                    'عنوان جذاب مع أرقام',
                    'اطلب الاشتراك والجرس',
                    'أضف وصف مفصل'
                ]
            }
        }

        spec = platform_specs.get(platform, platform_specs['facebook'])

        system_prompt = f"""أنت خبير محتوى احترافي لمنصة {platform}.
        مهمتك إنشاء محتوى {content_type} عالي الجودة عن {topic} في مجال {user_niche}.

        مواصفات {platform}:
        - طول النص: حتى {spec['max_length']} حرف
        - عدد الهاشتاجات: حتى {spec['hashtag_limit']}
        - أفضل أوقات النشر: {', '.join(spec['best_times'])}

        اجعل المحتوى:
        - أصلي ومميز 100%
        - يجذب الجمهور العربي
        - يحفز على التفاعل
        - مناسب تماماً لطبيعة {platform}"""

        prompt = f"""أنشئ منشور {content_type} احترافي عن "{topic}" لمنصة {platform} في مجال {user_niche}.

        المطلوب:
        1. نص المنشور الأساسي
        2. هاشتاجات مُحسنة ({spec['hashtag_limit']} حتى)
        3. أفضل وقت نشر
        4. نصائح لزيادة التفاعل
        5. اقتراح نوع الصورة/الفيديو المناسب

        اجعل المحتوى جاهز للنسخ والنشر فوراً!"""

        content = self.call_perplexity_api(prompt, system_prompt)

        # إضافة معلومات إضافية للمنشور
        post_data = {
            'platform': platform,
            'content_type': content_type,
            'topic': topic,
            'niche': user_niche,
            'content': content,
            'specs': spec,
            'created_at': datetime.now().isoformat(),
            'ready_to_post': True
        }

        return post_data

    def create_weekly_content_pack(self, user_niche="تطوير الذات", user_goals="زيادة التفاعل"):
        """إنشاء حزمة محتوى أسبوعية جاهزة للنشر"""

        weekly_plan = {
            'الأحد': {'platform': 'facebook', 'type': 'motivational', 'topic': 'بداية قوية للأسبوع'},
            'الاثنين': {'platform': 'instagram', 'type': 'educational', 'topic': 'نصيحة مفيدة'},
            'الثلاثاء': {'platform': 'tiktok', 'type': 'entertaining', 'topic': 'محتوى خفيف ومرح'},
            'الأربعاء': {'platform': 'youtube', 'type': 'educational', 'topic': 'شرح مفصل'},
            'الخميس': {'platform': 'instagram', 'type': 'behind_scenes', 'topic': 'خلف الكواليس'},
            'الجمعة': {'platform': 'facebook', 'type': 'community', 'topic': 'تفاعل مع المجتمع'},
            'السبت': {'platform': 'tiktok', 'type': 'trending', 'topic': 'ترند أو تحدي'}
        }

        weekly_content = {}

        print("🗓️ إنشاء حزمة محتوى أسبوعية...")

        for day, plan in weekly_plan.items():
            print(f"📝 {day}: {plan['platform']} - {plan['type']}")

            post_data = self.generate_platform_ready_post(
                platform=plan['platform'],
                content_type=plan['type'],
                topic=plan['topic'],
                user_niche=user_niche
            )

            weekly_content[day] = post_data
            time.sleep(1)  # راحة قصيرة

        return weekly_content

    def create_publishing_dashboard(self, weekly_content):
        """إنشاء لوحة نشر تفاعلية"""

        # تحويل المحتوى إلى JSON للاستخدام في الـ dashboard
        content_json = json.dumps(weekly_content, ensure_ascii=False, indent=2)

        dashboard_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 لوحة النشر الذكي - جاهز للنسخ والنشر</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            color: #4f46e5;
            font-size: 2.5rem;
            margin-bottom: 15px;
        }}

        .posts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
        }}

        .post-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}

        .post-card:hover {{
            transform: translateY(-5px);
        }}

        .platform-header {{
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #e5e7eb;
        }}

        .platform-icon {{
            font-size: 2rem;
            margin-left: 15px;
        }}

        .platform-name {{
            font-size: 1.3rem;
            font-weight: bold;
            color: #1e293b;
        }}

        .post-content {{
            background: #f8fafc;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 1px solid #e2e8f0;
            line-height: 1.6;
            white-space: pre-wrap;
        }}

        .post-meta {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 15px;
            font-size: 0.9rem;
            color: #64748b;
        }}

        .copy-button {{
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease;
            width: 100%;
            font-size: 1rem;
        }}

        .copy-button:hover {{
            transform: translateY(-2px);
        }}

        .copy-button:active {{
            background: #22c55e;
        }}

        .success-message {{
            background: #22c55e;
            color: white;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-top: 10px;
            display: none;
        }}

        .tips-section {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }}

        .tips-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        .tip-item {{
            background: #f1f5f9;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #4f46e5;
        }}

        @media (max-width: 768px) {{
            .posts-grid {{
                grid-template-columns: 1fr;
            }}
            .header h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 لوحة النشر الذكي</h1>
            <p>محتوى جاهز للنسخ والنشر على جميع منصات التواصل الاجتماعي</p>
            <div style="background: #22c55e; color: white; padding: 10px 20px; border-radius: 25px; display: inline-block; margin-top: 15px;">
                ✅ تم توليد 7 منشورات احترافية
            </div>
        </div>

        <div class="posts-grid" id="postsGrid">
        </div>

        <div class="tips-section">
            <h2 style="color: #4f46e5; margin-bottom: 20px;">💡 نصائح للنشر الناجح</h2>
            <div class="tips-grid">
                <div class="tip-item">
                    <h4>⏰ التوقيت المثالي</h4>
                    <p>انشر في الأوقات المذكورة مع كل منشور للحصول على أقصى تفاعل</p>
                </div>
                <div class="tip-item">
                    <h4>📸 الصور والفيديوهات</h4>
                    <p>استخدم صور عالية الجودة أو فيديوهات قصيرة لزيادة التفاعل</p>
                </div>
                <div class="tip-item">
                    <h4>💬 التفاعل السريع</h4>
                    <p>رد على التعليقات خلال أول ساعة من النشر</p>
                </div>
                <div class="tip-item">
                    <h4>📊 تتبع الأداء</h4>
                    <p>راقب إحصائيات كل منشور لتحسين المحتوى القادم</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        const weeklyContent = {content_json};

        const platformIcons = {{
            'facebook': '📘',
            'instagram': '📸', 
            'tiktok': '🎵',
            'youtube': '📺'
        }};

        const platformNames = {{
            'facebook': 'فيسبوك',
            'instagram': 'إنستغرام',
            'tiktok': 'تيك توك', 
            'youtube': 'يوتيوب'
        }};

        const contentTypes = {{
            'motivational': 'تحفيزي',
            'educational': 'تعليمي',
            'entertaining': 'ترفيهي',
            'behind_scenes': 'خلف الكواليس',
            'community': 'مجتمعي',
            'trending': 'رائج'
        }};

        function renderPosts() {{
            const grid = document.getElementById('postsGrid');

            Object.entries(weeklyContent).forEach(([day, post]) => {{
                const card = document.createElement('div');
                card.className = 'post-card';
                card.innerHTML = `
                    <div class="platform-header">
                        <span class="platform-icon">${{platformIcons[post.platform]}}</span>
                        <div>
                            <div class="platform-name">${{platformNames[post.platform]}}</div>
                            <div style="color: #64748b; font-size: 0.9rem;">${{day}} - ${{contentTypes[post.content_type]}}</div>
                        </div>
                    </div>

                    <div class="post-content" id="content-${{day}}">${{post.content}}</div>

                    <div class="post-meta">
                        <div><strong>أفضل وقت:</strong> ${{post.specs.best_times.join(', ')}}</div>
                        <div><strong>الهاشتاجات:</strong> حتى ${{post.specs.hashtag_limit}}</div>
                    </div>

                    <button class="copy-button" onclick="copyContent('${{day}}')">
                        📋 نسخ المنشور
                    </button>

                    <div class="success-message" id="success-${{day}}">
                        ✅ تم النسخ بنجاح! جاهز للنشر
                    </div>
                `;

                grid.appendChild(card);
            }});
        }}

        function copyContent(day) {{
            const content = document.getElementById(`content-${{day}}`).textContent;

            navigator.clipboard.writeText(content).then(() => {{
                const button = event.target;
                const successMsg = document.getElementById(`success-${{day}}`);

                button.style.background = '#22c55e';
                button.textContent = '✅ تم النسخ!';
                successMsg.style.display = 'block';

                setTimeout(() => {{
                    button.style.background = '';
                    button.innerHTML = '📋 نسخ المنشور';
                    successMsg.style.display = 'none';
                }}, 2000);
            }});
        }}

        // تشغيل التطبيق
        renderPosts();

        console.log('🎉 لوحة النشر الذكي جاهزة!');
        console.log('📱 المحتوى جاهز للنسخ والنشر على جميع المنصات');
    </script>
</body>
</html>"""

        with open('./smart_publisher/ready_posts/publishing_dashboard.html', 'w', encoding='utf-8') as f:
            f.write(dashboard_html)

        print("🌐 تم إنشاء لوحة النشر التفاعلية!")
        return './smart_publisher/ready_posts/publishing_dashboard.html'

    def run_smart_publisher(self, user_niche="تطوير الذات"):
        """تشغيل النظام الذكي لتوليد المحتوى الجاهز"""

        print("🚀 بدء النظام الذكي لتوليد المحتوى...")
        print(f"🎯 المجال: {user_niche}")
        print("-" * 50)

        try:
            # إنشاء محتوى أسبوعي جاهز
            weekly_content = self.create_weekly_content_pack(user_niche)

            # حفظ المحتوى كملف JSON
            with open('./smart_publisher/ready_posts/weekly_content.json', 'w', encoding='utf-8') as f:
                json.dump(weekly_content, f, ensure_ascii=False, indent=2)

            # إنشاء لوحة النشر التفاعلية
            dashboard_path = self.create_publishing_dashboard(weekly_content)

            # إنشاء ملف نصي بالمحتوى للمراجعة السريعة
            text_summary = "📋 ملخص المحتوى الأسبوعي الجاهز للنشر\n\n"
            for day, post in weekly_content.items():
                text_summary += f"📅 {day} - {post['platform']} ({post['content_type']}):\n"
                text_summary += f"{post['content'][:100]}...\n\n"

            with open('./smart_publisher/ready_posts/content_summary.txt', 'w', encoding='utf-8') as f:
                f.write(text_summary)

            print("\n✅ تم إنشاء النظام بنجاح!")
            print("🌐 لوحة النشر: ./smart_publisher/ready_posts/publishing_dashboard.html")
            print("📁 ملفات المحتوى: ./smart_publisher/ready_posts/")
            print("📋 ملخص نصي: ./smart_publisher/ready_posts/content_summary.txt")
            print("\n🎯 كيفية الاستخدام:")
            print("1. افتح لوحة النشر في المتصفح")
            print("2. انسخ المحتوى بضغطة واحدة") 
            print("3. الصق في المنصة المناسبة")
            print("4. انشر في الوقت المحدد")
            print("\n💡 النظام جاهز للاستخدام!")

            return True

        except Exception as e:
            print(f"❌ خطأ: {e}")
            return False

def main():
    """الدالة الرئيسية"""
    try:
        print("🌟 نظام النشر الذكي الهجين")
        print("💡 الحل الأمثل للنشر على جميع المنصات")
        print("🎯 يولد محتوى جاهز للنسخ واللصق")
        print("="*60)

        # إنشاء الناشر الذكي
        publisher = SmartSocialPublisher()

        # تشغيل النظام
        success = publisher.run_smart_publisher("تطوير الذات وريادة الأعمال")

        if success:
            print("\n🎉 النظام جاهز للاستخدام!")
            print("🚀 ابدأ النشر وحقق النتائج المذهلة!")

        return success

    except Exception as e:
        print(f"❌ خطأ في النظام: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
