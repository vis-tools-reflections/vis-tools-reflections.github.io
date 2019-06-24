import subprocess
import glob

for file in glob.glob("videos/*.mp4"):
    output = file.replace(".mp4", ".jpg")

    subprocess.check_call([
        "ffmpeg", "-y", "-i", file, "-vframes", "1",
        "-vf", "scale=640:360",
        "-f", "image2", output
    ])
