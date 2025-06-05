"""
Warning
if you get the below while running the script

[ WARN:0@7.813] global cap_ffmpeg_impl.hpp:1595 grabFrame packet read max attempts exceeded, if your video have multiple streams (video, audio) try to increase attempt limit by setting environment variable OPENCV_FFMPEG_READ_ATTEMPTS (current value is 4096)
Extracted 81 frames to 'test'

is because the file contains multiple streams.

FIX
For Linux run: export OPENCV_FFMPEG_READ_ATTEMPTS=10000
For Windows run: set OPENCV_FFMPEG_READ_ATTEMPTS=10000

If the above does not work, then re-encoding to a clean frame via ffmpeg:

ffmpeg -i YOUR-ORIGINAL-FILE.mp4 -an -c:v libx264 -preset fast -crf 23 -r 30 cleaned-frame.mp4

run again the script and give as a file the cleaned-frame.mp4
"""

import os
try:
    import cv2
except ImportError as e:
    print(f"Missing module: {e.name}. Please install it using: pip install opencv-python")
    exit()

video_full_name = input("Enter the name of the video, e.g: video.mp4: ")

if os.path.exists(video_full_name):
    print("Video exists")

    video_name, ext = os.path.splitext(video_full_name)

    if not os.path.exists(video_name):
        os.makedirs(video_name, exist_ok=True)
    else:
        print("Export directory already exists")

    cap = cv2.VideoCapture(video_full_name)

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        exit()

    # Extract frames
    frame_number = 0
    while cap.isOpened():
        # ret: is a boolean -> true if frame read, false if it's not
        # frame: the main frame
        ret, frame = cap.read()
        if not ret:
            break

        # :04d is a format specifier that tells Python how to display the value of frame_number:
        # 0: zeros instead of spaces
        # 4: 4 digits
        # d: decimal

        output_path = os.path.join(video_name, f"frame_{frame_number:04d}.png")
        cv2.imwrite(output_path, frame)
        frame_number += 1

    cap.release()
    print(f"Extracted {frame_number} frames to '{video_name}'") 

else:
    print("Error: Video file does not exist.")