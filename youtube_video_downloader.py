import yt_dlp

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA: {d['_eta_str']}")
    elif d['status'] == 'finished':
        print("Download complete!")

def download_video(url):
    
    ydl_opts = {
        "format": "best",
        "outtmpl": R"D:\code\resources for code\video or photo install from yt facebook etc/%(title)s.%(ext)s",
        "progress_hooks": [progress_hook]  # Corrected comma placement
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Download failed: {str(e)}")

# Example usage
video_url = input("Enter the video URL: ")
download_video(video_url)