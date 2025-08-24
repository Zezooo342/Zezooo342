#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧠 Smart Viral Video Harvester – تصحيح نهائي لمشكلة latin-1
"""

import os
import re
import sys
import requests
from datetime import datetime
from typing import List, Dict

# دعم UTF-8 للإخراج
sys.stdout.reconfigure(encoding='utf-8')

{
  "query": "List top 5 trending tiktok & facebook & instgram videos in comedy niche with direct .mp4 links."
  "model": "llama-3.1-sonar-large-128k-online"
}

def get_api_key() -> str:
    raw = os.getenv("PERPLEXITY_API_KEY", "")
    # قم بإزالة جميع الفراغات والأسطر الفارغة
    key = re.sub(r'\s+', '', raw)
    # اترك فقط ASCII
    key = ''.join(c for c in key if ord(c) < 128)
    if not key:
        raise RuntimeError("🔑 PERPLEXITY_API_KEY غير مضبوط أو غير صالح")
    return key

def fetch_top_videos(platform: str, niche: str, api_key: str):
    prompt = (
        f"List top 5 trending {platform} videos in the {niche} niche "
        "with direct .mp4 download URLs."
    )
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "query": prompt
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    # … بقية المعالجة كما هو  

def download_video(url: str, dest: str, name: str) -> str:
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, name)
    r = requests.get(url, stream=True, timeout=60)
    r.raise_for_status()
    with open(path, "wb") as f:
        for chunk in r.iter_content(1024*1024):
            if chunk:
                f.write(chunk)
    return path

def create_dummy(dest: str, name: str) -> str:
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, name)
    header = b"\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom"
    with open(path, "wb") as f:
        f.write(header)
        f.write(b"\x00" * 100000)
    return path

def main():
    api_key = get_api_key()
    niche = os.getenv("NICHE", "comedy").strip()
    plats = [p.strip() for p in os.getenv("TARGET_PLATFORMS","tiktok,youtube").split(",")]
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"harvest_{now}"
    stats = {"found":0,"dl":0,"dummy":0}

    for p in plats:
        print(f"🔍 {p} | niche={niche}")
        try:
            vids = fetch_top_videos(p, niche, api_key)
        except Exception as e:
            print(f"❌ API error: {e}")
            vids = []
        stats["found"] += len(vids)
        dest = os.path.join(base,p)
        if vids:
            for i,v in enumerate(vids,1):
                name=f"{p}_{i}.mp4"
                try:
                    print(f"⬇️ {v['url']}")
                    path=download_video(v["url"],dest,name)
                    print(f"✅ {path}")
                    stats["dl"]+=1
                except:
                    path=create_dummy(dest,name)
                    print(f"📝 dummy {path}")
                    stats["dummy"]+=1
        else:
            for i in range(2):
                name=f"{p}_dummy_{i+1}.mp4"
                path=create_dummy(dest,name)
                print(f"📝 {path}")
                stats["dummy"]+=1

    print("================================")
    print(f"🔍 found={stats['found']}  ⬇️ downloaded={stats['dl']}  📝 dummy={stats['dummy']}")
    print(f"📂 {base}")

if __name__=="__main__":
    main()
