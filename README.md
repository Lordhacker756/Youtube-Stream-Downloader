# Video Clip Extractor

This application allows you to download YouTube videos and extract specific clips from them based on timestamps. It consists of two scripts: `multi_clip.py` for extracting multiple clips from a single video, and `single_clip.py` for extracting a single clip from a video.

## Prerequisites

- Python 3.6+
- yt-dlp
- ffmpeg
- pandas

Install the required Python packages:

```
pip install yt-dlp pandas
```

Make sure `ffmpeg` is installed and accessible from your system's PATH.

## Usage

### multi_clip.py

This script downloads a YouTube video and extracts multiple clips based on timestamps provided in a CSV file.

1. Prepare a CSV file named `timestamps.csv` with the following columns:
   - `start_time`: Start time of the clip (format: HH:MM:SS)
   - `end_time`: End time of the clip (format: HH:MM:SS)
   - `clip_name`: Name for the extracted clip

2. Run the script:

```
python multi_clip.py
```

3. When prompted, enter the YouTube video URL.

4. The script will download the video and extract the clips based on the timestamps in the CSV file.

Example:

```
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading video...
Extracting clips...
Done! All clips have been extracted.
```

### single_clip.py

This script extracts a single clip from a local video file based on user-provided start and end times.

1. Run the script:

```
python single_clip.py
```

2. Follow the prompts to enter:
   - The path to the input video file
   - Start time of the clip (format: HH:MM:SS)
   - End time of the clip (format: HH:MM:SS)
   - Output file name for the clip

Example:

```
Enter the path to the input video file: C:\Videos\my_video.mp4
Enter the start time of the clip (HH:MM:SS): 00:01:30
Enter the end time of the clip (HH:MM:SS): 00:02:45
Enter the output file name for the clip: funny_moment
Extracting clip...
Clip extracted successfully: C:\Videos\clips\funny_moment.mp4
```

## Output

- `multi_clip.py` saves the downloaded video in a `downloads` folder and the extracted clips in a `clips` subfolder.
- `single_clip.py` saves the extracted clip in a `clips` folder in the same directory as the input video.

## Notes

- Make sure to update the `YTDLP_PATH` and `FFMPEG_PATH` variables in the scripts with the correct paths to your yt-dlp and ffmpeg executables.
- The scripts use the MKV format for compatibility. You can modify the output format by changing the file extension and ffmpeg parameters if needed.
