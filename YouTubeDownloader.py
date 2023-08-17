from pytube import YouTube

link = input('Please insert YT link: ')
yt =  YouTube(link)

print("Title: ", yt.title)

yt.streams.get_highest_resolution().download('C:\Temp')
