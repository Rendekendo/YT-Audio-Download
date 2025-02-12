import subprocess
import os

url = input("Please enter the YouTube URL: ")

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

command = f'yt-dlp -x --audio-format mp3 --embed-thumbnail --add-metadata -o "{desktop_path}\%(title)s.%(ext)s" {url}'

subprocess.run(command, shell=True)