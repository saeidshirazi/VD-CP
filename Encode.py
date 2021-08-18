import os
import subprocess

directory = input("please enter your video directory: ")

for subdirs, dirs, files in os.walk(directory):
    for file in files:
        extention = os.path.splitext(file)[-1].lower()
        if extention == ".mov":
            if not os.path.exists(subdirs + "/compressed"):
                os.makedirs(subdirs +"/compressed")
            media_input=subdirs+ "/"+ file
            media_output = subdirs +"/compressed/"+ file
            subprocess.run("ffmpeg -i "+ media_input.replace(" ","\\ ") + " -vcodec libx264 -crf 22 "+ media_output.replace(" ","\\ "), shell=True)
        elif extention == ".mp4":
            if not os.path.exists(subdirs + "/compressed"):
                os.makedirs(subdirs +"/compressed")
            media_input=subdirs+ "/"+ file
            media_output = subdirs +"/compressed/"+ file
            command = "ffmpeg -i "+ media_input.replace(" ","\\ ") + " -vcodec libx264 -crf 22 "+ media_output.replace(" ","\\ ")
            print()
            subprocess.run("ffmpeg -i "+ media_input.replace(" ","\\ ") + " -vcodec libx264 -crf 22 "+ media_output.replace(" ","\\ "), shell=True)