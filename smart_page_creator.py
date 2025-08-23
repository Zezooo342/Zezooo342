#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام حاصد الفيديوهات الذكي - النسخة النهائية الجاهزة للعمل
===========================================================
"""

import os
import json
import subprocess
from datetime import datetime
import time
import hashlib
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import requests
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# === إعداد المجلدات ===
def setup_directories():
    folders = [
        'intelligent_harvest',
        'intelligent_harvest/raw_videos',
        'intelligent_harvest/processed_videos',
        'intelligent_harvest/ready_to_publish',
        'intelligent_harvest/metadata',
        'intelligent_harvest/analytics'
    ]
    for f in folders:
        os.makedirs(f, exist_ok=True)

# === استدعاء Perplexity API لاكتشاف الفيديوهات الرائجة ===
def discover_videos(platform, niche, timeframe, api_key):
    system_prompt = f"""أنت محلل فيديوهات رائج على {platform} في مجال {niche}.
أعطني قائمة بأفضل 5 روابط فيديو عالية المشاهدات خلال {timeframe}."""
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': system_prompt}
    ]
    data = {
        'model': 'llama-3.1-sonar-large-128k-online',
        'messages': messages,
        'max_tokens': 1500,
        'temperature': 0.7
    }
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    try:
        resp = requests.post('https://api.perplexity.ai/chat/completions', headers=headers, json=data, timeout=30)
        content = resp.json()['choices'][0]['message']['content']
        urls = [u.strip() for u in content.split() if u.startswith('http')]
        return urls[:5]
    except Exception:
        return []

# === تحميل الفيديو باستخدام yt-dlp ===
def download_video(url):
    hash_id = hashlib.md5(url.encode()).hexdigest()[:8]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': f"intelligent_harvest/raw_videos/%(id)s_{hash_id}_{timestamp}.%(ext)s",
        'writesubtitles': False
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename

# === معالجة الفيديو (علامة مائية ونص مقدمة) ===
def process_video(input_path):
    clip = VideoFileClip(input_path)
    watermark = TextClip("🔥 @YourPage", fontsize=24, color='white', font='Arial-Bold')\
                .set_opacity(0.7).set_position(("right","bottom")).set_duration(clip.duration)
    intro = TextClip("🚀 شاهد حتى النهاية", fontsize=36, color='yellow', font='Arial-Bold')\
            .set_duration(3).set_position("center")
    final = CompositeVideoClip([intro, clip.set_start(3), watermark.set_start(0)])
    base = os.path.basename(input_path).rsplit('.',1)[0]
    output = f"intelligent_harvest/processed_videos/{base}_processed.mp4"
    final.write_videofile(output, codec='libx264', audio_codec='aac', fps=24)
    clip.close(); final.close()
    return output

# === إنشاء نسخ جاهزة للنشر لكل منصة ===
def create_platform_versions(video_path):
    sizes = {
        'tiktok': (720,1280,60),
        'instagram': (720,1280,90),
        'youtube': (1280,720,None),
        'facebook': (720,720,240)
    }
    versions = {}
    base = os.path.basename(video_path).replace('_processed','')
    for p,(w,h,dur) in sizes.items():
        clip = VideoFileClip(video_path)
        sub = clip.subclip(0, min(dur or clip.duration, clip.duration))
        resized = sub.resize((w,h))
        out = f"intelligent_harvest/ready_to_publish/{base}_{p}.mp4"
        resized.write_videofile(out, codec='libx264', audio_codec='aac', fps=24)
        clip.close(); resized.close()
        versions[p] = out
    return versions

# === رفع الملفات إلى Google Drive ===
def upload_to_drive(folder_id, creds_json_b64):
    creds_info = json.loads(base64.b64decode(creds_json_b64).decode())
    creds = service_account.Credentials.from_service_account_info(creds_info, scopes=['https://www.googleapis.com/auth/drive'])
    drive = build('drive','v3',credentials=creds)
    # حذف القديم
    files = drive.files().list(q=f"'{folder_id}' in parents and trashed=false", fields="files(id)").execute().get('files',[])
    for f in files:
        drive.files().delete(fileId=f['id']).execute()
    # رفع الجديد
    for root,_,fs in os.walk("intelligent_harvest/ready_to_publish"):
        for f in fs:
            fp = os.path.join(root,f)
            media = MediaFileUpload(fp, resumable=True)
            drive.files().create(body={'name':f,'parents':[folder_id]}, media_body=media).execute()

# === الرئيسية ===
def main():
    api_key    = os.getenv('PERPLEXITY_API_KEY','')
    folder_id  = os.getenv('GDRIVE_FOLDER_ID','')
    creds_b64  = os.getenv('GDRIVE_CREDENTIALS','')
    niche      = os.getenv('NICHE','تطوير الذات')
    platforms  = os.getenv('TARGET_PLATFORMS','tiktok,youtube').split(',')

    setup_directories()
    all_videos = []

    for p in platforms:
        urls = discover_videos(p, niche, "أسبوعين", api_key)
        for u in urls:
            print(f"[*] {p} → {u}")
            path = download_video(u)
            proc = process_video(path)
            vs = create_platform_versions(proc)
            all_videos.append({'platform':p,'original':path,'processed':proc,'versions':vs})

    if folder_id and creds_b64:
        upload_to_drive(folder_id, creds_b64)

    # حفظ تقرير
    report = {
        'timestamp': datetime.now().isoformat(),
        'niche': niche,
        'harvested': len(all_videos)
    }
    with open('intelligent_harvest/analytics/report.json','w',encoding='utf-8') as f:
        json.dump(report,f,ensure_ascii=False,indent=2)

    print("✅ اكتمال الحصاد والمعالجة والنشر إلى Drive")
    print(json.dumps(report, ensure_ascii=False))

if __name__=="__main__":
    main()
