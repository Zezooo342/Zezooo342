#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧠 Smart Video Harvester
اكتشاف وتحميل فيديوهات بصيغة .mp4 عبر Perplexity API فقط، بدون أدوات خارجية.
"""

import os
import re
import sys
import json
import requests
from datetime import datetime
from typing import List

# تأكد من أن stdout يطبع UTF-8
sys.stdout.reconfigure(encoding='utf-8')

API_URL = "https://api.perplexity.ai/chat/completions"
MODEL   = "llama-3.1-sonar-large-128k-online"

def get_api_key() -> str:
    key = os.getenv("PERPLEXITY_API_KEY", "").strip().replace("\n", "")
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
    payload = {"model": MODEL, "messages": [{"role": "user", "content": prompt}]}
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=20)
    resp.raise_for_status()
    text = resp.json()["choices"][0]["message"]["content"]
    return re.findall(r"https?://[^\s]+?\.mp4", text)

def download_video(url: str, dest: str) -> str:
    os.makedirs(dest, exist_ok=True)
    filename = os.path.join(dest, os.path.basename(url))
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(1024*1024):
                if chunk:
                    f.write(chunk)
    return filename

def main():
    api_key = get_api_key()
    niche   = os.getenv("NICHE", "تطوير الذات").strip()
    plats   = [p.strip() for p in os.getenv("TARGET_PLATFORMS", "tiktok,youtube").split(",")]
    now     = datetime.now().strftime("%Y%m%d_%H%M%S")
    base    = f"harvest_{now}"
    os.makedirs(base, exist_ok=True)

    found = downloaded = 0
    for p in plats:
        print(f"🔍 اكتشاف فيديوهات من {p}...")
        try:
            links = discover_mp4_links(p, niche, api_key)
        except Exception as e:
            print(f"❌ فشل الاكتشاف: {e}")
            continue
        print(f"✅ وُجدت {len(links)} روابط.")
        found += len(links)
        for url in links:
            try:
                print(f"⬇️ تحميل {url}...")
                path = download_video(url, os.path.join(base, p))
                print(f"✅ تم الحفظ: {path}")
                downloaded += 1
            except Exception as e:
                print(f"❌ فشل التحميل: {e}")

    print("================================")
    print(f"📊 روابط مكتشفة = {found}, روابط محمّلة = {downloaded}")
    print(f"📂 المجلد: {base}")

if __name__ == "__main__":
    main()
