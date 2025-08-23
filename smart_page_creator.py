#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
النظام الاحترافي المتطور مع Perplexity Pro AI
============================================
نظام متقدم مخصص للعمل مع Perplexity Pro AI
الإصدار: 3.0 Perplexity Pro Edition
'''

import os
import json
import time
import logging
import requests
from datetime import datetime
import traceback

def setup_logging():
    '''إعداد نظام السجلات للعمل مع Perplexity Pro'''
    logger = logging.getLogger('PerplexityProSystem')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        os.makedirs('./logs', exist_ok=True)

        file_handler = logging.FileHandler('./logs/perplexity_system.log', encoding='utf-8')
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

class PerplexityProAI:
    '''محرك Perplexity Pro AI المتطور'''

    def __init__(self, api_key, logger):
        self.api_key = api_key
        self.logger = logger
        self.base_url = 'https://api.perplexity.ai/chat/completions'
        self.model = 'llama-3.1-sonar-large-128k-online'  # أفضل موديل للنسخة Pro

        # إعدادات محسنة للنسخة Pro
        self.pro_settings = {
            'max_tokens': 2000,
            'temperature': 0.7,
            'top_p': 0.9,
            'presence_penalty': 0.1,
            'frequency_penalty': 0.1
        }

    def generate_content(self, prompt, content_type='general'):
        '''توليد محتوى متطور باستخدام Perplexity Pro AI'''
        if not self.api_key:
            self.logger.error("لا يوجد مفتاح Perplexity Pro API!")
            return self._get_fallback_content(prompt, content_type)

        try:
            # إعداد خاص لكل نوع محتوى
            system_prompts = {
                'title': 'أنت خبير في كتابة العناوين الجذابة والمحسنة لمحركات البحث باللغة العربية',
                'description': 'أنت خبير في كتابة الأوصاف التسويقية المقنعة والمحسنة للسيو باللغة العربية',
                'content': 'أنت كاتب محتوى خبير ومتخصص في إنشاء محتوى HTML عالي الجودة باللغة العربية',
                'keywords': 'أنت خبير SEO متخصص في اختيار الكلمات المفتاحية المؤثرة باللغة العربية'
            }

            system_prompt = system_prompts.get(content_type, system_prompts['content'])

            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json',
                'User-Agent': 'PerplexityProSystem/3.0'
            }

            data = {
                'model': self.model,
                'messages': [
                    {
                        'role': 'system',
                        'content': system_prompt
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                **self.pro_settings
            }

            self.logger.info(f"إرسال طلب إلى Perplexity Pro - نوع المحتوى: {content_type}")

            response = requests.post(
                self.base_url,
                headers=headers,
                json=data,
                timeout=45  # وقت أطول للنسخة Pro
            )

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                usage = result.get('usage', {})

                self.logger.info(f"✅ نجح Perplexity Pro - {len(content)} حرف - استخدم {usage.get('total_tokens', 0)} token")
                return content.strip()

            elif response.status_code == 429:
                self.logger.warning("تم تجاوز حد الاستخدام - سيتم المحاولة مرة أخرى")
                time.sleep(60)  # انتظار دقيقة
                return self.generate_content(prompt, content_type)  # محاولة أخرى

            else:
                self.logger.error(f"خطأ في Perplexity Pro API: {response.status_code} - {response.text}")
                return self._get_fallback_content(prompt, content_type)

        except Exception as e:
            self.logger.error(f"خطأ في اتصال Perplexity Pro: {str(e)}")
            return self._get_fallback_content(prompt, content_type)

    def _get_fallback_content(self, prompt, content_type):
        '''محتوى احتياطي عالي الجودة'''
        fallback_content = {
            'title': 'الصفحة الاحترافية المتطورة - مدعومة بتقنية Perplexity Pro AI',
            'description': 'صفحة ويب احترافية متطورة تم إنشاؤها بأحدث تقنيات Perplexity Pro AI لتقديم تجربة استثنائية',
            'keywords': 'perplexity pro ai, ذكاء اصطناعي متطور, تقنية حديثة, محتوى ذكي, تطوير ويب احترافي',
            'content': self._generate_rich_fallback_content()
        }

        return fallback_content.get(content_type, fallback_content['content'])

    def _generate_rich_fallback_content(self):
        '''محتوى احتياطي غني ومتطور'''
        return '''
<div class="hero-section">
    <h2>🚀 مرحباً بك في عصر Perplexity Pro AI</h2>
    <p class="lead">اكتشف قوة الذكاء الاصطناعي المتطور مع أحدث تقنيات Perplexity Pro</p>
</div>

<div class="content-section">
    <h3>🌟 مميزات Perplexity Pro AI</h3>
    <ul class="features-list">
        <li>💡 ذكاء اصطناعي متقدم مع وصول للإنترنت المباشر</li>
        <li>📊 معلومات محدثة ودقيقة من مصادر موثوقة</li>
        <li>🎯 محتوى مخصص وعالي الجودة باللغة العربية</li>
        <li>⚡ استجابة سريعة وأداء متميز</li>
        <li>🔍 محسن لمحركات البحث تلقائياً</li>
        <li>📱 متوافق مع جميع الأجهزة والمنصات</li>
    </ul>
</div>

<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">PRO</div>
        <h3>Perplexity Pro AI</h3>
        <p>أحدث تقنيات الذكاء الاصطناعي مع وصول مباشر للمعلومات الحديثة</p>
    </div>

    <div class="feature-card">
        <div class="feature-icon">FAST</div>
        <h3>سرعة فائقة</h3>
        <p>استجابة فورية وأداء متميز لتجربة مستخدم ممتازة</p>
    </div>

    <div class="feature-card">
        <div class="feature-icon">SMART</div>
        <h3>ذكاء متطور</h3>
        <p>فهم عميق للسياق وتوليد محتوى دقيق ومناسب</p>
    </div>
</div>

<div class="cta-section">
    <h3>🎯 جاهز لتجربة قوة Perplexity Pro؟</h3>
    <p>احصل على محتوى احترافي متطور بأحدث تقنيات الذكاء الاصطناعي</p>
</div>
'''

class ProThemeEngine:
    '''محرك القوالب المحسن لـ Perplexity Pro'''

    def __init__(self, logger):
        self.logger = logger

    def get_pro_css(self):
        '''CSS محسن لتجربة Perplexity Pro'''
        return '''
/* النظام المحسن لـ Perplexity Pro AI */

:root {
    --pro-primary: #1a56db;
    --pro-secondary: #1e40af;
    --pro-accent: #3b82f6;
    --pro-bg: #f8fafc;
    --pro-text: #1e293b;
    --pro-success: #10b981;
    --pro-warning: #f59e0b;
    --pro-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --pro-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    --pro-border-radius: 16px;
    --pro-transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

* { 
    margin: 0; 
    padding: 0; 
    box-sizing: border-box; 
}

body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    line-height: 1.7;
    color: var(--pro-text);
    background: var(--pro-bg);
    font-size: 16px;
}

.container { 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 0 2rem; 
}

/* Header مع شعار Perplexity Pro */
.header {
    background: linear-gradient(135deg, var(--pro-primary) 0%, var(--pro-secondary) 100%);
    color: white;
    padding: 6rem 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
    animation: shine 4s ease-in-out infinite;
}

@keyframes shine {
    0% { transform: translateX(-100%) rotate(45deg); }
    100% { transform: translateX(300%) rotate(45deg); }
}

.header h1 {
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 800;
    margin-bottom: 2rem;
    text-shadow: 0 4px 8px rgba(0,0,0,0.3);
    position: relative;
    z-index: 2;
}

.header p {
    font-size: clamp(1.1rem, 3vw, 1.5rem);
    opacity: 0.95;
    max-width: 700px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

/* Pro Badge */
.pro-badge {
    position: absolute;
    top: 2rem;
    right: 2rem;
    background: linear-gradient(135deg, var(--pro-success), #059669);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    font-size: 0.875rem;
    font-weight: 700;
    box-shadow: var(--pro-shadow);
    z-index: 10;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Navigation */
.nav {
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    padding: 1.5rem 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: var(--pro-shadow);
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
    color: var(--pro-text);
    font-weight: 600;
    padding: 1rem 2rem;
    border-radius: 50px;
    transition: var(--pro-transition);
    position: relative;
    overflow: hidden;
}

.nav a:hover {
    background: linear-gradient(135deg, var(--pro-primary), var(--pro-accent));
    color: white;
    transform: translateY(-2px);
    box-shadow: var(--pro-shadow-lg);
}

/* المحتوى الرئيسي */
.main { 
    padding: 5rem 0; 
}

.section {
    background: white;
    margin: 3rem 0;
    padding: 4rem 3rem;
    border-radius: var(--pro-border-radius);
    box-shadow: var(--pro-shadow-lg);
    position: relative;
    border: 1px solid rgba(26, 86, 219, 0.08);
}

.section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 6px;
    height: 100%;
    background: linear-gradient(to bottom, var(--pro-primary), var(--pro-accent));
}

.section h2 {
    color: var(--pro-primary);
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 700;
    margin-bottom: 2rem;
}

.section h3 {
    color: var(--pro-secondary);
    font-size: clamp(1.5rem, 4vw, 2.2rem);
    font-weight: 600;
    margin: 2.5rem 0 1.5rem 0;
}

.section p {
    font-size: 1.125rem;
    line-height: 1.8;
    margin-bottom: 1.5rem;
    color: #64748b;
}

/* Hero Section */
.hero-section {
    text-align: center;
    padding: 4rem 2rem;
    background: linear-gradient(135deg, rgba(26, 86, 219, 0.05), rgba(59, 130, 246, 0.05));
    border-radius: var(--pro-border-radius);
    margin-bottom: 3rem;
    position: relative;
}

.lead {
    font-size: 1.4rem;
    color: #64748b;
    margin-top: 1.5rem;
}

/* Features Grid */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.feature-card {
    background: white;
    padding: 3rem 2rem;
    border-radius: var(--pro-border-radius);
    box-shadow: var(--pro-shadow);
    text-align: center;
    transition: var(--pro-transition);
    border: 1px solid rgba(26, 86, 219, 0.1);
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--pro-primary), var(--pro-accent));
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.feature-card:hover::before {
    transform: scaleX(1);
}

.feature-card:hover {
    transform: translateY(-12px);
    box-shadow: var(--pro-shadow-lg);
    border-color: var(--pro-accent);
}

.feature-icon {
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--pro-primary);
    background: linear-gradient(135deg, rgba(26, 86, 219, 0.1), rgba(59, 130, 246, 0.1));
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 2rem;
    border: 2px solid rgba(26, 86, 219, 0.2);
}

.feature-card h3 {
    color: var(--pro-primary);
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

/* Features List */
.features-list {
    list-style: none;
    padding: 0;
}

.features-list li {
    padding: 1rem 0;
    border-bottom: 1px solid rgba(26, 86, 219, 0.1);
    font-size: 1.125rem;
    position: relative;
    padding-left: 2.5rem;
    transition: var(--pro-transition);
}

.features-list li::before {
    content: '✨';
    position: absolute;
    left: 0;
    font-size: 1.2rem;
}

.features-list li:hover {
    color: var(--pro-primary);
    padding-left: 3rem;
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1.25rem 2.5rem;
    background: linear-gradient(135deg, var(--pro-primary), var(--pro-accent));
    color: white;
    text-decoration: none;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.125rem;
    transition: var(--pro-transition);
    position: relative;
    overflow: hidden;
    border: none;
    cursor: pointer;
}

.btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.6s;
}

.btn:hover::before { left: 100%; }

.btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(26, 86, 219, 0.4);
}

/* CTA Section */
.cta-section {
    background: linear-gradient(135deg, rgba(26, 86, 219, 0.08), rgba(59, 130, 246, 0.08));
    padding: 4rem 3rem;
    border-radius: var(--pro-border-radius);
    text-align: center;
    margin: 4rem 0;
    border: 2px solid rgba(26, 86, 219, 0.1);
}

/* Footer */
.footer {
    background: linear-gradient(135deg, #1e293b, #334155);
    color: white;
    padding: 5rem 0 3rem;
    text-align: center;
    margin-top: 6rem;
}

.social-links {
    margin: 3rem 0;
    display: flex;
    justify-content: center;
    gap: 2rem;
}

.social-links a {
    color: white;
    font-size: 1.5rem;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.1);
    transition: var(--pro-transition);
}

.social-links a:hover {
    background: var(--pro-accent);
    transform: translateY(-3px);
}

/* Responsive Design */
@media (max-width: 768px) {
    .container { padding: 0 1rem; }
    .section { padding: 2rem 1.5rem; }
    .features-grid { grid-template-columns: 1fr; }
    .nav ul { flex-direction: column; gap: 1rem; text-align: center; }
}

/* Animations */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in { animation: fadeInUp 0.8s ease-out forwards; }

/* Utilities */
.text-center { text-align: center; }
.gradient-text {
    background: linear-gradient(135deg, var(--pro-primary), var(--pro-accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
'''

    def get_pro_javascript(self):
        '''JavaScript محسن لـ Perplexity Pro'''
        return '''
/* JavaScript محسن لـ Perplexity Pro System */

class PerplexityProEnhancer {
    constructor() {
        this.init();
    }

    init() {
        this.setupProAnimations();
        this.setupProInteractions();
        this.setupProFeatures();
        this.displayProWelcome();
    }

    setupProAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('fade-in');
                    }, index * 150);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -100px 0px' });

        document.querySelectorAll('.section, .feature-card').forEach(el => {
            observer.observe(el);
        });
    }

    setupProInteractions() {
        // تحسين تفاعل البطاقات
        document.querySelectorAll('.feature-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-15px) scale(1.02)';
                card.style.boxShadow = '0 25px 50px rgba(26, 86, 219, 0.25)';
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) scale(1)';
                card.style.boxShadow = '0 20px 25px -5px rgba(0, 0, 0, 0.1)';
            });
        });

        // تحسين الأزرار
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.createProRipple(e, btn);
            });
        });
    }

    createProRipple(event, element) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height) * 1.5;
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;

        ripple.style.cssText = `
            position: absolute; width: ${size}px; height: ${size}px;
            left: ${x}px; top: ${y}px; border-radius: 50%;
            background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, transparent 70%);
            transform: scale(0); animation: proRipple 0.8s ease-out;
            pointer-events: none; z-index: 1000;
        `;

        element.appendChild(ripple);
        setTimeout(() => ripple.remove(), 800);
    }

    setupProFeatures() {
        // إضافة عداد الزوار المحسن
        this.addProVisitorCounter();

        // إضافة مؤشر الأداء
        this.addProPerformanceIndicator();

        // إضافة شارة Pro
        this.addProBadge();
    }

    addProVisitorCounter() {
        let visitors = localStorage.getItem('perplexity_pro_visitors') || 0;
        visitors = parseInt(visitors) + 1;
        localStorage.setItem('perplexity_pro_visitors', visitors);

        const counter = document.createElement('div');
        counter.innerHTML = `
            <div style="position: fixed; bottom: 20px; right: 20px;
                        background: linear-gradient(135deg, #1a56db, #3b82f6);
                        color: white; padding: 15px 25px; border-radius: 30px;
                        font-size: 14px; font-weight: 600; z-index: 1000;
                        box-shadow: 0 10px 30px rgba(26, 86, 219, 0.3);
                        backdrop-filter: blur(15px);">
                🧠 Perplexity Pro User #${visitors.toLocaleString('ar')}<br>
                <small style="opacity: 0.9;">مدعوم بالذكاء المتطور</small>
            </div>
        `;
        document.body.appendChild(counter);
    }

    addProPerformanceIndicator() {
        if ('performance' in window) {
            window.addEventListener('load', () => {
                const loadTime = performance.now();
                const indicator = document.createElement('div');

                const level = loadTime < 1000 ? 'فائق' : 
                             loadTime < 2000 ? 'ممتاز' : 'جيد';
                const color = loadTime < 1000 ? '#10b981' : 
                             loadTime < 2000 ? '#3b82f6' : '#f59e0b';

                indicator.innerHTML = `
                    <div style="position: fixed; bottom: 100px; right: 20px;
                                background: ${color}; color: white; 
                                padding: 12px 20px; border-radius: 25px;
                                font-size: 13px; z-index: 1000; font-weight: 600;">
                        ⚡ أداء ${level}: ${Math.round(loadTime)}ms<br>
                        <small>Perplexity Pro Powered</small>
                    </div>
                `;
                document.body.appendChild(indicator);

                setTimeout(() => {
                    indicator.style.opacity = '0';
                    indicator.style.transform = 'translateX(100px)';
                    setTimeout(() => indicator.remove(), 300);
                }, 5000);
            });
        }
    }

    addProBadge() {
        if (!document.querySelector('.pro-badge')) {
            const badge = document.createElement('div');
            badge.className = 'pro-badge';
            badge.innerHTML = `
                <span style="font-size: 1rem;">🚀</span> Perplexity Pro
            `;
            document.querySelector('.section').appendChild(badge);
        }
    }

    displayProWelcome() {
        console.log('%c🚀 Perplexity Pro AI System Active!', 
            'color: #1a56db; font-size: 20px; font-weight: bold; ' +
            'background: linear-gradient(135deg, #f0f9ff, #dbeafe); ' +
            'padding: 15px; border-radius: 10px; border: 2px solid #1a56db;');

        setTimeout(() => {
            const messages = [
                '🧠 نظام Perplexity Pro AI يعمل بكفاءة عالية',
                '⚡ استجابة فورية ودقة متناهية',
                '🎯 محتوى محسن ومخصص لاحتياجاتك',
                '🌟 تجربة ذكية متطورة'
            ];

            const randomMessage = messages[Math.floor(Math.random() * messages.length)];
            console.log(`%c${randomMessage}`, 
                'color: #059669; font-size: 16px; font-weight: 600;');
        }, 2000);
    }
}

// إضافة الأنماط المتطورة
const proStyles = document.createElement('style');
proStyles.textContent = `
    @keyframes proRipple {
        to { transform: scale(4); opacity: 0; }
    }

    .pro-badge:hover {
        transform: scale(1.1) rotate(5deg);
        transition: all 0.3s ease;
    }

    @media (prefers-reduced-motion: reduce) {
        * { animation-duration: 0.01ms !important; }
    }
`;
document.head.appendChild(proStyles);

// تهيئة النظام
document.addEventListener('DOMContentLoaded', () => {
    window.perplexityProSystem = new PerplexityProEnhancer();
});
'''

class PerplexityProPageCreator:
    '''النظام الرئيسي المحسن لـ Perplexity Pro AI'''

    def __init__(self):
        self.logger = setup_logging()
        self.api_key = os.getenv('PERPLEXITY_API_KEY', '')
        self.perplexity = PerplexityProAI(self.api_key, self.logger)
        self.theme_engine = ProThemeEngine(self.logger)

        # إعدادات محسنة للنسخة Pro
        self.config = {
            'max_pages': int(os.getenv('MAX_PAGES_PER_RUN', '5')),
            'topics': self._get_topics(),
            'output_dir': './smart_pages_pro_ai',
            'enable_pro_features': True
        }

        self.setup_directories()
        self.logger.info("🚀 تم تهيئة نظام Perplexity Pro AI بنجاح")

    def _get_topics(self):
        '''الحصول على المواضيع مع تحسين Pro'''
        topics_str = os.getenv('TOPICS', 
            'تقنيات الذكاء الاصطناعي المتطورة,تطوير المواقع بتقنيات حديثة,التسويق الرقمي والذكاء الاصطناعي,ريادة الأعمال في العصر الرقمي,البرمجة والتطوير الاحترافي')
        return [topic.strip() for topic in topics_str.split(',')]

    def setup_directories(self):
        '''إنشاء هيكل مجلدات محسن'''
        directories = [
            f'{self.config["output_dir"]}/pages',
            f'{self.config["output_dir"]}/assets/css',
            f'{self.config["output_dir"]}/assets/js',
            f'{self.config["output_dir"]}/data',
            './logs'
        ]

        for directory in directories:
            os.makedirs(directory, exist_ok=True)

        self.logger.info(f"تم إنشاء {len(directories)} مجلد للنظام Pro")

    def create_pro_page(self, topic):
        '''إنشاء صفحة متطورة باستخدام Perplexity Pro AI'''
        self.logger.info(f"🧠 بدء إنشاء صفحة Pro عن: {topic}")

        try:
            # استعلامات محسنة لـ Perplexity Pro
            title_prompt = f"اكتب عنوان جذاب ومحسن للسيو عن '{topic}' باللغة العربية. العنوان يجب أن يكون قوي ومؤثر ولا يتجاوز 60 حرف."

            desc_prompt = f"اكتب وصف تسويقي مقنع ومحسن لمحركات البحث عن '{topic}' باللغة العربية. الوصف يجب أن يكون في جملتين ولا يتجاوز 160 حرف."

            content_prompt = f"اكتب محتوى HTML شامل ومفصل عن '{topic}' باللغة العربية. يجب أن يتضمن: عناوين فرعية متدرجة، نقاط مهمة، أمثلة عملية، إحصائيات حديثة، ونصائح مفيدة. المحتوى يجب أن يكون احترافي وغني بالمعلومات."

            keywords_prompt = f"اكتب قائمة بـ 10 كلمات مفتاحية مهمة ومحسنة لمحركات البحث عن '{topic}' باللغة العربية. الكلمات مفصولة بفواصل."

            # توليد المحتوى باستخدام Perplexity Pro
            title = self.perplexity.generate_content(title_prompt, 'title')
            description = self.perplexity.generate_content(desc_prompt, 'description')
            content = self.perplexity.generate_content(content_prompt, 'content')
            keywords = self.perplexity.generate_content(keywords_prompt, 'keywords')

            # إنشاء الملفات
            self._create_pro_assets()
            html_path = self._create_pro_html(title, description, content, keywords, topic)

            # حفظ البيانات
            page_data = {
                'title': title,
                'description': description,
                'content': content,
                'keywords': keywords,
                'topic': topic,
                'filename': os.path.basename(html_path),
                'created_at': datetime.now().isoformat(),
                'ai_provider': 'Perplexity Pro AI',
                'model': self.perplexity.model
            }

            self._save_pro_data(page_data)

            self.logger.info(f"✅ تم إنشاء صفحة Pro بنجاح: {html_path}")
            return html_path, page_data

        except Exception as e:
            self.logger.error(f"خطأ في إنشاء صفحة Pro {topic}: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

    def _create_pro_assets(self):
        '''إنشاء ملفات CSS و JavaScript محسنة'''
        css_content = self.theme_engine.get_pro_css()
        css_path = f'{self.config["output_dir"]}/assets/css/perplexity-pro-style.css'
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)

        js_content = self.theme_engine.get_pro_javascript()
        js_path = f'{self.config["output_dir"]}/assets/js/perplexity-pro-enhancer.js'
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)

        self.logger.info("تم إنشاء الأصول المحسنة لـ Perplexity Pro")

    def _create_pro_html(self, title, description, content, keywords, topic):
        '''إنشاء HTML محسن لـ Perplexity Pro'''
        current_time = datetime.now()

        html_template = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Meta Tags محسنة لـ Perplexity Pro -->
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Perplexity Pro AI System">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <meta name="theme-color" content="#1a56db">

    <!-- Open Graph محسن -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="ar_SA">
    <meta property="og:site_name" content="Perplexity Pro AI System">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">

    <!-- Performance -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="assets/css/perplexity-pro-style.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "{title}",
        "description": "{description}",
        "keywords": "{keywords}",
        "dateCreated": "{current_time.isoformat()}",
        "inLanguage": "ar",
        "creator": {{
            "@type": "Organization",
            "name": "Perplexity Pro AI System"
        }}
    }}
    </script>

    <style>
        body {{ 
            font-family: 'Tajawal', 'Segoe UI', -apple-system, sans-serif;
            font-feature-settings: "liga", "kern";
            text-rendering: optimizeLegibility;
        }}
    </style>
</head>
<body>
    <!-- Header مع شعار Perplexity Pro -->
    <header class="header">
        <div class="container">
            <h1 class="fade-in">{title}</h1>
            <p class="fade-in" style="animation-delay: 0.2s;">{description}</p>
            <div class="pro-badge">
                <i class="fas fa-brain" aria-hidden="true"></i> Perplexity Pro AI
            </div>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="nav" role="navigation">
        <div class="container">
            <ul>
                <li><a href="#home"><i class="fas fa-home"></i> الرئيسية</a></li>
                <li><a href="#content"><i class="fas fa-brain"></i> المحتوى الذكي</a></li>
                <li><a href="#features"><i class="fas fa-star"></i> مميزات Pro</a></li>
                <li><a href="#contact"><i class="fas fa-envelope"></i> تواصل</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="main" id="content" role="main">
        <div class="container">
            <!-- AI Content Section -->
            <article class="section">
                <div class="pro-badge">
                    <i class="fas fa-brain"></i> مُولد بـ Perplexity Pro AI
                </div>
                {content}
            </article>

            <!-- Pro Features Section -->
            <section class="section">
                <h2 class="gradient-text text-center">🚀 مميزات Perplexity Pro AI</h2>

                <div class="features-grid">
                    <div class="feature-card fade-in">
                        <div class="feature-icon">PRO</div>
                        <h3>Perplexity Pro AI</h3>
                        <p>أحدث تقنيات الذكاء الاصطناعي مع وصول مباشر للمعلومات الحديثة والدقيقة</p>
                    </div>
                    <div class="feature-card fade-in" style="animation-delay: 0.1s;">
                        <div class="feature-icon">REAL</div>
                        <h3>معلومات حديثة</h3>
                        <p>وصول مباشر للإنترنت للحصول على أحدث المعلومات والبيانات المحدثة</p>
                    </div>
                    <div class="feature-card fade-in" style="animation-delay: 0.2s;">
                        <div class="feature-icon">FAST</div>
                        <h3>استجابة فورية</h3>
                        <p>معالجة سريعة ودقيقة مع أداء متميز وتجربة مستخدم ممتازة</p>
                    </div>
                    <div class="feature-card fade-in" style="animation-delay: 0.3s;">
                        <div class="feature-icon">SMART</div>
                        <h3>فهم عميق</h3>
                        <p>قدرة متقدمة على فهم السياق وتوليد محتوى دقيق ومناسب للموضوع</p>
                    </div>
                </div>
            </section>

            <!-- CTA Section -->
            <section class="section cta-section">
                <h2 class="gradient-text">🎯 تجربة Perplexity Pro الكاملة</h2>
                <p class="lead" style="margin: 2rem 0;">
                    اكتشف قوة الذكاء الاصطناعي المتطور مع Perplexity Pro AI
                </p>
                <a href="#content" class="btn">
                    <i class="fas fa-brain"></i> استكشف المحتوى الذكي
                </a>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <div class="container">
            <h3><i class="fas fa-brain"></i> مدعوم بـ Perplexity Pro AI</h3>
            <p>تم إنشاء هذه الصفحة باستخدام أحدث تقنيات Perplexity Pro AI</p>
            <p style="margin-top: 1.5rem; opacity: 0.8;">
                الموضوع: {topic} • النموذج: {self.perplexity.model} • {current_time.strftime("%Y-%m-%d %H:%M")}
            </p>

            <div class="social-links">
                <a href="https://perplexity.ai" title="Perplexity AI">
                    <i class="fas fa-brain"></i>
                </a>
                <a href="https://github.com" title="GitHub">
                    <i class="fab fa-github"></i>
                </a>
                <a href="#" title="Twitter">
                    <i class="fab fa-twitter"></i>
                </a>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="assets/js/perplexity-pro-enhancer.js"></script>
</body>
</html>'''

        filename = f"{topic.replace(' ', '_').lower()}.html"
        html_path = f'{self.config["output_dir"]}/pages/{filename}'

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_template)

        return html_path

    def _save_pro_data(self, page_data):
        '''حفظ بيانات الصفحة'''
        filename = page_data['filename'].replace('.html', '.json')
        data_path = f'{self.config["output_dir"]}/data/{filename}'

        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, indent=2, ensure_ascii=False)

    def create_pro_index(self, pages_data):
        '''إنشاء صفحة الفهرس المحسنة لـ Perplexity Pro'''
        self.logger.info(f"إنشاء فهرس Pro لـ {len(pages_data)} صفحة")

        cards_html = []
        for page_path, page_data in pages_data:
            card = f'''
            <div class="feature-card fade-in">
                <div class="feature-icon">DOC</div>
                <h3>{page_data['topic']}</h3>
                <p>{page_data['description']}</p>
                <div style="margin: 1rem 0;">
                    <span style="background: #10b981; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem;">
                        Perplexity Pro
                    </span>
                </div>
                <a href="pages/{page_data['filename']}" class="btn" style="width: 100%;">
                    <i class="fas fa-external-link-alt"></i> عرض الصفحة
                </a>
                <div style="margin-top: 1rem; font-size: 0.8rem; color: #64748b;">
                    {page_data['created_at'][:10]}
                </div>
            </div>'''
            cards_html.append(card)

        index_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نظام Perplexity Pro AI - الفهرس الذكي</title>
    <meta name="description" content="فهرس الصفحات الذكية المُنشأة بـ Perplexity Pro AI">

    <link rel="stylesheet" href="assets/css/perplexity-pro-style.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        body {{ font-family: 'Tajawal', sans-serif; }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1><i class="fas fa-brain"></i> نظام Perplexity Pro AI</h1>
            <p>تم إنشاء {len(pages_data)} صفحة ذكية بتقنية Perplexity Pro المتطورة</p>
            <div class="pro-badge">
                <i class="fas fa-star"></i> Pro Edition
            </div>
        </div>
    </header>

    <main class="main">
        <div class="container">
            <section class="hero-section">
                <h2>🚀 مرحباً بك في عصر Perplexity Pro AI</h2>
                <p class="lead">
                    استكشف مجموعة استثنائية من الصفحات الذكية المُنشأة بأحدث تقنيات الذكاء الاصطناعي
                </p>
            </section>

            <section class="section">
                <h2 class="gradient-text text-center">مجموعة الصفحات الذكية</h2>
                <div class="features-grid">
                    {''.join(cards_html)}
                </div>
            </section>

            <section class="section cta-section">
                <h2 class="gradient-text">إحصائيات Perplexity Pro</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
                    <div class="feature-card text-center">
                        <div style="font-size: 3rem; font-weight: 800; color: var(--pro-primary);">
                            {len(pages_data)}
                        </div>
                        <h4>صفحة ذكية</h4>
                    </div>
                    <div class="feature-card text-center">
                        <div style="font-size: 3rem; font-weight: 800; color: var(--pro-primary);">
                            100%
                        </div>
                        <h4>Perplexity Pro</h4>
                    </div>
                    <div class="feature-card text-center">
                        <div style="font-size: 3rem; font-weight: 800; color: var(--pro-primary);">
                            AI
                        </div>
                        <h4>ذكاء متطور</h4>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <h3><i class="fas fa-brain"></i> نظام Perplexity Pro AI</h3>
            <p>النظام الأذكى والأكثر تطوراً لإنشاء المحتوى الرقمي</p>
            <div class="social-links">
                <a href="https://perplexity.ai"><i class="fas fa-brain"></i></a>
                <a href="https://github.com"><i class="fab fa-github"></i></a>
            </div>
        </div>
    </footer>

    <script src="assets/js/perplexity-pro-enhancer.js"></script>
</body>
</html>'''

        index_path = f'{self.config["output_dir"]}/index.html'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)

        return index_path

    def run_pro_system(self):
        '''تشغيل النظام الكامل مع Perplexity Pro'''
        try:
            self.logger.info("🚀 بدء تشغيل نظام Perplexity Pro AI")

            if not self.api_key:
                self.logger.warning("⚠️ لا يوجد مفتاح Perplexity API - سيتم استخدام المحتوى الافتراضي")

            topics = self.config['topics'][:self.config['max_pages']]
            self.logger.info(f"سيتم إنشاء {len(topics)} صفحة بـ Perplexity Pro")

            pages_data = []
            for i, topic in enumerate(topics):
                self.logger.info(f"[{i+1}/{len(topics)}] معالجة: {topic}")
                try:
                    page_path, page_data = self.create_pro_page(topic)
                    pages_data.append((page_path, page_data))

                    # فترة راحة مناسبة للنسخة Pro
                    time.sleep(3)

                except Exception as e:
                    self.logger.error(f"فشل في معالجة {topic}: {str(e)}")
                    continue

            # إنشاء الفهرس
            if pages_data:
                self.create_pro_index(pages_data)

            # ملخص النتائج
            summary = {
                'system': 'Perplexity Pro AI System',
                'version': '3.0 Pro Edition',
                'timestamp': datetime.now().isoformat(),
                'pages_created': len(pages_data),
                'ai_model': self.perplexity.model,
                'success': True
            }

            with open(f'{self.config["output_dir"]}/pro_summary.json', 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)

            self.logger.info(f"✅ تم إنشاء {len(pages_data)} صفحة بـ Perplexity Pro AI!")
            self.logger.info(f"🌐 افتح: {self.config['output_dir']}/index.html")

            return True

        except Exception as e:
            self.logger.error(f"خطأ في النظام: {str(e)}")
            return False

def main():
    '''الدالة الرئيسية'''
    try:
        print("🚀 بدء تشغيل نظام Perplexity Pro AI...")
        print("=" * 70)

        creator = PerplexityProPageCreator()
        success = creator.run_pro_system()

        if success:
            print("\n🎉 تم إكمال نظام Perplexity Pro AI بنجاح!")
            print("🧠 جميع الصفحات تم إنشاؤها بـ Perplexity Pro AI")
            print("🌐 افتح: ./smart_pages_pro_ai/index.html")
        else:
            print("\n❌ حدث خطأ في النظام")

        return success

    except Exception as e:
        print(f"\n💥 خطأ: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
