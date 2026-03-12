# convert the videos to mp3
import os
import subprocess
import re

files  = os.listdir("videos")
for file in files:
    print("File: ", file)
    file_name = file.split(".")[0]
    print("File_name :", file_name)
    video_number = re.findall(r'\d+', file_name)[0]
    print("Video_number :", video_number)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{video_number}_{file_name}.mp3"])
                    