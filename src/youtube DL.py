Here's a basic Python script for downloading videos from YouTube using the `youtube-dl` library. This script requires the `youtube-dl` package to be installed before running.

First, you'll need to install `youtube-dl` using pip:

```
pip install youtube-dl
```

Then, create a new Python file (e.g., `youtube_downloader.py`) and add the following code:

```python
import os
import sys
import argparse
from youtube_dl import YoutubeDL

# Define command-line arguments for video URL and output directory
parser = argparse.ArgumentParser(description='Download YouTube videos')
parser.add_argument('url', help='URL of the YouTube video')
parser.add_argument('-o', '--output_dir', help='Output directory for downloaded videos')
args = parser.parse_args()

# Set default output directory to current working directory if not specified
if args.output_dir is None:
    args.output_dir = os.getcwd()
    
# Set up options for `youtube-dl` and download the video
options = {
    'format': 'best',  # Download video in highest available quality
    'outtmpl': os.path.join(args.output_dir, '%(id)s-%(title)s%(ext)s'),  # Set naming convention for downloaded files (ID and title with extension)
    'quiet': True,  # Disable progress bar and status messages during downloading process
    'no_warnings': True,  # Disable warnings during downloading process (e.g., about age restrictions)
}
with YoutubeDL(options) as ydl:
    ydl.download([args.url])  # Download the video using the URL provided by the user
    
# Print success message if download was successful, or error message if there was an issue with the URL or permissions to download the video
if os.path.exists(os.path.join(args.output_dir, f"{os.path.basename(args.url)}")):  # Check if video was successfully downloaded to specified output directory
    print("Video downloaded successfully!") else:  # If video could not be downloaded, print error message and exit script with error code 1 (indicating failure)
        print("Error: Failed to download video.", file=sys.stderr) sys.exit(1) ``` 
This script takes a single required argument, `url`, which is the URL of the YouTube video to be downloaded, and an optional argument, `output_dir`, which specifies the directory where the downloaded video should be saved (the default is the current working directory). The script uses the `argparse` library to parse command-line arguments and set up options for `youtube-dl`. It then sets up options for `youtube-dl`, such as the desired video format and naming convention for downloaded files, and uses a context manager to handle errors during the download process using a `with` statement around the `YoutubeDL` object creation and call to its `download()` method. After downloading the video, it checks whether it was successfully saved in the specified output directory and prints an appropriate success or error message accordingly. Note that this script assumes that you have already installed `youtube-dl` using pip, as described at the beginning of this answer. If you haven't done so yet, you'll need to install it before running this script by executing `pip install youtube-dl`.