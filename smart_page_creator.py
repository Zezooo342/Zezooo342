#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📥 نظام ذكي لتحميل الفيديوهات عبر Perplexity API فقط
===================================================
يستخدم Perplexity API لاكتشاف روابط .mp4 مباشرة ثم يحمّلها بواسطة requests بدون أدوات خارجية.
"""

import os
import re
import requests
from datetime import datetime
from typing import List

API_URL = "https://api.perplexity.ai/chat/completions"
MODEL    = "llama-3.1-sonar-large-128k-online"

def discover_mp4_links(platform: str, niche: str) -> List[str]:
    prompt = (
        f"أنت محلل فيديو متخصص في {platform} بمجال {niche}. "
        "أعطني قائمة بأفضل 5 روابط مباشرة لملفات فيديو بصيغة .mp4 "
        "عالية الجودة والرائجة خلال الأسبوع الماضي. "
        "أرجو أن تكون الروابط من مصادر عامة وقابلة للتحميل مباشرة."
    )
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY','')}", "Content-Type": "application/json"},
        json={"model": MODEL, "messages":[{"role":"user","content":prompt}]},
        timeout=20
    )
    content = resp.json()["choices"][0]["message"]["content"]
    # ابحث عن روابط تنتهي بـ .mp4
    return re.findall(r"https?://[^\s]+?\.mp4", content)

def download_video(url: str, dest_folder: str) -> str:
    os.makedirs(dest_folder, exist_ok=True)
    local_name = os.path.join(dest_folder, url.split("/")[-1])
    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()
    with open(local_name, "wb") as f:
        for chunk in resp.iter_content(1024*1024):
            if chunk:
                f.write(chunk)
    return local_name

def main():
    niche     = os.getenv("NICHE", "تطوير الذات")
    platforms = os.getenv("TARGET_PLATFORMS", "tiktok,youtube").split(",")
    now       = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir  = f"intelligent_harvest_{now}"
    os.makedirs(base_dir, exist_ok=True)

    total = {"found":0, "downloaded":0}
    for plat in platforms:
        print(f"🔍 اكتشاف فيديوهات .mp4 من {plat}...")
        links = discover_mp4_links(plat, niche)
        print(f"  ✅ وجدت {len(links)} رابطاً.")
        total["found"] += len(links)
        folder = os.path.join(base_dir, plat)
        for url in links:
            try:
                print(f"⬇️ تحميل: {url}")
                path = download_video(url, folder)
                print(f"   ✅ تم الحفظ: {path}")
                total["downloaded"] += 1
            except Exception as e:
                print(f"   ❌ فشل تحميل {url}: {e}")

    print("============================================")
    print(f"📊 المجموع: روابط مكتشفة = {total['found']}, روابط محمّلة = {total['downloaded']}")
    print(f"📁 المجلد النهائي: {base_dir}")

if __name__ == "__main__":
    main()
