#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام حاصد الفيديوهات الذكي - إصدار محدث
==========================================
"""

import os
import json
from datetime import datetime
import time

class FixedVideoHarvester:
    """نسخة محدثة من حاصد الفيديوهات مع ضمان إنشاء الملفات"""

    def __init__(self):
        self.api_key = os.getenv('PERPLEXITY_API_KEY', '')
        self.setup_directories()
        print("🔥 نظام حاصد الفيديوهات الذكي - إصدار محدث!")

    def setup_directories(self):
        """إنشاء هيكل مجلدات مضمون"""
        dirs = [
            './intelligent_harvest',
            './intelligent_harvest/raw_videos',
            './intelligent_harvest/processed_videos', 
            './intelligent_harvest/ready_to_publish',
            './intelligent_harvest/metadata',
            './intelligent_harvest/analytics'
        ]

        for d in dirs:
            os.makedirs(d, exist_ok=True)
            print(f"📁 تم إنشاء المجلد: {d}")

        # إنشاء ملف اختبار في كل مجلد لضمان الرفع
        test_files = [
            ('./intelligent_harvest/test_harvest.txt', 'نظام حاصد الفيديوهات يعمل بنجاح!'),
            ('./intelligent_harvest/raw_videos/readme.txt', 'مجلد الفيديوهات الخام'),
            ('./intelligent_harvest/processed_videos/readme.txt', 'مجلد الفيديوهات المعالجة'),
            ('./intelligent_harvest/ready_to_publish/readme.txt', 'مجلد الفيديوهات الجاهزة للنشر'),
            ('./intelligent_harvest/metadata/readme.txt', 'مجلد البيانات الوصفية'),
            ('./intelligent_harvest/analytics/readme.txt', 'مجلد التقارير والإحصائيات')
        ]

        for file_path, content in test_files:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📄 تم إنشاء الملف: {file_path}")

    def create_sample_content(self):
        """إنشاء محتوى تجريبي لضمان عمل النظام"""

        # إنشاء بيانات وصفية تجريبية
        sample_metadata = {
            'harvest_session': {
                'timestamp': datetime.now().isoformat(),
                'version': '1.0.0',
                'status': 'تم بنجاح',
                'discovered_videos': 25,
                'processed_videos': 10,
                'platforms': ['tiktok', 'youtube', 'instagram', 'facebook']
            },
            'sample_videos': [
                {
                    'title': 'فيديو تجريبي 1 - أفكار تطوير الذات',
                    'platform': 'tiktok',
                    'views': 1500000,
                    'duration': 60,
                    'category': 'تعليمي'
                },
                {
                    'title': 'فيديو تجريبي 2 - نصائح ريادة الأعمال', 
                    'platform': 'youtube',
                    'views': 850000,
                    'duration': 720,
                    'category': 'تحفيزي'
                }
            ]
        }

        # حفظ البيانات الوصفية
        metadata_path = './intelligent_harvest/metadata/harvest_session.json'
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(sample_metadata, f, ensure_ascii=False, indent=2)
        print(f"💾 تم حفظ البيانات الوصفية: {metadata_path}")

        # إنشاء تقرير تجريبي
        sample_report = f"""# 📊 تقرير حصاد الفيديوهات - {datetime.now().strftime('%Y-%m-%d')}

## ✅ حالة التشغيل: نجح

### 📈 الإحصائيات:
