#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📥 نظام ذكي لتحميل الفيديوهات عبر Perplexity API فقط – مع تصحيح تهيئة المفتاح
===================================================
يزيل الفراغات والأسطر الفارغة من قيمة API_KEY قبل الاستخدام.
"""

import os
import re
import requests
from datetime import datetime
from typing import List

API_URL = "https://api.perplexity.ai/chat/completions"
MODEL   = "llama-3.1-sonar-large-128k-online"

def get_api_key() -> str:
    key = os.getenv("PERPLEXITY_API_KEY", "")
    key = key.strip()                 # إزالة الفراغات من البداية والنهاية
    key = key.replace("\n", "")       # إزالة جميع الأسطر الفارغة
    if not key:
        raise RuntimeError("🔑 متغير PERPLEXITY_API_KEY غير مضبوط أو فارغ")
    return key

def discover_mp4_links(platform: str, niche: str, api_key: str) -> List[str]:
    prompt = (
        f"أنت محلل فيديو متخصص في {platform} بمجال {niche}. "
        "أعطني قائمة بأفضل 5 روابط مباشرة لملفات فيديو بصيغة .mp4 "
        "عالية الجودة والرائجة خلال الأسبوع الماضي."
    )
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=20)
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    return re.findall(r"https?://[^\s]+?\.mp4", content)

def download_video(url: str, dest_folder: str) -> str:
    os.makedirs(dest_folder, exist_ok=True)
    local_name = os.path.join(dest_folder, url.split("/")[-1])
    with requests.get(url, stream=True, timeout=60) as resp:
        resp.raise_for_status()
        with open(local_name, "wb") as f:
            for chunk in resp.iter_content(1024*1024):
                if chunk:
                    f.write(chunk)
    return local_name

def main():
    api_key   = get_api_key()
    niche     = os.getenv("NICHE", "تطوير الذات").strip()
    platforms = [p.strip() for p in os.getenv("TARGET_PLATFORMS", "tiktok,youtube").split(",")]
    now       = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir  = f"intelligent_harvest_{now}"
    os.makedirs(base_dir, exist_ok=True)

    found = downloaded = 0
    for plat in platforms:
        print(f"🔍 اكتشاف فيديوهات .mp4 من {plat}...")
        try:
            links = discover_mp4_links(plat, niche, api_key)
        except Exception as e:
            print(f"   ❌ خطأ في الاكتشاف: {e}")
            continue
        print(f"  ✅ وجدت {len(links)} رابطاً.")
        found += len(links)
        folder = os.path.join(base_dir, plat)
        for url in links:
            try:
                print(f"⬇️ تحميل: {url}")
                path = download_video(url, folder)
                print(f"   ✅ تم الحفظ: {path}")
                downloaded += 1
            except Exception as e:
                print(f"   ❌ فشل تحميل {url}: {e}")

    print("============================================")
    print(f"📊 المجموع: روابط مكتشفة = {found}, روابط محمّلة = {downloaded}")
    print(f"📁 المجلد النهائي: {base_dir}")

if __name__ == "__main__":
    main()
