import os
import subprocess
from pathlib import Path
import re

# Set the paths for yt-dlp.exe and ffmpeg
YTDLP_PATH = r"C:\Users\utkar\OneDrive\Desktop\YT\Script test\yt-dlp.exe"  # Update this with the actual path
FFMPEG_PATH = "ffmpeg.exe"  # Update this with the actual path

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video(video_url, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    command = [
        YTDLP_PATH,
        video_url,
        "-o", f"{output_folder}/%(title)s.%(ext)s"
    ]
    subprocess.run(command, check=True)

def extract_clip(video_path, start_time, end_time, clip_name, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, f"{clip_name}.mkv")
    
    command = [
        FFMPEG_PATH,
        "-i", video_path,
        "-ss", start_time,
        "-to", end_time,
        "-c", "copy",
        output_path
    ]
    subprocess.run(command, check=True)

def main():
    video_url = input("Enter the YouTube video URL: ")
    start_time = input("Enter the start time of the clip (hh:mm:ss): ")
    end_time = input("Enter the end time of the clip (hh:mm:ss): ")
    clip_name = input("Enter the name for the clip: ")
    
    clip_name = sanitize_filename(clip_name)
    
    video_folder = Path(os.getcwd()) / "downloads"
    clips_folder = video_folder / "clips"
    
    print("Downloading video...")
    download_video(video_url, video_folder)
    
    video_file = next(video_folder.glob("*.mkv"))
    
    print("Extracting clip...")
    extract_clip(video_file, start_time, end_time, clip_name, clips_folder)
    
    print(f"Done! Clip '{clip_name}' has been extracted and saved in the clips folder.")

if __name__ == "__main__":
    main()
