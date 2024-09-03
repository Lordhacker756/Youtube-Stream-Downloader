import os
import subprocess
import pandas as pd
import sys
from pathlib import Path
import re

# Set the paths for yt-dlp.exe and ffmpeg
YTDLP_PATH = r"C:\Users\utkar\OneDrive\Desktop\YT\Script test\yt-dlp.exe"  # Update this with the actual path
FFMPEG_PATH = "ffmpeg.exe"  # Update this with the actual path

def sanitize_filename(filename):
    # Replace or remove problematic characters
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video(video_url, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Download the video using yt-dlp.exe
    command = [
        YTDLP_PATH,
        video_url,
        "-o", f"{output_folder}/%(title)s.%(ext)s"
    ]
    subprocess.run(command, check=True)

def extract_clips(video_path, clips_info, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    print("Using video file: ", video_path)
    
    for _, row in clips_info.iterrows():
        start_time = row['start_time']
        end_time = row['end_time']
        clip_name = sanitize_filename(row['clip_name'])
        
        output_path = os.path.join(output_folder, f"{clip_name}.mkv")
        
        # Extract the clip using ffmpeg
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
    # Get the video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Download the video
    print("Downloading video...")
    video_folder = Path(os.getcwd()) / "downloads"
    # download_video(video_url, video_folder)
    
    # Get the downloaded video file
    video_file = next(video_folder.glob("*.mkv"))
    
    # Read the CSV file
    clips_info = pd.read_csv(r"C:\Users\utkar\OneDrive\Desktop\YT\Script test\timestamps.csv")
    
    # Create the clips folder
    clips_folder = video_folder / "clips"
    
    # Extract clips
    print("Extracting clips...")
    extract_clips(video_file, clips_info, clips_folder)
    
    print("Done! All clips have been extracted.")

if __name__ == "__main__":
    main()
