from  os import system
from pytube import YouTube
system("cls")
x = 1
while(x):
    link = input("enter the link ")
    ytobj = YouTube(link)
    print(ytobj.title)
    streams = ytobj.streams
    audiostreams = streams.filter(only_audio=True)
    progressive = streams.filter(progressive=True)
    videostreams = streams.filter(only_video= True)
    y = input("press a for audio streams, p form progressive streams and  v for video streams \n")
    if(y == "a"):
        for i in audiostreams:
            print(i)
    elif (y == "p"):
        for i in progressive:
            print(i)
    else:
        for i in videostreams:
            print(i)
    itag = int(input("enter the itag value of the stream from the values listed below "))
    todownload = ytobj.streams.get_by_itag(itag)
    todownload.download()
    x = int(input("press 1 to contiue and 0 to exit \n"))