import moviepy.editor
from pytube import *
from datetime import *
from moviepy.editor import *
import moviepy.video.fx.all as vfx


def audioSplit(dirVideo, dirAudio):
    video = moviepy.editor.VideoFileClip(dirVideo)
    audio = video.audio
    audio.write_audiofile("{}.mp3".format(dirAudio))


def videoTrim(dirVideo):
    trimStart = int(input("Trim start (sec) > "))
    trimEnd = int(input("Trim end (sec) > "))
    newClip = dirVideo.subclip(trimStart, trimEnd)
    fps = int(input("FPS > "))

    print('''
    Video quality:
    [1] Normal (libx264, compressed)
    [2] High (mpeg4, higher quality)
    [3] Raw video (uncompressed, raw)
    [4] Perfect quality, smaller than raw video in size
    [5] Ogv file - open source
    [6] Webm file        
    ''')
    vidChoice = int(input("Input choice > "))
    result = str(input("Output file name > "))

    if (choice == 3 or choice == 4):
        newClip.write_videofile("{}.avi".format(result), codec=videoQuality(vidChoice), fps=fps)
    elif (choice == 5):
        newClip.write_videofile("{}.ogv".format(result), codec=videoQuality(vidChoice), fps=fps)
    elif (choice == 6):
        newClip.write_videofile("{}.webm".format(result), codec=videoQuality(vidChoice), fps=fps)
    else:
        newClip.write_videofile("{}.mp4".format(result), codec=videoQuality(vidChoice), fps=fps)

    newClip.close()


def videoQuality(vidChoice):
    switcher = {
        1: "libx264",
        2: "mpeg4",
        3: "rawvideo",
        4: "png",
        5: "libvorbis",
        6: "libvpx"
    }
    return switcher.get(vidChoice)


def gifCreate(dirVideo):
    trimStart = int(input("Trim start (sec) > "))
    trimEnd = int(input("Trim end (sec) > "))
    newClip = dirVideo.subclip(trimStart, trimEnd)
    result = input("Output name > ")
    newClip.write_gif("{}.gif".format(result), fps=15)


def ytInfo(yt):
    print("Title: ", yt.title)
    print("Number of views (as of {}):".format(date.today()), yt.views, "views")
    print("Length of video: ", yt.length, "seconds")
    print("Ratings: ", yt.rating)


def ytDownloader(yt):
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download()
    print("Download complete")


def ytVidInfo(yt):
    print(yt.streams.filter(progressive=True))


def boomerang(dirVideo):
    trimStart = int(input("Trim start (sec) > "))
    trimEnd = int(input("Trim end (sec) > "))

    sub = dirVideo.subclip(trimStart, trimEnd)
    clip2 = sub.speedx(final_duration=2)
    clip3 = clip2.fx(vfx.time_mirror)
    final = concatenate_videoclips([clip2, clip3])
    result = input("Output name > ")
    final.to_gif("{}.gif".format(result), fps=15)


print('''
[1] Split audio from video
[2] Trim video
[3] Create a gif
[4] Youtube video information
[5] Download YouTube video
[6] Youtube download resolution info
[7] Boomerang GIF
''')

choice = int(input("Input number > "))

if (choice == 1):
    print("Insert video directory, USE '\\\\' FOR BACKSLASH")
    dirVideo = str(input("Video location > "))
    print()
    dirAudio = str(input("Output name > "))
    audioSplit(dirVideo, dirAudio)
elif (choice == 2):
    print("Insert video directory, USE '\\\\' FOR BACKSLASH")
    dirVideo = VideoFileClip(str(input("Video location > ")))
    videoTrim(dirVideo)
elif (choice == 3):
    print("Insert video directory, USE '\\\\' FOR BACKSLASH")
    dirVideo = VideoFileClip(str(input("Video location > ")))
    gifCreate(dirVideo)
elif (choice == 4):
    link = str(input("Link > "))
    yt = YouTube(link)
    ytInfo(yt)
elif (choice == 5):
    link = str(input("Link > "))
    yt = YouTube(link)
    ytDownloader(yt)
elif (choice == 6):
    link = str(input("Link > "))
    yt = YouTube(link)
    ytVidInfo(yt)
elif (choice == 7):
    print("Insert video directory, USE '\\\\' FOR BACKSLASH")
    dirVideo = VideoFileClip(str(input("Video location > ")))
    boomerang(dirVideo)
