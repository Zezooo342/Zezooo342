#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧠 Smart Viral Video Harvester
يجلب أعلى 5 فيديوهات مشاهدة في المجال المحدد عبر Perplexity Pro API
ثم يحمّلها عبر requests فقط، ويخزنها مهيكلة حسب المنصة.
"""

import os
import re
import sys
import requests
from datetime import datetime
from typing import List, Dict

# تأكد من طباعة UTF-8
sys.stdout.reconfigure(encoding='utf-8')

API_URL = "https://api.perplexity.ai/chat/completions"
MODEL   = "llama-3.1-sonar-large-128k-online"

def get_api_key() -> str:
    key = os.getenv("PERPLEXITY_API_KEY", "").strip()
    if not key:
        raise RuntimeError("🔑 لم يتم ضبط متغير PERPLEXITY_API_KEY")
    return key

def fetch_top_videos(platform: str, niche: str, api_key: str) -> List[Dict]:
    """
    يطلب من Perplexity Pro API قائمة بأعلى 5 فيديوهات مشاهدة في المجال على المنصة.
    يعيد قائمة dict: {'url':..., 'title':...}
    """
    prompt = (
        f"أنت خبير محتوى. أعطني قائمة أعلى 5 فيديوهات مشاهدة على {platform} "
        f"in مجال {niche} خلال الشهر الماضي. لكل فيديو، أعطني الرابط المباشر واسم الفيديو."
    )
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"model": MODEL, "messages":[{"role":"user","content":prompt}]}
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=20)
    resp.raise_for_status()
    text = resp.json()["choices"][0]["message"]["content"]
    # استخراج أزواج URL وعنوان
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    videos = []
    for line in lines:
        m = re.match(r"(https?://\S+\.mp4)\s*-\s*(.+)$", line)
        if m:
            videos.append({"url": m.group(1), "title": m.group(2)})
        if len(videos) >= 5:
            break
    return videos

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
    api_key   = get_api_key()
    niche     = os.getenv("NICHE", "تطوير الذات").strip()
    plats     = [p.strip() for p in os.getenv("TARGET_PLATFORMS","tiktok,youtube,instagram,facebook").split(",")]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir  = f"smart_harvest_{timestamp}"
    os.makedirs(base_dir, exist_ok=True)

    total = {"found":0, "downloaded":0}
    for plat in plats:
        print(f"\n🔍 Fetching top videos from {plat} in '{niche}'...")
        try:
            vids = fetch_top_videos(plat, niche, api_key)
        except Exception as e:
            print(f"❌ API error on {plat}: {e}")
            continue
        print(f"✅ Found {len(vids)} videos.")
        total["found"] += len(vids)
        dest = os.path.join(base_dir, plat)
        for v in vids:
            url, title = v["url"], v["title"]
            print(f"⬇️ Downloading: {title} ({url})")
            try:
                path = download_video(url, dest)
                print(f"   ✅ Saved: {path}")
                total["downloaded"] += 1
            except Exception as e:
                print(f"   ❌ Download failed: {e}")

    print("\n================================")
    print(f"📊 Total found = {total['found']}, downloaded = {total['downloaded']}")
    print(f"📂 Output folder: {base_dir}")

if __name__ == "__main__":
    main()
