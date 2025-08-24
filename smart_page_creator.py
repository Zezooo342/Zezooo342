#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧠 Smart Viral Video Harvester - الإصدار النهائي المضمون
يعالج مشاكل التشفير في GitHub Secrets ويضمن عمل API صحيح.
"""

import os
import re
import sys
import requests
from datetime import datetime
from typing import List, Dict

# ضبط UTF-8 للإخراج
sys.stdout.reconfigure(encoding='utf-8')

API_URL = "https://api.perplexity.ai/chat/completions"
MODEL   = "llama-3.1-sonar-large-128k-online"

def clean_api_key() -> str:
    """
    ينظف المفتاح من الأسطر الفارغة والمسافات والأحرف غير المرغوبة
    """
    key = os.getenv("PERPLEXITY_API_KEY", "")
    # إزالة جميع المسافات والأسطر الفارغة والتابات
    key = re.sub(r'[\n\r\t\s]+', '', key.strip())
    if not key:
        raise RuntimeError("🔑 PERPLEXITY_API_KEY غير مضبوط أو فارغ")
    return key

def fetch_top_videos(platform: str, niche: str, api_key: str) -> List[Dict]:
    """
    يجلب أعلى 5 فيديوهات من Perplexity API
    """
    prompt = f"Find top 5 trending {platform} videos in {niche} niche with direct .mp4 download links"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        
        # استخراج روابط MP4
        urls = re.findall(r'https?://[^\s<>"]+\.mp4', content)
        return [{"url": url, "title": f"video_{i+1}"} for i, url in enumerate(urls[:5])]
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request Error: {e}")
        return []

def download_video(url: str, dest_folder: str, filename: str) -> str:
    """
    يحمل الفيديو مع تجربة عدة مرات عند الفشل
    """
    os.makedirs(dest_folder, exist_ok=True)
    filepath = os.path.join(dest_folder, filename)
    
    for attempt in range(3):
        try:
            resp = requests.get(url, stream=True, timeout=60)
            resp.raise_for_status()
            
            with open(filepath, "wb") as f:
                for chunk in resp.iter_content(1024*1024):
                    if chunk:
                        f.write(chunk)
            return filepath
            
        except Exception as e:
            print(f"   ⚠️ محاولة {attempt+1} فشلت: {e}")
            if attempt == 2:
                raise

def create_sample_video(dest_folder: str, filename: str) -> str:
    """
    ينشئ ملف MP4 تجريبي كبديل عند فشل التحميل
    """
    os.makedirs(dest_folder, exist_ok=True)
    filepath = os.path.join(dest_folder, filename)
    
    # بنية MP4 أساسية
    mp4_header = b"\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom"
    with open(filepath, "wb") as f:
        f.write(mp4_header)
        f.write(b"\x00" * (100 * 1024))  # 100KB
    return filepath

def main():
    try:
        api_key = clean_api_key()
        print(f"✅ تم تنظيف API Key بنجاح")
    except Exception as e:
        print(f"❌ خطأ في API Key: {e}")
        return

    niche = os.getenv("NICHE", "comedy").strip()
    platforms = [p.strip() for p in os.getenv("TARGET_PLATFORMS", "tiktok,youtube").split(",")]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"smart_harvest_{timestamp}"
    
    stats = {"found": 0, "downloaded": 0, "created": 0}
    
    for platform in platforms:
        print(f"\n🔍 البحث في {platform} عن {niche}...")
        
        # جلب الفيديوهات من API
        videos = fetch_top_videos(platform, niche, api_key)
        stats["found"] += len(videos)
        
        dest_folder = os.path.join(base_dir, platform)
        
        if videos:
            print(f"✅ وُجدت {len(videos)} فيديو")
            for i, video in enumerate(videos):
                filename = f"{platform}_video_{i+1}.mp4"
                print(f"⬇️ تحميل: {video['title']}")
                
                try:
                    path = download_video(video["url"], dest_folder, filename)
                    print(f"   ✅ تم الحفظ: {path}")
                    stats["downloaded"] += 1
                except:
                    # إنشاء ملف تجريبي عند فشل التحميل
                    path = create_sample_video(dest_folder, filename)
                    print(f"   📝 تم إنشاء ملف تجريبي: {path}")
                    stats["created"] += 1
        else:
            print("❌ لم يتم العثور على فيديوهات، سيتم إنشاء ملفات تجريبية")
            for i in range(2):
                filename = f"{platform}_sample_{i+1}.mp4"
                path = create_sample_video(dest_folder, filename)
                print(f"📝 تم إنشاء: {path}")
                stats["created"] += 1

    print("\n" + "="*50)
    print(f"📊 النتائج النهائية:")
    print(f"   🔍 فيديوهات مكتشفة: {stats['found']}")
    print(f"   ⬇️ فيديوهات محمّلة: {stats['downloaded']}")
    print(f"   📝 فيديوهات تجريبية: {stats['created']}")
    print(f"📂 المجلد: {base_dir}")

if __name__ == "__main__":
    main()
